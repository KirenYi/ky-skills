#!/usr/bin/env bash
# Link all ky-* skills into common Agent skill directories.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="$ROOT/skills"

link_one() {
  local name="$1"
  local src="$SKILLS_DIR/$name"
  local targets=(
    "$HOME/.agents/skills/$name"
    "$HOME/.claude/skills/$name"
    "$HOME/.codex/skills/$name"
    "$HOME/.grok/skills/$name"
  )
  for t in "${targets[@]}"; do
    mkdir -p "$(dirname "$t")"
    ln -sfn "$src" "$t"
    echo "linked $t -> $src"
  done
}

if [[ $# -gt 0 ]]; then
  for name in "$@"; do
    link_one "$name"
  done
else
  for d in "$SKILLS_DIR"/ky-*; do
    [[ -d "$d" ]] || continue
    link_one "$(basename "$d")"
  done
fi

echo "done."
