---
name: git-conventions
description: Use when asked for branch names, commit messages, or PR descriptions for code changes. Triggers on requests like "give me a branch name", "write a commit message", "draft a PR", or when the user describes a change and expects git metadata in return. Output is always in English.
---

# Git Conventions

## Safety Rule

**Never commit, push, or create a PR unless the user explicitly asks you to do that specific action.** Providing a branch name, commit message, or PR draft is not permission to execute it.

## Staging Check (required)

**Before producing any git metadata, check the staging area.** The types and scope must reflect what's actually staged, not what's in the working tree or on the branch.

1. Run `git diff --cached --stat` to see staged files. Also run `git diff --cached --name-only` for a clean file list.
2. **If nothing is staged:** stop and tell the user: "No changes are staged. Please stage the changes you want metadata for (e.g., `git add <files>`), then ask again." Do not produce output based on unstaged changes.
3. If there are staged changes, run `git diff --cached` to understand the nature of the changes. Use this to determine the correct type prefix and scope.
4. Also check `git log --oneline -10` to derive the branch name format the repo uses.

## Workflow

When asked for branch / commit / PR metadata:

1. **Check staging area first.** Follow the Staging Check steps above. Do not skip this.
2. Read `git log --oneline -10` to detect the repo's existing commit style (prefixes, capitalization, trailers). Adopt it. Also inspect merge commits to derive the branch name convention (e.g., `type/description` vs `type/scope-description`).
3. Check for `.github/PULL_REQUEST_TEMPLATE.md`. If present, match its sections exactly.
4. If the repo has no discernible conventions, use the defaults below.
5. All output in English.

## Type Prefix Table

| Prefix | When you... |
|--------|------------|
| `feat` | Add new behavior, capability, or feature |
| `fix` | Correct a bug, crash, or incorrect behavior |
| `style` | Change visuals only — CSS, layout, spacing, icons |
| `refactor` | Restructure code without changing external behavior |
| `perf` | Improve performance without changing behavior |
| `chore` | Update deps, config, build scripts — no product code |
| `docs` | Change documentation only |
| `test` | Add or fix tests only |

Edge cases: visual-only → `style`, not `feat` or `fix`. Logic fix + UI change → `fix`. Dead code removal → `chore`.

## Branch Name

Derive the branch name format from the repo's actual branch names in `git log --oneline` (look at merge commits like `Merge pull request #N from …`). Common patterns:

- `type/description` — two segments (e.g., `feat/i18n`, `refactor/monorepo`)
- `type/scope-description` — three segments (e.g., `fix/auth-token-expiry`)

Lowercase, kebab-case, 4-5 words max. Match the repo's convention; do not impose a format it doesn't use.

## Commit Message

```
type(scope): brief subject in sentence case

Body paragraph(s) explaining what and why. Hard-wrap at 72 chars.
```

Subject: ≤50 chars, stands alone in `git log --oneline`. Body: what and why, no filler. Match the repo's style if it uses a different format.

## PR Description

If the repo has a PR template, fill each section concisely. If not, provide a summary, motivation, and verification steps. For UI-facing changes that affect multiple states, include a test prompt the reviewer can paste and run. Never include `Co-Authored-By: Claude` or similar trailers unless explicitly asked.

## Anti-Patterns

| Don't | Do |
|-------|----|
| Produce metadata without checking staging area | Run `git diff --cached --stat` first; prompt user to stage if empty |
| Invent a style without checking `git log` | Read 10 commits, adopt the repo's conventions |
| Ignore the repo's PR template | Check `.github/PULL_REQUEST_TEMPLATE.md` |
| Output in Chinese | English for all git metadata |
| Commit / push / create PR without being asked | Only provide the text; let the user execute |
| Use `fix` for CSS-only changes | Use `style` |
| Use `feat` for visual polish | Use `style` |
