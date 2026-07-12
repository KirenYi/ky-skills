# ky-wechat-html 样式库（真源）

生成前按 **style id** 找到条目，把下方 CSS 原样放入 HTML 的 `<style>`。

## 预览组合（6）

`clean` · `essay` · `docs` · `pulse` · `ledger` · `lecture`

## 全量

`clean` · `essay` · `docs` · `pulse` · `ledger` · `lecture` · `memo` · `stage`

---

## clean · 净稿

- 别名：默认、极简、干净、报告
- 适合：方法论、诊断稿、默认排版
- 分组：基础

```css
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;font-size:16px;line-height:1.84;color:#2c2c2c;max-width:740px;margin:0 auto;padding:28px 22px;background:#fff;}
h1{font-size:24px;line-height:1.35;font-weight:800;margin:28px 0 22px;color:#111;padding-bottom:14px;border-bottom:2px solid #111;}
h2{font-size:19px;line-height:1.45;font-weight:800;margin:40px 0 14px;color:#111;}
h2:before{content:"";display:block;width:28px;height:3px;background:#111;margin:0 0 10px;}
h3{font-size:17px;line-height:1.5;font-weight:700;margin:28px 0 10px;color:#222;}
p{margin:12px 0;line-height:1.84;}
blockquote{margin:20px 0;padding:12px 16px;border-left:3px solid #111;background:#f6f6f6;color:#555;}
ul{margin:12px 0;padding-left:22px;}
li{margin:7px 0;line-height:1.84;}
strong{font-weight:800;color:#111;}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;background:#f0f0f0;padding:2px 6px;border-radius:3px;font-size:14px;}
pre{background:#f0f0f0;padding:14px 16px;overflow:auto;font-size:14px;line-height:1.6;}
pre code{background:none;padding:0;}
hr{border:none;border-top:1px solid #e2e2e2;margin:32px 0;}
```

---

## essay · 长文

- 别名：随笔、观点、个人长文
- 适合：叙事与议论并重的长文
- 分组：阅读

```css
body{font-family:Georgia,"Times New Roman","Songti SC","Noto Serif CJK SC","PingFang SC",serif;font-size:16px;line-height:1.92;color:#242424;max-width:680px;margin:0 auto;padding:36px 24px;background:#fff;}
h1{font-size:28px;line-height:1.3;font-weight:700;margin:36px 0 26px;color:#111;}
h2{font-size:22px;line-height:1.35;font-weight:700;margin:48px 0 16px;color:#111;}
h3{font-size:18px;line-height:1.45;font-weight:700;margin:32px 0 12px;color:#333;}
p{margin:15px 0;line-height:1.92;}
blockquote{margin:26px 0;padding:0 0 0 20px;border-left:3px solid #333;color:#444;font-size:17px;line-height:1.88;font-style:italic;}
ul{margin:14px 0;padding-left:24px;}
li{margin:8px 0;line-height:1.9;}
strong{font-weight:800;color:#111;}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;background:#f3f3f3;padding:2px 6px;border-radius:3px;font-size:14px;}
pre{background:#f3f3f3;padding:14px 16px;overflow:auto;font-size:14px;line-height:1.6;}
pre code{background:none;padding:0;}
hr{border:none;border-top:1px solid #ddd;margin:40px auto;width:36%;}
```

---

## docs · 说明书

- 别名：教程、文档、步骤、工具说明
- 适合：可执行说明、操作指南
- 分组：工具

