from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from .models import AuthorConfig, Post


class ArchiveStorage:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.data_dir = root / "data"
        self.library_dir = root / "library"
        self.logs_dir = root / "logs"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.library_dir.mkdir(parents=True, exist_ok=True)
        self.logs_dir.mkdir(parents=True, exist_ok=True)

    def jsonl_path(self, handle: str) -> Path:
        return self.data_dir / f"@{handle.lower()}.jsonl"

    def load_existing_ids(self, handle: str) -> set[str]:
        path = self.jsonl_path(handle)
        if not path.exists():
            return set()
        ids: set[str] = set()
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if "id" in obj:
                    ids.add(str(obj["id"]))
        return ids

    def append_posts(self, handle: str, posts: list[Post]) -> int:
        if not posts:
            return 0
        path = self.jsonl_path(handle)
        with path.open("a", encoding="utf-8") as f:
            for post in posts:
                f.write(json.dumps(post.to_dict(), ensure_ascii=False) + "\n")
        return len(posts)

    def rebuild_markdown_for_author(self, handle: str, note: str = "") -> None:
        handle = handle.lower()
        path = self.jsonl_path(handle)
        author_dir = self.library_dir / handle
        author_dir.mkdir(parents=True, exist_ok=True)

        posts: list[Post] = []
        if path.exists():
            with path.open("r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        posts.append(Post.from_dict(json.loads(line)))
                    except Exception:
                        continue

        # De-dupe by id, keep first occurrence (usually chronological append order)
        deduped: dict[str, Post] = {}
        for p in posts:
            if p.id not in deduped:
                deduped[p.id] = p
        posts = list(deduped.values())

        def sort_key(p: Post) -> str:
            return p.created_at or ""

        posts.sort(key=sort_key, reverse=True)

        by_month: dict[str, list[Post]] = defaultdict(list)
        for p in posts:
            month = _month_key(p.created_at)
            by_month[month].append(p)

        # Remove old monthly files then rewrite
        for old in author_dir.glob("*.md"):
            if old.name in {"_index.md", "_coverage.md"}:
                continue
            old.unlink(missing_ok=True)

        for month, month_posts in sorted(by_month.items(), reverse=True):
            md_path = author_dir / f"{month}.md"
            lines = [
                f"# @{handle} — {month}",
                "",
                f"共 {len(month_posts)} 条",
                "",
            ]
            for p in month_posts:
                flags = []
                if p.is_retweet:
                    flags.append("转推")
                if p.is_reply:
                    flags.append("回复")
                if p.is_quote:
                    flags.append("引用")
                flag_s = f" ({', '.join(flags)})" if flags else ""
                lines.append(f"### {p.created_at or '未知时间'}{flag_s}")
                lines.append("")
                if p.url:
                    lines.append(f"链接: {p.url}")
                    lines.append("")
                lines.append(p.text.strip() or "（无文本）")
                lines.append("")
                lines.append("---")
                lines.append("")
            md_path.write_text("\n".join(lines), encoding="utf-8")

        index_lines = [
            f"# @{handle}",
            "",
        ]
        if note:
            index_lines += [f"> {note}", ""]
        index_lines += [
            f"- 归档条数: **{len(posts)}**",
            f"- JSONL: `data/@{handle}.jsonl`",
            f"- 最近更新: {datetime.now(timezone.utc).astimezone().isoformat(timespec='seconds')}",
            "",
            "## 月份",
            "",
        ]
        for month in sorted(by_month.keys(), reverse=True):
            index_lines.append(f"- [{month}](./{month}.md) — {len(by_month[month])} 条")
        index_lines.append("")
        (author_dir / "_index.md").write_text("\n".join(index_lines), encoding="utf-8")

    def write_readme(
        self,
        authors: list[AuthorConfig],
        *,
        last_sync_summary: str,
        source: str,
    ) -> None:
        lines = [
            "# X Thought Archive",
            "",
            "本地高质量博主思想归档（自动生成，请勿手改后依赖它不被覆盖）。",
            "",
            f"- 数据源: `{source}`",
            f"- 上次同步: {datetime.now(timezone.utc).astimezone().isoformat(timespec='seconds')}",
            "",
            "## 同步摘要",
            "",
            last_sync_summary,
            "",
            "## 博主",
            "",
        ]
        for a in authors:
            h = a.normalized_handle()
            jsonl = self.jsonl_path(h)
            count = 0
            if jsonl.exists():
                with jsonl.open("r", encoding="utf-8") as f:
                    count = sum(1 for line in f if line.strip())
            note = f" — {a.note}" if a.note else ""
            lines.append(f"- [@{h}](library/{h}/_index.md){note}（{count} 条）")
        lines += [
            "",
            "## 目录说明",
            "",
            "- `data/@handle.jsonl`：机器可读真源（一行一条）",
            "- `library/handle/`：人类可读 Markdown",
            "- `state.json`：去重与同步状态",
            "- `logs/`：运行日志",
            "",
        ]
        (self.root / "README.md").write_text("\n".join(lines), encoding="utf-8")

    def append_log(self, message: str) -> None:
        day = datetime.now().strftime("%Y-%m-%d")
        path = self.logs_dir / f"sync-{day}.log"
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with path.open("a", encoding="utf-8") as f:
            f.write(f"[{ts}] {message}\n")


def _month_key(created_at: str) -> str:
    if not created_at:
        return "unknown"
    # ISO or similar
    if len(created_at) >= 7 and created_at[4] == "-":
        return created_at[:7]
    return "unknown"
