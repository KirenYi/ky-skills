#!/usr/bin/env bash
# Create only the essential macOS switcher apps (keep desktop clean).
set -euo pipefail
BIN="${CODEX_BIN_DIR:-$HOME/.codex/bin}"
DESTS=("$HOME/Desktop" "$HOME/Applications")

make_app() {
  local name="$1" mode="$2" dest_root="$3"
  local app="$dest_root/${name}.app"
  rm -rf "$app"
  mkdir -p "$app/Contents/MacOS"
  cat > "$app/Contents/Info.plist" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>CFBundleExecutable</key><string>launcher</string>
  <key>CFBundleIdentifier</key><string>local.ky.codex.provider.${mode}</string>
  <key>CFBundleName</key><string>${name}</string>
  <key>CFBundlePackageType</key><string>APPL</string>
  <key>CFBundleShortVersionString</key><string>3.1</string>
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

# Remove legacy per-model shortcuts if present (Claude/DeepSeek/Gemini/.command)
cleanup_legacy() {
  local dest="$1"
  rm -rf \
    "$dest/Codex → Claude.app" \
    "$dest/Codex → DeepSeek.app" \
    "$dest/Codex → Gemini.app" \
    "$dest/Codex → claude.app" \
    2>/dev/null || true
  rm -f "$dest"/Codex*.command "$dest"/Codex→*.command 2>/dev/null || true
}

for dest in "${DESTS[@]}"; do
  mkdir -p "$dest"
  cleanup_legacy "$dest"
  # Only 5 apps — keep the desktop simple
  make_app "Codex 切换模型" "pick" "$dest"
  make_app "Codex 使用教程" "tutorial" "$dest"
  make_app "Codex → OpenAI" "openai" "$dest"
  make_app "Codex → Grok" "grok" "$dest"
  make_app "Codex → API合集" "api" "$dest"
done
