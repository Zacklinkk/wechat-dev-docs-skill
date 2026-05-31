# wechat-dev-docs · 让 AI 读懂微信小程序/小游戏文档

[![CI](https://github.com/Zacklinkk/wechat-dev-docs-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/Zacklinkk/wechat-dev-docs-skill/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Claude Skill](https://img.shields.io/badge/Claude-Skill-8A63D2.svg)](https://docs.claude.com/en/docs/claude-code/skills)

> **Make WeChat mini-program & mini-game docs agent-readable.**

微信官方开发文档是为**人**写的:单页应用、深层导航、正文混在 UI 里,AI 几乎没法整页喂、没法快速检索。
这个 skill 把它变成**为 agent 写的**:一张完整的导航地图 + 一个"把任意官方页面变成干净 markdown"的工具。

## 痛点 → 解法 / Before → After

| | 之前 Before | 之后 After |
|---|---|---|
| 找页面 | 在 SPA 里逐层点开侧边栏 | 在 `maps/*.md` 里一次 grep 命中,直接拿官方深链 |
| 读正文 | 复制粘贴混着导航/页脚 | `uv run fetch_doc.py <url>` → 纯 markdown(标题/表格/代码块) |
| 时效性 | 离线副本很快过期 | 永远现抓官方,绝不过期 |

## 30 秒上手 / Quickstart

```bash
git clone https://github.com/Zacklinkk/wechat-dev-docs-skill
cd wechat-dev-docs-skill
# 全局安装(任意项目可用):
pwsh -File install.ps1      # Windows
./install.sh                # macOS / Linux
```

重启 Claude Code 后,问它"用 view 组件做个可滚动列表"之类的问题,它会自动查地图、按需抓全文。

手动试一下抓取工具:
```bash
uv run skill/wechat-dev-docs/tools/fetch_doc.py \
  https://developers.weixin.qq.com/miniprogram/dev/component/view.html
```

## 能力一览 / What's inside

- **完整导航地图**:`maps/miniprogram.md` + `maps/minigame.md`,覆盖指南/框架/组件/API/服务端/工具/云开发,每条带官方深链。
- **按需抓取**:`fetch_doc.py`,URL → 干净 markdown,自包含(`uv run`,依赖自动装),只允许官方域名。
- **维护者工具**:`tools/build/build_maps.py`,文档改版时一键重生成地图。

## 架构 / How it works

官方站基于 VuePress,正文与侧边栏都在 SSR HTML 里 → 纯 `httpx` 即可爬取与转换,无需浏览器。
仓库只存**事实**(标题、URL、结构),**正文按需现抓**——这让它既不过期,也可公开发布。

```
maps/ (静态地图) ──▶ 找到官方 URL ──▶ fetch_doc.py ──▶ 干净 markdown ──▶ 喂给 agent
```

## 版权 / License & Content

代码以 **MIT** 授权。文档**正文版权归腾讯所有**,本仓库不转载正文,仅提供结构化索引 +
实时抓取工具,内容以[官方文档](https://developers.weixin.qq.com/miniprogram/dev/framework/)为准。
详见 [`NOTICE.md`](./NOTICE.md)。

## 贡献 / Contributing

欢迎 PR:补充结构化参考、改进抓取清洗、修复失效链接。请勿提交官方正文的整页转载。
