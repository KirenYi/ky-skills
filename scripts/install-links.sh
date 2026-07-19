#!/usr/bin/env bash
# Link all ky-* skills into as many Agent skill directories as exist on this machine.
# One git clone → many hosts (Claude Code, Codex, Grok, Doubao, Trae, …).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="$ROOT/skills"
HOST_HOME="${KY_SKILLS_HOST_HOME:-$HOME}"
DRY_RUN=0
QUIET=0
LINK_COUNT=0
CONFLICT_COUNT=0

usage() {
  cat <<'EOF'
Usage:
  ./scripts/install-links.sh              # link all skills/ky-*
  ./scripts/install-links.sh ky-x         # link only named skills
  ./scripts/install-links.sh --dry-run    # print actions only
  ./scripts/install-links.sh --quiet      # only print the result

Creates symlinks from each existing host skills directory to the repo source.
Does not copy files. Does not overwrite real (non-symlink) directories.
EOF
}

log() {
  if [[ "$QUIET" -eq 0 ]]; then
    echo "$*"
  fi
}

# Host skill parent dirs (link targets live at $dir/<skill-name>).
# Only used when the parent directory already exists OR is a well-known primary.
HOST_SKILL_PARENTS=(
  "$HOST_HOME/.agents/skills"          # 豆包 / Trae Solo / generic agents
  "$HOST_HOME/.claude/skills"          # Claude Code
  "$HOST_HOME/.codex/skills"           # Codex
  "$HOST_HOME/.grok/skills"            # Grok
  "$HOST_HOME/.trae/skills"            # Trae
  "$HOST_HOME/.trae-cn/skills"         # Trae CN
  "$HOST_HOME/.codebuddy/skills"       # CodeBuddy (if present)
  "$HOST_HOME/.continue/skills"
  "$HOST_HOME/.cursor/skills"
  "$HOST_HOME/.windsurf/skills"
  "$HOST_HOME/.codeium/windsurf/skills"
  "$HOST_HOME/.qwen/skills"
  "$HOST_HOME/.iflow/skills"
  "$HOST_HOME/.lingma/skills"
  "$HOST_HOME/.augment/skills"
  "$HOST_HOME/.openhands/skills"
  "$HOST_HOME/.config/goose/skills"
)

# Primary dirs we may create if missing (core multi-host set).
PRIMARY_CREATE=(
  "$HOST_HOME/.agents/skills"
  "$HOST_HOME/.claude/skills"
  "$HOST_HOME/.codex/skills"
  "$HOST_HOME/.grok/skills"
)

ARGS=()
for a in "$@"; do
  case "$a" in
    -h|--help) usage; exit 0 ;;
    --dry-run) DRY_RUN=1 ;;
    --quiet) QUIET=1 ;;
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
        log "DRY update link $target -> $src"
      else
        ln -sfn "$src" "$target"
        log "updated $target -> $src"
      fi
      LINK_COUNT=$((LINK_COUNT + 1))
    else
      echo "CONFLICT (real file/dir, not linking): $target" >&2
      CONFLICT_COUNT=$((CONFLICT_COUNT + 1))
      return 1
    fi
  else
    if [[ "$DRY_RUN" -eq 1 ]]; then
      log "DRY link $target -> $src"
    else
      ln -sfn "$src" "$target"
      log "linked $target -> $src"
    fi
    LINK_COUNT=$((LINK_COUNT + 1))
  fi
}

ensure_primary_parents() {
  local p
  for p in "${PRIMARY_CREATE[@]}"; do
    if [[ ! -d "$p" ]]; then
      if [[ "$DRY_RUN" -eq 1 ]]; then
        log "DRY mkdir $p"
      else
        mkdir -p "$p"
        log "mkdir $p"
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

log "Source root: $SKILLS_DIR"
log "---"

names=()
while IFS= read -r n; do
  [[ -n "$n" ]] && names+=("$n")
done < <(list_skill_names)

if [[ ${#names[@]} -eq 0 ]]; then
  echo "No skills to link under $SKILLS_DIR" >&2
  exit 1
fi

for name in "${names[@]}"; do
  log "# skill: $name"
  for parent in "${HOST_SKILL_PARENTS[@]}"; do
    # Link only if parent exists (primary ones were just created)
    if [[ -d "$parent" ]]; then
      link_one_into "$name" "$parent" || true
    fi
  done
  log ""
done

echo "已安装 ${#names[@]} 个 Skill，创建或更新 $LINK_COUNT 个链接。"
if [[ "$CONFLICT_COUNT" -gt 0 ]]; then
  echo "有 $CONFLICT_COUNT 个目录存在同名文件，已跳过；请查看上方提示。" >&2
fi
if [[ "$QUIET" -eq 0 ]]; then
  echo "如果 Agent 暂时找不到 Skill，请重启应用。"
fi
