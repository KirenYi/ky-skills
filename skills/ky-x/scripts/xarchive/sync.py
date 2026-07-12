from __future__ import annotations

import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from .config import effective_filters, expand_path, load_config
from .fetchers import build_fetcher
from .models import AppConfig, Filters, Post
from .state import StateStore
from .storage import ArchiveStorage


@dataclass
class AuthorSyncResult:
    handle: str
    fetched: int
    new: int
    skipped_filter: int
    error: str | None = None


def filter_posts(posts: list[Post], filters: Filters) -> tuple[list[Post], int]:
    kept: list[Post] = []
    skipped = 0
    for p in posts:
        if p.is_retweet and not filters.include_retweets:
            skipped += 1
            continue
        if p.is_reply and not filters.include_replies:
            skipped += 1
            continue
        # Quotes are kept by default; if disabled, drop posts that look like pure quotes
        # only when also not original-looking. Heuristic: if include_quotes is False and
        # is_quote, still keep unless it's empty-ish — actually drop quotes when disabled.
        if p.is_quote and not filters.include_quotes and not p.is_retweet:
            # Keep original posts that also quote; only skip if title suggests RT-like quote-only.
            # Conservative: if disabled, skip posts marked is_quote with short own text.
            skipped += 1
            continue
        kept.append(p)
    return kept, skipped


def run_sync(
    config_path: str | Path | None = None,
    only_handles: list[str] | None = None,
) -> list[AuthorSyncResult]:
    config = load_config(config_path)
    root = expand_path(config.output_dir)
    storage = ArchiveStorage(root)
    state = StateStore(root / "state.json")
    fetcher = build_fetcher(config)

    authors = list(config.authors)
    if only_handles:
        wanted = {h.lstrip("@").strip().lower() for h in only_handles if h}
        authors = [a for a in authors if a.normalized_handle() in wanted]
        missing = wanted - {a.normalized_handle() for a in authors}
        if missing:
            raise ValueError(
                "配置中没有这些博主，请先 add: "
                + ", ".join(f"@{h}" for h in sorted(missing))
            )

    results: list[AuthorSyncResult] = []
    now = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")

    for idx, author in enumerate(authors):
        handle = author.normalized_handle()
        if idx > 0 and config.request_delay_sec > 0:
            time.sleep(config.request_delay_sec)

        try:
            posts = fetcher.fetch_user_posts(handle)
            filters = effective_filters(config, author)
            filtered, skipped = filter_posts(posts, filters)

            existing = storage.load_existing_ids(handle) | state.seen_ids(handle)
            new_posts = [p for p in filtered if p.id not in existing]

            # Append in chronological order when possible (old -> new)
            new_posts.sort(key=lambda p: p.created_at or "")

            storage.append_posts(handle, new_posts)
            state.mark_seen(handle, [p.id for p in filtered])
            state.set_success(handle, now, len(new_posts))
            storage.rebuild_markdown_for_author(handle, note=author.note)

            result = AuthorSyncResult(
                handle=handle,
                fetched=len(posts),
                new=len(new_posts),
                skipped_filter=skipped,
            )
            storage.append_log(
                f"OK @{handle}: fetched={result.fetched} new={result.new} filtered_out={skipped}"
            )
            results.append(result)
        except Exception as exc:  # noqa: BLE001
            msg = str(exc)
            state.set_error(handle, msg)
            storage.append_log(f"ERR @{handle}: {msg}")
            results.append(
                AuthorSyncResult(
                    handle=handle,
                    fetched=0,
                    new=0,
                    skipped_filter=0,
                    error=msg,
                )
            )

    state.save()

    # Rebuild README
    summary_lines = []
    for r in results:
        if r.error:
            summary_lines.append(f"- @{r.handle}: 失败 — {r.error}")
        else:
            summary_lines.append(
                f"- @{r.handle}: 拉取 {r.fetched}，新增 {r.new}，过滤 {r.skipped_filter}"
            )
    storage.write_readme(
        config.authors,
        last_sync_summary="\n".join(summary_lines) if summary_lines else "（无）",
        source=config.source,
    )
    return results


def print_status(config_path: str | Path | None = None) -> None:
    config = load_config(config_path)
    root = expand_path(config.output_dir)
    storage = ArchiveStorage(root)
    state = StateStore(root / "state.json")

    print(f"输出目录: {root}")
    print(f"数据源:   {config.source}")
    print(f"博主数:   {len(config.authors)}")
    print("")
    for author in config.authors:
        h = author.normalized_handle()
        st = state.author(h)
        jsonl = storage.jsonl_path(h)
        count = 0
        if jsonl.exists():
            with jsonl.open("r", encoding="utf-8") as f:
                count = sum(1 for line in f if line.strip())
        note = f" ({author.note})" if author.note else ""
        print(f"@{h}{note}")
        print(f"  本地条数: {count}")
        print(f"  上次成功: {st.get('last_success_at') or '—'}")
        print(f"  上次新增: {st.get('last_new_count', 0)}")
        if st.get("last_error"):
            print(f"  上次错误: {st['last_error']}")
        print("")
