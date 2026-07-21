---
name: ky-dy
description: |
  下载抖音公开视频（MP4 + 元数据）。
  触发：/ky-dy、「抖音下载」「下抖音」
---

# ky-dy · 下抖音

**核心：抖音链接 → 本地 MP4。**

脚本由 KY 维护：`scripts/download.py`。

## 用法

1. 用户给链接（`v.douyin.com` 短链先展开为 `www.douyin.com/video/<id>`）  
2. 立刻执行，不要空谈  

```bash
pip install playwright requests
python -m playwright install chromium
python3 "$SKILL_ROOT/scripts/download.py" "URL"
python3 "$SKILL_ROOT/scripts/download.py" "URL" --metadata-only
```

`SKILL_ROOT` = 本文件所在目录。  
默认：`~/Downloads/douyin_<id>.mp4` 与旁路 `*.metadata.json`。

## 限制

- 风控、版权、地区限制可导致失败。  
- 仅合法范围内的个人存档。  
- 不做口播转写（另工具处理）。  

## 完成

```markdown
## ky-dy | 文件 | 标题 | 作者
```
