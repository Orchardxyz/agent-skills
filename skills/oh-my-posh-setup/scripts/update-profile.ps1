param(
    [string]$ProfilePath = $PROFILE,
    [switch]$IncludePSReadLine,
    [switch]$IncludeTerminalIcons
)

$importPsReadLine = if ($IncludePSReadLine) {
@"
    try {
        Import-Module PSReadLine -ErrorAction SilentlyContinue
        Set-PSReadLineOption -PredictionSource History -ErrorAction Stop
        Set-PSReadLineOption -PredictionViewStyle ListView -ErrorAction Stop
    } catch {}
"@
} else {
    ""
}

$importTerminalIcons = if ($IncludeTerminalIcons) {
    "    Import-Module Terminal-Icons -ErrorAction SilentlyContinue"
} else {
    ""
}

$managedBlock = @"
# >>> oh-my-posh-setup >>>
if (`$PSVersionTable.PSVersion.Major -ge 7) {
$importPsReadLine
$importTerminalIcons
    if (Get-Command oh-my-posh -ErrorAction SilentlyContinue) {
        oh-my-posh init pwsh | Invoke-Expression
    }
}
# <<< oh-my-posh-setup <<<
"@.Trim()

$parent = Split-Path -Parent $ProfilePath
if ($parent -and -not (Test-Path $parent)) {
    New-Item -ItemType Directory -Path $parent -Force | Out-Null
}

if (-not (Test-Path $ProfilePath)) {
    New-Item -ItemType File -Path $ProfilePath -Force | Out-Null
}

$existing = Get-Content $ProfilePath -Raw
$pattern = '(?s)# >>> oh-my-posh-setup >>>.*?# <<< oh-my-posh-setup <<<'

if ($existing -match $pattern) {
    $updated = [regex]::Replace($existing, $pattern, [System.Text.RegularExpressions.MatchEvaluator]{ param($m) $managedBlock }, 1)
} elseif ([string]::IsNullOrWhiteSpace($existing)) {
    $updated = $managedBlock + [Environment]::NewLine
} else {
    $updated = $existing.TrimEnd() + [Environment]::NewLine + [Environment]::NewLine + $managedBlock + [Environment]::NewLine
}

Set-Content -Path $ProfilePath -Value $updated
Write-Output $ProfilePath