```css
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;font-size:16px;line-height:1.78;color:#2a3142;max-width:760px;margin:0 auto;padding:26px 22px;background:#fafbff;}
h1{font-size:25px;line-height:1.32;font-weight:800;margin:32px 0 22px;color:#0f1c33;}
h2{font-size:19px;line-height:1.45;font-weight:800;margin:40px 0 12px;color:#0f1c33;padding:10px 12px;background:#eef2ff;border-left:4px solid #3b5bdb;}
h3{font-size:17px;line-height:1.5;font-weight:750;margin:28px 0 10px;color:#3d4a63;}
p{margin:12px 0;}
blockquote{margin:18px 0;padding:12px 14px;background:#fff;border:1px solid #dbe3f4;border-left:4px solid #3b5bdb;color:#3d4a63;}
ul{margin:12px 0;padding-left:0;list-style:none;counter-reset:ky;}
li{margin:8px 0;padding:9px 10px;background:#fff;border:1px solid #e5ebf5;line-height:1.76;}
li:before{counter-increment:ky;content:counter(ky, decimal-leading-zero) " ";font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px;color:#3b5bdb;font-weight:800;}
strong{font-weight:800;color:#0f1c33;}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;background:#e8edff;color:#2b3f9a;padding:2px 6px;border-radius:4px;font-size:14px;}
pre{background:#e8edff;color:#2b3f9a;padding:14px 16px;overflow:auto;font-size:14px;line-height:1.6;}
pre code{background:none;padding:0;}
hr{border:none;border-top:1px solid #dbe3f4;margin:30px 0;}
```

---

## pulse · 脉冲

- 别名：科技、产品、冲击、发布
- 适合：科技观点、产品叙事
- 分组：节奏

```css
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;font-size:16px;line-height:1.74;color:#121212;max-width:750px;margin:0 auto;padding:24px 22px;background:#fff;}
h1{font-size:27px;line-height:1.18;font-weight:900;margin:32px 0 24px;color:#111;border-top:5px solid #111;border-bottom:5px solid #111;padding:14px 0;}
h2{font-size:20px;line-height:1.35;font-weight:900;margin:40px 0 12px;color:#111;background:#d8ff3c;padding:10px 12px;}
h3{font-size:18px;line-height:1.4;font-weight:850;margin:28px 0 10px;color:#111;text-decoration:underline;text-decoration-thickness:3px;text-decoration-color:#1ec8ff;text-underline-offset:5px;}
p{margin:12px 0;}
blockquote{margin:20px 0;padding:14px 16px;background:#111;color:#fff;font-weight:700;}
ul{margin:12px 0;padding-left:0;list-style:none;}
li{margin:8px 0;padding:8px 10px;background:#f3f3f3;border-left:5px solid #111;line-height:1.72;}
strong{font-weight:900;background:#d8ff3c;color:#111;}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;background:#111;color:#1ec8ff;padding:2px 6px;font-size:14px;}
pre{background:#111;color:#1ec8ff;padding:14px 16px;overflow:auto;font-size:14px;line-height:1.6;}
pre code{background:none;padding:0;color:inherit;}
hr{border:none;height:4px;background:#111;margin:32px 0;}
```

---

## ledger · 账本

- 别名：商业、分析、财经感、判断
- 适合：商业复盘、市场判断
- 分组：判断

```css
body{font-family:Georgia,"Times New Roman","Songti SC","Noto Serif CJK SC","PingFang SC",serif;font-size:16px;line-height:1.9;color:#2a241c;max-width:740px;margin:0 auto;padding:26px 22px;background:#fff8ef;}
h1{font-size:26px;line-height:1.3;font-weight:800;margin:34px 0 22px;color:#14110d;border-bottom:3px double #6b573f;padding-bottom:12px;}
h2{font-size:20px;line-height:1.42;font-weight:800;margin:42px 0 14px;color:#3a2f22;padding-top:8px;border-top:1px solid #8a7356;}
h3{font-size:18px;line-height:1.5;font-weight:750;margin:28px 0 10px;color:#4a3c2c;}
p{margin:13px 0;}
blockquote{margin:20px 0;padding:12px 0 12px 16px;border-left:4px solid #8a7356;background:#f6e6d0;color:#4a3c2c;}
ul{margin:12px 0;padding-left:22px;}
li{margin:7px 0;line-height:1.9;}
strong{font-weight:850;color:#14110d;}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;background:#f0dcc2;padding:2px 6px;border-radius:2px;font-size:14px;}
pre{background:#f0dcc2;padding:14px 16px;overflow:auto;font-size:14px;line-height:1.6;}
pre code{background:none;padding:0;}
hr{border:none;border-top:1px solid #8a7356;margin:32px 0;width:56%;}
```

---

## lecture · 讲义

- 别名：课程、学习、笔记
- 适合：结构化讲授、知识点罗列
- 分组：学习

