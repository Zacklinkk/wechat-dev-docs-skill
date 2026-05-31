# 微信小程序 API 结构化参考 — ad

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.getShowSplashAdStatus(Object object)

基础库 3.7.8 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/wx.getShowSplashAdStatus.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | status | string | 封面广告组件展示状态 |
|  | | 合法值 | 说明 | | --- | --- | | unknown | 初始值，状态未知 | | pending | 进行展示中 | | success | 展示成功 | | fail | 展示失败 | | | |
|  | code | number | 封面广告组件展示状态码 |
|  | | 合法值 | 说明 | | --- | --- | | -1 | 初始值，状态未知 | | 1 | 展示成功 | | 2 | 主动拦截过滤，不展示广告 | | 3 | 展示超时 | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| unknown | 初始值，状态未知 |
| pending | 进行展示中 |
| success | 展示成功 |
| fail | 展示失败 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| -1 | 初始值，状态未知 |
| 1 | 展示成功 |
| 2 | 主动拦截过滤，不展示广告 |
| 3 | 展示超时 |

---

### RewardedVideoAd wx.createRewardedVideoAd(Object object)

基础库 2.0.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/wx.createRewardedVideoAd.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| adUnitId | string |  | 是 | 广告单元 id |  |
| multiton | boolean |  | 否 | 是否启用多例模式，默认为false | [2.8.0](../../framework/compatibility.html) |
| disableFallbackSharePage | boolean |  | 否 | 是否禁用分享页，默认为false | [3.7.7](../../framework/compatibility.html) |

---

### InterstitialAd wx.createInterstitialAd(Object object)

基础库 2.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/wx.createInterstitialAd.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| adUnitId | string |  | 是 | 广告单元 id |

---

### InterstitialAd

插屏广告组件。插屏广告组件是一个原生组件，层级比普通组件高。插屏广告组件每次创建都会返回一个全新的实例（小程序端的插屏广告实例不允许跨页面使用），默认是隐藏的，需要调用 InterstitialAd.show() 将其显示。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/InterstitialAd.html

---

### InterstitialAd.destroy()

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/InterstitialAd.destroy.html

---

### Promise InterstitialAd.load()

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/InterstitialAd.load.html

---

### InterstitialAd.offClose(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/InterstitialAd.offClose.html

---

### InterstitialAd.offError(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/InterstitialAd.offError.html

---

### InterstitialAd.offLoad(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/InterstitialAd.offLoad.html

---

### InterstitialAd.onClose(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/InterstitialAd.onClose.html

---

### InterstitialAd.onError(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/InterstitialAd.onError.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | errMsg | string | 错误信息 |
|  | errCode | number | 错误码 |
|  | | 合法值 | 说明 | | --- | --- | | 1000 | 后端接口调用失败 | | 1001 | 参数错误 | | 1002 | 广告单元无效 | | 1003 | 内部错误 | | 1004 | 无合适的广告 | | 1005 | 广告组件审核中 | | 1006 | 广告组件被驳回 | | 1007 | 广告组件被封禁 | | 1008 | 广告单元已关闭 | | | |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| 1000 | 后端接口调用失败 |
| 1001 | 参数错误 |
| 1002 | 广告单元无效 |
| 1003 | 内部错误 |
| 1004 | 无合适的广告 |
| 1005 | 广告组件审核中 |
| 1006 | 广告组件被驳回 |
| 1007 | 广告组件被封禁 |
| 1008 | 广告单元已关闭 |

**错误码信息与解决方案表**

| 代码 | 异常情况 | 理由 | 解决方案 |
| --- | --- | --- | --- |
| 1000 | 后端错误调用失败 | 该项错误不是开发者的异常情况 | 一般情况下忽略一段时间即可恢复。 |
| 1001 | 参数错误 | 使用方法错误 | 可以前往developers.weixin.qq.com确认具体教程（小程序和小游戏分别有各自的教程，可以在顶部选项中，“设计”一栏的右侧进行切换。 |
| 1002 | 广告单元无效 | 可能是拼写错误、或者误用了其他APP的广告ID | 请重新前往mp.weixin.qq.com确认广告位ID。 |
| 1003 | 内部错误 | 该项错误不是开发者的异常情况 | 一般情况下忽略一段时间即可恢复。 |
| 1004 | 无适合的广告 | 广告不是每一次都会出现，这次没有出现可能是由于该用户不适合浏览广告 | 属于正常情况，且开发者需要针对这种情况做形态上的兼容。 |
| 1005 | 广告组件审核中 | 你的广告正在被审核，无法展现广告 | 请前往mp.weixin.qq.com确认审核状态，且开发者需要针对这种情况做形态上的兼容。 |
| 1006 | 广告组件被驳回 | 你的广告审核失败，无法展现广告 | 请前往mp.weixin.qq.com确认审核状态，且开发者需要针对这种情况做形态上的兼容。 |
| 1007 | 广告组件被封禁 | 你的广告能力已经被封禁，封禁期间无法展现广告 | 请前往mp.weixin.qq.com确认小程序广告封禁状态。 |
| 1008 | 广告单元已关闭 | 该广告位的广告能力已经被关闭 | 请前往mp.weixin.qq.com重新打开对应广告位的展现。 |

