# ky-skills

Kiren Yi（KY）的 Agent Skill 集合。前缀统一为 `ky-`，可安装到 Claude Code、Codex、Grok、Trae 等支持 Skills 的工具。

## 能做什么

| Skill | 功能 |
|-------|------|
| [`ky-x`](./skills/ky-x/) | 按账号增量归档 X 公开帖（Markdown + JSONL） |
| [`ky-wechat-html`](./skills/ky-wechat-html/) | Markdown → 微信公众号可粘贴 HTML |
| [`ky-douyin`](./skills/ky-douyin/) | 下载抖音公开视频 + 元数据 |
| [`ky-xhs`](./skills/ky-xhs/) | 抓取小红书公开笔记（视频/图文/字幕） |
| [`ky-wx-channels`](./skills/ky-wx-channels/) | 微信视频号 / 公众号获取工作流（编排开源下载器） |
| [`ky-x-article`](./skills/ky-x-article/) | Markdown → X Articles **草稿**（默认不发布） |

## 环境要求

- macOS / Linux / Windows
- Python 3.10+（多数带脚本的 skill 需要）
- 支持 Skills 的 Agent 工具

部分 skill 额外依赖见各自 README（如 Playwright、微信 PC 上游工具）。

## 安装

把下面这句话发给 Agent：

```text
帮我安装这里的 Skills：https://github.com/KirenYi/ky-skills
```

或终端：

```bash
curl -fsSL https://github.com/KirenYi/ky-skills/raw/main/install.sh | bash
```

Windows 可先 `git clone` 再执行：

```bash
./scripts/install-links.sh
```

安装后重启 Agent，使用 `/ky-x`、`/ky-douyin`、`/ky-xhs` 等命令。

## 快速示例

### ky-x

```text
/ky-x
归档 @naval 的公开帖子
```

### ky-douyin

```bash
pip install playwright requests && python -m playwright install chromium
python3 skills/ky-douyin/scripts/download.py "https://www.douyin.com/video/<id>"
```

### ky-xhs

```bash
pip install requests
python3 skills/ky-xhs/scripts/fetch.py "https://www.xiaohongshu.com/explore/<id>?xsec_token=..."
```

### ky-wx-channels

安装 [wx_channels_download](https://github.com/ltaoo/wx_channels_download) 后，在 Agent 中输入 `/ky-wx-channels` 按流程操作。

### ky-x-article

```text
/ky-x-article
把 article.md 上传为 X 长文草稿
```

### ky-wechat-html

```text
/ky-wechat-html
把 article.md 排成微信公众号 HTML
```

## 数据与限制

- 用户运行时数据（如 `~/.ky-x/`、临时 cookies）保存在本机，**不要提交 Git**。
- 平台接口与风控会变；文档中的限制请如实遵守。
- 仅在合法范围内用于个人学习与创作工作流。
- 详见 [`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md)。

## License

[MIT](./LICENSE)
