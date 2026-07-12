# SOURCE_OF_TRUTH.md

本文件标明 **ky-skills** 仓库内「谁说了算」。

## 真源层级

```text
1. skills/<ky-name>/          ← Skill 实现与 Agent 工作流（最高优先级）
2. AGENTS.md                  ← 多 Agent 协作与仓库纪律
3. docs/PROGRESS.md           ← 跨工具进度与交接（时间序）
4. README.md                  ← 面向人类用户的安装与说明
5. ~/.*/skills/<name>         ← 仅 bridge / 软链，不是真源
```

## 路径对照

| 你想改的东西 | 应改的位置 |
|--------------|------------|
| `/ky-x` 怎么执行 | `skills/ky-x/SKILL.md` + `skills/ky-x/scripts/` |
| 用户怎么安装到各端 | `scripts/install-links.sh` + `docs/MULTI_HOST.md` + `README.md` |
| 多工具如何避免打架 | `AGENTS.md` + `docs/PROGRESS.md` |
| 版本号 | 集合：`VERSION`；单 skill：`skills/<name>/VERSION` |

## Bridge 规则

- Bridge / 软链目录：**只指向** 本仓库 `skills/`，不承载长期逻辑。
- 发现 bridge 与真源内容不一致：删掉错误副本，重建软链，**以 git 中 skills/ 为准**。

## 用户数据

| 路径 | 是否真源 | 是否进 git |
|------|----------|------------|
| `~/.ky-x/` | 用户自己的运行数据 | **否** |
| 仓库内 `config.json`（若误生成） | 否 | **否**（见 `.gitignore`） |
