# PROGRESS — 跨 Agent 进度板

> **每个 Agent（Claude Code / Codex / Grok / 其他）在本仓库做完一轮有意义的改动后，必须在本文件顶部追加一条记录。**  
> 这样下一个工具打开仓库时能立刻对齐状态，而不是只靠聊天上下文。

格式固定：

```markdown
## YYYY-MM-DD HH:MM TZ — <工具名> — <一句话标题>

- **操作者**：Grok / Claude Code / Codex / Human / …
- **目标**：…
- **已完成**：
  - …
- **改动路径**：
  - `path/to/file`
- **验证**：
  - …
- **未完成 / 下一步**：
  - …
- **风险或注意**：
  - …
```

---

## 2026-07-20 — Grok — 新增媒体抓取与 X 草稿四 skill 并准备推送

- **操作者**：Grok
- **目标**：将抖音 / 小红书 / 视频号 / X Article 草稿能力沉淀为正式 `ky-*` skill，并入 ky-skills 真源后推送 GitHub
- **已完成**：
  - 新增 `ky-douyin`（Playwright 拦截下载 + metadata）
  - 新增 `ky-xhs`（INITIAL_STATE 抓取 + 媒体）
  - 新增 `ky-wx-channels`（编排 wx_channels_download 工作流）
  - 新增 `ky-x-article`（Markdown → X Articles 草稿）
  - 更新根 README、VERSION 0.4.0、AGENTS、install.sh 提示、THIRD_PARTY_NOTICES
- **改动路径**：
  - `skills/ky-douyin/**`
  - `skills/ky-xhs/**`
  - `skills/ky-wx-channels/**`
  - `skills/ky-x-article/**`
  - `README.md`、`VERSION`、`AGENTS.md`、`install.sh`、`THIRD_PARTY_NOTICES.md`、`docs/PROGRESS.md`
- **验证**：
  - `python -m py_compile` 对新脚本（若环境有 Python）
  - `git status` 确认仅相关文件
- **未完成 / 下一步**：
  - `git push` 到 `KirenYi/ky-skills`（本轮执行）
  - 用户本机 `./scripts/install-links.sh` 刷新软链
- **风险或注意**：
  - 平台抓取随时可能被风控；文档已写诚实限制
  - 勿提交 cookies / 用户数据

---

## 2026-07-19 07:23 PDT — Codex — 增加一行命令安装入口

- **操作者**：Codex
- **目标**：让非技术用户无需理解 Git 和目录结构即可安装或更新 Skills
- **已完成**：
  - 将“把仓库链接发给 Agent，让 Agent 自动安装”设为首选入口
  - 新增根目录 `install.sh`，一条命令自动下载、更新并连接 Skills
  - 在没有 Git 时自动使用 GitHub 压缩包安装
  - 为链接脚本增加简洁输出模式和隔离测试目录支持
  - 将 README 安装入口改为可直接复制的一行命令
- **改动路径**：
  - `install.sh`
  - `scripts/install-links.sh`
  - `README.md`
  - `docs/MULTI_HOST.md`
  - `VERSION`
  - `docs/PROGRESS.md`
- **验证**：
  - `bash -n install.sh scripts/install-links.sh`
  - 在 `/tmp` 隔离环境验证首次安装、重复更新、安装全部与只安装 `ky-x`
  - 验证生成的多宿主链接均指向受管安装目录
- **未完成 / 下一步**：
  - 无
- **风险或注意**：
  - 一键安装依赖 GitHub 可访问；失败时用户可让 Agent 按仓库 README 手动安装

---

## 2026-07-19 07:11 PDT — Codex — 精简公开介绍并移除测试账号

- **操作者**：Codex
- **目标**：精简仓库与 Skill 的公开说明，移除早期测试账号及与功能无关的个人化介绍
- **已完成**：
  - 将根 README 收敛为项目功能、安装、使用与限制说明
  - 从文档、示例配置和初始化逻辑中移除早期测试账号；必要示例统一为 `naval`
  - 清理 `ky-x` 与 `ky-wechat-html` 中会外显的署名、品牌解释和 HTML 标题后缀
  - 同步版本号、变更记录与 `ky-x` 命令行帮助文本
- **改动路径**：
  - `README.md`、`VERSION`
  - `skills/ky-x/**`
  - `skills/ky-wechat-html/**`
  - `docs/PROGRESS.md`
- **验证**：
  - `git diff --check`
  - `python3 -m xarchive --help`、`python3 -m xarchive --version`
  - 临时目录执行 `python3 -m xarchive init` 并通过 JSON 校验
  - `./scripts/install-links.sh --dry-run`
  - 全仓搜索确认早期测试账号无命中
- **未完成 / 下一步**：
  - 用户确认后推送远端
- **风险或注意**：
  - `.gitignore` 继续保留旧版数据目录规则，防止历史用户数据被误提交

---

## 2026-07-12 — Grok — 出镜封面规则 v2（竖屏修正 / 横屏暂缓）

- **操作者**：Grok
- **目标**：按用户反馈修正出镜封面：竖屏大字在脸下或头上；横屏仅记录
- **已完成**：
  - 重出竖屏封面样本（脸下/头上大字）
  - 笔记 `docs/COVER_ON_CAMERA_NOTES.md` + 云盘 `出镜封面规则_v2.md`
