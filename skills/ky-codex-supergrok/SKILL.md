---
name: ky-codex-supergrok
description: |
  把 OpenAI Codex（桌面端 / CLI）接到 xAI SuperGrok 订阅通道：用 `grok login` 即可，不必买 console.x.ai API。
  提供本地代理、模型目录、以及「Codex → Grok / OpenAI」一键切换。
  触发方式：/ky-codex-supergrok、/codex-supergrok、「Codex 接 Grok」「SuperGrok 登录用 Codex」「Codex 一键切换 Grok」「装 SuperGrok 给 Codex」
  Wire OpenAI Codex Desktop/CLI to SuperGrok subscription (no paid xAI API key) with one-click toggle.
---

# ky-codex-supergrok

让 **Codex** 使用 **SuperGrok 订阅**（与 Grok Build 同一套 `grok login`），**不是** console.x.ai 按量 API。

## 触发后怎么做

按用户意图选一条路径，**直接执行脚本**，不要只给概念说明。

| 用户意图 | 动作 |
|----------|------|
| 安装 / 配置 / 修好 | 跑 `install.sh` |
| 切到 Grok | `~/.codex/bin/codex-provider grok` |
| 切回 OpenAI | `~/.codex/bin/codex-provider openai` |
| 来回切 | `codex-provider toggle` |
| 查状态 / 报错 | `codex-provider status` + `supergrok-proxy status` + 读 log |
| 只要原理 | 打开 `references/how-it-works.md` 摘要回答 |

### 路径

- `SKILL_ROOT` = 本文件所在目录
- 脚本：`$SKILL_ROOT/scripts/`
- 安装后运行时：`~/.codex/bin/`

### 安装（首选）

```bash
bash "$SKILL_ROOT/scripts/install.sh"
```

安装会：

1. 复制 `supergrok-token` / `supergrok-proxy` / `codex-provider` → `~/.codex/bin/`
2. 生成 `~/.codex/model-catalogs/xai-models.json`
3. 在 `~/.codex/config.toml` 注册 `[model_providers.xai]`（若尚未有）
4. macOS 创建桌面一键 App：`Codex → Grok` / `Codex → OpenAI` / `Codex 切换模型`
5. 若已有 `~/.grok/auth.json`，启动本地代理并切到 Grok 模式

### 用户前置条件

1. 已装 **Grok Build CLI**，且执行过：`grok login`（SuperGrok / 有订阅）
2. 已装 **ChatGPT / Codex 桌面端** 或 Codex CLI
3. Python 3.10+（仅标准库）
4. **不要**要求用户创建 `XAI_API_KEY`（那是另一条付费 API 路）

### 日常使用

```bash
~/.codex/bin/supergrok-proxy start    # 代理常驻
~/.codex/bin/codex-provider grok      # 默认改成 Grok 并重启桌面端
# 或双击桌面「Codex → Grok」
```

CLI 也可用：

```bash
codex --profile xai
```

**重要：** 切换后让用户 **新建对话**；旧会话可能仍绑旧模型。

### 如何确认在用 Grok

- `codex-provider status` → `mode: grok`，`proxy: running`
- 桌面端左下角常见 `xAI SuperGrok`，右下角可能显示「自定义」
- **不要**用「你是什么模型？」当唯一依据（Codex 会注入 GPT-5 人设；代理会尽量改写，仍可能自称 GPT）
- 看 `~/.codex/supergrok-proxy.log` 是否有 `POST /v1/responses ... 200`

### 常见故障

| 现象 | 处理 |
|------|------|
| 502 / Tunnel 503 | 代理默认已绕过系统 VPN 代理；执行 `supergrok-proxy restart`。必须走系统代理时：`SUPERGROK_USE_SYSTEM_PROXY=1 supergrok-proxy restart` |
| 401 / 要登录 | `grok login`，再 `supergrok-proxy restart` |
| 代理 not running | `~/.codex/bin/supergrok-proxy start` |
| 仍走 OpenAI 额度 | `codex-provider grok` 后 **重启桌面端 + 新对话** |
| 想完全卸载通道 | `codex-provider openai`；`supergrok-proxy stop`；可选删桌面 App；配置备份在 `~/.codex/provider-switch-backups/` |

### 安全与合规（必须告诉用户）

- 使用 **订阅 OAuth 会话** 调 `cli-chat-proxy.grok.com`，属于非官方集成，可能随时失效或违反平台条款；用户自负风险。
- **永不**把 `~/.grok/auth.json`、token、API key 写入仓库或聊天明文日志。
- 不修改 ChatGPT.app 本体，只改用户级 `~/.codex/` 与本机脚本。

### 回复风格

- 中文用户用中文；命令与路径保持可复制原文。
- 安装结束后给：**下一步 3 条** + `status` 摘要。
- 不要把「付费 API Key」方案当成默认；只有用户明确要 API 时才提。
