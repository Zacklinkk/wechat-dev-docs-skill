# 微信小游戏 API 结构化参考 — share

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.updateShareMenu(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.updateShareMenu.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | withShareTicket | boolean | false | 否 | 是否使用带 shareTicket 的转发[详情](../../guide/open-ability/share/share.html) |  |
|  | isUpdatableMessage | boolean | false | 否 | 是否是动态消息，详见[动态消息](../../guide/open-ability/share/updatable-message.html) | [2.4.0](../../guide/runtime/client-lib/compatibility.html) |
|  | activityId | string |  | 否 | 动态消息的 activityId。通过 [updatableMessage.createActivityId](errorupdatableMessage.createActivityId)) 接口获取 | [2.4.0](../../guide/runtime/client-lib/compatibility.html) |
|  | toDoActivityId | string |  | 否 | 群待办消息的id，通过toDoActivityId可以把多个群待办消息聚合为同一个。通过 [updatableMessage.createActivityId](errorupdatableMessage.createActivityId)) 接口获取。详见[群待办消息](../../guide/open-ability/share/share.html) | [2.11.0](../../guide/runtime/client-lib/compatibility.html) |
|  | templateInfo | Object |  | 否 | 动态消息的模板信息 | [2.4.0](../../guide/runtime/client-lib/compatibility.html) |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | parameterList | Array.<Object> |  | 是 | 参数列表 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | name | string |  | 是 | 参数名 | |  | value | string |  | 是 | 参数值 | | | | | | |  | templateId | string |  | 是 | 模板ID | | | | | | |
|  | isPrivateMessage | boolean |  | 否 | 是否是私密消息。详见 [小程序私密消息](../../guide/open-ability/share/private-message.html) | [2.13.0](../../guide/runtime/client-lib/compatibility.html) |
|  | participant | Array.<string> | [] | 否 | 参与用户此聊天室下的 group\_openid 列表 |  |
|  | useForChatTool | boolean | false | 否 | 聊天工具模式特殊动态消息 | [3.7.8](../../guide/runtime/client-lib/compatibility.html) |
|  | chooseType | number | 1 | 否 | 指定成员的方式 | [3.7.8](../../guide/runtime/client-lib/compatibility.html) |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | parameterList | Array.<Object> |  | 是 | 参数列表 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | name | string |  | 是 | 参数名 | |  | value | string |  | 是 | 参数值 | | | | | |
|  | templateId | string |  | 是 | 模板ID |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | name | string |  | 是 | 参数名 |
|  | value | string |  | 是 | 参数值 |

---