- **改动路径**：
  - `docs/COVER_ON_CAMERA_NOTES.md`
  - 用户云盘 `ky-封面测试/from-video-chatgpt56/`
- **验证**：png_covers_v2 导出
- **未完成 / 下一步**：用户确认竖屏版本后，再考虑写入 ky-cover
- **风险或注意**：横屏等真实横屏成片再执行

---

## 2026-07-12 — Grok — 字体商用许可硬约束

- **操作者**：Grok
- **目标**：封面/排版统一「可公开、可商用、无侵权风险」字体策略
- **已完成**：
  - 新增 `docs/FONT_LICENSE.md`（白名单 + 禁止项 + 检查清单）
  - `AGENTS.md`、`ky-wechat-html` SKILL / styles 引用该约束
  - 封面测试说明补充字体条款
- **改动路径**：
  - `docs/FONT_LICENSE.md`、`AGENTS.md`、`skills/ky-wechat-html/**`、用户云盘测试说明
- **验证**：文档交叉引用存在
- **未完成 / 下一步**：正式 `ky-cover` 时默认 Noto 渲染管线
- **风险或注意**：系统字体栈用于本机光栅化位图通常不构成分发字体文件；若未来打包 .ttf 必须只用 OFL 并附 LICENSE

---

## 2026-07-12 — Grok — ky-wechat-html 扩充 5 套风格

- **操作者**：Grok
- **目标**：调研公开排版范式后，扩展 KY 风格库并保持微信兼容
- **已完成**：
  - 新增 `ink` / `cream` / `swiss` / `night` / `fresh`（styles.md + SKILL 表）
  - 版本 0.2.0，changelog 更新
- **改动路径**：
  - `skills/ky-wechat-html/templates/styles.md`
  - `skills/ky-wechat-html/SKILL.md`
  - `skills/ky-wechat-html/VERSION`
  - `skills/ky-wechat-html/references/changelog.md`
- **验证**：styles.md 含 13 个 `## id ·` 段落
- **未完成 / 下一步**：用户可指定把新风格跑进纳瓦尔文稿预览
- **风险或注意**：`night` 暗色在部分公众号外壳下观感可能被冲淡

---

## 2026-07-12 — Grok — 新增 ky-wechat-html

- **操作者**：Grok
- **目标**：借鉴 dbs-wechat-html 的核心结构，写成 KY 自有公众号 HTML skill（非全文抄袭）
- **已完成**：
  - 新增 `skills/ky-wechat-html/`（SKILL.md + 8 套原创风格 styles.md）
  - 输出目录 `ky-公众号HTML/`、风格 id 独立命名
  - 更新根 README skill 表；`install-links` 可挂多端
- **改动路径**：
  - `skills/ky-wechat-html/**`
  - `README.md`
  - `docs/PROGRESS.md`
- **验证**：
  - 目录结构完整；`./scripts/install-links.sh ky-wechat-html`
- **未完成 / 下一步**：
  - 可选：Python 渲染脚本提高长文稳定性
  - 人类用真实 MD 试跑一轮排版
- **风险或注意**：
  - 当前仍为 Agent 按规则生成 HTML（与参考 skill 同类），长文依赖模型遵守规则

---

## 2026-07-12 — Grok — 多 Agent 协作文档 + 跨端安装

- **操作者**：Grok
- **目标**：
  1. 为多工具协作增加规范与进度同步文件
  2. 明确 ky-skills 是「多 skill 集合」，ky-x 仅为 v0.1 第一个 skill
  3. 强化「任意主流 Agent 宿主都能装同一套 skill」的安装方式
- **已完成**：
  - 新增 `AGENTS.md`、`CLAUDE.md`、`SOURCE_OF_TRUTH.md`
  - 新增 `docs/PROGRESS.md`、`docs/MULTI_HOST.md`、`docs/COLLABORATION.md`
  - 扩展 `scripts/install-links.sh` 覆盖更多 skills 目录（含 Trae / 通用 Agents 等）
  - 更新根 `README.md`：集合定位 + 多端安装
- **改动路径**：
  - `AGENTS.md`、`CLAUDE.md`、`SOURCE_OF_TRUTH.md`
  - `docs/*`
  - `scripts/install-links.sh`
  - `README.md`
- **验证**：
  - `./scripts/install-links.sh ky-x`（推送前本地执行）
- **未完成 / 下一步**：
  - 人类确认后 `git push`
  - 后续可增加更多 `ky-*` skill
  - 若某宿主路径特殊（如 Work Buddy 官方目录），补进 `MULTI_HOST.md` 与 install 脚本
- **风险或注意**：
  - 部分宿主 skills 路径可能随版本变化；以各产品文档为准，脚本采用「存在则链接、不存在则跳过」策略

---

## 2026-07-12 — Grok — 初版仓库上线

- **操作者**：Grok
- **目标**：发布 ky-skills 与首个 skill `ky-x`
- **已完成**：
  - 仓库结构、`ky-x` 实现、GitHub `KirenYi/ky-skills` public 推送
- **改动路径**：
  - 初版全量
- **验证**：
  - `python3 -m xarchive` 冒烟；remote push 成功
- **未完成 / 下一步**：
  - 多 Agent 协作文档（本轮）
- **风险或注意**：
  - `ky-x` 依赖公开 RSS，非全量历史
