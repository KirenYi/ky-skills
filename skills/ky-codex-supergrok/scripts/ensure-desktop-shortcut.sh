#!/usr/bin/env bash
# Create a desktop (+ Applications) one-click app for a profile after first successful use.
# Usage: ensure-desktop-shortcut.sh <profile_id> [display_name]
set -euo pipefail
PID="${1:-}"
LABEL="${2:-}"
[[ -n "$PID" ]] || exit 0
# Never create shortcuts for hub-only pseudo modes
case "$PID" in
  pick|tutorial|help|menu|__tutorial__) exit 0 ;;
esac

BIN="${CODEX_BIN_DIR:-$HOME/.codex/bin}"
PROFILES="${KY_CODEX_PROFILES:-$HOME/.codex/ky-profiles.json}"

if [[ -z "$LABEL" && -f "$PROFILES" ]]; then
  LABEL=$(python3 -c "import json;from pathlib import Path;d=json.loads(Path(r'''$PROFILES''').read_text());print(d['profiles'].get(r'''$PID''',{}).get('label') or r'''$PID''')" 2>/dev/null || echo "$PID")
fi
LABEL="${LABEL:-$PID}"

# Short desktop name: Codex → <short>
short=$(python3 -c "
pid=r'''$PID'''
label=r'''$LABEL'''
# prefer short names for known ids
m={
  'openai':'OpenAI',
  'grok':'Grok',
  'api':'API合集',
  'claude':'Claude',
  'claude-opus':'Claude Opus',
  'deepseek':'DeepSeek',
  'deepseek-r1':'DeepSeek R1',
  'gemini':'Gemini',
  'relay':'中转站',
}
print(m.get(pid) or label.split('（')[0].split('(')[0].strip()[:16])
")
APP_NAME="Codex → ${short}"

make_one() {
  local dest_root="$1"
  local app="$dest_root/${APP_NAME}.app"
  mkdir -p "$app/Contents/MacOS" "$app/Contents/Resources"
  ICON="$BIN/CodexSwitch.icns"
  if [[ -f "$ICON" ]]; then cp "$ICON" "$app/Contents/Resources/AppIcon.icns"; fi
  # stable id from profile
  local bid="local.ky.codex.provider.shortcut.${PID}"
  cat > "$app/Contents/Info.plist" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>CFBundleExecutable</key><string>launcher</string>
  <key>CFBundleIdentifier</key><string>${bid}</string>
  <key>CFBundleName</key><string>${APP_NAME}</string>
  <key>CFBundlePackageType</key><string>APPL</string>
  <key>CFBundleShortVersionString</key><string>5.0</string>
  <key>CFBundleIconFile</key><string>AppIcon</string>
  <key>LSUIElement</key><false/>
</dict>
</plist>
PLIST
  cat > "$app/Contents/MacOS/launcher" <<LAUNCH
#!/usr/bin/env bash
exec "$BIN/codex-provider-app-run" "${PID}"
LAUNCH
  chmod 755 "$app/Contents/MacOS/launcher"
  xattr -cr "$app" 2>/dev/null || true
}

CREATED=0
for dest in "$HOME/Desktop" "$HOME/Applications"; do
  mkdir -p "$dest"
  target="$dest/${APP_NAME}.app"
  if [[ -d "$target" ]]; then
    # refresh launcher in case bin path changed
    make_one "$dest"
  else
    make_one "$dest"
    CREATED=1
  fi
done

# track created shortcuts
TRACK="$HOME/.codex/ky-desktop-shortcuts.txt"
mkdir -p "$HOME/.codex"
grep -qxF "$PID" "$TRACK" 2>/dev/null || echo "$PID" >>"$TRACK"

if [[ "$CREATED" == "1" ]]; then
  osascript -e "display notification \"下次可直接点「${APP_NAME}」秒切\" with title \"已生成桌面快捷方式\"" 2>/dev/null || true
  echo "desktop shortcut created: ${APP_NAME}"
else
  echo "desktop shortcut refreshed: ${APP_NAME}"
fi
