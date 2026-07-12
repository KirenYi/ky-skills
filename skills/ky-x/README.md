# ky-x

**Kiren Yi（KY）** 个人技能集中的 **X 推文归档** skill。

- 调用名：`/ky-x`
- 作用：输入博主 handle → 本地 JSONL + Markdown
- 默认：无需 X API

安装与集合说明见仓库根目录 [README](../../README.md)。

## 命令行

```bash
export PYTHONPATH=/path/to/ky-skills/skills/ky-x/scripts
python3 -m xarchive init -c ~/.ky-x/config.json
python3 -m xarchive add dontbesilent -c ~/.ky-x/config.json
python3 -m xarchive sync --handle dontbesilent -c ~/.ky-x/config.json
```
