import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "tools" / "build" / "build_maps.py"
_spec = importlib.util.spec_from_file_location("build_maps", _PATH)
build_maps = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build_maps)


def test_extract_section_links_filters_prefix_dedups_and_keeps_titles():
    html = """
    <div class="sidebar">
      <a href="/miniprogram/dev/component/view.html">view 视图容器</a>
      <a href="/miniprogram/dev/component/view.html#样式">view 锚点(dupe)</a>
      <a href="/miniprogram/dev/component/scroll-view.html">scroll-view</a>
      <a href="/miniprogram/dev/api/">API 首页</a>
      <a href="https://other.example.com/x.html">外站</a>
    </div>
    """
    links = build_maps.extract_section_links(html, "/miniprogram/dev/component/")
    hrefs = [h for h, _ in links]
    assert "/miniprogram/dev/component/view.html" in hrefs
    assert "/miniprogram/dev/component/scroll-view.html" in hrefs
    assert "/miniprogram/dev/api/" not in hrefs          # outside prefix
    assert "https://other.example.com/x.html" not in hrefs
    # de-duplicated by path (anchor stripped)
    assert hrefs.count("/miniprogram/dev/component/view.html") == 1
    assert dict(links)["/miniprogram/dev/component/view.html"] == "view 视图容器"
