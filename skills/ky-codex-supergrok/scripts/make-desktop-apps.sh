#!/usr/bin/env bash
# Create double-clickable macOS apps for multi-profile Codex switching.
set -euo pipefail
BIN="${CODEX_BIN_DIR:-$HOME/.codex/bin}"
DESTS=("$HOME/Desktop" "$HOME/Applications")
PROFILES_JSON="${1:-$BIN/../ky-profiles.json}"
if [[ ! -f "$PROFILES_JSON" ]]; then
  # fallback next to installed skill scripts copy
  for c in \
    "$HOME/.codex/ky-profiles.json" \
    "$(cd "$(dirname "$0")" && pwd)/profiles.json"
  do
    [[ -f "$c" ]] && PROFILES_JSON="$c" && break
  done
fi

make_app() {
  local name="$1" mode="$2" dest_root="$3"
  local app="$dest_root/${name}.app"
  rm -rf "$app"
  mkdir -p "$app/Contents/MacOS" "$app/Contents/Resources"
  cat > "$app/Contents/Info.plist" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>CFBundleExecutable</key><string>launcher</string>
  <key>CFBundleIdentifier</key><string>local.ky.codex.provider.${mode}</string>
  <key>CFBundleName</key><string>${name}</string>
  <key>CFBundlePackageType</key><string>APPL</string>
  <key>CFBundleShortVersionString</key><string>2.0</string>
  <key>LSUIElement</key><true/>
  <key>NSHighResolutionCapable</key><true/>
</dict>
</plist>
PLIST
  cat > "$app/Contents/MacOS/launcher" <<LAUNCH
#!/usr/bin/env bash
exec "$BIN/codex-provider-app-run" "${mode}"
LAUNCH
  chmod 755 "$app/Contents/MacOS/launcher"
  xattr -cr "$app" 2>/dev/null || true
  echo "created $app"
}

for dest in "${DESTS[@]}"; do
  mkdir -p "$dest"
  # Master picker first
  make_app "Codex 切换模型" "pick" "$dest"
  make_app "Codex → OpenAI" "openai" "$dest"
  make_app "Codex → Grok" "grok" "$dest"
  make_app "Codex → Claude" "claude" "$dest"
  make_app "Codex → DeepSeek" "deepseek" "$dest"
  make_app "Codex → Gemini" "gemini" "$dest"
done
