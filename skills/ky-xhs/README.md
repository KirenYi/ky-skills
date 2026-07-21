# ky-xhs

Fetch public Xiaohongshu notes into a local folder (HTML snapshot, metadata JSON, video/images/subtitles when available).

## Usage

```bash
pip install requests
python3 scripts/fetch.py "https://www.xiaohongshu.com/explore/<id>?xsec_token=..."
python3 scripts/fetch.py "URL" --skip-media
```

Optional: `XHS_COOKIE` env for logged-in HTML. Never commit cookies.
