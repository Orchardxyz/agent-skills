# Oh My Posh Setup

Set up and troubleshoot a polished Windows terminal stack based on `Windows Terminal`, `PowerShell 7`, and `oh-my-posh`, with guidance for common installation and configuration pitfalls.

## Installation

```bash
npx skills add https://github.com/Orchardxyz/agent-skills --skill oh-my-posh-setup
```

## Included Scripts

- `scripts/check-state.ps1`: Inspect whether `wt`, `pwsh`, `oh-my-posh`, and `winget` are available, and report profile/settings paths.
- `scripts/update-profile.ps1`: Create or update a managed `oh-my-posh` block in the current user's PowerShell profile.
- `scripts/update-windows-terminal.ps1`: Update Windows Terminal `settings.json` so `PowerShell 7` is the default profile and the configured font is applied.

## Notes

- These scripts are PowerShell-based and target Windows environments.
- `update-profile.ps1` writes to the current user's PowerShell profile.
- `update-windows-terminal.ps1` writes to Windows Terminal `settings.json`.
