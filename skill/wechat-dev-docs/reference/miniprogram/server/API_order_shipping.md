# 小程序服务端 API 结构化参考 — API/order_shipping

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 发货信息录入

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/order_shipping/api_uploadshippinginfo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| order\_key | [object](#Body__order_key) | 是 | 订单，需要上传物流信息的订单 |
| logistics\_type | number | 是 | 物流模式，发货方式枚举值：1、实体物流配送采用快递公司进行实体物流配送形式 2、同城配送 3、虚拟商品，虚拟商品，例如话费充值，点卡等，无实体配送形式 4、用户自提 |
| delivery\_mode | number | 是 | 发货模式，发货模式枚举值：1、UNIFIED\_DELIVERY（统一发货）2、SPLIT\_DELIVERY（分拆发货） |
| is\_all\_delivered | boolean | 否 | 分拆发货模式时必填，用于标识分拆发货模式下是否已全部发货完成，只有全部发货完成的情况下才会向用户推送发货完成通知。示例值: true/false |
| shipping\_list | [objarray](#Body__shipping_list<Array>) | 是 | 物流信息列表，发货物流单列表，支持统一发货（单个物流单）和分拆发货（多个物流单）两种模式，多重性: [1, 15] |
| upload\_time | string | 是 | 上传时间，用于标识请求的先后顺序 示例值: `2022-12-15T13:29:35.120+08:00` |
| payer | [object](#Body__payer) | 是 | 支付者，支付者信息 |

**Body.order_key Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| order\_number\_type | number | 是 | 订单单号类型，用于确认需要上传详情的订单。枚举值1，使用下单商户号和商户侧单号；枚举值2，使用微信支付单号。 |
| transaction\_id | string | 否 | 原支付交易对应的微信订单号 |
| mchid | string | 否 | 支付下单商户的商户号，由微信支付生成并下发。 |
| out\_trade\_no | string | 否 | 商户系统内部订单号，只能是数字、大小写字母`\_-\*`且在同一个商户号下唯一 |

**Body.shipping_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tracking\_no | string | 否 | 物流单号，物流快递发货时必填，示例值: 323244567777 字符字节限制: [1, 128] |
| express\_company | string | 否 | 物流公司编码，快递公司ID，参见[获取运力 id 列表get\_delivery\_list](../weixin-express/express-msg/api_get_delivery_list)，物流快递发货时必填， 示例值: DHL 字符字节限制: [1, 128] |
| item\_desc | string | 是 | 商品信息，例如：微信红包抱枕\*1个，限120个字以内 |
| contact | [object](#Body__shipping_list<Array>__contact) | 否 | 联系方式，当发货的物流公司为顺丰时，联系方式为必填，收件人或寄件人联系方式二选一 |

**Body.payer Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户标识，用户在小程序appid下的唯一标识。 下单前需获取到用户的Openid 示例值: oUpF8uMuAJO\_M2pxb1Q9zNjWeS6o 字符字节限制: [1, 128] |

**Body.shipping_list(Array).contact Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| consignor\_contact | string | 否 | 寄件人联系方式，寄件人联系方式，采用掩码传输，最后4位数字不能打掩码 示例值: `189\*\*\*\*1234, 021-\*\*\*\*1234, \*\*\*\*1234, 0\*\*2-\*\*\*1234, 0\*\*2-\*\*\*\*\*\*23-10, \*\*\*\*123-8008` 值限制: 0 ≤ value ≤ 1024 |
| receiver\_contact | string | 否 | 收件人联系方式，收件人联系方式为，采用掩码传输，最后4位数字不能打掩码 示例值: `189\*\*\*\*1234, 021-\*\*\*\*1234, \*\*\*\*1234, 0\*\*2-\*\*\*1234, 0\*\*2-\*\*\*\*\*\*23-10, \*\*\*\*123-8008` 值限制: 0 ≤ value ≤ 1024 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | system error。系统繁忙，此时请开发者稍候再试 |
| 10060001 | 支付单不存在。请检查微信支付单号形式下 transaction\_id 字段或商户侧单号形式下 mchid、out\_trade\_no 字段是否有误 |
| 10060002 | 支付单已完成发货，无法继续发货。请检查支付单发货情况 |
| 10060003 | 支付单已使用重新发货机会。支付单处于已发货状态时调用该API视为重新发货，仅可重新发货一次，请检查支付单发货情况 |
| 10060004 | 支付单处于不可发货的状态。请检查支付单状态 |
| 10060005 | 物流类型有误。按照文档中物流类型枚举填写该字段 |
| 10060006 | 非快递发货时不允许分拆发货。非快递发货时不允许分拆发货，请检查请求参数 |
| 10060007 | 分拆发货模式下必须填写 is\_all\_delivered 字段。请检查请求参数中的 is\_all\_delivered 字段 |
| 10060008 | 商品描述 item\_desc 字段不能为空。用于发货信息录入场景时商品描述字段不能为空 |
| 10060009 | 商品描述 item\_desc 字段太长。请检查商品描述字段 |
| 10060012 | 系统错误。系统繁忙，此时请开发者稍候再试 |
| 10060014 | 参数错误。根据错误原因描述修改参数 |
| 10060019 | 系统错误。系统繁忙，此时请开发者稍候再试 |
| 10060020 | 该笔支付单在没有任何商品描述的情况下不允许完成发货。请补充商品描述 item\_desc |
| 10060023 | 发货信息未更新。支付单信息不变 |
| 10060024 | 物流信息列表太长。支付单物流信息列表长度不可大于 15 |
| 10060025 | 物流公司编码太长。请检查物流公司编码是否有误 |
| 10060026 | 物流单号太长.。请检查物流单号是否有误 |
| 10060031 | 该笔支付单不属于 openid 所指定的用户。请检查支付单号或 openid 是否有误 |
| 268485194 | 订单单号类型非法。按照文档中订单单号类型枚举填写该字段 |
| 268485195 | 微信支付单号形式下 transaction\_id 字段不能为空。微信支付单号形式下 transaction\_id 字段必须设置 |
| 268485196 | 商户侧单号形式下 mchid 字段不能为空。商户侧单号形式下 mchid 字段必须设置 |
| 268485197 | 商户侧单号形式下 out\_trade\_no 字段不能为空。商户侧单号形式下 out\_trade\_no 字段必须设置 |
| 268485216 | 上传时间非法，请按照 RFC 3339 格式填写。上传时间必须满足 RFC 3339 格式，如 2022-12-15T13:29:35.120+08:00 |
| 268485224 | 发货模式非法。按照文档中发货模式枚举设置该字段 |
| 268485226 | 物流单号不能为空。物流快递发货时物流单号必须填写 |
| 268485227 | 物流公司编码不能为空。物流快递发货时物流公司编码必须填写 |
| 268485228 | 统一发货模式下，物流信息列表长度必须为 1。统一发货模式下，物流信息列表长度必须为 1 |

---

### 发货信息合单录入

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/order_shipping/api_uploadcombinedshippinginfo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| order\_key | [object](#Body__order_key) | 是 | 合单订单，需要上传物流详情的合单订单，根据订单类型二选一 |
| sub\_orders | [objarray](#Body__sub_orders<Array>) | 否 | 子单物流详情 |
| upload\_time | string | 是 | 上传时间，用于标识请求的先后顺序 示例值: `2022-12-15T13:29:35.120+08:00` |
| payer | [object](#Body__payer) | 是 | 支付者，支付者信息 |

**Body.order_key Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| order\_number\_type | number | 是 | 订单单号类型，用于确认需要上传详情的订单。枚举值1，使用下单商户号和商户侧单号；枚举值2，使用微信支付单号。 |
| transaction\_id | string | 否 | 原支付交易对应的微信订单号 |
| mchid | string | 否 | 支付下单商户的商户号，由微信支付生成并下发。 |
| out\_trade\_no | string | 否 | 商户系统内部订单号，只能是数字、大小写字母`\_-\*`且在同一个商户号下唯一 |

**Body.sub_orders(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| order\_key | [object](#Body__sub_orders<Array>__order_key) | 是 | 需要上传物流详情的子单订单，订单类型与合单订单保持一致 |
| logistics\_type | number | 是 | 物流模式，发货方式枚举值：1、实体物流配送采用快递公司进行实体物流配送形式 2、同城配送 3、虚拟商品，虚拟商品，例如话费充值，点卡等，无实体配送形式 4、用户自提 |
| delivery\_mode | number | 是 | 发货模式，发货模式枚举值：1、UNIFIED\_DELIVERY（统一发货）2、SPLIT\_DELIVERY（分拆发货） 示例值: UNIFIED\_DELIVERY |
| is\_all\_delivered | boolean | 否 | 分拆发货模式时必填，用于标识分拆发货模式下是否已全部发货完成，只有全部发货完成的情况下才会向用户推送发货完成通知。示例值: true/false |
| shipping\_list | [objarray](#Body__sub_orders<Array>__shipping_list<Array>) | 否 | 子单物流信息列表 多重性: [1, 15] |

**Body.payer Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户标识，用户在小程序appid下的唯一标识。 下单前需获取到用户的Openid 示例值: oUpF8uMuAJO\_M2pxb1Q9zNjWeS6o 字符字节限制: [1, 128] |

**Body.sub_orders(Array).order_key Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| order\_number\_type | number | 是 | 订单单号类型，用于确认需要上传详情的订单。枚举值1，使用下单商户号和商户侧单号；枚举值2，使用微信支付单号。 |
| transaction\_id | string | 否 | 原支付交易对应的微信订单号 |
| mchid | string | 否 | 支付下单商户的商户号，由微信支付生成并下发。 |
| out\_trade\_no | string | 否 | 商户系统内部订单号，只能是数字、大小写字母`\_-\*`且在同一个商户号下唯一 |

**Body.sub_orders(Array).shipping_listObject Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tracking\_no | string | 否 | 物流单号，物流快递发货时必填，示例值: 323244567777 字符字节限制: [1, 128] |
| express\_company | string | 否 | 物流公司编码，快递公司ID，参见[获取运力 id 列表get\_delivery\_list](../weixin-express/express-msg/api_get_delivery_list)，物流快递发货时必填， 示例值: DHL 字符字节限制: [1, 128] |
| item\_desc | string | 是 | 商品信息，例如：微信红包抱枕\*1个，限120个字以内 |
| contact | [object](#Body__sub_orders<Array>__shipping_list<Array>__contact) | 否 | 联系方式，当发货的物流公司为顺丰时，联系方式为必填，收件人或寄件人联系方式二选一 |

**Body.sub_orders(Array).shipping_list.contact Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| consignor\_contact | string | 否 | 寄件人联系方式，寄件人联系方式，采用掩码传输，最后4位数字不能打掩码 示例值: `189\*\*\*\*1234, 021-\*\*\*\*1234, \*\*\*\*1234, 0\*\*2-\*\*\*1234, 0\*\*2-\*\*\*\*\*\*23-10, \*\*\*\*123-8008` 值限制: 0 ≤ value ≤ 1024 |
| receiver\_contact | string | 否 | 收件人联系方式，收件人联系方式为，采用掩码传输，最后4位数字不能打掩码 示例值: `189\*\*\*\*1234, 021-\*\*\*\*1234, \*\*\*\*1234, 0\*\*2-\*\*\*1234, 0\*\*2-\*\*\*\*\*\*23-10, \*\*\*\*123-8008` 值限制: 0 ≤ value ≤ 1024 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | system error。系统繁忙，此时请开发者稍候再试 |
| 10060001 | 支付单不存在。请检查微信支付单号形式下 transaction\_id 字段或商户侧单号形式下 mchid、out\_trade\_no 字段是否有误 |
| 10060002 | 支付单已完成发货，无法继续发货。请检查支付单发货情况 |
| 10060003 | 支付单已使用重新发货机会。支付单处于已发货状态时调用该API视为重新发货，仅可重新发货一次，请检查支付单发货情况 |
| 10060004 | 支付单处于不可发货的状态。请检查支付单状态 |
| 10060005 | 物流类型有误。按照文档中物流类型枚举填写该字段 |
| 10060006 | 非快递发货时不允许分拆发货。非快递发货时不允许分拆发货，请检查请求参数 |
| 10060007 | 分拆发货模式下必须填写 is\_all\_delivered 字段。请检查请求参数中的 is\_all\_delivered 字段 |
| 10060008 | 商品描述 item\_desc 字段不能为空。用于发货信息录入场景时商品描述字段不能为空 |
| 10060009 | 商品描述 item\_desc 字段太长。请检查商品描述字段 |
| 10060012 | 系统错误。系统繁忙，此时请开发者稍候再试 |
| 10060014 | 参数错误。根据错误原因描述修改参数 |
| 10060019 | 系统错误。系统繁忙，此时请开发者稍候再试 |
| 10060020 | 该笔支付单在没有任何商品描述的情况下不允许完成发货。请补充商品描述 item\_desc |
| 10060023 | 发货信息未更新。支付单信息不变 |
| 10060024 | 物流信息列表太长。支付单物流信息列表长度不可大于 15 |
| 10060025 | 物流公司编码太长。请检查物流公司编码是否有误 |
| 10060026 | 物流单号太长.。请检查物流单号是否有误 |
| 10060031 | 该笔支付单不属于 openid 所指定的用户。请检查支付单号或 openid 是否有误 |
| 268485194 | 订单单号类型非法。按照文档中订单单号类型枚举填写该字段 |
| 268485195 | 微信支付单号形式下 transaction\_id 字段不能为空。微信支付单号形式下 transaction\_id 字段必须设置 |
| 268485196 | 商户侧单号形式下 mchid 字段不能为空。商户侧单号形式下 mchid 字段必须设置 |
| 268485197 | 商户侧单号形式下 out\_trade\_no 字段不能为空。商户侧单号形式下 out\_trade\_no 字段必须设置 |
| 268485216 | 上传时间非法，请按照 RFC 3339 格式填写。上传时间必须满足 RFC 3339 格式，如 2022-12-15T13:29:35.120+08:00 |
| 268485224 | 发货模式非法。按照文档中发货模式枚举设置该字段 |
| 268485226 | 物流单号不能为空。物流快递发货时物流单号必须填写 |
| 268485227 | 物流公司编码不能为空。物流快递发货时物流公司编码必须填写 |
| 268485228 | 统一发货模式下，物流信息列表长度必须为 1。统一发货模式下，物流信息列表长度必须为 1 |

---

### 查询订单发货状态

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/order_shipping/api_getorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transaction\_id | string | 否 | 原支付交易对应的微信订单号。 |
| merchant\_id | string | 否 | 支付下单商户的商户号，由微信支付生成并下发。 |
| sub\_merchant\_id | string | 否 | 二级商户号。 |
| merchant\_trade\_no | string | 否 | 商户系统内部订单号，只能是数字、大小写字母`\_-\*`且在同一个商户号下唯一。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| order | [object](#Res__order) | - | 支付单信息。 |

**Res.order Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| transaction\_id | string | 原支付交易对应的微信订单号。 |
| merchant\_id | string | 支付下单商户的商户号，由微信支付生成并下发。 |
| sub\_merchant\_id | string | 二级商户号。 |
| merchant\_trade\_no | string | 商户系统内部订单号，只能是数字、大小写字母`\_-\*`且在同一个商户号下唯一。 |
| description | string | 以分号连接的该支付单的所有商品描述，当超过120字时自动截断并以 “...” 结尾。 |
| paid\_amount | number | 支付单实际支付金额，整型，单位：分钱。 |
| openid | string | 支付者openid。 |
| trade\_create\_time | number | 交易创建时间，时间戳形式。 |
| pay\_time | number | 支付时间，时间戳形式。 |
| order\_state | number | 订单状态枚举：(1) 待发货；(2) 已发货；(3) 确认收货；(4) 交易完成；(5) 已退款；(6) 资金待结算。 |
| in\_complaint | boolean | 是否处在交易纠纷中。 |
| shipping | [object](#Res__order__shipping) | 发货信息。 |

**Res.order.shipping Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| delivery\_mode | number | 发货模式，发货模式枚举值：1、UNIFIED\_DELIVERY（统一发货）2、SPLIT\_DELIVERY（分拆发货） 示例值: UNIFIED\_DELIVERY |
| logistics\_type | number | 物流模式，发货方式枚举值：1、实体物流配送采用快递公司进行实体物流配送形式 2、同城配送 3、虚拟商品，虚拟商品，例如话费充值，点卡等，无实体配送形式 4、用户自提 |
| finish\_shipping | boolean | 是否已完成全部发货。 |
| goods\_desc | string | 在小程序后台发货信息录入页录入的商品描述。 |
| finish\_shipping\_count | number | 已完成全部发货的次数，未完成时为 0，完成时为 1，重新发货并完成后为 2。 |
| shipping\_list | [objarray](#Res__order__shipping__shipping_list<Array>) | 物流信息列表，发货物流单列表，支持统一发货（单个物流单）和分拆发货（多个物流单）两种模式。 |

**Res.order.shipping.shipping_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| tracking\_no | string | 物流单号，示例值: "323244567777"。 |
| express\_company | string | 同城配送公司名或物流公司编码，快递公司ID，参见「获取运力 id 列表get\_delivery\_list」 示例值: "DHL"。 |
| goods\_desc | string | 使用上传物流信息 API 录入的该物流信息的商品描述。 |
| upload\_time | number | 该物流信息的上传时间，时间戳形式。 |
| contact | [object](#Res__order__shipping__shipping_list<Array>__contact) | 联系方式。 |

**Res.order.shipping.shipping_list(Array).contact Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| consignor\_contact | string | 寄件人联系方式。 |
| receiver\_contact | string | 收件人联系方式。 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | system error。系统繁忙，此时请开发者稍候再试 |
| 10060001 | 支付单不存在。请检查微信支付单号形式下 transaction\_id 字段或商户侧单号形式下 mchid、out\_trade\_no 字段是否有误 |
| 10060002 | 支付单已完成发货，无法继续发货。请检查支付单发货情况 |
| 10060003 | 支付单已使用重新发货机会。支付单处于已发货状态时调用该API视为重新发货，仅可重新发货一次，请检查支付单发货情况 |
| 10060004 | 支付单处于不可发货的状态。请检查支付单状态 |
| 10060005 | 物流类型有误。按照文档中物流类型枚举填写该字段 |
| 10060006 | 非快递发货时不允许分拆发货。非快递发货时不允许分拆发货，请检查请求参数 |
| 10060007 | 分拆发货模式下必须填写 is\_all\_delivered 字段。请检查请求参数中的 is\_all\_delivered 字段 |
| 10060008 | 商品描述 item\_desc 字段不能为空。用于发货信息录入场景时商品描述字段不能为空 |
| 10060009 | 商品描述 item\_desc 字段太长。请检查商品描述字段 |
| 10060012 | 系统错误。系统繁忙，此时请开发者稍候再试 |
| 10060014 | 参数错误。根据错误原因描述修改参数 |
| 10060019 | 系统错误。系统繁忙，此时请开发者稍候再试 |
| 10060020 | 该笔支付单在没有任何商品描述的情况下不允许完成发货。请补充商品描述 item\_desc |
| 10060023 | 发货信息未更新。支付单信息不变 |
| 10060024 | 物流信息列表太长。支付单物流信息列表长度不可大于 15 |
| 10060025 | 物流公司编码太长。请检查物流公司编码是否有误 |
| 10060026 | 物流单号太长.。请检查物流单号是否有误 |
| 10060031 | 该笔支付单不属于 openid 所指定的用户。请检查支付单号或 openid 是否有误 |
| 268485194 | 订单单号类型非法。按照文档中订单单号类型枚举填写该字段 |
| 268485195 | 微信支付单号形式下 transaction\_id 字段不能为空。微信支付单号形式下 transaction\_id 字段必须设置 |
| 268485196 | 商户侧单号形式下 mchid 字段不能为空。商户侧单号形式下 mchid 字段必须设置 |
| 268485197 | 商户侧单号形式下 out\_trade\_no 字段不能为空。商户侧单号形式下 out\_trade\_no 字段必须设置 |
| 268485216 | 上传时间非法，请按照 RFC 3339 格式填写。上传时间必须满足 RFC 3339 格式，如 2022-12-15T13:29:35.120+08:00 |
| 268485224 | 发货模式非法。按照文档中发货模式枚举设置该字段 |
| 268485226 | 物流单号不能为空。物流快递发货时物流单号必须填写 |
| 268485227 | 物流公司编码不能为空。物流快递发货时物流公司编码必须填写 |
| 268485228 | 统一发货模式下，物流信息列表长度必须为 1。统一发货模式下，物流信息列表长度必须为 1 |

---

### 查询订单列表

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/order_shipping/api_getorderlist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pay\_time\_range | [object](#Body__pay_time_range) | 否 | 支付时间所属范围。 |
| order\_state | number | 否 | 订单状态枚举：(1) 待发货；(2) 已发货；(3) 确认收货；(4) 交易完成；(5) 已退款；(6) 资金待结算。 |
| openid | string | 否 | 支付者openid。 |
| last\_index | string | 否 | 翻页时使用，获取第一页时不用传入，如果查询结果中 has\_more 字段为 true，则传入该次查询结果中返回的 last\_index 字段可获取下一页。 |
| page\_size | number | 否 | 翻页时使用，返回列表的长度，默认为100。 返回参数 |

**Body.pay_time_range Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin\_time | number | 否 | 起始时间，时间戳形式，不填则视为从0开始。 |
| end\_time number | number | 否 | 结束时间（含），时间戳形式，不填则视为32位无符号整型的最大值。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | [错误码](#apierrcode) |
| last\_index | string | - | 翻页时使用。 |
| has\_more | boolean | - | 是否还有更多支付单。 |
| order\_list | [object](#Res__order_list) | - | 支付单信息列表。 |

**Res.order_list Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| transaction\_id | string | 原支付交易对应的微信订单号。 |
| merchant\_id | string | 支付下单商户的商户号，由微信支付生成并下发。 |
| sub\_merchant\_id | string | 二级商户号。 |
| merchant\_trade\_no | string | 商户系统内部订单号，只能是数字、大小写字母`\_-\*`且在同一个商户号下唯一。 |
| description | string | 以分号连接的该支付单的所有商品描述，当超过120字时自动截断并以 “...” 结尾。 |
| paid\_amount | number | 支付单实际支付金额，整型，单位：分钱。 |
| openid | string | 支付者openid。 |
| trade\_create\_time | number | 交易创建时间，时间戳形式。 |
| pay\_time | number | 支付时间，时间戳形式。 |
| order\_state | number | 订单状态枚举：(1) 待发货；(2) 已发货；(3) 确认收货；(4) 交易完成；(5) 已退款；(6) 资金待结算。 |
| in\_complaint | boolean | 是否处在交易纠纷中。 |
| shipping | [object](#Res__order_list__shipping) | 发货信息。 |

**Res.order_list.shipping Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| delivery\_mode | number | 发货模式，发货模式枚举值：1、UNIFIED\_DELIVERY（统一发货）2、SPLIT\_DELIVERY（分拆发货） 示例值: UNIFIED\_DELIVERY |
| logistics\_type | number | 物流模式，发货方式枚举值：1、实体物流配送采用快递公司进行实体物流配送形式 2、同城配送 3、虚拟商品，虚拟商品，例如话费充值，点卡等，无实体配送形式 4、用户自提 |
| finish\_shipping | boolean | 是否已完成全部发货。 |
| goods\_desc | string | 在小程序后台发货信息录入页录入的商品描述。 |
| finish\_shipping\_count | number | 已完成全部发货的次数，未完成时为 0，完成时为 1，重新发货并完成后为 2。 |
| shipping\_list | [objarray](#Res__order_list__shipping__shipping_list<Array>) | 物流信息列表，发货物流单列表，支持统一发货（单个物流单）和分拆发货（多个物流单）两种模式。 |

**Res.order_list.shipping.shipping_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| tracking\_no | string | 物流单号，示例值: "323244567777"。 |
| express\_company | string | 同城配送公司名或物流公司编码，快递公司ID，参见[获取运力 id 列表get\_delivery\_list](../weixin-express/express-msg/api_get_delivery_list) 示例值: "DHL"。 |
| goods\_desc | string | 使用上传物流信息 API 录入的该物流信息的商品描述。 |
| upload\_time | number | 该物流信息的上传时间，时间戳形式。 |
| contact | [object](#Res__order_list__shipping__shipping_list<Array>__contact) | 联系方式。 |

**Res.order_list.shipping.shipping_list(Array).contact Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| consignor\_contact | string | 寄件人联系方式。 |
| receiver\_contact | string | 收件人联系方式。 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | system error。系统繁忙，此时请开发者稍候再试 |
| 10060001 | 支付单不存在。请检查微信支付单号形式下 transaction\_id 字段或商户侧单号形式下 mchid、out\_trade\_no 字段是否有误 |
| 10060002 | 支付单已完成发货，无法继续发货。请检查支付单发货情况 |
| 10060003 | 支付单已使用重新发货机会。支付单处于已发货状态时调用该API视为重新发货，仅可重新发货一次，请检查支付单发货情况 |
| 10060004 | 支付单处于不可发货的状态。请检查支付单状态 |
| 10060005 | 物流类型有误。按照文档中物流类型枚举填写该字段 |
| 10060006 | 非快递发货时不允许分拆发货。非快递发货时不允许分拆发货，请检查请求参数 |
| 10060007 | 分拆发货模式下必须填写 is\_all\_delivered 字段。请检查请求参数中的 is\_all\_delivered 字段 |
| 10060008 | 商品描述 item\_desc 字段不能为空。用于发货信息录入场景时商品描述字段不能为空 |
| 10060009 | 商品描述 item\_desc 字段太长。请检查商品描述字段 |
| 10060011 | last\_index不合法。请检查last\_index字段是否有误。 |
| 10060012 | 系统错误。系统繁忙，此时请开发者稍候再试 |
| 10060014 | 参数错误。根据错误原因描述修改参数 |
| 10060019 | 系统错误。系统繁忙，此时请开发者稍候再试 |
| 10060020 | 该笔支付单在没有任何商品描述的情况下不允许完成发货。请补充商品描述 item\_desc |
| 10060023 | 发货信息未更新。支付单信息不变 |
| 10060024 | 物流信息列表太长。支付单物流信息列表长度不可大于 15 |
| 10060025 | 物流公司编码太长。请检查物流公司编码是否有误 |
| 10060026 | 物流单号太长.。请检查物流单号是否有误 |
| 10060031 | 该笔支付单不属于 openid 所指定的用户。请检查支付单号或 openid 是否有误 |
| 268485194 | 订单单号类型非法。按照文档中订单单号类型枚举填写该字段 |
| 268485195 | 微信支付单号形式下 transaction\_id 字段不能为空。微信支付单号形式下 transaction\_id 字段必须设置 |
| 268485196 | 商户侧单号形式下 mchid 字段不能为空。商户侧单号形式下 mchid 字段必须设置 |
| 268485197 | 商户侧单号形式下 out\_trade\_no 字段不能为空。商户侧单号形式下 out\_trade\_no 字段必须设置 |
| 268485216 | 上传时间非法，请按照 RFC 3339 格式填写。上传时间必须满足 RFC 3339 格式，如 2022-12-15T13:29:35.120+08:00 |
| 268485224 | 发货模式非法。按照文档中发货模式枚举设置该字段 |
| 268485226 | 物流单号不能为空。物流快递发货时物流单号必须填写 |
| 268485227 | 物流公司编码不能为空。物流快递发货时物流公司编码必须填写 |
| 268485228 | 统一发货模式下，物流信息列表长度必须为 1。统一发货模式下，物流信息列表长度必须为 1 |

---

### 确认收货提醒

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/order_shipping/api_notifyconfirmreceive.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transaction\_id | string | 否 | 原支付交易对应的微信订单号。 |
| merchant\_id | string | 否 | 支付下单商户的商户号，由微信支付生成并下发。 |
| sub\_merchant\_id | string | 否 | 二级商户号。 |
| merchant\_trade\_no | string | 否 | 商户系统内部订单号，只能是数字、大小写字母`\_-\*`且在同一个商户号下唯一。 |
| received\_time | number | 是 | 快递签收时间，时间戳形式。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | system error。系统繁忙，此时请开发者稍候再试 |
| 10060001 | 支付单不存在。请检查微信支付单号形式下 transaction\_id 字段或商户侧单号形式下 mchid、out\_trade\_no 字段是否有误 |
| 10060002 | 支付单已完成发货，无法继续发货。请检查支付单发货情况 |
| 10060003 | 支付单已使用重新发货机会。支付单处于已发货状态时调用该API视为重新发货，仅可重新发货一次，请检查支付单发货情况 |
| 10060004 | 支付单处于不可发货的状态。请检查支付单状态 |
| 10060005 | 物流类型有误。按照文档中物流类型枚举填写该字段 |
| 10060006 | 非快递发货时不允许分拆发货。非快递发货时不允许分拆发货，请检查请求参数 |
| 10060007 | 分拆发货模式下必须填写 is\_all\_delivered 字段。请检查请求参数中的 is\_all\_delivered 字段 |
| 10060008 | 商品描述 item\_desc 字段不能为空。用于发货信息录入场景时商品描述字段不能为空 |
| 10060009 | 商品描述 item\_desc 字段太长。请检查商品描述字段 |
| 10060012 | 系统错误。系统繁忙，此时请开发者稍候再试 |
| 10060014 | 参数错误。根据错误原因描述修改参数 |
| 10060019 | 系统错误。系统繁忙，此时请开发者稍候再试 |
| 10060020 | 该笔支付单在没有任何商品描述的情况下不允许完成发货。请补充商品描述 item\_desc |
| 10060023 | 发货信息未更新。支付单信息不变 |
| 10060024 | 物流信息列表太长。支付单物流信息列表长度不可大于 15 |
| 10060025 | 物流公司编码太长。请检查物流公司编码是否有误 |
| 10060026 | 物流单号太长.。请检查物流单号是否有误 |
| 10060028 | 支付单不是已发货状态。请检查支付单状态 |
| 10060029 | 签收时间非法。请检查签收时间是否在发货时间之后 |
| 10060030 | 支付单已使用提醒收货机会。不可再提醒收货 |
| 10060031 | 该笔支付单不属于 openid 所指定的用户。请检查支付单号或 openid 是否有误 |
| 10060032 | 只有物流快递发货时允许提醒用户确认收货。请检查支付单物流类型 |
| 268485194 | 订单单号类型非法。按照文档中订单单号类型枚举填写该字段 |
| 268485195 | 微信支付单号形式下 transaction\_id 字段不能为空。微信支付单号形式下 transaction\_id 字段必须设置 |
| 268485196 | 商户侧单号形式下 mchid 字段不能为空。商户侧单号形式下 mchid 字段必须设置 |
| 268485197 | 商户侧单号形式下 out\_trade\_no 字段不能为空。商户侧单号形式下 out\_trade\_no 字段必须设置 |
| 268485216 | 上传时间非法，请按照 RFC 3339 格式填写。上传时间必须满足 RFC 3339 格式，如 2022-12-15T13:29:35.120+08:00 |
| 268485224 | 发货模式非法。按照文档中发货模式枚举设置该字段 |
| 268485226 | 物流单号不能为空。物流快递发货时物流单号必须填写 |
| 268485227 | 物流公司编码不能为空。物流快递发货时物流公司编码必须填写 |
| 268485228 | 统一发货模式下，物流信息列表长度必须为 1。统一发货模式下，物流信息列表长度必须为 1 |

---

### 消息跳转路径设置

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/order_shipping/api_setmsgjumppath.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 商户自定义跳转路径。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | system error。系统繁忙，此时请开发者稍候再试 |

---

### 查询小程序是否已开通发货信息管理服务

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/order_shipping/api_istrademanaged.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appid | string | 是 | 待查询小程序的 appid，非服务商调用时仅能查询本账号 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| is\_trade\_managed | boolean | - | 是否已开通小程序发货信息管理服务 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | system error。系统繁忙，此时请开发者稍候再试 |
| 40013 | appid非法。请检查appid是否有误 |
| 40097 | 请求参数非法。请检查appid是否已填写 |
| 44990 | 达到频控上限。系统繁忙，此时请开发者稍候再试 |
| 61003 | 服务商未被授权。请检查小程序是否已授权18或142权限集。 |
| 61004 | 客户端ip未授权。请检查调用端ip是否在服务商ip白名单中。 |
| 61011 | 服务商不合法。请检查access\_token是否有误 |

---

### 查询小程序是否已完成交易结算管理确认

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/order_shipping/api_istrademanagementconfirmationcompleted.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appid | string | 是 | 待查询小程序的 appid，非服务商调用时仅能查询本账号 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| completed | boolean | - | 是否已完成交易结算管理确认 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | system error。系统繁忙，此时请开发者稍候再试 |
| 40013 | appid非法。请检查appid是否有误 |
| 40097 | 请求参数非法。请检查appid是否已填写 |
| 44990 | 达到频控上限。系统繁忙，此时请开发者稍候再试 |
| 61003 | 服务商未被授权。请检查小程序是否已授权18或142权限集。 |
| 61004 | 客户端ip未授权。请检查调用端ip是否在服务商ip白名单中。 |
| 61011 | 服务商不合法。请检查access\_token是否有误 |

---

### 特殊发货报备

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/order_shipping/api_opspecialorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| order\_id | string | 是 | 需要特殊发货报备的订单号，可传入微信支付单号或商户单号 |
| type | number | 是 | 特殊发货报备类型，1为预售商品订单，2为测试订单 |
| delay\_to | number | 否 | 预计发货时间的unix时间戳，type为1时必填，type为2可省略 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 268546000 | type非法。请检查type |
| 268546001 | delay\_to非法。请检查delay\_to参数 |
| 268546002 | 账户不存在这个待发货单号。请检查单号是否有误 |

---

### 品牌申请

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/order_shipping/api_famousbrandapply.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| Application | [object](#Body__Application) | 是 | 申请品牌信息 |

**Body.Application Object Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| apply\_for | number | 是 | 品牌申请类型枚举值 | [枚举值](#Enum_Body__Application__apply_for) |
| audit\_info | [object](#Body__Application__audit_info) | 否 | 申请品牌信息，当申请类型为知名品牌时必填 | - |

**Body.Application.audit_info Object Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 | 枚举 |
| --- | --- | --- | --- | --- | --- |
| brand\_name | string | 是 | 我的小店 | 品牌名称 | - |
| brand\_type | number | 是 | 4 | 品牌类型 | [枚举值](#Enum_Body__Application__audit_info__brand_type) |
| flagship\_in\_which\_ec\_platform | string | 否 | 淘宝 | 当品牌类型是电商平台旗舰店为必填，表示该品牌是哪个电商平台的旗舰店 | - |
| ec\_platform\_proof\_list | array | 否 | - | 当品牌类型是电商平台旗舰店为必填，表示该品牌为官方旗舰店的佐证材料，使用[新增临时素材](../kf-mgnt/kf-message/api_uploadtempmedia)上传图片 | - |
| other\_material\_list | array | 否 | - | 其他补充说明材料，使用[新增临时素材](../kf-mgnt/kf-message/api_uploadtempmedia)上传图片 | - |
| authority\_certified\_proof\_list | array | 否 | - | 当品牌类型是有关部门认定的驰名商标时为必填，表示该品牌是有关部门认定的驰名商标、著名商标的佐证材料，使用[新增临时素材](../kf-mgnt/kf-message/api_uploadtempmedia)上传图片 | - |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | 错误原因 |

**Body.Application.apply_for Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 知名品牌 |
| 2 | 已接入小店商品组件 |

**Body.Application.audit_info.brand_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 工信部消费品名单 |
| 2 | 中国连锁经营协会网络零售 |
| 3 | 中华老字号 |
| 4 | 电商平台旗舰店 |
| 5 | 全球500强企业品牌 |
| 6 | 中国500强企业经营品牌 |
| 7 | 有关部门认定的驰名商标、著名商标 |
| 8 | 工信部消费名品成长企业名单 |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 10210001 | 参数错误 |
| 10210002 | 状态错误 |
| 10210003 | 图片解析失败 |

---

### 小程序品牌申请状态查询

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/order_shipping/api_getfamousbrandapplystatus.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | [错误码](#apierrcode) |
| errmsg | string | ok | 错误原因 |
| progress | [object](#Res__progress) | - | 品牌申请进度 |
| application | [object](#Res__application) | - | 申请品牌信息 |

**Res.progress Object Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| status | number | 品牌申请状态 | [枚举值](#Enum_Res__progress__status) |

**Res.application Object Payload**

| 参数名 | 类型 | 示例 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| apply\_for | number | 1 | 申请类型 | [枚举值](#Enum_Res__application__apply_for) |
| audit\_info | [object](#Res__application__audit_info) | - | 申请品牌信息 | - |
| status | number | - | 品牌申请状态 | [枚举值](#Enum_Res__application__status) |

**Res.application.audit_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| audit\_reason | string | 审核原因，只有在审核驳回时才有值 |

**Res.progress.status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 平台审核中 |
| 2 | 审核驳回 |
| 3 | 审核通过 |

**Res.application.apply_for Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 知名品牌 |
| 2 | 已接入小店商品组件 |

**Res.application.status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 平台审核中 |
| 2 | 审核驳回 |
| 3 | 审核通过 |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 41001 | access\_token missing |
| 42001 | access\_token expired |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 61004 | access clientip is not registered, not in ip-white-list |
| 10210001 | 参数错误 |
| 10210002 | 状态错误 |
| 10210003 | 图片解析失败 |

---

### 小程序交易类型变更申请

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/order_shipping/api_setwxatradetypecgi.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| trade\_type | number | 是 | 申请变更后的目标交易类型 | [枚举值](#Enum_Body__trade_type) |
| material\_list | [objarray](#Body__material_list<Array>) | 是 | 申请材料列表，最多10个，其中视频最多3个 | - |
| reason | string | 是 | 申请理由 | - |

**Body.material_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | number | 是 | 材料类型：1-图片，2-视频 |
| media\_id | string | 是 | 通过 [新增临时素材](../kf-mgnt/kf-message/api_uploadtempmedia) 接口上传后获取的 media\_id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**Body.trade_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 综合类 |
| 2 | 实物电商类 |
| 3 | 线下服务类 |
| 4 | 在线服务类 |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统错误 |
| 0 | ok | 成功 |
| 268486048 |  | 重复申请，一个账号只能申请一次 |

---

<!-- pages: 12 -->
