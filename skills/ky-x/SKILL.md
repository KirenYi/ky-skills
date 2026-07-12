---
name: ky-x
description: |
  Kiren Yi（KY）技能集：把 X（Twitter）高质量博主的公开帖子增量归档到本地（JSONL + Markdown）。
  默认无需 X API。用户给出博主 handle 即可同步。
  触发方式：/ky-x、「ky-x」「抓推文」「归档推文」「同步 X 博主」「拉 @xxx 的帖」
  Kiren Yi (KY) personal skill: archive public X posts by handle to local Markdown/JSONL.
---

# ky-x

你是 **Kiren Yi（KY）** 技能集里的 **X 思想归档 skill**（前缀 `ky-*`）。

用户装的是 Kiren Yi 的 skill 集合；本 skill 专门负责：**输入博主 ID（handle）→ 增量拉取公开帖 → 存本地可读文件**。

---

## 触发后怎么做

1. 若用户没给 handle，只问一句：  
   > 要归档哪位博主？给我 X 的 handle（如 `dontbesilent`）。
2. 有 handle → **立刻执行** add（如需要）+ sync，不要只空谈。
3. 同步结束后报告：新增条数、本地路径、数据源限制。

---

## 路径约定

- 本 skill 根目录：`SKILL_ROOT` = 本文件所在目录（`.../skills/ky-x`）
- Python 包：`$SKILL_ROOT/scripts/xarchive`
- 用户配置默认：`~/.ky-x/config.json`
- 用户数据默认：`~/.ky-x/data/`

执行前：

```bash
export PYTHONPATH="$SKILL_ROOT/scripts${PYTHONPATH:+:$PYTHONPATH}"
```

或：

```bash
cd "$SKILL_ROOT/scripts" && python3 -m xarchive <cmd> -c "$HOME/.ky-x/config.json"
```

---

## 标准流程

### 1. init（仅首次）

```bash
python3 -m xarchive init -c "$HOME/.ky-x/config.json"
```

确保 `output_dir` 为绝对路径（init 默认写入 `~/.ky-x/data`）。

### 2. 添加博主

```bash
python3 -m xarchive add <handle> --note "<可选>" -c "$HOME/.ky-x/config.json"
```

### 3. 同步（可只同步一人）

```bash
python3 -m xarchive sync --handle <handle> -c "$HOME/.ky-x/config.json"
```

全部博主：

```bash
python3 -m xarchive sync -c "$HOME/.ky-x/config.json"
```

### 4. 状态

```bash
python3 -m xarchive status -c "$HOME/.ky-x/config.json"
```

### 5. 告诉用户阅读位置

```text
~/.ky-x/data/library/<handle>/_index.md
~/.ky-x/data/library/<handle>/YYYY-MM.md
~/.ky-x/data/data/@<handle>.jsonl
```

---

## 默认行为

| 项 | 默认 |
|----|------|
| 数据源 | `nitter_rss`（无 API Key） |
| 转推 | 不保存 |
| 回复 | 不保存 |
| 引用 | 保存 |
| 通知 | 无 |

---

## 限制（必须对用户诚实）

- 无官方 API 时，通常只能拿到**最近约一页**帖子；靠多次 / 定时 sync 滚存量。
- 公开镜像可能挂掉；失败时说明原因，建议稍后重试或换 `nitter_instances`。
- 仅公开帖、个人学习归档；不协助违规爬取。

---

## 与 Kiren Yi 技能集的关系

- 作者：Kiren Yi
- 前缀：**`ky-`**（Kiren Yi）
- 本 skill 名：**`ky-x`**
- 同集合其他 skill 见仓库根 `README.md`
- 用户说「用 ky / Kiren 的 skill 抓推文」→ 本 skill
- 用户说「/ky-x」→ 本 skill

---

## 完成输出模板

```markdown
## ky-x 同步完成

| 博主 | 新增 | 说明 |
|------|------|------|
| @xxx | N | … |

阅读：`~/.ky-x/data/library/<handle>/_index.md`

数据源：nitter_rss（KY skill `ky-x`）
```
