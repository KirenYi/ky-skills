# ky-skills

一组可安装到 Agent 工具中的实用 Skills。目前提供 X（Twitter）公开帖子本地归档和微信公众号 HTML 排版能力。

## 能做什么

| Skill | 功能 |
|-------|------|
| [`ky-x`](./skills/ky-x/) | 按账号增量归档 X 公开帖子，保存为本地 Markdown 与 JSONL |
| [`ky-wechat-html`](./skills/ky-wechat-html/) | 将 Markdown 转成可复制到微信公众号后台的单文件 HTML |

这些 Skills 可安装到 Claude Code、Codex、Grok、Trae 等支持 Skills 的 Agent 工具中，也可以直接使用其中的命令行脚本。

## 环境要求

- macOS / Linux（Windows 可使用 WSL）
- Python 3.10+（仅 `ky-x` 命令行功能需要）
- 支持 Skills 的 Agent 工具

`ky-x` 仅使用 Python 标准库，默认无需申请 X API。

## 安装

```bash
git clone https://github.com/KirenYi/ky-skills.git ~/ky-skills
cd ~/ky-skills
./scripts/install-links.sh
```

安装单个 Skill：

```bash
./scripts/install-links.sh ky-x
./scripts/install-links.sh ky-wechat-html
```

安装脚本会将 Skill 软链接到本机已有的兼容目录。不同工具的目录说明见 [`docs/MULTI_HOST.md`](./docs/MULTI_HOST.md)。

## 使用 ky-x

在已安装的 Agent 中输入：

```text
/ky-x
归档 @naval 的公开帖子
```

也可以直接使用命令行：

```bash
export PYTHONPATH=~/ky-skills/skills/ky-x/scripts

python3 -m xarchive init -c ~/.ky-x/config.json
python3 -m xarchive add naval -c ~/.ky-x/config.json
python3 -m xarchive sync --handle naval -c ~/.ky-x/config.json
python3 -m xarchive status -c ~/.ky-x/config.json
```

归档结果保存在：

```text
~/.ky-x/data/library/<handle>/_index.md
~/.ky-x/data/library/<handle>/YYYY-MM.md
~/.ky-x/data/data/@<handle>.jsonl
```

`ky-x` 支持多账号增量同步，可过滤转推和回复。默认数据源为公开 RSS 镜像，通常只能获取最近一部分帖子，无法保证完整历史或持续可用。

详细说明见 [`skills/ky-x/README.md`](./skills/ky-x/README.md)。

## 使用 ky-wechat-html

在已安装的 Agent 中输入：

```text
/ky-wechat-html
把 article.md 排成微信公众号 HTML
```

它只负责排版，不改写文章观点或文案。生成的 HTML 可在浏览器中打开并复制到微信公众号后台。

详细说明见 [`skills/ky-wechat-html/README.md`](./skills/ky-wechat-html/README.md)。

## 数据与使用限制

- `ky-x` 只处理公开帖子，用户配置和归档默认保存在本机 `~/.ky-x/`，不会写入本仓库。
- 请遵守平台服务条款、内容权利和当地法律，仅在合法范围内使用。
- 不要将 Cookie、Token、私有配置或个人归档提交到 Git。

## License

[MIT](./LICENSE)
