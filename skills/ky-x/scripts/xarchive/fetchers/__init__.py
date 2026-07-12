from __future__ import annotations

from ..models import AppConfig
from .base import Fetcher
from .nitter_rss import NitterRssFetcher


def build_fetcher(config: AppConfig) -> Fetcher:
    source = (config.source or "nitter_rss").strip().lower()
    if source in {"nitter", "nitter_rss", "rss"}:
        return NitterRssFetcher(config)
    if source in {"x_api", "twitter_api", "official"}:
        raise NotImplementedError(
            "官方 X API 数据源尚未接入。当前请使用 source: nitter_rss。\n"
            "效果验证通过后，可在同一项目中切换到 x_api。"
        )
    raise ValueError(f"未知数据源: {config.source!r}（支持: nitter_rss）")
