# AGENTS.md — 多 Agent 协作总则（真源）

> 本文件是 **Claude Code / Codex / Grok / 豆包 / Trae / 其他 Agent** 操作本仓库时的**共同规则**。  
> 改项目行为前先读本文件；宿主专属说明见 `CLAUDE.md`（若存在）等薄兼容层。

**作者**：Kiren Yi（KY）  
**仓库**：https://github.com/KirenYi/ky-skills  
**前缀**：所有 skill 以 `ky-` 开头  

---

## 1. 这是什么项目

`ky-skills` 是 **Kiren Yi 的个人 Agent Skill 集合**，不是单一脚本仓库。

- 当前（v0.5.0）已发布：`ky-x`、`ky-dy`、`ky-xhs`、`ky-sph`、`ky-xdraft`、`ky-mphtml`、`ky-codex-switch`  
- 命名原则：**短命令 + description 只写核心能力**  
- **对外表述**：只写 KY 自有能力与用法；禁止把第三方仓库写成「本 skill 组件 / 强制依赖」；借鉴方法论可以，挂靠、整包转贴、冒充自有实现不可以
- 之后会有更多 `ky-*` skill，全部放在 `skills/` 下
- 用户装一次集合后，应能在 **多个终端 / 多个 Agent 产品** 里用同一套 skill

---

## 2. 真源（Source of Truth）

| 内容 | 真源位置 | 禁止 |
|------|----------|------|
| Skill 逻辑与说明 | `skills/<name>/`（尤其 `SKILL.md` + `scripts/`） | 在 `~/.claude/skills` 等 bridge 里改长期逻辑 |
| 多 Agent 协作规则 | **本文件 `AGENTS.md`** | 各端各写一套互相矛盾的规则 |
| 进度 / 交接 | `docs/PROGRESS.md` | 只写在聊天里不落盘 |
| 产品说明（给人） | `README.md` | 与 AGENTS 冲突时以代码+AGENTS 为准，再回写 README |
| 用户运行时数据 | 用户本机 `~/.ky-x/` 等 | **永不提交** 用户归档、token、私有 config |

详细见 [`SOURCE_OF_TRUTH.md`](./SOURCE_OF_TRUTH.md)。

---

## 3. 多 Agent 同时操作时的纪律

本仓库会被 **多个工具交替修改**（Grok、Claude Code、Codex 等）。为避免互相踩踏：

### 3.1 开工前（必做）

1. `git status` + `git pull`（有 remote 时）
2. 读 **`docs/PROGRESS.md`** 最新条目
3. 读本 `AGENTS.md` 相关章节
4. 若改某个 skill，先读该 skill 的 `SKILL.md`

### 3.2 干活中

1. **小步提交**：一个意图一个 commit，完整句子写清 why
2. **不改无关文件**：不做顺手大重构
3. **不覆盖他人未提交工作**：发现陌生未提交改动先停，写入 PROGRESS 询问
4. **脚本优于口头约定**：安装、桥接用 `scripts/`，不要每次重写 one-off 命令

### 3.3 收工前（必做）

1. 更新 **`docs/PROGRESS.md`**：做了什么、改了哪些路径、下一步建议、风险
2. 若改了对外行为：同步 `README.md` / skill `VERSION` / `references/changelog.md`
3. 能跑的冒烟测试要跑（至少 `python3 -m xarchive --help` 或对应 skill 的最小命令）
4. 需要发布时：`git push`（仅在用户明确要求或本会话已授权推送时）

### 3.4 冲突处理

| 情况 | 做法 |
|------|------|
| 与 `docs/PROGRESS.md` 中「进行中」任务重叠 | 不要抢；在 PROGRESS 留言或换任务 |
| merge 冲突 | 保留真源目录完整性；优先人工理解后再合 |
| bridge 与真源不一致 | **以 `skills/` 真源为准**，重建软链 |

---

## 4. 多端安装原则（用户侧）

用户应只维护 **一份 git 仓库真源**，各 Agent 通过 **软链 / 薄 bridge** 引用：

| 宿主 | 典型 skill 目录 | 方式 |
|------|-----------------|------|
| 通用 Agents（豆包 Mac、Trae Solo、部分 Codex） | `~/.agents/skills/<name>` | 软链 → 仓库 `skills/<name>` |
| Claude Code | `~/.claude/skills/<name>` | 软链 |
| Codex | `~/.codex/skills/<name>` | 软链 |
| Grok | `~/.grok/skills/<name>` | 软链或含 `user_invocable: true` 的薄 bridge |
| Trae / Trae CN | `~/.trae/skills`、`~/.trae-cn/skills` | 软链 |
| 其他兼容 SKILL.md 的工具 | 其文档中的 skills 目录 | 软链到同一真源 |

一键安装：

```bash
./scripts/install-links.sh          # 全部 ky-*
./scripts/install-links.sh ky-x     # 仅一个
```

**禁止**：把 skill 复制多份到各端再分别修改 → 必分叉。

详见 [`docs/MULTI_HOST.md`](./docs/MULTI_HOST.md)。

---

## 5. 新增 skill 的规范

1. 目录名 = 调用名 = `ky-<短名>`
2. 必须有 `skills/ky-<短名>/SKILL.md`（含 frontmatter `name` + `description` + 触发词）
3. 可选 `scripts/`、`references/`、`VERSION`
4. 更新根 `README.md` skill 表
5. 在 `docs/PROGRESS.md` 记一笔
6. 跑 `./scripts/install-links.sh ky-<短名>` 验证可链

骨架：`templates/skill-skeleton/`

---

## 6. 安全与隐私

- 不提交 API Key、Cookie、Bearer Token
- 不提交 `~/.ky-x/` 或任何用户归档数据
- 公开镜像抓取仅用于个人学习场景；文档中保持诚实限制说明
- 破坏性操作（删 remote、force push、改历史）须用户明确确认

### 6.1 字体许可（硬性）

- **对外内容用到的字体，必须可公开获取且允许商用，不得引入侵权风险。**  
- 细则与白名单见 [`docs/FONT_LICENSE.md`](./docs/FONT_LICENSE.md)。  
- 禁止打包/分发来路不明或未授权的商用字库文件。  
- 封面与公众号 HTML：**优先 Noto / Source Han（OFL 线）+ 系统字体回退栈**；不确定授权的字体直接不用。

---

## 7. 语言

- 用户中文 → 回复中文
- 代码标识符、路径、命令保持可复制的原文
- Commit message：完整句子，说明意图（英文或中文均可，仓库当前以英文 why 为主、可混用）

---

## 8. 快速检查清单（每次 PR / 推送前）

- [ ] 只改了本次任务相关文件
- [ ] `docs/PROGRESS.md` 已更新
- [ ] 真源在 `skills/`，没有只改 bridge
- [ ] README / changelog 与行为一致（若有用户可见变更）
- [ ] `.gitignore` 仍排除用户数据与密钥
