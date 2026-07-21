# ky-codex-supergrok changelog

## 0.1.0 — 2026-07-21

- 首次发布：SuperGrok 订阅通道 + Codex 本地代理
- `install.sh`：安装 bin、模型目录、provider 配置
- `codex-provider`：grok / openai / toggle / status
- macOS 一键 App：`Codex → Grok` / `Codex → OpenAI` / `Codex 切换模型`
- 请求适配：剥离 Codex 专有 `additional_tools` 等，尽量兼容 SuperGrok Responses
- 默认绕过系统 HTTP 代理，缓解 VPN Tunnel 503
- 开发者提示词身份改写（减轻自称 GPT-5）
