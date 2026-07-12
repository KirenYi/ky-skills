from __future__ import annotations

import html
import re
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser


class _HTMLTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._parts: list[str] = []
        self._skip = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style"}:
            self._skip = True
            return
        if tag in {"br", "p", "div", "li", "tr"}:
            self._parts.append("\n")
        elif tag == "hr":
            self._parts.append("\n---\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"}:
            self._skip = False
            return
        if tag in {"p", "div", "li", "tr"}:
            self._parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self._skip and data:
            self._parts.append(data)

    def text(self) -> str:
        joined = "".join(self._parts)
        joined = html.unescape(joined)
        joined = re.sub(r"[ \t]+\n", "\n", joined)
        joined = re.sub(r"\n{3,}", "\n\n", joined)
        joined = re.sub(r"[ \t]{2,}", " ", joined)
        return joined.strip()


def html_to_text(raw: str) -> str:
    if not raw:
        return ""
    parser = _HTMLTextExtractor()
    try:
        parser.feed(raw)
        parser.close()
        text = parser.text()
        if text:
            return text
    except Exception:
        pass
    # Fallback: crude strip
    text = re.sub(r"<[^>]+>", " ", raw)
    return html.unescape(re.sub(r"\s+", " ", text)).strip()


def parse_rss_date(value: str | None) -> str:
    if not value:
        return ""
    try:
        dt = parsedate_to_datetime(value)
        return dt.isoformat()
    except Exception:
        return value.strip()


def looks_like_retweet(title: str, text: str) -> bool:
    t = (title or "").strip()
    if t.startswith("RT by @") or t.startswith("RT @"):
        return True
    body = (text or "").lstrip()
    return body.startswith("RT @")


def looks_like_reply(title: str, text: str) -> bool:
    t = (title or "").strip()
    # Nitter often uses "R to @user: ..." for replies
    if re.match(r"^R to @\w+", t, flags=re.I):
        return True
    if re.match(r"^Replying to @\w+", t, flags=re.I):
        return True
    body = (text or "").lstrip()
    return bool(re.match(r"^@\w+", body))


def looks_like_quote(text: str) -> bool:
    # Heuristic: nitter quote blocks often leave a horizontal rule / quoted footer
    body = text or ""
    return "\n---\n" in body or "twitter.com/" in body and "status/" in body


def nitter_link_to_x(url: str) -> str:
    if not url:
        return ""
    # https://nitter.net/user/status/123#m -> https://x.com/user/status/123
    m = re.search(r"/(?P<user>[A-Za-z0-9_]+)/status/(?P<id>\d+)", url)
    if m:
        return f"https://x.com/{m.group('user')}/status/{m.group('id')}"
    return url.replace("nitter.net", "x.com")


def extract_status_id(guid: str | None, link: str | None) -> str:
    for candidate in (guid, link):
        if not candidate:
            continue
        m = re.search(r"status/(\d+)", candidate)
        if m:
            return m.group(1)
        # pure numeric guid from nitter
        if re.fullmatch(r"\d+", candidate.strip()):
            return candidate.strip()
    return ""
