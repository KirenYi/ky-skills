#!/usr/bin/env bash
# Link all ky-* skills into as many Agent skill directories as exist on this machine.
# One git clone → many hosts (Claude Code, Codex, Grok, Doubao, Trae, …).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="$ROOT/skills"
DRY_RUN=0

usage() {
  cat <<'EOF'
Usage:
  ./scripts/install-links.sh              # link all skills/ky-*
  ./scripts/install-links.sh ky-x         # link only named skills
  ./scripts/install-links.sh --dry-run    # print actions only

Creates symlinks from each existing host skills directory to the repo source.
Does not copy files. Does not overwrite real (non-symlink) directories.
EOF
}

# Host skill parent dirs (link targets live at $dir/<skill-name>).
# Only used when the parent directory already exists OR is a well-known primary.
HOST_SKILL_PARENTS=(
  "$HOME/.agents/skills"          # 豆包 / Trae Solo / generic agents
  "$HOME/.claude/skills"          # Claude Code
  "$HOME/.codex/skills"           # Codex
  "$HOME/.grok/skills"            # Grok
  "$HOME/.trae/skills"            # Trae
  "$HOME/.trae-cn/skills"         # Trae CN
  "$HOME/.codebuddy/skills"     # CodeBuddy (if present)
  "$HOME/.continue/skills"
  "$HOME/.cursor/skills"
  "$HOME/.windsurf/skills"
  "$HOME/.codeium/windsurf/skills"
  "$HOME/.qwen/skills"
  "$HOME/.iflow/skills"
  "$HOME/.lingma/skills"
  "$HOME/.augment/skills"
  "$HOME/.openhands/skills"
  "$HOME/.config/goose/skills"
)

# Primary dirs we may create if missing (core multi-host set).
PRIMARY_CREATE=(
  "$HOME/.agents/skills"
  "$HOME/.claude/skills"
  "$HOME/.codex/skills"
  "$HOME/.grok/skills"
)

ARGS=()
for a in "$@"; do
  case "$a" in
    -h|--help) usage; exit 0 ;;
    --dry-run) DRY_RUN=1 ;;
    *) ARGS+=("$a") ;;
  esac
done

link_one_into() {
  local name="$1"
  local parent="$2"
  local src="$SKILLS_DIR/$name"
  local target="$parent/$name"

  if [[ ! -d "$src" ]]; then
    echo "skip missing source: $src" >&2
    return 1
  fi
  if [[ ! -f "$src/SKILL.md" ]]; then
    echo "skip (no SKILL.md): $src" >&2
    return 1
  fi

  if [[ ! -d "$parent" ]]; then
    return 0
  fi

  if [[ -e "$target" || -L "$target" ]]; then
    if [[ -L "$target" ]]; then
      if [[ "$DRY_RUN" -eq 1 ]]; then
        echo "DRY update link $target -> $src"
      else
        ln -sfn "$src" "$target"
        echo "updated $target -> $src"
      fi
    else
      echo "CONFLICT (real file/dir, not linking): $target" >&2
      return 1
    fi
  else
    if [[ "$DRY_RUN" -eq 1 ]]; then
      echo "DRY link $target -> $src"
    else
      ln -sfn "$src" "$target"
      echo "linked $target -> $src"
    fi
  fi
}

ensure_primary_parents() {
  local p
  for p in "${PRIMARY_CREATE[@]}"; do
    if [[ ! -d "$p" ]]; then
      if [[ "$DRY_RUN" -eq 1 ]]; then
        echo "DRY mkdir $p"
      else
        mkdir -p "$p"
        echo "mkdir $p"
      fi
    fi
  done
}

list_skill_names() {
  if [[ ${#ARGS[@]} -gt 0 ]]; then
    printf '%s\n' "${ARGS[@]}"
    return
  fi
  local d
  for d in "$SKILLS_DIR"/ky-*; do
    [[ -d "$d" ]] || continue
    basename "$d"
  done
}

ensure_primary_parents

echo "Source root: $SKILLS_DIR"
echo "---"

names=()
while IFS= read -r n; do
  [[ -n "$n" ]] && names+=("$n")
done < <(list_skill_names)

if [[ ${#names[@]} -eq 0 ]]; then
  echo "No skills to link under $SKILLS_DIR" >&2
  exit 1
fi

for name in "${names[@]}"; do
  echo "# skill: $name"
  for parent in "${HOST_SKILL_PARENTS[@]}"; do
    # Link only if parent exists (primary ones were just created)
    if [[ -d "$parent" ]]; then
      link_one_into "$name" "$parent" || true
    fi
  done
  echo
done

echo "done."
echo "Tip: restart your Agent app if /ky-x does not appear immediately."
