# ky-xhs

抓取**小红书公开笔记**到本地目录（元数据 / 图文或视频 / 字幕若有）。

## 安装依赖

```bash
pip install requests
```

## 用法

```bash
python3 scripts/fetch.py "https://www.xiaohongshu.com/explore/<id>?xsec_token=..."
python3 scripts/fetch.py "URL" --skip-media
```

可选：进程内设置 `XHS_COOKIE`（勿写入仓库、勿提交 Git）。

Agent：`/ky-xhs`

## 说明

- 本 skill 的脚本在 `scripts/fetch.py`，由 KY 维护。  
- 需要完整链接或登录态时以页面实际为准。  
- 仅用于你有权保存的公开内容。  
