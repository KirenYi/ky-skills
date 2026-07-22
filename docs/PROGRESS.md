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

## 2026-07-21 — Grok — Skill 更名 ky-codex-switch

- **操作者**：Grok
- **目标**：skill 命名改为 ky-codex- + 主功能「切换」
- **已完成**：目录/文档/脚本路径全部更名为 ky-codex-switch；多端软链更新
- **改动路径**：skills/ky-codex-switch/**、README、AGENTS
- **注意**：旧名 ky-codex-supergrok 已废弃

---

## 2026-07-21 — Grok — 官方 Codex 图标 + 误删可重生 + 清理桌面

- 图标改用 ChatGPT 内置 icon-codex-dark-color
- 桌面仅保留「Codex 切换模型」；通道快捷方式可再选一次重新生成
- 文档/教程补充误删恢复说明

---

## 2026-07-21 — Grok — 主图标设计 + 中转站 API + 去掉教程图标

- **已完成**：仅保留「Codex 切换模型」主图标（.icns）；教程只在菜单；新增⑤中转站（base_url+key+model + relay-proxy）
- **改动**：make-desktop-apps、build-app-icon、relay-proxy、profiles、tutorial/README

---

## 2026-07-21 — Grok — 支持 DeepSeek 官网 API Key

- **问题**：用户使用 DeepSeek 官网 Key，却走 OpenRouter → 401
- **修复**：deepseek-proxy 本地桥（Responses→Chat）；profile 用 DEEPSEEK_API_KEY；弹窗区分官网 Key
- **验证**：本地 /v1/responses 返回 200 且含 DEEPSEEK_OK

---

## 2026-07-21 — Grok — 修复 OpenRouter Desktop 401 Missing Authentication

- **原因**：Codex Desktop 读不到 ky-provider.env，请求无 Authorization
- **修复**：sync-openrouter-bearer.py 把 Key 写入 experimental_bearer_token；切换时自动同步
- **验证**：本机 config 已含 bearer；用户需重启 Codex 并确认 Key 为 sk-or-v1- 格式

---

## 2026-07-21 — Grok — 桌面按需生成快捷方式

- **操作者**：Grok
- **目标**：桌面不预装一堆图标；首次选中通道后自动生成快捷方式
- **已完成**：默认仅「切换模型」+「使用教程」；ensure-desktop-shortcut 在成功切换后创建 Codex → xxx
- **改动路径**：skills/ky-codex-switch/scripts/*
- **验证**：use grok → 桌面出现 Codex → Grok
- **下一步**：无

---

## 2026-07-21 — Grok — 清理桌面切换器图标

- **操作者**：Grok
- **目标**：桌面只保留最新 5 个入口
- **已完成**：删除 Claude/DeepSeek/Gemini 等多余 App 与旧 .command；make-desktop-apps 同步
- **改动路径**：本机 Desktop/Applications；skills/ky-codex-switch/scripts/make-desktop-apps.sh
- **验证**：ls Desktop Codex*
- **下一步**：无

---

## 2026-07-21 09:00 PDT — Grok — 多模型切换 UX：弹窗填 Key + 图文教程

- **操作者**：Grok
- **目标**：让非技术用户点按钮即可切换；缺 API 时引导填写并提供「不会使用怎么办」教程
- **已完成**：
  - 首次 OpenRouter Key 的 macOS 对话框（保存并切换 / 查看教程 / 取消）
  - 离线教程 HTML + 「Codex 使用教程」桌面 App
  - OpenRouter 多模型 catalog + `api` 合集 profile
  - pick 菜单增加教程入口；失败时引导教程
- **改动路径**：
  - `skills/ky-codex-switch/**`
  - `docs/PROGRESS.md`、`VERSION`、根 `README`（若有）
- **验证**：
  - bash -n / install 本地安装
  - codex-provider list / tutorial 路径存在
- **风险或注意**：
  - 教程说明走 OpenRouter 而非 DeepSeek 官网直连的原因

---

## 2026-07-21 08:10 PDT — Grok — ky-codex-switch 多模型一键切换

- **操作者**：Grok
- **目标**：在 SuperGrok/OpenAI 之外加入 Claude、DeepSeek、Gemini 等一键切换
- **已完成**：
  - `profiles.json` 多 profile 注册表
  - `codex-provider use|list|pick|status|toggle|keys`
  - OpenRouter provider（Responses）承载 Claude/DeepSeek/Gemini
  - 密钥文件 `~/.codex/ky-provider.env` + 桌面多通道 App
  - 文档与 skill VERSION 0.2.0
- **改动路径**：
  - `skills/ky-codex-switch/**`
  - `README.md`
  - `docs/PROGRESS.md`
  - `VERSION`
- **验证**：
  - `bash -n` codex-provider / install
  - 本机 `install.sh` + `codex-provider list`
- **未完成 / 下一步**：
  - 用户自备 OPENROUTER_API_KEY 后验证 Claude/DeepSeek 实请求
- **风险或注意**：
  - 直连 DeepSeek/Anthropic 与 Codex Responses 不兼容，故走 OpenRouter
  - 勿提交 ky-provider.env

---

## 2026-07-21 07:25 PDT — Grok — 新增 ky-codex-switch

- **操作者**：Grok
- **目标**：把 Codex ↔ SuperGrok 订阅通道与一键切换做成可发布 skill
- **已完成**：
  - 新增 `skills/ky-codex-switch/`（SKILL/README/scripts/references）
  - 安装脚本：本地代理、token 刷新、config provider、macOS 桌面一键 App
  - 更新根 README skill 表与 AGENTS 已发布列表
- **改动路径**：
  - `skills/ky-codex-switch/**`
  - `README.md`
  - `AGENTS.md`
  - `docs/PROGRESS.md`
  - `VERSION`
- **验证**：
  - `bash -n` 安装与切换脚本
  - `python3 -m py_compile` proxy/token
  - `./scripts/install-links.sh --dry-run ky-codex-switch`
- **未完成 / 下一步**：
  - 推送到 GitHub main
- **风险或注意**：
  - 非官方 SuperGrok 订阅代理集成；文档已标明风险与非 API Key 路径
  - 勿提交 `~/.grok/auth.json` 或任何 token

---

## 2026-07-21 — Grok — 去掉对外「挂靠第三方」表述，改为自有产品说明

- **操作者**：Grok
- **目标**：借鉴可以，但公开文档不得把别人的项目写成我们的组件/依赖清单，避免抄袭与蹭项目观感
- **已完成**：
  - 重写根 README：自有安装与使用说明，依赖表不再链到外部下载器仓库
  - `ky-sph` 改为原料入库工作流，明确不捆绑任何第三方下载器
  - `ky-xdraft` 改为自有草稿流程说明，移除仓库内非自研上传脚本
  - `THIRD_PARTY_NOTICES` 改为「非关联 / 不捆绑」声明
  - dy/xhs README 改为纯 KY 产品语气
- **改动路径**：
  - `README.md`、`THIRD_PARTY_NOTICES.md`、`VERSION`
  - `skills/ky-sph/**`、`skills/ky-xdraft/**`、`skills/ky-dy/**`、`skills/ky-xhs/**`
- **验证**：
  - 全文不再把外部仓库当作 skill 安装依赖展示
- **未完成 / 下一步**：
  - push
- **风险或注意**：
  - ky-xdraft 暂以手动草稿流程为主；自动化需后续 KY 自研再加

---

## 2026-07-21 — Grok — 精简 skill 命名与核心描述

- **操作者**：Grok
- **目标**：命名尽量短，description 只保留核心能力
- **已完成**：
  - 重命名：`ky-douyin`→`ky-dy`，`ky-wx-channels`→`ky-sph`，`ky-x-article`→`ky-xdraft`，`ky-wechat-html`→`ky-mphtml`
  - 统一 description 为一行核心能力 + 短触发
  - 更新 README / install / AGENTS / THIRD_PARTY / 字体文档引用
- **改动路径**：
  - `skills/ky-dy|ky-xhs|ky-sph|ky-xdraft|ky-mphtml|ky-x/**`
  - `README.md` `VERSION` `AGENTS.md` `install.sh` `docs/**`
- **验证**：
  - 目录名与 SKILL frontmatter `name` 一致
- **未完成 / 下一步**：
  - push；本机重链 soft link
- **风险或注意**：
  - 旧命令名失效，需重启 Agent

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
