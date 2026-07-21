---
name: ky-sph
description: |
  微信视频号下载与公众号 RSS 工作流（编排开源下载器）。
  触发：/ky-sph、「视频号」「sph」「公众号 RSS」
---

# ky-sph · 视频号 / 公众号

**核心：微信 PC 内容 → 本地文件或 RSS。**  
上游：[wx_channels_download](https://github.com/ltaoo/wx_channels_download)（自装，本 skill 只编排）。

## 视频号

1. 管理员运行上游 → 代理成功  
2. 微信 PC 打开视频号，播放后暂停 → 点下载  
3. Agent 不能代点微信 UI  

分享链 `weixin.qq.com/sph/...` 可试：https://sph.litao.workers.dev/

长视频用上游：`download --url ... --key ...`

## 公众号 RSS

上游运行 + 打开任意公众号文章页 →  
`http://127.0.0.1:2022/rss/mp?biz=...` 或 `/mp/home`

## 不做

不内置二进制；不绕过付费墙。

## 完成

```markdown
## ky-sph | 路径 | 结果文件或阻塞原因
```
