$ErrorActionPreference = 'Stop'

$NodeVersion = '24.16.0'
$NvmVersion = '1.2.2'
$GitVersion = '2.52.0.windows.1'

function Write-Info {
    param([string]$Message)
    Write-Host "[INFO] $Message" -ForegroundColor Cyan
}

function Write-Ok {
    param([string]$Message)
    Write-Host "[ OK ] $Message" -ForegroundColor Green
}

function Write-WarnMsg {
    param([string]$Message)
    Write-Host "[WARN] $Message" -ForegroundColor Yellow
}

function Test-CommandExists {
    param([string]$Name)
    return [bool](Get-Command $Name -ErrorAction SilentlyContinue)
}

function Refresh-SessionPath {
    $userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
    $machinePath = [Environment]::GetEnvironmentVariable('Path', 'Machine')
    $env:Path = "$userPath;$machinePath"
}

function Get-UserPathParts {
    $current = [Environment]::GetEnvironmentVariable('Path', 'User')
    if (-not $current) {
        return @()
    }

    return @(
        $current -split ';' |
        Where-Object { $_ -and $_.Trim() } |
        ForEach-Object { $_.Trim() }
    )
}

function Set-UserPathParts {
    param([string[]]$Parts)

    $clean = @(
        $Parts |
        Where-Object { $_ -and $_.Trim() } |
        Select-Object -Unique
    )

    [Environment]::SetEnvironmentVariable('Path', ($clean -join ';'), 'User')
}

function Add-UserPathEntry {
    param([string]$Entry)

    if (-not $Entry) {
        return
    }

    $parts = Get-UserPathParts
    if ($parts -notcontains $Entry) {
        $parts += $Entry
        Set-UserPathParts -Parts $parts
        Write-Info "Added PATH entry: $Entry"
    }
}

function Ensure-UserPath {
    $nvmHome = Join-Path $env:LOCALAPPDATA 'nvm'
    $nvmSymlink = 'C:\nvm4w\nodejs'
    $gitCmd = 'C:\Program Files\Git\cmd'
    $codeBin = Join-Path $env:LOCALAPPDATA 'Programs\Microsoft VS Code\bin'
    $windowsApps = Join-Path $env:LOCALAPPDATA 'Microsoft\WindowsApps'

    Add-UserPathEntry -Entry $windowsApps

    if (Test-Path $nvmHome) {
        Add-UserPathEntry -Entry $nvmHome
    }

    if (Test-Path $nvmSymlink) {
        Add-UserPathEntry -Entry $nvmSymlink
    }

    if (Test-Path $gitCmd) {
        Add-UserPathEntry -Entry $gitCmd
    }

    if (Test-Path $codeBin) {
        Add-UserPathEntry -Entry $codeBin
    }

    Refresh-SessionPath
}

function Ensure-ExecutionPolicy {
    $policy = Get-ExecutionPolicy -Scope CurrentUser
    if ($policy -ne 'RemoteSigned') {
        Write-Info 'Setting PowerShell execution policy for CurrentUser to RemoteSigned'
        Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
    } else {
        Write-Ok 'PowerShell execution policy already set to RemoteSigned'
    }
}

function Invoke-Download {
    param(
        [Parameter(Mandatory = $true)][string]$Url,
        [Parameter(Mandatory = $true)][string]$OutFile
    )

    Write-Info "Downloading: $Url"
    curl.exe -L $Url -o $OutFile
    if (-not (Test-Path $OutFile)) {
        throw "Download failed: $Url"
    }
}

function Ensure-NvmEnvironmentVariables {
    $nvmHome = Join-Path $env:LOCALAPPDATA 'nvm'
    $nvmSymlink = 'C:\nvm4w\nodejs'

    if ([Environment]::GetEnvironmentVariable('NVM_HOME', 'User') -ne $nvmHome) {
        [Environment]::SetEnvironmentVariable('NVM_HOME', $nvmHome, 'User')
        Write-Info "Set NVM_HOME to $nvmHome"
    }

    if ([Environment]::GetEnvironmentVariable('NVM_SYMLINK', 'User') -ne $nvmSymlink) {
        [Environment]::SetEnvironmentVariable('NVM_SYMLINK', $nvmSymlink, 'User')
        Write-Info "Set NVM_SYMLINK to $nvmSymlink"
    }

    $env:NVM_HOME = $nvmHome
    $env:NVM_SYMLINK = $nvmSymlink
}

