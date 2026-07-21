## 0.5.1 — 2026-07-21

- 菜单/教程/README 统一数字标注：①官方 ②Grok ③DeepSeek官网 ④OpenRouter

## 0.5.0 — 2026-07-21

- DeepSeek 官网 API Key 直连（本地 deepseek-proxy 协议桥）
- 与 OpenRouter 路径分离；教程增加 DeepSeek 专节

## 0.4.0 — 2026-07-21

- 桌面默认仅「切换模型」+「使用教程」
- 首次成功切换某通道后自动生成「Codex → xxx」快捷方式

# ky-codex-supergrok changelog

## 0.3.1 — 2026-07-21

- 桌面仅保留 5 个入口；安装时清理旧的 per-model 快捷方式与 `.command`

## 0.3.0 — 2026-07-21

- **首次缺 Key 弹窗**：粘贴 OpenRouter Key / 查看教程 / 取消
- **「Codex 使用教程」App** + 离线图文 `references/tutorials/index.html`
- 切换菜单首项：**不会使用？打开教程**
- **API 模型合集** profile + OpenRouter 多模型 catalog（便于列表内切换）
- 失败时桌面 App 提示并引导打开教程

## 0.2.0 — 2026-07-21

- **多模型一键切换**：OpenAI / SuperGrok / Claude / Claude Opus / DeepSeek / R1 / Gemini
- Profile 注册表 `profiles.json` → 安装为 `~/.codex/ky-profiles.json`
- `codex-provider use|list|pick|status|toggle|keys`
- OpenRouter provider（Responses）承载 Claude / DeepSeek / Gemini
- 密钥文件 `~/.codex/ky-provider.env`
- macOS：主菜单 App「Codex 切换模型」+ 各通道快捷 App

## 0.1.0 — 2026-07-21

- 首次发布：SuperGrok 订阅 + OpenAI 双通道与一键切换
