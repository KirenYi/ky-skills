#!/usr/bin/env python3
"""ky-xhs: fetch a public Xiaohongshu note (metadata + media).

MIT License — Kiren Yi (KY) / ky-skills
Parses window.__INITIAL_STATE__; optional XHS_COOKIE env for logged-in HTML.
"""

from __future__ import annotations

import argparse
import html as html_lib
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    print("缺少 requests。请执行: pip install requests", file=sys.stderr)
    sys.exit(1)

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


def headers(referer: Optional[str] = None) -> Dict[str, str]:
    h = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    }
    if referer:
        h["Referer"] = referer
    cookie = os.environ.get("XHS_COOKIE", "").strip()
    if cookie:
        h["Cookie"] = cookie
    return h


def note_id_from_url(url: str) -> str:
    for pattern in (r"/explore/([0-9a-zA-Z]+)", r"/discovery/item/([0-9a-zA-Z]+)", r"[?&]note_id=([0-9a-zA-Z]+)"):
        m = re.search(pattern, url)
        if m:
            return m.group(1)
    parts = [p for p in urlparse(url).path.split("/") if p]
    if parts:
        return parts[-1]
    raise ValueError("无法识别 note_id")


def extract_initial_state(page_html: str) -> Dict[str, Any]:
    m = re.search(r"window\.__INITIAL_STATE__\s*=\s*", page_html)
    if not m:
        raise ValueError("未找到 __INITIAL_STATE__（可能需 xsec_token 或 XHS_COOKIE）")
    start = m.end()
    end = page_html.find("</script>", start)
    if end < 0:
        raise ValueError("INITIAL_STATE 截断异常")
    raw = page_html[start:end].strip().rstrip(";")
    raw = html_lib.unescape(raw)
    raw = re.sub(r"\bundefined\b", "null", raw)
    return json.loads(raw)


