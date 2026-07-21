#!/usr/bin/env bash
# Only the main hub app. Tutorial is inside the menu. Channel shortcuts on first use.
set -euo pipefail
BIN="${CODEX_BIN_DIR:-$HOME/.codex/bin}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ICON_SRC="$SCRIPT_DIR/assets/CodexSwitch.icns"
ICON_DST="${CODEX_HOME:-$HOME/.codex}/bin/CodexSwitch.icns"
DESTS=("$HOME/Desktop" "$HOME/Applications")

if [[ -f "$ICON_SRC" ]]; then
  mkdir -p "$(dirname "$ICON_DST")"
  cp "$ICON_SRC" "$ICON_DST"
fi

make_app() {
  local name="$1" mode="$2" dest_root="$3"
  local app="$dest_root/${name}.app"
  rm -rf "$app"
  mkdir -p "$app/Contents/MacOS" "$app/Contents/Resources"
  if [[ -f "$ICON_DST" ]]; then
    cp "$ICON_DST" "$app/Contents/Resources/AppIcon.icns"
  elif [[ -f "$ICON_SRC" ]]; then
    cp "$ICON_SRC" "$app/Contents/Resources/AppIcon.icns"
  fi
  cat > "$app/Contents/Info.plist" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>CFBundleExecutable</key><string>launcher</string>
  <key>CFBundleIdentifier</key><string>local.ky.codex.provider.${mode}</string>
  <key>CFBundleName</key><string>${name}</string>
  <key>CFBundleDisplayName</key><string>${name}</string>
  <key>CFBundlePackageType</key><string>APPL</string>
  <key>CFBundleShortVersionString</key><string>5.0</string>
  <key>CFBundleIconFile</key><string>AppIcon</string>
  <key>LSUIElement</key><false/>
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
  # touch to refresh Finder icon cache
  touch "$app"
  echo "created $app"
}

# Remove obsolete hub/tutorial/channel preseeds (keep user first-use shortcuts tracked separately)
cleanup_obsolete() {
  local dest="$1"
  rm -rf \
    "$dest/Codex 使用教程.app" \
    "$dest/Codex→使用教程.app" \
    2>/dev/null || true
  rm -f "$dest"/Codex*.command 2>/dev/null || true
}

for dest in "${DESTS[@]}"; do
  mkdir -p "$dest"
  cleanup_obsolete "$dest"
  make_app "Codex 切换模型" "pick" "$dest"
done

echo "Hub app ready (tutorial lives inside the menu)."
