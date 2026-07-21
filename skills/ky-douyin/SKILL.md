---
name: ky-douyin
description: |
  下载抖音公开视频到本地（Playwright 拦截 aweme/detail 取播放地址 + metadata）。
  触发：/ky-douyin、「下载抖音」「抓抖音视频」「douyin 下载」
  Download public Douyin videos via Playwright network intercept.
---

# ky-douyin

**输入抖音链接 → 本地 MP4 + JSON 元数据。**

## 触发后怎么做

1. 若无链接，只问一句：抖音视频 URL 是什么？  
2. 有链接 → 立刻跑脚本（不要只空谈）。  
3. 短链 `v.douyin.com`：先展开成 `www.douyin.com/video/<id>` 再下载。  
4. 报告：路径、标题、作者、限制说明。

## 路径

- `SKILL_ROOT` = 本文件所在目录  
- 脚本：`$SKILL_ROOT/scripts/download.py`

## 依赖

```bash
pip install playwright requests
python -m playwright install chromium
```

## 命令

```bash
python3 "$SKILL_ROOT/scripts/download.py" "https://www.douyin.com/video/<id>"
python3 "$SKILL_ROOT/scripts/download.py" "URL" "/path/out.mp4"
python3 "$SKILL_ROOT/scripts/download.py" "URL" --metadata-only
```

Windows：

```powershell
python "$env:USERPROFILE\.ky-skills\skills\ky-douyin\scripts\download.py" "URL"
```

默认输出：`~/Downloads/douyin_<id>.mp4` 与旁路 `*.metadata.json`。

## 限制（诚实）

- 公开页可拦截时可用；登录墙 / 版权 / 风控会导致失败。  
- 不保证无水印永久可用；平台接口会变。  
- 仅个人学习与合法存档；不协助侵权搬运。  
- 本 skill **不**做口播转写；转写用本地 whisper 等另工具。

## 完成模板

```markdown
## ky-douyin

| 项 | 内容 |
|----|------|
| 标题 | |
| 作者 | |
| 文件 | |
| 元数据 | |
| 说明 | |
```
