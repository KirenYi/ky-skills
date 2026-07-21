# ky-codex-supergrok

让 **Codex 换模型尽量像点按钮一样简单**。


## 菜单怎么选（重要）

| 菜单项 | 你要准备什么 | 不要填 |
|--------|--------------|--------|
| ① OpenAI / ChatGPT 官方额度 | ChatGPT 登录 | 任何 API Key |
| ② SuperGrok（X 订阅） | `grok login` | API Key |
| ③ DeepSeek … **← 官网 Key** | [DeepSeek 控制台](https://platform.deepseek.com/api_keys) 的 Key | OpenRouter Key |
| ④ OpenRouter / Claude / Gemini | [OpenRouter](https://openrouter.ai/keys) 的 `sk-or-v1-…` | DeepSeek 官网 Key |
| ⑤ 中转站 / 自定义 API | 中转站 Base URL + Key + 模型名 | 乱填无关 Key |

一句话：**DeepSeek 看「官网 Key」；Claude/Gemini 看「OpenRouter」。**

## 用户怎么用（推荐）

### 1. 安装一次

```bash
bash skills/ky-codex-supergrok/scripts/install.sh
```

或在 Agent 里：`/ky-codex-supergrok` → 帮我安装。

### 2. 日常怎么点（桌面不堆图标）

默认桌面**只有 1 个主图标**（带设计图标）：

| 图标 | 作用 |
|------|------|
| **Codex 切换模型** | 主菜单选通道；第一项可打开教程网页 |

**第一次**选中某通道并成功后，才自动生成 `Codex → 该通道` 快捷方式。


### 3. 第一次用 DeepSeek / Claude？

点选后若还没 Key：

1. 弹出窗口  
2. 可点 **「查看教程」** → 浏览器打开图文步骤  
3. 或直接粘贴 `sk-or-v1-...` → **「保存并切换」**  

Key 只存本机 `~/.codex/ky-provider.env`。  
**第二次起再点同一通道 = 直接切换。**

### 4. 不会用？

在切换菜单选「不会使用？打开教程」，或：

```bash
~/.codex/bin/codex-provider tutorial
```

### 5. 切换后

**新建对话** 再聊（旧会话可能绑旧模型）。

---

## 两条「简单路径」

**A. 只要 Grok 订阅**  
`grok login` → 点 **Codex → Grok**

**B. 要 DeepSeek / Claude / 多家 API**  
申请 [OpenRouter Key](https://openrouter.ai/keys)（一次）→ 点 **API 合集** 或 DeepSeek/Claude  
→ 之后尽量在 Codex **模型列表**里换 Claude/DeepSeek/Gemini（同一 OpenRouter 通道 + 多模型目录）

> 为何不用 DeepSeek 官网 Key 直连？新版 Codex 只走 Responses 协议，直连易失败；OpenRouter 兼容且一个 Key 多家模型。

---

## 命令行（可选）

```bash
codex-provider pick
codex-provider use deepseek
codex-provider use grok
codex-provider use api
codex-provider tutorial
codex-provider status
```

---

## 限制

- SuperGrok 与官方 OpenAI 是不同通道，需切换器切换。  
- 桌面端自定义模型名可能显示「自定义」。  
- 非官方集成，平台条款与费用自负。  
- 勿把 `ky-provider.env` 提交到 Git。

MIT · [ky-skills](https://github.com/KirenYi/ky-skills)
