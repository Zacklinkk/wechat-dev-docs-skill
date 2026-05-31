# 微信小程序 API 结构化参考 — open-api

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.pluginLogin(Object args)

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/wx.pluginLogin.html

**Object args**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object args**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| code | string | 用于换取 openpid 的凭证（有效期五分钟）。插件开发者可以用此 code 在开发者服务器后台调用 [getPluginOpenPId]((getPluginOpenPId)) 换取 openpid。 |

---

### wx.login(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/wx.login.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| timeout | number |  | 否 | 超时时间，单位ms | [1.9.90](../../../framework/compatibility.html) |
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
| errno | Number | errno 错误码，错误码的详细说明参考 [Errno错误码](../../../framework/usability/PublicErrno.html) | [2.24.0](../../../framework/compatibility.html) |

---

### wx.checkSession(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/wx.checkSession.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### Object wx.getAccountInfoSync()

基础库 2.2.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/account-info/wx.getAccountInfoSync.html

**Object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | miniProgram | Object | 小程序账号信息 |
|  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | appId | string | 小程序 appId |  | |  | envVersion | string | 小程序版本 | [2.10.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | | --- | --- | | develop | 开发版，提交代码审核时默认使用开发版进行审核。 | | trial | 体验版 | | release | 正式版 | | | | | |  | version | string | 线上小程序版本号 | [2.10.2](../../../framework/compatibility.html) | | | |
|  | plugin | Object | 插件账号信息（仅在插件中调用时包含这一项） |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 插件 appId | |  | version | string | 插件版本号 | | | |

**Object**

|  | 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | appId | string | 小程序 appId |  |
|  | envVersion | string | 小程序版本 | [2.10.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | develop | 开发版，提交代码审核时默认使用开发版进行审核。 | | trial | 体验版 | | release | 正式版 | | | | |
|  | version | string | 线上小程序版本号 | [2.10.2](../../../framework/compatibility.html) |

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

### wx.getUserProfile(Object object)

用户头像昵称获取规则已调整，参考小程序用户头像昵称获取规则调整公告

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/user-info/wx.getUserProfile.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | lang | string | en | 否 | 显示用户信息的语言 |
|  | | 合法值 | 说明 | | --- | --- | | en | 英文 | | zh\_CN | 简体中文 | | zh\_TW | 繁体中文 | | | | | |
|  | desc | string |  | 是 | 声明获取用户个人信息后的用途，不超过30个字符 |
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
| userInfo | [UserInfo](UserInfo.html) | 用户信息对象 | [2.10.4](../../../framework/compatibility.html) |
| rawData | string | 不包括敏感信息的原始数据字符串，用于计算签名 | [2.10.4](../../../framework/compatibility.html) |
| signature | string | 使用 sha1( rawData + sessionkey ) 得到字符串，用于校验用户信息，详见 [用户数据的签名验证和加解密](../../../framework/open-ability/signature.html) | [2.10.4](../../../framework/compatibility.html) |
| encryptedData | string | 包括敏感数据在内的完整用户信息的加密数据，详见 [用户数据的签名验证和加解密](../../../framework/open-ability/signature.html#加密数据解密算法) | [2.10.4](../../../framework/compatibility.html) |
| iv | string | 加密算法的初始向量，详见 [用户数据的签名验证和加解密](../../../framework/open-ability/signature.html#加密数据解密算法) | [2.10.4](../../../framework/compatibility.html) |
| cloudID | string | 敏感数据对应的云 ID，开通[云开发](../../../wxcloudservice/wxcloud/basis/getting-started.html)的小程序才会返回，可通过云调用直接获取开放数据，详细见[云调用直接获取开放数据](../../../framework/open-ability/signature.html#method-cloud) | [2.10.4](../../../framework/compatibility.html) |

---

### wx.getUserInfo(Object object)

用户头像昵称获取规则已调整，参考用户信息接口调整说明、小程序用户头像昵称获取规则调整公告

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/user-info/wx.getUserInfo.html

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
| signature | string | 使用 sha1( rawData + sessionkey ) 得到字符串，用于校验用户信息，详见 [用户数据的签名验证和加解密](../../../framework/open-ability/signature.html) |  |
| encryptedData | string | 包括敏感数据在内的完整用户信息的加密数据，详见 [用户数据的签名验证和加解密](../../../framework/open-ability/signature.html#加密数据解密算法) |  |
| iv | string | 加密算法的初始向量，详见 [用户数据的签名验证和加解密](../../../framework/open-ability/signature.html#加密数据解密算法) |  |
| cloudID | string | 敏感数据对应的云 ID，开通[云开发](../../../wxcloudservice/wxcloud/basis/getting-started.html)的小程序才会返回，可通过云调用直接获取开放数据，详细见[云调用直接获取开放数据](../../../framework/open-ability/signature.html#method-cloud) | [2.7.0](../../../framework/compatibility.html) |

---

### UserInfo

用户头像昵称获取规则已调整，参考用户信息接口调整说明、小程序用户头像昵称获取规则调整公告

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/user-info/UserInfo.html

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

### wx.authorizeForMiniProgram(Object object)

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/authorize/wx.authorizeForMiniProgram.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | scope | string |  | 是 | 需要获取权限的 scope，详见 [scope 列表](../../../framework/open-ability/authorize.html#scope-列表) |
|  | | 合法值 | 说明 | | --- | --- | | scope.record |  | | scope.writePhotosAlbum |  | | scope.camera |  | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| scope.record |  |
| scope.writePhotosAlbum |  |
| scope.camera |  |

---

### wx.authorize(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/authorize/wx.authorize.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| scope | string |  | 是 | 需要获取权限的 scope，详见 [scope 列表](../../../framework/open-ability/authorize.html#scope-%E5%88%97%E8%A1%A8) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.openSetting(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/setting/wx.openSetting.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| withSubscriptions | Boolean | false | 否 | 是否同时获取用户订阅消息的订阅状态，默认不获取。注意：withSubscriptions 只返回用户勾选过订阅面板中的“总是保持以上选择，不再询问”的订阅消息。 | [2.10.3](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| authSetting | [AuthSetting](AuthSetting.html) | 用户授权结果 |  |
| subscriptionsSetting | [SubscriptionsSetting](SubscriptionsSetting.html) | 用户订阅消息设置，接口参数`withSubscriptions`值为`true`时才会返回。 | [2.10.3](../../../framework/compatibility.html) |

---

### wx.getSetting(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/setting/wx.getSetting.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| withSubscriptions | Boolean | false | 否 | 是否同时获取用户订阅消息的订阅状态，默认不获取。注意：withSubscriptions 只返回用户勾选过订阅面板中的“总是保持以上选择，不再询问”的订阅消息。 | [2.10.1](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| authSetting | [AuthSetting](AuthSetting.html) | 用户授权结果 |  |
| subscriptionsSetting | [SubscriptionsSetting](SubscriptionsSetting.html) | 用户订阅消息设置，接口参数`withSubscriptions`值为`true`时才会返回。 | [2.10.1](../../../framework/compatibility.html) |
| miniprogramAuthSetting | [AuthSetting](AuthSetting.html) | 在插件中调用时，当前宿主小程序的用户授权结果 |  |

---

### AuthSetting

用户授权设置信息，详情参考权限

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/setting/AuthSetting.html

---

### SubscriptionsSetting

订阅消息设置

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/setting/SubscriptionsSetting.html

---

### wx.chooseAddress(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/address/wx.chooseAddress.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| userName | string | 收货人姓名 |
| postalCode | string | 邮编 |
| provinceName | string | 国标收货地址第一级地址 |
| cityName | string | 国标收货地址第二级地址 |
| countyName | string | 国标收货地址第三级地址 |
| streetName | string | 国标收货地址第四级地址 |
| detailInfo | string | 详细收货地址信息（包括街道地址） |
| detailInfoNew | string | 新选择器详细收货地址信息 |
| nationalCode | string | 收货地址国家码 |
| telNumber | string | 收货人手机号码 |
| errMsg | string | 错误信息 |

---

### wx.openCard(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/card/wx.openCard.html

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

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/card/wx.addCard.html

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

### wx.chooseInvoiceTitle(Object object)

基础库 1.5.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/invoice/wx.chooseInvoiceTitle.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | type | string | 抬头类型 |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 单位 | | 1 | 个人 | | | |
|  | title | string | 抬头名称 |
|  | taxNumber | string | 抬头税号 |
|  | companyAddress | string | 单位地址 |
|  | telephone | string | 手机号码 |
|  | bankName | string | 银行名称 |
|  | bankAccount | string | 银行账号 |
|  | errMsg | string | 错误信息 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 0 | 单位 |
| 1 | 个人 |

---

### wx.chooseInvoice(Object object)

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/invoice/wx.chooseInvoice.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| invoiceInfo | String | 用户选中的发票信息，格式为一个 JSON 字符串，包含三个字段： card\_id：所选发票卡券的 cardId，encrypt\_code：所选发票卡券的加密 code，报销方可以通过 cardId 和 encryptCode 获得报销发票的信息，app\_id： 发票方的 appId。 |

---

### wx.startSoterAuthentication(Object object)

基础库 1.5.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/soter/wx.startSoterAuthentication.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | requestAuthModes | Array.<string> |  | 是 | 请求使用的可接受的生物认证方式 |
|  | | 合法值 | 说明 | | --- | --- | | fingerPrint | 指纹识别 | | facial | 人脸识别 | | speech | 声纹识别（暂未支持） | | | | | |
|  | challenge | string |  | 是 | 挑战因子。挑战因子为调用者为此次生物鉴权准备的用于签名的字符串关键识别信息，将作为 `resultJSON` 的一部分，供调用者识别本次请求。例如：如果场景为请求用户对某订单进行授权确认，则可以将订单号填入此参数。 |
|  | authContent | string | '' | 否 | 验证描述，即识别过程中显示在界面上的对话框提示内容 |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| fingerPrint | 指纹识别 |
| facial | 人脸识别 |
| speech | 声纹识别（暂未支持） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| authMode | string | 生物认证方式 |
| resultJSON | string | 在设备安全区域（TEE）内获得的本机安全信息（如TEE名称版本号等以及防重放参数）以及本次认证信息（仅Android支持，本次认证的指纹ID）。具体说明见下文 |
| resultJSONSignature | string | 用SOTER安全密钥对 `resultJSON` 的签名(SHA256 with RSA/PSS, saltlen=20) |
| errCode | number | 错误码 |
| errMsg | string | 错误信息 |

**resultJSON 说明**

| 字段名 | 说明 |
| --- | --- |
| raw | 调用者传入的challenge |
| fid | （仅Android支持）本次生物识别认证的生物信息编号（如指纹识别则是指纹信息在本设备内部编号） |
| counter | 防重放特征参数 |
| tee\_n | TEE名称（如高通或者trustonic等） |
| tee\_v | TEE版本号 |
| fp\_n | 指纹以及相关逻辑模块提供商（如FPC等） |
| fp\_v | 指纹以及相关模块版本号 |
| cpu\_id | 机器唯一识别ID |
| uid | 概念同Android系统定义uid，即应用程序编号 |

---

### wx.checkIsSupportSoterAuthentication(Object object)

基础库 1.5.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/soter/wx.checkIsSupportSoterAuthentication.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | supportMode | Array.<string> | 该设备支持的可被SOTER识别的生物识别方式 |
|  | | 合法值 | 说明 | | --- | --- | | fingerPrint | 指纹识别 | | facial | 人脸识别 | | speech | 声纹识别（暂未支持） | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| fingerPrint | 指纹识别 |
| facial | 人脸识别 |
| speech | 声纹识别（暂未支持） |

---

### wx.checkIsSoterEnrolledInDevice(Object object)

基础库 1.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/soter/wx.checkIsSoterEnrolledInDevice.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | checkAuthMode | string |  | 是 | 认证方式 |
|  | | 合法值 | 说明 | | --- | --- | | fingerPrint | 指纹识别 | | facial | 人脸识别 | | speech | 声纹识别（暂未支持） | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| fingerPrint | 指纹识别 |
| facial | 人脸识别 |
| speech | 声纹识别（暂未支持） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| isEnrolled | boolean | 是否已录入信息 |
| errMsg | string | 错误信息 |

---

### wx.shareToWeRun(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/werun/wx.shareToWeRun.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | recordList | Array.<Object> |  | 是 | 运动数据列表 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | typeId | number |  | 是 | 运动项目id | |  | time | number |  | 是 | 运动时长 | |  | distance | number |  | 是 | 运动距离 | |  | calorie | number |  | 是 | 消耗卡路里 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | typeId | number |  | 是 | 运动项目id |
|  | time | number |  | 是 | 运动时长 |
|  | distance | number |  | 是 | 运动距离 |
|  | calorie | number |  | 是 | 消耗卡路里 |

---

### wx.getWeRunData(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/werun/wx.getWeRunData.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| encryptedData | string | 包括敏感数据在内的完整用户信息的加密数据，详细见[加密数据解密算法](../../../framework/open-ability/signature.html)。解密后得到的数据结构见后文 |  |
| iv | string | 加密算法的初始向量，详细见[加密数据解密算法](../../../framework/open-ability/signature.html) |  |
| cloudID | string | 敏感数据对应的云 ID，开通云开发的小程序才会返回，可通过云调用直接获取开放数据，详细见[云调用直接获取开放数据](../../../framework/open-ability/signature.html#method-cloud) | [2.7.0](../../../framework/compatibility.html) |

**开放数据 JSON 结构**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| timestamp | number | 时间戳，表示数据对应的时间 |
| step | number | 微信运动步数 |

---

### wx.requestSubscribeMessage(Object object)

基础库 2.4.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/subscribe-message/wx.requestSubscribeMessage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| tmplIds | Array |  | 是 | 需要订阅的消息模板的id的集合，一次调用最多可订阅5条消息（注意：iOS客户端7.0.6版本、Android客户端7.0.7版本之后的一次性订阅/长期订阅才支持多个模板消息，iOS客户端7.0.5版本、Android客户端7.0.6版本之前的一次订阅只支持一个模板消息）消息模板id在[微信公众平台(mp.weixin.qq.com)-功能-订阅消息]中配置。每个tmplId对应的模板标题需要不相同，否则会被过滤。 |
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
| 10005 | Cannot show subscribe message UI | 无法展示 UI，一般是小程序这个时候退后台了导致的 |
| 20001 | No template data return, verify the template id exist | 没有模板数据，一般是模板 ID 不存在 或者和模板类型不对应 导致的 |
| 20002 | Templates type must be same | 模板消息类型 既有一次性的又有永久的 |
| 20003 | Templates count out of max bounds | 模板消息数量超过上限 |
| 20004 | The main switch is switched off | 用户关闭了主开关，无法进行订阅 |
| 20005 | This mini program was banned from subscribing messages | 小程序被禁封 |
| 20013 | Reject DeviceMsg Template | 不允许通过该接口订阅设备消息 |

---

### wx.requestSubscribeDeviceMessage(Object object)

基础库 2.20.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/subscribe-message/wx.requestSubscribeDeviceMessage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| tmplIds | Array |  | 是 | 需要订阅的消息模板的 id 的集合，一次调用最多可订阅3条消息 |
| sn | String |  | 是 | 设备唯一序列号。由厂商分配，长度不能超过128字节。字符只接受数字，大小写字母，下划线（\_）和连字符（-）。 |
| snTicket | String |  | 是 | 设备票据，5分钟内有效。 |
| modelId | String |  | 是 | 设备型号 id 。通过微信公众平台注册设备获得。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | String | 接口调用成功时errMsg值为'requestSubscribeDeviceMessage:ok' |
| [TEMPLATE\_ID: string] | String | [TEMPLATE\_ID]是动态的键，即模板id，值包括'accept'、'reject'、'ban'、'filter'、'acceptWithAudio'。'accept'表示用户同意订阅该条id对应的模板消息，'reject'表示用户拒绝订阅该条id对应的模板消息，'ban'表示已被后台封禁，'acceptWithAudio' 表示用户接收订阅消息并开启了语音提醒，'filter'表示该模板因为模板标题同名被后台过滤。例如 { errMsg: "requestSubscribeDeviceMessage:ok", zun-LzcQyW-edafCVvzPkK4de2Rllr1fFpw2A\_x0oXE: "accept"} 表示用户同意订阅zun-LzcQyW-edafCVvzPkK4de2Rllr1fFpw2A\_x0oXE这条消息 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | String | 接口调用失败错误信息 |
| errCode | Number | 接口调用失败错误码，有可能为空 |

**错误码**

| errCode | errMsg | 说明 |
| --- | --- | --- |
| 10001 | TmplIds can't be empty | tmplIds 为空 |
| 10004 | Invalid template id | tmplId 参数类型错误 |
| 20001 | No template data return, verify the template id exist | tmplId 为空 |
| 20003 | Templates count out of max bounds | tmplId 数量超过上限 |
| 19720726 | check sn\_ticket fail | snTicket 不合法 |
| 19720727 | sn\_ticket expire | snTicket 过期 |
| 19720728 | err\_not\_found\_tid | tmplId 不存在 |
| 19720736 | template\_id do not match model\_id | modelId 类型与 tmplId 类型不符 |

---

### wx.showRedPackage(Object object)

基础库 2.10.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/redpackage/wx.showRedPackage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| url | string |  | 是 | 封面地址 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.openStoreOrderDetail(Object object)

基础库 3.7.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/store/wx.openStoreOrderDetail.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| orderId | string |  | 是 | 订单id，通过[回调事件](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/cooperation_shop/order_callback.html#%E4%BA%94%E3%80%81%E5%90%88%E4%BD%9C%E8%B4%A6%E5%8F%B7%E5%BA%97%E9%93%BA%E8%AE%A2%E5%8D%95%E9%80%9A%E7%9F%A5%E4%BA%8B%E4%BB%B6)获取 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | message | string | 错误信息 |
|  | code | number | 错误码 |
|  | | 合法值 | 说明 | | --- | --- | | -1 | 系统失败 | | 0 | 成功 | | 1001 | 缺少必要参数 | | 1002 | 网络错误 | | 817323001 | 合作账号订单id不合法 | | 817323002 | 无法获取该订单 | | 817323003 | 当前小程序不是绑定的合作账号 | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 1001 | 缺少必要参数 |
| 1002 | 网络错误 |
| 817323001 | 合作账号订单id不合法 |
| 817323002 | 无法获取该订单 |
| 817323003 | 当前小程序不是绑定的合作账号 |

---

### wx.openStoreCouponDetail(Object object)

基础库 3.8.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/store/wx.openStoreCouponDetail.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| couponId | string |  | 是 | 优惠券id，可以通过[小店后台](https://store.weixin.qq.com/shop/marketing/coupon)获取 |  |
| shopAppid | string |  | 是 | 小店appid，可以通过[小店后台](https://store.weixin.qq.com/shop/setting/home)获取 |  |
| promoterShareLink | string |  | 是 | 推客参数，可以通过[接口](https://developers.weixin.qq.com/doc/store/leagueheadsupplier/API/promotion/content/coupon/getcouponpromotersharelink.html)获取。 | [3.8.11](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| message | string | 错误信息 |
| code | number | 错误码 |

---

### wx.addVideoToFavorites(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/favorites/wx.addVideoToFavorites.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| videoPath | string |  | 是 | 要收藏的视频地址，必须为本地路径或临时路径 |
| thumbPath | string |  | 否 | 缩略图路径，若留空则使用视频首帧 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.addFileToFavorites(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/favorites/wx.addFileToFavorites.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| filePath | string |  | 是 | 要收藏的文件地址，必须为本地路径或临时路径 |
| fileName | string |  | 否 | 自定义文件名，若留空则使用filePath中的文件名 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.requestSubscribeEmployeeMessage(Object object)

基础库 3.10.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/employee-relation/wx.requestSubscribeEmployeeMessage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| tmplIds | Array.<string> |  | 是 | 订阅消息模板id列表，一次最多传入6条；如果传入则会在绑定成功后自动拉起订阅消息列表页面。此处要求传入的的模板消息为未订阅状态。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | bindingStatus | string | 绑定状态 |
|  | | 合法值 | 说明 | | --- | --- | | accept | 已绑定 | | | |
|  | TEMPLATE\_ID | String | [TEMPLATE\_ID]是动态的键，即模板消息id，值包括'accept'、'reject'。'accept'表示用户同意订阅该条id对应的模板消息，'reject'表示用户拒绝订阅该条id对应的模板消息。例如 { zun-LzcQyW-edafCVvzPkK4de2Rllr1fFpw2A\_x0oXE: "accept"} 表示用户同意订阅zun-LzcQyW-edafCVvzPkK4de2Rllr1fFpw2A\_x0oXE这条消息 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| accept | 已绑定 |

---

### wx.checkEmployeeRelation(Object object)

基础库 3.10.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/employee-relation/wx.checkEmployeeRelation.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | bindingStatus | string | 绑定状态 |
|  | | 合法值 | 说明 | | --- | --- | | accept | 已绑定 | | reject | 已拒绝 | | '' | 未绑定且未拒绝 | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| accept | 已绑定 |
| reject | 已拒绝 |
| '' | 未绑定且未拒绝 |

---

### wx.bindEmployeeRelation(Object object)

基础库 3.10.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/employee-relation/wx.bindEmployeeRelation.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| tmplIds | Array.<string> |  | 是 | 订阅消息模板id列表，一次最多传入6条；如果传入则会在绑定成功后自动拉起订阅消息列表页面。此处要求传入的的模板消息为未订阅状态。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | bindingStatus | string | 绑定状态 |
|  | | 合法值 | 说明 | | --- | --- | | accept | 已绑定 | | reject | 已拒绝 | | | |
|  | TEMPLATE\_ID | String | [TEMPLATE\_ID]是动态的键，即模板消息id，值包括'accept'、'reject'。'accept'表示用户同意订阅该条id对应的模板消息，'reject'表示用户拒绝订阅该条id对应的模板消息。例如 { zun-LzcQyW-edafCVvzPkK4de2Rllr1fFpw2A\_x0oXE: "accept"} 表示用户同意订阅zun-LzcQyW-edafCVvzPkK4de2Rllr1fFpw2A\_x0oXE这条消息 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| accept | 已绑定 |
| reject | 已拒绝 |

---

### wx.checkIsAddedToMyMiniProgram(Object object)

基础库 2.29.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/my-miniprogram/wx.checkIsAddedToMyMiniProgram.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/face/wx.requestFacialVerify.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/face/wx.checkIsSupportFacialRecognition.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.chooseLicensePlate(Object object)

基础库 2.19.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/license-plate/wx.chooseLicensePlate.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| plateNumber | string | 用户选择的车牌号 |

---

### wx.reserveChannelsLive(Object object)

基础库 2.19.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.reserveChannelsLive.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.openChannelsUserProfile.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| finderUserName | string |  | 是 | 视频号id（参考格式为：sphcqO59YEPCvoe；查看路径为：微信客户端->我tab->视频号->右上角.-＞视频号名字-视频号ID） |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.openChannelsLiveNoticeInfo(Object object)

基础库 3.13.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.openChannelsLiveNoticeInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| finderUserName | string |  | 是 | 视频号 id，以"sph"开头的id，可在视频号助手获取 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.openChannelsLive(Object object)

基础库 2.15.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.openChannelsLive.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.openChannelsEvent.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.openChannelsActivity.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| finderUserName | string |  | 是 | 视频号 id，以“sph”开头的id，可在视频号助手获取 |
| feedId | string |  | 是 | 视频 feedId |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.getChannelsShareKey(Object object)

基础库 2.22.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.getChannelsShareKey.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | sharerOpenId | string | 分享者 openid |
|  | promoter | Object | 推广员 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | finderNickname | string | 推广员昵称 | |  | promoterId | string | 推广员 id | |  | promoterOpenId | string | 推广员 openid | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | finderNickname | string | 推广员昵称 |
|  | promoterId | string | 推广员 id |
|  | promoterOpenId | string | 推广员 openid |

---

### wx.getChannelsLiveNoticeInfo(Object object)

基础库 2.19.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.getChannelsLiveNoticeInfo.html

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
| otherInfos | Array.<Object> | 除最近的一条预告信息外，其他的预告信息列表（注意：每次最多返回按时间戳增序排列的15个预告信息，其中时间最近的那个预告信息会在接口其他的返回参数中展示，其余的预告信息会在该字段中展示）。 | [2.24.6](../../../framework/compatibility.html) |

---

### wx.getChannelsLiveInfo(Object object)

基础库 2.15.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.getChannelsLiveInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| finderUserName | string |  | 是 | 视频号 id，以“sph”开头的id，可在视频号助手获取 |  |
| startTime | number |  | 否 | 起始时间，筛选指定时间段的直播。若上传了endTime，未上传startTime，则startTime默认为0 | [2.29.0](../../../framework/compatibility.html) |
| endTime | number |  | 否 | 结束时间，筛选指定时间段的直播。若上传了startTime，未上传endTime，则endTime默认取当前时间 | [2.29.0](../../../framework/compatibility.html) |
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
|  | replayStatus | string | 直播回放状态 | [2.29.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 未生成 | | 1 | 已生成 | | 3 | 生成中 | | 6 | 已过期 | | | | |
|  | otherInfos | Array.<Object> | 除最近的一条直播外，其他的直播列表（注意：每次最多返回按时间戳增序排列的15个直播信息，其中时间最近的那个直播会在接口其他的返回参数中展示，其余的直播会在该字段中展示）。 | [2.29.0](../../../framework/compatibility.html) |

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

### wx.requestDeviceVoIP(Object object)

基础库 2.27.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/device-voip/wx.requestDeviceVoIP.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| sn | String |  | 是 | 设备唯一序列号。由厂商分配，长度不能超过128字节。字符只接受数字，大小写字母，下划线（\_）和连字符（-）。 |  |
| snTicket | String |  | 是 | [设备票据](https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/hardware-device/getSnTicket.html)，5分钟内有效。 |  |
| modelId | String |  | 是 | 设备型号 id。通过微信公众平台注册设备获得。 |  |
| deviceName | String |  | 是 | 设备名称，将显示在授权弹窗内（长度不超过13）。授权框中「设备名字」= 「deviceName」 + 「modelId 对应设备型号」。 |  |
| isGroup | Boolean | false | 否 | 是否为授权设备组，默认 false 。 | [2.30.4](../../../framework/compatibility.html) |
| groupId | String |  | 是 | 设备组的唯一标识 id 。isGroup 为 true 时只需要传该参数，isGroup 为 false 时不需要传该参数，但需要传 sn、snTicket、modelId、deviceName 。 | [2.30.4](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### wx.getDeviceVoIPList(Object object)

基础库 2.30.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/device-voip/wx.getDeviceVoIPList.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | list | Array.<Object> |  |
|  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | sn | string | 设备唯一序列号。（仅单台设备时） |  | |  | model\_id | string | 设备型号 id。通过微信公众平台注册设备获得。（仅单台设备时） |  | |  | group\_id | string | 设备组的唯一标识 id（仅设备组时） | [2.30.4](../../../framework/compatibility.html) | |  | status | number | 设备（组）授权状态。0：未授权；1：已授权 |  | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | sn | string | 设备唯一序列号。（仅单台设备时） |  |
|  | model\_id | string | 设备型号 id。通过微信公众平台注册设备获得。（仅单台设备时） |  |
|  | group\_id | string | 设备组的唯一标识 id（仅设备组时） | [2.30.4](../../../framework/compatibility.html) |
|  | status | number | 设备（组）授权状态。0：未授权；1：已授权 |  |

---

### wx.getGroupEnterInfo(Object object)

基础库 2.10.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/group/wx.getGroupEnterInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| allowSingleChat | boolean | false | 否 | 开启后单聊下返回 open\_single\_roomid | [3.7.8](../../../framework/compatibility.html) |
| needGroupOpenID | boolean | false | 否 | 开启后返回用户在群(含单聊)下的 group\_openid | [3.7.8](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| errMsg | string | 错误信息 |  |
| encryptedData | string | 包括敏感数据在内的完整转发信息的加密数据，详细见[加密数据解密算法](../../../framework/open-ability/signature.html) |  |
| iv | string | 加密算法的初始向量，详细见[加密数据解密算法](../../../framework/open-ability/signature.html) |  |
| cloudID | string | 敏感数据对应的云 ID，开通[云开发](../../../wxcloudservice/wxcloud/basis/getting-started.html)的小程序才会返回，可通过云调用直接获取开放数据，详细见[云调用直接获取开放数据](../../../framework/open-ability/signature.html#method-cloud) | [2.7.0](../../../framework/compatibility.html) |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 40097 |  | 场景错误 |
| 65206 |  | 用户已不在该群内 |

---

### wx.requirePrivacyAuthorize(Object object)

基础库 2.32.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/privacy/wx.requirePrivacyAuthorize.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.openPrivacyContract(Object object)

基础库 2.32.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/privacy/wx.openPrivacyContract.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.onNeedPrivacyAuthorization(function listener)

基础库 2.32.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/privacy/wx.onNeedPrivacyAuthorization.html

**Object eventInfo**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| referrer | string | 触发本次 onNeedPrivacyAuthorization 事件的接口或组件名（例如："getUserProfile", "button.getPhoneNumber"） |

**resolve 接口参数**

| 属性 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 用户操作类型 |
| buttonId | string | 是 | 同意授权按钮的id （仅event=agree时必填） |

**event 合法值**

| event | 说明 |
| --- | --- |
| exposureAuthorization | 自定义隐私弹窗曝光 |
| agree | 用户同意隐私授权 |
| disagree | 用户拒绝隐私授权 |

---

### wx.getPrivacySetting(Object object)

基础库 2.32.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/privacy/wx.getPrivacySetting.html

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

基础库 2.19.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/service-chat/wx.openCustomerServiceChat.html

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

### wx.openStickerSetView(Object object)

基础库 3.0.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/sticker/wx.openStickerSetView.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| url | string |  | 是 | 表情专辑链接，可前往[表情开放平台](https://sticker.weixin.qq.com/cgi-bin/mmemoticon-bin/loginpage?t=login/index)，在详情页中的「小程序跳转链接」入口复制 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.openStickerIPView(Object object)

基础库 3.0.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/sticker/wx.openStickerIPView.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| url | string |  | 是 | 表情IP合辑链接，可前往[表情开放平台](https://sticker.weixin.qq.com/cgi-bin/mmemoticon-bin/loginpage?t=login/index)，在详情页中的「小程序跳转链接」入口复制 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.openSingleStickerView(Object object)

基础库 3.0.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/open-api/sticker/wx.openSingleStickerView.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| url | string |  | 是 | 表情链接，可前往[表情开放平台](https://sticker.weixin.qq.com/cgi-bin/mmemoticon-bin/loginpage?t=login/index)，在详情页中的「小程序跳转链接」入口复制 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

<!-- pages: 57 -->
