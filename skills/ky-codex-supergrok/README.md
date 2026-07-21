# ky-codex-supergrok

OpenAI **Codex** 多模型一键切换（桌面端 / CLI）。

| 一点就切 | 说明 |
|----------|------|
| OpenAI | ChatGPT 登录官方模型（如 gpt-5.6-sol） |
| SuperGrok | `grok login` 订阅，**不买** API Key |
| Claude / DeepSeek / Gemini | 经 [OpenRouter](https://openrouter.ai)（Responses 兼容） |

## 为什么 Claude / DeepSeek 要走 OpenRouter？

新版 Codex **只支持 Responses API**（`wire_api = "chat"` 已废弃）。  
DeepSeek / 多数 Claude 直连是 Chat Completions，容易 4xx。  
OpenRouter 提供 Responses 兼容层，一个 Key 可切多家模型。

## 安装

Agent：

```text
/ky-codex-supergrok
帮我安装 / 升级 Codex 多模型切换
```

终端：

```bash
bash skills/ky-codex-supergrok/scripts/install.sh
```

## 配置密钥（Claude / DeepSeek / Gemini）

```bash
nano ~/.codex/ky-provider.env
# OPENROUTER_API_KEY=sk-or-v1-...
chmod 600 ~/.codex/ky-provider.env
```

## 使用

### macOS 桌面

双击 **「Codex 切换模型」** → 列表里选通道。  

或分别点：

- Codex → OpenAI  
- Codex → Grok  
- Codex → Claude  
- Codex → DeepSeek  
- Codex → Gemini  

### 命令行

```bash
~/.codex/bin/codex-provider list
~/.codex/bin/codex-provider pick          # macOS 菜单
~/.codex/bin/codex-provider use openai
~/.codex/bin/codex-provider use grok
~/.codex/bin/codex-provider use claude
~/.codex/bin/codex-provider use deepseek
~/.codex/bin/codex-provider use gemini
~/.codex/bin/codex-provider status
```

**每次切换后新建对话。**

## 内置 Profile（可改）

配置文件：`~/.codex/ky-profiles.json`（安装时从 skill 复制）。

| id | 默认 model slug |
|----|-----------------|
| openai | `gpt-5.6-sol` |
| grok | `grok-4.5`（本地 SuperGrok 代理） |
| claude | `anthropic/claude-sonnet-4.6` |
| claude-opus | `anthropic/claude-opus-4.6` |
| deepseek | `deepseek/deepseek-chat` |
| deepseek-r1 | `deepseek/deepseek-r1` |
| gemini | `google/gemini-2.5-pro` |

OpenRouter 模型 id 会变：以 [openrouter.ai/models](https://openrouter.ai/models) 为准，改 JSON 后 `codex-provider use <id>` 即可。

## SuperGrok 单独说明

```bash
grok login
~/.codex/bin/supergrok-proxy start
~/.codex/bin/codex-provider use grok
```

详见 [`references/how-it-works.md`](./references/how-it-works.md)。

## 限制与风险

- SuperGrok / OpenRouter 均为**非官方**对接 Codex 的方式，可能失效。  
- 遵守各平台条款；费用以 OpenRouter / 订阅账单为准。  
- 勿提交 `~/.codex/ky-provider.env` 或 `~/.grok/auth.json`。

## License

MIT（[ky-skills](https://github.com/KirenYi/ky-skills)）。与 OpenAI / xAI / Anthropic / DeepSeek / OpenRouter 无官方关系。
