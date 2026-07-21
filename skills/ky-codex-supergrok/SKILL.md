---
name: ky-codex-supergrok
description: |
  把 OpenAI Codex（桌面端/CLI）一键切换到多种模型通道：SuperGrok 订阅、OpenAI/ChatGPT、Claude、DeepSeek、Gemini 等。
  SuperGrok 用 grok login（非 API Key）；Claude/DeepSeek/Gemini 经 OpenRouter（需 OPENROUTER_API_KEY）。
  触发：/ky-codex-supergrok、「Codex 切换模型」「Codex 接 Grok」「Codex 用 Claude」「Codex DeepSeek」「一键切换模型」
  One-click multi-model switcher for Codex Desktop/CLI (SuperGrok + OpenRouter Claude/DeepSeek/…).
---

# ky-codex-supergrok

Codex **多模型一键切换**：

| Profile | 通道 | 密钥 |
|---------|------|------|
| `openai` | ChatGPT / 官方 Codex 额度 | ChatGPT 登录 |
| `grok` | SuperGrok 订阅 | `grok login`（非 API） |
| `claude` / `claude-opus` | OpenRouter → Claude | `OPENROUTER_API_KEY` |
| `deepseek` / `deepseek-r1` | OpenRouter → DeepSeek | `OPENROUTER_API_KEY` |
| `gemini` | OpenRouter → Gemini | `OPENROUTER_API_KEY` |

> Codex 现版只支持 `wire_api = "responses"`。DeepSeek/Claude **官方直连**常不兼容，故 API 类模型统一走 **OpenRouter Responses**。

## 触发后怎么做

| 意图 | 动作 |
|------|------|
| 安装 / 升级 | `bash "$SKILL_ROOT/scripts/install.sh"` |
| 列出模型 | `~/.codex/bin/codex-provider list` |
| 切换 | `codex-provider use <id>` 或 `pick` |
| 状态 | `codex-provider status` |
| 写密钥 | 编辑 `~/.codex/ky-provider.env` |

### 路径

- `SKILL_ROOT` = 本文件目录
- 安装后：`~/.codex/bin/codex-provider`、`~/.codex/ky-profiles.json`

### 安装

```bash
bash "$SKILL_ROOT/scripts/install.sh"
```

### 密钥（Claude / DeepSeek / Gemini）

```bash
# ~/.codex/ky-provider.env  (chmod 600)
OPENROUTER_API_KEY=sk-or-v1-...
```

密钥页：https://openrouter.ai/keys  

**不要**把 key 写进 git 或 skill 仓库。

### SuperGrok

```bash
grok login
~/.codex/bin/codex-provider use grok
```

### 一键切换（macOS）

- **Codex 切换模型** — 弹出列表任选  
- **Codex → OpenAI / Grok / Claude / DeepSeek / Gemini** — 直达  

或：

```bash
codex-provider pick
codex-provider use claude
codex-provider use deepseek
codex-provider use openai
```

切换后 **新建 Codex 对话**（旧会话可能绑旧模型）。桌面会重启 ChatGPT/Codex。

### 确认

```bash
codex-provider status
# mode: claude / grok / …
```

不要用「你是什么模型」当唯一依据。

### 故障

| 现象 | 处理 |
|------|------|
| missing OPENROUTER_API_KEY | 写入 `~/.codex/ky-provider.env` |
| SuperGrok 502 | `supergrok-proxy restart`；先 `grok login` |
| 仍走旧额度 | `use` 后再新对话 + 确认 status |
| 模型 404 | 编辑 `~/.codex/ky-profiles.json` 里 OpenRouter slug |

### 安全

- 非官方集成；OpenRouter / SuperGrok 条款用户自负  
- 永不提交 `ky-provider.env`、`auth.json`、token  
- 不修改 ChatGPT.app 本体  

### 回复

中文用户用中文；给可复制命令；安装后列 profile 表 + 下一步（密钥 / grok login / pick）。
