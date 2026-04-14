#!/usr/bin/env python3
"""Search aitmpl.com component registry for skills matching a project's tech stack.

Fetches the full component catalog from aitmpl.com/components.json,
caches it locally for 24h, and filters by stack keywords.
Returns scored results as JSON to stdout.

Usage:
    python3 search_registries.py --stack "nextjs,prisma,tailwind" --types "skills,commands,agents,hooks"
"""

import argparse
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

CACHE_DIR = Path("/tmp/project-setup-cache")
CACHE_TTL = 86400  # 24 hours
COMPONENTS_URL = "https://www.aitmpl.com/components.json"


def fetch_components():
    """Fetch components.json with local file caching."""
    CACHE_DIR.mkdir(exist_ok=True)
    cache_file = CACHE_DIR / "components.json"

    if cache_file.exists():
        age = time.time() - cache_file.stat().st_mtime
        if age < CACHE_TTL:
            with open(cache_file) as f:
                return json.load(f)

    try:
        req = urllib.request.Request(
            COMPONENTS_URL,
            headers={"User-Agent": "project-setup-skill/1.0"},
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read())

        with open(cache_file, "w") as f:
            json.dump(data, f)

        return data
    except Exception as e:
        # If fetch fails but cache exists (even stale), use it
        if cache_file.exists():
            with open(cache_file) as f:
                return json.load(f)
        print(json.dumps({"error": str(e)}))
        sys.exit(1)


def score_component(component, stack_keywords):
    """Score a component's relevance to the detected stack.

    Higher score = more relevant. Matches in name and keywords
    are weighted higher than matches in description or content.
    """
    score = 0
    name = (component.get("name") or "").lower()
    desc = (component.get("description") or "").lower()
    keywords = [k.lower() for k in (component.get("keywords") or [])]
    content_preview = (component.get("content") or "")[:600].lower()

    for kw in stack_keywords:
        kw = kw.lower()
        if kw in name:
            score += 10
        if kw in keywords:
            score += 8
        if kw in desc:
            score += 5
        if kw in content_preview:
            score += 2

    return score


def search(stack_keywords, types, top_n=10):
    """Search the component catalog for matches against stack keywords."""
    data = fetch_components()
    results = {}

    type_keys = {
        "skills": "skills",
        "commands": "commands",
        "agents": "agents",
        "hooks": "hooks",
        "settings": "settings",
    }

    for type_name in types:
        key = type_keys.get(type_name)
        if not key or key not in data:
            continue

        components = data[key]
        if not isinstance(components, list):
            continue

        scored = []
        for comp in components:
            s = score_component(comp, stack_keywords)
            if s > 0:
                scored.append(
                    {
                        "name": comp.get("name", ""),
                        "description": (comp.get("description") or "")[:200],
                        "score": s,
                        "author": comp.get("author", ""),
                        "downloads": comp.get("downloads", 0),
                        "category": comp.get("category", ""),
                        "source": "aitmpl.com",
                    }
                )

        scored.sort(key=lambda x: (-x["score"], -(x.get("downloads") or 0)))
        results[type_name] = scored[:top_n]

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Search aitmpl.com for components matching a tech stack"
    )
    parser.add_argument(
        "--stack",
        required=True,
        help="Comma-separated stack keywords (e.g. 'nextjs,prisma,tailwind')",
    )
    parser.add_argument(
        "--types",
        default="skills,commands,agents,hooks",
        help="Comma-separated component types to search",
    )
    parser.add_argument(
        "--top", type=int, default=10, help="Max results per type (default: 10)"
    )
    parser.add_argument(
        "--clear-cache", action="store_true", help="Clear cached data before searching"
    )
    args = parser.parse_args()

    if args.clear_cache:
        cache_file = CACHE_DIR / "components.json"
        if cache_file.exists():
            cache_file.unlink()

    stack_keywords = [k.strip() for k in args.stack.split(",") if k.strip()]
    types = [t.strip() for t in args.types.split(",") if t.strip()]

    results = search(stack_keywords, types, args.top)
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
