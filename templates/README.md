# 如何新增一个 `ky-*` skill（Kiren Yi 技能集）

1. 复制骨架：

```bash
cp -R templates/skill-skeleton skills/ky-<短名>
```

2. 改 `skills/ky-<短名>/SKILL.md`：
   - frontmatter `name: ky-<短名>`
   - `description` 里写清触发词：`/ky-<短名>`、中文说法
   - 正文写 Agent 分步动作（能直接执行）

3. 如需脚本，放进 `skills/ky-<短名>/scripts/`

4. 更新根 `README.md` 的 skill 表格

5.  bump 根 `VERSION` 或该 skill 自己的 `VERSION`，写 changelog

## 命名规则

- 必须 `ky-` 前缀
- 短名：小写字母、数字、连字符，尽量 1～2 个词
- 示例：`ky-x`、`ky-note`、`ky-clip`
