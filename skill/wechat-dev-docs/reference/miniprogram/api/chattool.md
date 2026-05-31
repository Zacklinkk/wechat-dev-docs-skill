# 微信小程序 API 结构化参考 — chattool

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.shareVideoToGroup(Object object)

基础库 3.7.8 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.shareVideoToGroup.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| videoPath | string |  | 是 | 要分享的视频地址，必须为本地路径或临时路径 |
| thumbPath | string |  | 否 | 缩略图路径，若留空则使用视频首帧 |
| needShowEntrance | boolean | true | 否 | 分享的图片消息是否要带小程序入口 |
| entrancePath | string | '' | 否 | 从消息小程序入口打开小程序的路径，默认为聊天工具启动路径 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.shareImageToGroup(Object object)

基础库 3.7.8 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.shareImageToGroup.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| imagePath | string |  | 是 | 要分享的图片地址，必须为本地路径或临时路径 |
| needShowEntrance | boolean | true | 否 | 分享的图片消息是否要带小程序入口 |
| entrancePath | string | '' | 否 | 从消息小程序入口打开小程序的路径，默认为聊天工具启动路径 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.shareFileToGroup(Object object)

基础库 3.7.8 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.shareFileToGroup.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| filePath | string |  | 是 | 要分享的文件地址，必须为本地路径或临时路径 |
| fileName | string |  | 否 | 自定义文件名，若留空则使用filePath中的文件名 |
| needShowEntrance | boolean | true | 否 | 分享的图片消息是否要带小程序入口 |
| entrancePath | string | '' | 否 | 从消息小程序入口打开小程序的路径，默认为聊天工具启动路径 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.shareEmojiToGroup(Object object)

基础库 3.7.8 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.shareEmojiToGroup.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| imagePath | string |  | 是 | 要分享的表情地址，必须为本地路径或临时路径 |
| needShowEntrance | boolean | true | 否 | 分享的表情消息是否要带小程序入口 |
| entrancePath | string | '' | 否 | 从消息小程序入口打开小程序的路径，默认为聊天工具启动路径 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.shareAppMessageToGroup(Object object)

基础库 3.7.8 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.shareAppMessageToGroup.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| title | string |  | 是 | 转发标题 |
| path | string | '' | 否 | 转发路径，必须是以 / 开头的完整路径，默认为当前页面 |
| imageUrl | string | '' | 否 | 自定义图片路径，支持PNG及JPG，显示图片长宽比是 5:4，默认使用截图 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.selectGroupMembers(Object object)

基础库 3.7.8 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.selectGroupMembers.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| maxSelectCount | number |  | 否 | 最多可选人数 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| members | Array.<string> | 所选用户在此聊天室下的唯一标识，同一个用户在不同的聊天室下id不同 |

---

### wx.openChatTool(Object object)

基础库 3.7.8 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.openChatTool.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | url | string |  | 是 | 聊天工具分包内的页面路径 |
|  | roomid | string |  | 否 | 聊天室 id，不传则拉起群选择框，可以传入多聊群的 opengid 值，或者单聊群的 open\_single\_roomid 值 |
|  | chatType | number |  | 否 | 群聊类型 |
|  | | 合法值 | 说明 | | --- | --- | | 1 | 微信联系人单聊 | | 2 | 企业微信联系人单聊 | | 3 | 普通微信群聊 | | 4 | 企业微信互通群聊 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 1 | 微信联系人单聊 |
| 2 | 企业微信联系人单聊 |
| 3 | 普通微信群聊 |
| 4 | 企业微信互通群聊 |

---

### wx.notifyGroupMembers(Object object)

基础库 3.7.8 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.notifyGroupMembers.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | title | string |  | 是 | 文字链标题，发送的内容将由微信拼接为：@的成员列表+“请完成：”/"请参与："+打开小程序的文字链，如「@alex @cindy 请完成：团建报名统计」。 |
|  | members | Array.<string> |  | 是 | 需要提醒的用户 group\_openid 列表 |
|  | entrancePath | string |  | 是 | 文字链跳转路径 |
|  | type | string | complete | 否 | 展示的动词 |
|  | | 合法值 | 说明 | | --- | --- | | participate | 请参与 | | complete | 请完成 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| participate | 请参与 |
| complete | 请完成 |

---

### wx.getChatToolInfo(Object object)

基础库 3.7.8 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.getChatToolInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |
| encryptedData | string | 包括敏感数据在内的完整转发信息的加密数据，详细见[加密数据解密算法](../../framework/open-ability/signature.html) |
| iv | string | 加密算法的初始向量，详细见[加密数据解密算法](../../framework/open-ability/signature.html) |
| cloudID | string | 敏感数据对应的云 ID，开通[云开发](../../wxcloudservice/wxcloud/basis/getting-started.html)的小程序才会返回，可通过云调用直接获取开放数据，详细见[云调用直接获取开放数据](../../framework/open-ability/signature.html#method-cloud) |

---

### wx.enterChatToolMode(Object object)

基础库 3.12.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.enterChatToolMode.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| chatToolRooms | Array.<string> |  | 否 | 聊天室 id，不传则拉起群选择框，可以传入多聊群的 opengid 值 |
| singleChatRoom | boolean |  | 否 | 是否单选群聊，true 为单选，false 为多选 |
| selectLimit | number |  | 否 | 多选模式下最多选择的群聊数量 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

<!-- pages: 10 -->
