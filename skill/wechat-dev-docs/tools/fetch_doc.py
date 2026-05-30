#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["httpx>=0.27", "beautifulsoup4>=4.12", "markdownify>=0.13"]
# ///
"""Fetch one WeChat mini-program / mini-game doc page and print it as clean markdown.

Usage:
    uv run fetch_doc.py <official-url-or-path>

Only developers.weixin.qq.com is allowed. Prose is © Tencent; this tool extracts it
live at use time and does not store it.
"""
from __future__ import annotations

import sys
from urllib.parse import urljoin, urlparse

import httpx
from bs4 import BeautifulSoup
from markdownify import markdownify as md

BASE = "https://developers.weixin.qq.com"
ALLOWED_HOST = "developers.weixin.qq.com"
CONTENT_SELECTORS = ["main.page", ".theme-container .content", "main", "#app"]
STRIP_SELECTORS = [
    "script", "style", "nav", "header", "footer", "aside",
    ".sidebar", ".navbar", ".page-nav", ".page-edit", ".global-ui",
]
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) wechat-dev-docs-skill/1.0"


def normalize_url(target: str) -> str:
    """Turn a URL or path into a validated absolute official URL."""
    target = target.strip()
    if target.startswith(("http://", "https://")):
        url = target
    elif target.startswith("/"):
        url = BASE + target
    else:
        url = BASE + "/" + target
    host = urlparse(url).netloc
    if host != ALLOWED_HOST:
        raise ValueError(
            f"Refusing to fetch non-official host {host!r}. Only {ALLOWED_HOST} is allowed."
        )
    return url


def html_to_markdown(html: str, base_url: str) -> str:
    """Extract the doc content node, strip site chrome, absolutize links, return markdown."""
    soup = BeautifulSoup(html, "html.parser")
    node = None
    for sel in CONTENT_SELECTORS:
        node = soup.select_one(sel)
        if node is not None:
            break
    if node is None:
        node = soup.body or soup
    for sel in STRIP_SELECTORS:
        for el in node.select(sel):
            el.decompose()
    for a in node.find_all("a", href=True):
        a["href"] = urljoin(base_url, a["href"])
    for img in node.find_all("img", src=True):
        img["src"] = urljoin(base_url, img["src"])
    markdown = md(str(node), heading_style="ATX")
    # collapse runs of >2 blank lines
    out, blank = [], 0
    for line in (ln.rstrip() for ln in markdown.splitlines()):
        if line == "":
            blank += 1
            if blank <= 2:
                out.append(line)
        else:
            blank = 0
            out.append(line)
    return "\n".join(out).strip()


def fetch_doc(target: str, timeout: float = 30.0) -> str:
    """Fetch an official doc page and return a markdown document with a source header."""
    url = normalize_url(target)
    resp = httpx.get(url, headers={"User-Agent": UA}, timeout=timeout, follow_redirects=True)
    resp.raise_for_status()
    title_tag = BeautifulSoup(resp.text, "html.parser").find("title")
    title = title_tag.get_text(strip=True) if title_tag else url
    body = html_to_markdown(resp.text, url)
    header = (
        f"<!-- Source: {url} | 正文版权归腾讯所有,内容以官方为准 -->\n"
        f"# {title}\n\n"
        f"> 来源 / Source: {url}\n\n---\n\n"
    )
    return header + body


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print("Usage: uv run fetch_doc.py <official-url-or-path>", file=sys.stderr)
        return 2
    try:
        print(fetch_doc(argv[1]))
        return 0
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except httpx.HTTPError as exc:
        print(f"Error: HTTP request failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
