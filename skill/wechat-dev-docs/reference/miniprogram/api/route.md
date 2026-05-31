# 微信小程序 API 结构化参考 — route

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.switchTab(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.switchTab.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| url | string |  | 是 | 需要跳转的 tabBar 页面的路径 (代码包路径)（需在 app.json 的 [tabBar](../../reference/configuration/app.html#tabbar) 字段定义的页面），路径后不能带参数。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.rewriteRoute(Object object)

基础库 3.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.rewriteRoute.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| url | string |  | 是 | 重写目标页面的路径 (代码包路径), 路径后可以带参数。参数与路径之间使用 `?` 分隔，参数键与参数值用 `=` 相连，不同参数用 `&` 分隔；如 `'path?key=value&key2=value2'` |
| preserveQuery | boolean | false | 否 | 是否直接保留当前路由事件的参数，默认为 `false`；开启时，`url` 里面传入的参数会被丢弃 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.reLaunch(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.reLaunch.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| url | string |  | 是 | 需要跳转的应用内页面路径 (代码包路径)，路径后可以带参数。参数与路径之间使用?分隔，参数键与参数值用=相连，不同参数用&分隔；如 'path?key=value&key2=value2' |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.redirectTo(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.redirectTo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| url | string |  | 是 | 需要跳转的应用内非 tabBar 的页面的路径 (代码包路径), 路径后可以带参数。参数与路径之间使用 `?` 分隔，参数键与参数值用 `=` 相连，不同参数用 `&` 分隔；如 'path?key=value&key2=value2' |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.navigateTo(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.navigateTo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| url | string |  | 是 | 需要跳转的应用内非 tabBar 的页面的路径 (代码包路径), 路径后可以带参数。参数与路径之间使用 `?` 分隔，参数键与参数值用 `=` 相连，不同参数用 `&` 分隔；如 'path?key=value&key2=value2' |
| events | Object |  | 否 | 页面间通信接口，用于监听被打开页面发送到当前页面的数据。基础库 2.7.3 开始支持。 |
| routeType | string |  | 否 | 2.29.2 自定义路由类型，相关文档 [自定义路由](../../framework/runtime/skyline/custom-route.html) |
| routeConfig | Object |  | 否 | 3.4.0 自定义路由配置，相关文档 [自定义路由](../../framework/runtime/skyline/custom-route.html) |
| routeOptions | Object |  | 否 | 3.4.0 自定义路由参数，相关文档 [自定义路由](../../framework/runtime/skyline/custom-route.html) |
| withOpenContainer | Object |  | 否 | 3.12.2 skyline 下指定路由动画所用OpenContainerContext，相关文档 [OpenContainerContext](../../framework/custom-component/glass-easel/skyline.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| eventChannel | [EventChannel](EventChannel.html) | 和被打开页面进行通信 |

---

### wx.navigateBack(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.navigateBack.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| delta | number | 1 | 否 | 返回的页面数，如果 delta 大于现有页面数，则返回到页面栈中只剩一个页面为止。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### EventChannel

基础库 2.7.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/route/EventChannel.html

---

### EventChannel.emit(string eventName, any args)

基础库 2.7.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/route/EventChannel.emit.html

---

### EventChannel.off(string eventName, function fn)

基础库 2.7.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/route/EventChannel.off.html

---

### EventChannel.on(string eventName, function fn)

基础库 2.7.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/route/EventChannel.on.html

---

### EventChannel.once(string eventName, function fn)

基础库 2.7.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/route/EventChannel.once.html

---

### wx.router

基础库 2.29.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/route/router/wx.router.html

---

### router.addRouteBuilder(string routeType, function routeBuilder)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/route/router/base/router.addRouteBuilder.html

---

### router.getRouteContext(Object this)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/route/router/base/router.getRouteContext.html

---

### router.removeRouteBuilder(string routeType)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/route/router/base/router.removeRouteBuilder.html

---

<!-- pages: 15 -->
