# ky-xdraft

Markdown → X 长文**草稿**（默认不发布）。

```bash
pip install playwright pycryptodome && python -m playwright install chromium
python3 scripts/export_x_cookies_from_chrome.py --output /tmp/x_cookies.json
python3 scripts/upload_markdown_to_x_article.py article.md --cookies-json /tmp/x_cookies.json --dry-run
```
