# 多工具协作指南

适用对象：会改本仓库的 **人类** 与 **Agent**（Claude Code、Codex、Grok、Cursor 等）。

## 为什么需要这个文件

同一仓库会被多个 Agent「接力」修改。若进度只留在各自聊天窗口，后一个工具会：

- 重复劳动
- 覆盖前一个未完成的设计
- 在 bridge 副本上改出分叉

因此约定：**进度落盘到 `docs/PROGRESS.md`，规则落盘到 `AGENTS.md`。**

## 推荐工作流（给 Agent）

```text
pull / status
  → 读 AGENTS.md
  → 读 docs/PROGRESS.md（最新 1～3 条）
  → 做任务（只动真源 skills/ 与文档）
  → 本地验证
  → 写 PROGRESS 新条目
  → commit（用户要求时 push）
```

## 推荐工作流（给人类）

1. 用任意 Agent 前：`git pull`
2. 让 Agent 改完后检查 `docs/PROGRESS.md` 是否有新记录
3. Code review 以 `skills/` 与测试为准，不要 review 各端 `~/.*/skills` 副本
4. 发布：push `main`；用户侧 `git pull` + 必要时重跑 `./scripts/install-links.sh`

## 「进行中」任务怎么占坑

在 `docs/PROGRESS.md` 顶部写一条，标题带 **WIP**：

```markdown
## 2026-07-12 — Codex — WIP: ky-x 官方 API fetcher

- **操作者**：Codex
- **目标**：…
- **未完成 / 下一步**：正在实现 fetchers/x_api.py
```

其他 Agent 看到 **WIP** 且时间很近，应避开同一文件集合，或先沟通。

完成后把标题里的 `WIP` 去掉，补上「已完成」。

## 禁止

- 在未读 PROGRESS 的情况下大规模重构
- force push `main`（除非人类明确要求）
- 把用户的 `~/.ky-x` 数据拷进仓库
- 在 `~/.claude/skills/ky-x` 里直接改文件当开发（应改仓库真源）