def walk_note_maps(obj: Any) -> Iterable[Dict[str, Any]]:
    if isinstance(obj, dict):
        nm = obj.get("noteDetailMap")
        if isinstance(nm, dict):
            yield nm
        for v in obj.values():
            yield from walk_note_maps(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk_note_maps(v)


def extract_note(state: Dict[str, Any], note_id: str) -> Dict[str, Any]:
    for note_map in walk_note_maps(state):
        detail = note_map.get(note_id)
        if isinstance(detail, dict) and isinstance(detail.get("note"), dict):
            return detail["note"]
        for detail in note_map.values():
            if not isinstance(detail, dict):
                continue
            note = detail.get("note")
            if isinstance(note, dict) and (note.get("noteId") == note_id or note.get("id") == note_id):
                return note
    raise ValueError("INITIAL_STATE 中无目标笔记")


def parse_media_v2(note: Dict[str, Any]) -> Dict[str, Any]:
    video = note.get("video") or {}
    raw = video.get("mediaV2") or (video.get("consumer") or {}).get("mediaV2")
    if not raw:
        return {}
    if isinstance(raw, dict):
        return raw
    try:
        return json.loads(raw)
    except Exception:
        return {}


def video_urls(note: Dict[str, Any]) -> List[str]:
    urls: List[str] = []
    streams = [
        (parse_media_v2(note).get("video") or {}).get("stream") or {},
        ((note.get("video") or {}).get("media") or {}).get("stream") or {},
    ]
    for stream in streams:
        if not isinstance(stream, dict):
            continue
        for codec in ("h264", "h265", "h266", "av1"):
            for item in stream.get(codec) or []:
                if not isinstance(item, dict):
                    continue
                for key in ("masterUrl", "master_url"):
                    u = item.get(key)
                    if u and u not in urls:
                        urls.append(u)
                for u in item.get("backupUrls") or item.get("backup_urls") or []:
                    if u and u not in urls:
                        urls.append(u)
    return urls


def image_urls(note: Dict[str, Any]) -> List[str]:
    out: List[str] = []
    for image in note.get("imageList") or []:
        if not isinstance(image, dict):
            continue
        candidates = [image.get("urlDefault"), image.get("url"), image.get("urlPre")]
        for info in image.get("infoList") or []:
            if isinstance(info, dict):
                candidates.append(info.get("url"))
        for u in candidates:
            if u and u not in out:
                out.append(u)
                break
    return out


def subtitle_entries(note: Dict[str, Any]) -> List[Dict[str, str]]:
    subs: List[Dict[str, str]] = []
    smap = ((parse_media_v2(note).get("video") or {}).get("subtitles")) or {}
    for label, entries in smap.items():
        if not isinstance(entries, list):
            continue
        for entry in entries:
            if isinstance(entry, dict) and entry.get("url"):
                subs.append(
                    {
                        "label": str(label),
                        "language": str(entry.get("language") or label),
                        "url": entry["url"],
                    }
                )
    return subs


def build_metadata(note: Dict[str, Any], source_url: str, note_id: str) -> Dict[str, Any]:
    user = note.get("user") or {}
    tags = [t.get("name") for t in (note.get("tagList") or []) if isinstance(t, dict) and t.get("name")]
    vurls = video_urls(note)
    return {
        "source_url": source_url,
        "fetched_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "note_id": note_id,
        "title": note.get("title") or "",
        "desc": note.get("desc") or "",
        "type": note.get("type") or "",
        "author": user.get("nickname") or "",
        "user_id": user.get("userId") or "",
        "time": note.get("time"),
        "interact_info": note.get("interactInfo") or {},
        "tags": tags,
        "video_url": vurls[0] if vurls else "",
        "backup_urls": vurls[1:],
        "image_urls": image_urls(note),
        "subtitle_urls": subtitle_entries(note),
        "tool": "ky-xhs",
    }


def download(urls: List[str], path: Path, referer: str, label: str) -> Optional[Path]:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.stat().st_size > 0:
        print(f"{label} 已存在: {path}")
        return path
    last: Optional[Exception] = None
    for url in urls:
        try:
            with requests.get(url, headers=headers(referer), stream=True, timeout=90) as resp:
                resp.raise_for_status()
                with open(path, "wb") as f:
                    for chunk in resp.iter_content(chunk_size=256 * 1024):
                        if chunk:
                            f.write(chunk)
            return path
        except Exception as exc:
            last = exc
    print(f"{label} 失败: {last}")
    return None


def srt_to_text(srt: str) -> str:
    lines: List[str] = []
    for block in re.split(r"\n\s*\n", srt.strip()):
        bl = [x.strip() for x in block.splitlines() if x.strip()]
        idx = next((i for i, line in enumerate(bl) if "-->" in line), None)
        if idx is None:
            continue
        start = bl[idx].split("-->", 1)[0].strip()
        text = " ".join(bl[idx + 1 :]).strip()
        if text:
            lines.append(f"[{start}] {text}")
    return "\n".join(lines) + ("\n" if lines else "")


def main() -> int:
    parser = argparse.ArgumentParser(description="ky-xhs 笔记抓取")
    parser.add_argument("url", help="小红书笔记链接")
    parser.add_argument("output_dir", nargs="?", help="输出目录")
    parser.add_argument("--skip-media", action="store_true")
    args = parser.parse_args()

    try:
        note_id = note_id_from_url(args.url)
    except Exception as exc:
        print(f"失败: {exc}", file=sys.stderr)
        return 1

    out = Path(args.output_dir).expanduser() if args.output_dir else Path.home() / "Downloads" / f"xhs_{note_id}"
    out.mkdir(parents=True, exist_ok=True)
    print("ky-xhs")
    print(f"note_id={note_id}")
    print(f"out={out}")

    try:
        page = requests.get(args.url, headers=headers(), timeout=60)
        page.raise_for_status()
        html = page.text
        (out / f"xhs_{note_id}.html").write_text(html, encoding="utf-8")
        state = extract_initial_state(html)
        note = extract_note(state, note_id)
        meta = build_metadata(note, args.url, note_id)
        meta_path = out / f"xhs_{note_id}.metadata.json"
        meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"标题: {meta.get('title') or '(无)'}")
        print(f"作者: {meta.get('author') or '(无)'}")
        print(f"类型: {meta.get('type') or '(无)'}")
        print(f"元数据: {meta_path}")

        if args.skip_media:
            return 0

        if meta.get("type") == "video":
            vurls = video_urls(note)
            if vurls:
                vp = download(vurls, out / f"xhs_{note_id}.mp4", args.url, "视频")
                if vp:
                    print(f"视频: {vp}")
            for i, sub in enumerate(subtitle_entries(note)):
                lang = re.sub(r"[^0-9A-Za-z._-]+", "_", f"{sub['label']}_{sub['language']}")
                sp = download([sub["url"]], out / f"xhs_{note_id}.{lang}.srt", args.url, f"字幕{i}")
                if sp and i == 0:
                    text = srt_to_text(sp.read_text(encoding="utf-8", errors="ignore"))
                    tp = out / f"xhs_{note_id}.transcript.txt"
                    tp.write_text(text, encoding="utf-8")
                    print(f"口播: {tp}")
        else:
            imgs = image_urls(note)
            img_dir = out / "images"
            for i, u in enumerate(imgs, 1):
                suffix = Path(urlparse(u).path).suffix or ".jpg"
                download([u], img_dir / f"xhs_{note_id}_{i:02d}{suffix}", args.url, f"图{i}")
        print("完成")
        return 0
    except Exception as exc:
        print(f"失败: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
