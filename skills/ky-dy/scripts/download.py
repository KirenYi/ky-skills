#!/usr/bin/env python3
"""ky-dy: download a public Douyin video via Playwright network intercept.

MIT License — Kiren Yi (KY) / ky-skills
Technique: headless Chromium intercepts aweme/detail JSON for play URLs.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

try:
    import requests
except ImportError:
    print("缺少 requests。请执行: pip install requests playwright", file=sys.stderr)
    sys.exit(1)

try:
    from playwright.sync_api import Error as PlaywrightError
    from playwright.sync_api import sync_playwright
except ImportError:
    print("缺少 playwright。请执行: pip install playwright && python -m playwright install chromium", file=sys.stderr)
    sys.exit(1)

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
MISSING_BROWSER = ("Executable doesn't exist", "playwright install")


def extract_video_id(url: str) -> Optional[str]:
    for pattern in (r"/video/(\d+)", r"modal_id=(\d+)", r"resource_id=(\d+)"):
        m = re.search(pattern, url)
        if m:
            return m.group(1)
    return None


def normalize_url(url: str) -> str:
    vid = extract_video_id(url)
    return f"https://www.douyin.com/video/{vid}" if vid else url


def ensure_chromium() -> None:
    print("正在安装 Playwright Chromium…")
    subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])


def pick_play_url(aweme: dict[str, Any]) -> Optional[str]:
    video = aweme.get("video") or {}
    for key in ("play_addr", "play_addr_h264", "download_addr"):
        urls = (video.get(key) or {}).get("url_list") or []
        if urls:
            return urls[0]
    return None


def fetch_aweme(url: str, timeout: int = 60) -> dict[str, Any]:
    try:
        return _fetch_aweme_once(url, timeout)
    except PlaywrightError as exc:
        if any(h in str(exc) for h in MISSING_BROWSER):
            ensure_chromium()
            return _fetch_aweme_once(url, timeout)
        raise


def _fetch_aweme_once(url: str, timeout: int) -> dict[str, Any]:
    page_url = normalize_url(url)
    aweme: dict[str, Any] = {}
    play_url: Optional[str] = None

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            context = browser.new_context(user_agent=USER_AGENT, locale="zh-CN")
            page = context.new_page()

            def on_response(response) -> None:
                nonlocal aweme, play_url
                if "aweme/detail" not in response.url or "douyin.com" not in response.url:
                    return
                try:
                    body = response.json()
                    detail = body.get("aweme_detail") or {}
                    if detail:
                        aweme = detail
                        play_url = pick_play_url(detail)
                except Exception:
                    pass

            page.on("response", on_response)
            print(f"打开: {page_url}")
            try:
                page.goto(page_url, wait_until="domcontentloaded", timeout=30000)
            except Exception as exc:
                print(f"页面提示: {exc}")
            deadline = time.time() + timeout
            while time.time() < deadline and not aweme:
                page.wait_for_timeout(500)
        finally:
            browser.close()

    if not aweme:
        raise RuntimeError("未拦截到 aweme/detail，请检查链接是否有效或稍后重试")
    if not play_url:
        play_url = pick_play_url(aweme)
    return {
        "aweme": aweme,
        "play_url": play_url,
        "title": aweme.get("desc") or "",
        "author": (aweme.get("author") or {}).get("nickname") or "",
        "aweme_id": str(aweme.get("aweme_id") or extract_video_id(url) or ""),
    }


def metadata_blob(info: dict[str, Any], source_url: str) -> dict[str, Any]:
    aweme = info["aweme"]
    author = aweme.get("author") or {}
    video = aweme.get("video") or {}
    return {
        "source_url": source_url,
        "fetched_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "aweme_id": info["aweme_id"],
        "title": info["title"],
        "author": info["author"],
        "author_id": author.get("uid") or "",
        "create_time": aweme.get("create_time"),
        "duration_ms": video.get("duration"),
        "statistics": aweme.get("statistics") or {},
        "tool": "ky-dy",
    }


def download_file(play_url: str, dest: Path) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    headers = {"User-Agent": USER_AGENT, "Referer": "https://www.douyin.com/"}
    with requests.get(play_url, headers=headers, stream=True, timeout=90) as resp:
        resp.raise_for_status()
        total = int(resp.headers.get("Content-Length") or 0)
        done = 0
        with open(dest, "wb") as f:
            for chunk in resp.iter_content(chunk_size=256 * 1024):
                if not chunk:
                    continue
                f.write(chunk)
                done += len(chunk)
                if total:
                    pct = min(100, done * 100 // total)
                    if pct % 20 == 0:
                        print(f"进度 {pct}%")
    return dest


def main() -> int:
    parser = argparse.ArgumentParser(description="ky-dy 视频下载")
    parser.add_argument("url", help="抖音视频链接")
    parser.add_argument("output", nargs="?", help="输出 mp4 路径")
    parser.add_argument("--metadata-only", action="store_true")
    parser.add_argument("--timeout", type=int, default=60)
    args = parser.parse_args()

    print("ky-dy")
    try:
        info = fetch_aweme(args.url, timeout=args.timeout)
    except Exception as exc:
        print(f"失败: {exc}", file=sys.stderr)
        return 1

    print(f"标题: {info['title'] or '(无)'}")
    print(f"作者: {info['author'] or '(无)'}")
    print(f"ID: {info['aweme_id']}")

    out = Path(args.output).expanduser() if args.output else Path.home() / "Downloads" / f"douyin_{info['aweme_id']}.mp4"
    meta_path = Path(str(out) + ".metadata.json")
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.write_text(json.dumps(metadata_blob(info, args.url), ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"元数据: {meta_path}")

    if args.metadata_only:
        return 0
    if not info.get("play_url"):
        print("无播放地址", file=sys.stderr)
        return 1
    try:
        path = download_file(info["play_url"], out)
    except Exception as exc:
        print(f"下载失败: {exc}", file=sys.stderr)
        return 1
    size_mb = path.stat().st_size / 1024 / 1024
    print(f"完成: {path} ({size_mb:.2f} MB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
