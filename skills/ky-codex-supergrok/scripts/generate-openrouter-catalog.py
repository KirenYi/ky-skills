#!/usr/bin/env python3
"""Generate ~/.codex/model-catalogs/openrouter-models.json for in-UI model switching."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

OUT = Path.home() / ".codex" / "model-catalogs" / "openrouter-models.json"

# OpenRouter slugs — users can edit ky-profiles.json / this list later
MODELS = [
    {
        "slug": "anthropic/claude-sonnet-4.6",
        "display_name": "Claude Sonnet",
        "description": "Claude Sonnet via OpenRouter",
        "context_window": 200000,
        "priority": 0,
    },
    {
        "slug": "anthropic/claude-opus-4.6",
        "display_name": "Claude Opus",
        "description": "Claude Opus via OpenRouter",
        "context_window": 200000,
        "priority": 1,
    },
    {
        "slug": "deepseek/deepseek-chat",
        "display_name": "DeepSeek Chat",
        "description": "DeepSeek via OpenRouter",
        "context_window": 128000,
        "priority": 2,
    },
    {
        "slug": "deepseek/deepseek-r1",
        "display_name": "DeepSeek R1",
        "description": "DeepSeek R1 via OpenRouter",
        "context_window": 128000,
        "priority": 3,
    },
    {
        "slug": "google/gemini-2.5-pro",
        "display_name": "Gemini 2.5 Pro",
        "description": "Gemini via OpenRouter",
        "context_window": 1000000,
        "priority": 4,
    },
    {
        "slug": "openai/gpt-4.1",
        "display_name": "GPT-4.1 (OpenRouter)",
        "description": "OpenAI GPT via OpenRouter (billed on OpenRouter)",
        "context_window": 128000,
        "priority": 5,
    },
]

BASE = """You are Codex, a coding agent.
When asked which model you are, say you are running via OpenRouter (check the selected model id) and do not claim to be a different vendor's model.
Collaborate with the user until their goal is handled. Prefer concrete actions over long planning.
"""


def template() -> dict:
    entry = {
        "slug": "placeholder",
        "display_name": "placeholder",
        "description": "",
        "context_window": 128000,
        "max_context_window": 128000,
        "default_reasoning_level": "high",
        "supported_reasoning_levels": [
            {"effort": "low", "description": "Faster"},
            {"effort": "medium", "description": "Balanced"},
            {"effort": "high", "description": "Deeper"},
        ],
        "shell_type": "shell_command",
        "visibility": "list",
        "supported_in_api": True,
        "priority": 0,
        "availability_nux": None,
        "upgrade": None,
        "base_instructions": BASE,
        "supports_reasoning_summaries": True,
        "support_verbosity": False,
        "default_verbosity": None,
        "apply_patch_tool_type": None,
        "truncation_policy": {"mode": "tokens", "limit": 10000},
        "supports_parallel_tool_calls": True,
        "experimental_supported_tools": [],
    }
    try:
        codex = Path("/Applications/ChatGPT.app/Contents/Resources/codex")
        if codex.exists():
            raw = subprocess.check_output(
                [str(codex), "debug", "models", "--bundled"], text=True, timeout=30
            )
            tpl = json.loads(raw)["models"][0]
            for k, v in entry.items():
                tpl.setdefault(k, v)
            for drop in ("service_tiers", "additional_speed_tiers"):
                tpl.pop(drop, None)
            tpl["base_instructions"] = BASE
            tpl["availability_nux"] = None
            tpl["upgrade"] = None
            tpl["visibility"] = "list"
            tpl["supported_in_api"] = True
            return tpl
    except Exception:
        pass
    return entry


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else OUT
    out.parent.mkdir(parents=True, exist_ok=True)
    tpl = template()
    models = []
    for m in MODELS:
        e = dict(tpl)
        e.update(m)
        e["max_context_window"] = m.get("context_window", 128000)
        e["context_window"] = m.get("context_window", 128000)
        models.append(e)
    out.write_text(json.dumps({"models": models}, ensure_ascii=False, indent=2) + "\n")
    print(f"wrote {out} ({len(models)} models)")


if __name__ == "__main__":
    main()