---

### InterstitialAd.onLoad(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/InterstitialAd.onLoad.html

---

### Promise InterstitialAd.show()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/InterstitialAd.show.html

**错误码信息表**

| 代码 | 异常情况 | 理由 |
| --- | --- | --- |
| 2001 | 触发频率限制 | 小程序启动一定时间内不允许展示插屏广告 |
| 2002 | 触发频率限制 | 距离小程序插屏广告或者激励视频广告上次播放时间间隔不足，不允许展示插屏广告 |
| 2003 | 触发频率限制 | 当前正在播放激励视频广告或者插屏广告，不允许再次展示插屏广告 |
| 2004 | 广告渲染失败 | 该项错误不是开发者的异常情况，或因小程序页面切换导致广告渲染失败 |
| 2005 | 广告调用异常 | 插屏广告实例不允许跨页面调用 |

---

### RewardedVideoAd

激励视频广告组件。激励视频广告组件是一个原生组件，层级比普通组件高。激励视频广告是一个单例（小游戏端是全局单例，小程序端是页面内单例，在小程序端的单例对象不允许跨页面使用），默认是隐藏的，需要调用 RewardedVideoAd.show() 将其显示。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/RewardedVideoAd.html

---

### RewardedVideoAd.destroy()

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/RewardedVideoAd.destroy.html

---

### Promise RewardedVideoAd.load()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/RewardedVideoAd.load.html

---

### RewardedVideoAd.offClose(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/RewardedVideoAd.offClose.html

---

### RewardedVideoAd.offError(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/RewardedVideoAd.offError.html

---

### RewardedVideoAd.offLoad(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/RewardedVideoAd.offLoad.html

---

### RewardedVideoAd.onClose(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/RewardedVideoAd.onClose.html

**function listener**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| isEnded | boolean | 视频是否是在用户完整观看的情况下被关闭的 | [2.1.0](../../framework/compatibility.html) |

---

### RewardedVideoAd.onError(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/RewardedVideoAd.onError.html

**function listener**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | errMsg | string | 错误信息 |  |
|  | errCode | number | 错误码 | [2.2.2](../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | 1000 | 后端接口调用失败 | | 1001 | 参数错误 | | 1002 | 广告单元无效 | | 1003 | 内部错误 | | 1004 | 无合适的广告 | | 1005 | 广告组件审核中 | | 1006 | 广告组件被驳回 | | 1007 | 广告组件被封禁 | | 1008 | 广告单元已关闭 | | | | |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| 1000 | 后端接口调用失败 |
| 1001 | 参数错误 |
| 1002 | 广告单元无效 |
| 1003 | 内部错误 |
| 1004 | 无合适的广告 |
| 1005 | 广告组件审核中 |
| 1006 | 广告组件被驳回 |
| 1007 | 广告组件被封禁 |
| 1008 | 广告单元已关闭 |

**错误码信息与解决方案表**

| 代码 | 异常情况 | 理由 | 解决方案 |
| --- | --- | --- | --- |
| 1000 | 后端错误调用失败 | 该项错误不是开发者的异常情况 | 一般情况下忽略一段时间即可恢复。 |
| 1001 | 参数错误 | 使用方法错误 | 可以前往developers.weixin.qq.com确认具体教程（小程序和小游戏分别有各自的教程，可以在顶部选项中，“设计”一栏的右侧进行切换。 |
| 1002 | 广告单元无效 | 可能是拼写错误、或者误用了其他APP的广告ID | 请重新前往mp.weixin.qq.com确认广告位ID。 |
| 1003 | 内部错误 | 该项错误不是开发者的异常情况 | 一般情况下忽略一段时间即可恢复。 |
| 1004 | 无适合的广告 | 广告不是每一次都会出现，这次没有出现可能是由于该用户不适合浏览广告 | 属于正常情况，且开发者需要针对这种情况做形态上的兼容。 |
| 1005 | 广告组件审核中 | 你的广告正在被审核，无法展现广告 | 请前往mp.weixin.qq.com确认审核状态，且开发者需要针对这种情况做形态上的兼容。 |
| 1006 | 广告组件被驳回 | 你的广告审核失败，无法展现广告 | 请前往mp.weixin.qq.com确认审核状态，且开发者需要针对这种情况做形态上的兼容。 |
| 1007 | 广告组件被封禁 | 你的广告能力已经被封禁，封禁期间无法展现广告 | 请前往mp.weixin.qq.com确认小程序广告封禁状态。 |
| 1008 | 广告单元已关闭 | 该广告位的广告能力已经被关闭 | 请前往mp.weixin.qq.com重新打开对应广告位的展现。 |

---

### RewardedVideoAd.onLoad(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/RewardedVideoAd.onLoad.html

**function listener**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| useFallbackSharePage | boolean | 仅小游戏支持，本次展示使用激励广告分享页 | [3.7.7](../../framework/compatibility.html) |

---

### Promise RewardedVideoAd.show()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ad/RewardedVideoAd.show.html

---

<!-- pages: 23 -->
