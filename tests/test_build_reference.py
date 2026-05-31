import importlib.util, pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "tools" / "build" / "build_reference.py"
_spec = importlib.util.spec_from_file_location("build_reference", _PATH)
build_reference = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build_reference)


def test_clean_heading_strips_vuepress_anchor_hash():
    assert build_reference.clean_heading("#scroll-view") == "scroll-view"
    assert build_reference.clean_heading("  ## 参数 ") == "参数"
    assert build_reference.clean_heading("wx.request(Object object)") == "wx.request(Object object)"


def test_extract_reference_keeps_facts_drops_prose_and_code():
    html = """
    <html><body>
      <div class="sidebar"><a href="/x">NAV</a></div>
      <main class="page"><div class="theme-container">
        <h1>#scroll-view</h1>
        <p>基础库 1.0.0 开始支持。</p>
        <p>这是一段很长的说明散文,应当被丢弃,不进入参考。</p>
        <h2>#属性说明</h2>
        <table><thead><tr><th>属性</th><th>类型</th><th>默认值</th></tr></thead>
          <tbody><tr><td>scroll-x</td><td>boolean</td><td>false</td></tr></tbody></table>
        <h2>#示例代码</h2>
        <pre><code>Page({})</code></pre>
      </div></main>
      <footer>FOOTER</footer>
    </body></html>
    """
    out = build_reference.extract_reference(html, "https://developers.weixin.qq.com/miniprogram/dev/component/scroll-view.html")
    assert "### scroll-view" in out
    assert "基础库 1.0.0 开始支持。" in out
    assert "这是一段很长的说明散文" not in out
    assert "scroll-x" in out and "boolean" in out
    assert "属性说明" in out
    assert "Page({})" not in out
    assert "NAV" not in out and "FOOTER" not in out
    assert "scroll-view.html" in out


def test_links_from_map_filters_by_substring(tmp_path, monkeypatch):
    mapfile = tmp_path / "miniprogram.md"
    mapfile.write_text(
        "- [view](https://developers.weixin.qq.com/miniprogram/dev/component/view.html)\n"
        "- [wx.request](https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html)\n"
        "- [guide](https://developers.weixin.qq.com/miniprogram/dev/framework/quickstart/)\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(build_reference, "MAP_FILE", mapfile)
    comp = build_reference.links_from_map("/component/")
    api = build_reference.links_from_map("/api/")
    assert comp == ["https://developers.weixin.qq.com/miniprogram/dev/component/view.html"]
    assert api == ["https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html"]
