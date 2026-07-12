# ky-wechat-html 样式库（真源）

> **字体**：须遵守仓库 `docs/FONT_LICENSE.md`。仅使用可商用公开字体或系统回退栈；禁止未授权商用字库。

生成前按 **style id** 找到条目，把下方 CSS 原样放入 HTML 的 `<style>`。

## 预览组合（6）

`clean` · `essay` · `docs` · `pulse` · `ledger` · `lecture`

## 全量（13）

`clean` · `essay` · `docs` · `pulse` · `ledger` · `lecture` · `memo` · `stage` · `ink` · `cream` · `swiss` · `night` · `fresh`

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

---

## ink · 宣纸

- 别名：水墨、国风、文人、文艺
- 适合：人文、哲思、引用感强的长文（如纳瓦尔类）
- 分组：人文
- 灵感：中文公众号「宣纸/留白」范式 + 传统阅读节奏（非抄某站模板）

```css
body{font-family:"Songti SC","Noto Serif CJK SC","PingFang SC","STSong",serif;font-size:16px;line-height:1.95;color:#2a2622;max-width:700px;margin:0 auto;padding:32px 24px;background:#f7f1e6;}
h1{font-size:26px;line-height:1.35;font-weight:700;margin:36px 0 28px;color:#1a1612;text-align:center;letter-spacing:0.06em;}
h1:after{content:"";display:block;width:36px;height:1px;background:#8b7355;margin:18px auto 0;}
h2{font-size:20px;line-height:1.45;font-weight:700;margin:46px 0 16px;color:#1a1612;text-align:center;}
h3{font-size:17px;line-height:1.5;font-weight:700;margin:30px 0 12px;color:#3d342c;}
p{margin:14px 0;line-height:1.95;text-align:justify;}
blockquote{margin:26px 24px;padding:0;border-left:0;color:#5c5044;font-size:15px;line-height:1.9;text-align:center;font-style:normal;}
blockquote:before{content:"「";color:#a0896c;font-size:22px;}
blockquote:after{content:"」";color:#a0896c;font-size:22px;}
ul{margin:14px 0;padding-left:22px;}
li{margin:8px 0;line-height:1.9;}
strong{font-weight:800;color:#1a1612;}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;background:#ebe2d2;padding:2px 6px;border-radius:2px;font-size:14px;}
pre{background:#ebe2d2;padding:14px 16px;overflow:auto;font-size:14px;line-height:1.6;}
pre code{background:none;padding:0;}
hr{border:none;border-top:1px solid #c4b59a;margin:36px auto;width:28%;}
```

---

## cream · 奶刊

- 别名：Newsletter、Substack感、订阅信、奶油底
- 适合：个人通讯、系列专栏、温和说理
- 分组：订阅
- 灵感：Substack / 邮件 newsletter 常见奶油底 + 强调色点缀

```css
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;font-size:16px;line-height:1.86;color:#292524;max-width:680px;margin:0 auto;padding:30px 24px;background:#fffaf3;}
h1{font-size:27px;line-height:1.28;font-weight:800;margin:32px 0 10px;color:#1c1917;}
h1+p,h1+h2{/* spacing */;}
h2{font-size:19px;line-height:1.4;font-weight:800;margin:40px 0 12px;color:#1c1917;padding-bottom:8px;border-bottom:2px solid #fb923c;}
h3{font-size:17px;line-height:1.45;font-weight:750;margin:28px 0 10px;color:#44403c;}
p{margin:13px 0;line-height:1.86;}
blockquote{margin:22px 0;padding:14px 16px;background:#fff7ed;border-left:4px solid #ea580c;color:#44403c;}
ul{margin:12px 0;padding-left:22px;}
li{margin:7px 0;line-height:1.84;}
strong{font-weight:800;color:#c2410c;}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;background:#ffedd5;color:#9a3412;padding:2px 6px;border-radius:4px;font-size:14px;}
pre{background:#ffedd5;color:#9a3412;padding:14px 16px;overflow:auto;font-size:14px;line-height:1.6;}
pre code{background:none;padding:0;}
hr{border:none;border-top:1px dashed #fdba74;margin:32px 0;}
```

---

## swiss · 网格

- 别名：瑞士、Bauhaus、大留白、现代主义
- 适合：品牌感强、结构清晰的深度文
- 分组：设计
- 灵感：Swiss Style / 国际字体风格：大字号标题、克制色、明确层级

