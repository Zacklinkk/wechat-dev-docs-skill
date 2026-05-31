# 小程序服务端 API 结构化参考 — API/student

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 快速获取学生身份

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/student/api_quickcheckstudentidentity.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户在业务方下的openid 需为已开通接口权限小程序对应的用户openid。 |
| wx\_studentcheck\_code | string | 是 | 用户授权查询code 由授权插件返回，插件可选择不同场景：是否为快速验证。 微信学生身份验证和微信学生身份快速验证需要使用对应场景生成的不同的code。 code有效期两小时 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| bind\_status | number | 绑定状态： 1-未绑定 2-审核中 3-已绑定 |
| is\_student | boolean | 用户学生身份绑定状态说明。true-是学生，false-不是学生 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 40097 | check\_code和openid不匹配；check\_code不存在 |
| 43002 | 非POST方法 |
| 48001 | 无api权限 |
| 61007 | 无api权限 |
| 83400 | check\_code过期 |
| 83401 | 本日该用户信息查询次数已达上限 |
| 83402 | code不匹配，快查接口只能用快查code查询 |

---

<!-- pages: 1 -->
