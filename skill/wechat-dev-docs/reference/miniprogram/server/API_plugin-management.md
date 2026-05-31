# 小程序服务端 API 结构化参考 — API/plugin-management

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 插件申请管理

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/plugin-management/api_managepluginapplication.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | string | 是 | dev\_agree表示同意申请、dev\_refuse表示拒绝申请、dev\_delete表示删除已拒绝的申请者、dev\_apply\_list表示获取当前所有插件使用方信息 |
| appid | string | 否 | action为"dev\_agree"时填写，使用者的 appid，同意申请时填写。 |
| page | number | 否 | action为"dev\_apply\_list"时填写，要拉取第几页的数据 |
| num | number | 否 | action为"dev\_apply\_list"时填写，每页的记录数 |
| reason | string | 否 | action为"dev\_refuse"时填写，拒绝理由。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| apply\_list | [objarray](#Res__apply_list<Array>) | 插件使用方列表，action为"dev\_apply\_list"时返回 |

**Res.apply_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| appid | string | 使用者的appid |
| status | number | 插件状态 |
| nickname | string | 使用者的昵称 |
| headimgurl | string | 使用者的头像 |
| reason | string | 使用者的申请说明 |
| apply\_url | string | 使用者的小程序码 |
| create\_time | string | 使用者的申请时间 |
| categories | [objarray](#Res__apply_list<Array>__categories<Array>) | 使用者的类目 |

**Res.apply_list(Array).categoriesObject Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| first | string | 一级类目名称 |
| second | string | 二级类目名称 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 插件管理

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/plugin-management/api_manageplugin.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | string | 是 | action可取值为"list"、"apply"、 "unbind"、"update"，分别表示“查询已添加的插件列表”、“申请使用插件”、“删除已添加的插件”、“快速更新插件版本号” |
| plugin\_appid | string | 是 | 插件的 appid |
| reason | string | 否 | 当action是"apply"时必填，申请原因 |
| user\_version | string | 否 | 当action是"update"时使用。升级至版本号，要求此插件版本支持快速更新 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| plugin\_list | [objarray](#Res__plugin_list<Array>) | 申请或使用中的插件信息列表，当 action == 'list' 时返回 |

**Res.plugin_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| appid | string | 插件 appId |
| status | number | 插件状态。1表示申请中；2表示申请通过；3表示被拒绝；4表示申请已超时 |
| nickname | string | 插件昵称 |
| headimgurl | string | 插件头像 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 80067 |  | 找不到使用的插件 |

---

<!-- pages: 2 -->
