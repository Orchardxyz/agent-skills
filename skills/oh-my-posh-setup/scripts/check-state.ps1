param()

$commands = @("wt", "pwsh", "oh-my-posh", "winget")

$results = foreach ($name in $commands) {
    $command = Get-Command $name -ErrorAction SilentlyContinue
    [pscustomobject]@{
        Name = $name
        Available = [bool]$command
        CommandType = if ($command) { $command.CommandType } else { $null }
        Source = if ($command) { $command.Source } else { $null }
        Path = if ($command) { $command.Path } else { $null }
    }
}

$terminalSettingsPath = Join-Path $env:LOCALAPPDATA "Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"

[pscustomobject]@{
    Commands = $results
    PowerShellProfile = $PROFILE
    ProfileExists = Test-Path $PROFILE
    WindowsTerminalSettingsPath = $terminalSettingsPath
    WindowsTerminalSettingsExists = Test-Path $terminalSettingsPath
} | ConvertTo-Json -Depth 4
