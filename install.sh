#!/usr/bin/env bash
# One-command installer for ky-skills.
set -euo pipefail

REPO_URL="${KY_SKILLS_REPO_URL:-https://github.com/KirenYi/ky-skills.git}"
ARCHIVE_URL="${KY_SKILLS_ARCHIVE_URL:-https://github.com/KirenYi/ky-skills/archive/refs/heads/main.tar.gz}"
INSTALL_DIR="${KY_SKILLS_INSTALL_DIR:-${HOME:-}/.ky-skills}"
FORCE_ARCHIVE="${KY_SKILLS_FORCE_ARCHIVE:-0}"
INSTALLER_TMP=""
INSTALLER_BACKUP=""

info() {
  printf '%s\n' "$*"
}

fail() {
  printf '安装失败：%s\n' "$*" >&2
  exit 1
}

require_command() {
  command -v "$1" >/dev/null 2>&1 || fail "缺少命令 $1"
}

cleanup() {
  local status=$?
  set +e

  if [[ "$status" -ne 0 && -n "$INSTALLER_BACKUP" && -e "$INSTALLER_BACKUP" ]]; then
    if [[ -e "$INSTALL_DIR" ]]; then
      mv "$INSTALL_DIR" "${INSTALL_DIR}.failed.$$"
    fi
    mv "$INSTALLER_BACKUP" "$INSTALL_DIR"
    printf '%s\n' "已恢复安装前的版本。" >&2
  fi

  if [[ -n "$INSTALLER_TMP" && -d "$INSTALLER_TMP" ]]; then
    rm -rf -- "$INSTALLER_TMP"
  fi

  if [[ "$status" -eq 0 && -n "$INSTALLER_BACKUP" && -d "$INSTALLER_BACKUP" ]]; then
    rm -rf -- "$INSTALLER_BACKUP"
  fi

  exit "$status"
}
trap cleanup EXIT

install_from_archive() {
  require_command curl
  require_command tar

  INSTALLER_TMP="$(mktemp -d "${TMPDIR:-/tmp}/ky-skills-install.XXXXXX")"
  mkdir -p "$INSTALLER_TMP/source"

  info "正在下载……"
  curl -fsSL "$ARCHIVE_URL" -o "$INSTALLER_TMP/source.tar.gz"
  tar -xzf "$INSTALLER_TMP/source.tar.gz" -C "$INSTALLER_TMP/source" --strip-components=1

  [[ -x "$INSTALLER_TMP/source/scripts/install-links.sh" ]] || \
    fail "下载内容不完整，请稍后重试"

  mkdir -p "$(dirname "$INSTALL_DIR")"
  if [[ -e "$INSTALL_DIR" ]]; then
    INSTALLER_BACKUP="${INSTALL_DIR}.backup.$$"
    mv "$INSTALL_DIR" "$INSTALLER_BACKUP"
  fi
  mv "$INSTALLER_TMP/source" "$INSTALL_DIR"
}

[[ -n "${HOME:-}" ]] || fail "无法确定用户目录"
case "$INSTALL_DIR" in
  ""|"/"|"$HOME") fail "安装目录不安全：$INSTALL_DIR" ;;
esac
[[ ! -L "$INSTALL_DIR" ]] || fail "安装目录不能是软链接：$INSTALL_DIR"

info "正在安装 ky-skills……"

if [[ -d "$INSTALL_DIR/.git" ]]; then
  require_command git
  git -C "$INSTALL_DIR" pull --ff-only --quiet
elif [[ -e "$INSTALL_DIR" ]]; then
  install_from_archive
elif [[ "$FORCE_ARCHIVE" != "1" ]] && command -v git >/dev/null 2>&1; then
  git clone --depth 1 --quiet "$REPO_URL" "$INSTALL_DIR"
else
  install_from_archive
fi

"$INSTALL_DIR/scripts/install-links.sh" --quiet "$@"

if [[ "$#" -eq 0 ]]; then
  info "完成。请重启 Agent，然后输入 /ky-x /ky-dy /ky-xhs /ky-sph /ky-xdraft /ky-mphtml。"
else
  installed_commands=""
  for skill_name in "$@"; do
    installed_commands="${installed_commands} /${skill_name}"
  done
  info "完成。请重启 Agent，然后调用：${installed_commands# }"
fi
