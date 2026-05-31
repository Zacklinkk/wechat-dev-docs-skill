# 微信小游戏 API 结构化参考 — ad

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.onDirectAdStatusChange(function listener)

基础库 3.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/wx.onDirectAdStatusChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| isInMask | boolean | 当前是否处于蒙层阶段 |
| isInDirectGameAd | boolean | 当前是否处于直接广告中 |
| isEndByAbnormal | boolean | 当前直玩广告是否由于异常流程而结束（如 下拉/搜索 进入正在直玩广告流程中的游戏） |

---

### wx.offDirectAdStatusChange(function listener)

基础库 3.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/wx.offDirectAdStatusChange.html

---

### wx.getShowSplashAdStatus(Object object)

基础库 3.7.8 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/wx.getShowSplashAdStatus.html

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

### Object wx.getDirectAdStatusSync()

基础库 3.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/wx.getDirectAdStatusSync.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| isInMask | boolean | 当前是否处于蒙层阶段 |
| isInDirectGameAd | boolean | 当前是否处于直接广告中 |

---

### RewardedVideoAd wx.createRewardedVideoAd(Object object)

基础库 2.0.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/wx.createRewardedVideoAd.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| adUnitId | string |  | 是 | 广告单元 id |  |
| multiton | boolean |  | 否 | 是否启用多例模式，默认为false | [2.8.0](../../guide/runtime/client-lib/compatibility.html) |
| disableFallbackSharePage | boolean |  | 否 | 是否禁用分享页，默认为false | [3.7.7](../../guide/runtime/client-lib/compatibility.html) |

---

### InterstitialAd wx.createInterstitialAd(Object object)

基础库 2.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/wx.createInterstitialAd.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| adUnitId | string |  | 是 | 广告单元 id |

---

### GridAd wx.createGridAd(Object object)

从基础库2.30.2开始，本接口停止维护

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/wx.createGridAd.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | adUnitId | string |  | 是 | 广告单元 id |
|  | adIntervals | number |  | 否 | 广告自动刷新的间隔时间，单位为秒，参数值必须大于等于30（该参数不传入时 grid(格子) 广告不会自动刷新） |
|  | style | Object |  | 是 | grid(格子) 广告组件的样式 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | left | number |  | 是 | grid(格子) 广告组件的左上角横坐标 | |  | top | number |  | 是 | grid(格子) 广告组件的左上角纵坐标 | |  | width | number |  | 是 | grid(格子) 广告组件的宽度 | |  | height | number |  | 是 | grid(格子) 广告组件的高度 | | | | | |
|  | adTheme | string |  | 是 | grid(格子) 广告广告组件的主题，提供 `white` `black` 两种主题选择。 |
|  | gridCount | number |  | 是 | grid(格子) 广告组件的格子个数，可设置爱5，8两种格子个数样式，默认值为5 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | left | number |  | 是 | grid(格子) 广告组件的左上角横坐标 |
|  | top | number |  | 是 | grid(格子) 广告组件的左上角纵坐标 |
|  | width | number |  | 是 | grid(格子) 广告组件的宽度 |
|  | height | number |  | 是 | grid(格子) 广告组件的高度 |

---

### CustomAd wx.createCustomAd(Object object)

基础库 2.11.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/wx.createCustomAd.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | adUnitId | string |  | 是 | 广告单元 id |
|  | adIntervals | number |  | 是 | 广告自动刷新的间隔时间，单位为秒，参数值必须大于等于30（仅对支持自动刷新的模板生效） |
|  | style | Object |  | 是 | 原生模板广告组件的样式 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | left | number |  | 是 | 原生模板广告组件的左上角横坐标 | |  | top | number |  | 是 | 原生模板广告组件的左上角纵坐标 | |  | width | number |  | 是 | 原生模板广告组件的宽度（仅在某些模板生效，如矩阵格子） | |  | fixed | boolean |  | 是 | (只对小程序适用) 原生模板广告组件是否固定屏幕位置（不跟随屏幕滚动） | | | | | |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | left | number |  | 是 | 原生模板广告组件的左上角横坐标 |
|  | top | number |  | 是 | 原生模板广告组件的左上角纵坐标 |
|  | width | number |  | 是 | 原生模板广告组件的宽度（仅在某些模板生效，如矩阵格子） |
|  | fixed | boolean |  | 是 | (只对小程序适用) 原生模板广告组件是否固定屏幕位置（不跟随屏幕滚动） |

