# Codex Proxy

Automatically detect and configure the proxy for Codex by reading system proxy settings on Windows or macOS and writing the required environment variables to `~/.codex/.env`.

## Installation

```bash
npx skills add https://github.com/Orchardxyz/agent-skills --skill codex-proxy
```

## Usage

```bash
python scripts/configure_proxy.py
```

If auto-detection fails, provide the proxy explicitly:

```bash
python scripts/configure_proxy.py --proxy 127.0.0.1:7897
```

Preview detection without writing files:

```bash
python scripts/configure_proxy.py --dry-run
```

After writing `~/.codex/.env`, restart Codex so the new environment variables are loaded.

## Requirements

- Python 3
- Standard library only; no extra packages are required

## Detection sources

- Windows user proxy in `HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings`
- Windows `netsh winhttp show proxy`
- macOS `networksetup`
- Common local proxy ports such as Clash-style localhost ports
