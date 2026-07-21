# ky-douyin

Download public Douyin videos with Playwright (intercept `aweme/detail`) and save MP4 + metadata JSON.

## Install deps

```bash
pip install playwright requests
python -m playwright install chromium
```

## Usage

```bash
python3 scripts/download.py "https://www.douyin.com/video/<id>"
python3 scripts/download.py "URL" --metadata-only
```

## Notes

- Platform APIs change; failures are expected under risk control.
- Personal learning / lawful local archive only.
