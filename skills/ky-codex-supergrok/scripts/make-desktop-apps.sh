#!/usr/bin/env bash
# Only install the hub apps. Per-channel desktop shortcuts are created on first use.
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
  <key>CFBundleShortVersionString</key><string>4.0</string>
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

cleanup_all_channel_shortcuts() {
  local dest="$1"
  # Remove pre-seeded / legacy channel icons (kept list is only hub + tutorial)
  rm -rf \
    "$dest/Codex → OpenAI.app" \
    "$dest/Codex → Grok.app" \
    "$dest/Codex → API合集.app" \
    "$dest/Codex → Claude.app" \
    "$dest/Codex → DeepSeek.app" \
    "$dest/Codex → Gemini.app" \
    "$dest/Codex → claude-opus.app" \
    "$dest/Codex → deepseek-r1.app" \
    2>/dev/null || true
  rm -f "$dest"/Codex*.command "$dest"/Codex→*.command 2>/dev/null || true
}

for dest in "${DESTS[@]}"; do
  mkdir -p "$dest"
  # Do NOT wipe user-created channel shortcuts on reinstall — only remove if KY_CODEX_RESET_SHORTCUTS=1
  if [[ "${KY_CODEX_RESET_SHORTCUTS:-0}" == "1" ]]; then
    cleanup_all_channel_shortcuts "$dest"
  else
    # still remove old .command clutter
    rm -f "$dest"/Codex*.command 2>/dev/null || true
  fi
  make_app "Codex 切换模型" "pick" "$dest"
  make_app "Codex 使用教程" "tutorial" "$dest"
done

echo "Hub apps ready. Channel shortcuts appear after first successful switch."
