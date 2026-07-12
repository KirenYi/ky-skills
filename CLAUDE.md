# CLAUDE.md — Claude Code 兼容层

本项目的**共同规则真源**是仓库根目录的 [`AGENTS.md`](./AGENTS.md)。

Claude Code 在本仓库工作时：

1. **先读** `AGENTS.md`
2. **再读** `docs/PROGRESS.md`（同步其他工具留下的进度）
3. 修改 skill 时以 `skills/<name>/SKILL.md` 与其 `scripts/` 为真源
4. 收工更新 `docs/PROGRESS.md`
5. 多端安装使用 `./scripts/install-links.sh`，不要复制 skill 到 `~/.claude/skills` 后在副本上开发

Claude 专属提示（若有）只写在本文件；通用协作规则只维护在 `AGENTS.md`。
