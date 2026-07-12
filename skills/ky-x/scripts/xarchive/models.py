from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class Post:
    id: str
    handle: str
    text: str
    created_at: str  # ISO-8601 when possible
    url: str
    is_retweet: bool = False
    is_reply: bool = False
    is_quote: bool = False
    source: str = ""
    raw_title: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Post":
        return cls(
            id=str(data["id"]),
            handle=str(data["handle"]).lstrip("@").lower(),
            text=str(data.get("text") or ""),
            created_at=str(data.get("created_at") or ""),
            url=str(data.get("url") or ""),
            is_retweet=bool(data.get("is_retweet", False)),
            is_reply=bool(data.get("is_reply", False)),
            is_quote=bool(data.get("is_quote", False)),
            source=str(data.get("source") or ""),
            raw_title=str(data.get("raw_title") or ""),
        )


@dataclass
class AuthorConfig:
    handle: str
    note: str = ""
    include_replies: bool | None = None
    include_retweets: bool | None = None
    include_quotes: bool | None = None

    def normalized_handle(self) -> str:
        return self.handle.lstrip("@").strip().lower()


@dataclass
class Filters:
    include_replies: bool = False
    include_retweets: bool = False
    include_quotes: bool = True


@dataclass
class AppConfig:
    output_dir: str
    source: str = "nitter_rss"
    nitter_instances: list[str] = field(default_factory=lambda: ["https://nitter.net"])
    authors: list[AuthorConfig] = field(default_factory=list)
    filters: Filters = field(default_factory=Filters)
    request_timeout_sec: int = 25
    request_delay_sec: float = 1.0
    user_agent: str = "x-archive/0.1 (+local personal archiver)"
