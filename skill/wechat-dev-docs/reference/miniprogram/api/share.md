# 微信小程序 API 结构化参考 — share

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.updateShareMenu(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.updateShareMenu.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | withShareTicket | boolean | false | 否 | 是否使用带 shareTicket 的转发[详情](../../framework/open-ability/share.html) |  |
|  | isUpdatableMessage | boolean | false | 否 | 是否是动态消息，详见[动态消息](../../framework/open-ability/share/updatable-message.html) | [2.4.0](../../framework/compatibility.html) |
|  | activityId | string |  | 否 | 动态消息的 activityId。通过 [updatableMessage.createActivityId](errorupdatableMessage.createActivityId)) 接口获取 | [2.4.0](../../framework/compatibility.html) |
|  | toDoActivityId | string |  | 否 | 群待办消息的id，通过toDoActivityId可以把多个群待办消息聚合为同一个。通过 [updatableMessage.createActivityId](errorupdatableMessage.createActivityId)) 接口获取。详见[群待办消息](../../framework/open-ability/share.html) | [2.11.0](../../framework/compatibility.html) |
|  | templateInfo | Object |  | 否 | 动态消息的模板信息 | [2.4.0](../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | parameterList | Array.<Object> |  | 是 | 参数列表 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | name | string |  | 是 | 参数名 | |  | value | string |  | 是 | 参数值 | | | | | | |  | templateId | string |  | 是 | 模板ID | | | | | | |
|  | isPrivateMessage | boolean |  | 否 | 是否是私密消息。详见 [小程序私密消息](../../framework/open-ability/share/private-message.html) | [2.13.0](../../framework/compatibility.html) |
|  | participant | Array.<string> | [] | 否 | 参与用户此聊天室下的 group\_openid 列表 |  |
|  | useForChatTool | boolean | false | 否 | 聊天工具模式特殊动态消息 | [3.7.8](../../framework/compatibility.html) |
|  | chooseType | number | 1 | 否 | 指定成员的方式 | [3.7.8](../../framework/compatibility.html) |
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

### wx.showShareMenu(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.showShareMenu.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| withShareTicket | boolean | false | 否 | 是否使用带 shareTicket 的转发[详情](../../framework/open-ability/share.html) |  |
| menus | Array.<string> |  | 否 | 本接口为 Beta 版本，暂只在 Android 平台支持。需要显示的转发按钮名称列表，默认['shareAppMessage']。按钮名称合法值包含 "shareAppMessage"、"shareTimeline" 两种 | [2.11.3](../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### wx.showShareImageMenu(Object object)

基础库 2.14.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.showShareImageMenu.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| path | string |  | 是 | 要分享的图片地址，必须为本地路径或临时路径 |  |
| needShowEntrance | boolean | true | 否 | 分享的图片消息是否要带小程序入口 | [3.2.0](../../framework/compatibility.html) |
| entrancePath | string | '' | 否 | 发送给朋友时，小程序入口打开小程序的路径，如果当前页面允许分享给朋友，则默认为当前页面路径，否则默认为小程序首页 | [3.2.0](../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### wx.shareVideoMessage(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.shareVideoMessage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| videoPath | string |  | 是 | 要分享的视频地址，必须为本地路径或临时路径 |
| thumbPath | string |  | 否 | 缩略图路径，若留空则使用视频首帧 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.shareToOfficialAccount(Object object)

基础库 3.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.shareToOfficialAccount.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| title | string |  | 是 | 贴图的标题 |  |
| content | string |  | 否 | 贴图的正文 |  |
| tags | Array.<string> |  | 否 | 贴图的标签，上限10个 |  |
| images | Array.<string> |  | 否 | 贴图的图片，必须为本地路径或临时路径 |  |
| path | string |  | 否 | 开发者自定义小程序路径 |  |
| recommendLink | string |  | 否 | 贴图链接卡片字段，暂时只支持小程序短链 | [3.16.0](../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| status | string | 贴图发表状态 |
| postUrl | string | 贴图发表后的文章链接，仅在success回调中返回，并且只有在发表成功后链接才可访问 |

---

### wx.shareFileMessage(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.shareFileMessage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| filePath | string |  | 是 | 要分享的文件地址，必须为本地路径或临时路径 |
| fileName | string |  | 否 | 自定义文件名，若留空则使用filePath中的文件名 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.onCopyUrl(function listener)

基础库 2.14.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.onCopyUrl.html

**function listener**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| query | string | 用短链打开小程序时当前页面携带的查询字符串，默认为空字符串。小程序中使用时，应在进入页面时调用 `wx.onCopyUrl` 自定义 `query`，退出页面时调用 `wx.offCopyUrl`，防止影响其它页面。 |  |
| title | string | 短链中的自定义标题，显示在小程序名称之后。在基础库3.15.1之前，默认是 navigationBarTitleText 的值，在基础库3.15.1及之后，默认为空字符串。 | [3.15.1](../../framework/compatibility.html) |
| promise | Object | 如果该参数存在且为有效的 Promise，则最终的 `query` 和 `title` 将以该 Promise 的 resolve 结果为准；如果 Promise 在 2 秒内未 resolve 或 reject，则回退使用同步传入的默认参数。 | [3.16.0](../../framework/compatibility.html) |

---

### wx.offCopyUrl()

基础库 2.14.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.offCopyUrl.html

---

### wx.hideShareMenu(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.hideShareMenu.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| menus | Array.<string> |  | 否 | 本接口为 Beta 版本，暂只在 Android 平台支持。需要隐藏的转发按钮名称列表，默认['shareAppMessage', 'shareTimeline']。按钮名称合法值包含 "shareAppMessage"、"shareTimeline" 两种 | [2.11.3](../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### wx.getShareInfo(Object object)

从基础库2.17.3开始，本接口停止维护，请使用wx.getGroupEnterInfo代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.getShareInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| shareTicket | string |  | 是 | shareTicket，详见[获取更多转发信息](../../framework/open-ability/share.html#获取更多转发信息) |  |
| timeout | number |  | 否 | 超时时间，单位 ms | [1.9.90](../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| errMsg | string | 错误信息 |  |
| encryptedData | string | 包括敏感数据在内的完整转发信息的加密数据，详细见[加密数据解密算法](../../framework/open-ability/signature.html) |  |
| iv | string | 加密算法的初始向量，详细见[加密数据解密算法](../../framework/open-ability/signature.html) |  |
| cloudID | string | 敏感数据对应的云 ID，开通[云开发](../../wxcloudservice/wxcloud/basis/getting-started.html)的小程序才会返回，可通过云调用直接获取开放数据，详细见[云调用直接获取开放数据](../../framework/open-ability/signature.html#method-cloud) | [2.7.0](../../framework/compatibility.html) |

---

### wx.authPrivateMessage(Object object)

基础库 2.13.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.authPrivateMessage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| shareTicket | string |  | 是 | shareTicket。可以从 wx.getEnterOptionsSync 中获取。详情 [shareTicket](../../framework/open-ability/share.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |
| valid | boolean | 验证是否通过 |
| encryptedData | string | 经过加密的activityId，解密后可得到原始的activityId。若解密后得到的activityId可以与开发者后台的活动id对应上则验证通过，否则表明valid字段不可靠（被篡改） 详细见[加密数据解密算法](../../framework/open-ability/signature.html) |
| iv | string | 加密算法的初始向量，详细见[加密数据解密算法](../../framework/open-ability/signature.html) |

---

<!-- pages: 11 -->