---

### BannerAd wx.createBannerAd(Object object)

从基础库3.5.5开始，本接口停止维护，请使用wx.createCustomAd代替

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/wx.createBannerAd.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | adUnitId | string |  | 是 | 广告单元 id |
|  | adIntervals | number |  | 否 | 广告自动刷新的间隔时间，单位为秒，参数值必须大于等于30（该参数不传入时 Banner 广告不会自动刷新） |
|  | style | Object |  | 是 | banner 广告组件的样式 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | left | number |  | 是 | banner 广告组件的左上角横坐标 | |  | top | number |  | 是 | banner 广告组件的左上角纵坐标 | |  | width | number |  | 是 | banner 广告组件的宽度 | |  | height | number |  | 是 | banner 广告组件的高度 | | | | | |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | left | number |  | 是 | banner 广告组件的左上角横坐标 |
|  | top | number |  | 是 | banner 广告组件的左上角纵坐标 |
|  | width | number |  | 是 | banner 广告组件的宽度 |
|  | height | number |  | 是 | banner 广告组件的高度 |

---

### BannerAd

banner 广告组件。banner 广告组件是一个原生组件，层级比普通组件高。banner 广告组件默认是隐藏的，需要调用 BannerAd.show() 将其显示。banner 广告会根据开发者设置的宽度进行等比缩放，缩放后的尺寸将通过 BannerAd.onResize() 事件中提供。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/BannerAd.html

**Object style**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| left | number | banner 广告组件的左上角横坐标 |
| top | number | banner 广告组件的左上角纵坐标 |
| width | number | banner 广告组件的宽度。最小 300，最大至 `屏幕宽度`（屏幕宽度可以通过 wx.getSystemInfoSync() 获取）。 |
| height | number | banner 广告组件的高度 |
| realWidth | number | banner 广告组件经过缩放后真实的宽度 |
| realHeight | number | banner 广告组件经过缩放后真实的高度 |

---

### BannerAd.destroy()

销毁 banner 广告。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/BannerAd.destroy.html

---

### BannerAd.hide()

隐藏 banner 广告。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/BannerAd.hide.html

---

### BannerAd.offError(function listener)

移除 banner 广告错误事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/BannerAd.offError.html

---

### BannerAd.offLoad(function listener)

移除 banner 广告加载事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/BannerAd.offLoad.html

---

### BannerAd.offResize(function listener)

移除 banner 广告尺寸变化事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/BannerAd.offResize.html

---

### BannerAd.onError(function listener)

监听 banner 广告错误事件。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/BannerAd.onError.html

**function listener**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | errMsg | string | 错误信息 |  |
|  | errCode | number | 错误码 | [2.2.2](../../guide/runtime/client-lib/compatibility.html) |
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

### BannerAd.onLoad(function listener)

监听 banner 广告加载事件。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/BannerAd.onLoad.html

---

### BannerAd.onResize(function listener)

监听 banner 广告尺寸变化事件。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/BannerAd.onResize.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 缩放后的宽度 |
| height | number | 缩放后的高度 |

---

### Promise BannerAd.show()

显示 banner 广告。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/BannerAd.show.html

---

### CustomAd

原生模板广告组件。原生模板广告组件是一个原生组件，层级比普通组件高。原生模板广告组件默认是隐藏的，需要调用 CustomAd.show() 将其显示。如果宽度可配置，原生模板广告会根据开发者设置的宽度进行等比缩放，部分模板缩放后的尺寸会通过 CustomAd.onResize() 事件中提供。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/CustomAd.html

**Object style**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| left | number | 原生模板广告组件的左上角横坐标 |
| top | number | 原生模板广告组件的左上角纵坐标 |
| fixed | boolean | (只对小程序适用) 原生模板广告组件是否固定屏幕位置（不跟随屏幕滚动） |

---

### CustomAd.destroy()

