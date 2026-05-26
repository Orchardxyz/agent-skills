param(
    [string]$SettingsPath = (Join-Path $env:LOCALAPPDATA "Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"),
    [string]$FontFace = "MesloLGM Nerd Font Mono",
    [string]$ProfileName = "PowerShell 7",
    [string]$CommandLine = "pwsh.exe"
)

if (-not (Test-Path $SettingsPath)) {
    throw "Windows Terminal settings.json not found at $SettingsPath"
}

$settings = Get-Content $SettingsPath -Raw | ConvertFrom-Json -Depth 100

if (-not $settings.profiles) {
    $settings | Add-Member -MemberType NoteProperty -Name profiles -Value ([pscustomobject]@{ list = @() })
}

if (-not ($settings.profiles.PSObject.Properties.Name -contains "list")) {
    $settings.profiles | Add-Member -MemberType NoteProperty -Name list -Value @()
}

$profiles = @($settings.profiles.list)
$targetProfile = $profiles | Where-Object { $_.name -eq $ProfileName } | Select-Object -First 1

if (-not $targetProfile) {
    $targetProfile = [pscustomobject]@{
        guid = [guid]::NewGuid().ToString("B")
        name = $ProfileName
        commandline = $CommandLine
    }
    $profiles += $targetProfile
    $settings.profiles.list = $profiles
}

$targetProfile.commandline = $CommandLine
if (-not ($targetProfile.PSObject.Properties.Name -contains "font")) {
    $targetProfile | Add-Member -MemberType NoteProperty -Name font -Value ([pscustomobject]@{ face = $FontFace })
} else {
    $targetProfile.font = [pscustomobject]@{ face = $FontFace }
}

if (-not ($settings.PSObject.Properties.Name -contains "defaultProfile")) {
    $settings | Add-Member -MemberType NoteProperty -Name defaultProfile -Value $targetProfile.guid
} else {
    $settings.defaultProfile = $targetProfile.guid
}

if (-not $settings.profiles.defaults) {
    $settings.profiles | Add-Member -MemberType NoteProperty -Name defaults -Value ([pscustomobject]@{})
}

$settings.profiles.defaults | Add-Member -MemberType NoteProperty -Name font -Value ([pscustomobject]@{ face = $FontFace }) -Force

$json = $settings | ConvertTo-Json -Depth 100
Set-Content -Path $SettingsPath -Value $json
Write-Output $SettingsPath