### wx.startHandoff(Object object)

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.startHandoff.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.showShareMenu(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.showShareMenu.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| withShareTicket | boolean | false | 否 | 是否使用带 shareTicket 的转发[详情](../../guide/open-ability/share/share.html) |  |
| menus | Array.<string> |  | 否 | 本接口为 Beta 版本，暂只在 Android 平台支持。需要显示的转发按钮名称列表，默认['shareAppMessage']。按钮名称合法值包含 "shareAppMessage"、"shareTimeline" 两种 | [2.11.3](../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### wx.showShareImageMenu(Object object)

基础库 2.14.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.showShareImageMenu.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| path | string |  | 是 | 要分享的图片地址，必须为本地路径或临时路径 |  |
| needShowEntrance | boolean | false | 否 | 分享的图片消息是否要带小程序入口 (仅部分小程序类目可用) | [3.2.0](../../guide/runtime/client-lib/compatibility.html) |
| entrancePath | string | '' | 否 | 从消息小程序入口打开小程序的路径，如果当前页面允许分享给朋友，则默认为当前页面路径，否则默认为小程序首页 | [3.2.0](../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### wx.shareAppMessage(Object object)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.shareAppMessage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| title | string |  | 否 | 转发标题，不传则默认使用当前小游戏的昵称。 |  |
| imageUrl | string |  | 否 | 转发显示图片的链接，可以是网络图片路径或本地图片文件路径或相对代码包根目录的图片文件路径。显示图片长宽比是 5:4 |  |
| query | string |  | 否 | 查询字符串，从这条转发消息进入后，可通过 wx.getLaunchOptionsSync() 或 wx.onShow() 获取启动参数中的 query。必须是 key1=val1&key2=val2 的格式。 |  |
| imageUrlId | string |  | 否 | 审核通过的图片编号，详见 [使用审核通过的转发图片](../../guide/open-ability/share/share.html#%E4%BD%BF%E7%94%A8%E5%AE%A1%E6%A0%B8%E9%80%9A%E8%BF%87%E7%9A%84%E8%BD%AC%E5%8F%91%E5%9B%BE%E7%89%87) | [2.4.3](../../guide/runtime/client-lib/compatibility.html) |
| toCurrentGroup | boolean | true | 否 | 是否转发到当前群。该参数只对从群工具栏打开的场景下生效，默认转发到当前群，填入false时可转发到其他会话。 | [2.12.2](../../guide/runtime/client-lib/compatibility.html) |
| path | string |  | 否 | 独立分包路径。详见 [小游戏独立分包指南](../../guide/base-ability/independent-sub-packages.html) | [2.12.2](../../guide/runtime/client-lib/compatibility.html) |

---

### boolean wx.setMessageToFriendQuery(Object object)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.setMessageToFriendQuery.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| shareMessageToFriendScene | number |  | 是 | 需要传递的代表场景的数字，需要在 0 - 50 之间 |
| query | string |  | 是 | 需要传递的字符串数据，长度需要在 128 之内 |

---

### Boolean wx.setHandoffQuery(String query)

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.setHandoffQuery.html

---

### wx.onShareTimeline(function listener)

基础库 2.11.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.onShareTimeline.html

**function listener**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| title | string | 转发标题，不传则默认使用当前小游戏的昵称。 |  |
| imageUrl | string | 转发显示图片的链接，可以是网络图片路径或本地图片文件路径或相对代码包根目录的图片文件路径。（该图片用于分享到朋友圈的卡片以及从朋友圈转发到会话消息的卡片展示） |  |
| imageUrlId | string | 审核通过的图片编号，详见 [使用审核通过的转发图片](../../guide/open-ability/share/share.html#%E4%BD%BF%E7%94%A8%E5%AE%A1%E6%A0%B8%E9%80%9A%E8%BF%87%E7%9A%84%E8%BD%AC%E5%8F%91%E5%9B%BE%E7%89%87) |  |
| imagePreviewUrl | string | 朋友圈预览图链接，不传则默认使用当前游戏画面截图 | [2.14.3](../../guide/runtime/client-lib/compatibility.html) |
| imagePreviewUrlId | string | 审核通过的朋友圈预览图图片编号，详见 [使用审核通过的转发图片](../../guide/open-ability/share/share.html#%E4%BD%BF%E7%94%A8%E5%AE%A1%E6%A0%B8%E9%80%9A%E8%BF%87%E7%9A%84%E8%BD%AC%E5%8F%91%E5%9B%BE%E7%89%87) | [2.14.3](../../guide/runtime/client-lib/compatibility.html) |
| query | string | 查询字符串，必须是 key1=val1&key2=val2 的格式。从这条转发消息进入后，可通过 wx.getLaunchOptionsSync() 或 wx.onShow() 获取启动参数中的 query。不传则默认使用当前页面query。 |  |
| path | string | 独立分包路径。详见 [小游戏独立分包指南](../../guide/base-ability/independent-sub-packages.html) | [2.12.2](../../guide/runtime/client-lib/compatibility.html) |

---

### wx.onShareMessageToFriend(function listener)

基础库 2.9.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.onShareMessageToFriend.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| success | boolean | 是否成功 |
| errMsg | string | 错误信息 |

---

### wx.onShareAppMessage(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.onShareAppMessage.html

**function listener**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| title | string | 转发标题，不传则默认使用当前小游戏的昵称。 |  |
| imageUrl | string | 转发显示图片的链接，可以是网络图片路径或本地图片文件路径或相对代码包根目录的图片文件路径。显示图片长宽比是 5:4 |  |
| query | string | 查询字符串，必须是 key1=val1&key2=val2 的格式。从这条转发消息进入后，可通过 wx.getLaunchOptionsSync() 或 wx.onShow() 获取启动参数中的 query。 |  |
| imageUrlId | string | 审核通过的图片编号，详见 [使用审核通过的转发图片](../../guide/open-ability/share/share.html#%E4%BD%BF%E7%94%A8%E5%AE%A1%E6%A0%B8%E9%80%9A%E8%BF%87%E7%9A%84%E8%BD%AC%E5%8F%91%E5%9B%BE%E7%89%87) | [2.4.3](../../guide/runtime/client-lib/compatibility.html) |
| promise | promise | 如果该参数存在，则其它的参数将会以 resolve 结果为准，如果三秒内不 resolve，分享会使用上面传入的默认参数 | [2.12.0](../../guide/runtime/client-lib/compatibility.html) |
| toCurrentGroup | boolean | 是否转发到当前群。该参数只对从群工具栏打开的场景下生效，默认转发到当前群，填入false时可转发到其他会话。 | [2.12.2](../../guide/runtime/client-lib/compatibility.html) |
| path | string | 独立分包路径。详见 [小游戏独立分包指南](../../guide/base-ability/independent-sub-packages.html) | [2.12.2](../../guide/runtime/client-lib/compatibility.html) |

---

### wx.onHandoff(function listener)

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.onHandoff.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| query | string | 需要传递给接力客户端的 query |

---

### wx.onCopyUrl(function listener)

基础库 2.14.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.onCopyUrl.html

**function listener**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| query | string | 用短链打开小程序时当前页面携带的查询字符串，默认为空字符串。小程序中使用时，应在进入页面时调用 `wx.onCopyUrl` 自定义 `query`，退出页面时调用 `wx.offCopyUrl`，防止影响其它页面。 |  |
| title | string | 短链中的自定义标题，显示在小程序名称之后。在基础库3.15.1之前，默认是 navigationBarTitleText 的值，在基础库3.15.1及之后，默认为空字符串。 | [3.15.1](../../guide/runtime/client-lib/compatibility.html) |
| promise | Object | 如果该参数存在且为有效的 Promise，则最终的 `query` 和 `title` 将以该 Promise 的 resolve 结果为准；如果 Promise 在 2 秒内未 resolve 或 reject，则回退使用同步传入的默认参数。 | [3.16.0](../../guide/runtime/client-lib/compatibility.html) |

---

### wx.onAddToFavorites(function listener)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.onAddToFavorites.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| title | string | 收藏标题，不传则默认使用当前小游戏的昵称。 |
| query | string | 查询字符串，必须是 key1=val1&key2=val2 的格式。从收藏进入后，可通过 wx.getLaunchOptionsSync() 或 wx.onShow() 获取启动参数中的 query。 |
| imageUrl | string | 转发显示图片的链接，可以是网络图片路径或本地图片文件路径或相对代码包根目录的图片文件路径。显示图片长宽比是 5:4 |
| disableForward | boolean | 禁止收藏后长按转发，默认 false |

---

### wx.offShareTimeline(function listener)

基础库 2.11.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.offShareTimeline.html

---

### wx.offShareMessageToFriend(function listener)

基础库 2.9.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.offShareMessageToFriend.html

---

### wx.offShareAppMessage(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.offShareAppMessage.html

---

### wx.offHandoff()

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.offHandoff.html

---

### wx.offCopyUrl()

基础库 2.14.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.offCopyUrl.html

---

### wx.offAddToFavorites()

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.offAddToFavorites.html

---

### wx.hideShareMenu(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.hideShareMenu.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| menus | Array.<string> |  | 否 | 本接口为 Beta 版本，暂只在 Android 平台支持。需要隐藏的转发按钮名称列表，默认['shareAppMessage', 'shareTimeline']。按钮名称合法值包含 "shareAppMessage"、"shareTimeline" 两种 | [2.11.3](../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### wx.getShareInfo(Object object)

从基础库2.17.3开始，本接口停止维护，请使用wx.getGroupEnterInfo代替

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.getShareInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| shareTicket | string |  | 是 | shareTicket，详见[获取更多转发信息](../../guide/open-ability/share/share.html#获取更多转发信息) |  |
| timeout | number |  | 否 | 超时时间，单位 ms | [1.9.90](../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| errMsg | string | 错误信息 |  |
| encryptedData | string | 包括敏感数据在内的完整转发信息的加密数据，详细见[加密数据解密算法](../../guide/open-ability/signature.html) |  |
| iv | string | 加密算法的初始向量，详细见[加密数据解密算法](../../guide/open-ability/signature.html) |  |
| cloudID | string | 敏感数据对应的云 ID，开通[云开发](../../wxcloud/basis/getting-started.html)的小程序才会返回，可通过云调用直接获取开放数据，详细见[云调用直接获取开放数据](../../guide/open-ability/signature.html#method-cloud) | [2.7.0](../../guide/runtime/client-lib/compatibility.html) |

---

### wx.checkHandoffEnabled(Object object)

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.checkHandoffEnabled.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| isEnabled | boolean | 是否可以进行接力 |
| errCode | number | 错误码，0未知，1用户取消，2电脑未登录，3电脑版本过低，4暂未支持 |

---

### wx.authPrivateMessage(Object object)

基础库 2.13.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/share/wx.authPrivateMessage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| shareTicket | string |  | 是 | shareTicket。可以从 wx.getEnterOptionsSync 中获取。详情 [shareTicket](../../guide/open-ability/share/share.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |
| valid | boolean | 验证是否通过 |
| encryptedData | string | 经过加密的activityId，解密后可得到原始的activityId。若解密后得到的activityId可以与开发者后台的活动id对应上则验证通过，否则表明valid字段不可靠（被篡改） 详细见[加密数据解密算法](../../guide/open-ability/signature.html) |
| iv | string | 加密算法的初始向量，详细见[加密数据解密算法](../../guide/open-ability/signature.html) |

---

<!-- pages: 23 -->
