from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import AppConfig, AuthorConfig, Filters


DEFAULT_CONFIG_NAME = "config.json"


def default_config_path() -> Path:
    return Path.cwd() / DEFAULT_CONFIG_NAME


def expand_path(path: str | Path) -> Path:
    return Path(path).expanduser().resolve()


def load_config(path: str | Path | None = None) -> AppConfig:
    cfg_path = expand_path(path or default_config_path())
    if not cfg_path.exists():
        raise FileNotFoundError(
            f"找不到配置文件: {cfg_path}\n"
            f"请先复制 config.example.json 为 config.json，并填入博主列表。"
        )

    with cfg_path.open("r", encoding="utf-8") as f:
        raw: dict[str, Any] = json.load(f)

    filters_raw = raw.get("filters") or {}
    filters = Filters(
        include_replies=bool(filters_raw.get("include_replies", False)),
        include_retweets=bool(filters_raw.get("include_retweets", False)),
        include_quotes=bool(filters_raw.get("include_quotes", True)),
    )

    authors: list[AuthorConfig] = []
    for item in raw.get("authors") or []:
        if isinstance(item, str):
            authors.append(AuthorConfig(handle=item))
            continue
        authors.append(
            AuthorConfig(
                handle=str(item.get("handle") or item.get("username") or ""),
                note=str(item.get("note") or ""),
                include_replies=item.get("include_replies"),
                include_retweets=item.get("include_retweets"),
                include_quotes=item.get("include_quotes"),
            )
        )

    authors = [a for a in authors if a.normalized_handle()]
    if not authors:
        raise ValueError("config.authors 为空，请至少添加一个博主 handle。")

    instances = raw.get("nitter_instances") or ["https://nitter.net"]
    instances = [str(u).rstrip("/") for u in instances if str(u).strip()]

    output_dir = str(raw.get("output_dir") or "./data")
    return AppConfig(
        output_dir=output_dir,
        source=str(raw.get("source") or "nitter_rss"),
        nitter_instances=instances,
        authors=authors,
        filters=filters,
        request_timeout_sec=int(raw.get("request_timeout_sec") or 25),
        request_delay_sec=float(raw.get("request_delay_sec") or 1.0),
        user_agent=str(
            raw.get("user_agent") or "x-archive/0.1 (+local personal archiver)"
        ),
    )


def save_config(config: AppConfig, path: str | Path | None = None) -> Path:
    cfg_path = expand_path(path or default_config_path())
    payload = {
        "output_dir": config.output_dir,
        "source": config.source,
        "nitter_instances": config.nitter_instances,
        "request_timeout_sec": config.request_timeout_sec,
        "request_delay_sec": config.request_delay_sec,
        "user_agent": config.user_agent,
        "filters": {
            "include_replies": config.filters.include_replies,
            "include_retweets": config.filters.include_retweets,
            "include_quotes": config.filters.include_quotes,
        },
        "authors": [
            {
                "handle": a.normalized_handle(),
                "note": a.note,
                **(
                    {"include_replies": a.include_replies}
                    if a.include_replies is not None
                    else {}
                ),
                **(
                    {"include_retweets": a.include_retweets}
                    if a.include_retweets is not None
                    else {}
                ),
                **(
                    {"include_quotes": a.include_quotes}
                    if a.include_quotes is not None
                    else {}
                ),
            }
            for a in config.authors
        ],
    }
    cfg_path.parent.mkdir(parents=True, exist_ok=True)
    with cfg_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return cfg_path


def effective_filters(config: AppConfig, author: AuthorConfig) -> Filters:
    return Filters(
        include_replies=(
            config.filters.include_replies
            if author.include_replies is None
            else bool(author.include_replies)
        ),
        include_retweets=(
            config.filters.include_retweets
            if author.include_retweets is None
            else bool(author.include_retweets)
        ),
        include_quotes=(
            config.filters.include_quotes
            if author.include_quotes is None
            else bool(author.include_quotes)
        ),
    )