销毁原生模板广告。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/CustomAd.destroy.html

---

### Promise CustomAd.hide()

隐藏原生模板广告。（某些模板广告无法隐藏）

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/CustomAd.hide.html

---

### boolean CustomAd.isShow()

查询原生模板广告展示状态。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/CustomAd.isShow.html

---

### CustomAd.offClose(function listener)

移除原生模板广告关闭事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/CustomAd.offClose.html

---

### CustomAd.offError(function listener)

移除原生模板广告错误事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/CustomAd.offError.html

---

### CustomAd.offHide(function listener)

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/CustomAd.offHide.html

---

### CustomAd.offLoad(function listener)

移除原生模板广告加载事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/CustomAd.offLoad.html

---

### CustomAd.offResize(function listener)

移除原生模板广告宽高回调事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/CustomAd.offResize.html

---

### CustomAd.onClose(function listener)

监听原生模板广告关闭事件（仅部分可被用户关闭的模板支持）。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/CustomAd.onClose.html

---

### CustomAd.onError(function listener)

监听原生模板广告错误事件。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/CustomAd.onError.html

**function listener**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | errMsg | string | 错误信息 |  |
|  | errCode | number | 错误码 | [2.2.2](../../guide/runtime/client-lib/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | 1000 | 后端接口调用失败 | | 1001 | 参数错误 | | 1002 | 广告单元无效 | | 1003 | 内部错误 | | 1004 | 无合适的广告 | | 1005 | 广告组件审核中 | | 1006 | 广告组件被驳回 | | 1007 | 广告组件被封禁 | | 1008 | 广告单元已关闭 | | 2001 | 模板渲染错误 | | 2002 | 模板为空 | | 2003 | 模板解析失败 | | 2004 | 触发频率限制 | | 2005 | 触发频率限制 | | | | |

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
| 2001 | 模板渲染错误 |
| 2002 | 模板为空 |
| 2003 | 模板解析失败 |
| 2004 | 触发频率限制 |
| 2005 | 触发频率限制 |

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
| 2001 | 模板渲染错误 | 渲染过程出现错误 |  |
| 2002 | 模板为空 | 该广告位的广告能力已经被关闭 |  |
| 2003 | 模板解析失败 | 该广告位的广告能力已经被关闭 |  |
| 2004 | 触发频率限制 | 小程序启动一定时间内不允许展示原生模板广告 |  |
| 2005 | 触发频率限制 | 距离小程序插屏广告或者激励视频广告上次播放时间间隔不足，不允许展示原生模板广告 |  |

---

### CustomAd.onHide(function listener)

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/CustomAd.onHide.html

---

### CustomAd.onLoad(function listener)

监听原生模板广告加载事件。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/CustomAd.onLoad.html

---

### CustomAd.onResize(function listener)

监听原生模板广告宽高回调事件（部分横幅模板支持）。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/CustomAd.onResize.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 缩放后的宽度 |
| height | number | 缩放后的高度 |

---

### Promise CustomAd.show()

显示原生模板广告。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/CustomAd.show.html

---

### GridAd

grid(格子) 广告组件。grid(格子) 广告组件是一个原生组件，层级比普通组件高。grid(格子) 广告组件默认是隐藏的，需要调用 GridAd.show() 将其显示。grid(格子) 广告会根据开发者设置的宽度进行等比缩放，缩放后的尺寸将通过 GridAd.onResize() 事件中提供。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/GridAd.html

**Object style**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| left | number | grid(格子) 广告广告组件的左上角横坐标 |
| top | number | grid(格子) 广告组件的左上角纵坐标 |
| width | number | grid(格子) 广告组件的宽度。最小 300，最大至 `屏幕宽度`（屏幕宽度可以通过 wx.getSystemInfoSync() 获取）。 |
| height | number | grid(格子) 广告组件的高度 |
| realWidth | number | grid(格子) 广告组件经过缩放后真实的宽度 |
| realHeight | number | grid(格子) 广告组件经过缩放后真实的高度 |

---

### GridAd.destroy()

从基础库2.30.2开始，本接口停止维护

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/GridAd.destroy.html

---

### GridAd.hide()

从基础库2.30.2开始，本接口停止维护

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/GridAd.hide.html

---

### GridAd.offError(function listener)

从基础库2.30.2开始，本接口停止维护

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/GridAd.offError.html

---

### GridAd.offLoad(function listener)

从基础库2.30.2开始，本接口停止维护

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/GridAd.offLoad.html

---

### GridAd.offResize(function listener)

从基础库2.30.2开始，本接口停止维护

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/GridAd.offResize.html

---

### GridAd.onError(function listener)

从基础库2.30.2开始，本接口停止维护

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/GridAd.onError.html

**function listener**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | errMsg | string | 错误信息 |  |
|  | errCode | number | 错误码 | [2.2.2](../../guide/runtime/client-lib/compatibility.html) |
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

### GridAd.onLoad(function listener)

从基础库2.30.2开始，本接口停止维护

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/GridAd.onLoad.html

---

### GridAd.onResize(function listener)

从基础库2.30.2开始，本接口停止维护

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/GridAd.onResize.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 缩放后的宽度 |
| height | number | 缩放后的高度 |

---

### Promise GridAd.show()

从基础库2.30.2开始，本接口停止维护

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/GridAd.show.html

---

### InterstitialAd

插屏广告组件。插屏广告组件是一个原生组件，层级比普通组件高。插屏广告组件每次创建都会返回一个全新的实例（小程序端的插屏广告实例不允许跨页面使用），默认是隐藏的，需要调用 InterstitialAd.show() 将其显示。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/InterstitialAd.html

---

### InterstitialAd.destroy()

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/InterstitialAd.destroy.html

---

### Promise InterstitialAd.load()

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/InterstitialAd.load.html

---

### InterstitialAd.offClose(function listener)

移除插屏广告关闭事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/InterstitialAd.offClose.html

---

### InterstitialAd.offError(function listener)

移除插屏错误事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/InterstitialAd.offError.html

---

### InterstitialAd.offLoad(function listener)

移除插屏广告加载事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/InterstitialAd.offLoad.html

---

### InterstitialAd.onClose(function listener)

监听插屏广告关闭事件。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/InterstitialAd.onClose.html

---

### InterstitialAd.onError(function listener)

监听插屏错误事件。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/InterstitialAd.onError.html

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

监听插屏广告加载事件。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/InterstitialAd.onLoad.html

---

### Promise InterstitialAd.show()

显示插屏广告。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/InterstitialAd.show.html

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

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/RewardedVideoAd.html

---

### RewardedVideoAd.destroy()

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/RewardedVideoAd.destroy.html

---

### Promise RewardedVideoAd.load()

加载激励视频广告。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/RewardedVideoAd.load.html

---

### RewardedVideoAd.offClose(function listener)

移除用户点击关闭广告按钮的事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/RewardedVideoAd.offClose.html

---

### RewardedVideoAd.offError(function listener)

移除激励视频错误事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/RewardedVideoAd.offError.html

---

### RewardedVideoAd.offLoad(function listener)

移除激励视频广告加载事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/RewardedVideoAd.offLoad.html

---

### RewardedVideoAd.onClose(function listener)

监听用户点击关闭广告按钮的事件。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/RewardedVideoAd.onClose.html

**function listener**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| isEnded | boolean | 视频是否是在用户完整观看的情况下被关闭的 | [2.1.0](../../guide/runtime/client-lib/compatibility.html) |

---

### RewardedVideoAd.onError(function listener)

监听激励视频错误事件。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/RewardedVideoAd.onError.html

**function listener**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | errMsg | string | 错误信息 |  |
|  | errCode | number | 错误码 | [2.2.2](../../guide/runtime/client-lib/compatibility.html) |
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

监听激励视频广告加载事件。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/RewardedVideoAd.onLoad.html

**function listener**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| useFallbackSharePage | boolean | 仅小游戏支持，本次展示使用激励广告分享页 | [3.7.7](../../guide/runtime/client-lib/compatibility.html) |

---

### Promise RewardedVideoAd.show()

显示激励视频广告。激励视频广告将从屏幕下方推入。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ad/RewardedVideoAd.show.html

---

<!-- pages: 64 -->
