# ky-wechat-html

**Kiren Yi（KY）** 技能集：Markdown → 微信公众号可粘贴 HTML。

- 调用：`/ky-wechat-html`
- 只做排版，不改观点
- 风格真源：`templates/styles.md`（KY 原创 id 命名）

## 在 Agent 里

```text
/ky-wechat-html
把这篇文章排成公众号 HTML
```

或指定：

```text
/ky-wechat-html essay 风格，文件 path/to/article.md
```

## 与 dbs-wechat-html 的关系

本 skill **借鉴了**「流程分模式 + 样式外置 + 微信兼容约束」的产品结构，  
**不是**对方文案/风格 id/输出目录的复制。风格命名与 CSS 为 KY 重写。

## 安装

在 `ky-skills` 仓库根目录：

```bash
./scripts/install-links.sh ky-wechat-html
```
