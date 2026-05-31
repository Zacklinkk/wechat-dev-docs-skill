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

BASE = "https://developers.weixin.qq.com"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) wechat-dev-docs-skill-build/1.0"
MAP_FILE = pathlib.Path(__file__).resolve().parents[2] / "skill" / "wechat-dev-docs" / "maps" / "miniprogram.md"
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
    first_p = node.find("p")
    brief = " ".join(first_p.get_text(strip=True).split()) if first_p else ""

    lines = [f"### {title}", ""]
    if brief:
        lines += [brief, ""]
    lines += [f"官方 / Source: {url}", ""]
    for table in node.find_all("table"):
        prev = table.find_previous(["h2", "h3"])
        label = clean_heading(prev.get_text()) if prev else ""
        if label:
            lines += [f"**{label}**", ""]
        lines += [table_to_markdown(table), ""]
    return "\n".join(lines).rstrip() + "\n"


def links_from_map(substring: str) -> list[str]:
    """Official .html URLs from the Phase-1 map whose path contains `substring`, de-duped, in order."""
    text = MAP_FILE.read_text(encoding="utf-8")
    urls = re.findall(r"\]\((https://developers\.weixin\.qq\.com[^)]+)\)", text)
    return [u for u in dict.fromkeys(urls) if substring in u and u.endswith(".html")]


def _fetch(url: str) -> str:
    resp = httpx.get(url, headers={"User-Agent": UA}, timeout=30.0, follow_redirects=True)
    resp.raise_for_status()
    return resp.text


def _safe_fetch(url: str):
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
    """Discover API namespaces (the path segment after /api/)."""
    groups = []
    for u in links_from_map("/miniprogram/dev/api/"):
        m = re.search(r"/api/([a-z0-9-]+)/", u)
        if m and m.group(1) not in groups:
            groups.append(m.group(1))
    return groups


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
    print("Usage: uv run build_reference.py [components | api-groups | api <group>]", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