```css
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;font-size:16px;line-height:1.82;color:#243044;max-width:740px;margin:0 auto;padding:26px 22px;background:#fff;}
h1{font-size:24px;line-height:1.35;font-weight:800;margin:28px 0 18px;color:#143a66;padding:12px 14px;background:#eaf3ff;border-radius:8px;}
h2{font-size:19px;line-height:1.45;font-weight:800;margin:36px 0 12px;color:#143a66;}
h2:before{content:"§ ";color:#3b82f6;}
h3{font-size:17px;line-height:1.5;font-weight:750;margin:26px 0 10px;color:#2b4a72;}
p{margin:12px 0;}
blockquote{margin:18px 0;padding:12px 14px;background:#f3f8ff;border-left:4px solid #3b82f6;color:#334e6d;}
ul{margin:12px 0;padding-left:22px;}
li{margin:7px 0;line-height:1.82;}
strong{font-weight:800;color:#143a66;}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;background:#e8f0fe;color:#1e40af;padding:2px 6px;border-radius:4px;font-size:14px;}
pre{background:#e8f0fe;color:#1e40af;padding:14px 16px;overflow:auto;font-size:14px;line-height:1.6;}
pre code{background:none;padding:0;}
hr{border:none;border-top:1px dashed #b6c8e0;margin:30px 0;}
```

---

## memo · 备忘

- 别名：复盘、内部、笔记
- 适合：项目备忘、轻量总结
- 分组：笔记

```css
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;font-size:16px;line-height:1.82;color:#37352f;max-width:720px;margin:0 auto;padding:28px 24px;background:#fffcf7;}
h1{font-size:26px;line-height:1.3;font-weight:780;margin:32px 0 20px;color:#37352f;}
h2{font-size:19px;line-height:1.45;font-weight:720;margin:36px 0 12px;color:#37352f;background:#f4f1ea;padding:9px 12px;}
h3{font-size:17px;line-height:1.5;font-weight:720;margin:26px 0 10px;color:#37352f;}
p{margin:12px 0;}
blockquote{margin:18px 0;padding:12px 14px;border-left:3px solid #9b9a97;background:#f4f1ea;color:#4f4d48;}
ul{margin:12px 0;padding-left:22px;}
li{margin:7px 0;line-height:1.82;}
strong{font-weight:800;background:#fff2b8;color:#37352f;}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;background:#efece6;padding:2px 6px;border-radius:3px;font-size:14px;}
pre{background:#efece6;padding:14px 16px;overflow:auto;font-size:14px;line-height:1.6;}
pre code{background:none;padding:0;}
hr{border:none;border-top:1px solid #e5e0d6;margin:30px 0;}
```

---

## stage · 发布台

- 别名：活动、招募、公告、转化
- 适合：活动通知、报名说明
- 分组：行动

```css
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;font-size:16px;line-height:1.8;color:#1f2933;max-width:740px;margin:0 auto;padding:26px 22px;background:#fff;}
h1{font-size:26px;line-height:1.28;font-weight:900;margin:28px 0 20px;color:#fff;background:linear-gradient(90deg,#111 0%,#333 100%);padding:16px 18px;}
h2{font-size:19px;line-height:1.4;font-weight:850;margin:36px 0 12px;color:#111;padding-left:12px;border-left:6px solid #ef4444;}
h3{font-size:17px;line-height:1.45;font-weight:800;margin:26px 0 10px;color:#222;}
p{margin:12px 0;}
blockquote{margin:18px 0;padding:14px 16px;background:#fff5f5;border:1px solid #fecaca;color:#7f1d1d;font-weight:650;}
ul{margin:12px 0;padding-left:0;list-style:none;}
li{margin:8px 0;padding:10px 12px;background:#f9fafb;border-left:4px solid #111;line-height:1.78;}
strong{font-weight:900;color:#b91c1c;}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;background:#111;color:#fef2f2;padding:2px 6px;font-size:14px;}
pre{background:#111;color:#fef2f2;padding:14px 16px;overflow:auto;font-size:14px;line-height:1.6;}
pre code{background:none;padding:0;color:inherit;}
hr{border:none;height:3px;background:#111;margin:30px 0;width:40%;}
```
