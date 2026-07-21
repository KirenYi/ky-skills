#!/usr/bin/env python3
"""Generate ~/.codex/model-catalogs/xai-models.json for SuperGrok."""
from __future__ import annotations

import json
import sys
from pathlib import Path

OUT = Path.home() / ".codex" / "model-catalogs" / "xai-models.json"

BASE_INSTRUCTIONS = """You are Codex running on Grok 4.5 (xAI SuperGrok subscription).

Important identity facts:
- Your underlying model is Grok 4.5 from xAI, accessed via SuperGrok (cli-chat-proxy), not OpenAI GPT-5 and not console.x.ai paid API billing.
- When asked what model you are, answer honestly: Codex agent on Grok 4.5 (xAI SuperGrok).
- Do not claim to be GPT-5, GPT-4, Claude, or any non-Grok model.

You and the user share one workspace. Collaborate until their goal is genuinely handled.
Be a pragmatic coding agent: inspect before editing, make focused changes, run checks when useful, and explain briefly what you did.
Prefer concrete actions over long planning unless the user asks for a plan.
"""

ENTRY = {
    "slug": "grok-4.5",
    "display_name": "Grok 4.5 (SuperGrok)",
    "description": "Grok 4.5 via SuperGrok subscription (not OpenAI GPT). Same login as Grok Build.",
    "context_window": 500000,
    "max_context_window": 500000,
    "default_reasoning_level": "high",
    "supported_reasoning_levels": [
        {"effort": "low", "description": "Fast responses with lighter reasoning"},
        {"effort": "medium", "description": "Balances speed and reasoning depth"},
        {"effort": "high", "description": "Greater reasoning depth for complex problems"},
    ],
    "shell_type": "shell_command",
    "visibility": "list",
    "supported_in_api": True,
    "priority": 0,
    "availability_nux": None,
    "upgrade": None,
    "base_instructions": BASE_INSTRUCTIONS,
    "supports_reasoning_summaries": True,
    "support_verbosity": False,
    "default_verbosity": None,
    "apply_patch_tool_type": None,
    "truncation_policy": {"mode": "tokens", "limit": 10000},
    "supports_parallel_tool_calls": True,
    "experimental_supported_tools": [],
}


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else OUT
    out.parent.mkdir(parents=True, exist_ok=True)
    # Prefer cloning a bundled Codex model template when available (strict parsers).
    entry = dict(ENTRY)
    try:
        import subprocess

        codex = Path("/Applications/ChatGPT.app/Contents/Resources/codex")
        if codex.exists():
            raw = subprocess.check_output(
                [str(codex), "debug", "models", "--bundled"],
                text=True,
                timeout=30,
            )
            tpl = json.loads(raw)["models"][0]
            merged = dict(tpl)
            for k, v in ENTRY.items():
                merged[k] = v
            for drop in ("service_tiers", "additional_speed_tiers"):
                merged.pop(drop, None)
            entry = merged
    except Exception:
        pass

    out.write_text(json.dumps({"models": [entry]}, ensure_ascii=False, indent=2) + "\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
