---
name: git-workflow-automator
description: This skill automates the complete git workflow for personal projects. Use this skill when the user has staged changes and wants to create a new branch, generate a conventional commit message, add a changeset, and open a pull request. This skill should be triggered when users say things like "commit these changes", "create a PR", "I want to commit and open a pull request", or indicate they have staged changes ready to commit. The skill also detects when the user is on a protected branch (main, master, admin) and prompts them to create a new feature branch.
---

# Git Workflow Automator

## Overview

Automate the complete git workflow for personal projects: analyze staged changes, determine the change type, create an appropriately-typed branch, generate a conventional commit message, create a changeset, and open a pull request with a generated summary.

## When to Use This Skill

Use this skill when:
- The user has staged changes (`git add` has been used) and wants to commit them
- The user wants to create a new branch and commit in one workflow
- The user wants to open a pull request for their changes
- The user mentions "commit", "PR", "branch" in the context of their staged changes

## Workflow

Follow this step-by-step workflow to automate the git process:

### Step 0: Check Current Branch (Protected Branch Detection)

Before proceeding, check if the user is on a protected branch:

```bash
git branch --show-current
```

Protected branches typically include: `main`, `master`, `admin`, `develop`, `production`, `staging`, or any branch the user indicates should not be committed to directly.

**If on a protected branch:**

Ask the user if they want to automatically create a new conventional branch and check it out. For example:

> "You're currently on the `main` branch. Direct commits to protected branches are not recommended. I can create a new feature branch based on your staged changes. Would you like me to automatically generate a branch name and check it out?"

If the user agrees:
1. Proceed to analyze the staged changes (Step 1)
2. Generate a conventional branch name (Step 3)
3. Create and checkout the new branch (Step 4)
4. Continue with the rest of the workflow

If the user declines, ask what they would like to do instead.

**If not on a protected branch:**

Continue with Step 1.

### Step 1: Analyze Staged Changes

First, examine what changes are staged:

```bash
git diff --cached
```

Analyze the diff to understand:
- What files were modified
- What functionality was added, changed, or removed
- The scope and impact of the changes

### Step 2: Determine Change Type

Based on the analysis, categorize the change using conventional commit types:

| Type | When to Use | Example Changes |
|------|-------------|-----------------|
| `feat` | New feature or functionality | Adding a new function, endpoint, component |
| `fix` | Bug fix | Fixing a bug, error handling, edge case |
| `chore` | Maintenance tasks | Updating dependencies, config changes |
| `docs` | Documentation only | README updates, comments, docstrings |
| `refactor` | Code refactoring | Restructuring without behavior change |
| `test` | Test changes | Adding or modifying tests |

If uncertain, default to `feat` for new functionality or `fix` for bug corrections.

### Step 3: Generate Branch Name

Create a branch name following the format:

```
<type>/<short-description>
```

Rules:
- Use lowercase for the type prefix
- Use kebab-case for the description
- Keep the description concise (3-5 words)
- Make it descriptive of the change

Examples:
- `feat/oauth2-login`
- `fix/user-api-null-pointer`
- `chore/update-dependencies`
- `docs/api-readme`
- `refactor/auth-service`

### Step 4: Create and Checkout New Branch

```bash
git checkout -b <branch-name>
```

### Step 5: Generate Conventional Commit Message

Create a conventional commit message following this format:

```
<type>(<scope>): <description>

[Optional body with more details]
```

Consult [references/commit_conventions.md](references/commit_conventions.md) for detailed formatting rules.

The commit message should:
- Use the type determined in Step 2
- Include a relevant scope (e.g., the module/component affected)
- Provide a clear, concise description in English
- Use imperative mood ("add" not "added" or "adds")
- Start with a capital letter
- Not end with a period

Examples:
- `feat(auth): add OAuth2 login support`
- `fix(api): resolve null pointer in user endpoint`
- `chore(deps): update React to v18`
- `docs(readme): add installation instructions`

### Step 6: Create Changeset

Since the project uses `@changesets/cli`, create a changeset for version management:

```bash
npx changeset add
```

When prompted:
- Select the appropriate semver type based on the change type:
  - `feat` → `minor`
  - `fix` → `patch`
  - `chore`/`docs`/`refactor` → `patch` (usually)
  - Breaking changes → `major`
- Provide a summary of the change for the changelog

### Step 7: Commit the Changes

Stage the changeset file and commit with the conventional commit message:

```bash
git add .
git commit -m "<commit-message>"
```

### Step 8: Push and Create Pull Request

Push the branch to the remote:

```bash
git push -u origin <branch-name>
```

Create a pull request using `gh pr create`:

```bash
gh pr create --title "<commit-message>" --body "<pr-body>"
```

The PR body should follow the format specified in [references/pr_format.md](references/pr_format.md).

## Example Complete Workflow

Given staged changes that add a new login feature:

```bash
# 1. Analyze changes
git diff --cached

# 2. Determine: feat (new feature)

# 3. Branch: feat/oauth-login

# 4. Create branch
git checkout -b feat/oauth-login

# 5. Commit: feat(auth): add OAuth login support

# 6. Create changeset
npx changeset add
# → Select minor, describe as "Add OAuth login support"

# 7. Commit
git add .
git commit -m "feat(auth): add OAuth login support"

# 8. Push and create PR
git push -u origin feat/oauth-login
gh pr create --title "feat(auth): add OAuth login support" --body "..."
```

## Resources

### references/commit_conventions.md

Detailed rules for conventional commit formatting. Reference this when generating commit messages to ensure consistency.

### references/pr_format.md

Pull request template and formatting guidelines. Use this to generate well-structured PR descriptions.
