---
name: ky-wx-channels
description: |
  微信视频号 / 公众号内容本地获取工作流。编排开源工具 wx_channels_download（代理注入下载、分享链解析、公众号 RSS），不自研微信爬虫内核。
  触发：/ky-wx-channels、「视频号下载」「微信视频号」「公众号 RSS」「sph 链接」
  WeChat Channels / Official Account capture workflow via upstream open-source downloader.
---

# ky-wx-channels

**微信 PC 生态内容 → 本地文件 / RSS。**  
上游工具：[ltaoo/wx_channels_download](https://github.com/ltaoo/wx_channels_download)（独立安装，本 skill 只编排用法）。

## 触发后怎么做

### A. 视频号下载（主路径）

1. 确认用户已安装上游构建包（[Releases](https://github.com/ltaoo/wx_channels_download/releases)）。  
2. **Windows 管理员运行**上游程序 → 装证书 → 代理启动成功。  
3. 打开 **微信 PC → 视频号**，打开目标视频。  
4. **播放后暂停**，点页面下载按钮（或悬浮按钮）。  
5. 记录下载目录中的文件路径，反馈给用户。  
6. Agent **不能**代替用户点击微信 UI。

### B. 分享链解析

- 链接形如 `https://weixin.qq.com/sph/...`  
- 可尝试上游文档中的在线解析页：https://sph.litao.workers.dev/  
- 拿到直链后用户自行保存；失败则走 A。

### C. 长视频 CLI（上游）

详情页「打印下载命令」后类似：

```bash
wx_video_download download --url "..." --key <key> --filename "out.mp4"
```

### D. 公众号列表 / RSS（上游）

1. 上游运行中，并打开任意公众号文章页（保持连接）。  
2. 管理页示例：`http://127.0.0.1:2022/mp/home`  
3. RSS 示例：`http://127.0.0.1:2022/rss/mp?biz=...`（`content=1` 可带正文）  
4. 凭证约 30 分钟失效；不宜监控过多账号（上游文档有风控说明）。

## 本 skill 不做什么

- 不内置 Go 二进制或解密实现  
- 不绕过付费墙 / 不协助侵权  
- 不自动点微信界面  

## 与其它 ky skill

| 需求 | skill |
|------|--------|
| 抖音 | `ky-douyin` |
| 小红书 | `ky-xhs` |
| X 归档 | `ky-x` |
| 公众号排版 HTML | `ky-wechat-html`（排版，不是抓取） |

## 合规

遵守上游免责声明与当地法律；仅个人学习与合法存档。

## 完成模板

```markdown
## ky-wx-channels

| 项 | 内容 |
|----|------|
| 路径 | UI下载 / sph解析 / CLI / 公众号RSS / 仅说明 |
| 结果 | 文件路径或阻塞原因 |
| 下一步 | 转写 / 蒸馏 / 无 |
```
