# Contributing

Thanks for interest in **ky-skills** (Kiren Yi).

## Ground rules

- Keep the `ky-` prefix for all skills.
- Prefer small, reviewable PRs.
- Do not commit personal archives, tokens, or `config.json` with secrets.
- Document user-facing behavior in the skill’s `SKILL.md` and root `README.md`.
- **Multi-agent**: read [`AGENTS.md`](./AGENTS.md) and append to [`docs/PROGRESS.md`](./docs/PROGRESS.md) after meaningful work.
- **Source of truth**: edit `skills/` in this repo, not copies under `~/.claude/skills` etc.

## Local setup

```bash
git clone https://github.com/KirenYi/ky-skills.git
cd ky-skills
./scripts/install-links.sh
```

For `ky-x`:

```bash
export PYTHONPATH=$PWD/skills/ky-x/scripts
python3 -m xarchive init -c /tmp/ky-x-dev.json
python3 -m xarchive add <handle> -c /tmp/ky-x-dev.json
python3 -m xarchive sync --handle <handle> -c /tmp/ky-x-dev.json
```

## Adding a skill

1. Copy `templates/skill-skeleton` → `skills/ky-<name>`
2. Fill `SKILL.md` (triggers + step-by-step agent workflow)
3. Add scripts under `skills/ky-<name>/scripts/` if needed
4. Update root README skill table
5. Bump `VERSION` / skill `VERSION` and changelog when shipping

## Reporting issues

Please include:

- OS + Python version
- Command or Agent prompt used
- Full error output
- Whether network / Nitter instances are reachable
