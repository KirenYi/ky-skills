# ky-x

将 X（Twitter）账号的公开帖子增量归档到本地。

- 调用名：`/ky-x`
- 作用：输入博主 handle → 本地 JSONL + Markdown
- 默认：无需 X API

安装与集合说明见仓库根目录 [README](../../README.md)。

## 命令行

```bash
export PYTHONPATH=/path/to/ky-skills/skills/ky-x/scripts
python3 -m xarchive init -c ~/.ky-x/config.json
python3 -m xarchive add naval -c ~/.ky-x/config.json
python3 -m xarchive sync --handle naval -c ~/.ky-x/config.json
```