function Get-NvmExePath {
    $candidates = @(
        (Join-Path $env:LOCALAPPDATA 'nvm\nvm.exe'),
        'C:\Program Files\nvm\nvm.exe',
        'C:\nvm\nvm.exe'
    )

    foreach ($candidate in $candidates) {
        if (Test-Path $candidate) {
            return $candidate
        }
    }

    return $null
}

function Ensure-NvmInstalled {
    $nvmExe = Get-NvmExePath
    if ($nvmExe) {
        Write-Ok "nvm already installed: $nvmExe"
        return $nvmExe
    }

    Write-Info "Installing nvm for Windows $NvmVersion"
    $installer = Join-Path $env:TEMP 'nvm-setup.exe'
    $url = "https://github.com/coreybutler/nvm-windows/releases/download/$NvmVersion/nvm-setup.exe"

    Invoke-Download -Url $url -OutFile $installer
    Start-Process -FilePath $installer -ArgumentList '/VERYSILENT', '/SUPPRESSMSGBOXES', '/NORESTART', '/SP-' -Wait

    Ensure-NvmEnvironmentVariables
    Ensure-UserPath

    $nvmExe = Get-NvmExePath
    if (-not $nvmExe) {
        throw 'nvm installation completed but nvm.exe was not found.'
    }

    Write-Ok "nvm installed: $nvmExe"
    return $nvmExe
}

function Invoke-Nvm {
    param(
        [Parameter(Mandatory = $true)][string[]]$Arguments
    )

    $nvmExe = Get-NvmExePath
    if (-not $nvmExe) {
        throw 'nvm.exe not found.'
    }

    Ensure-NvmEnvironmentVariables
    Refresh-SessionPath

    & $nvmExe @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "nvm command failed: $($Arguments -join ' ')"
    }
}

function Ensure-NodeInstalled {
    Write-Info "Ensuring Node.js $NodeVersion is installed via nvm"
    Invoke-Nvm -Arguments @('install', $NodeVersion, '64')
    Invoke-Nvm -Arguments @('use', $NodeVersion)
    Write-Ok "Node.js $NodeVersion is active"
}

function Ensure-GlobalNpmPackages {
    Refresh-SessionPath

    if (-not (Test-CommandExists 'npm.cmd')) {
        throw 'npm.cmd not found after Node setup.'
    }

    Write-Info 'Installing/updating global npm packages'
    & npm.cmd install -g npm pnpm @anthropic-ai/claude-code
    if ($LASTEXITCODE -ne 0) {
        throw 'Global npm package installation failed.'
    }

    Write-Ok 'Global npm packages are installed'
}

function Ensure-GitInstalled {
    if (Test-Path 'C:\Program Files\Git\cmd\git.exe') {
        Write-Ok 'Git already installed'
        return
    }

    Write-Info "Installing Git for Windows $GitVersion"
    $installer = Join-Path $env:TEMP 'git-installer.exe'
    $url = "https://github.com/git-for-windows/git/releases/download/v$GitVersion/Git-$GitVersion-64-bit.exe"

    Invoke-Download -Url $url -OutFile $installer
    Start-Process -FilePath $installer -ArgumentList '/VERYSILENT', '/NORESTART', '/NOCANCEL', '/SP-' -Wait

    if (-not (Test-Path 'C:\Program Files\Git\cmd\git.exe')) {
        throw 'Git installation completed but git.exe was not found.'
    }

    Write-Ok 'Git installed'
}

function Verify-Setup {
    Refresh-SessionPath

    Write-Host ''
    Write-Info 'Verification'

    & git --version
    & node -v
    & npm.cmd -v
    & npx.cmd -v
    & pnpm.cmd -v
    & claude.cmd --version

    if (Test-CommandExists 'code') {
        & code --version
    } else {
        Write-WarnMsg 'VS Code CLI (code) not found in PATH. If VS Code is installed, reopen PowerShell or repair PATH.'
    }

    Write-Host ''
    Write-Ok 'Windows frontend coding setup is complete'
}

Write-Info 'Starting Windows frontend coding setup'

Ensure-NvmEnvironmentVariables
Ensure-ExecutionPolicy
Ensure-NvmInstalled | Out-Null
Ensure-UserPath
Refresh-SessionPath
Ensure-NodeInstalled
Ensure-UserPath
Refresh-SessionPath
Ensure-GlobalNpmPackages
Ensure-GitInstalled
Ensure-UserPath
Refresh-SessionPath
Verify-Setup
