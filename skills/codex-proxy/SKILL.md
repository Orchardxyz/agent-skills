---
name: codex-proxy
description: Configure Codex to use the machine's proxy by detecting the active proxy on Windows or macOS, validating it, and writing the required variables to ~/.codex/.env. Use when Codex shows "Reconnecting", cannot connect, or the user asks to configure a proxy for Codex.
---

# Codex Proxy

Run `scripts/configure_proxy.py` first. It detects the active proxy from Windows or macOS system settings, falls back to common local proxy ports, validates the proxy, and writes `~/.codex/.env`.

## Workflow

1. Run `python scripts/configure_proxy.py`.
2. If auto-detection fails, ask the user for a proxy address in `host:port` form and rerun `python scripts/configure_proxy.py --proxy <host:port>`.
3. Restart Codex after the script writes `~/.codex/.env`.

## Notes

- Prefer the script over redoing proxy-detection logic in the prompt.
- The script accepts an explicit `--proxy` override and a `--dry-run` mode for verification.
- If the machine has a system proxy but Codex still reconnects, rewriting `~/.codex/.env` is usually enough.
