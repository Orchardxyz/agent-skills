# windows-fe-dev-setup

Bootstrap or repair a Windows frontend development environment with a reusable Agent Skill.

This skill is focused on Windows machines using PowerShell. It installs or repairs the common toolchain needed for frontend work, with extra attention to PATH and shell issues that often break otherwise-correct installs.

## What It Does

- Installs or repairs `nvm for Windows`
- Installs and activates `Node.js 24.16.0`
- Installs global npm tools:
  - `npm`
  - `pnpm`
  - `@anthropic-ai/claude-code`
- Installs `Git for Windows` if missing
- Repairs common user `PATH` entries
- Sets PowerShell execution policy to `RemoteSigned` for `CurrentUser` when needed
- Verifies `git`, `node`, `npm`, `npx`, `pnpm`, `claude`, and `code`

## Installation

Install this skill from the repo:

```bash
npx skills add https://github.com/Orchardxyz/agent-skills --skill windows-fe-dev-setup
```

Validate the local skill definition:

```bash
npx skills-ref validate ./skills/windows-fe-dev-setup
```

## When To Use

Use this skill when you need to:

- Set up a new Windows frontend development machine
- Repair a broken Windows Node.js / npm / pnpm environment
- Fix missing `git`, `node`, `npx`, or `code` commands caused by PATH issues
- Standardize a Windows frontend environment around `nvm` and Node.js 24 LTS

## Requirements

- Windows
- PowerShell
- Permission to install software
- Permission to edit user environment variables
- Network access for downloading installers and npm packages

## Included Script

Run the setup script from this skill directory:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\setup.ps1
```

The script currently installs or manages:

- `nvm for Windows` `1.2.2`
- `Node.js` `24.16.0`
- `Git for Windows` `2.52.0.windows.1`

## Notes

- The script is designed to be idempotent and prefers repair over reinstall.
- After PATH changes, a new PowerShell window may be required before all commands resolve normally.
- `npx` failures in PowerShell are often caused by execution policy rather than a missing installation.
- The script downloads installers and npm packages from the network and writes to user environment variables.
