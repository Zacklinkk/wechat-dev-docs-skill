# 小程序服务端 API 结构化参考 — API/user-login

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 小程序登录凭证校验

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/user-login/api_code2session.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appid | string | 是 | 小程序 appId |
| secret | string | 是 | 小程序 appSecret |
| js\_code | string | 是 | 登录时获取的 code，可通过[wx.login](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/wx.login.html)获取 |
| grant\_type | string | 是 | 授权类型，此处只需填写 authorization\_code |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| session\_key | string | 会话密钥 |
| unionid | string | 用户在开放平台的唯一标识符，若当前小程序已绑定到微信开放平台帐号下会返回，详见 [UnionID 机制说明](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/union-id.html)。 |
| openid | string | 用户唯一标识 |
| errcode | number | 错误码，请求失败时返回 |
| errmsg | string | 错误信息，请求失败时返回 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40029 | code 无效 | js\_code无效 |
| 40226 | code blocked | 高风险等级用户，小程序登录拦截 。风险等级详见[用户安全解方案](https://developers.weixin.qq.com/miniprogram/dev/framework/operation.html) |
| 45011 | api minute-quota reach limit  mustslower  retry next minute | API 调用太频繁，请稍候再试 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 检验登录态

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/user-login/api_checksessionkey.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户唯一标识符 |
| signature | string | 是 | 用户登录态签名，用session\_key对空字符串签名得到的结果。即 signature = hmac\_sha256(session\_key, "") |
| sig\_method | string | 是 | 用户登录态签名的哈希方法，目前只支持 hmac\_sha256 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok | ok |
| 87009 | invalid signature | 无效的签名 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 重置登录态

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/user-login/api_resetusersessionkey.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户唯一标识符 |
| signature | string | 是 | 用户登录态签名，用session\_key对空字符串签名得到的结果。即 signature = hmac\_sha256(session\_key, "") |
| sig\_method | string | 是 | 用户登录态签名的哈希方法，目前只支持 hmac\_sha256 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| openid | string | 用户唯一标识符 |
| session\_key | string | 重置后的用户登录态 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40097 | invalid args | 参数错误 |
| 45011 | api minute-quota reach limit  mustslower  retry next minute | API 调用太频繁，请稍候再试 |
| 87007 | session\_key is not existd or expired |  |
| 87008 | invalid sig\_method |  |
| 87009 | invalid signature | 无效的签名 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

<!-- pages: 3 -->
