---
name: ky-xdraft
description: |
  Markdown 上传为 X 长文草稿（默认不发布）。
  触发：/ky-xdraft、「X 草稿」「X Article」「上 X 长文」
---

# ky-xdraft · X 长文草稿

**核心：本地 Markdown → X Articles 草稿。**

## 硬规则

- **不点「发布」**，除非用户明确确认  
- 独立 Playwright 浏览器；临时 cookies，用完删除  

## 用法

```bash
pip install playwright pycryptodome
python -m playwright install chromium

python3 "$SKILL_ROOT/scripts/export_x_cookies_from_chrome.py" --output /tmp/x_cookies.json
python3 "$SKILL_ROOT/scripts/upload_markdown_to_x_article.py" "/abs/article.md" \
  --cookies-json /tmp/x_cookies.json --dry-run
python3 "$SKILL_ROOT/scripts/upload_markdown_to_x_article.py" "/abs/article.md" \
  --cookies-json /tmp/x_cookies.json
rm -f /tmp/x_cookies.json
```

建议正文**第一张有效内容是封面图**；否则 dry-run 停下。

## 完成

```markdown
## ky-xdraft | 草稿 URL | cookies 已删?
```
