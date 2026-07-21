# ky-dy

下载**抖音公开视频**到本地（MP4 + 元数据 JSON）。

## 安装依赖

```bash
pip install playwright requests
python -m playwright install chromium
```

## 用法

```bash
python3 scripts/download.py "https://www.douyin.com/video/<id>"
python3 scripts/download.py "URL" --metadata-only
python3 scripts/download.py "URL" "/path/out.mp4"
```

Agent：`/ky-dy`

## 说明

- 本 skill 的脚本在 `scripts/download.py`，由 KY 维护。  
- 平台接口与风控变化时可能失败，属正常。  
- 仅用于你有权保存的公开内容。  
