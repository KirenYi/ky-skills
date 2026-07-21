# ky-codex-supergrok

把 **OpenAI Codex**（ChatGPT 桌面端里的 Codex / Codex CLI）接到 **xAI SuperGrok 订阅**，与 Grok Build 一样用 `grok login`，**不必**购买 console.x.ai API Key。

提供：

- 本地代理（会话 token → SuperGrok 上游）
- Codex `model_providers` + 模型目录
- **一键切换**：SuperGrok ↔ 原来的 OpenAI 模型

## 你需要准备什么

| 项 | 说明 |
|----|------|
| SuperGrok（或同等可登录 Grok Build 的订阅） | 浏览器 `grok login` |
| Grok Build CLI | 本机有 `grok` 命令 |
| Codex 桌面端或 CLI | ChatGPT.app / Codex |
| Python 3.10+ | 仅标准库 |
| macOS（一键 App） | Linux 可用 CLI 切换 |

## 安装

在已安装 [ky-skills](https://github.com/KirenYi/ky-skills) 的 Agent 里：

```text
/ky-codex-supergrok
帮我安装 SuperGrok 给 Codex
```

或终端（在本 skill 目录下）：

```bash
bash skills/ky-codex-supergrok/scripts/install.sh
```

然后：

```bash
grok login
~/.codex/bin/supergrok-proxy start
~/.codex/bin/codex-provider grok   # 或双击桌面「Codex → Grok」
```

**新建 Codex 对话** 再使用。

## 一键切换（macOS）

安装后桌面与 `~/Applications` 会出现：

| App | 作用 |
|-----|------|
| **Codex → Grok** | 默认改为 SuperGrok，重启 ChatGPT/Codex |
| **Codex → OpenAI** | 改回 `gpt-5.6-sol`（或你配置的 OpenAI 模型） |
| **Codex 切换模型** | 两者互切 |

终端等价：

```bash
~/.codex/bin/codex-provider grok
~/.codex/bin/codex-provider openai
~/.codex/bin/codex-provider toggle
~/.codex/bin/codex-provider status
```

## 怎么确认在用 Grok

```bash
~/.codex/bin/codex-provider status
# mode: grok
# proxy: running ... 18765
```

桌面端左下角常显示 **xAI SuperGrok**。  
右下角可能是「自定义」（Desktop 显示限制，正常）。

> 问模型「你是谁」**不可靠**：Codex 会注入 GPT-5 人设；以 provider / 代理日志为准。

## 原理（一句话）

```text
Codex → http://127.0.0.1:18765 (本地代理)
      → 注入 grok login 的 OAuth token + CLI 头
      → https://cli-chat-proxy.grok.com  (SuperGrok 订阅通道)
```

详见 [`references/how-it-works.md`](./references/how-it-works.md)。

## 常见问题

**502 / Tunnel 503**  
本机 VPN 的 HTTP 代理有时会搞挂 HTTPS 隧道。默认代理已直连上游。重启：

```bash
~/.codex/bin/supergrok-proxy restart
```

**还在扣 ChatGPT Codex 额度**  
执行 `codex-provider grok`，**完全退出并重开** ChatGPT/Codex，**新建对话**。

**会不会改坏 Codex？**  
不会改 App 本体。只写用户目录 `~/.codex/` 与本机脚本。备份在 `~/.codex/provider-switch-backups/`。切回：

```bash
~/.codex/bin/codex-provider openai
~/.codex/bin/supergrok-proxy stop
```

## 限制与风险

- **非官方集成**，依赖 Grok CLI 订阅代理行为，可能随时变更或失效。
- 可能不符合 xAI / OpenAI 的服务条款；**自用风险自担**。
- 工具协议与官方 OpenAI Codex 模型不完全一致，部分能力可能有差异。
- 不要提交或分享 `~/.grok/auth.json`。

## 许可

随 [ky-skills](https://github.com/KirenYi/ky-skills) MIT 许可发布。与 OpenAI、xAI 无官方关系。
