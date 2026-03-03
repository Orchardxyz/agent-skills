---
name: git-conditional-identities
description: Use when Git needs to switch user.name and user.email automatically based on repository location (per-folder identities via includeIf gitdir).
---

# Git Conditional Identities

## Overview
Automatically switch Git `user.name` and `user.email` based on repo location using `includeIf.gitdir`. Keep a global default while assigning per-folder identities for workspaces, clients, or personal projects.

## When to Use
- Need different commit identities for specific folders (e.g., work vs personal) without manual `git config` changes
- Want to enforce a default global identity but override for certain directories
- Supporting multiple clients/organizations where repos live under known paths

## Quick Start
1) **Create a per-identity config file** (example for `~/work`):
   ```ini
   # ~/.gitconfig-work
   [user]
       name = Your Work Name
       email = your.work@example.com
   ```
2) **Reference it from the global config with includeIf**:
   ```ini
   # ~/.gitconfig
   [user]
       name = Your Default Name
       email = your.default@example.com

   [includeIf "gitdir:~/work/"]
       path = ~/.gitconfig-work
   ```
   Notes:
   - Trailing slash after the directory ensures subfolders match.
   - Order matters: global defaults are read first; include overrides when path matches.
3) **Test resolution**:
   ```bash
   git -C ~/work/some-repo config user.name
   git -C ~/work/some-repo config user.email
   git -C ~/personal/some-repo config user.name
   ```
   Expect work repos to show the override, others to show the global defaults.

## Multiple Directories
Add more blocks for other roots:
```ini
[includeIf "gitdir:~/clients/acme/"]
    path = ~/.gitconfig-acme

[includeIf "gitdir:~/oss/"]
    path = ~/.gitconfig-oss
```
Create matching files (`~/.gitconfig-acme`, etc.) with the identity for that folder.

## Tips & Gotchas
- Always include the trailing `/` in `gitdir:` when targeting a folder tree.
- Use absolute or `~` paths; avoid environment variables in `gitdir` patterns.
- The first matching include wins for settings defined there; unspecified keys fall back to global defaults.
- To see which file set a value: `git config --show-origin --get user.name`.
- For single-repo overrides, you can set local config inside that repo (`git config user.name ...`), but `includeIf` is better for folder-wide rules.

## Verification Checklist
- Global `user.name`/`user.email` still return defaults outside scoped folders.
- Inside each targeted folder, `git config user.*` reflects the intended identity.
- `git config --show-origin --get user.email` points to the expected include file when inside matched repos.
