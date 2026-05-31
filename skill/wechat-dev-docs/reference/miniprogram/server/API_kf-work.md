# 小程序服务端 API 结构化参考 — API/kf-work

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 查询绑定情况

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-work/api_getkfworkbound.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| entityName | string | 该小程序的主体名称，未绑定时不返回 |
| corpid | string | 企业ID，未绑定时不返回 |
| bindTime | number | 绑定时间戳（单位：秒），未绑定时不返回 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok | ok |
| 10130030 | 小程序账号无权限 | 须为非个人主体的小程序 |

---

### 绑定微信客服

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-work/api_bindkfwork.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| corpid | string | 是 | 企业ID，获取方式参考：[术语说明-corpid](https://developer.work.weixin.qq.com/document/path/90665#corpid)。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok | ok |
| 10130002 | 参数错误 | 检查参数 |
| 10130030 | 小程序账号无权限 | 须为非个人主体的小程序 |
| 10130600 | corpid不合法 | 检查corpid |
| 10130601 | corpid不合法 | 检查corpid |
| 10130602 | corpid与小程序实体名称不一致 | 检查corpid |
| 10130603 | 已经绑定 | 请解绑后重试 |

---

### 解除绑定微信客服

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-work/api_unbindkfwork.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| corpid | string | 是 | 企业ID，获取方式参考：[术语说明-corpid](https://developer.work.weixin.qq.com/document/path/90665#corpid)。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok | ok |
| 10130002 | 参数错误 | 检查参数 |
| 10130600 | corpid不合法 | 检查corpid |
| 10130601 | corpid不合法 | 检查corpid |
| 10130602 | corpid与小程序实体名称不一致 | 检查corpid |
| 10130604 | 尚未绑定 | 无需解绑 |

---

<!-- pages: 3 -->
