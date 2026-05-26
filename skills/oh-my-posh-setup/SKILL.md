---
name: oh-my-posh-setup
description: Set up or troubleshoot a modern Windows terminal environment based on Windows Terminal, PowerShell 7, and oh-my-posh. Use when asked to install, configure, verify, or repair oh-my-posh on Windows, especially for users coming from zsh or oh-my-zsh who want a similar prompt experience.
---

# Oh My Posh Setup

Standardize the environment around `Windows Terminal + PowerShell 7 + oh-my-posh`. Keep the conversation focused on the user's target experience, then use the bundled scripts for deterministic checks and file edits.

## Target State

Aim for this result unless the user asks for a different setup:

- `Windows Terminal` is installed and usable.
- `PowerShell 7` is installed and available as `pwsh`.
- `oh-my-posh` is installed and callable.
- A Nerd Font such as `MesloLGM Nerd Font Mono` is installed.
- PowerShell profile initializes `oh-my-posh` safely.
- `Windows Terminal` defaults to `PowerShell 7` and uses the Nerd Font.

## Workflow

### 1. Inspect before changing anything

Run `scripts/check-state.ps1` first when you need a quick inventory of the current machine state.

Use it to confirm:

- whether `wt`, `pwsh`, `oh-my-posh`, and `winget` resolve
- where the PowerShell profile lives
- whether Windows Terminal settings are present

### 2. Install only what is missing

Prefer `winget` for core packages:

```powershell
winget install --id Microsoft.PowerShell -e --accept-package-agreements --accept-source-agreements
winget install --id Microsoft.WindowsTerminal -e --accept-package-agreements --accept-source-agreements
winget install --id JanDeDobbeleer.OhMyPosh -e --accept-package-agreements --accept-source-agreements
```

Install a Nerd Font with:

```powershell
oh-my-posh font install meslo --headless --plain
```

Install optional modules only when the user wants the enhanced experience:

```powershell
Set-PSRepository -Name PSGallery -InstallationPolicy Trusted
Install-Module PSReadLine -Scope CurrentUser -Force -AllowClobber
Install-Module Terminal-Icons -Scope CurrentUser -Force -AllowClobber
```

### 3. Use scripts for deterministic config edits

- Use `scripts/update-profile.ps1` to add or refresh a managed `oh-my-posh` block in the user's PowerShell profile without wiping unrelated customizations.
- Use `scripts/update-windows-terminal.ps1` to ensure a `PowerShell 7` profile exists, make it the default profile, and apply the desired font.

Read the script before changing behavior, then run it with explicit parameters when needed.

### 4. Verify from a fresh `pwsh` session

Check at least:

```powershell
pwsh -NoLogo -NoProfile -Command '$PSVersionTable.PSVersion.ToString()'
pwsh -NoLogo -Command 'Get-Command oh-my-posh'
```

If the user expects a terminal app to change automatically, explain that the shell (`pwsh`) and the terminal host (`Windows Terminal`, editor terminal, other embedded terminals) are separate layers.

## Troubleshooting

- If a command still cannot be found right after install, assume session `PATH` or app alias refresh is the first suspect.
- If `oh-my-posh font install` opens a UI or hangs, use `--headless --plain`.
- If `PSReadLine` prediction settings fail in non-interactive terminals, keep them wrapped in `try/catch`.
- If Windows Terminal JSON edits behave inconsistently, rerun under `pwsh` instead of Windows PowerShell 5.1.

## Communication Notes

- Explain terminal app vs shell clearly for users coming from `zsh` or `oh-my-zsh`.
- Recommend `PowerShell 7 + oh-my-posh` for native Windows workflows.
- Mention `WSL + zsh` only when the user wants Unix-first behavior.
- Be explicit about which changes affect the machine, the shell profile, or one specific terminal app.
