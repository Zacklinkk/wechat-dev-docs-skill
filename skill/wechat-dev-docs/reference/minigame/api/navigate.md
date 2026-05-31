# 微信小游戏 API 结构化参考 — navigate

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.restartMiniProgram(Object object)

基础库 2.22.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/navigate/wx.restartMiniProgram.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| path | string |  | 否 | 打开的页面路径，path 中 ? 后面的部分会成为 query |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.navigateToMiniProgram(Object object)

基础库 2.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/navigate/wx.navigateToMiniProgram.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | appId | string |  | 否 | 要打开的小程序 appId |  |
|  | path | string |  | 否 | 打开的页面路径，如果为空则打开首页。path 中 ? 后面的部分会成为 query，在小程序的 `App.onLaunch`、`App.onShow` 和 `Page.onLoad` 的回调函数或小游戏的 [wx.onShow](../base/app/life-cycle/wx.onShow.html) 回调函数、[wx.getLaunchOptionsSync](../base/app/life-cycle/wx.getLaunchOptionsSync.html) 中可以获取到 query 数据。对于小游戏，可以只传入 query 部分，来实现传参效果，如：传入 "?foo=bar"。 |  |
|  | extraData | object |  | 否 | 需要传递给目标小程序的数据，目标小程序可在 `App.onLaunch`，`App.onShow` 中获取到这份数据。如果跳转的是小游戏，可以在 [wx.onShow](../base/app/life-cycle/wx.onShow.html)、[wx.getLaunchOptionsSync](../base/app/life-cycle/wx.getLaunchOptionsSync.html) 中可以获取到这份数据。 |  |
|  | envVersion | string | release | 否 | 要打开的小程序版本。仅在当前小程序为开发版或体验版时此参数有效。如果当前小程序是正式版，则打开的小程序必定是正式版。 |  |
|  | | 合法值 | 说明 | | --- | --- | | develop | 开发版 | | trial | 体验版 | | release | 正式版 | | | | | | |
|  | shortLink | string |  | 否 | 小程序链接，当传递该参数后，可以不传 appId 和 path。链接可以通过【小程序菜单】->【复制链接】获取。 | [2.18.1](../../guide/runtime/client-lib/compatibility.html) |
|  | noRelaunchIfPathUnchanged | boolean | false | 否 | 不reLaunch目标小程序，直接打开目标跳转的小程序退后台时的页面，需满足以下条件：1. 目标跳转的小程序生命周期未被销毁；2. 且目标当次启动的path、query与上次启动相同，apiCategory以wx.getApiCategory接口的返回结果为准。 | [2.24.0](../../guide/runtime/client-lib/compatibility.html) |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| develop | 开发版 |
| trial | 体验版 |
| release | 正式版 |

---

### wx.navigateBackMiniProgram(Object object)

基础库 3.5.6 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/navigate/wx.navigateBackMiniProgram.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| extraData | Object | {} | 否 | 需要返回给上一个小程序的数据，上一个小程序可在 `App.onShow` 中获取到这份数据。 [详情]((App))。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.exitMiniProgram(Object object)

基础库 2.17.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/navigate/wx.exitMiniProgram.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

<!-- pages: 4 -->
