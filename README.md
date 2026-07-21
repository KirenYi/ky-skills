# ky-skills

Kiren Yi（KY）Agent Skill 集合。短名、单技能、可多端安装。

## Skills

| 命令 | 核心能力 |
|------|----------|
| [`/ky-x`](./skills/ky-x/) | 归档 X 公开帖 |
| [`/ky-dy`](./skills/ky-dy/) | 下载抖音视频 |
| [`/ky-xhs`](./skills/ky-xhs/) | 抓小红书笔记 |
| [`/ky-sph`](./skills/ky-sph/) | 视频号 / 公众号获取 |
| [`/ky-xdraft`](./skills/ky-xdraft/) | Markdown → X 长文草稿 |
| [`/ky-mphtml`](./skills/ky-mphtml/) | Markdown → 公众号 HTML |

## 安装

发给 Agent：

```text
帮我安装这里的 Skills：https://github.com/KirenYi/ky-skills
```

或：

```bash
curl -fsSL https://github.com/KirenYi/ky-skills/raw/main/install.sh | bash
```

Windows 可 `git clone` 后：

```bash
./scripts/install-links.sh
```

重启 Agent 后使用上表命令。

## 依赖速查

| Skill | 额外依赖 |
|-------|----------|
| ky-x | Python 3.10+（标准库） |
| ky-dy | `playwright` `requests` + Chromium |
| ky-xhs | `requests`（可选 `XHS_COOKIE`） |
| ky-sph | [wx_channels_download](https://github.com/ltaoo/wx_channels_download) + 微信 PC |
| ky-xdraft | `playwright` `pycryptodome`；Chrome 已登录 X |
| ky-mphtml | 无（Agent 按模板生成 HTML） |

## 限制

- 用户数据（`~/.ky-x/`、cookies）不进 Git  
- 平台风控会导致抓取失败，属正常  
- 合法个人学习 / 创作用途  

见 [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md)。

## License

[MIT](./LICENSE)
