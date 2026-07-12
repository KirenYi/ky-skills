from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class StateStore:
    """Per-author sync state: seen ids + last success metadata."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self._data: dict[str, Any] = {"authors": {}}
        self.load()

    def load(self) -> None:
        if not self.path.exists():
            self._data = {"authors": {}}
            return
        with self.path.open("r", encoding="utf-8") as f:
            self._data = json.load(f)
        self._data.setdefault("authors", {})

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(self._data, f, ensure_ascii=False, indent=2)
            f.write("\n")

    def author(self, handle: str) -> dict[str, Any]:
        key = handle.lstrip("@").lower()
        authors = self._data.setdefault("authors", {})
        if key not in authors:
            authors[key] = {
                "seen_ids": [],
                "last_success_at": None,
                "last_error": None,
                "last_new_count": 0,
            }
        return authors[key]

    def seen_ids(self, handle: str) -> set[str]:
        raw = self.author(handle).get("seen_ids") or []
        return {str(x) for x in raw}

    def mark_seen(self, handle: str, post_ids: list[str], *, keep_last: int = 5000) -> None:
        entry = self.author(handle)
        merged = list(dict.fromkeys(list(entry.get("seen_ids") or []) + post_ids))
        # Keep the most recent end of the list to bound file size.
        entry["seen_ids"] = merged[-keep_last:]

    def set_success(self, handle: str, when_iso: str, new_count: int) -> None:
        entry = self.author(handle)
        entry["last_success_at"] = when_iso
        entry["last_new_count"] = new_count
        entry["last_error"] = None

    def set_error(self, handle: str, message: str) -> None:
        self.author(handle)["last_error"] = message

    def all_authors(self) -> dict[str, Any]:
        return dict(self._data.get("authors") or {})
