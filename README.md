# ky-skills

**Kiren Yi（KY）** 的个人 Agent Skill 集合。

统一前缀：`ky-`（Kiren Yi）

用 Claude Code / Codex / Grok / 豆包 等 Agent 时，安装本仓库后即可通过 `/ky-x` 这类命令调用对应能力。

| Skill | 说明 | 状态 |
|-------|------|------|
| [`ky-x`](./skills/ky-x/) | 把 X（Twitter）博主公开帖子增量归档到本地（JSONL + Markdown） | ✅ v0.1 |

---

## 这是什么

这不是一个网页 App，而是一套 **可安装的 Agent Skill**：

1. **给人看的文档**（本 README）
2. **给 Agent 看的说明**（每个 skill 目录下的 `SKILL.md`）
3. **真正干活的脚本**（如 `ky-x` 里的 Python 包）

设计目标：

- **有品牌**：前缀固定为 `ky-`，方便用户记忆「这是 Kiren Yi 的工具」
- **可扩展**：新能力以 `ky-<name>` 形式加入 `skills/`
- **可落地**：装上就能跑，不强制先申请 X API

---

## 环境要求

- macOS / Linux（Windows 可用 WSL）
- Python **3.10+**
- 任意支持 Skills 目录的 Agent（Claude Code、Codex、Grok、`~/.agents/skills` 等）
- 网络（`ky-x` 默认通过公开 RSS 镜像拉帖）

`ky-x` 的 Python 部分 **零第三方依赖**（仅标准库）。

---

## 安装

### 1. 克隆仓库

```bash
git clone https://github.com/KirenYi/ky-skills.git ~/ky-skills
cd ~/ky-skills
```

### 2. 挂到各 Agent 的 skills 目录

一键软链（推荐）：

```bash
./scripts/install-links.sh
```

这会把 `skills/ky-*` 链到：

- `~/.agents/skills/`
- `~/.claude/skills/`
- `~/.codex/skills/`
- `~/.grok/skills/`

只装某一个：

```bash
./scripts/install-links.sh ky-x
```

手动示例：

```bash
ln -sfn ~/ky-skills/skills/ky-x ~/.agents/skills/ky-x
```

### 3. 在 Agent 里调用

```text
/ky-x
抓取 @dontbesilent
```

或：

```text
用 ky-x 同步 naval 的推文
```

---

## 使用 `ky-x`（命令行）

不经过 Agent 也可以直接跑：

```bash
export PYTHONPATH=~/ky-skills/skills/ky-x/scripts

# 首次：生成配置（默认数据目录 ~/.ky-x/data）
python3 -m xarchive init -c ~/.ky-x/config.json

# 添加博主
python3 -m xarchive add dontbesilent --note "商业/开源" -c ~/.ky-x/config.json

# 同步（可指定单人）
python3 -m xarchive sync --handle dontbesilent -c ~/.ky-x/config.json

# 查看状态
python3 -m xarchive status -c ~/.ky-x/config.json
```

### 读哪里

```text
~/.ky-x/data/library/<handle>/_index.md    # 入口
~/.ky-x/data/library/<handle>/YYYY-MM.md   # 按月
~/.ky-x/data/data/@<handle>.jsonl          # 机器可读真源
```

### 配置要点

见 [`skills/ky-x/scripts/config.example.json`](./skills/ky-x/scripts/config.example.json)。

| 字段 | 含义 |
|------|------|
| `output_dir` | 归档根目录（建议绝对路径） |
| `authors` | 博主列表 `handle` + 可选 `note` |
| `filters.include_retweets` | 是否存转推（默认 `false`） |
| `filters.include_replies` | 是否存回复（默认 `false`） |
| `nitter_instances` | 公开 RSS 镜像列表 |

---

## 能力与限制（请先读）

**能做**

- 多博主增量同步
- 本地 Markdown 精读
- 过滤转推 / 回复（启发式）
- 无 X API 即可起步

**不能保证**

- 一次拉全历史
- 公开镜像 100% 可用
- 与官网逐字完全一致
- 实时推送 / 通知

默认数据源是 Nitter 等公开 RSS，通常只有**最近约一页**帖子。长期使用靠多次或定时 `sync` 滚存量。更稳的官方 API 接入见 [`skills/ky-x/references/roadmap.md`](./skills/ky-x/references/roadmap.md)。

仅供个人学习与研究；请遵守 X 服务条款与当地法律。

---

## 仓库结构

```text
ky-skills/
├── README.md                 # 你正在读的说明
├── LICENSE                   # MIT
├── VERSION                   # 集合版本
├── scripts/
│   └── install-links.sh      # 多端软链安装
├── skills/
│   └── ky-x/                 # 单个 skill（可独立软链）
│       ├── SKILL.md          # Agent 行为说明（核心）
│       ├── README.md
│       ├── VERSION
│       ├── scripts/          # 可执行逻辑
│       └── references/       # 数据源 / 路线图 / changelog
└── templates/                # 新建 ky-* 的骨架
```

---

## 开发：新增一个 `ky-*` skill

```bash
cp -R templates/skill-skeleton skills/ky-<短名>
# 编辑 skills/ky-<短名>/SKILL.md
# 如需脚本，放进 skills/ky-<短名>/scripts/
# 更新本 README 的 skill 表格
./scripts/install-links.sh ky-<短名>
```

命名规则：小写、`ky-` 前缀、尽量短。详见 [`templates/README.md`](./templates/README.md)。

---

## 版本

- 集合版本：根目录 [`VERSION`](./VERSION)
- `ky-x` 版本：[`skills/ky-x/VERSION`](./skills/ky-x/VERSION)
- 变更记录：[`skills/ky-x/references/changelog.md`](./skills/ky-x/references/changelog.md)

---

## 作者

**Kiren Yi**（KY）

- GitHub: [KirenYi](https://github.com/KirenYi)

---

## License

[MIT](./LICENSE)
