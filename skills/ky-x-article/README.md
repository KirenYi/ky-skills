# ky-x-article

Upload a local Markdown article to an **X Articles draft** (does not publish unless you explicitly ask).

## Requirements

```bash
pip install playwright pycryptodome
python -m playwright install chromium
```

Chrome must already be logged in to X.

## Usage

```bash
python3 scripts/export_x_cookies_from_chrome.py --output /tmp/x_current_cookies.json

python3 scripts/upload_markdown_to_x_article.py /path/to/article.md \
  --cookies-json /tmp/x_current_cookies.json --dry-run

python3 scripts/upload_markdown_to_x_article.py /path/to/article.md \
  --cookies-json /tmp/x_current_cookies.json

rm -f /tmp/x_current_cookies.json
```

## Privacy

Never commit cookie JSON files. Delete temporary cookies after use.