```css
body{font-family:-apple-system,BlinkMacSystemFont,"Helvetica Neue","PingFang SC","Microsoft YaHei",sans-serif;font-size:16px;line-height:1.78;color:#0a0a0a;max-width:720px;margin:0 auto;padding:40px 28px;background:#fff;}
h1{font-size:32px;line-height:1.12;font-weight:800;margin:24px 0 28px;color:#0a0a0a;letter-spacing:-0.02em;}
h2{font-size:14px;line-height:1.4;font-weight:800;margin:48px 0 16px;color:#0a0a0a;text-transform:uppercase;letter-spacing:0.14em;padding-top:16px;border-top:1px solid #0a0a0a;}
h3{font-size:18px;line-height:1.4;font-weight:700;margin:28px 0 10px;color:#0a0a0a;}
p{margin:14px 0;line-height:1.82;max-width:38em;}
blockquote{margin:28px 0;padding:0 0 0 16px;border-left:2px solid #0a0a0a;color:#404040;font-size:15px;}
ul{margin:14px 0;padding-left:18px;}
li{margin:8px 0;line-height:1.8;}
strong{font-weight:800;color:#0a0a0a;}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;background:#f4f4f5;padding:2px 6px;border-radius:0;font-size:13px;}
pre{background:#f4f4f5;padding:16px;overflow:auto;font-size:13px;line-height:1.55;}
pre code{background:none;padding:0;}
hr{border:none;border-top:1px solid #0a0a0a;margin:40px 0;width:48px;}
```

---

## night · 夜读

- 别名：暗色、夜间、深色模式
- 适合：夜读感、科技随笔、降低刺眼
- 分组：阅读
- 灵感：暗色阅读模式 / 代码编辑器夜色（注意公众号预览仍可能被外壳影响）

```css
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;font-size:16px;line-height:1.86;color:#e4e4e7;max-width:720px;margin:0 auto;padding:28px 22px;background:#18181b;}
h1{font-size:26px;line-height:1.28;font-weight:800;margin:30px 0 22px;color:#fafafa;}
h2{font-size:19px;line-height:1.4;font-weight:800;margin:40px 0 12px;color:#fafafa;padding-left:12px;border-left:3px solid #a78bfa;}
h3{font-size:17px;line-height:1.45;font-weight:750;margin:28px 0 10px;color:#d4d4d8;}
p{margin:13px 0;line-height:1.86;color:#d4d4d8;}
blockquote{margin:20px 0;padding:14px 16px;background:#27272a;border-left:3px solid #a78bfa;color:#e4e4e7;}
ul{margin:12px 0;padding-left:22px;}
li{margin:7px 0;line-height:1.84;color:#d4d4d8;}
strong{font-weight:800;color:#f5f3ff;}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;background:#27272a;color:#c4b5fd;padding:2px 6px;border-radius:4px;font-size:14px;}
pre{background:#27272a;color:#c4b5fd;padding:14px 16px;overflow:auto;font-size:14px;line-height:1.6;}
pre code{background:none;padding:0;}
hr{border:none;border-top:1px solid #3f3f46;margin:32px 0;}
```

---

## fresh · 青芽

- 别名：小清新、浅绿、生活感、柔和
- 适合：生活、成长、轻量观点、女向/生活方式号
- 分组：生活
- 灵感：国内公众号常见「小清新」浅绿留白（秀米类模板气质，自研色板）

```css
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;font-size:16px;line-height:1.88;color:#334155;max-width:720px;margin:0 auto;padding:28px 22px;background:#f7fdf9;}
h1{font-size:25px;line-height:1.32;font-weight:800;margin:30px 0 20px;color:#14532d;text-align:center;}
h2{font-size:19px;line-height:1.42;font-weight:800;margin:38px 0 12px;color:#166534;padding:8px 12px;background:#dcfce7;border-radius:8px;}
h3{font-size:17px;line-height:1.5;font-weight:750;margin:26px 0 10px;color:#15803d;}
p{margin:12px 0;line-height:1.88;}
blockquote{margin:20px 0;padding:14px 16px;background:#fff;border:1px solid #bbf7d0;border-radius:10px;color:#3f6212;box-shadow:0 1px 0 #dcfce7;}
ul{margin:12px 0;padding-left:0;list-style:none;}
li{margin:8px 0;padding:9px 12px;background:#fff;border-radius:8px;border:1px solid #e2e8f0;line-height:1.8;}
li:before{content:"🌱 ";}
strong{font-weight:800;color:#166534;}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;background:#dcfce7;color:#14532d;padding:2px 6px;border-radius:4px;font-size:14px;}
pre{background:#dcfce7;color:#14532d;padding:14px 16px;overflow:auto;font-size:14px;line-height:1.6;border-radius:8px;}
pre code{background:none;padding:0;}
hr{border:none;border-top:1px dashed #86efac;margin:30px auto;width:50%;}
```
