# 多宿主安装（同一套 skill，到处能用）

目标：用一条命令安装，在 Codex、Claude Code、豆包、Trae、Grok 等工具里调用 `/ky-x` 等 Skill。

## 原理

```text
~/.ky-skills/skills/ky-x    ← 本机安装目录
        ▲
        │ 软链 / 薄 bridge
        │
~/.agents/skills/ky-x       ← 豆包 / Trae Solo / 通用 Agents
~/.claude/skills/ky-x       ← Claude Code
~/.codex/skills/ky-x        ← Codex
~/.grok/skills/ky-x         ← Grok
~/.trae/skills/ky-x         ← Trae
~/.trae-cn/skills/ky-x      ← Trae 国区
…其他兼容 SKILL.md 的目录
```

改真源 → 所有软链自动看到新版本（无需每端复制粘贴）。

## 推荐安装方式

直接发给支持终端操作的 Agent：

```text
帮我安装这里的 Skills：https://github.com/KirenYi/ky-skills
```

Codex 用户也可以调用 `$skill-installer`，让它从上述仓库安装全部 Skills。

如果 Agent 无法安装，再使用终端命令：

```bash
curl -fsSL https://github.com/KirenYi/ky-skills/raw/main/install.sh|bash
```

这条命令会自动：

1. 下载或更新项目到 `~/.ky-skills`
2. 安装全部可用 Skills
3. 连接到本机常见的 Agent Skills 目录

完成后重启 Agent 即可使用。以后重新执行同一条命令即可更新。

只安装一个 Skill：

```bash
curl -fsSL https://github.com/KirenYi/ky-skills/raw/main/install.sh|bash -s -- ky-x
```

## 手动安装（可选）

```bash
git clone https://github.com/KirenYi/ky-skills.git ~/ky-skills
cd ~/ky-skills
./scripts/install-links.sh
./scripts/install-links.sh --dry-run
```

## 各宿主说明

| 产品 | 常见 skills 路径 | 说明 |
|------|------------------|------|
| 豆包 Mac App | `~/.agents/skills` | 通用 Agents 根目录 |
| Trae Solo / Trae | `~/.agents/skills` 或 `~/.trae/skills` | 以你本机实际为准 |
| Trae 国区 | `~/.trae-cn/skills` | |
| Claude Code | `~/.claude/skills` | |
| Codex | `~/.codex/skills` | 有时也读 `~/.agents/skills` |
| Grok | `~/.grok/skills` | 需能发现 `SKILL.md`；复杂场景可用薄 bridge + `user_invocable: true` |
| Work Buddy 等 | 见该产品文档中的 Agent / Skills 目录 | 若路径已知，可提 Issue 加入 `install-links.sh` |

若某工具不支持 skills 目录：仍可用 **命令行** 跑 `ky-x` 的 Python 模块（见根 README）。

## 升级

```bash
curl -fsSL https://github.com/KirenYi/ky-skills/raw/main/install.sh|bash
```

## 卸载链接（不删仓库）

手动删除各端软链即可，例如：

```bash
rm ~/.agents/skills/ky-x ~/.claude/skills/ky-x ~/.codex/skills/ky-x ~/.grok/skills/ky-x
```

不要删除 `~/.ky-skills` 除非你要卸载整个集合。

## 故障排查

| 现象 | 处理 |
|------|------|
| Agent 找不到 `/ky-x` | 确认软链存在：`ls -la ~/.agents/skills/ky-x`；重启 Agent |
| 改了代码 Agent 仍像旧版 | 确认改的是仓库真源不是副本；`readlink` 检查软链目标 |
| 一端正常另一端没有 | 对该端路径再跑 `install-links.sh`；检查产品是否使用不同 skills 根目录 |
