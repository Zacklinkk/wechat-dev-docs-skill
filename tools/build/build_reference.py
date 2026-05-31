#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["httpx>=0.27", "beautifulsoup4>=4.12", "markdownify>=0.13"]
# ///
"""Maintainer tool: build compact STRUCTURED REFERENCE (facts only) for mini-program
component / API pages — title, one-line brief, attribute/param tables (with their section
heading), and the official deep link. Long prose and example code are intentionally dropped.

NOT shipped to ~/.claude/skills. Reads the Phase-1 map to learn which pages to fetch.

Usage:
    uv run build_reference.py components > skill/wechat-dev-docs/reference/miniprogram/components.md
    uv run build_reference.py api-groups            # prints the discovered API namespaces
    uv run build_reference.py api <group>           # e.g. network  -> reference/miniprogram/api/network.md
"""
from __future__ import annotations

import pathlib
import re
import sys
from concurrent.futures import ThreadPoolExecutor

import httpx
from bs4 import BeautifulSoup
from markdownify import markdownify as md

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) wechat-dev-docs-skill-build/1.0"
MAP_DIR = pathlib.Path(__file__).resolve().parents[2] / "skill" / "wechat-dev-docs" / "maps"
MAP_FILE = MAP_DIR / "miniprogram.md"  # default; kept for back-compat
DROP_SELECTORS = ["script", "style", "nav", "header", "footer", "aside", ".sidebar", ".navbar"]


def clean_heading(text: str) -> str:
    """Strip the VuePress anchor '#' prefix and surrounding whitespace."""
    return text.strip().lstrip("#").strip()


def table_to_markdown(table) -> str:
    return md(str(table), heading_style="ATX").strip()


def extract_reference(html: str, url: str) -> str:
    """Return a compact fact-only markdown block for one doc page."""
    soup = BeautifulSoup(html, "html.parser")
    node = soup.select_one("main.page") or soup.select_one("main") or soup.body or soup
    for sel in DROP_SELECTORS:
        for el in node.select(sel):
            el.decompose()
    h1 = node.find("h1")
    title = clean_heading(h1.get_text()) if h1 else url
    first_p = next(
        (p for p in node.find_all("p") if p.find_parent("table") is None),
        None,
    )
    brief = " ".join(first_p.get_text(strip=True).split()) if first_p else ""

    lines = [f"### {title}", ""]
    if brief:
        lines += [brief, ""]
    lines += [f"官方 / Source: {url}", ""]
    for table in node.find_all("table"):
        prev = table.find_previous(["h2", "h3"])
        if prev is not None and not any(parent is node for parent in prev.parents):
            prev = None  # heading escaped the content node; ignore
        label = clean_heading(prev.get_text()) if prev else ""
        if label:
            lines += [f"**{label}**", ""]
        lines += [table_to_markdown(table), ""]
    return "\n".join(lines).rstrip() + "\n"


def links_from(map_path, substring: str) -> list[str]:
    """Official .html URLs from `map_path` whose path contains `substring`, de-duped, in order."""
    text = pathlib.Path(map_path).read_text(encoding="utf-8")
    urls = re.findall(r"\]\((https://developers\.weixin\.qq\.com[^)]+)\)", text)
    return [u for u in dict.fromkeys(urls) if substring in u and u.endswith(".html")]


def groups_for(map_path, base_prefix: str) -> list[str]:
    """Namespaces = the path segment immediately after `base_prefix`, in order, de-duped."""
    pat = re.compile(re.escape(base_prefix) + r"([A-Za-z0-9_-]+)/")
    groups: list[str] = []
    for u in links_from(map_path, base_prefix):
        m = pat.search(u)
        if m and m.group(1) not in groups:
            groups.append(m.group(1))
    return groups


def _resolve_map(name_or_path: str) -> pathlib.Path:
    """Accept a map name ('miniprogram'/'minigame') or an explicit path."""
    p = pathlib.Path(name_or_path)
    return p if p.exists() else (MAP_DIR / f"{name_or_path}.md")


def links_from_map(substring: str) -> list[str]:
    return links_from(MAP_FILE, substring)


def _fetch(url: str) -> str:
    resp = httpx.get(url, headers={"User-Agent": UA}, timeout=30.0, follow_redirects=True)
    resp.raise_for_status()
    return resp.text


def _safe_fetch(url: str) -> str | None:
    try:
        return _fetch(url)
    except Exception as exc:  # one bad page must not kill the whole run
        print(f"WARN: skip {url}: {exc}", file=sys.stderr)
        return None


def _build_for(urls: list[str], heading: str) -> str:
    out = [f"# {heading}", "",
           "> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。",
           "> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。", ""]
    with ThreadPoolExecutor(max_workers=8) as pool:
        pairs = list(zip(urls, pool.map(_safe_fetch, urls)))
    for url, html in pairs:
        if html is None:
            continue
        out.append(extract_reference(html, url))
        out.append("---\n")
    out.append(f"<!-- pages: {sum(1 for _, h in pairs if h is not None)} -->")
    return "\n".join(out)


def api_groups() -> list[str]:
    return groups_for(MAP_FILE, "/miniprogram/dev/api/")


def main(argv: list[str]) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    if len(argv) >= 2 and argv[1] == "components":
        urls = links_from_map("/miniprogram/dev/component/")
        print(_build_for(urls, "微信小程序组件结构化参考 (components)"))
        return 0
    if len(argv) >= 2 and argv[1] == "api-groups":
        print("\n".join(api_groups()))
        return 0
    if len(argv) >= 3 and argv[1] == "api":
        group = argv[2]
        urls = links_from_map(f"/miniprogram/dev/api/{group}/")
        print(_build_for(urls, f"微信小程序 API 结构化参考 — {group}"))
        return 0
    if len(argv) >= 4 and argv[1] == "groups":
        print("\n".join(groups_for(_resolve_map(argv[2]), argv[3])))
        return 0
    if len(argv) >= 6 and argv[1] == "build":
        map_path = _resolve_map(argv[2])
        base, group, heading = argv[3], argv[4], " ".join(argv[5:])
        urls = links_from(map_path, f"{base}{group}/")
        print(_build_for(urls, heading))
        return 0
    print("Usage: uv run build_reference.py [components | api-groups | api <group> | groups <map> <prefix> | build <map> <prefix> <group> <heading>]", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
