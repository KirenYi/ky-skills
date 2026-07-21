#!/usr/bin/env bash
# Install multi-model Codex switcher: SuperGrok + OpenAI + OpenRouter (Claude/DeepSeek/…).
set -euo pipefail

SKILL_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SCRIPTS="$SKILL_ROOT/scripts"
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
BIN="$CODEX_HOME/bin"

echo "== ky-codex-supergrok install (multi-model) =="
echo "skill: $SKILL_ROOT"
echo "codex home: $CODEX_HOME"

mkdir -p "$BIN" "$CODEX_HOME/model-catalogs" "$CODEX_HOME/provider-switch-backups"

install_bin() {
  local name="$1"
  cp "$SCRIPTS/$name" "$BIN/$name"
  chmod 700 "$BIN/$name"
  echo "installed $BIN/$name"
}

install_bin supergrok-token
install_bin supergrok-proxy
install_bin codex-provider
install_bin codex-provider-app-run
install_bin ensure-desktop-shortcut.sh
cp "$SCRIPTS/profiles.json" "$CODEX_HOME/ky-profiles.json"
echo "installed $CODEX_HOME/ky-profiles.json"
cp "$SCRIPTS/generate-catalog.py" "$BIN/generate-catalog.py" 2>/dev/null || true
chmod 700 "$BIN/generate-catalog.py" 2>/dev/null || true

python3 "$SCRIPTS/generate-catalog.py" "$CODEX_HOME/model-catalogs/xai-models.json"
python3 "$SCRIPTS/generate-openrouter-catalog.py" "$CODEX_HOME/model-catalogs/openrouter-models.json"

# Offline tutorials for "不会使用怎么办"
mkdir -p "$CODEX_HOME/ky-tutorials"
cp -R "$SKILL_ROOT/references/tutorials/." "$CODEX_HOME/ky-tutorials/" 2>/dev/null || true


# Ensure providers via codex-provider
"$BIN/codex-provider" list >/dev/null
# force provider blocks
python3 - <<PY
import json
from pathlib import Path
import subprocess, os
os.environ["KY_CODEX_PROFILES"] = str(Path("$CODEX_HOME/ky-profiles.json"))
# run ensure via use --no-restart openai is heavy; call provider list/status after path
print("profiles ok")
PY

# Ensure provider tables exist by calling internal ensure: use status after PATH
export KY_CODEX_PROFILES="$CODEX_HOME/ky-profiles.json"
# Trigger ensure_providers by a dry path: python snippet from install
python3 - "$CODEX_HOME/config.toml" "$CODEX_HOME/ky-profiles.json" <<'PY'
import json, sys
from pathlib import Path
cfg_path = Path(sys.argv[1]); prof = json.loads(Path(sys.argv[2]).read_text())
text = cfg_path.read_text() if cfg_path.exists() else ""
providers = prof.get("providers") or {}
changed = False
for pid, p in providers.items():
    marker = f"[model_providers.{pid}]"
    if marker in text:
        continue
    block = [f"\n# --- ky-codex-supergrok provider: {pid} ---", marker, f'name = "{p["name"]}"', f'base_url = "{p["base_url"]}"', f'wire_api = "{p.get("wire_api","responses")}"']
    if p.get("env_key"):
        block.append(f'env_key = "{p["env_key"]}"')
    if p.get("supports_websockets") is False:
        block.append("supports_websockets = false")
    block.append("request_max_retries = 4")
    block.append("stream_idle_timeout_ms = 600000")
    headers = p.get("http_headers") or {}
    if headers:
        block.append("http_headers = { " + ", ".join(f'"{k}" = "{v}"' for k,v in headers.items()) + " }")
    text = text.rstrip() + "\n" + "\n".join(block) + "\n"
    changed = True
cfg_path.parent.mkdir(parents=True, exist_ok=True)
cfg_path.write_text(text if text.endswith("\n") else text+"\n")
print("providers updated" if changed else "providers already present")
PY

# env example
if [[ ! -f "$CODEX_HOME/ky-provider.env" ]]; then
  cat > "$CODEX_HOME/ky-provider.env" <<'ENV'
# ky-codex-supergrok secrets (chmod 600). Do NOT commit this file.
# OpenRouter unlocks Claude / DeepSeek / Gemini one-click profiles:
#   https://openrouter.ai/keys
# OPENROUTER_API_KEY=sk-or-v1-...

# Optional (not required for SuperGrok subscription path):
# DEEPSEEK_API_KEY=
# ANTHROPIC_API_KEY=
# XAI_API_KEY=
ENV
  chmod 600 "$CODEX_HOME/ky-provider.env"
  echo "created $CODEX_HOME/ky-provider.env (add OPENROUTER_API_KEY for Claude/DeepSeek)"
else
  echo "keep existing $CODEX_HOME/ky-provider.env"
fi

# layered profile for CLI
cat > "$CODEX_HOME/xai.config.toml" <<'TOML'
model = "grok-4.5"
model_provider = "xai"
model_reasoning_effort = "high"
model_catalog_json = "~/.codex/model-catalogs/xai-models.json"
TOML

if [[ "$(uname -s)" == "Darwin" ]]; then
  # Hub + tutorial only; per-channel icons created on first successful switch
  bash "$SCRIPTS/make-desktop-apps.sh" || true
fi

if [[ -f "$HOME/.grok/auth.json" ]]; then
  env -u http_proxy -u https_proxy -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY -u all_proxy \
    "$BIN/supergrok-proxy" restart 2>/dev/null || "$BIN/supergrok-proxy" start 2>/dev/null || true
fi

echo
echo "Install complete (multi-model)."
echo
echo "Profiles:"
KY_CODEX_PROFILES="$CODEX_HOME/ky-profiles.json" "$BIN/codex-provider" list
echo
echo "Next (simple):"
echo "  • Desktop only has 2 icons: 「Codex 切换模型」+「Codex 使用教程」"
echo "  • First time you pick Grok/DeepSeek/... → auto-creates that shortcut on Desktop"
echo "  • Later: click the shortcut to switch in one tap"
echo "  • First API use: dialog for OpenRouter key + tutorial button"
echo "  • After switch: always NEW chat in Codex"
echo
KY_CODEX_PROFILES="$CODEX_HOME/ky-profiles.json" "$BIN/codex-provider" status || true
