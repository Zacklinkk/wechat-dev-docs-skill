# 小程序服务端 API 结构化参考 — API/mp-message-management

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 创建activity_id

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/updatable-message/api_createactivityid.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| unionid | string | 否 | 为私密消息创建activity\_id时，指定分享者为unionid用户。其余用户不能用此activity\_id分享私密消息。 **openid与unionid填一个即可。**私密消息暂不支持云函数生成activity id。 |
| openid | string | 否 | 为私密消息创建activity\_id时，指定分享者为openid用户。其余用户不能用此activity\_id分享私密消息。**openid与unionid填一个即可。** 私密消息暂不支持云函数生成activity id。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| activity\_id | string | 动态消息的 ID |
| expiration\_time | number | activity\_id 的过期时间戳。默认24小时后过期。 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 修改动态消息

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/updatable-message/api_setupdatablemsg.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| activity\_id | string | 是 | 动态消息的 ID，通过 createActivityId 接口获取 | - |
| target\_state | number | 是 | 动态消息修改后的状态 | [枚举值](#Enum_Body__target_state) |
| template\_info | [object](#Body__template_info) | 是 | 动态消息对应的模板信息 | - |

**Body.template_info Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter\_list | [objarray](#Body__template_info__parameter_list<Array>) | 是 | 模板中需要修改的参数 |

**Body.template_info.parameter_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 要修改的参数名，见下文其他说明 |
| value | string | 是 | 修改后的参数值 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**Body.target_state Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 未开始 |
| 1 | 已开始 |

**name 的合法值**

| 值 | 说明 |
| --- | --- |
| member\_count | target\_state = 0 时必填，文字内容模板中 member\_count 的值 |
| room\_limit | target\_state = 0 时必填，文字内容模板中 room\_limit 的值 |
| path | target\_state = 1 时必填，点击「进入」启动小程序时使用的路径。对于小游戏，没有页面的概念，可以用于传递查询字符串（query），如 "?foo=bar" |
| version\_type | target\_state = 1 时必填，点击「进入」启动小程序时使用的版本。有效参数值为：develop（开发版），trial（体验版），release（正式版） |

**消息状态**

| 状态 | 文字内容 | 颜色 | 允许转移的状 |
| --- | --- | --- | --- |
| 0 | "成员正在加入，当前 {member\_count}/{room\_limit} 人" | #FA9D39 | 0, 1 |
| 1 | "已开始" | #CCCCCC | 无 |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 44002 | empty post data | POST 的数据包为空 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 47501 | activity\_id error | 参数 activity\_id 错误 |
| 47502 | target\_state error | 参数 target\_state 错误 |
| 47503 | version\_type error | 参数 version\_type 错误，调整后重试 |
| 47504 | activity\_id expired time | activity\_id 过期 |

**8. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 修改小程序聊天工具的动态卡片消息

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/updatable-message/api_setchattoolmsg.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| activity\_id | string | 是 | 动态消息的 ID，通过 [createActivityId](api_createactivityid) 接口获取 |
| target\_state | number | 是 | 动态消息修改后的状态 |
| template\_id | string | 是 | 模板id |
| participator\_info\_list | [objarray](#Body__participator_info_list<Array>) | 否 | 更新后的聊天室成员状态 |
| version\_type | number | 是 | 0 正式版 1 开发版 2 体验版 |

**Body.participator_info_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| group\_openid | string | 是 | 聊天室用户的GroupOpenID，仅允许传入动态卡片所在聊天室内的GroupOpenID |
| state | number | 是 | 用户对卡片事件的完成状态。0：未完成（初始状态），1：已完成。目前只支持设置为 1 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40013 | appid不正确，或者不符合绑定关系要求 |  |
| 40097 | invalid args | 参数错误 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 44002 | empty post data | POST 的数据包为空。post请求body参数不能为空。 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;参数需以 JSON 字符串格式写在post请求的 body 中，请检查修正后重试 |
| 47501 | activity\_id error | 参数 activity\_id 错误 |
| 47502 | target\_state error | 参数 target\_state 错误 |
| 47504 | activity\_id expired time | activity\_id 过期 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 删除模板

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/subscribe-message/api_delwxanewtemplate.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| priTmplId | string | 是 | 要删除的模板id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 20001 | 系统错误 |  |
| 20002 | 参数错误 |  |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 200001 | 系统错误 | 请稍后再试 |
| 200002 |  | 入参错误 |
| 200014 | 模版 tid 参数错误 |  |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | 仅认证 | 仅认证 | ✔ |

---

### 获取类目

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/subscribe-message/api_getcategory.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| data | [objarray](#Res__data<Array>) | 类目列表 |

**Res.data(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | number | 类目id，查询公共模板库时需要 |
| name | string | 类目的中文名 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 404 | 404 not found | 请检查调用方法是否有误[get|post] |
| 20001 | 系统错误 | 请稍后重试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 200100 | 账号类型不合法 | 请使用小程序账号调用 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | 仅认证 | 仅认证 | ✔ |

---

### 获取模板中的关键词

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/subscribe-message/api_getpubnewtemplatekeywords.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| tid | string | 是 | 模板标题 id，可通过接口获取 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| count | number | 模版标题列表总数 |
| data | [objarray](#Res__data<Array>) | 关键词列表 |

**Res.data(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| kid | number | 关键词 id，选用模板时需要 |
| name | string | 关键词内容 |
| example | string | 关键词内容对应的示例 |
| rule | string | 参数类型 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 20001 | 系统错误 |  |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 200002 | 入参错误 |  |
| 200014 | 模板 tid 参数错误 |  |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | 仅认证 | 仅认证 | ✔ |

---

### 获取类目下的公共模板

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/subscribe-message/api_getpubnewtemplatetitles.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| ids | string | 是 | 类目 id，多个用逗号隔开 |
| start | number | 是 | 用于分页，表示从 start 开始。从 0 开始计数 |
| limit | number | 是 | 用于分页，表示拉取 limit 条记录。最大为 30 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| count | number | 模版标题列表总数 |
| data | [objarray](#Res__data<Array>) | 模板标题列表 |

**Res.data(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| tid | number | 模版标题 id |
| title | string | 模版标题 |
| type | number | 模版类型，2 为一次性订阅，3 为长期订阅 |
| categoryId | number | 模版所属类目 id |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 404 | 404 not found | 请检查调用方法是否有误[get|post] |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 200001 | 系统错误 | 请稍后再试 |
| 200016 | start 参数错误 |  |
| 200017 | limit 参数错误 |  |
| 200018 | 类目 ids 缺失 |  |
| 200019 | 类目 ids 不合法 |  |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | 仅认证 | 仅认证 | ✔ |

---

### 获取已有模板列表

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/subscribe-message/api_getwxapubnewtemplate.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| data | [objarray](#Res__data<Array>) | 模板列表 |

**Res.data(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| priTmplId | string | 添加至帐号下的模板 id，发送小程序订阅消息时所需 |
| title | string | 模版标题 |
| content | string | 模版内容 |
| example | string | 模板内容示例 |
| type | number | 模版类型，2 为一次性订阅，3 为长期订阅 |
| keywordEnumValueList | [objarray](#Res__data<Array>__keywordEnumValueList<Array>) | 枚举参数值范围 |

**Res.data(Array).keywordEnumValueListObject Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| keywordCode | string | 枚举参数的 key |
| enumValueList | array | 枚举参数值范围列表 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 404 | 404 not found | 请检查调用方法是否有误[get|post] |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 200100 | 账号类型不合法 | 请使用小程序账号调用 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | 仅认证 | 仅认证 | ✔ |

---

### 发送订阅消息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/subscribe-message/api_sendmessage.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| template\_id | string | 是 | 所需下发的订阅模板id |
| page | string | 否 | 点击模板卡片后的跳转页面，仅限本小程序内的页面。支持带参数,（示例index?foo=bar）。该字段不填则模板无跳转 |
| touser | string | 是 | 接收者（用户）的 openid |
| data | [object](#Body__data) | 是 | 模板内容，格式形如{ "phrase3": { "value": "审核通过" }, "name1": { "value": "订阅" }, "date2": { "value": "2019-12-25 09:42" } } |
| miniprogram\_state | string | 是 | 跳转小程序类型：developer为开发版；trial为体验版；formal为正式版；默认为正式版 |
| lang | string | 是 | 进入小程序查看”的语言类型，支持zh\_CN(简体中文)、en\_US(英文)、zh\_HK(繁体中文)、zh\_TW(繁体中文)，默认为zh\_CN |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**4. 注意事项**

| 参数类别 | 参数说明 | 参数值限制 | 说明 |
| --- | --- | --- | --- |
| thing.DATA | 事物 | 20个以内字符 | 可汉字、数字、字母或符号组合 |
| number.DATA | 数字 | 32位以内数字 | 只能数字，可带小数 |
| letter.DATA | 字母 | 32位以内字母 | 只能字母 |
| symbol.DATA | 符号 | 5位以内符号 | 只能符号 |
| character\_string.DATA | 字符串 | 32位以内数字、字母或符号 | 可数字、字母或符号组合 |
| time.DATA | 时间 | 24小时制时间格式（支持+年月日），支持填时间段，两个时间点之间用“~”符号连接 | 例如：15:01，或：2019年10月1日 15:01 |
| date.DATA | 日期 | 年月日格式（支持+24小时制时间），支持填时间段，两个时间点之间用“~”符号连接 | 例如：2019年10月1日，或：2019年10月1日 15:01 |
| amount.DATA | 金额 | 1个币种符号+10位以内纯数字，可带小数，结尾可带“元” | 可带小数 |
| phone\_number.DATA | 电话 | 17位以内，数字、符号 | 电话号码，例：+86-0766-66888866 |
| car\_number.DATA | 车牌 | 8位以内，第一位与最后一位可为汉字，其余为字母或数字 | 车牌号码：粤A8Z888挂 |
| name.DATA | 姓名 | 10个以内纯汉字或20个以内纯字母或符号 | 中文名10个汉字内；纯英文名20个字母内；中文和字母混合按中文名算，10个字内 |
| phrase.DATA | 汉字 | 5个以内汉字 | 5个以内纯汉字，例如：配送中 |
| enum.DATA | 枚举值 | 只能上传枚举值范围内的字段值 | [调用接口获取参考枚举值](api_getwxapubnewtemplate) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40003 | invalid openid | 不合法的 OpenID ，请开发者确认 OpenID （该用户）是否已关注公众号，或是否是其他公众号的 OpenID |
| 40014 | invalid access\_token | 不合法的 access\_token ，请开发者认真比对 access\_token 的有效性（如是否过期），或查看是否正在为恰当的公众号调用接口 |
| 40037 | invalid template\_id | 不合法的 template\_id |
| 43101 | 用户未订阅消息 | 检查订阅弹窗回调结果或事件推送确认是否订阅成功，检查是否一次性订阅的次数之前已下发完 |
| 43107 | 订阅消息能力封禁 | 检查账号是否被封禁订阅消息能力，检查模板id对应的模板是否被封禁 |
| 43108 | 并发下发消息给同一个粉丝 | 检查是否有同时下发多个消息给同一粉丝的情况 |
| 45168 | 命中敏感词 | 检查下发消息中是否带有敏感词 |
| 47003 | 参数错误 | 根据wiki文档检查data结构格式是否正确，检查各个关键词是否满足对应规则 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 选用模板

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/subscribe-message/api_addwxanewtemplate.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tid | string | 是 | 模板标题 id，可通过接口获取，也可登录小程序后台查看获取 |
| kidList | numarray | 是 | 开发者自行组合好的模板关键词列表，关键词顺序可以自由搭配（例如 [3,5,4] 或 [4,5,3]），最多支持5个，最少2个关键词组合 |
| sceneDesc | string | 是 | 服务场景描述，15个字以内 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| priTmplId | string | 添加至帐号下的模板id，发送小程序订阅消息时所需 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40400 | HTTP报文不符合规范（HTTP Bad Request） | 开发者修复 |
| 200001 | 系统错误 | 请稍后再试 |
| 200011 | 此账号已被封禁 | 前往公众平台查看站内信了解封禁原因并按照站内信通知进行处理 |
| 200012 | 私有模板数已达上限 | 删除已有的私有模版后可添加 |
| 200013 | 此模版已被封禁 | 前往公众平台查看站内信了解封禁原因并按照站内信通知进行处理 |
| 200014 | 模版 tid 参数错误 | 请检查tid是否为空值以及该tid是否存在 |
| 200020 | 关键词列表 kidList 参数错误 | kidList中的关键词不存在，请使用已有的关键词或者申请新的关键词 |
| 200021 | 场景描述 sceneDesc 参数错误 | 请检查sceneDesc是否为空值以及格式是否合法 |
| 200022 | 相同标题和关键字的模板已存在 | 更换标题和关键字重试 |
| 200100 | 账号类型不合法 | 请使用小程序账号调用 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | 仅认证 | 仅认证 | ✔ |

---

### 激活与更新服务卡片

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/subscribe-message/api_setusernotify.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户身份标识符。 当使用微信支付订单号作为 code 时，需要与实际支付用户一致；当通过前端获取 code 时，需要与点击 button 的用户一致。 |
| notify\_type | number | 是 | 卡片id。可在[文中](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/subscribe-message-2.html)（1.1）中查阅。 |
| notify\_code | string | 是 | 动态更新令牌。获取方式可在[文中](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/subscribe-message-2.html)（1.3或1.4）中查阅。 需要注意的是，微信支付订单号从生成到可被校验存在一定的时延可能，若收到报错为 notify\_code 不存在，建议在1分钟后重试。 |
| content\_json | string | 是 | 卡片状态与状态相关字段，不同卡片的定义不同，可在[文中](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/subscribe-message-2.html)（1.1中各模版定义链接）中查阅。 |
| check\_json | string | 否 | 微信支付订单号验证字段。 当将微信支付订单号作为 notify\_code 时，在激活时需要传入。见下文其他说明check\_json定义 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**check_json定义**

| 参数 | 是否必填 | 类型 | 说明 | 格式要求 |
| --- | --- | --- | --- | --- |
| pay\_amount | 是 | uint32 | 订单支付金额。若订单有优惠，支持传入下单金额或实际支付金额。若为合单支付的子订单号，可传入子单的下单金额、子单的实际支付金额、合单的下单金额或合单的实际支付金额。 | 单位为 |
| pay\_time | 是 | uint32 | 支付时间 | 秒级时间戳 |
| pay\_channel | 否 | uint32 | 订单渠道，0：普通微信支付，1001：支付分 |  |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40003 | invalid openid | 不合法的 OpenID ，请开发者确认 OpenID 的有效性 |
| 85431 | system error | 系统繁忙，稍后重试 |
| 85433 | invalid check\_json | check\_json 参数不合法 |
| 85434 | invalid notify\_type | notify\_type 参数不合法 |
| 85435 | invalid content\_json | content\_json 参数不合法 |
| 85436 | notify\_code abnormal | notify\_code 异常（被封禁） |
| 85437 | invalid notify\_code | notify\_code 不存在 |
| 85438 | notify\_code expired | notify\_code 已过期 |
| 85439 | content\_json with wrong status | content\_json 状态不合法 |
| 85440 | content\_json lack need field | content\_json 缺少字段 |
| 85441 | content\_json has unformat field | content\_json 字段格式不对 |
| 85442 | content\_json blocked by securiy audit | content\_json 包含审核不通过信息 |
| 85443 | content\_json has illegal utf8 char | content\_json 包含非utf8字符 |
| 85448 | notify\_code has used | notify\_code 已经推送过 |
| 85449 | notify\_code is dealing and locked, retry later | notify\_code 正在更新，已加锁，稍后重试 |
| 85461 | notify\_type access deny | notify\_type 准入驳回 |
| 85462 | app aceess deny | 小程序准入驳回 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 更新服务卡片扩展信息

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/subscribe-message/api_setusernotifyext.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户身份标识符。 当使用微信支付订单号作为 code 时，需要与实际支付用户一致；当通过前端获取 code 时，需要与点击 button 的用户一致。 |
| notify\_type | number | 是 | 卡片id。可在[文中](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/subscribe-message-2.html)（1.1）中查阅。 |
| notify\_code | string | 是 | 动态更新令牌。获取方式可在[文中](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/subscribe-message-2.html)（1.3或1.4）中查阅。 需要注意的是，微信支付订单号从生成到可被校验存在一定的时延可能，若收到报错为 notify\_code 不存在，建议在1分钟后重试。 |
| ext\_json | string | 是 | 扩展信息，不同卡片的定义不同，可在[文中](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/subscribe-message-2.html)（1.1中各模版定义链接）中查阅。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40003 | invalid openid | 不合法的 OpenID ，请开发者确认 OpenID 的有效性 |
| 85431 | system error | 系统繁忙，稍后重试 |
| 85434 | invalid notify\_type | notify\_type 参数不合法 |
| 85436 | notify\_code abnormal | notify\_code 异常（被封禁） |
| 85437 | invalid notify\_code | notify\_code 不存在 |
| 85444 | pay\_info check fail | pay\_info 校验不通过 |
| 85445 | store\_info check fail | store\_info 校验不通过 |
| 85446 | shipping\_list check fail | shipping\_list 校验不通过 |
| 85447 | product\_list check fail | product\_list 校验不通过 |
| 85461 | notify\_type access deny | notify\_type 准入驳回 |
| 85462 | app aceess deny | 小程序准入驳回 |
| 85470 | invalid ext\_json | ext\_json 参数不合法 |
| 85471 | ext\_json has illegal utf8 char | ext\_json 包含非utf8字符 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 查询服务卡片状态

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/subscribe-message/api_getusernotify.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户身份标识符 |
| notify\_code | string | 是 | 动态更新令牌 |
| notify\_type | number | 是 | 卡片id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| notify\_info | [object](#Res__notify_info) | 卡片状态 |

**Res.notify_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| notify\_type | number | 卡片id |
| content\_json | string | 上次有效推送的卡片状态与状态相关字段，没推送过为空字符串。 |
| code\_state | number | code 状态：0 正常；1 有风险；2 异常；10 用户拒收本次code |
| code\_expire\_time | number | code 过期时间，秒级时间戳。 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40003 | invalid openid | 不合法的 OpenID ，请开发者确认 OpenID 的有效性 |
| 85431 | system error | 系统繁忙，稍后重试 |
| 85434 | invalid notify\_type | notify\_type 参数不合法 |
| 85437 | invalid notify\_code | notify\_code 不存在 |
| 85438 | notify\_code expired | notify\_code 已过期 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

<!-- pages: 13 -->
