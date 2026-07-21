---
name: ky-xhs
description: |
  抓取小红书公开笔记：元数据、视频/图片、字幕与口播文本（若有）。
  触发：/ky-xhs、「抓小红书」「下载小红书」「xhs 笔记」
  Fetch public Xiaohongshu notes (metadata, video/images, subtitles when available).
---

# ky-xhs

**输入小红书笔记链接 → 本地目录（html / metadata / 媒体）。**

## 触发后怎么做

1. 无链接则只问一句：笔记 URL？  
2. 有链接 → 立刻执行 `scripts/fetch.py`。  
3. 尽量使用带 `xsec_token` 的完整链接。  
4. 失败时提示设置临时环境变量 `XHS_COOKIE`（浏览器登录后复制，**不写入仓库**）。  
5. 报告输出目录与类型（video / 图文）。

## 路径

- `SKILL_ROOT` = 本文件所在目录  
- 脚本：`$SKILL_ROOT/scripts/fetch.py`

## 依赖

```bash
pip install requests
```

## 命令

```bash
python3 "$SKILL_ROOT/scripts/fetch.py" "https://www.xiaohongshu.com/explore/<id>?xsec_token=..."
python3 "$SKILL_ROOT/scripts/fetch.py" "URL" "/path/out_dir"
python3 "$SKILL_ROOT/scripts/fetch.py" "URL" --skip-media
```

可选登录态：

```bash
export XHS_COOKIE='your_cookie_here'   # 仅进程内；勿提交 git
```

默认输出：`~/Downloads/xhs_<note_id>/`

## 限制

- 强依赖页面 `__INITIAL_STATE__`；风控时需 Cookie 或新 token。  
- 视频直链会过期，需重抓。  
- 仅个人学习与合法存档。  
- 不默认写入任何云表格；本地文件为真源。

## 完成模板

```markdown
## ky-xhs

| 项 | 内容 |
|----|------|
| note_id | |
| 类型 | |
| 目录 | |
| 说明 | |
```
