---
name: ky-xhs
description: |
  抓取小红书公开笔记（元数据 / 视频或图片 / 字幕）。
  触发：/ky-xhs、「小红书」「抓笔记」
---

# ky-xhs · 抓小红书

**核心：笔记链接 → 本地目录。**

脚本由 KY 维护：`scripts/fetch.py`。

## 用法

1. 尽量使用带访问参数的完整链接  
2. 立刻跑脚本  

```bash
pip install requests
python3 "$SKILL_ROOT/scripts/fetch.py" "URL"
python3 "$SKILL_ROOT/scripts/fetch.py" "URL" --skip-media
```

可选：`export XHS_COOKIE='...'`（仅进程内，勿提交 Git）。  
默认输出：`~/Downloads/xhs_<note_id>/`

## 限制

- 页面结构或风控变化时可能失败。  
- 仅合法范围内的个人存档。  

## 完成

```markdown
## ky-xhs | note_id | 类型 | 目录
```
