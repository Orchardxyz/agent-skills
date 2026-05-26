---
name: windows-fe-dev-setup
description: Set up or repair a Windows frontend development environment with NVM for Windows, Node.js 24 LTS, npm, pnpm, Claude Code, Git, VS Code CLI, PowerShell compatibility, and PATH fixes.
---

Use this skill when you need to bootstrap or repair a Windows frontend coding environment on a Windows machine.

This skill is designed to be idempotent:
- It checks existing tools before installing.
- It repairs PATH and PowerShell issues that commonly break `git`, `node`, `npx`, or `code`.
- It verifies the final environment after setup.

What this skill manages:
- `nvm for Windows`
- `Node.js 24 LTS` as the active default version
- Global npm tools:
  - `npm`
  - `pnpm`
  - `@anthropic-ai/claude-code`
- `Git for Windows`
- `VS Code` CLI path (`code`)
- PowerShell execution policy for Node shims like `npx`
- User PATH consistency

Expected environment:
- Windows
- PowerShell
- Permission to install software
- Permission to edit user environment variables

Workflow:
1. Check whether `nvm`, `node`, `npm`, `npx`, `pnpm`, `claude`, `git`, and `code` are available.
2. Install `nvm for Windows` if missing.
3. Install and activate Node.js 24 LTS with `nvm`.
4. Install or update global npm packages:
   - `npm`
   - `pnpm`
   - `@anthropic-ai/claude-code`
5. Install Git if missing.
6. Ensure the VS Code CLI path is present if VS Code is installed.
7. Set the PowerShell execution policy for `CurrentUser` to `RemoteSigned` if needed.
8. Repair the user PATH so the following locations are available when present:
   - `%LOCALAPPDATA%\Microsoft\WindowsApps`
   - `%LOCALAPPDATA%\nvm`
   - `C:\nvm4w\nodejs`
   - `C:\Program Files\Git\cmd`
   - `%LOCALAPPDATA%\Programs\Microsoft VS Code\bin`
9. Verify:
   - `git --version`
   - `node -v`
   - `npm -v`
   - `npx -v`
   - `pnpm -v`
   - `claude --version`
   - `code --version`

Run:
`powershell -ExecutionPolicy Bypass -File .\scripts\setup.ps1`

Notes:
- A newly opened PowerShell window may be required after PATH updates.
- `npx` failures in PowerShell are often caused by execution policy, not missing installation.
- Prefer repair over reinstall when tools are already present.
