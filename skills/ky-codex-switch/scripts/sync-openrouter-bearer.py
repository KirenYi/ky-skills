#!/usr/bin/env python3
"""Sync OPENROUTER_API_KEY from ky-provider.env into config.toml for Codex Desktop."""
from __future__ import annotations

import os
import sys
from pathlib import Path

def main() -> int:
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    cfg_path = Path(sys.argv[1]) if len(sys.argv) > 1 else codex_home / "config.toml"
    env_path = Path(sys.argv[2]) if len(sys.argv) > 2 else codex_home / "ky-provider.env"

    key = None
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            s = line.strip()
            if s.startswith("OPENROUTER_API_KEY="):
                key = s.split("=", 1)[1].strip().strip('"').strip("'")
                break
    if not key:
        key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        print("no OPENROUTER_API_KEY to sync", file=sys.stderr)
        return 0

    esc = key.replace("\\", "\\\\").replace('"', '\\"')
    block = (
        "[model_providers.openrouter]\n"
        'name = "OpenRouter"\n'
        'base_url = "https://openrouter.ai/api/v1"\n'
        'wire_api = "responses"\n'
        'env_key = "OPENROUTER_API_KEY"\n'
        f'experimental_bearer_token = "{esc}"\n'
        "supports_websockets = false\n"
        "request_max_retries = 4\n"
        "stream_idle_timeout_ms = 600000\n"
        'http_headers = { "HTTP-Referer" = "https://github.com/KirenYi/ky-skills", '
        '"X-Title" = "ky-codex-switch" }\n'
    )

    text = cfg_path.read_text() if cfg_path.exists() else ""
    marker = "[model_providers.openrouter]"
    if marker in text:
        start = text.find(marker)
        lines = text[start:].splitlines(keepends=True)
        n = 1
        while n < len(lines):
            if lines[n].startswith("["):
                break
            n += 1
        end = start + sum(len(x) for x in lines[:n])
        text = text[:start] + block + "\n" + text[end:].lstrip("\n")
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    cfg_path.parent.mkdir(parents=True, exist_ok=True)
    cfg_path.write_text(text if text.endswith("\n") else text + "\n")
    print("openrouter bearer synced for Desktop")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
