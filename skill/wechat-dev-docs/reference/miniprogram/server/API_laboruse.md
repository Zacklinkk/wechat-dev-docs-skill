# 小程序服务端 API 结构化参考 — API/laboruse

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 推送用工消息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/laboruse/api_sendemployeerelationmsg.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| template\_id | string | 是 | bV8Jk-XXXXXX | 消息模版id |
| page | string | 是 | page/XXX | 跳转路径 |
| touser | string | 是 | oL7T268t3zlOb64IvrN64-XXXXXX | 被推送用户openid |
| data | string | 是 | {\"data\":{\"character\_string1\":{\"value\":\"aaa\"},\"amount1\":{\"value\":\"222\"}}} | 消息内容 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40097 | invalid args | 参数错误 |
| 40256 | invalid employee relation | 向非绑定用工关系的用户推送消息 |
| 40257 | decode touser error | 解析接收用户openid错误 |
| 43104 | this app does not have poermission | app无权限推送模版消息 |
| 50001 | user unauthorized | 用户未订阅模版 |

---

### 解绑用工关系

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/laboruse/api_unbinduserb2cauthinfo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| openid\_list | array | 是 | ["oL7T268t3zlOb64IvrN64-XXXXXX"，"oL7T268t3zlOb64IvrN64-YYYYYY"] | 被解绑用户的openid列表 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40003 | invalid openid | 不合法的 OpenID ，请开发者确认 OpenID 的有效性 |
| 40097 | invalid args | 参数错误 |

---

<!-- pages: 2 -->
