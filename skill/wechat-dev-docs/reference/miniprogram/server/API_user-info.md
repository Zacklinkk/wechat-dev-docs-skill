# 小程序服务端 API 结构化参考 — API/user-info

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 获取插件用户openpid

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/user-info/basic-info/api_getpluginopenpid.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | string | 是 | 通过 [wx.pluginLogin](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/wx.pluginLogin.html) 获得的插件用户标志凭证 code，有效时间为5分钟，一个 code 只能获取一次 openpid。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| openpid | string | 插件用户的唯一标识。 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok | ok |
| 1000 | 系统错误 |  |
| 1001 | 请求参数非法 |  |
| 1003 | 请求频率过快 |  |
| 1005 | 插件 appid 与数据不匹配 |  |
| 1007 | openpid数据不存在 |  |
| 1022 | json数据解析错误 |  |
| 40016 | invalid button size | 不合法的按钮个数 |
| 45009 | reach max api daily quota limit | 天级别频率限制，2种解决途径2选1: 1.到小程序mp-开发管理-接口设置-调用额度重置;2.调用限频重置API |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 检查加密信息

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/user-info/basic-info/api_checkencrypteddata.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encrypted\_msg\_hash | string | 是 | 加密数据的sha256，通过Hex（Base16）编码后的字符串 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | 错误提示信息 |
| vaild | boolean | 是否是合法的数据 |
| create\_time | number | 加密数据生成的时间戳 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 1 | data not exit | 加密数据不存在，数据生成的时间超过保存的限制（3天）或者 key 不存在，或者数据和appid不匹配 |
| 40097 | invalid args | 参数错误 |
| 44002 | empty post data | POST 的数据包为空。post请求body参数不能为空。 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 支付后获取Unionid

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/user-info/basic-info/api_getpaidunionid.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 支付用户唯一标识 |
| transaction\_id | string | 否 | [微信支付订单号](https://pay.weixin.qq.com/doc/v3/merchant/4012791902) |
| mch\_id | string | 否 | 微信支付分配的[商户号](https://pay.weixin.qq.com/doc/v3/merchant/4012791902)，和商户订单号配合使用 |
| out\_trade\_no | string | 否 | [微信支付商户订单号](https://pay.weixin.qq.com/doc/v3/merchant/4012791902)，和商户号配合使用 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| unionid | string | 用户唯一标识，调用成功后返回 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 0 | ok | ok |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40003 | invalid openid | 不合法的 OpenID ，请开发者确认 OpenID （该用户）是否已关注公众号，或是否是其他公众号的 OpenID |
| 89002 | open not exists | open not exists，该公众号/小程序未绑定微信开放平台帐号。 |
| 89300 | invalid trade | 订单无效 |

---

### 获取用户encryptKey

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/user-info/internet/api_getuserencryptkey.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| openid | string | 是 | 用户的openid |
| signature | string | 是 | 用sessionkey作为密钥对空字符串签名得到的结果。session\_key可通过[code2Session](../../user-login/api_code2session)接口获得。 伪代码：signature = hmac\_sha256(session\_key, "") |
| sig\_method | string | 是 | 签名方法，只支持 hmac\_sha256 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| key\_info\_list | [objarray](#Res__key_info_list<Array>) | 用户最近三次的加密key列表 |

**Res.key_info_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| encrypt\_key | string | 加密key |
| version | number | key的版本号 |
| expire\_in | number | 剩余有效时间 |
| iv | string | 加密iv |
| create\_time | number | 创建key的时间戳 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 87007 | session\_key is not existd or expired | 加密key不存在或已过期 |
| 87008 | invalid sig\_method | 无效的签名方法 |
| 87009 | invalid signature | 无效的签名 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取手机号

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/user-info/phone-number/api_getphonenumber.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | string | 是 | [手机号获取凭证](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/getPhoneNumber.html) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| phone\_info | [object](#Res__phone_info) | 用户手机号信息 |

**Res.phone_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| phoneNumber | string | 用户绑定的手机号（国外手机号会有区号） |
| purePhoneNumber | string | 没有区号的手机号 |
| countryCode | string | 区号 |
| watermark | [object](#Res__phone_info__watermark) | 数据水印 |

**Res.phone_info.watermark Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| timestamp | number | 用户获取手机号操作的时间戳 |
| appid | string | 小程序appid |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40013 | invalid appid | 请求appid身份与获取code的小程序appid不匹配 |
| 40029 | code 无效 | js\_code无效 |
| 45011 | api minute-quota reach limit  mustslower  retry next minute | API 调用太频繁，请稍候再试 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

<!-- pages: 5 -->
