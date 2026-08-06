from __future__ import annotations

import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


class BetterComments(Extension):
    """Human-friendly colorful comment highlighting for alerts, queries, and todos."""

    def __init__(self, api: ExtensionsAPI) -> None:
        super().__init__(api)
        self.api = api
        self.tags = {
            "!": {"name": "alert", "color": "#FF2D55"},
            "?": {"name": "query", "color": "#34C759"},
            "TODO": {"name": "todo", "color": "#FF9500"},
            "*": {"name": "highlight", "color": "#007AFF"},
            "//": {"name": "strikethrough", "color": "#8E8E93"},
        }
        self.api.logger.info("Better Comments extension initialised.")

    def categorize_comment(self, comment_text: str) -> dict | None:
        clean = comment_text.lstrip("/#* -")
        for tag, info in self.tags.items():
            if clean.startswith(tag):
                return {
                    "tag": tag,
                    "category": info["name"],
                    "color": info["color"],
                    "content": clean[len(tag):].strip()
                }
        return None

    def install(self) -> None:
        self.api.logger.info("Better Comments extension installed.")
