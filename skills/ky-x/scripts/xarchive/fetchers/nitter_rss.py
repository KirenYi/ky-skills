from __future__ import annotations

import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

from ..models import AppConfig, Post
from ..textutil import (
    extract_status_id,
    html_to_text,
    looks_like_quote,
    looks_like_reply,
    looks_like_retweet,
    nitter_link_to_x,
    parse_rss_date,
)
from .base import Fetcher


class NitterRssFetcher(Fetcher):
    """Fetch public timelines via Nitter-compatible RSS endpoints (no X API key)."""

    name = "nitter_rss"

    def __init__(self, config: AppConfig) -> None:
        self.config = config
        self._last_ok_instance: str | None = None

    def fetch_user_posts(self, handle: str) -> list[Post]:
        handle = handle.lstrip("@").strip()
        instances = list(self.config.nitter_instances)
        # Prefer last successful instance first.
        if self._last_ok_instance and self._last_ok_instance in instances:
            instances = [self._last_ok_instance] + [
                i for i in instances if i != self._last_ok_instance
            ]

        errors: list[str] = []
        for base in instances:
            url = f"{base.rstrip('/')}/{handle}/rss"
            try:
                posts = self._fetch_url(url, handle=handle)
                self._last_ok_instance = base.rstrip("/")
                return posts
            except Exception as exc:  # noqa: BLE001 - collect and try next
                errors.append(f"{base}: {exc}")
                time.sleep(0.3)

        raise RuntimeError(
            "所有 Nitter 实例均失败。\n" + "\n".join(f"  - {e}" for e in errors)
        )

    def _fetch_url(self, url: str, *, handle: str) -> list[Post]:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": self.config.user_agent,
                "Accept": "application/rss+xml, application/xml, text/xml, */*",
            },
            method="GET",
        )
        try:
            with urllib.request.urlopen(req, timeout=self.config.request_timeout_sec) as resp:
                body = resp.read()
                content_type = (resp.headers.get("Content-Type") or "").lower()
        except urllib.error.HTTPError as e:
            raise RuntimeError(f"HTTP {e.code}") from e
        except urllib.error.URLError as e:
            raise RuntimeError(f"网络错误: {e.reason}") from e

        text = body.decode("utf-8", errors="replace")
        if "<rss" not in text.lower() and "<feed" not in text.lower():
            raise RuntimeError(
                f"返回的不是 RSS（content-type={content_type!r}），可能被验证码拦截"
            )
        if "whitelisted" in text.lower() and "<item>" in text.lower() and "not yet" in text.lower():
            raise RuntimeError("RSS 源要求白名单，跳过该实例")

        return self._parse_rss(text, handle=handle)

    def _parse_rss(self, xml_text: str, *, handle: str) -> list[Post]:
        try:
            root = ET.fromstring(xml_text)
        except ET.ParseError as e:
            raise RuntimeError(f"RSS XML 解析失败: {e}") from e

        # RSS 2.0 items
        items = root.findall("./channel/item")
        if not items:
            # Some feeds use atom
            ns = {"atom": "http://www.w3.org/2005/Atom"}
            items = root.findall("atom:entry", ns)
            if items:
                return self._parse_atom(items, handle=handle, ns=ns)

        if not items:
            raise RuntimeError("RSS 中没有 item（账号不存在、被保护，或实例失效）")

        posts: list[Post] = []
        for item in items:
            title = (item.findtext("title") or "").strip()
            description = item.findtext("description") or ""
            link = (item.findtext("link") or "").strip()
            guid = (item.findtext("guid") or "").strip()
            pub = item.findtext("pubDate")

            text = html_to_text(description) or title
            post_id = extract_status_id(guid, link)
            if not post_id:
                # Fall back to hash-like guid to keep dedupe working
                post_id = guid or link or title[:40]
            url = nitter_link_to_x(link) or f"https://x.com/{handle}/status/{post_id}"

            posts.append(
                Post(
                    id=str(post_id),
                    handle=handle.lower(),
                    text=text,
                    created_at=parse_rss_date(pub),
                    url=url,
                    is_retweet=looks_like_retweet(title, text),
                    is_reply=looks_like_reply(title, text),
                    is_quote=looks_like_quote(text),
                    source=self.name,
                    raw_title=title,
                )
            )
        return posts

    def _parse_atom(self, entries: list[ET.Element], *, handle: str, ns: dict[str, str]) -> list[Post]:
        posts: list[Post] = []
        for entry in entries:
            title = (entry.findtext("atom:title", default="", namespaces=ns) or "").strip()
            content = (
                entry.findtext("atom:content", default="", namespaces=ns)
                or entry.findtext("atom:summary", default="", namespaces=ns)
                or ""
            )
            link_el = entry.find("atom:link", ns)
            link = ""
            if link_el is not None:
                link = link_el.attrib.get("href") or ""
            entry_id = entry.findtext("atom:id", default="", namespaces=ns) or ""
            published = (
                entry.findtext("atom:published", default="", namespaces=ns)
                or entry.findtext("atom:updated", default="", namespaces=ns)
            )
            text = html_to_text(content) or title
            post_id = extract_status_id(entry_id, link) or entry_id or title[:40]
            url = nitter_link_to_x(link) or f"https://x.com/{handle}/status/{post_id}"
            posts.append(
                Post(
                    id=str(post_id),
                    handle=handle.lower(),
                    text=text,
                    created_at=published or "",
                    url=url,
                    is_retweet=looks_like_retweet(title, text),
                    is_reply=looks_like_reply(title, text),
                    is_quote=looks_like_quote(text),
                    source=self.name,
                    raw_title=title,
                )
            )
        return posts
