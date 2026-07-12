from __future__ import annotations

from abc import ABC, abstractmethod

from ..models import Post


class Fetcher(ABC):
    name: str = "base"

    @abstractmethod
    def fetch_user_posts(self, handle: str) -> list[Post]:
        """Return recent posts for handle, newest-first or arbitrary order."""
