# AGENTS.md — Guidance for AI Agents

This file provides instructions for AI agents (Claude, Windsurf, Cursor, etc.) working inside this repository. Read this file before making any changes.

## Repository Purpose

This repository stores reusable [Agent Skills](https://agentskills.io/) — structured instruction sets that extend AI agent capabilities. Skills are consumed by agent products that support the Agent Skills specification.

## Repository Structure

```
agent-skills/
├── skills/
│   ├── git-conditional-identities/
│   └── skill-comparison/
├── AGENTS.md            # This file
├── README.md
├── LICENSE
└── .gitignore
```

Each individual skill lives in its own subdirectory under `skills/`:

```
skills/
└── my-skill/
    ├── SKILL.md          # Required
    ├── scripts/          # Optional: executable scripts
    ├── references/       # Optional: reference docs
    └── assets/           # Optional: templates, data files
```

## Rules for Creating New Skills

### 1. Directory and Naming

- Place new skills in `skills/` unless explicitly told otherwise
- The skill directory name **must** match the `name` field in `SKILL.md` exactly
- Use **kebab-case** only: lowercase letters `a-z` and hyphens `-`
- No uppercase, no underscores, no spaces, no consecutive hyphens (`--`)
- Must not start or end with a hyphen
- Length: 1–64 characters

Valid examples: `pdf-processing`, `code-review`, `data-analysis`  
Invalid examples: `PDF-Processing`, `code_review`, `-data-analysis`, `data--analysis`

### 2. Required SKILL.md Frontmatter

Every `SKILL.md` must begin with YAML frontmatter containing at minimum:

```yaml
---
name: skill-name
description: A clear description of what this skill does and when to use it.
---
```

**`name` field rules:**
- Must exactly match the parent directory name
- 1–64 characters, lowercase alphanumeric and hyphens only

**`description` field rules:**
- 1–1,024 characters
- Must describe **both** what the skill does **and** when to use it
- Include specific keywords that help agents identify relevant tasks
- Avoid vague descriptions like "Helps with PDFs" — be specific

### 3. Optional Frontmatter Fields

```yaml
---
name: skill-name
description: What this skill does and when to use it.
license: MIT
compatibility: Requires Python 3.10+, internet access
metadata:
  author: your-github-username
  version: "1.0"
allowed-tools: Bash(git:*) Read Write
---
```

- **`license`**: Specify the license for this skill (e.g., `MIT`, `Apache-2.0`). Defaults to the repo's MIT license if omitted.
- **`compatibility`**: Only include if the skill has specific environment requirements (1–500 characters).
- **`metadata`**: A map of string key-value pairs for additional properties. Use reasonably unique key names.
- **`allowed-tools`**: Space-delimited list of pre-approved tools. Experimental — support varies by agent.

### 4. SKILL.md Body Content

Keep the body **under 5,000 tokens** (recommended). Structure it clearly:

```markdown
# Skill Name

## When to use this skill
Describe the exact scenarios that should trigger this skill.

## How to [main task]
Step-by-step instructions...

## Examples
Concrete input/output examples...

## Edge cases
Known limitations and how to handle them...
```

Use **progressive disclosure**: put the most important instructions first. Reference external files for details:

```markdown
See [the reference guide](references/REFERENCE.md) for full API details.
Run the extraction script: `scripts/extract.py`
```

### 5. Optional Directories

- **`scripts/`** — Executable code. Scripts must be self-contained or clearly document their dependencies. Include helpful error messages and handle edge cases gracefully.
- **`references/`** — Detailed documentation (e.g., `REFERENCE.md`, `FORMS.md`, domain-specific files). Loaded only when referenced.
- **`assets/`** — Templates, images, data files, schemas. Loaded only when referenced.

### 6. Required README

Every skill directory must include a `README.md` that, at minimum, contains an **Installation** section explaining how to set up or install any needed dependencies.

## Code Quality Guidelines

- Write instructions that are **unambiguous** — an agent should be able to follow them without guessing
- Prefer **numbered steps** over prose for procedural instructions
- Include **concrete examples** with realistic inputs and outputs
- Test your skill by mentally simulating an agent following the instructions
- Keep `SKILL.md` focused — one skill, one responsibility
- If a skill grows too large, consider splitting it

## Validation

Validate a skill before committing:

```bash
npx skills-ref validate ./skills/my-skill
```

This checks that:
- `name` matches the directory name
- `description` is present and within length limits
- Frontmatter YAML is valid
- No required fields are missing

## Git Workflow Best Practices

- Create a new branch for each new skill: `git checkout -b add/skill-name`
- Commit message format: `feat(skills): add skill-name skill`
- One skill per pull request (keeps reviews focused)
- Update `README.md` skills table when adding a curated skill
- Do not commit directly to `main`

## Safety Considerations

- **Never hardcode secrets**, API keys, tokens, or passwords in any file
- **Never hardcode personal information** (emails, usernames, account IDs)
- Scripts in `scripts/` should not make network requests without documenting this in `compatibility`
- If a skill requires credentials, instruct the agent to read them from environment variables
- Prefer read-only operations; document any write/delete operations explicitly

## Skill Discovery Mechanism

Agent products that support the Agent Skills spec discover skills by:

1. Scanning configured skill directories for subdirectories containing `SKILL.md`
2. Parsing the `name` and `description` frontmatter fields (~100 tokens per skill)
3. Injecting metadata into the agent's context as structured XML
4. Loading the full `SKILL.md` body only when a task matches the skill's description

This means:
- The `description` field is **critical** — it is the primary signal agents use to decide whether to activate a skill
- Skills with vague descriptions will be overlooked
- Skills with overly broad descriptions will be activated unnecessarily
