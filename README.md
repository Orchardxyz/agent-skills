# My Agent Skills

My personal collection of reusable [Agent Skills](https://agentskills.io/) for AI coding assistants (Claude Code, Windsurf, Cursor, etc.). Open source — feel free to use them in your own projects.

## Skills

| Skill | Description | Status |
|-------|-------------|--------|
| *(more coming soon)* | | |

## Usage

### Install a specific skill

```bash
npx skills add https://github.com/Orchardxyz/agent-skills --skill [skill-name]
```

Example for `skill-comparison`:

```bash
npx skills add https://github.com/Orchardxyz/agent-skills --skill skill-comparison
```

### Install all curated skills

```bash
npx skills add https://github.com/Orchardxyz/agent-skills --skill '*'
```

Skills are installed into `.windsurf/skills/` or `.claude/skills/` (depending on your agent) and are automatically discovered at startup.

## Repository Structure

```
skills/
├── git-conditional-identities/
├── git-workflow-automator/
├── one-page-visual/
├── project-to-ci-template/
└── skill-comparison/
```

Each skill is a self-contained directory:

```
skill-name/
├── SKILL.md       # Instructions + metadata (required)
├── scripts/       # Executable code (optional)
├── references/    # Reference docs (optional)
└── assets/        # Templates, data files (optional)
```

## Contributing

Issues and PRs are welcome. See [AGENTS.md](AGENTS.md) for the conventions used in this repo.

## License

[MIT](LICENSE)
