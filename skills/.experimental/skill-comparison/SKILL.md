---
name: skill-comparison
description: Compare multiple similar skills to help users choose the best one for their needs. Use when the user wants to evaluate, compare, or choose between different skills from URLs, local paths, or skill repositories. Triggers on phrases like "compare these skills", "which skill should I use", "evaluate skills", "difference between skills", or when multiple skill options exist for the same purpose.
compatibility: Requires internet access for fetching remote skills, Python 3.8+
metadata:
  version: "1.0"
---

# Skill Comparison

## Overview

This skill helps you systematically compare multiple skills that serve similar purposes, enabling informed decisions about which skill best fits specific requirements. It analyzes skills from various sources (URLs, local file paths, repositories) and presents a structured comparison.

## When to Use This Skill

- User mentions comparing skills, evaluating options, or choosing between alternatives
- Multiple skills exist for the same task and the user needs guidance
- User provides URLs or paths to different skill implementations
- User asks "which skill is better" or "what's the difference between X and Y"
- User wants to understand trade-offs between similar approaches

## Core Comparison Process

### 1. Gather Skills

Collect skills from the provided sources:

**Local paths:**
```bash
# Read skill from local directory
cat /path/to/skill/SKILL.md
```

**URLs:**
Use the fetch script to retrieve remote skills:
```bash
python scripts/fetch_skill.py <url>
```

**Skill repositories:**
If the user references a skill by name from a known repository, locate and read it.

### 2. Parse Skill Metadata

For each skill, extract:
- **Name** and **description** from frontmatter
- **Compatibility** requirements (dependencies, tools, environment)
- **License** information
- **Metadata** (author, version, etc.)
- **Structure** (scripts, references, assets)

### 3. Analyze Core Characteristics

Evaluate each skill across these dimensions:

**Scope & Purpose:**
- What specific problem does it solve?
- What are the stated use cases?
- How narrow or broad is the scope?

**Complexity:**
- How many steps/instructions?
- Does it require external dependencies?
- Are there bundled scripts or just instructions?

**Quality Indicators:**
- Clarity of instructions
- Presence of examples
- Error handling guidance
- Edge case coverage
- Documentation completeness

**Flexibility:**
- How configurable is it?
- Does it handle multiple scenarios?
- Can it be easily adapted?

**Maintenance:**
- Version information
- Author/source credibility
- Last update (if available)

### 4. Create Comparison Matrix

Present findings in a structured format:

```markdown
## Skill Comparison: [Purpose]

### Quick Summary
| Aspect | Skill A | Skill B | Skill C |
|--------|---------|---------|---------|
| Complexity | Low | Medium | High |
| Dependencies | None | Python 3.8+ | Node.js, Python |
| Scope | Narrow | Medium | Broad |
| Documentation | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |

### Detailed Analysis

#### Skill A: [name]
**Strengths:**
- [List key advantages]

**Weaknesses:**
- [List limitations]

**Best for:**
- [Specific use cases where this excels]

#### Skill B: [name]
...
```

### 5. Provide Recommendation

Based on the analysis, offer guidance:

**If there's a clear winner:**
```markdown
## Recommendation

For your use case ([describe user's context]), **Skill B** is the best choice because:
1. [Primary reason]
2. [Secondary reason]
3. [Additional reason]

However, consider Skill A if [alternative scenario].
```

**If it depends on context:**
```markdown
## Recommendation

The best choice depends on your specific needs:

- **Choose Skill A** if you need [specific requirement]
- **Choose Skill B** if you prioritize [different requirement]
- **Choose Skill C** if you have [particular constraint]
```

## Comparison Criteria Reference

See [references/COMPARISON_CRITERIA.md](references/COMPARISON_CRITERIA.md) for detailed evaluation framework.

## Examples

### Example 1: Comparing Git Skills

**User request:**
"Compare these two git skills: https://example.com/git-workflow.md and ~/skills/git-helper/SKILL.md"

**Process:**
1. Fetch remote skill using `scripts/fetch_skill.py`
2. Read local skill from filesystem
3. Parse both skills' frontmatter and content
4. Analyze across dimensions (scope, complexity, dependencies)
5. Create comparison matrix
6. Provide recommendation based on user's likely needs

**Output structure:**
- Side-by-side comparison table
- Detailed analysis of each skill
- Recommendation with reasoning

### Example 2: Evaluating Multiple Options

**User request:**
"I found three skills for data visualization. Which one should I use?"

**Process:**
1. Ask user for the three skill sources (URLs/paths)
2. Gather all three skills
3. Identify common purpose and differentiating factors
4. Evaluate quality, complexity, and feature coverage
5. Present findings with clear trade-offs
6. Recommend based on typical use cases or ask clarifying questions

## Handling Edge Cases

**Missing information:**
- If a skill lacks metadata, note this as a quality indicator
- Infer purpose from content if description is unclear
- Flag incomplete or poorly documented skills

**Incompatible formats:**
- If a source isn't a valid SKILL.md, attempt to extract useful information
- Note format issues in the comparison
- Suggest standardization if appropriate

**Too many skills:**
- If user provides >5 skills, suggest narrowing down first
- Offer to do initial filtering based on specific criteria
- Create tiered comparison (quick overview, then detailed for top candidates)

**Subjective preferences:**
- When trade-offs are balanced, ask user about priorities:
  - "Do you prefer simplicity or comprehensive features?"
  - "Are you comfortable with external dependencies?"
  - "Is active maintenance important to you?"

## Tips for Effective Comparison

1. **Stay objective** - Present facts, not opinions
2. **Highlight trade-offs** - Every choice has pros and cons
3. **Consider context** - User's skill level, environment, constraints
4. **Be specific** - Vague comparisons aren't helpful
5. **Show examples** - Demonstrate differences with concrete scenarios
6. **Update recommendations** - If user provides more context, refine advice

## Output Template

Always structure your comparison response like this:

```markdown
# Skill Comparison: [Purpose]

## Skills Being Compared
1. **[Skill A Name]** - [Source]
2. **[Skill B Name]** - [Source]
3. **[Skill C Name]** - [Source]

## Quick Comparison
[Comparison matrix table]

## Detailed Analysis
[Individual skill breakdowns]

## Key Differences
[Highlight the most important distinctions]

## Recommendation
[Context-aware guidance]

## Next Steps
[Actionable advice for the user]
```
