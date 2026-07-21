---
name: ky-x-article
description: |
  将本地 Markdown 上传为 X（Twitter）Articles 草稿（默认不点发布）。
  Playwright 独立浏览器 + 从本机 Chrome 导出的临时 cookies。
  触发：/ky-x-article、「上传 X 长文」「X Article 草稿」「Markdown 发 X 文章」
  Upload local Markdown to an X Articles draft (never publish unless user confirms).
---

# ky-x-article

**Markdown → X Articles 草稿。** 默认只保存草稿。

## 硬性原则

1. **除非用户明确说可以公开发布，否则绝不点击「发布」。**  
2. 使用独立 Playwright 浏览器，不抢用户当前 Chrome 窗口。  
3. Cookie 仅临时文件；用完删除；不进 git。  
4. 建议文章**第一个有效块是封面图**；否则先 dry-run 并提醒。

## 依赖

```bash
pip install playwright pycryptodome
python -m playwright install chromium
```

Chrome 需已登录 x.com。

## 路径

- `SKILL_ROOT` = 本文件所在目录  
- 脚本：`$SKILL_ROOT/scripts/`

## 流程

### 1. 导出 cookies

```bash
python3 "$SKILL_ROOT/scripts/export_x_cookies_from_chrome.py" --output /tmp/x_current_cookies.json
```

Windows 可用 `%TEMP%\x_current_cookies.json`。

### 2. dry-run（不打开 X）

```bash
python3 "$SKILL_ROOT/scripts/upload_markdown_to_x_article.py" "/abs/path/article.md" \
  --cookies-json /tmp/x_current_cookies.json --dry-run
```

若提示缺少封面图 → 停下让用户加图。仅当用户明确拒绝封面时加 `--allow-no-cover`。

### 3. 上传草稿

```bash
python3 "$SKILL_ROOT/scripts/upload_markdown_to_x_article.py" "/abs/path/article.md" \
  --cookies-json /tmp/x_current_cookies.json
```

### 4. 清理

```bash
rm -f /tmp/x_current_cookies.json
```

## 常见问题

| 现象 | 处理 |
|------|------|
| 跳转登录 | 重导 cookies |
| 封面遮罩 | 脚本会点「应用」；失败则人工点一次 |
| 图位错 | 新建干净草稿重跑 |

## 完成模板

```markdown
## ky-x-article

| 项 | 内容 |
|----|------|
| 文章 | |
| 草稿 URL | |
| dry-run | |
| cookies | 已删除 / 待删 |
```
