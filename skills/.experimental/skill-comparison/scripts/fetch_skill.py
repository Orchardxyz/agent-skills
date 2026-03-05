#!/usr/bin/env python3
"""
Fetch a skill from a URL or local path and output its content.

Usage:
    python fetch_skill.py <url_or_path>
    python fetch_skill.py https://example.com/skill/SKILL.md
    python fetch_skill.py /path/to/local/skill/SKILL.md
"""

import sys
import os
from pathlib import Path
from urllib.parse import urlparse
import urllib.request
import urllib.error


def is_url(source: str) -> bool:
    """Check if the source is a URL."""
    try:
        result = urlparse(source)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


def fetch_from_url(url: str) -> str:
    """Fetch content from a URL."""
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            content = response.read().decode('utf-8')
            return content
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


def main():
    if len(sys.argv) != 2:
        print("Usage: python fetch_skill.py <url_or_path>", file=sys.stderr)
        print("\nExamples:", file=sys.stderr)
        print("  python fetch_skill.py https://example.com/skill/SKILL.md", file=sys.stderr)
        print("  python fetch_skill.py /path/to/skill/SKILL.md", file=sys.stderr)
        print("  python fetch_skill.py ~/skills/my-skill/SKILL.md", file=sys.stderr)
        sys.exit(1)
    
    source = sys.argv[1]
    
    if is_url(source):
        content = fetch_from_url(source)
    else:
        content = fetch_from_path(source)
    
    print(content)


if __name__ == "__main__":
    main()
