# Skill Comparison

A skill for systematically comparing multiple similar skills to help users choose the best option for their needs.

## Installation

```bash
npx skills add https://github.com/Orchardxyz/agent-skills --skill skill-comparison
```

## Purpose

When multiple skills exist for the same purpose, this skill helps users:
- Understand the differences between similar skills
- Evaluate trade-offs and strengths/weaknesses
- Make informed decisions based on their specific requirements
- Compare skills from various sources (URLs, local paths, repositories)

## Structure

```
skill-comparison/
├── SKILL.md                           # Main skill instructions
├── README.md                          # This file
├── scripts/
│   └── fetch_skill.py                 # Utility to fetch skills from URLs or local paths
└── references/
    └── COMPARISON_CRITERIA.md         # Detailed evaluation framework
```

## Usage

This skill is triggered when users want to compare or evaluate multiple skills. Example phrases:
- "Compare these two skills..."
- "Which skill should I use for X?"
- "What's the difference between skill A and skill B?"
- "Help me choose between these options..."

## Features

### Multi-Source Support
- **URLs**: Fetch skills from remote locations
- **Local paths**: Read skills from filesystem
- **Repositories**: Reference skills by name from known repos

### Comprehensive Analysis
Evaluates skills across multiple dimensions:
- Scope and purpose
- Complexity and learning curve
- Documentation quality
- Flexibility and adaptability
- Dependencies and requirements
- Maintenance status

### Structured Output
Provides clear, actionable comparisons:
- Quick comparison matrix
- Detailed analysis of each skill
- Context-aware recommendations
- Trade-off explanations

## Examples

### Comparing Two Local Skills

```bash
# User provides two skill paths
Skill A: ~/skills/git-helper/SKILL.md
Skill B: ~/skills/git-workflow/SKILL.md

# The skill will:
# 1. Read both SKILL.md files
# 2. Parse metadata and content
# 3. Analyze across comparison dimensions
# 4. Present structured comparison
# 5. Recommend based on user context
```

### Comparing Remote and Local Skills (safe pattern)

```bash
# User provides mixed sources
Skill A: https://github.com/user/repo/skills/data-viz/SKILL.md
Skill B: /Users/me/custom-skills/chart-maker/SKILL.md

# The skill will:
# 1. Use fetch_skill.py with explicit allowlist to retrieve remote skill
#    python scripts/fetch_skill.py --allow-remote --allow-hosts github.com,raw.githubusercontent.com https://github.com/user/repo/skills/data-viz/SKILL.md
# 2. Read local skill from filesystem
# 3. Perform comparison analysis
# 4. Provide recommendation
```

## Tools

### fetch_skill.py (safer defaults)

Utility script to retrieve skills from various sources. Remote fetching is **disabled by default**; enable it explicitly and scope allowed hosts.

**Usage:**
```bash
# Local file (default safe path)
python scripts/fetch_skill.py /path/to/local/skill/SKILL.md

# HTTPS remote (requires explicit consent and allowlist)
python scripts/fetch_skill.py --allow-remote --allow-hosts github.com,raw.githubusercontent.com https://raw.githubusercontent.com/user/repo/main/skills/data-viz/SKILL.md
```

**Examples:**
```bash
# Fetch from a trusted HTTPS URL (explicitly allowed)
python scripts/fetch_skill.py --allow-remote --allow-hosts example.com https://example.com/skill/SKILL.md

# Read from local path
python scripts/fetch_skill.py /path/to/skill/SKILL.md

# Read with tilde expansion
python scripts/fetch_skill.py ~/skills/my-skill/SKILL.md
```

## Comparison Framework

See `references/COMPARISON_CRITERIA.md` for the complete evaluation framework, including:
- Detailed assessment criteria
- Rating scales
- Decision frameworks
- Best practices
- Red flags to watch for

## Dependencies

- **Python 3.8+** (for fetch_skill.py script)
- **Internet access** (only when remote fetching is explicitly enabled)

No additional Python packages required - uses only standard library. Remote content is limited to HTTPS and capped at ~500 KB; prefer local/trusted sources.

## License

MIT (inherits from repository license)
