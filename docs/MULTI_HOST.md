# 多宿主安装（同一套 skill，到处能用）

目标：用户 **只 clone 一份** `ky-skills`，在 Codex、Claude Code、豆包、Trae、Grok 等工具里都能调用 `/ky-x` 等 skill。

## 原理

```text
~/ky-skills/skills/ky-x     ← 唯一真源（git）
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

## 一键安装

```bash
git clone https://github.com/KirenYi/ky-skills.git ~/ky-skills
cd ~/ky-skills
./scripts/install-links.sh
```

脚本会对**本机已存在的** skills 父目录创建软链；目录不存在则跳过（避免误建混乱结构）。

只安装一个 skill：

```bash
./scripts/install-links.sh ky-x
```

查看将链接到哪些位置：

```bash
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
cd ~/ky-skills
git pull
./scripts/install-links.sh   # 新 skill 会补链；旧链仍指向真源
```

## 卸载链接（不删仓库）

手动删除各端软链即可，例如：

```bash
rm ~/.agents/skills/ky-x ~/.claude/skills/ky-x ~/.codex/skills/ky-x ~/.grok/skills/ky-x
```

不要删除 `~/ky-skills` 除非你要卸载整个集合。

## 故障排查

| 现象 | 处理 |
|------|------|
| Agent 找不到 `/ky-x` | 确认软链存在：`ls -la ~/.agents/skills/ky-x`；重启 Agent |
| 改了代码 Agent 仍像旧版 | 确认改的是仓库真源不是副本；`readlink` 检查软链目标 |
| 一端正常另一端没有 | 对该端路径再跑 `install-links.sh`；检查产品是否使用不同 skills 根目录 |
