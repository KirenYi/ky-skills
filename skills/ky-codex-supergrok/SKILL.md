---
name: ky-codex-supergrok
description: |
  Codex 多模型「尽量一键」：SuperGrok 订阅、OpenAI 官方、Claude/DeepSeek/Gemini（OpenRouter）。
  首次缺 API 时弹窗填 Key，并提供「查看教程 / 不会使用怎么办」图文指南。
  触发：/ky-codex-supergrok、「Codex 切换模型」「Codex 教程」「DeepSeek 怎么配」「不会使用怎么办」
---

# ky-codex-supergrok

目标：**用户越少思考越好**——点按钮切换；缺配置就弹窗 + 教程，而不是丢一堆命令。

## Agent 该做什么

1. **安装/升级**：`bash "$SKILL_ROOT/scripts/install.sh"`
2. **引导使用**：优先让用户双击 **Codex 切换模型** / **Codex 使用教程**
3. **缺 Key**：说明会自动弹窗；也可 `codex-provider tutorial`
4. **不要**默认要求用户手写复杂 config.toml

## 安装

```bash
bash "$SKILL_ROOT/scripts/install.sh"
```

会安装：bin、profiles、SuperGrok 代理、OpenRouter 多模型目录、离线教程、桌面 App。

## 用户路径（请按此教）

| 场景 | 操作 |
|------|------|
| 日常切换 | 双击「Codex 切换模型」 |
| 第一次 DeepSeek/Claude | 点选 → 弹窗贴 OpenRouter Key 或点「查看教程」 |
| 第二次及以后 | 再点 = 直接切换 |
| SuperGrok | 先 `grok login`，再点 Grok |
| 不会用 | 「Codex 使用教程」或 `codex-provider tutorial` |
| 切换后 | **新建对话** |

## 教程位置

- 离线：`$SKILL_ROOT/references/tutorials/index.html`  
- 安装后：`~/.codex/ky-tutorials/index.html`  
- 命令：`~/.codex/bin/codex-provider tutorial`

## 安全

- Key 仅 `~/.codex/ky-provider.env`（600）  
- 永不把 Key 写入仓库或聊天  
- 非官方集成，风险自负  

## 回复模板（安装后）

用中文短说明：

1. 点「Codex 切换模型」  
2. 第一次 API 会弹窗 / 可点查看教程  
3. 有「Codex 使用教程」按钮  
4. 切换后新建对话  
