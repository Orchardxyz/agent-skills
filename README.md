# My Agent Skills

A small public collection of [Agent Skills](https://agentskills.io/) for AI coding assistants.

Most skills in this repo come from my personal workflow, habits, and tooling preferences, so they may feel opinionated. They are still open for reuse, and `skill-comparison` in particular is designed to be broadly useful beyond my own setup.

## Skills

| Skill | Notes |
|-------|-------|
| `skill-comparison` | General-purpose skill for comparing similar skills and choosing the best fit. |
| `git-conventions` | Opinionated git naming and PR-writing helper based on my preferred workflow. |
| `git-conditional-identities` | Personal productivity helper for per-folder Git identities. |
| `codex-proxy` | Environment-specific helper for fixing Codex proxy connectivity issues. |

## Install

Install one skill:

```bash
npx skills add https://github.com/Orchardxyz/agent-skills --skill skill-comparison
```

Install all skills:

```bash
npx skills add https://github.com/Orchardxyz/agent-skills --skill '*'
```

## Format

Each skill lives under `skills/<skill-name>/` and should at least contain:

```text
SKILL.md
README.md
```

Validate a skill with:

```bash
npx skills-ref validate ./skills/<skill-name>
```

See [AGENTS.md](AGENTS.md) for the repo conventions.

## License

[MIT](LICENSE)
