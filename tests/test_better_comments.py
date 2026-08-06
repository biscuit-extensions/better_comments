from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.better_comments import setup
from src.better_comments.extension import BetterComments


class TestBetterCommentsExtension:
    def test_extension_setup(self, app_instance) -> None:
        setup(app_instance.api)
        ext = BetterComments(app_instance.api)
        res = ext.categorize_comment("// ! Critical security flaw")
        assert res is not None
        assert res["category"] == "alert"
        todo = ext.categorize_comment("# TODO: Refactor loop")
        assert todo is not None
        assert todo["category"] == "todo"
