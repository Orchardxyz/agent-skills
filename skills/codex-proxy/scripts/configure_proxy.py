#!/usr/bin/env python3
"""Detect and write Codex proxy settings for Windows and macOS."""

from __future__ import annotations

import argparse
import os
import platform
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

try:
    import winreg  # type: ignore
except ImportError:  # pragma: no cover - only missing off Windows
    winreg = None


COMMON_PORTS = (7890, 7891, 7897)
DEFAULT_TEST_URL = "https://httpbin.org/ip"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Detect the active machine proxy and write ~/.codex/.env."
    )
    parser.add_argument(
        "--proxy",
        help="Explicit proxy address such as 127.0.0.1:7897 or http://127.0.0.1:7897.",
    )
    parser.add_argument(
        "--codex-home",
        default=os.environ.get("CODEX_HOME", str(Path.home() / ".codex")),
        help="Codex home directory. Defaults to CODEX_HOME or ~/.codex.",
    )
    parser.add_argument(
        "--test-url",
        default=DEFAULT_TEST_URL,
        help=f"Connectivity test URL. Defaults to {DEFAULT_TEST_URL}.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=5.0,
        help="Network timeout in seconds for proxy validation.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Detect and validate the proxy without writing ~/.codex/.env.",
    )
    return parser.parse_args()


def normalize_proxy(value: str) -> str | None:
    text = value.strip()
    if not text:
        return None

    if "://" in text:
        scheme, rest = text.split("://", 1)
        if scheme.lower() not in {"http", "https"}:
            return None
        candidate = rest.strip().rstrip("/")
    else:
        candidate = text.rstrip("/")

    if not candidate:
        return None

    if ";" in candidate and "=" in candidate:
        mapping = parse_proxy_mapping(candidate)
        return mapping

    return candidate


def parse_proxy_mapping(text: str) -> str | None:
    for item in text.split(";"):
        if "=" not in item:
            continue
        key, value = item.split("=", 1)
        if key.strip().lower() in {"http", "https", "socks"}:
            normalized = normalize_proxy(value)
            if normalized:
                return normalized
    return None


def test_proxy(address: str, url: str, timeout: float) -> tuple[bool, str]:
    proxy_url = f"http://{address}"
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler(
            {
                "http": proxy_url,
                "https": proxy_url,
            }
        )
    )
    request = urllib.request.Request(url, headers={"User-Agent": "codex-proxy-skill/1.0"})

    try:
        with opener.open(request, timeout=timeout) as response:
            code = getattr(response, "status", None) or response.getcode()
            return True, str(code)
    except urllib.error.HTTPError as exc:
        return True, str(exc.code)
    except Exception as exc:  # pragma: no cover - network/env specific
        return False, str(exc)


def detect_windows_proxy() -> list[str]:
    found: list[str] = []

    if winreg is not None:
        try:
            with winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",
            ) as key:
                proxy_enabled = int(winreg.QueryValueEx(key, "ProxyEnable")[0])
                proxy_server = str(winreg.QueryValueEx(key, "ProxyServer")[0])
                if proxy_enabled and proxy_server:
                    normalized = normalize_proxy(proxy_server)
                    if normalized:
                        found.append(normalized)
        except OSError:
            pass

    try:
        result = subprocess.run(
            ["netsh", "winhttp", "show", "proxy"],
            capture_output=True,
            text=True,
            check=False,
        )
        text = result.stdout
        match = re.search(r"Proxy Server\(s\)\s*:\s*(.+)", text)
        if match:
            normalized = normalize_proxy(match.group(1))
            if normalized and normalized not in found:
                found.append(normalized)
    except OSError:
        pass

    return found


def detect_macos_proxy() -> list[str]:
    found: list[str] = []
    try:
        services = subprocess.run(
            ["networksetup", "-listallnetworkservices"],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return found

    for raw_service in services.stdout.splitlines():
        service = raw_service.strip()
        if not service or service.startswith("*"):
            continue

        try:
            proxy = subprocess.run(
                ["networksetup", "-getwebproxy", service],
                capture_output=True,
                text=True,
                check=False,
            )
        except OSError:
            continue

        enabled = None
        server = None
        port = None
        for line in proxy.stdout.splitlines():
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            key = key.strip().lower()
            value = value.strip()
            if key == "enabled":
                enabled = value.lower() == "yes"
            elif key == "server":
                server = value
            elif key == "port":
                port = value

        if enabled and server and port:
            candidate = normalize_proxy(f"{server}:{port}")
            if candidate and candidate not in found:
                found.append(candidate)

    return found


def detect_common_local_proxies() -> list[str]:
    return [f"127.0.0.1:{port}" for port in COMMON_PORTS]


def candidate_proxies(explicit: str | None) -> list[str]:
    candidates: list[str] = []

    def add(value: str | None) -> None:
        normalized = normalize_proxy(value or "")
        if normalized and normalized not in candidates:
            candidates.append(normalized)

    add(explicit)

    system = platform.system().lower()
    if system == "windows":
        for item in detect_windows_proxy():
            add(item)
    elif system == "darwin":
        for item in detect_macos_proxy():
            add(item)

    for item in detect_common_local_proxies():
        add(item)

    return candidates


def build_env(proxy: str) -> str:
    proxy_url = f"http://{proxy}"
    return "\n".join(
        [
            f"HTTP_PROXY={proxy_url}",
            f"HTTPS_PROXY={proxy_url}",
            f"ALL_PROXY={proxy_url}",
            f"http_proxy={proxy_url}",
            f"https_proxy={proxy_url}",
            f"all_proxy={proxy_url}",
            "NO_PROXY=localhost,127.0.0.1",
            "no_proxy=localhost,127.0.0.1",
            "",
        ]
    )


def write_env(codex_home: Path, proxy: str) -> Path:
    codex_home.mkdir(parents=True, exist_ok=True)
    env_path = codex_home / ".env"
    env_path.write_text(build_env(proxy), encoding="utf-8")
    return env_path


def main() -> int:
    args = parse_args()
    candidates = candidate_proxies(args.proxy)

    for candidate in candidates:
        ok, detail = test_proxy(candidate, args.test_url, args.timeout)
        if not ok:
            print(f"skip {candidate}: {detail}", file=sys.stderr)
            continue

        print(f"proxy ok: {candidate} (status {detail})")
        if args.dry_run:
            return 0

        env_path = write_env(Path(args.codex_home), candidate)
        print(f"wrote {env_path}")
        print("restart Codex to reload ~/.codex/.env")
        return 0

    print(
        "failed to detect a working proxy automatically; rerun with --proxy 127.0.0.1:PORT",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
