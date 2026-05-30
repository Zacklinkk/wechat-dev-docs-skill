import importlib.util
import pathlib
import pytest

# Load the PEP723 script as a module
_PATH = pathlib.Path(__file__).resolve().parents[1] / "skill" / "wechat-dev-docs" / "tools" / "fetch_doc.py"
_spec = importlib.util.spec_from_file_location("fetch_doc", _PATH)
fetch_doc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fetch_doc)


def test_normalize_url_passes_full_official_url():
    url = "https://developers.weixin.qq.com/miniprogram/dev/component/view.html"
    assert fetch_doc.normalize_url(url) == url


def test_normalize_url_prefixes_root_relative_path():
    assert fetch_doc.normalize_url("/miniprogram/dev/component/view.html") == \
        "https://developers.weixin.qq.com/miniprogram/dev/component/view.html"


def test_normalize_url_prefixes_bare_path():
    assert fetch_doc.normalize_url("minigame/dev/api/render/canvas/wx.createCanvas.html") == \
        "https://developers.weixin.qq.com/minigame/dev/api/render/canvas/wx.createCanvas.html"


def test_normalize_url_rejects_foreign_host():
    with pytest.raises(ValueError):
        fetch_doc.normalize_url("https://evil.example.com/x")


def test_normalize_url_rejects_http_scheme():
    with pytest.raises(ValueError):
        fetch_doc.normalize_url("http://developers.weixin.qq.com/x")


def test_html_to_markdown_extracts_content_strips_chrome_absolutizes_links():
    html = """
    <html><body>
      <div class="sidebar"><a href="/nav">NAV NOISE</a></div>
      <main class="page"><div class="theme-container">
        <h1>view</h1>
        <p>视图容器。</p>
        <table><tr><th>属性</th><th>类型</th></tr><tr><td>hover-class</td><td>string</td></tr></table>
        <a href="/miniprogram/dev/component/scroll-view.html">scroll-view</a>
      </div></main>
      <footer>FOOTER NOISE</footer>
    </body></html>
    """
    out = fetch_doc.html_to_markdown(html, "https://developers.weixin.qq.com/miniprogram/dev/component/view.html")
    assert "# view" in out
    assert "视图容器" in out
    assert "hover-class" in out                      # table preserved
    assert "NAV NOISE" not in out and "FOOTER NOISE" not in out   # chrome stripped
    assert "https://developers.weixin.qq.com/miniprogram/dev/component/scroll-view.html" in out  # absolutized
