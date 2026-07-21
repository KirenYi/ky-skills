---
name: ky-xhs
description: |
  抓取小红书公开笔记（元数据 / 视频或图片 / 字幕）。
  触发：/ky-xhs、「小红书」「抓笔记」
---

# ky-xhs · 抓小红书

**核心：笔记链接 → 本地目录。**

## 用法

1. 尽量用带 `xsec_token` 的完整链接  
2. 立刻跑脚本  

```bash
pip install requests
python3 "$SKILL_ROOT/scripts/fetch.py" "URL"
python3 "$SKILL_ROOT/scripts/fetch.py" "URL" --skip-media
# 可选：export XHS_COOKIE='...'  （勿提交 git）
```

默认输出：`~/Downloads/xhs_<note_id>/`

## 限制

风控时需 Cookie；直链会过期。仅合法个人存档。

## 完成

```markdown
## ky-xhs | note_id | 类型 | 目录
```
