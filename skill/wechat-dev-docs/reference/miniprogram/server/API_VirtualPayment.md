# 小程序服务端 API 结构化参考 — API/VirtualPayment

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 查询代币余额

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_query_user_balance.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| signature | string | 是 | - | 用户态签名 |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户的openid |
| env | number | 是 | 0-正式环境 1-沙箱环境 |
| user\_ip | string | 是 | 用户ip，例如:1.1.1.1 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| balance | number | 代币总余额，包括有价和赠送部分 |
| present\_balance | number | 赠送账户的代币余额 |
| sum\_save | number | 累计有价货币充值数量 |
| sum\_present | number | 累计赠送无价货币数量 |
| sum\_balance | number | 历史总增加的代币金额 |
| sum\_cost | number | 历史总消耗代币金额 |
| first\_save\_flag | boolean | 是否满足首充活动标记。0:不满足。1:满足 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 扣减代币

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_currency_pay.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| signature | string | 是 | - | 用户态签名 |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 否 | 用户的openid |
| env | number | 否 | 0-正式环境 1-沙箱环境 |
| user\_ip | string | 否 | 用户ip，例如:1.1.1.1 |
| amount | number | 否 | 支付的代币数量 |
| order\_id | string | 否 | 订单号 |
| payitem | string | 否 | 物品信息。记录到账户流水中。如:[{"productid":"物品id", "unit\_price": 单价, "quantity": 数量}] |
| remark | string | 否 | 备注 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| order\_id | string | 订单号 |
| balance | number | 总余额，包括有价和赠送部分 |
| used\_present\_amount | number | 使用赠送部分的代币数量 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 查询创建的订单

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_query_order.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户的openid |
| env | number | 是 | 0-正式环境 1-沙箱环境 |
| order\_id | string | 否 | 创建的订单号 |
| wx\_order\_id | string | 否 | 微信内部单号(与order\_id二选一) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| order | [object](#Res__order) | 订单信息 |

**Res.order Object Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| order\_id | string | 订单号 | - |
| create\_time | number | 创建时间 | - |
| update\_time | number | 更新时间 | - |
| status | number | 当前状态 | [枚举值](#Enum_Res__order__status) |
| biz\_type | number | 业务类型0-短剧 | - |
| order\_fee | number | 订单金额，单位分 | - |
| coupon\_fee | number | 订单优惠金额，单位分(暂无此字段) | - |
| paid\_fee | number | 用户支付金额 | - |
| order\_type | number | 订单类型 | [枚举值](#Enum_Res__order__order_type) |
| refund\_fee | number | 当类型为退款单时表示退款金额，单位分 | - |
| paid\_time | number | 支付/退款时间，unix秒级时间戳 | - |
| provide\_time | number | 发货时间 | - |
| biz\_meta | string | 订单创建时传的信息 | - |
| env\_type | number | 环境类型1-现网 2-沙箱 | - |
| token | string | 下单时米大师返回的token | - |
| left\_fee | number | 支付单类型时表示此单经过退款还剩余的金额，单位分 | - |
| wx\_order\_id | string | 微信内部单号 | - |
| channel\_order\_id | string | 渠道单号，为用户微信支付详情页面上的商户单号 | - |
| wxpay\_order\_id | string | 微信支付交易单号，为用户微信支付详情页面上的交易单号 | - |
| sett\_time | number | 结算时间的秒级时间戳，大于0表示结算成功 | - |
| sett\_state | number | 结算状态0-未开始结算 1-结算中 2-结算成功 3-待结算（与0相同） | - |
| platform\_fee\_fen | number | 虚拟支付技术服务费，单位为分；sett\_state = 2时返回 | - |
| cps\_fee\_fen | number | 公众号、视频号平台的cps服务费，单位为分；sett\_state = 2时返回 | - |

**Res.order.status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 订单初始化（未创建成功，不可用于支付） |
| 1 | 订单创建成功 |
| 2 | 订单已经支付，待发货 |
| 3 | 订单发货中 |
| 4 | 订单已发货 |
| 5 | 订单已经退款 |
| 6 | 订单已经关闭（不可再使用） |
| 7 | 订单退款失败 |
| 8 | 用户退款完成 |
| 9 | 回收广告金完成 |
| 10 | 分账回退完成 |

**Res.order.order_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 普通虚拟支付 |
| 1 | 普通退款 |
| 7 | 苹果iOS支付 |
| 8 | 苹果iOS退款 |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 代币支付退款

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_cancel_currency_pay.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| signature | string | 是 | - | 用户态签名 |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户的openid |
| env | number | 是 | 0-正式环境 1-沙箱环境 |
| user\_ip | string | 是 | 用户ip，例如1.1.1.1 |
| pay\_order\_id | string | 是 | 代币支付(调用currency\_pay接口时)时传的order\_id |
| order\_id | string | 是 | 本次退款单的单号 |
| amount | number | 是 | 退款金额 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| order\_id | string | 退款订单号 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 通知已发货完成

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_notify_provide_goods.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| order\_id | string | 是 | 下单时传的单号 |
| wx\_order\_id | string | 是 | 微信内部单号(与order\_id二选一) |
| env | number | 是 | 0-正式环境 1-沙箱环境 |

---

### 代币赠送

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_present_currency.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户的openid |
| env | number | 是 | 0-正式环境 1-沙箱环境 |
| order\_id | string | 是 | 赠送单号 |
| amount | number | 是 | 赠送金额 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| balance | number | 赠送后用户的代币余额 |
| order\_id | string | 赠送单号 |
| present\_balance | number | 用户收到的总赠送金额 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 下载小程序账单

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_download_bill.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin\_ds | number | 是 | 起始时间（如20230801） |
| end\_ds | number | 是 | 截止时间（如20230810） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| url | string | 下载地址（有效时间为半小时，失效后需重新获取） |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 启动订单退款任务

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_refund_order.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 下单时的用户openid |
| order\_id | string | 否 | 下单时的单号，即jsapi接口传入的OutTradeNo，与wx\_order\_id字段二选一 |
| wx\_order\_id | string | 否 | 支付单对应的微信侧单号，与order\_id字段二选一 |
| refund\_order\_id | string | 是 | 本次退款时需要传的单号，长度为[8,32]，字符只允许使用字母、数字、'\\_'、'-' |
| left\_fee | number | 是 | 当前单剩余可退金额，单位分，可以通过调用query\_order接口查到 |
| refund\_fee | number | 是 | 本次退款金额，单位分，需要(0,left\_fee] |
| biz\_meta | string | 是 | 商家自定义数据，传入后可在query\_order接口查询时原样返回，长度需要[0,1024] |
| refund\_reason | string | 是 | 退款原因，当前仅支持以下值 0-暂无描述 1-产品问题，影响使用或效果不佳 2-售后问题，无法满足需求 3-意愿问题，用户主动退款 4-价格问题 5:其他原因 |
| req\_from | string | 是 | 退款来源，当前仅支持以下值 1-人工客服退款，即用户电话给客服，由客服发起退款流程 2-用户自己发起退款流程 3-其它 |
| env | number | 是 | 0-正式环境 1-沙箱环境 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| refund\_order\_id | string | 退款单号 |
| refund\_wx\_order\_id | string | 退款单的微信侧单号 |
| pay\_order\_id | string | 该退款单对应的支付单单号 |
| pay\_wx\_order\_id | string | 该退款单对应的支付单微信侧单号 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 创建提现单

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_create_withdraw_order.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| withdraw\_no | string | 是 | 提现单单号，长度为[8,32]，字符只允许使用字母、数字、'\\_'、'-' |
| withdraw\_amount | string | 是 | 提现的金额，单位元，例如提现1分钱请使用0.01，允许不传，不传的情况下表示全额提现 |
| env | number | 是 | 0-正式环境 1-沙箱环境 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| withdraw\_no | string | 提现单号 |
| wx\_withdraw\_no | string | 提现单的微信侧单号 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 查询提现单

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_query_withdraw_order.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| withdraw\_no | string | 是 | 提现单单号 |
| env | number | 是 | 0-正式环境 1-沙箱环境 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| withdraw\_no | string | 提现单号 |
| status | number | 提现状态，1-创建成功，提现中 2-提现成功 3-提现失败 |
| withdraw\_amount | string | 提现金额 |
| wx\_withdraw\_no | string | 提现单的微信侧单号 |
| withdraw\_success\_timestamp | string | 提现单成功的秒级时间戳 |
| create\_time | string | 提现单创建时间 |
| fail\_reason | string | 提现失败的原因 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 批量上传道具

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_start_upload_goods.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| upload\_item | [objarray](#Body__upload_item<Array>) | 是 | 上传的商品列表 |
| env | number | 是 | 0-正式环境 1-沙箱环境 |

**Body.upload_item(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 道具id，长度(0,64]，字符只允许使用字母、数字、'\\_'、'-' |
| name | string | 是 | 道具名称，长度(0，20] |
| price | number | 是 | 道具单价，单位分，需要大于0 |
| remark | string | 是 | 道具备注，长度(0,1024] |
| item\_url | string | 是 | 道具图片的url地址，当前仅支持jpg,png等格式 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 查询批量上传道具任务

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_query_upload_goods.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | number | 是 | 0-正式环境 1-沙箱环境 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| upload\_item | [objarray](#Res__upload_item<Array>) | 上传的道具列表 |
| status | number | 0-无任务在运行 1-任务运行中 2-上传失败或部分失败（上传任务已经完成） 3-上传成功 |

**Res.upload_item(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 道具id |
| name | string | 道具名称 |
| price | number | 道具单价，单位分 |
| remark | string | 道具备注 |
| item\_url | string | 道具图片的url地址（微信转存后） |
| upload\_status | number | 0-上传中 1-id已经存在 2-上传成功 3-上传失败 |
| errmsg | string | 上传失败的原因 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 启动批量发布道具任务

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_start_publish_goods.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| publish\_item | [objarray](#Body__publish_item<Array>) | 是 | 发布的商品列表 |
| env | number | 是 | 0-正式环境 1-沙箱环境 |

**Body.publish_item(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 道具id，添加到开发环境时传的道具id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 查询批量发布道具任务

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_query_publish_goods.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | number | 是 | 0-正式环境 1-沙箱环境 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| errcode | number | [错误码](#apierrcode) | - |
| errmsg | string | [错误信息](#apierrcode) | - |
| publish\_item | [objarray](#Res__publish_item<Array>) | 发布的道具列表 | - |
| status | number | 发布状态 | [枚举值](#Enum_Res__status) |

**Res.publish_item(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 道具id |
| publish\_status | number | 0-上传中 1-id已经存在 2-发布成功 3-发布失败 |
| errmsg | string | 发布失败的原因 |

**Res.status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 无任务在运行 |
| 1 | 任务运行中 |
| 2 | 发布失败或部分失败（发布任务已经完成） |
| 3 | 发布成功 |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 查询商家账户可提现余额

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_query_biz_balance.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | number | 是 | 0-正式环境 1-沙箱环境（仅作为签名校验，查询的结果都是正式环境的） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| balance\_available | [object](#Res__balance_available) | 可提现余额 |

**Res.balance_available Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| amount | string | 可提现余额，单位元 |
| currency\_code | string | 币种（一般为CNY） |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 查询广告金充值账户

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_query_transfer_account.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | number | 是 | 0-正式环境 1-沙箱环境（仅作为签名校验，查询的结果都是正式环境的） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| acct\_list | [objarray](#Res__acct_list<Array>) | 广告金充值账户列表 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**Res.acct_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| transfer\_account\_name | string | 充值账户名称 |
| transfer\_account\_uid | number | 充值账户 uid |
| transfer\_account\_agency\_id | number | 充值账户服务商账号 id |
| transfer\_account\_agency\_name | string | 充值账户服务商账号名称 |
| state | number | 0-待审核，1-审核通过，2-审核驳回 |
| bind\_result | number | 1-绑定成功，2-绑定失败 |
| error\_msg | string | 错误信息 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 查询广告金发放记录

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_query_adver_funds.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| page | number | 否 | 查询页码，不小于 1 |
| page\_size | number | 否 | 每页记录数量 |
| filter | [object](#Body__filter) | 否 | 查询过滤条件 |
| env | number | 否 | 0-正式环境 1-沙箱环境（仅作为签名校验，查询的结果都是正式环境的） |

**Body.filter Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| settle\_begin | number | 否 | 查询结算周期开始时间，unix秒级时间戳 |
| settle\_end | number | 否 | 查询结算周期结束时间，unix秒级时间戳 |
| fund\_type | number | 否 | (可选)广告金发放原因， 0:通用赠送，1:广告激励，2:定向激励 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| adver\_funds\_list | [objarray](#Res__adver_funds_list<Array>) | 广告金发放记录列表 |
| total\_page | number | 查询命中总的页数 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**Res.adver_funds_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| settle\_begin | number | 结算周期开始时间，unix秒级时间戳 |
| settle\_end | number | 结算周期结束时间，unix秒级时间戳 |
| total\_amount | number | 发放广告金金额，单位分 |
| remain\_amount | number | 剩余可用广告金金额，单位分 |
| expire\_time | number | 广告金过期时间，unix秒级时间戳 |
| fund\_type | number | 广告金发放原因， 0:通用赠送，1:广告激励，2:定向激励 |
| fund\_id | string | 广告金发放ID |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 充值广告金

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_create_funds_bill.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transfer\_amount | number | 是 | 充值金额，单位分 |
| transfer\_account\_uid | number | 是 | 充值账户 uid |
| transfer\_account\_name | string | 是 | 充值账户名称 |
| transfer\_account\_agency\_id | number | 是 | 充值账户服务商账号 id |
| request\_id | string | 是 | 用户定义每一次请求的唯一 id，相同 id 的不同请求视为重复请求(不超过 1024 个字符) |
| settle\_begin | number | 是 | 充值所使用的广告金对应的结算周期开始时间，unix秒级时间戳 |
| settle\_end | number | 是 | 充值所使用的广告金对应的结算周期结束时间，unix秒级时间戳 |
| env | number | 是 | 0-正式环境 1-沙箱环境（仅作为签名校验，查询的结果都是正式环境的） |
| authorize\_advertise | number | 是 | 是否授权广告数据, 0:否，1:是 |
| fund\_type | number | 是 | 广告金发放原因， 0:通用赠送，1:广告激励，2:定向激励 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| bill\_id | string | 充值单 id |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 绑定广告金充值账户

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_bind_transfer_accout.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transfer\_account\_uid | number | 否 | 充值账户 uid |
| transfer\_account\_org\_name | string | 否 | 充值账户主体名称 |
| env | number | 否 | 0-正式环境 1-沙箱环境（仅作为签名校验，查询的结果都是正式环境的） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 查询广告金充值记录

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_query_funds_bill.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| page | number | 是 | 查询页码，不小于 1 |
| page\_size | number | 是 | 每页记录数量 |
| filter | [object](#Body__filter) | 是 | 查询过滤条件 |
| env | number | 是 | 0-正式环境 1-沙箱环境（仅作为签名校验，查询的结果都是正式环境的） |

**Body.filter Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oper\_time\_begin | number | 是 | 查询充值开始时间，unix秒级时间戳 |
| oper\_time\_end | number | 是 | 查询充值结束时间，unix秒级时间戳 |
| bill\_id | string | 否 | (可选)广告金充值单 ID |
| request\_id | string | 否 | (可选)调用接口 create\_funds\_bill 进行广告金充值时传入的 request\_id 字段 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| bill\_list | [objarray](#Res__bill_list<Array>) | 广告金充值记录列表 |
| total\_page | number | 查询命中总的页数 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**Res.bill_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| bill\_id | string | 充值单 ID |
| oper\_time | number | 充值时间，unix秒级时间戳 |
| settle\_begin | number | 对应广告金结算周期开始时间，unix秒级时间戳 |
| settle\_end | number | 对应广告金结算周期结束时间，unix秒级时间戳 |
| fund\_id | string | 对应广告金ID |
| transfer\_account\_name | string | 充值账户 |
| transfer\_account\_uid | number | 充值账户UID |
| transfer\_amount | number | 充值金额，单位：分 |
| status | number | 广告金充值状态：0-充值中，1-充值成功，2-充值失败 |
| request\_id | string | 调用接口 create\_funds\_bill 进行广告金充值时传入的 request\_id 字段 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 查询广告金回收记录

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_query_recover_bill.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| page | number | 是 | 查询页码，不小于 1 |
| page\_size | number | 是 | 每页记录数量 |
| filter | [object](#Body__filter) | 是 | 查询过滤条件 |
| env | number | 是 | 0-正式环境 1-沙箱环境（仅作为签名校验，查询的结果都是正式环境的） |

**Body.filter Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recover\_time\_begin | number | 是 | 查询回收开始时间，unix秒级时间戳 |
| recover\_time\_end | number | 是 | 查询回收结束时间，unix秒级时间戳 |
| bill\_id | string | 是 | (可选)广告金回收单 ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| bill\_list | [objarray](#Res__bill_list<Array>) | 广告金回收记录列表 |
| total\_page | number | 查询命中总的页数 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**Res.bill_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| bill\_id | string | 回收单 ID |
| recover\_time | number | 回收时间，unix秒级时间戳 |
| settle\_begin | number | 结算周期开始时间，unix秒级时间戳 |
| settle\_end | number | 结算周期结束时间，unix秒级时间戳 |
| fund\_id | string | 对应的发放广告金ID |
| recover\_account\_name | string | 回收广告金账户 |
| recover\_amount | number | 回收金额，单位：分 |
| refund\_order\_list | array | 对应的退款订单 id |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 获取投诉列表

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_get_complaint_list.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | number | 是 | 0-正式环境 1-沙箱环境（仅作为签名校验，查询的结果都是正式环境的） |
| begin\_date | string | 是 | 筛选开始时间，格式为yyyy-mm-dd,如"2023-01-01" |
| end\_date | string | 是 | 筛选结束时间，格式为yyyy-mm-dd,如"2023-01-01" |
| offset | number | 是 | 筛选偏移，从0开始 |
| limit | number | 是 | 筛选最多返回条数 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| total | number | 总条数 |
| complaints | [objarray](#Res__complaints<Array>) | 投诉列表 |

**Res.complaints(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| complaint\_id | string | 投诉id |
| complaint\_time | string | 投诉时间 格式为yyyy-mm-dd'T'HH:MM:ssXXX，其中XXX为时区偏移，例如：2023-11-28T11:11:49+08:00 |
| complaint\_detail | string | 投诉内容 |
| complaint\_state | string | 投诉状态 PENDING-待处理；PROCESSING-处理中；PROCESSED-已处理完成 |
| payer\_phone | string | 投诉人联系方式 |
| payer\_openid | string | 投诉人在商户AppID下的唯一标识 |
| complaint\_order\_info | [objarray](#Res__complaints<Array>__complaint_order_info<Array>) | 投诉单关联订单信息 |
| complaint\_full\_refunded | boolean | 投诉单下所有订单是否已全部全额退款 |
| incoming\_user\_response | boolean | 投诉单是否有待回复的用户留言 |
| user\_complaint\_times | number | 用户投诉次数。用户首次发起投诉记为1次，用户每有一次继续投诉就加1 |
| complaint\_media\_list | [objarray](#Res__complaints<Array>__complaint_media_list<Array>) | 用户上传的投诉相关资料，包括图片凭证等 |
| problem\_description | string | 用户发起投诉前选择的faq标题 |
| problem\_type | string | 问题类型为申请退款的单据是需要最高优先处理的单据。REFUND: 申请退款；SERVICE\_NOT\_WORK: 服务权益未生效；OTHERS: 其他类型 |
| apply\_refund\_amount | number | 当问题类型为申请退款时, 有值, (单位:分) |
| user\_tag\_list | array | 用户标签列表，每一项内容为string。TRUSTED: 此类用户满足极速退款条件；HIGH\_RISK: 高风险投诉，请按照运营要求优先妥善处理 |
| service\_order\_info | [objarray](#Res__complaints<Array>__service_order_info<Array>) | 投诉单关联服务单信息 |

**Res.complaints(Array).complaint_order_infoObject Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| transaction\_id | string | 投诉单关联的微信支付交易单号 |
| out\_trade\_no | string | 渠道单号，query\_order接口返回的channel\_order\_id |
| amount | number | 订单金额，单位（分） |
| wxa\_out\_trade\_no | string | 商户单号，商家在拉起支付时传的单号 |
| wx\_order\_id | string | 小程序侧单号 |

**Res.complaints(Array).complaint_media_listObject Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| media\_type | string | 媒体文件对应的业务类型，USER\_COMPLAINT\_IMAGE: 用户提交投诉时上传的图片凭证；OPERATION\_IMAGE: 用户、商户、微信支付客服在协商解决投诉时，上传的图片凭证 |
| media\_url | array | 每一项的内容为string，媒体文件请求url |

**Res.complaints(Array).service_order_infoObject Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| order\_id | string | 微信支付服务订单号，每个微信支付服务订单号与商户号下对应的商户服务订单号一一对应 |
| out\_order\_no | string | 商户系统内部服务订单号（不是交易单号），与创建订单时一致 |
| state | string | 此处上传的是用户发起投诉时的服务单状态，不会实时更新。DOING: 服务订单进行中；REVOKED: 服务订单已取消；WAITPAY: 服务订单待支付；DONE: 服务订单已完成 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 获取投诉详情

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_get_complaint_detail.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | number | 是 | 0-正式环境 1-沙箱环境（仅作为签名校验，查询的结果都是正式环境的） |
| complaint\_id | string | 是 | 投诉id，get\_complaint\_list接口返回 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| complaint | [object](#Res__complaint) | 与get\_complaint\_list接口的complaints一致 |

**Res.complaint Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| complaint\_id | string | 投诉id |
| complaint\_time | string | 投诉时间 格式为yyyy-mm-dd'T'HH:MM:ssXXX，其中XXX为时区偏移，例如：2023-11-28T11:11:49+08:00 |
| complaint\_detail | string | 投诉内容 |
| complaint\_state | string | 投诉状态 PENDING-待处理；PROCESSING-处理中；PROCESSED-已处理完成 |
| payer\_phone | string | 投诉人联系方式 |
| payer\_openid | string | 投诉人在商户AppID下的唯一标识 |
| complaint\_order\_info | array | 投诉单关联订单信息 |
| complaint\_full\_refunded | boolean | 投诉单下所有订单是否已全部全额退款 |
| incoming\_user\_response | boolean | 投诉单是否有待回复的用户留言 |
| user\_complaint\_times | number | 用户投诉次数。用户首次发起投诉记为1次，用户每有一次继续投诉就加1 |
| complaint\_media\_list | array | 用户上传的投诉相关资料，包括图片凭证等 |
| problem\_description | string | 用户发起投诉前选择的faq标题 |
| problem\_type | string | 问题类型为申请退款的单据是需要最高优先处理的单据。REFUND: 申请退款；SERVICE\_NOT\_WORK: 服务权益未生效；OTHERS: 其他类型 |
| apply\_refund\_amount | number | 当问题类型为申请退款时, 有值, (单位:分) |
| user\_tag\_list | array | 用户标签列表，每一项内容为string。TRUSTED: 此类用户满足极速退款条件；HIGH\_RISK: 高风险投诉，请按照运营要求优先妥善处理 |
| service\_order\_info | array | 投诉单关联服务单信息 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 获取协商历史

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_get_negotiation_history.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | number | 是 | 0-正式环境 1-沙箱环境（仅作为签名校验，查询的结果都是正式环境的） |
| complaint\_id | string | 是 | 投诉id，get\_complaint\_list接口返回 |
| offset | number | 是 | 筛选偏移，从0开始 |
| limit | number | 是 | 筛选最多返回条数 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| total | number | 总条数 |
| history | [objarray](#Res__history<Array>) | 协商历史 |

**Res.history(Array) Object Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| log\_id | string | 操作流水号 | - |
| operator | string | 当前投诉协商记录的操作人 | - |
| operate\_time | string | 当前操作时间，格式为yyyy-mm-dd'T'HH:MM:ssXXX，其中XXX为时区偏移，例如：2023-11-28T11:11:49+08:00 | - |
| operate\_type | string | 当前投诉协商记录的操作类型 | [枚举值](#Enum_Res__history<Array>__operate_type) |
| operate\_details | string | 当前投诉协商记录的具体内容 | - |
| complaint\_media\_list | [objarray](#Res__history<Array>__complaint_media_list<Array>) | 投诉单执行操作时上传的资料凭证，包含用户、商户、微信支付客服等角色操作 | - |

**Res.history(Array).complaint_media_listObject Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| media\_type | string | 媒体文件对应的业务类型 | [枚举值](#Enum_Res__history<Array>__complaint_media_list<Array>__media_type) |
| media\_url | array | 每一项的内容为string，媒体文件请求url | - |

**Res.history(Array).operate_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| USER\_CREATE\_COMPLAINT | 用户提交投诉 |
| USER\_CONTINUE\_COMPLAINT | 用户继续投诉 |
| USER\_RESPONSE | 用户留言 |
| PLATFORM\_RESPONSE | 平台留言 |
| MERCHANT\_RESPONSE | 商户留言 |
| MERCHANT\_CONFIRM\_COMPLETE | 商户申请结单 |
| USER\_CREATE\_COMPLAINT\_SYSTEM\_MESSAGE | 用户提交投诉系统通知 |
| COMPLAINT\_FULL\_REFUNDED\_SYSTEM\_MESSAGE | 投诉单发起全额退款系统通知 |
| USER\_CONTINUE\_COMPLAINT\_SYSTEM\_MESSAGE | 用户继续投诉系统通知 |
| USER\_REVOKE\_COMPLAINT | 用户主动撤诉（只存在于历史投诉单的协商历史中） |
| USER\_COMFIRM\_COMPLAINT | 用户确认投诉解决（只存在于历史投诉单的协商历史中） |
| PLATFORM\_HELP\_APPLICATION | 平台催办 |
| USER\_APPLY\_PLATFORM\_HELP | 用户申请平台协助 |
| MERCHANT\_APPROVE\_REFUND | 商户同意退款申请 |
| MERCHANT\_REFUSE\_RERUND | 商户拒绝退款申请, 此时操作内容里展示拒绝原因 |
| USER\_SUBMIT\_SATISFACTION | 用户提交满意度调查结果,此时操作内容里会展示满意度分数 |
| SERVICE\_ORDER\_CANCEL | 服务订单已取消 |
| SERVICE\_ORDER\_COMPLETE | 服务订单已完成 |
| COMPLAINT\_PARTIAL\_REFUNDED\_SYSTEM\_MESSAGE | 投诉单发起部分退款系统通知 |
| COMPLAINT\_REFUND\_RECEIVED\_SYSTEM\_MESSAGE | 投诉单退款到账系统通知 |

**Res.history(Array).complaint_media_list.media_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| USER\_COMPLAINT\_IMAGE | 用户提交投诉时上传的图片凭证 |
| OPERATION\_IMAGE | 用户、商户、微信支付客服在协商解决投诉时，上传的图片凭证 |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 回复用户

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_response_complaint.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | number | 是 | 0-正式环境 1-沙箱环境（仅作为签名校验，查询的结果都是正式环境的） |
| complaint\_id | string | 是 | 投诉id，get\_complaint\_list接口返回 |
| response\_content | string | 是 | 回复内容 |
| response\_images | array | 是 | 每一项的内容为string，传upload\_vp\_file接口返回的file\_id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 完成投诉处理

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_complete_complaint.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | number | 是 | 0-正式环境 1-沙箱环境（仅作为签名校验，查询的结果都是正式环境的） |
| complaint\_id | string | 是 | 投诉id，[获取投诉列表](api_get_complaint_list)接口返回 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 上传媒体文件

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_upload_vp_file.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | number | 是 | 0-正式环境 1-沙箱环境（仅作为签名校验，查询的结果都是正式环境的） |
| base64\_img | string | 是 | 经base64编码后的图片内容，使用这个字段最多只能传1m的图片，超过1m请使用img\_url字段 |
| img\_url | string | 是 | 图片url，需要能直接下载，不能是返回302等返回码的地址，最高允许传2m图片（优先使用img\_url） |
| file\_name | string | 是 | 图片名称 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| file\_id | string | 返回文件id |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 获取微信支付反馈投诉图片的签名头部

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_get_upload_file_sign.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | number | 是 | 0-正式环境 1-沙箱环境（仅作为签名校验，查询的结果都是正式环境的） |
| wxpay\_url | string | 是 | 微信支付的图片地址格式为"https://api.mch.weixin.qq.com/v3/merchant-service/images/{xxxxxx}" |
| convert\_cos | boolean | 是 | 是否转存到cos，转存后可以获得图片的临时下载地址，30分钟有效 |
| complaint\_id | string | 是 | 对应的反馈投诉id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| sign | string | 返回微信支付图片请求的Authorization头部值，具体使用方法可查看备注 |
| cos\_url | string | 当convert\_cos为true时才有意义，返回转存后的url地址，30分钟有效 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 下载广告金对应的商户订单信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_download_adverfunds_order.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fund\_id | string | 是 | 广告金发放ID |
| env | number | 是 | 0-正式环境 1-沙箱环境（仅作为签名校验，查询的结果都是正式环境的） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| url | string | 订单下载链接 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 268490001 | openid错误 |
| 268490002 | 请求参数字段错误，具体看errmsg |
| 268490003 | 签名错误 |
| 268490004 | 重复操作（赠送和代币支付和充值广告金相关接口会返回，表示之前的操作已经成功） |
| 268490005 | 订单已经通过cancel\_currency\_pay接口退款，不支持再退款 |
| 268490006 | 代币的退款/支付操作金额不足 |
| 268490007 | 图片或文字存在敏感内容，禁止使用 |
| 268490008 | 代币未发布，不允许进行代币操作 |
| 268490009 | 用户session\_key不存在或已过期，请重新登录 |
| 268490011 | 数据生成中，请稍后调用本接口获取 |
| 268490012 | 批量任务运行中，请等待完成后才能再次运行 |
| 268490013 | 禁止对核销状态的单进行退款 |
| 268490014 | 退款操作进行中，稍后可以使用相同参数重试 |
| 268490015 | 频率限制 |
| 268490016 | 退款的left\_fee字段与实际不符，请通过query\_order接口查询确认 |
| 268490018 | 广告金充值帐户行业 id 不匹配 |
| 268490019 | 广告金充值帐户 id已绑定其他 appid |
| 268490020 | 广告金充值帐户主体名称错误 |
| 268490021 | 账户未完成进件 |
| 268490022 | 广告金充值账户无效 |
| 268490023 | 广告金余额不足 |
| 268490024 | 广告金充值金额必须大于 0 |

---

### 查询签约关系

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_query_subscribe_contract.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户的openid |
| product\_id | string | 是 | 道具 id，需为订阅制道具 |
| out\_contract\_code | string | 是 | 签约时传入的协议号 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| authorization\_state | string | SIGNED: 签约生效中。TERMINATED: 生效的签约协议已被解约。此时协议已经到达终态，该协议无法再次进行签约；可更换协议号再发起签约。UNBINDUSER: 从未签约过 |

---

### 预通知扣款

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_send_subscribe_pre_payment.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户的openid |
| deduct\_price | number | 是 | 金额/分，属于 [100，道具价格] |
| product\_id | string | 是 | 道具 id，需为订阅制道具 |
| out\_contract\_code | string | 是 | 签约时传入的协议号 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | sys error | 非预期系统错误，可重试 |
| 674690001 | product type not support""input deduct\_price not valid | 参数错误 |
| 690000000 | user not subscribed | 用户未签约 |
| 690000001 | not allowed to trigger pre payment at this time | 预通知时间不合法 1.  上一单成功支付，且订阅周期到期 T-3 之前 2.  上一单支付失败 or 没有发起支付 or 正在支付中，且在上一单的 T+8 内 3.  发起时间不在 07:10 ~ 21:50 |

---

### 发起订阅扣款

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_submit_subscribe_pay_order.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户的openid |
| offer\_id | string | 是 | 在米大师侧申请的应用 id, mp-支付基础配置中的offerid |
| buy\_quantity | number | 是 | 购买数量，填：1 |
| env | number | 否 | 环境配置, 0 正式环境, 仅支持正式环境 |
| currency\_type | string | 是 | 币种，填：CNY |
| product\_id | string | 是 | 订阅道具ID |
| deduct\_price | number | 是 | 扣款金额(分), 属于 [1，道具价格] |
| order\_id | string | 是 | 业务订单号, 每个订单号只能使用一次, 重复使用会失败(不建议业务强依赖平台对这里的唯一性校验)，要求8-32个字符内, 只能是数字、大小写字母、符号 \_-\ |
| attach | string | 是 | 透传数据, 发货通知时会透传给开发者 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -15027 | 扣款价格不合法 |
| -15026 | 扣款时间不合法 |
| -15025 | 不存在预通知单/重复下单 |
| -15021 | 小程序被限频交易 |
| -15020 | 操作过快，请稍候再试 |
| -15019 | 调微信报商户受限,商家可以登录微信商户平台/微信支付商家助手小程序查看原因和解决方案 |
| -15018 | 代币或者道具productId审核不通过 |
| -15017 | 此商家涉嫌违规，收款功能已被限制，暂无法支付。商家可以登录微信商户平台/微信支付商家助手小程序查看原因和解决方案 |
| -15016 | signData格式有问题 |
| -15014 | 道具/代币发布未生效，禁止下单，大概10分钟后生效 |
| -15013 | goodsPrice道具价格错误 |
| -15012 | 调用米大师失败导致关单,请换新单号重试 |
| -15011 | 现网版本的env只能是0,不能填1(沙盒环境) |
| -15010 | 道具productId未发布 |
| -15009 | 代币未发布 |
| -15008 | 二级商户进件未完成 |
| -15007 | session\_key过期 |
| -15006 | 支付签名paySig错误 |
| -15005 | 用户态签名signature错误 |
| -15004 | currencyType错误,目前只能填CNY |
| -15003 | 系统错误 |
| -15002 | outTradeNo重复使用,请换新单号重试 |
| -15001 | 参数错误,具体原因见err\_msg |
| 1001 | 参数错误 |

---

### 商家解约

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_cancel_subscribe_contract.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户的openid |
| termination\_reason | string | 是 | 解约原因 |
| product\_id | string | 是 | 道具 id，需为订阅制道具 |
| out\_contract\_code | string | 是 | 签约时传入的协议号 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

---

### 下载支付订单

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_start_download_order.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| begin\_ds | number | 是 | 20260420 | 开始日期，格式 YYYYMMDD |
| end\_ds | number | 是 | 20260420 | 结束日期，格式 YYYYMMDD，与 begin\_ds 间隔不超过 31 天 |
| order\_type | number | 是 | 1 | 订单类型：1=代币交易订单 /2=道具直购交易订单 /3=会员订阅订单 /4=退款订单 |
| order\_info | string | 否 |  | 订单信息搜索关键字，支持按交易单号/商户单号/用户ID 模糊匹配 |
| is\_provided | boolean | 否 | true | 发货状态，order\_type 为 2(道具) 或 3(会员订阅) 时必须传入；true=已发货 /false=未发货；不传默认 true |
| refund\_status | number | 否 | 0 | 退款状态筛选，仅 order\_type=4(退款订单) 时有效；0=全部 /2=已退款 /4=退款中 /5=退款失败；不传默认 0（全部） |
| env | number | 是 | 0 | 环境标识：0=现网 /1=沙箱（用于基类签名校验） |
| pay\_channel | number | 是 | 1 | 支付渠道：1=普通虚拟支付 /2=苹果IAP |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | 错误码，0 表示成功 |
| errmsg | string |  | [错误信息](#apierrcode) |
| task\_id | string |  | 下载任务 ID，用于后续查询下载结果 |

---

### 查询下载订单任务

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_query_download_order.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | - | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| task\_id | string | 是 |  | 下载任务 ID，由 StartDownloadOrder 接口返回 |
| env | number | 是 | 0 | 环境标识：0=现网 /1=沙箱（用于基类签名校验） |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | 错误码，0 表示成功 |
| errmsg | string |  | [错误信息](#apierrcode) |
| task\_id | string |  | 下载任务 ID，与请求参数对应 |
| status | number | 2 | 任务状态：0=初始化 /1=运行中 /2=成功 /3=失败 |
| download\_url | string |  | 下载文件 URL，仅 status=2(成功) 时有值 |
| expire\_at | number | 1745328000 | URL 过期时间（Unix 秒级时间戳） |

---

<!-- pages: 35 -->
