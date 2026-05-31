# 微信小游戏 API 结构化参考 — open-api

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.getUserInfo(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/user-info/wx.getUserInfo.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | withCredentials | boolean |  | 否 | 是否带上登录态信息。当 withCredentials 为 true 时，要求此前有调用过 wx.login 且登录态尚未过期，此时返回的数据会包含 encryptedData, iv 等敏感信息；当 withCredentials 为 false 时，不要求有登录态，返回的数据不包含 encryptedData, iv 等敏感信息。 |
|  | lang | string | en | 否 | 显示用户信息的语言 |
|  | | 合法值 | 说明 | | --- | --- | | en | 英文 | | zh\_CN | 简体中文 | | zh\_TW | 繁体中文 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| en | 英文 |
| zh\_CN | 简体中文 |
| zh\_TW | 繁体中文 |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| userInfo | [UserInfo](UserInfo.html) | 用户信息对象，不包含 openid 等敏感信息 |  |
| rawData | string | 不包括敏感信息的原始数据字符串，用于计算签名 |  |
| signature | string | 使用 sha1( rawData + sessionkey ) 得到字符串，用于校验用户信息，详见 [用户数据的签名验证和加解密](../../../guide/open-ability/signature.html) |  |
| encryptedData | string | 包括敏感数据在内的完整用户信息的加密数据，详见 [用户数据的签名验证和加解密](../../../guide/open-ability/signature.html#加密数据解密算法) |  |
| iv | string | 加密算法的初始向量，详见 [用户数据的签名验证和加解密](../../../guide/open-ability/signature.html#加密数据解密算法) |  |
| cloudID | string | 敏感数据对应的云 ID，开通[云开发](../../../wxcloud/basis/getting-started.html)的小程序才会返回，可通过云调用直接获取开放数据，详细见[云调用直接获取开放数据](../../../guide/open-ability/signature.html#method-cloud) | [2.7.0](../../../guide/runtime/client-lib/compatibility.html) |

---

### wx.getPhoneNumber(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/user-info/wx.getPhoneNumber.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| isRealtime | boolean | false | 否 | 手机号实时验证，向用户申请，并在用户同意后，快速填写和实时验证手机号 [具体说明](https://developers.weixin.qq.com/minigame/dev/guide/open-ability/getRealtimePhoneNumber.html)。 |
| phoneNumberNoQuotaToast | boolean | true | 否 | 当手机号快速验证或手机号实时验证额度用尽时，是否对用户展示“申请获取你的手机号，但该功能使用次数已达当前小程序上限，暂时无法使用”的提示，默认展示。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| code | string | 动态令牌 |
| errMsg | string | 回调信息（成功失败都会返回） |
| errno | number | 错误码（失败时返回） |

---

### UserInfoButton wx.createUserInfoButton(Object object)

基础库 2.0.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/user-info/wx.createUserInfoButton.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | type | string |  | 是 | 按钮的类型。 |
|  | | 合法值 | 说明 | | --- | --- | | text | 可以设置背景色和文本的按钮 | | image | 只能设置背景贴图的按钮，背景贴图会直接拉伸到按钮的宽高 | | | | | |
|  | text | string |  | 否 | 按钮上的文本，仅当 type 为 `text` 时有效 |
|  | image | string |  | 否 | 按钮的背景图片，仅当 type 为 `image` 时有效 |
|  | style | Object |  | 是 | 按钮的样式 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | left | number |  | 是 | 左上角横坐标 | |  | top | number |  | 是 | 左上角纵坐标 | |  | width | number |  | 是 | 宽度 | |  | height | number |  | 是 | 高度 | |  | backgroundColor | string |  | 是 | 背景颜色 | |  | borderColor | string |  | 否 | 边框颜色 | |  | borderWidth | number |  | 否 | 边框宽度 | |  | borderRadius | number |  | 否 | 边框圆角 | |  | color | string |  | 否 | 文本的颜色。格式为 6 位 16 进制数。 | |  | textAlign | string |  | 否 | 文本的水平居中方式 | |  | | 合法值 | 说明 | | --- | --- | | left | 居左 | | center | 居中 | | right | 居右 | | | | | | |  | fontSize | number |  | 否 | 字号 | |  | lineHeight | number |  | 否 | 文本的行高 | | | | | |
|  | withCredentials | boolean | true | 否 | 是否带上登录态信息。当 withCredentials 为 true 时，要求此前有调用过 wx.login 且登录态尚未过期，此时返回的数据会包含 encryptedData, iv 等敏感信息；当 withCredentials 为 false 时，不要求有登录态，返回的数据不包含 encryptedData, iv 等敏感信息。 |
|  | lang | string | en | 否 | 描述用户信息的语言 |
|  | | 合法值 | 说明 | | --- | --- | | en | 英文 | | zh\_CN | 简体中文 | | zh\_TW | 繁体中文 | | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| text | 可以设置背景色和文本的按钮 |
| image | 只能设置背景贴图的按钮，背景贴图会直接拉伸到按钮的宽高 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | left | number |  | 是 | 左上角横坐标 |
|  | top | number |  | 是 | 左上角纵坐标 |
|  | width | number |  | 是 | 宽度 |
|  | height | number |  | 是 | 高度 |
|  | backgroundColor | string |  | 是 | 背景颜色 |
|  | borderColor | string |  | 否 | 边框颜色 |
|  | borderWidth | number |  | 否 | 边框宽度 |
|  | borderRadius | number |  | 否 | 边框圆角 |
|  | color | string |  | 否 | 文本的颜色。格式为 6 位 16 进制数。 |
|  | textAlign | string |  | 否 | 文本的水平居中方式 |
|  | | 合法值 | 说明 | | --- | --- | | left | 居左 | | center | 居中 | | right | 居右 | | | | | |
|  | fontSize | number |  | 否 | 字号 |
|  | lineHeight | number |  | 否 | 文本的行高 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| left | 居左 |
| center | 居中 |
| right | 居右 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| en | 英文 |
| zh\_CN | 简体中文 |
| zh\_TW | 繁体中文 |

---

### UserInfo

用户头像昵称获取规则已调整，参考用户信息接口调整说明、小程序用户头像昵称获取规则调整公告

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/user-info/UserInfo.html

**number gender**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 0 | 未知 |  |
| 1 | 男性 |  |
| 2 | 女性 |  |

**string language**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| en | 英文 |  |
| zh\_CN | 简体中文 |  |
| zh\_TW | 繁体中文 |  |

---

### UserInfoButton

用户信息按钮

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/user-info/UserInfoButton.html

**string type**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| text | 可以设置背景色和文本的按钮 |  |
| image | 只能设置背景贴图的按钮，背景贴图会直接拉伸到按钮的宽高 |  |

**Object style**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | left | number | 左上角横坐标 |
|  | top | number | 左上角纵坐标 |
|  | width | number | 宽度 |
|  | height | number | 高度 |
|  | backgroundColor | string | 背景颜色 |
|  | borderColor | string | 边框颜色 |
|  | borderWidth | number | 边框宽度 |
|  | borderRadius | number | 边框圆角 |
|  | color | string | 文本的颜色。格式为 6 位 16 进制数。 |
|  | textAlign | string | 文本的水平居中方式 |
|  | | 合法值 | 说明 | | --- | --- | | left | 居左 | | center | 居中 | | right | 居右 | | | |
|  | fontSize | number | 字号 |
|  | lineHeight | number | 文本的行高 |

**Object style**

| 合法值 | 说明 |
| --- | --- |
| left | 居左 |
| center | 居中 |
| right | 居右 |

---

### UserInfoButton.destroy()

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/user-info/UserInfoButton.destroy.html

---

### UserInfoButton.hide()

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/user-info/UserInfoButton.hide.html

---

### UserInfoButton.offTap(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/user-info/UserInfoButton.offTap.html

---

### UserInfoButton.onTap(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/user-info/UserInfoButton.onTap.html

**function listener**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| userInfo | [UserInfo](UserInfo.html) | 用户信息对象，不包含 openid 等敏感信息 |  |
| rawData | string | 不包括敏感信息的原始数据字符串，用于计算签名 |  |
| signature | string | 使用 sha1( rawData + sessionkey ) 得到字符串，用于校验用户信息，参考文档[signature](../../../guide/open-ability/signature.html) |  |
| encryptedData | string | 包括敏感数据在内的完整用户信息的加密数据，详细见[加密数据解密算法](../../../guide/open-ability/signature.html) |  |
| iv | string | 加密算法的初始向量，详细见[加密数据解密算法](../../../guide/open-ability/signature.html) |  |
| cloudID | string | 敏感数据对应的云 ID，开通[云开发](./../../wxcloud/basis/getting-started.html)的小程序才会返回，可通过云调用直接获取开放数据，详细见[云调用直接获取开放数据](../../../guide/open-ability/signature.html#method-cloud) | [2.7.0](../../../guide/runtime/client-lib/compatibility.html) |
| errMsg | string | 调用结果（错误原因） |  |

---

### UserInfoButton.show()

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/user-info/UserInfoButton.show.html

---

### wx.login(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/login/wx.login.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| timeout | number |  | 否 | 超时时间，单位ms | [1.9.90](../../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| code | string | 用户登录凭证（有效期五分钟）。开发者需要在开发者服务器后台调用 [code2Session](https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/user-login/code2Session.html)，使用 code 换取 openid、unionid、session\_key 等信息 |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| errMsg | String | 错误信息 |  |
| errno | Number | errno 错误码，错误码的详细说明参考 [Errno错误码](../../../guide/runtime/debug/PublicErrno.html) | [2.24.0](../../../guide/runtime/client-lib/compatibility.html) |

---

### wx.checkSession(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/login/wx.checkSession.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.authorize(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/authorize/wx.authorize.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| scope | string |  | 是 | 需要获取权限的 scope，详见 [scope 列表](../../../guide/base-ability/authorize.html#scope-%E5%88%97%E8%A1%A8) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.shareMessageToFriend(Object object)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/wx.shareMessageToFriend.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| openId | string |  | 是 | 发送对象的 openId |
| title | string |  | 否 | 转发标题，不传则默认使用当前小游戏的昵称。 |
| imageUrl | string |  | 否 | 转发显示图片的链接，可使用本地图片文件路径或相对代码包根目录的图片文件路径，不可使用网络图片。如需使用网络图片，可先在游戏域调用 wx.downloadFile 下载到本地后，调用 OpenDataContext.postMessage 发送本地图片路径到开放数据域使用。显示图片长宽比是 5:4 |
| imageUrlId | string |  | 否 | 审核通过的图片编号，详见 [使用审核通过的转发图片](../../../guide/open-ability/share/share.html#%E4%BD%BF%E7%94%A8%E5%AE%A1%E6%A0%B8%E9%80%9A%E8%BF%87%E7%9A%84%E8%BD%AC%E5%8F%91%E5%9B%BE%E7%89%87) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.setUserCloudStorage(Object object)

基础库 1.9.92 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/wx.setUserCloudStorage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| KVDataList | Array.<[KVData](KVData.html)> |  | 是 | 要修改的 KV 数据列表 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.sendGiftToFriend(Object object)

基础库 3.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/wx.sendGiftToFriend.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| giftId | string |  | 是 | 礼包 id |
| openid | string |  | 是 | 好友的 openid |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | errMsg | string | 错误信息 |
|  | errno | number | 错误码 |
|  | | 合法值 | 说明 | | --- | --- | | 151066169 | 注册天数不足 首次注册时间必须大于 24 小时才能赠礼 | | 151066170 | 风险用户 | | 151066168 | 当前时间周期已经赠送，目前支持一天赠送一次 | | 151066172 | 非好友关系 | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 151066169 | 注册天数不足 首次注册时间必须大于 24 小时才能赠礼 |
| 151066170 | 风险用户 |
| 151066168 | 当前时间周期已经赠送，目前支持一天赠送一次 |
| 151066172 | 非好友关系 |

---

### wx.removeUserCloudStorage(Object object)

基础库 1.9.92 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/wx.removeUserCloudStorage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyList | Array.<string> |  | 是 | 要删除掉 key 列表 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.onInteractiveStorageModified(function callback)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/wx.onInteractiveStorageModified.html

---

### wx.offInteractiveStorageModified(function callback)

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/wx.offInteractiveStorageModified.html

---

### wx.modifyFriendInteractiveStorage(Object object)

基础库 2.7.7 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/wx.modifyFriendInteractiveStorage.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | key | string |  | 是 | 需要修改的数据的 key，目前可以为 '1' - '50' |  |
|  | opNum | number |  | 是 | 需要修改的数值，目前只能为 1 |  |
|  | operation | string |  | 是 | 修改类型 |  |
|  | | 合法值 | 说明 | | --- | --- | | add | 加 | | | | | | |
|  | toUser | string |  | 否 | 目标好友的 openId |  |
|  | title | string |  | 否 | 分享标题，如果设置了这个值，则在交互成功后自动询问用户是否分享给好友（需要配置模板规则） | [2.9.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | imageUrl | string |  | 否 | 分享图片地址，详见 wx.shareMessageToFriend 同名参数（需要配置模板规则） | [2.9.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | imageUrlId | string |  | 否 | 分享图片编号，详见 wx.shareMessageToFriend 同名参数（需要配置模板规则） | [2.9.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | quiet | boolean | false | 否 | 是否静默修改（不弹框）。当进入场景是好友 [定向分享](wx.shareMessageToFriend.html) 的卡片时有效，代表分享反馈操作，此时 `toUser` 默认为原分享者的 openId | [2.9.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| add | 加 |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | errMsg | string | 错误信息 |
|  | errCode | number | 错误码 |
|  | | 合法值 | 说明 | | --- | --- | | -17006 | 非好友关系 | | -17007 | 非法的 toUser openId | | -17008 | 非法的 key | | -17009 | 非法的 operation | | -17010 | 非法的操作数 | | -17011 | JSServer 校验写操作失败 | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| -17006 | 非好友关系 |
| -17007 | 非法的 toUser openId |
| -17008 | 非法的 key |
| -17009 | 非法的 operation |
| -17010 | 非法的操作数 |
| -17011 | JSServer 校验写操作失败 |

---

### wx.getUserInteractiveStorage(Object object)

基础库 2.7.7 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/wx.getUserInteractiveStorage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyList | Array.<string> |  | 是 | 要获取的 key 列表 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| iv | string | 加密算法的初始向量，详见 [用户数据的签名验证和加解密](../../../guide/open-ability/signature.html#加密数据解密算法) |
| encryptedData | string | 加密数据，包含互动型托管数据的值。解密后的结果为一个 `KVDataList`，每一项为一个 `KVData`。 [用户数据的签名验证和加解密](../../../guide/open-ability/signature.html#加密数据解密算法) |
| cloudID | string | 敏感数据对应的云 ID，开通[云开发](../../../wxcloud/basis/getting-started.html)的小程序才会返回，可通过云调用直接获取开放数据，详细见[云调用直接获取开放数据](../../../guide/open-ability/signature.html#method-cloud) |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | errMsg | string | 错误信息 |
|  | errCode | number | 错误码 |
|  | | 合法值 | 说明 | | --- | --- | | -17008 | 非法的 key | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| -17008 | 非法的 key |

---

### wx.getUserCloudStorageKeys(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/wx.getUserCloudStorageKeys.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| keys | Array.<String> | 用户托管数据当中所有的 key 数组 |

---

### wx.getUserCloudStorage(Object object)

基础库 1.9.92 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/wx.getUserCloudStorage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyList | Array.<string> |  | 是 | 要获取的 key 列表 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| KVDataList | Array.<[KVData](KVData.html)> | 用户托管的 KV 数据列表 |

---

### Canvas wx.getSharedCanvas()

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/wx.getSharedCanvas.html

---

### wx.getRelationFriendList(Object object)

基础库 3.16.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/wx.getRelationFriendList.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| signature | string | 使用 sha1( rawData + sessionkey ) 得到字符串，用于校验用户信息 |
| encryptedData | string | 包括 RelationFriendData 在内的加密数据，详见[加密数据解密算法](../../../guide/open-ability/signature.html) |
| iv | string | 加密算法的初始向量 |
| cloudID | string | 敏感数据对应的云 ID，开通云开发的小程序才会返回，可通过[云调用直接获取开放数据](../../../guide/open-ability/signature.html) |

**encryptedData 解密后得到的 RelationFriendData 的结构**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| list | Array<RelationFriendInfo> | 同玩互动好友列表 |

**RelationFriendInfo 的结构**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| openid | string | 好友的openid |

---

### wx.getPotentialFriendList(Object object)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/wx.getPotentialFriendList.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| list | Array.<[FriendInfo](FriendInfo.html)> | 可能对游戏感兴趣的未注册好友名单 |

---

### wx.getGroupMembersInfo(Object object)

基础库 3.7.12 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/wx.getGroupMembersInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| members | Array.<string> |  | 是 | 需要获取的群用户的 groupOpenId 列表 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | membersInfo | Array.<Object> | 所选用户的头像昵称列表 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | avatarUrl | string | 用户头像图片 url | |  | city | string | 用户所在城市 | |  | country | string | 用户所在国家 | |  | gender | number | 用户性别 | |  | language | string | 显示 country province city 所用的语言 | |  | nickName | string | 用户昵称 | |  | openId | string | 用户 openId | |  | province | string | 用户所在省份 | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | avatarUrl | string | 用户头像图片 url |
|  | city | string | 用户所在城市 |
|  | country | string | 用户所在国家 |
|  | gender | number | 用户性别 |
|  | language | string | 显示 country province city 所用的语言 |
|  | nickName | string | 用户昵称 |
|  | openId | string | 用户 openId |
|  | province | string | 用户所在省份 |

---

### wx.getGroupInfo(Object object)

基础库 2.10.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/wx.getGroupInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| openGId | string |  | 是 | 群 openGId，可通过 `wx.getGroupEnterInfo` 或 `wx.getShareInfo` 获取 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| name | string | 群名称 |

---

### wx.getGroupCloudStorage(Object object)

基础库 1.9.92 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/wx.getGroupCloudStorage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| shareTicket | string |  | 否 | 群分享对应的 shareTicket。shareTicket 与 groupid 只需要传其中一个，建议使用 groupid |  |
| groupid | string |  | 否 | 对应群的 opengid。可通过主域中的 wx.getGroupEnterInfo 接口获取。shareTicket 与 groupid 只需要传其中一个，建议使用 groupid | [3.8.8](../../../guide/runtime/client-lib/compatibility.html) |
| keyList | Array.<string> |  | 是 | 要拉取的 key 列表 |  |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | Array.<[UserGameData](UserGameData.html)> | 群同玩成员的托管数据 |

---

### wx.getFriendSendGiftStatus(Object object)

基础库 3.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/wx.getFriendSendGiftStatus.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| giftId | string |  | 是 | 礼包 id |
| openidList | Array.<string> |  | 是 | 要查询的 openid 列表 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | Array.<[FriendSendGiftStatus](FriendSendGiftStatus.html)> | 好友送礼状态信息列表 |

---

### wx.getFriendCloudStorage(Object object)

基础库 1.9.92 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/wx.getFriendCloudStorage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyList | Array.<string> |  | 是 | 要拉取的 key 列表 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | Array.<[UserGameData](UserGameData.html)> | 同玩好友的托管数据 |

---

### FriendInfo

用户信息

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/FriendInfo.html

---

### FriendSendGiftStatus

用户送礼状态信息

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/FriendSendGiftStatus.html

**blockCode 枚举**

| 值 | 含义 |
| --- | --- |
| 151066168 | 当前时间周期已经赠送，目前支持一天赠送一次 |
| 151066169 | 注册天数不足 首次注册时间必须大于 24 小时才能赠礼 |

---

### KVData

托管的 KV 数据

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/KVData.html

**将排行榜显示在小游戏中心**

| 属性名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| score | Int32 | 是 | 该榜单对应分数值 |
| update\_time | Int64 | 是 | 该分数最后更新时间，Unix时间戳 |

---

### OpenDataContextUserInfo

用户信息

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/OpenDataContextUserInfo.html

---

### UserGameData

托管数据

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/UserGameData.html

---

### wx.getUserInfo(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/data/OpenDataContext-wx.getUserInfo.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | openIdList | Array.<string> | [] | 否 | 要获取信息的用户的 openId 数组，如果要获取当前用户信息，则将数组中的一个元素设为 'selfOpenId' |
|  | lang | string | en | 否 | 显示用户信息的语言 |
|  | | 合法值 | 说明 | | --- | --- | | en | 英文 | | zh\_CN | 简体中文 | | zh\_TW | 繁体中文 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| en | 英文 |
| zh\_CN | 简体中文 |
| zh\_TW | 繁体中文 |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | data | Array.<Object> | 用户信息列表 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | avatarUrl | string | 用户头像图片 url | |  | city | string | 用户所在城市 | |  | country | string | 用户所在国家 | |  | gender | number | 用户性别 | |  | language | string | 显示 country province city 所用的语言 | |  | nickName | string | 用户昵称 | |  | openId | string | 用户 openId | |  | province | string | 用户所在省份 | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | avatarUrl | string | 用户头像图片 url |
|  | city | string | 用户所在城市 |
|  | country | string | 用户所在国家 |
|  | gender | number | 用户性别 |
|  | language | string | 显示 country province city 所用的语言 |
|  | nickName | string | 用户昵称 |
|  | openId | string | 用户 openId |
|  | province | string | 用户所在省份 |

---

### wx.onMessage(function callback)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/context/wx.onMessage.html

---

### OpenDataContext wx.getOpenDataContext(Object object)

基础库 1.9.92 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/context/wx.getOpenDataContext.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | sharedCanvasMode | String | offscreenCanvas | 否 | 共享画布类型，有效值为 offscreenCanvas 和 screenCanvas，默认为 offscreenCanvas。区别： offscreenCanvas 模式下，sharedCanvas 绘制完后需要渲染到主屏；screenCanvas 模式下，sharedCanvas 为独立渲染，并且本身已经上屏。 |
|  | | 合法值 | 说明 | | --- | --- | | offscreenCanvas | sharedCanvas 绘制完后需要渲染到主屏 | | screenCanvas | sharedCanvas 独立渲染，并且本身已经上屏 | | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| offscreenCanvas | sharedCanvas 绘制完后需要渲染到主屏 |
| screenCanvas | sharedCanvas 独立渲染，并且本身已经上屏 |

---

### OpenDataContext

开放数据域对象

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/context/OpenDataContext.html

---

### OpenDataContext.postMessage(Object message)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/context/OpenDataContext.postMessage.html

---

### FeedbackButton wx.createFeedbackButton(Object object)

基础库 2.1.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/feedback/wx.createFeedbackButton.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | type | string |  | 是 | 按钮的类型。 |
|  | | 合法值 | 说明 | | --- | --- | | text | 可以设置背景色和文本的按钮 | | image | 只能设置背景贴图的按钮，背景贴图会直接拉伸到按钮的宽高 | | | | | |
|  | text | string |  | 否 | 按钮上的文本，仅当 type 为 `text` 时有效 |
|  | image | string |  | 否 | 按钮的背景图片，仅当 type 为 `image` 时有效 |
|  | style | Object |  | 是 | 按钮的样式 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | left | number |  | 是 | 左上角横坐标 | |  | top | number |  | 是 | 左上角纵坐标 | |  | width | number |  | 是 | 宽度 | |  | height | number |  | 是 | 高度 | |  | backgroundColor | string |  | 是 | 背景颜色 | |  | borderColor | string |  | 否 | 边框颜色 | |  | borderWidth | number |  | 否 | 边框宽度 | |  | borderRadius | number |  | 否 | 边框圆角 | |  | color | string |  | 否 | 文本的颜色。格式为 6 位 16 进制数。 | |  | textAlign | string |  | 否 | 文本的水平居中方式 | |  | | 合法值 | 说明 | | --- | --- | | left | 居左 | | center | 居中 | | right | 居右 | | | | | | |  | fontSize | number |  | 否 | 字号 | |  | lineHeight | number |  | 否 | 文本的行高 | | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| text | 可以设置背景色和文本的按钮 |
| image | 只能设置背景贴图的按钮，背景贴图会直接拉伸到按钮的宽高 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | left | number |  | 是 | 左上角横坐标 |
|  | top | number |  | 是 | 左上角纵坐标 |
|  | width | number |  | 是 | 宽度 |
|  | height | number |  | 是 | 高度 |
|  | backgroundColor | string |  | 是 | 背景颜色 |
|  | borderColor | string |  | 否 | 边框颜色 |
|  | borderWidth | number |  | 否 | 边框宽度 |
|  | borderRadius | number |  | 否 | 边框圆角 |
|  | color | string |  | 否 | 文本的颜色。格式为 6 位 16 进制数。 |
|  | textAlign | string |  | 否 | 文本的水平居中方式 |
|  | | 合法值 | 说明 | | --- | --- | | left | 居左 | | center | 居中 | | right | 居右 | | | | | |
|  | fontSize | number |  | 否 | 字号 |
|  | lineHeight | number |  | 否 | 文本的行高 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| left | 居左 |
| center | 居中 |
| right | 居右 |

---

### FeedbackButton

用户点击后打开意见反馈页面的按钮

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/feedback/FeedbackButton.html

**string type**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| text | 可以设置背景色和文本的按钮 |  |
| image | 只能设置背景贴图的按钮，背景贴图会直接拉伸到按钮的宽高 |  |

**Object style**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | left | number | 左上角横坐标 |
|  | top | number | 左上角纵坐标 |
|  | width | number | 宽度 |
|  | height | number | 高度 |
|  | backgroundColor | string | 背景颜色 |
|  | borderColor | string | 边框颜色 |
|  | borderWidth | number | 边框宽度 |
|  | borderRadius | number | 边框圆角 |
|  | color | string | 文本的颜色。格式为 6 位 16 进制数。 |
|  | textAlign | string | 文本的水平居中方式 |
|  | | 合法值 | 说明 | | --- | --- | | left | 居左 | | center | 居中 | | right | 居右 | | | |
|  | fontSize | number | 字号 |
|  | lineHeight | number | 文本的行高 |

**Object style**

| 合法值 | 说明 |
| --- | --- |
| left | 居左 |
| center | 居中 |
| right | 居右 |

---

### FeedbackButton.destroy()

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/feedback/FeedbackButton.destroy.html

---

### FeedbackButton.hide()

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/feedback/FeedbackButton.hide.html

---

### FeedbackButton.offTap(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/feedback/FeedbackButton.offTap.html

---

### FeedbackButton.onTap(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/feedback/FeedbackButton.onTap.html

---

### FeedbackButton.show()

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/feedback/FeedbackButton.show.html

---

### wx.openSetting(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/setting/wx.openSetting.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| withSubscriptions | Boolean | false | 否 | 是否同时获取用户订阅消息的订阅状态，默认不获取。注意：withSubscriptions 只返回用户勾选过订阅面板中的“总是保持以上选择，不再询问”的订阅消息。 | [2.10.3](../../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| authSetting | [AuthSetting](AuthSetting.html) | 用户授权结果 |  |
| subscriptionsSetting | [SubscriptionsSetting](SubscriptionsSetting.html) | 用户订阅消息设置，接口参数`withSubscriptions`值为`true`时才会返回。 | [2.10.3](../../../guide/runtime/client-lib/compatibility.html) |

---

### wx.getSetting(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/setting/wx.getSetting.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| withSubscriptions | Boolean | false | 否 | 是否同时获取用户订阅消息的订阅状态，默认不获取。注意：withSubscriptions 只返回用户勾选过订阅面板中的“总是保持以上选择，不再询问”的订阅消息。 | [2.10.1](../../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| authSetting | [AuthSetting](AuthSetting.html) | 用户授权结果 |  |
| subscriptionsSetting | [SubscriptionsSetting](SubscriptionsSetting.html) | 用户订阅消息设置，接口参数`withSubscriptions`值为`true`时才会返回。 | [2.10.1](../../../guide/runtime/client-lib/compatibility.html) |
| miniprogramAuthSetting | [AuthSetting](AuthSetting.html) | 在插件中调用时，当前宿主小程序的用户授权结果 |  |

---

### OpenSettingButton wx.createOpenSettingButton(Object object)

从基础库3.0.0开始，本接口停止维护，请使用wx.openSetting代替

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/setting/wx.createOpenSettingButton.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | type | string |  | 是 | 按钮的类型。 |
|  | | 合法值 | 说明 | | --- | --- | | text | 可以设置背景色和文本的按钮 | | image | 只能设置背景贴图的按钮，背景贴图会直接拉伸到按钮的宽高 | | | | | |
|  | text | string |  | 否 | 按钮上的文本，仅当 type 为 `text` 时有效 |
|  | image | string |  | 否 | 按钮的背景图片，仅当 type 为 `image` 时有效 |
|  | style | Object |  | 是 | 按钮的样式 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | left | number |  | 是 | 左上角横坐标 | |  | top | number |  | 是 | 左上角纵坐标 | |  | width | number |  | 是 | 宽度 | |  | height | number |  | 是 | 高度 | |  | backgroundColor | string |  | 是 | 背景颜色 | |  | borderColor | string |  | 否 | 边框颜色 | |  | borderWidth | number |  | 否 | 边框宽度 | |  | borderRadius | number |  | 否 | 边框圆角 | |  | color | string |  | 否 | 文本的颜色。格式为 6 位 16 进制数。 | |  | textAlign | string |  | 否 | 文本的水平居中方式 | |  | | 合法值 | 说明 | | --- | --- | | left | 居左 | | center | 居中 | | right | 居右 | | | | | | |  | fontSize | number |  | 否 | 字号 | |  | lineHeight | number |  | 否 | 文本的行高 | | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| text | 可以设置背景色和文本的按钮 |
| image | 只能设置背景贴图的按钮，背景贴图会直接拉伸到按钮的宽高 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | left | number |  | 是 | 左上角横坐标 |
|  | top | number |  | 是 | 左上角纵坐标 |
|  | width | number |  | 是 | 宽度 |
|  | height | number |  | 是 | 高度 |
|  | backgroundColor | string |  | 是 | 背景颜色 |
|  | borderColor | string |  | 否 | 边框颜色 |
|  | borderWidth | number |  | 否 | 边框宽度 |
|  | borderRadius | number |  | 否 | 边框圆角 |
|  | color | string |  | 否 | 文本的颜色。格式为 6 位 16 进制数。 |
|  | textAlign | string |  | 否 | 文本的水平居中方式 |
|  | | 合法值 | 说明 | | --- | --- | | left | 居左 | | center | 居中 | | right | 居右 | | | | | |
|  | fontSize | number |  | 否 | 字号 |
|  | lineHeight | number |  | 否 | 文本的行高 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| left | 居左 |
| center | 居中 |
| right | 居右 |

---

### AuthSetting

用户授权设置信息，详情参考权限

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/setting/AuthSetting.html

---

### OpenSettingButton

用户点击后打开设置页面的按钮

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/setting/OpenSettingButton.html

**string type**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| text | 可以设置背景色和文本的按钮 |  |
| image | 只能设置背景贴图的按钮，背景贴图会直接拉伸到按钮的宽高 |  |

**Object style**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | left | number | 左上角横坐标 |
|  | top | number | 左上角纵坐标 |
|  | width | number | 宽度 |
|  | height | number | 高度 |
|  | backgroundColor | string | 背景颜色 |
|  | borderColor | string | 边框颜色 |
|  | borderWidth | number | 边框宽度 |
|  | borderRadius | number | 边框圆角 |
|  | color | string | 文本的颜色。格式为 6 位 16 进制数。 |
|  | textAlign | string | 文本的水平居中方式 |
|  | | 合法值 | 说明 | | --- | --- | | left | 居左 | | center | 居中 | | right | 居右 | | | |
|  | fontSize | number | 字号 |
|  | lineHeight | number | 文本的行高 |

**Object style**

| 合法值 | 说明 |
| --- | --- |
| left | 居左 |
| center | 居中 |
| right | 居右 |

---

### OpenSettingButton.destroy()

销毁打开设置页面按钮

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/setting/OpenSettingButton.destroy.html

---

### OpenSettingButton.hide()

隐藏打开设置页面按钮。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/setting/OpenSettingButton.hide.html

---

### OpenSettingButton.offTap(function listener)

移除设置页面按钮的点击事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/setting/OpenSettingButton.offTap.html

---

### OpenSettingButton.onTap(function listener)

监听设置页面按钮的点击事件

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/setting/OpenSettingButton.onTap.html

---

### OpenSettingButton.show()

显示打开设置页面按钮

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/setting/OpenSettingButton.show.html

---

### SubscriptionsSetting

订阅消息设置

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/setting/SubscriptionsSetting.html

---

### wx.getGameClubData(Object object)

基础库 2.25.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/game-club/wx.getGameClubData.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | dataTypeList | Array.<Object> |  | 是 | 需要获取的数据指标的对象数组 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | type | number |  | 是 | 见type表格说明 | |  | subKey | string |  | 否 | 部分type需要传，见type表格说明 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | type | number |  | 是 | 见type表格说明 |
|  | subKey | string |  | 否 | 部分type需要传，见type表格说明 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| signature | string | 使用 sha1( rawData + sessionkey ) 得到字符串，用于校验用户信息 |
| encryptedData | string | 包括 GameClubData 在内的加密数据，详见[加密数据解密算法](../../../guide/open-ability/signature.html) |
| iv | string | 加密算法的初始向量 |
| cloudID | string | 敏感数据对应的云 ID，开通云开发的小程序才会返回，可通过[云调用直接获取开放数据](../../../guide/open-ability/signature.html) |

**type说明**

| type取值 | 说明 | subKey | GameClubDataByType.value |
| --- | --- | --- | --- |
| 1 | 加入该游戏圈时间 | 无需传入 | 秒级Unix时间戳 |
| 3 | 用户禁言状态 | 无需传入 | 0：正常 1：禁言 |
| 4 | 当天(自然日)点赞贴子数 | 无需传入 |  |
| 5 | 当天(自然日)评论贴子数 | 无需传入 |  |
| 6 | 当天(自然日)发表贴子数 | 无需传入 |  |
| 7 | 当天(自然日)发表视频贴子数 | 无需传入 |  |
| 8 | 当天(自然日)赞官方贴子数 | 无需传入 |  |
| 9 | 当天(自然日)评论官方贴子数 | 无需传入 |  |
| 10 | 当天(自然日)发表到本圈子话题的贴子数 | 传入话题id，从mp-游戏圈话题管理处获取 |  |
| 11 | 用户最近一次推荐游戏时间 | 无需传入 | 秒级时间戳 |

**encryptedData 解密后得到的 GameClubData 的结构**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| dataList | Array<GameClubDataByType> | 游戏圈相关数据的对象数组 |

**GameClubDataByType 的结构**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| dataType | number | 与输入的 dataType 一致 |
| value | number | 不同type返回的value含义不同，见type表格说明 |

---

### GameClubButton wx.createGameClubButton(Object object)

基础库 2.0.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/game-club/wx.createGameClubButton.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | type | string |  | 是 | 按钮的类型。 |  |
|  | | 合法值 | 说明 | | --- | --- | | text | 可以设置背景色和文本的按钮 | | image | 只能设置背景贴图的按钮，背景贴图会直接拉伸到按钮的宽高 | | | | | | |
|  | text | string |  | 否 | 按钮上的文本，仅当 type 为 `text` 时有效 |  |
|  | image | string |  | 否 | 按钮的背景图片，仅当 type 为 `image` 时有效 |  |
|  | style | Object |  | 是 | 按钮的样式 |  |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | left | number |  | 是 | 左上角横坐标 | |  | top | number |  | 是 | 左上角纵坐标 | |  | width | number |  | 是 | 宽度 | |  | height | number |  | 是 | 高度 | |  | backgroundColor | string |  | 是 | 背景颜色 | |  | borderColor | string |  | 否 | 边框颜色 | |  | borderWidth | number |  | 否 | 边框宽度 | |  | borderRadius | number |  | 否 | 边框圆角 | |  | color | string |  | 否 | 文本的颜色。格式为 6 位 16 进制数。 | |  | textAlign | string |  | 否 | 文本的水平居中方式 | |  | | 合法值 | 说明 | | --- | --- | | left | 居左 | | center | 居中 | | right | 居右 | | | | | | |  | fontSize | number |  | 否 | 字号 | |  | lineHeight | number |  | 否 | 文本的行高 | | | | | | |
|  | icon | string |  | 是 | 游戏圈按钮的图标，仅当 object.type 参数为 image 时有效。 |  |
|  | | 合法值 | 说明 | | --- | --- | | green | 绿色的图标 | | white | 白色的图标 | | dark | 有黑色圆角背景的白色图标 | | light | 有白色圆角背景的绿色图标 | | | | | | |
|  | openlink | string |  | 否 | 设置后可以跳到对应的活动页面，具体进入「MP后台-能力地图-游戏圈」-由帖子的"游戏内跳转ID"生成 | [2.30.3](../../../guide/runtime/client-lib/compatibility.html) |
|  | hasRedDot | boolean | true | 否 | 当传递了openlink值时，此字段生效，决定创建的按钮是否需要拥有红点，默认为true | [2.30.3](../../../guide/runtime/client-lib/compatibility.html) |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| text | 可以设置背景色和文本的按钮 |
| image | 只能设置背景贴图的按钮，背景贴图会直接拉伸到按钮的宽高 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | left | number |  | 是 | 左上角横坐标 |
|  | top | number |  | 是 | 左上角纵坐标 |
|  | width | number |  | 是 | 宽度 |
|  | height | number |  | 是 | 高度 |
|  | backgroundColor | string |  | 是 | 背景颜色 |
|  | borderColor | string |  | 否 | 边框颜色 |
|  | borderWidth | number |  | 否 | 边框宽度 |
|  | borderRadius | number |  | 否 | 边框圆角 |
|  | color | string |  | 否 | 文本的颜色。格式为 6 位 16 进制数。 |
|  | textAlign | string |  | 否 | 文本的水平居中方式 |
|  | | 合法值 | 说明 | | --- | --- | | left | 居左 | | center | 居中 | | right | 居右 | | | | | |
|  | fontSize | number |  | 否 | 字号 |
|  | lineHeight | number |  | 否 | 文本的行高 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| left | 居左 |
| center | 居中 |
| right | 居右 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| green | 绿色的图标 |
| white | 白色的图标 |
| dark | 有黑色圆角背景的白色图标 |
| light | 有白色圆角背景的绿色图标 |

---

### GameClubButton

游戏圈按钮。游戏圈按钮被点击后会跳转到小游戏的游戏圈。更多关于游戏圈的信息见游戏圈使用指南

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/game-club/GameClubButton.html

**string icon**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| green | 绿色的图标 |  |
| white | 白色的图标 |  |
| dark | 有黑色圆角背景的白色图标 |  |
| light | 有白色圆角背景的绿色图标 |  |

**string type**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| text | 可以设置背景色和文本的按钮 |  |
| image | 只能设置背景贴图的按钮，背景贴图会直接拉伸到按钮的宽高 |  |

**Object style**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | left | number | 左上角横坐标 |
|  | top | number | 左上角纵坐标 |
|  | width | number | 宽度 |
|  | height | number | 高度 |
|  | backgroundColor | string | 背景颜色 |
|  | borderColor | string | 边框颜色 |
|  | borderWidth | number | 边框宽度 |
|  | borderRadius | number | 边框圆角 |
|  | color | string | 文本的颜色。格式为 6 位 16 进制数。 |
|  | textAlign | string | 文本的水平居中方式 |
|  | | 合法值 | 说明 | | --- | --- | | left | 居左 | | center | 居中 | | right | 居右 | | | |
|  | fontSize | number | 字号 |
|  | lineHeight | number | 文本的行高 |

**Object style**

| 合法值 | 说明 |
| --- | --- |
| left | 居左 |
| center | 居中 |
| right | 居右 |

---

### GameClubButton.destroy()

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/game-club/GameClubButton.destroy.html

---

### GameClubButton.hide()

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/game-club/GameClubButton.hide.html

---

### GameClubButton.offTap(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/game-club/GameClubButton.offTap.html

---

### GameClubButton.onTap(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/game-club/GameClubButton.onTap.html

---

### GameClubButton.show()

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/game-club/GameClubButton.show.html

---

### wx.openCustomerServiceConversation(Object object)

基础库 2.0.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/customer-message/wx.openCustomerServiceConversation.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sessionFrom | string | '' | 否 | 会话来源。该字段会在进入客服会话时透传给开发者配置好的后台服务。该字段（utf-8编码）最长不得超过 1000 个字节（不是字符串长度），超过将被截断。 |
| showMessageCard | boolean | false | 否 | 是否显示会话内消息卡片，设置此参数为 true，用户进入客服会话会在右下角显示"可能要发送的小程序"提示，用户点击后可以快速发送小程序消息 |
| sendMessageTitle | string | '' | 否 | 会话内消息卡片标题 |
| sendMessagePath | string | '' | 否 | 会话内消息卡片路径 |
| sendMessageImg | string | '' | 否 | 会话内消息卡片图片路径 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| path | string | 在客服会话内点击小程序消息卡片进入小程序时，所带的小程序打开路径 |
| query | Object | 在客服会话内点击小程序消息卡片进入小程序时，所带的小程序打开参数 |

---

### wx.getWeRunData(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/werun/wx.getWeRunData.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| encryptedData | string | 包括敏感数据在内的完整用户信息的加密数据，详细见[加密数据解密算法](../../../guide/open-ability/signature.html)。解密后得到的数据结构见后文 |  |
| iv | string | 加密算法的初始向量，详细见[加密数据解密算法](../../../guide/open-ability/signature.html) |  |
| cloudID | string | 敏感数据对应的云 ID，开通云开发的小程序才会返回，可通过云调用直接获取开放数据，详细见[云调用直接获取开放数据](../../../guide/open-ability/signature.html#method-cloud) | [2.7.0](../../../guide/runtime/client-lib/compatibility.html) |

**开放数据 JSON 结构**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| timestamp | number | 时间戳，表示数据对应的时间 |
| step | number | 微信运动步数 |

---

### PageManager wx.createPageManager()

基础库 3.6.7 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/openlink/wx.createPageManager.html

**错误码信息**

| 代码 | 原因 | 解决方案 |
| --- | --- | --- |
| 0 | 无异常 | - |
| -1 | openlink异常 | 请确认openlink填写完整且正确。 |
| -2 | 基础库版本不支持 | 基础库版本较低引起，受平台灰度等策略影响。 |
| -3 | 当前设备暂不支持 | 通常受活动、能力本身对平台限制引起。 |
| -4 | 业务渠道方报错 | 由openlink业务方提供的错误信息，具体错误信息请详见 errInfo 字段。 |
| -5 | 其他错误 | 其他原因引发的错误，具体错误信息请详见 errInfo 字段。 |
| -6 | 网络错误 | 网络异常引发的错误，检查网络环境。 |
| -7 | 频繁错误 | 请勿高频发起load请求。 |
| -8 | 小游戏版本错误 | 小游戏版本与openlink不匹配，需正确使用openlink对应生效的 开发版、体验版、正式版。 |

---

### PageManager

基础库 3.6.7 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/openlink/PageManager.html

---

### PageManager.destroy()

基础库 3.6.7 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/openlink/PageManager.destroy.html

---

### Promise PageManager.load(Object object)

基础库 3.6.7 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/openlink/PageManager.load.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| openlink | string |  | 是 | 从不同渠道获得的OPENLINK字符串 |
| query | Object |  | 否 | 选填，部分活动、功能允许接收自定义query参数，请参阅渠道说明，默认可不填 |
| extraData | Object |  | 否 | 选填，部分活动、功能允许额外提供参数数据，具体使用请根据渠道说明，默认可不填 |

**Promise**

| 代码 | 原因 | 解决方案 |
| --- | --- | --- |
| 0 | 无异常 | - |
| -1 | openlink异常 | 请确认openlink填写完整且正确。 |
| -2 | 基础库版本不支持 | 基础库版本较低引起，受平台灰度等策略影响。 |
| -3 | 当前设备暂不支持 | 通常受活动、能力本身对平台限制引起。 |
| -4 | 业务渠道方报错 | 由openlink业务方提供的错误信息，具体错误信息请详见 errInfo 字段。 |
| -5 | 其他错误 | 其他原因引发的错误，具体错误信息请详见 errInfo 字段。 |
| -6 | 网络错误 | 网络异常引发的错误，检查网络环境。 |
| -7 | 频繁错误 | 请勿高频发起load请求。 |
| -8 | 小游戏版本错误 | 小游戏版本与openlink不匹配，需正确使用openlink对应生效的 开发版、体验版、正式版。 |

---

### PageManager.off(string eventName, function callback)

基础库 3.6.7 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/openlink/PageManager.off.html

---

### PageManager.on(string eventName, function callback)

基础库 3.6.7 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/openlink/PageManager.on.html

---

### Promise PageManager.show(Object object)

基础库 3.6.7 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/openlink/PageManager.show.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| openlink | string |  | 否 | 从不同渠道获得的OPENLINK字符串 |
| query | Object |  | 否 | 选填，部分活动、功能允许接收自定义query参数，请参阅渠道说明，默认可不填 |
| extraData | Object |  | 否 | 选填，部分活动、功能允许额外提供参数数据，具体使用请根据渠道说明，默认可不填 |

---

### RankManager wx.getRankManager()

基础库 3.14.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/game-component/wx.getRankManager.html

---

### RankManager

小游戏擂台赛组件管理器。可通过wx.getRankManager获取实例。关于小游戏擂台赛的功能介绍详见小游戏擂台赛指南文档。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/game-component/RankManager.html

---

### RankManager.abort(Object params)

基础库 3.14.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/game-component/RankManager.abort.html

**Object params**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### RankManager.createChallenge(Object params)

基础库 3.14.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/game-component/RankManager.createChallenge.html

**Object params**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| scoreKey | string |  | 是 | 玩法唯一标识，用于区分不同的擂台赛玩法。可以在 MP后台-运营功能管理-基础配置-游戏玩法ID 中配置 |
| subScoreKey | number |  | 否 | 可选子 key，正整数，取值范围1-1000。该参数可用于游戏同一玩法的关卡区分，从基础库版本3.12.1开始支持 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### RankManager.getScore(Object params)

基础库 3.14.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/game-component/RankManager.getScore.html

**Object params**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| scoreKeys | Array.<string> |  | 是 | 玩法唯一标识数组 |
| subScoreKeys | Array.<number> |  | 否 | 可选子 key 数组，从基础库版本3.12.1开始支持 |
| periodType | number |  | 是 | 查询的周期：1：自然日最高分；2：自然周最高分；3：自然月最高分；4：历史最高分；5 最新得分 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### RankManager.middleUpdate(Object params)

基础库 3.14.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/game-component/RankManager.middleUpdate.html

**Object params**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| scoreKey | string |  | 是 | 玩法唯一标识，用于区分不同的擂台赛玩法。可以在 MP后台-运营功能管理-基础配置-游戏玩法ID 中配置 |
| score | number |  | 是 | 用户得分 |
| subScoreKey | number |  | 否 | 可选子 key，正整数，取值范围1-1000。该参数可用于游戏同一玩法的关卡区分，从基础库版本3.12.1开始支持 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### RankManager.offChallengeStart(function callback)

基础库 3.14.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/game-component/RankManager.offChallengeStart.html

**function callback**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| scoreKey | string | 玩法唯一标识 |
| subScoreKey | number | 可选子 key |

---

### RankManager.onChallengeStart(function callback)

基础库 3.14.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/game-component/RankManager.onChallengeStart.html

**function callback**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| scoreKey | string | 玩法唯一标识 |
| subScoreKey | number | 可选子 key |

---

### RankManager.update(Object params)

基础库 3.14.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/game-component/RankManager.update.html

**Object params**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| scoreKey | string |  | 是 | 玩法唯一标识，用于区分不同的擂台赛玩法。可以在 MP后台-运营功能管理-基础配置-游戏玩法ID 中配置 |
| score | number |  | 是 | 分数值 |
| subScoreKey | number |  | 否 | 可选子 key，正整数，取值范围1-1000。该参数可用于游戏同一玩法的关卡区分，从基础库版本3.12.1开始支持 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### StoreGift wx.createStoreGift(Object object)

基础库 3.8.12 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/store-gift/wx.createStoreGift.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| presentOrderId | boolean |  | 否 | 礼物订单id，调用“创建并发送礼物”或通过“查询礼物订单列表”open api拿到，open api文档[链接](https://doc.weixin.qq.com/doc/w3_AecACAZVAPMCNRyNF8Tq1Ts0zKrGq)。 |
| openid | string |  | 否 | 用户 openid |

---

### StoreGift

基础库 3.8.12 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/store-gift/StoreGift.html

---

### Promise StoreGift.getOrderInfo()

基础库 3.8.12 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/store-gift/StoreGift.getOrderInfo.html

**Promise.<Object>**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| orderStatus | number | 当前订单对应的状态码 |
| wishMessage | string | 当前订单对应的祝福语 |

**orderStatus 状态码**

| 值 | 含义 |
| --- | --- |
| 10 | 支付成功，用户可以领取礼物(小程序/小游戏下单成功初始状态) |
| 20 | 礼物已经领取 |
| 180 | 礼物超时未领取 |
| 181 | 超时退款 |
| 250 | 订单已取消 |

**异常捕获**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errCode | number | 错误码 |
| errMsg | string | 错误信息 |

**异常捕获**

| 值 | 含义 |
| --- | --- |
| 40097 | 参数错误，请检查订单 id 是否传对 |
| 606662 | 606662 表示当前用户非收礼人 |

---

### boolean StoreGift.isSupported()

基础库 3.8.12 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/store-gift/StoreGift.isSupported.html

---

### Promise StoreGift.open()

基础库 3.8.12 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/store-gift/StoreGift.open.html

**异常捕获**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errCode | number | 错误码 |
| errMsg | string | 错误信息 |

**异常捕获**

| 值 | 含义 |
| --- | --- |
| -1000 | 订单加载失败，请重试 |
| -1001 | 订单参数错误 |
| -1002 | 打开礼物失败[礼物状态异常] |
| -1003 | 调用客户端接口失败 |
| -1004 | 正在加载订单信息 |
| -1005 | 当前环境不支持 |

---

### wx.openCard(Object object)

基础库 2.5.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/card/wx.openCard.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | cardList | Array.<Object> |  | 是 | 需要打开的卡券列表 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | cardId | string |  | 是 | 卡券 ID | |  | code | string |  | 是 | 由 [wx.addCard](wx.addCard.html) 的返回对象中的加密 code 通过解密后得到，解密请参照：[code 解码接口](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1499332673_Unm7V) | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | cardId | string |  | 是 | 卡券 ID |
|  | code | string |  | 是 | 由 [wx.addCard](wx.addCard.html) 的返回对象中的加密 code 通过解密后得到，解密请参照：[code 解码接口](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1499332673_Unm7V) |

---

### wx.addCard(Object object)

基础库 2.5.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/card/wx.addCard.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | cardList | Array.<Object> |  | 是 | 需要添加的卡券列表 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | cardId | string |  | 是 | 卡券 ID | |  | cardExt | string |  | 是 | 卡券的扩展参数。需将 CardExt 对象 JSON 序列化为\*\*字符串\*\*传入 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | cardId | string |  | 是 | 卡券 ID |
|  | cardExt | string |  | 是 | 卡券的扩展参数。需将 CardExt 对象 JSON 序列化为\*\*字符串\*\*传入 |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | cardList | Array.<Object> | 卡券添加结果列表 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | code | string | 加密 code，为用户领取到卡券的code加密后的字符串，解密请参照：[code 解码接口](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1499332673_Unm7V) | |  | cardId | string | 用户领取到卡券的 ID | |  | cardExt | string | 卡券的扩展参数，结构请参考下文 | |  | isSuccess | boolean | 是否成功 | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | code | string | 加密 code，为用户领取到卡券的code加密后的字符串，解密请参照：[code 解码接口](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1499332673_Unm7V) |
|  | cardId | string | 用户领取到卡券的 ID |
|  | cardExt | string | 卡券的扩展参数，结构请参考下文 |
|  | isSuccess | boolean | 是否成功 |

---

### wx.checkIsAddedToMyMiniProgram(Object object)

基础库 2.30.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/my-miniprogram/wx.checkIsAddedToMyMiniProgram.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| added | boolean | 是否被添加至 「我的小程序」 |

---

### wx.requestFacialVerify(Object object)

基础库 3.8.12 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/face/wx.requestFacialVerify.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| verifyId | string |  | 是 | 人脸核身会话唯一标识（小程序后台根据「用户实名信息（姓名+身份证）」调用微信后台[getVerifyId](https://developers.weixin.qq.com/miniprogram/dev/server/API/face/api_getverifyid.html)接口获取） |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | 人脸识别完成（需要通过[queryVerifyInfo](https://developers.weixin.qq.com/miniprogram/dev/server/API/face/api_queryverifyinfo.html)接口查询人脸核身真实验证结果） |  |

---

### wx.checkIsSupportFacialRecognition(Object object)

基础库 3.8.12 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/face/wx.checkIsSupportFacialRecognition.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.requestFacialRecognition(Object object)

基础库 3.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/account-info/wx.requestFacialRecognition.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | 人脸识别成功 |  |
| 2002004 | 人脸识别失败 |  |
| 2002006 | 用户取消/超时/不同意，导致未完成人脸识别 |  |
| 2002007 | 本用户7天内人脸识别已通过，通过日期为XX |  |
| 2002008 | 本日已调起过人脸识别或者本月调用次数已达上限 |  |
| 2002009 | 无权限发起人脸识别 |  |

---

### Object wx.getAccountInfoSync()

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/account-info/wx.getAccountInfoSync.html

**Object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | miniProgram | Object | 小程序账号信息 |
|  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | appId | string | 小程序 appId |  | |  | envVersion | string | 小程序版本 | [2.10.0](../../../guide/runtime/client-lib/compatibility.html) | |  | | 合法值 | 说明 | | --- | --- | | develop | 开发版，提交代码审核时默认使用开发版进行审核。 | | trial | 体验版 | | release | 正式版 | | | | | |  | version | string | 线上小程序版本号 | [2.10.2](../../../guide/runtime/client-lib/compatibility.html) | | | |
|  | plugin | Object | 插件账号信息（仅在插件中调用时包含这一项） |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 插件 appId | |  | version | string | 插件版本号 | | | |

**Object**

|  | 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | appId | string | 小程序 appId |  |
|  | envVersion | string | 小程序版本 | [2.10.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | develop | 开发版，提交代码审核时默认使用开发版进行审核。 | | trial | 体验版 | | release | 正式版 | | | | |
|  | version | string | 线上小程序版本号 | [2.10.2](../../../guide/runtime/client-lib/compatibility.html) |

**Object**

| 合法值 | 说明 |
| --- | --- |
| develop | 开发版，提交代码审核时默认使用开发版进行审核。 |
| trial | 体验版 |
| release | 正式版 |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | appId | string | 插件 appId |
|  | version | string | 插件版本号 |

---

### wx.reserveChannelsLive(Object object)

基础库 2.19.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/channels/wx.reserveChannelsLive.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| noticeId | string |  | 是 | 预告 id，通过 getChannelsLiveNoticeInfo 接口获取 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.openChannelsUserProfile(Object object)

基础库 2.21.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/channels/wx.openChannelsUserProfile.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| finderUserName | string |  | 是 | 视频号id（参考格式为：sphcqO59YEPCvoe；查看路径为：微信客户端->我tab->视频号->右上角.-＞视频号名字-视频号ID） |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.openChannelsLive(Object object)

基础库 2.15.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/channels/wx.openChannelsLive.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| finderUserName | string |  | 是 | 视频号 id，以“sph”开头的id，可在视频号助手获取 |
| feedId | string |  | 否 | 直播 feedId，通过 getChannelsLiveInfo 接口获取（基础库 v2.19.2 之前的版本需要填写） |
| nonceId | string |  | 否 | 直播 nonceId，通过 getChannelsLiveInfo 接口获取（基础库 v2.19.2 之前的版本需要填写） |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.openChannelsEvent(Object object)

基础库 2.21.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/channels/wx.openChannelsEvent.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| finderUserName | string |  | 是 | 视频号 id，以“sph”开头的id，可在视频号助手获取 |
| eventId | string |  | 是 | 活动 id |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.openChannelsActivity(Object object)

基础库 2.19.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/channels/wx.openChannelsActivity.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| finderUserName | string |  | 是 | 视频号 id，以“sph”开头的id，可在视频号助手获取 |
| feedId | string |  | 是 | 视频 feedId |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.getChannelsLiveNoticeInfo(Object object)

基础库 2.19.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/channels/wx.getChannelsLiveNoticeInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| finderUserName | string |  | 是 | 视频号 id，以“sph”开头的id，可在视频号助手获取 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| noticeId | string | 预告 id |  |
| status | number | 预告状态：0可用 1取消 2已用 |  |
| startTime | string | 开始时间 |  |
| headUrl | string | 直播封面 |  |
| nickname | string | 视频号昵称 |  |
| reservable | boolean | 是否可预约 |  |
| otherInfos | Array.<Object> | 除最近的一条预告信息外，其他的预告信息列表（注意：每次最多返回按时间戳增序排列的15个预告信息，其中时间最近的那个预告信息会在接口其他的返回参数中展示，其余的预告信息会在该字段中展示）。 | [2.24.6](../../../guide/runtime/client-lib/compatibility.html) |

---

### wx.getChannelsLiveInfo(Object object)

基础库 2.15.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/channels/wx.getChannelsLiveInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| finderUserName | string |  | 是 | 视频号 id，以“sph”开头的id，可在视频号助手获取 |  |
| startTime | number |  | 否 | 起始时间，筛选指定时间段的直播。若上传了endTime，未上传startTime，则startTime默认为0 | [2.29.0](../../../guide/runtime/client-lib/compatibility.html) |
| endTime | number |  | 否 | 结束时间，筛选指定时间段的直播。若上传了startTime，未上传endTime，则endTime默认取当前时间 | [2.29.0](../../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | feedId | string | 直播 feedId |  |
|  | nonceId | string | 直播 nonceId |  |
|  | description | string | 直播主题 |  |
|  | status | number | 直播状态 |  |
|  | | 合法值 | 说明 | | --- | --- | | 1 | 直播状态不存在（针对未开过直播的主播） | | 2 | 直播中 | | 3 | 直播已结束 | | 4 | 直播准备中（未开播） | | | | |
|  | headUrl | string | 视频号头像 |  |
|  | nickname | string | 视频号昵称 |  |
|  | replayStatus | string | 直播回放状态 | [2.29.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 未生成 | | 1 | 已生成 | | 3 | 生成中 | | 6 | 已过期 | | | | |
|  | otherInfos | Array.<Object> | 除最近的一条直播外，其他的直播列表（注意：每次最多返回按时间戳增序排列的15个直播信息，其中时间最近的那个直播会在接口其他的返回参数中展示，其余的直播会在该字段中展示）。 | [2.29.0](../../../guide/runtime/client-lib/compatibility.html) |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 1 | 直播状态不存在（针对未开过直播的主播） |
| 2 | 直播中 |
| 3 | 直播已结束 |
| 4 | 直播准备中（未开播） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 0 | 未生成 |
| 1 | 已生成 |
| 3 | 生成中 |
| 6 | 已过期 |

---

### wx.getGroupEnterInfo(Object object)

基础库 2.10.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/group/wx.getGroupEnterInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| allowSingleChat | boolean | false | 否 | 开启后单聊下返回 open\_single\_roomid | [3.7.8](../../../guide/runtime/client-lib/compatibility.html) |
| needGroupOpenID | boolean | false | 否 | 开启后返回用户在群(含单聊)下的 group\_openid | [3.7.8](../../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| errMsg | string | 错误信息 |  |
| encryptedData | string | 包括敏感数据在内的完整转发信息的加密数据，详细见[加密数据解密算法](../../../guide/open-ability/signature.html) |  |
| iv | string | 加密算法的初始向量，详细见[加密数据解密算法](../../../guide/open-ability/signature.html) |  |
| cloudID | string | 敏感数据对应的云 ID，开通[云开发](../../../wxcloud/basis/getting-started.html)的小程序才会返回，可通过云调用直接获取开放数据，详细见[云调用直接获取开放数据](../../../guide/open-ability/signature.html#method-cloud) | [2.7.0](../../../guide/runtime/client-lib/compatibility.html) |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 40097 |  | 场景错误 |
| 65206 |  | 用户已不在该群内 |

---

### wx.requirePrivacyAuthorize(Object object)

基础库 2.32.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/privacy/wx.requirePrivacyAuthorize.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.openPrivacyContract(Object object)

基础库 2.32.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/privacy/wx.openPrivacyContract.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.onNeedPrivacyAuthorization(function listener)

基础库 2.32.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/privacy/wx.onNeedPrivacyAuthorization.html

**Object eventInfo**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| referrer | string | 触发本次 onNeedPrivacyAuthorization 事件的接口或组件名（例如："getUserInfo", "UserInfoButton.onTap"） |

**resolve 接口参数**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| event | string | 用户操作类型 |

**event 合法值**

| event | 说明 |
| --- | --- |
| exposureAuthorization | 自定义隐私弹窗曝光 |
| agree | 用户同意隐私授权 |
| disagree | 用户拒绝隐私授权 |

---

### wx.getPrivacySetting(Object object)

基础库 2.32.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/privacy/wx.getPrivacySetting.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| needAuthorization | boolean | 是否需要用户授权隐私协议（如果开发者没有在「MP后台-设置-服务内容声明-用户隐私保护指引」中声明隐私收集类型则会返回false；如果开发者声明了隐私收集，且用户之前同意过隐私协议则会返回false；如果开发者声明了隐私收集，且用户还没同意过则返回true；如果用户之前同意过、但后来小程序又新增了隐私收集类型也会返回true） |
| privacyContractName | string | 隐私授权协议的名称 |

---

### wx.openCustomerServiceChat(Object object)

基础库 2.30.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/service-chat/wx.openCustomerServiceChat.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | extInfo | Object |  | 是 | 客服信息 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | url | String |  | 是 | 客服链接 | | | | | |
|  | corpId | String |  | 是 | 企业ID |
|  | showMessageCard | Boolean | false | 否 | 是否发送小程序气泡消息 |
|  | sendMessageTitle | String |  | 否 | 气泡消息标题 |
|  | sendMessagePath | String |  | 否 | 气泡消息小程序路径 |
|  | sendMessageImg | String |  | 否 | 气泡消息图片 |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | url | String |  | 是 | 客服链接 |

---

### wx.requestSubscribeSystemMessage(Object object)

基础库 2.9.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/subscribe-message/wx.requestSubscribeSystemMessage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| msgTypeList | Array.<string> |  | 是 | 系统订阅消息类型列表，一次调用最多可订阅3种类型的消息，目前支持："SYS\_MSG\_TYPE\_INTERACTIVE"（好友互动提醒）、"SYS\_MSG\_TYPE\_RANK"（排行榜超越提醒）、"SYS\_MSG\_TYPE\_WHATS\_NEW"（游戏更新提醒） |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | String | 接口调用成功时errMsg值为'requestSubscribeSystemMessage:ok' |
| MSG\_TYPE | String | [MSG\_TYPE]是动态的键，即系统订阅消息类型，值为'accept'、'reject'、'ban'，'accept'表示用户同意订阅该类型对应的模板消息，'reject'表示用户拒绝订阅该类型对应的模板消息，'ban'表示已被后台封禁。例如 { errMsg: "requestSubscribeSystemMessage:ok", SYS\_MSG\_TYPE\_INTERACTIVE: "accept" } 表示用户同意订阅'SYS\_MSG\_TYPE\_INTERACTIVE'这条消息 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | String | 接口调用失败错误信息 |
| errCode | Number | 接口调用失败错误码 |

**错误码**

| errCode | errMsg | 说明 |
| --- | --- | --- |
| 10001 | TmplIds can't be empty | 参数传空了 |
| 10002 | Request list fail | 网络问题，请求消息列表失败 |
| 10003 | Request subscribe fail | 网络问题，订阅请求发送失败 |
| 10004 | Invalid template id | 参数类型错误 |
| 10005 | Cannot show subscribe message UI | 无法展示 UI，一般是小游戏这个时候退后台了导致的 |
| 20004 | The main switch is switched off | 用户关闭了主开关，无法进行订阅 |
| 20005 | This mini program was banned from subscribing messages | 小游戏被禁封 |

---

### wx.requestSubscribeMessage(Object object)

基础库 2.4.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/open-api/subscribe-message/wx.requestSubscribeMessage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| tmplIds | Array.<string> |  | 是 | 需要订阅的消息模板的id的集合，一次调用最多可订阅3条消息（注意：iOS客户端7.0.6版本、Android客户端7.0.7版本之后的一次性订阅/长期订阅才支持多个模板消息，iOS客户端7.0.5版本、Android客户端7.0.6版本之前的一次订阅只支持一个模板消息）消息模板id在[微信公众平台(mp.weixin.qq.com)-功能-订阅消息]中配置。每个tmplId对应的模板标题需要不相同，否则会被过滤。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | String | 接口调用成功时errMsg值为'requestSubscribeMessage:ok' |
| [TEMPLATE\_ID: string] | String | [TEMPLATE\_ID]是动态的键，即模板id，值包括'accept'、'reject'、'ban'、'filter'。'accept'表示用户同意订阅该条id对应的模板消息，'reject'表示用户拒绝订阅该条id对应的模板消息，'ban'表示已被后台封禁，'filter'表示该模板因为模板标题同名被后台过滤。例如 { errMsg: "requestSubscribeMessage:ok", zun-LzcQyW-edafCVvzPkK4de2Rllr1fFpw2A\_x0oXE: "accept"} 表示用户同意订阅zun-LzcQyW-edafCVvzPkK4de2Rllr1fFpw2A\_x0oXE这条消息 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | String | 接口调用失败错误信息 |
| errCode | Number | 接口调用失败错误码 |

**错误码**

| errCode | errMsg | 说明 |
| --- | --- | --- |
| 10001 | TmplIds can't be empty | 参数传空了 |
| 10002 | Request list fail | 网络问题，请求消息列表失败 |
| 10003 | Request subscribe fail | 网络问题，订阅请求发送失败 |
| 10004 | Invalid template id | 参数类型错误 |
| 10005 | Cannot show subscribe message UI | 无法展示 UI，一般是小游戏这个时候退后台了导致的 |
| 20001 | No template data return, verify the template id exist | 没有模板数据，一般是模板 ID 不存在 或者和模板类型不对应 导致的 |
| 20002 | Templates type must be same | 模板消息类型 既有一次性的又有永久的 |
| 20003 | Templates count out of max bounds | 模板消息数量超过上限 |
| 20004 | The main switch is switched off | 用户关闭了主开关，无法进行订阅 |
| 20005 | This mini program was banned from subscribing messages | 小游戏被禁封 |

---

<!-- pages: 112 -->
