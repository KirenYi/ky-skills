# 路线图（ky-x）

按「先能用、再变稳、再变强」迭代。

## v0.1（当前）

- [x] 纳入 `ky-skills`  monorepo，调用名 **`/ky-x`**
- [x] Nitter RSS 增量同步  
- [x] 多博主 config，数据目录 `~/.ky-x/`  
- [x] JSONL + 按月 Markdown  
- [x] 过滤转推 / 回复（启发式）  
- [x] Agent `SKILL.md` 工作流  
- [x] 零第三方 Python 依赖  
- [x] `sync --handle`  

## v0.2

- [ ] 一键安装脚本（clone + 软链到 `~/.agents/skills` 等）  
- [x] `output_dir` 默认 `~/.ky-x/data`（init 时写绝对路径）
- [ ] `sync --handle xxx` 只同步一个人  
- [ ] 更稳的镜像列表 / 健康检查命令 `xarchive doctor`  
- [ ] macOS launchd / Linux systemd 示例  

## v0.3

- [ ] 官方 X API fetcher（`source: x_api`）  
- [ ] `backfill --since YYYY-MM-DD`（API）  
- [ ] 配置里按博主覆盖过滤规则的文档与测试  

## v0.4

- [ ] Obsidian / Logseq 友好 frontmatter  
- [ ] 可选：导入第三方 JSONL（知识原子等）  
- [ ] 简单本地搜索：`xarchive search "关键词"`  

## 原则

1. **Skill 说明与脚本一起发版**（改行为必改 `SKILL.md` + changelog）  
2. **默认路径零密钥**；付费能力永远 opt-in  
3. **破坏性变更** bump minor，并在 changelog 写迁移一句  
