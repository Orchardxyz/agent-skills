#!/usr/bin/env python3
from __future__ import annotations

"""
Fetch a skill from a URL or local path and output its content.

Security defaults:
- Remote fetching is disabled unless --allow-remote is explicitly set.
- Only HTTPS is allowed.
- Optional host allowlist via --allow-hosts (comma-separated).
- Content is capped to MAX_BYTES to avoid oversized payloads.

Usage:
    python fetch_skill.py <url_or_path>
    python fetch_skill.py --allow-remote --allow-hosts github.com,raw.githubusercontent.com https://github.com/user/repo/skills/data-viz/SKILL.md
    python fetch_skill.py /path/to/local/skill/SKILL.md
"""

import sys
import os
from pathlib import Path
from urllib.parse import urlparse
import urllib.request
import urllib.error
import argparse


MAX_BYTES = 512_000  # ~500 KB upper bound to reduce large payload risk


def is_url(source: str) -> bool:
    """Check if the source is a URL."""
    try:
        result = urlparse(source)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


def enforce_https_and_hosts(url: str, allowed_hosts: set[str] | None) -> None:
    parsed = urlparse(url)
    if parsed.scheme != "https":
        print("Error: Only HTTPS URLs are allowed.", file=sys.stderr)
        sys.exit(1)

    if allowed_hosts is not None and parsed.netloc not in allowed_hosts:
        print(
            "Error: Host not in allowlist. Use --allow-hosts to permit specific domains.",
            file=sys.stderr,
        )
        sys.exit(1)


def fetch_from_url(url: str, allowed_hosts: set[str] | None) -> str:
    """Fetch content from a URL with safety checks."""
    enforce_https_and_hosts(url, allowed_hosts)

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            # Guard against very large responses
            length_header = response.headers.get("Content-Length")
            if length_header:
                try:
                    if int(length_header) > MAX_BYTES:
                        print(
                            f"Error: Remote file too large (> {MAX_BYTES} bytes)",
                            file=sys.stderr,
                        )
                        sys.exit(1)
                except ValueError:
                    pass

            content_bytes = response.read(MAX_BYTES + 1)
            if len(content_bytes) > MAX_BYTES:
                print(
                    f"Error: Remote file exceeded {MAX_BYTES} byte limit.",
                    file=sys.stderr,
                )
                sys.exit(1)

            return content_bytes.decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error fetching URL: {e}", file=sys.stderr)
        sys.exit(1)


def fetch_from_path(path: str) -> str:
    """Fetch content from a local file path."""
    try:
        file_path = Path(path).expanduser().resolve()
        
        if not file_path.exists():
            print(f"Error: File not found: {file_path}", file=sys.stderr)
            sys.exit(1)
        
        if not file_path.is_file():
            print(f"Error: Path is not a file: {file_path}", file=sys.stderr)
            sys.exit(1)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except PermissionError:
        print(f"Error: Permission denied: {path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch a skill from URL or local path.")
    parser.add_argument("source", help="HTTPS URL or local file path to SKILL.md")
    parser.add_argument(
        "--allow-remote",
        action="store_true",
        help="Enable remote fetching. Without this, URL sources will be rejected.",
    )
    parser.add_argument(
        "--allow-hosts",
        help="Comma-separated allowlist of hostnames (e.g., github.com,raw.githubusercontent.com)",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    source = args.source

    allowed_hosts = None
    if args.allow_hosts:
        allowed_hosts = {host.strip() for host in args.allow_hosts.split(",") if host.strip()}

    if is_url(source):
        if not args.allow_remote:
            print(
                "Error: Remote fetching disabled. Pass --allow-remote and optionally --allow-hosts to proceed.",
                file=sys.stderr,
            )
            sys.exit(1)
        content = fetch_from_url(source, allowed_hosts)
    else:
        content = fetch_from_path(source)

    print(content)


if __name__ == "__main__":
    main()
