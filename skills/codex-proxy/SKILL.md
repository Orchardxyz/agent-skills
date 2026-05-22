---
name: codex-proxy
description: Use when Codex CLI shows "Reconnecting" errors, websocket connection failures, or the user says Codex cannot connect. Also use when the user asks to configure a proxy for Codex. Detects Clash/闪狐云 proxy address automatically via system settings, or asks the user when detection fails.
---

# Codex Proxy

## Overview

Codex CLI needs proxy environment variables to route WebSocket and subprocess traffic. Without them, Codex shows "Reconnecting" and can't establish persistent connections. This skill detects the active proxy (Clash, 闪狐云, or manual) and writes the configuration to `~/.codex/.env`.

## When to Use

- Codex shows "Reconnecting" repeatedly
- Codex WebSocket connections fail
- User asks to configure proxy for Codex
- After switching proxy apps (Clash ↔ 闪狐云), Codex stops working

## Detection & Configuration

### Step 1: Check existing config

```bash
cat ~/.codex/.env 2>/dev/null
```

If it exists with valid proxy settings, test them:

```bash
curl -s -o /dev/null -w "%{http_code}" --connect-timeout 3 -x "$(grep ^HTTP_PROXY= ~/.codex/.env | cut -d= -f2)" https://api.openai.com
```

If this returns 200+, the proxy is working — no changes needed. If not, continue.

### Step 2: Detect proxy from system settings

Check all active network interfaces for system proxy configuration:

```bash
networksetup -listallnetworkservices | while read svc; do
  proxy=$(networksetup -getwebproxy "$svc" 2>/dev/null)
  enabled=$(echo "$proxy" | grep "^Enabled:" | awk '{print $2}')
  if [ "$enabled" = "Yes" ]; then
    server=$(echo "$proxy" | grep "^Server:" | awk '{print $2}')
    port=$(echo "$proxy" | grep "^Port:" | awk '{print $2}')
    if [ -n "$server" ] && [ -n "$port" ]; then
      echo "$server:$port"
      break
    fi
  fi
done
```

If a proxy is found, test it:

```bash
curl -s -o /dev/null -w "%{http_code}" --connect-timeout 3 -x http://<server>:<port> https://api.openai.com
```

### Step 3: Check common Clash ports

If system proxy is not set, probe Clash default ports:

```bash
for port in 7890 7891; do
  code=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 2 -x http://127.0.0.1:$port https://httpbin.org/ip 2>/dev/null)
  if [ "$code" = "200" ]; then
    echo "127.0.0.1:$port"
    break
  fi
done
```

### Step 4: Ask the user

If all detection fails, ask: "无法自动检测代理地址。请提供你的代理地址（格式：127.0.0.1:端口）。"

### Step 5: Write the config

Once the proxy address is confirmed, write `~/.codex/.env`:

```
HTTP_PROXY=http://<address>
HTTPS_PROXY=http://<address>
ALL_PROXY=http://<address>
http_proxy=http://<address>
https_proxy=http://<address>
all_proxy=http://<address>
NO_PROXY=localhost,127.0.0.1
no_proxy=localhost,127.0.0.1
```

Both upper and lowercase variants cover all subprocess conventions. `NO_PROXY` prevents local loopback from being proxied.

### Step 6: Verify

Restart Codex and confirm the "Reconnecting" message no longer appears.

## Common Pitfalls

- **.env not loaded**: Codex reads `~/.codex/.env` at startup. Restart Codex after changes.
- **Clash daemon persists after quit**: ClashX Pro's menu bar icon → right-click → Quit (Cmd+Q). Closing the window leaves the core running.
- **System proxy mismatch**: After switching proxy apps, system proxy may point to a dead port. Re-check with Step 2.
- **WebSocket needs proxy too**: `ALL_PROXY` is essential — some Codex connections use non-HTTP protocols.
