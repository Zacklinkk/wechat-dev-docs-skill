#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["httpx>=0.27", "beautifulsoup4>=4.12"]
# ///
"""Maintainer tool: crawl WeChat doc section roots and emit a navigation map markdown.

NOT shipped to ~/.claude/skills — used only to (re)generate skill/wechat-dev-docs/maps/*.md.

Usage:
    uv run build_maps.py miniprogram > skill/wechat-dev-docs/maps/miniprogram.md
    uv run build_maps.py minigame    > skill/wechat-dev-docs/maps/minigame.md
"""
from __future__ import annotations

import sys
from concurrent.futures import ThreadPoolExecutor

import httpx
from bs4 import BeautifulSoup

BASE = "https://developers.weixin.qq.com"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) wechat-dev-docs-skill-build/1.0"

# Verified top-level section roots. Each root's SSR HTML carries that section's full sidebar.
SECTIONS = {
    "miniprogram": {
        "prefix": "/miniprogram/dev/",
        "roots": [
            ("指南 Guide", "/miniprogram/dev/framework/"),
            ("框架 Reference", "/miniprogram/dev/reference/"),
            ("组件 Components", "/miniprogram/dev/component/"),
            ("API", "/miniprogram/dev/api/"),
            ("服务端 Server", "/miniprogram/dev/server/API/"),
            ("工具 DevTools", "/miniprogram/dev/devtools/devtools.html"),
            ("云开发 CloudBase", "/miniprogram/dev/wxcloudservice/wxcloud/basis/getting-started.html"),
        ],
    },
    "minigame": {
        "prefix": "/minigame/dev/",
        # Seed with the guide + reference/api/component roots; refined in Task 4 Step 1.
        "roots": [
            ("指南 Guide", "/minigame/dev/guide/"),
            ("API", "/minigame/dev/api/"),
            ("组件 Components", "/minigame/dev/reference/components/"),
            ("引擎 Reference", "/minigame/dev/reference/"),
        ],
    },
}


def extract_section_links(html: str, prefix: str) -> list[tuple[str, str]]:
    """Return [(href_without_anchor, title)] for sidebar links under `prefix`, de-duped."""
    soup = BeautifulSoup(html, "html.parser")
    container = soup.select_one(".sidebar") or soup
    seen: dict[str, str] = {}
    for a in container.find_all("a", href=True):
        href = a["href"].split("#")[0]
        if not href.startswith(prefix):
            continue
        title = a.get_text(strip=True)
        if title and href not in seen:
            seen[href] = title
    return list(seen.items())


def fetch(path: str) -> str:
    url = BASE + path if path.startswith("/") else path
    resp = httpx.get(url, headers={"User-Agent": UA}, timeout=30.0, follow_redirects=True)
    resp.raise_for_status()
    return resp.text


def build(domain: str) -> str:
    cfg = SECTIONS[domain]
    prefix = cfg["prefix"]
    lines = [f"# 微信{'小程序' if domain == 'miniprogram' else '小游戏'}文档导航地图 ({domain})", ""]
    lines.append("> 由 tools/build/build_maps.py 生成。每条目为官方页面标题 + 深链。")
    lines.append("> 需要某页全文时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。")
    lines.append("")
    with ThreadPoolExecutor(max_workers=8) as pool:
        htmls = list(pool.map(lambda r: fetch(r[1]), cfg["roots"]))
    global_seen: set[str] = set()
    for (heading, _root), html in zip(cfg["roots"], htmls):
        links = extract_section_links(html, prefix)
        fresh = [(h, t) for h, t in links if h not in global_seen]
        if not fresh:
            continue
        lines.append(f"## {heading}")
        lines.append("")
        for href, title in fresh:
            global_seen.add(href)
            lines.append(f"- [{title}]({BASE}{href})")
        lines.append("")
    lines.append(f"<!-- total pages: {len(global_seen)} -->")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] not in SECTIONS:
        print(f"Usage: uv run build_maps.py [{'|'.join(SECTIONS)}]", file=sys.stderr)
        return 2
    print(build(argv[1]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
