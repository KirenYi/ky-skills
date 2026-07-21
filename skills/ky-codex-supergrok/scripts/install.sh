#!/usr/bin/env bash
# Install SuperGrok ↔ Codex bridge on this machine.
# Does NOT use console.x.ai paid API keys. Uses `grok login` SuperGrok session.
set -euo pipefail

SKILL_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SCRIPTS="$SKILL_ROOT/scripts"
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
BIN="$CODEX_HOME/bin"

echo "== ky-codex-supergrok install =="
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

# Fix app-run / provider to use installed paths (they already use $HOME/.codex/bin)
python3 "$SCRIPTS/generate-catalog.py" "$CODEX_HOME/model-catalogs/xai-models.json"

# Ensure provider block exists once (switcher manages model keys)
if ! grep -q '\[model_providers\.xai\]' "$CODEX_HOME/config.toml" 2>/dev/null; then
  mkdir -p "$CODEX_HOME"
  touch "$CODEX_HOME/config.toml"
  cat >> "$CODEX_HOME/config.toml" <<'TOML'

# --- ky-codex-supergrok provider (subscription SuperGrok, no API key) ---
[model_providers.xai]
name = "xAI SuperGrok"
base_url = "http://127.0.0.1:18765/v1"
wire_api = "responses"
request_max_retries = 4
stream_idle_timeout_ms = 600000
supports_websockets = false

[profiles.xai]
model = "grok-4.5"
model_provider = "xai"
model_reasoning_effort = "high"
model_catalog_json = "~/.codex/model-catalogs/xai-models.json"
TOML
  echo "appended [model_providers.xai] to config.toml"
else
  echo "model_providers.xai already present"
fi

# Write layered profile file
cat > "$CODEX_HOME/xai.config.toml" <<'TOML'
# codex --profile xai
model = "grok-4.5"
model_provider = "xai"
model_reasoning_effort = "high"
model_catalog_json = "~/.codex/model-catalogs/xai-models.json"
TOML

# Desktop apps (macOS)
if [[ "$(uname -s)" == "Darwin" ]]; then
  bash "$SCRIPTS/make-desktop-apps.sh" || true
fi

# Start proxy if grok auth exists
if [[ -f "$HOME/.grok/auth.json" ]]; then
  env -u http_proxy -u https_proxy -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY -u all_proxy \
    "$BIN/supergrok-proxy" restart || "$BIN/supergrok-proxy" start || true
  # Default to grok mode without forcing restart of ChatGPT during install
  NO_RESTART=1 "$BIN/codex-provider" grok || true
else
  echo
  echo "NOTE: ~/.grok/auth.json not found."
  echo "      Install Grok Build CLI and run:  grok login"
  echo "      Then:  ~/.codex/bin/supergrok-proxy start"
  echo "             ~/.codex/bin/codex-provider grok"
fi

echo
echo "Install complete."
echo
echo "Next:"
echo "  1) grok login          # SuperGrok subscription (not API key)"
echo "  2) ~/.codex/bin/supergrok-proxy start"
echo "  3) Double-click Desktop app:  Codex → Grok   or   Codex → OpenAI"
echo "     CLI:  ~/.codex/bin/codex-provider grok|openai|toggle|status"
echo "  4) Restart ChatGPT/Codex Desktop and open a NEW chat"
echo
echo "Status:"
"$BIN/codex-provider" status || true
