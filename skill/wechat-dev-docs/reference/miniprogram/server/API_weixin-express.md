# 小程序服务端 API 结构化参考 — API/weixin-express

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 查询运单

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/express-search/api_query_trace.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| waybill\_token | string | 是 | 查询id |
| openid | string | 否 | 用户openid |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| waybill\_info | [object](#Res__waybill_info) | 运单信息 |
| shop\_info | [object](#Res__shop_info) | 商品信息 |
| delivery\_info | [object](#Res__delivery_info) | 运力信息 |

**Res.waybill_info Object Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| status | number | 运单状态 | [枚举值](#Enum_Res__waybill_info__status) |
| waybill\_id | string | 运单号 | - |

**Res.shop_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| goods\_info | [object](#Res__shop_info__goods_info) | 商品信息 |

**Res.delivery_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| delivery\_id | string | 运力公司 id |
| delivery\_name | string | 运力公司名称 |

**Res.shop_info.goods_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| detail\_list | [object](#Res__shop_info__goods_info__detail_list) | 商品详情 |

**Res.shop_info.goods_info.detail_list Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| goods\_name | string | 商品名称(最大长度为utf-8编码下的60个字符） |
| goods\_img\_url | string | 商品图片url |

**Res.waybill_info.status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 运单不存在或者未揽收 |
| 1 | 已揽件 |
| 2 | 运输中 |
| 3 | 派件中 |
| 4 | 已签收 |
| 5 | 异常 |
| 6 | 代签收 |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40003 | invalid openid | 不合法的 OpenID ，请开发者确认 OpenID （该用户）是否已关注公众号，或是否是其他公众号的 OpenID |
| 9300507 | invalid token  can't decryption ordecryption result is different from the plaintext | waybill\_token参数错误 |
| 9300513 | out of quota | 调用次数达到上限 |
| 9300534 | invalid shop args | access\_token与openid参数不匹配 |
| 9300559 | waybill not exist | 运单不存在 |
| 9300560 | 达到修改次数上限 |  |

---

### 获取运力id列表

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/express-search/api_get_delivery_list.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| delivery\_list | [object](#Res__delivery_list) | delivery\_list |
| count | number | 运力公司个数 |

**Res.delivery_list Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| delivery\_id | string | 运力公司 id |
| delivery\_name | string | 运力公司名称 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40003 | invalid openid | 不合法的 OpenID ，请开发者确认 OpenID （该用户）是否已关注公众号，或是否是其他公众号的 OpenID |
| 9300507 | invalid token  can't decryption ordecryption result is different from the plaintext | waybill\_token参数错误 |
| 9300513 | out of quota | 调用次数达到上限 |
| 9300534 | invalid shop args | access\_token与openid参数不匹配 |
| 9300559 | waybill not exist | 运单不存在 |
| 9300560 | 达到修改次数上限 |  |

---

### 传运单

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/express-search/api_trace_waybill.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户openid |
| sender\_phone | string | 否 | 寄件人手机号 |
| receiver\_phone | string | 是 | 收件人手机号，部分运力需要用户手机号作为查单依据 |
| waybill\_id | string | 是 | 运单号 |
| goods\_info | [object](#Body__goods_info) | 是 | 商品信息 |
| trans\_id | string | 是 | 交易单号（微信支付生成的交易单号，一般以420开头） |
| order\_detail\_path | string | 是 | 点击落地页商品卡片跳转路径（建议为订单详情页path），不传默认跳转小程序首页。 |
| delivery\_id | string | 否 | 运力id（运单号所属运力公司id），该字段从 [get\_delivery\_list](../express-msg/api_get_delivery_list) 获取。 该参数用于提高运单号识别的准确度；特别是对非主流快递公司，建议传入该参数，确保查询正确率。 |

**Body.goods_info Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| detail\_list | [objarray](#Body__goods_info__detail_list<Array>) | 是 | 商品信息 |

**Body.goods_info.detail_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| goods\_name | string | 是 | 商品名称 |
| goods\_img\_url | string | 是 | 商品图片url |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| waybill\_token | string | 查询id |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40003 | invalid openid | 不合法的 OpenID ，请开发者确认 OpenID （该用户）是否已关注公众号，或是否是其他公众号的 OpenID |
| 9300507 | invalid token  can't decryption ordecryption result is different from the plaintext | waybill\_token参数错误 |
| 9300513 | out of quota | 调用次数达到上限 |
| 9300534 | invalid shop args | access\_token与openid参数不匹配 |
| 9300559 | waybill not exist | 运单不存在 |
| 9300560 | 达到修改次数上限 |  |

---

### 更新物流信息

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/express-search/api_update_waybill_goods.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| waybill\_token | string | 是 | 查询id |
| goods\_info | [object](#Body__goods_info) | 是 | 商品信息 |

**Body.goods_info Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| detail\_list | [objarray](#Body__goods_info__detail_list<Array>) | 是 | 商品信息 |

**Body.goods_info.detail_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| goods\_name | string | 是 | 商品名称(最大长度为utf-8编码下的60个字符） |
| goods\_img\_url | string | 是 | 商品图片url |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40003 | invalid openid | 不合法的 OpenID ，请开发者确认 OpenID （该用户）是否已关注公众号，或是否是其他公众号的 OpenID |
| 9300507 | invalid token  can't decryption ordecryption result is different from the plaintext | waybill\_token参数错误 |
| 9300513 | out of quota | 调用次数达到上限 |
| 9300534 | invalid shop args | access\_token与openid参数不匹配 |
| 9300559 | waybill not exist | 运单不存在 |
| 9300560 | 达到修改次数上限 |  |

---

### 更新物品信息接口

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/express-msg/api_update_follow_waybill_goods.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| waybill\_token | string | 是 | 查询id |
| goods\_info | [object](#Body__goods_info) | 是 | 商品信息 |

**Body.goods_info Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| detail\_list | [objarray](#Body__goods_info__detail_list<Array>) | 是 | 商品信息 |

**Body.goods_info.detail_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| goods\_name | string | 是 | 商品名称 |
| goods\_img\_url | string | 是 | 商品图片url |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40003 | invalid openid | 不合法的 OpenID ，请开发者确认 OpenID （该用户）是否已关注公众号，或是否是其他公众号的 OpenID |
| 9300507 | invalid token  can't decryption ordecryption result is different from the plaintext | waybill\_token参数错误 |
| 9300513 | out of quota | 调用次数达到上限 |
| 9300534 | invalid shop args | access\_token与openid参数不匹配 |
| 9300559 | waybill not exist | 运单不存在 |
| 9300560 | 达到修改次数上限 |  |

---

### 查运单

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/express-msg/api_query_follow_trace.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| waybill\_token | string | 是 | 查询id |
| openid | string | 否 | 用户openid |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| waybill\_info | [object](#Res__waybill_info) | 运单信息 |
| shop\_info | [object](#Res__shop_info) | 商品信息 |
| delivery\_info | [object](#Res__delivery_info) | 运力信息 |

**Res.waybill_info Object Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| status | number | 运单状态 | [枚举值](#Enum_Res__waybill_info__status) |
| waybill\_id | string | 运单号 | - |

**Res.shop_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| goods\_info | [object](#Res__shop_info__goods_info) | 商品信息 |

**Res.delivery_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| delivery\_id | string | 运力公司 id |
| delivery\_name | string | 运力公司名称 |

**Res.shop_info.goods_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| detail\_list | [object](#Res__shop_info__goods_info__detail_list) | 商品详情 |

**Res.shop_info.goods_info.detail_list Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| goods\_name | string | 商品名称(最大长度为utf-8编码下的60个字符） |
| goods\_img\_url | string | 商品图片url |

**Res.waybill_info.status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 运单不存在或者未揽收 |
| 1 | 已揽件 |
| 2 | 运输中 |
| 3 | 派件中 |
| 4 | 已签收 |
| 5 | 异常 |
| 6 | 代签收 |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40003 | invalid openid | 不合法的 OpenID ，请开发者确认 OpenID （该用户）是否已关注公众号，或是否是其他公众号的 OpenID |
| 9300507 | invalid token  can't decryption ordecryption result is different from the plaintext | waybill\_token参数错误 |
| 9300513 | out of quota | 调用次数达到上限 |
| 9300534 | invalid shop args | access\_token与openid参数不匹配 |
| 9300559 | waybill not exist | 运单不存在 |
| 9300560 | 达到修改次数上限 |  |

---

### 传运单

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/express-msg/api_follow_waybill.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户openid |
| sender\_phone | string | 否 | 寄件人手机号 |
| receiver\_phone | string | 是 | 收件人手机号，部分运力需要用户手机号作为查单依据 |
| waybill\_id | string | 是 | 运单号 |
| goods\_info | [object](#Body__goods_info) | 是 | 商品信息 |
| trans\_id | string | 是 | 交易单号（微信支付生成的交易单号，一般以420开头） |
| order\_detail\_path | string | 是 | 点击落地页商品卡片跳转路径（建议为订单详情页path），不传默认跳转小程序首页。 |
| delivery\_id | string | 否 | 运力id（运单号所属运力公司id），该字段从 [get\_delivery\_list](api_get_delivery_list) 获取。 该参数用于提高运单号识别的准确度；特别是对非主流快递公司，建议传入该参数，确保查询正确率。 |

**Body.goods_info Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| detail\_list | [objarray](#Body__goods_info__detail_list<Array>) | 是 | 商品信息 |

**Body.goods_info.detail_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| goods\_name | string | 是 | 商品名称 |
| goods\_img\_url | string | 是 | 商品图片url |
| goods\_desc | string | 否 | 商品详情描述，不传默认取“商品名称”值，最多40汉字 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| waybill\_token | string | 查询id |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40003 | invalid openid | 不合法的 OpenID ，请开发者确认 OpenID （该用户）是否已关注公众号，或是否是其他公众号的 OpenID |
| 9300507 | invalid token  can't decryption ordecryption result is different from the plaintext | waybill\_token参数错误 |
| 9300513 | out of quota | 调用次数达到上限 |
| 9300534 | invalid shop args | access\_token与openid参数不匹配 |
| 9300559 | waybill not exist | 运单不存在 |
| 9300560 | 达到修改次数上限 |  |

---

### 获取运力id列表

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/express-msg/api_get_delivery_list.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| delivery\_list | [object](#Res__delivery_list) | delivery\_list |
| count | number | 运力公司个数 |

**Res.delivery_list Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| delivery\_id | string | 运力公司 id |
| delivery\_name | string | 运力公司名称 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40003 | invalid openid | 不合法的 OpenID ，请开发者确认 OpenID （该用户）是否已关注公众号，或是否是其他公众号的 OpenID |
| 9300507 | invalid token  can't decryption ordecryption result is different from the plaintext | waybill\_token参数错误 |
| 9300513 | out of quota | 调用次数达到上限 |
| 9300534 | invalid shop args | access\_token与openid参数不匹配 |
| 9300559 | waybill not exist | 运单不存在 |
| 9300560 | 达到修改次数上限 |  |

---

### 开通无忧退货

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/freight/api_insurance_freight_open.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

---

### 查询开通状态

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/freight/api_insurance_freight_query_open.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| errcode | number | [错误码](#apierrcode) | - |
| errmsg | string | [错误描述](#apierrcode) | - |
| is\_open | number | 是否开通 | [枚举值](#Enum_Res__is_open) |

**Res.is_open Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 否 |
| 1 | 是 |

---

### 发货时投保

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/freight/api_insurance_freight_createorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 买家openid，必须和理赔openid一致 |
| order\_no | string | 是 | 微信支付单号，一个微信支付单号只能投保一次 |
| pay\_time | number | 是 | 微信支付时间，秒级时间戳，时间误差3天内 |
| pay\_amount | number | 是 | 微信支付金额（单位：分） |
| delivery\_no | string | 是 | 发货运单号 |
| delivery\_place | [object](#Body__delivery_place) | 是 | 发货地址 |
| receipt\_place | [object](#Body__delivery_place) | 是 | 收货地址 |
| product\_info | [object](#Body__product_info) | 是 | 投保订单信息，用于微信下发投保和理赔通知给用户，用户点击可查看投保订单，点击订单可跳回商家小程序 |

**Body.delivery_place Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| province | string | 是 | 省 |
| city | string | 是 | 市 |
| county | string | 是 | 区 |
| address | string | 是 | 详细地址 |

**Body.product_info Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| order\_path | string | 是 | 投保订单在商家小程序的path |
| goods\_list | [objarray](#Body__product_info__goods_list<Array>) | 是 | 投保商品list，一个元素为对象的数组 |

**Body.product_info.goods_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 投保商品名称 |
| url | string | 是 | 投保商品图片url |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| policy\_no | string | 保单号 |
| insurance\_end\_date | string | 保险止期，格式: yyyy-mm-dd hh24:mi:ss |
| estimate\_amount | number | 保险公司预估理赔金额，单位： 分 |
| premium | number | 保费，单位： 分 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 41009 | missing openid |

---

### 无忧退理赔

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/freight/api_insurance_freight_claim.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 买家openid，与投保保持一致 |
| order\_no | string | 是 | 微信支付单号，与投保保持一致 |
| refund\_delivery\_no | string | 是 | 退款运单号，理赔退款运单号唯一 |
| refund\_company | string | 是 | 退款快递公司 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| report\_no | string | 理赔报案号，成功申请理赔时返回 | - |
| is\_home\_pick\_up | number | 是否上门取件 | [枚举值](#Enum_Res__is_home_pick_up) |

**Res.is_home_pick_up Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 否 |
| 1 | 是 |

---

### 申请充值订单号

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/freight/api_insurance_freight_createchargeid.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| quota | number | 是 | 充值金额，单位：分 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| order\_id | number | 充值订单id |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

---

### 申请支付

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/freight/api_insurance_freight_applypay.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| order\_id | number | 是 | 充值订单id，与[申请充值订单号](api_insurance_freight_createchargeid)保持一致，js等语言防止精度错误传string |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| pay\_url | string | 充值链接 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

---

### 拉取充值订单信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/freight/api_insurance_freight_getpayorderlist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| status\_list | numarray | 是 | 订单状态 | [枚举值](#Enum_Body__status_list) |
| offset | number | 否 | 分页offset | - |
| limit | number | 否 | 分页limit | - |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| total | number | 总数 |
| list | [objarray](#Res__list<Array>) | 充值订单列表 |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| order\_id | number | 充值单号 | - |
| order\_status | number | 订单状态 | [枚举值](#Enum_Res__list<Array>__order_status) |
| total\_price | number | 充值金额 | - |
| create\_time | number | 订单创建时间 | - |
| pay\_time | number | 支付时间 | - |
| can\_refund | number | 是否可以退款 | - |
| refund\_time | number | 退款时间 | - |
| refund\_status | number | 退款状态 | [枚举值](#Enum_Res__list<Array>__refund_status) |
| refund\_amt | number | 退款金额 | - |

**Body.status_list Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 待支付 |
| 2 | 支付成功 |
| 3 | 使用中 |
| 4 | 已用完 |
| 5 | 退款中 |
| 6 | 已退款 |
| 10 | 支付超时 |

**Res.list(Array).order_status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 待支付 |
| 2 | 支付成功 |
| 3 | 使用中 |
| 4 | 已用完 |
| 5 | 退款中 |
| 6 | 已退款 |
| 10 | 支付超时 |

**Res.list(Array).refund_status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 未退款 |
| 2 | 退款中 |
| 4 | 退款成功 |
| 5 | 退款失败 |

---

### 充值保费退款

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/freight/api_insurance_freight_refund.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

---

### 拉取理赔摘要

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/freight/api_insurance_freight_getsummary.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin\_time | number | 是 | 查询开始时间， |
| end\_time | number | 是 | 查询结束时间戳，秒级时间戳 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| total | number | 投保总数 |
| claim\_num | number | 理赔总数 |
| claim\_succ\_num | number | 理赔成功数 |
| premium | number | 当前保费，单位: 分 |
| funds | number | 当前账号余额，单位: 分 |
| need\_close | boolean | 是否不能投保，系统安全原因不能投保 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -202 | 内部错误 | 可在一段时间后重试 |

---

### 拉取保单信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/freight/api_insurance_freight_getorderlist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| openid | string | 否 | 买家openid，与投保理赔保持一致 | - |
| order\_no | string | 否 | 微信支付单号，与投保理赔保持一致 | - |
| policy\_no | string | 否 | 保单号 | - |
| report\_no | string | 否 | 理赔报案号 | - |
| delivery\_no | string | 否 | 发货运单号 | - |
| refund\_delivery\_no | string | 否 | 退款运单号 | - |
| begin\_time | number | 否 | 查询开始时间，秒级时间戳 | - |
| end\_time | number | 否 | 查询结束时间，秒级时间戳 | - |
| status\_list | numarray | 否 | 保单状态 | [枚举值](#Enum_Body__status_list) |
| offset | number | 否 | 分页offset | - |
| limit | number | 否 | 分页limit（默认为100，最大为100） | - |
| sort\_direct | number | 否 | 排序方式 | [枚举值](#Enum_Body__sort_direct) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| total | number | 总数 |
| list | [objarray](#Res__list<Array>) | 保单列表 |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| order\_no | string | 微信支付单号 | - |
| policy\_no | string | 保单号 | - |
| report\_no | string | 理赔报案号 | - |
| delivery\_no | string | 发货运单号 | - |
| refund\_delivery\_no | string | 退款运单号 | - |
| premium | number | 保费（单位：分 ） | - |
| estimate\_amount | number | 预估理赔金额（单位：分 ） | - |
| status | number | 保单状态 | [枚举值](#Enum_Res__list<Array>__status) |
| pay\_fail\_reason | string | 理赔打款失败原因 | - |
| pay\_finish\_time | number | 理赔款打给用户的时间 | - |
| is\_home\_pick\_up | number | 是否上门取件 | [枚举值](#Enum_Res__list<Array>__is_home_pick_up) |

**Body.status_list Enum**

| 枚举值 | 描述 |
| --- | --- |
| 2 | 保障中 |
| 4 | 理赔中 |
| 5 | 理赔成功 |
| 6 | 理赔失败 |
| 7 | 投保过期 |

**Body.sort_direct Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | create\_time正序 |
| 1 | create\_time倒序 |

**Res.list(Array).status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 2 | 保障中 |
| 4 | 理赔中 |
| 5 | 理赔成功 |
| 6 | 理赔失败 |
| 7 | 投保过期 |

**Res.list(Array).is_home_pick_up Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 否 |
| 1 | 是 |

---

### 设置保费告警余额

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/freight/api_insurance_freight_update_notify_funds.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| notify\_funds | number | 是 | 通知的金额（单位：分；设置为0不通知） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

---

### 解绑退货ID

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/express-return/api_unbindreturnid.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| return\_id | string | 是 | 退货ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 请联系微信平台解决 |
| 40097 | return\_id为空 |
| 931023 | 运单不存在 |

---

### 查询退货ID状态

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/express-return/api_getreturnid.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| return\_id | string | 是 | 退货ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| status | number | 退货方式，0.用户未填写退货信息 1.预约上门取件 2.填写自行寄回运单号 |
| waybill\_id | string | 运单号 |
| order\_status | number | 物流信息，0.已下单待揽件 1.已揽件 2.运输中 3.派件中 4.已签收 5.异常 6.代签收 7.揽收失败 8.签收失败（拒收，超区） 11.已取消 13.退件中 14.已退件 99.未知 |
| delivery\_id | string | 运力公司编码 |
| delivery\_name | string | 运力公司名称 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 请联系微信平台解决 |
| 40097 | return\_id为空 |
| 931023 | 运单不存在 |

---

### 创建退货ID

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/express-return/api_addreturnid.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shop\_order\_id | string | 是 | 商家内部系统使用的退货编号 |
| biz\_addr | [object](#Body__biz_addr) | 是 | 商家退货地址 |
| user\_addr | [object](#Body__user_addr) | 否 | 用户购物时的收货地址 |
| openid | string | 是 | 退货用户的openid |
| order\_path | string | 是 | 退货订单在商家小程序的path。如投保时已传入订单商品信息，则以投保时传入的为准 |
| goods\_list | [objarray](#Body__goods_list<Array>) | 是 | 退货商品list，一个元素为对象的数组,结构如下↓ 如投保时已传入订单商品信息，则以投保时传入的为准 |
| order\_price | number | 是 | 退货订单的价格 |
| wx\_pay\_id | string | 是 | 填写已投保的微信支付单号 |

**Body.biz_addr Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 发/收件人姓名，不超过64字节 |
| tel | string | 是 | 发/收件人座机号码，若不填写则必须填写 mobile，不超过32字节 |
| mobile | string | 是 | 发/收件人手机号码，若不填写则必须填写 tel，不超过32字节 |
| company | string | 是 | 发/收件人公司名称，不超过64字节 |
| post\_code | string | 是 | 发/收件人邮编，不超过10字节 |
| country | string | 是 | 发/收件人国家，不超过64字节 |
| province | string | 是 | 发/收件人省份，比如："广东省"，不超过64字节 |
| city | string | 是 | 发/收件人市/地区，比如："广州市"，不超过64字节 |
| area | string | 是 | 发/收件人区/县，比如："海珠区"，不超过64字节 |
| address | string | 是 | 发/收件人详细地址，比如："XX路XX号XX大厦XX"，不超过512字节 |

**Body.user_addr Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 否 | 发/收件人姓名，不超过64字节 |
| tel | string | 否 | 发/收件人座机号码，若不填写则必须填写 mobile，不超过32字节 |
| mobile | string | 否 | 发/收件人手机号码，若不填写则必须填写 tel，不超过32字节 |
| company | string | 否 | 发/收件人公司名称，不超过64字节 |
| post\_code | string | 否 | 发/收件人邮编，不超过10字节 |
| country | string | 否 | 发/收件人国家，不超过64字节 |
| province | string | 否 | 发/收件人省份，比如："广东省"，不超过64字节 |
| city | string | 否 | 发/收件人市/地区，比如："广州市"，不超过64字节 |
| area | string | 否 | 发/收件人区/县，比如："海珠区"，不超过64字节 |
| address | string | 否 | 发/收件人详细地址，比如："XX路XX号XX大厦XX"，不超过512字节 |

**Body.goods_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 退货商品的名称 |
| url | string | 是 | 退货商品图片的url |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| return\_id | string | 退货ID |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 请联系微信平台解决 |
| 40097 | order\_id为空或者退货地址为空或者wx\_pay\_id为空 |
| 9300522 | shop\_order\_id 已存在 |
| 9300569 | wx\_pay\_id 为空 |
| 9300570 | 该微信支付单号填写错误或未投保 |

---

### 开通门店权限

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_apply.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | 错误码。0:请求成功，其他：请求失败 |
| errmsg | string | ok | 错误信息。 |

**物品类型列表**

| 物品类型 | 类型名称 |
| --- | --- |
| 1 | 快餐 |
| 2 | 药品 |
| 3 | 百货 |
| 6 | 生鲜 |
| 8 | 酒品 |
| 12 | 文件 |
| 13 | 蛋糕 |
| 14 | 鲜花 |
| 15 | 数码 |
| 16 | 服装 |
| 17 | 汽配 |
| 18 | 珠宝 |
| 32 | 饮料 |
| 36 | 证照 |
| 55 | 宠物用品 |
| 56 | 母婴用品 |
| 57 | 美妆用品 |
| 58 | 家居建材 |
| 99 | 其他 |

**运力列表**

| 运力名称 | 运力ID |
| --- | --- |
| 达达 | DADA |
| 顺丰同城 | SFTC |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 请求成功 |
| 48001 | api unauthorized。原因是小程序没有获得同城配送接口权限，在小程序管理后台开通【同城配送】后即可 |
| 61007 | api is unauthorized to component。此小程序没有授权当前服务商调用接口权限，服务商需获得小程序的51接口权限集 |
| 934000 | 其他逻辑错误 |
| 934001 | 请求参数有误，详细看错误提示 |
| 934002 | 订单已存在，且订单在处理中,请勿重复添加 |
| 934003 | 运力ID错误 |
| 934005 | 运力预创建订单错误 |
| 934006 | 有在途订单，暂不能退款，请等待配送完成 |
| 934007 | 不是在途订单 |
| 934008 | 门店ID和APPID不匹配 |
| 934009 | 不支持该门店所在城市 |
| 934010 | 重复创建门店，请更换out\_store\_id |
| 934011 | 请求签名错误 |
| 934011 | signature is needed, please refer document for help [https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting\_started/api\_signature.html]([https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)。 原因是接口没有带签名验证信息，可以参照[微信服务端api签名指南](https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)的指引开发，同时社区内也有同行分享的[php](https://developers.weixin.qq.com/community/develop/article/doc/00028ca675c708b23f100b8e161013)和[java](https://developers.weixin.qq.com/community/develop/article/doc/000e68b8038ed8796f00f6c2f68c13)的开发实践经验。 |
| 934012 | appid和access\_token不匹配 |
| 934013 | 门店余额不足无法下单 |
| 934014 | 运力公司返回了非法金额 |
| 934015 | 余额扣减失败 |
| 934016 | 订单不存在 |
| 934017 | 订单处在不能被取消的状态 |
| 934018 | 订单已取消，请勿重复操作 |
| 934019 | 超出运力支持的配送范围 |
| 934019 | 沙箱环境下单接口返回934019 用户超出配送范围 解决方法：使用顺丰的沙箱环境环境需要固定的收件人信息（达达没有要求） 收件人信息如下：收件人姓名：顺丰同城 收件人手机：13881979410 收件地址：北京市海淀区学清嘉创大厦A座15层 |
| 934020 | 商品超重 |
| 934021 | 门店不存在 |
| 934022 | 账号类型不可以为个人账号 |
| 934023 | 小程序类型必须为普通小程序 |
| 934999 | 内部系统错误 |

---

### 创建门店

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_createstore.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| out\_store\_id | string | 否 | 自定义门店编号 | - |
| store\_name | string | 否 | 门店名称 | - |
| order\_pattern | number | 否 | 运力偏好。1：价格优先，2：运力优先, 默认价格优先 | - |
| service\_trans\_prefer | string | 否 | 优先使用的运力ID。order\_pattern = 2时必填 | [枚举值](#Enum_Body__service_trans_prefer) |
| address\_info | [object](#Body__address_info) | 否 | 门店地址信息。务必要传入正确的门店地址作为发货地址 | - |

**Body.address_info Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| province | string | 是 | 省/自治区/直辖市。xxx省,xxx自治区,xxx市 |
| city | string | 是 | 地级市。xxx市 |
| area | string | 是 | 县/县级市/区。xxx区, xxx县 |
| street | string | 否 | 街道。xxx街道 |
| house | string | 是 | 具体门牌号或详细地址。xxxx号 |
| lat | double | 是 | 门店所在地纬度 |
| lng | double | 是 | 门店所在地经度 |
| phone | string | 是 | 门店联系电话。11位手机号或11位带区号的固话:020-8080880 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | 错误码。0:请求成功，其他：请求失败 |
| errmsg | string | ok | 错误信息。 |
| wx\_store\_id | string | - | 微信门店编号，在请求成功时返回 |
| appid | string | - | 小程序appid，在请求成功时返回 |
| out\_store\_id | string | - | 自定义门店ID，在请求成功时返回 |

**Body.service_trans_prefer Enum**

| 枚举值 | 描述 |
| --- | --- |
| DADA | 达达 |
| SFTC | 顺丰同城 |

**物品类型列表**

| 物品类型 | 类型名称 |
| --- | --- |
| 1 | 快餐 |
| 2 | 药品 |
| 3 | 百货 |
| 6 | 生鲜 |
| 8 | 酒品 |
| 12 | 文件 |
| 13 | 蛋糕 |
| 14 | 鲜花 |
| 15 | 数码 |
| 16 | 服装 |
| 17 | 汽配 |
| 18 | 珠宝 |
| 32 | 饮料 |
| 36 | 证照 |
| 55 | 宠物用品 |
| 56 | 母婴用品 |
| 57 | 美妆用品 |
| 58 | 家居建材 |
| 99 | 其他 |

**运力列表**

| 运力名称 | 运力ID |
| --- | --- |
| 达达 | DADA |
| 顺丰同城 | SFTC |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 请求成功 |
| 48001 | api unauthorized。原因是小程序没有获得同城配送接口权限，在小程序管理后台开通【同城配送】后即可 |
| 61007 | api is unauthorized to component。此小程序没有授权当前服务商调用接口权限，服务商需获得小程序的51接口权限集 |
| 934000 | 其他逻辑错误 |
| 934001 | 请求参数有误，详细看错误提示 |
| 934002 | 订单已存在，且订单在处理中,请勿重复添加 |
| 934003 | 运力ID错误 |
| 934005 | 运力预创建订单错误 |
| 934006 | 有在途订单，暂不能退款，请等待配送完成 |
| 934007 | 不是在途订单 |
| 934008 | 门店ID和APPID不匹配 |
| 934009 | 不支持该门店所在城市 |
| 934010 | 重复创建门店，请更换out\_store\_id |
| 934011 | 请求签名错误 |
| 934011 | signature is needed, please refer document for help [https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting\_started/api\_signature.html]([https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)。 原因是接口没有带签名验证信息，可以参照[微信服务端api签名指南](https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)的指引开发，同时社区内也有同行分享的[php](https://developers.weixin.qq.com/community/develop/article/doc/00028ca675c708b23f100b8e161013)和[java](https://developers.weixin.qq.com/community/develop/article/doc/000e68b8038ed8796f00f6c2f68c13)的开发实践经验。 |
| 934012 | appid和access\_token不匹配 |
| 934013 | 门店余额不足无法下单 |
| 934014 | 运力公司返回了非法金额 |
| 934015 | 余额扣减失败 |
| 934016 | 订单不存在 |
| 934017 | 订单处在不能被取消的状态 |
| 934018 | 订单已取消，请勿重复操作 |
| 934019 | 超出运力支持的配送范围 |
| 934019 | 沙箱环境下单接口返回934019 用户超出配送范围 解决方法：使用顺丰的沙箱环境环境需要固定的收件人信息（达达没有要求） 收件人信息如下：收件人姓名：顺丰同城 收件人手机：13881979410 收件地址：北京市海淀区学清嘉创大厦A座15层 |
| 934020 | 商品超重 |
| 934021 | 门店不存在 |
| 934022 | 账号类型不可以为个人账号 |
| 934023 | 小程序类型必须为普通小程序 |
| 934999 | 内部系统错误 |

---

### 查询门店

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_querystore.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wx\_store\_id | string | 否 | 微信门店编号 |
| out\_store\_id | string | 否 | 自定义门店编号 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | 错误码。0:请求成功，其他：请求失败 |
| errmsg | string | ok | 错误信息。 |
| store\_list | [objarray](#Res__store_list<Array>) | - | 门店信息列表，在请求成功时返回 |
| total | number | - | 符合条件的门店总数 |
| appid | string | - | 小程序appid |

**Res.store_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| wx\_store\_id | string | 微信门店编号 |
| out\_store\_id | string | 自定义门店编号 |
| city\_id | string | 门店所在城市ID |
| order\_pattern | number | 运力偏好 |
| service\_trans\_prefer | string | 优先使用的运力ID |
| address\_info | [object](#Res__store_list<Array>__address_info) | 门店地址信息 |

**Res.store_list(Array).address_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| province | string | 省/自治区/直辖市。xxx省,xxx自治区,xxx市 |
| city | string | 地级市。xxx市 |
| area | string | 县/县级市/区。xxx区, xxx县 |
| street | string | 街道。xxx街道 |
| house | string | 具体门牌号或详细地址。xxxx号 |
| lat | double | 门店所在地纬度 |
| lng | double | 门店所在地经度 |
| phone | string | 门店联系电话。11位手机号或11位带区号的固话:020-8080880 |

**物品类型列表**

| 物品类型 | 类型名称 |
| --- | --- |
| 1 | 快餐 |
| 2 | 药品 |
| 3 | 百货 |
| 6 | 生鲜 |
| 8 | 酒品 |
| 12 | 文件 |
| 13 | 蛋糕 |
| 14 | 鲜花 |
| 15 | 数码 |
| 16 | 服装 |
| 17 | 汽配 |
| 18 | 珠宝 |
| 32 | 饮料 |
| 36 | 证照 |
| 55 | 宠物用品 |
| 56 | 母婴用品 |
| 57 | 美妆用品 |
| 58 | 家居建材 |
| 99 | 其他 |

**运力列表**

| 运力名称 | 运力ID |
| --- | --- |
| 达达 | DADA |
| 顺丰同城 | SFTC |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 请求成功 |
| 48001 | api unauthorized。原因是小程序没有获得同城配送接口权限，在小程序管理后台开通【同城配送】后即可 |
| 61007 | api is unauthorized to component。此小程序没有授权当前服务商调用接口权限，服务商需获得小程序的51接口权限集 |
| 934000 | 其他逻辑错误 |
| 934001 | 请求参数有误，详细看错误提示 |
| 934002 | 订单已存在，且订单在处理中,请勿重复添加 |
| 934003 | 运力ID错误 |
| 934005 | 运力预创建订单错误 |
| 934006 | 有在途订单，暂不能退款，请等待配送完成 |
| 934007 | 不是在途订单 |
| 934008 | 门店ID和APPID不匹配 |
| 934009 | 不支持该门店所在城市 |
| 934010 | 重复创建门店，请更换out\_store\_id |
| 934011 | 请求签名错误 |
| 934011 | signature is needed, please refer document for help [https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting\_started/api\_signature.html]([https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)。 原因是接口没有带签名验证信息，可以参照[微信服务端api签名指南](https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)的指引开发，同时社区内也有同行分享的[php](https://developers.weixin.qq.com/community/develop/article/doc/00028ca675c708b23f100b8e161013)和[java](https://developers.weixin.qq.com/community/develop/article/doc/000e68b8038ed8796f00f6c2f68c13)的开发实践经验。 |
| 934012 | appid和access\_token不匹配 |
| 934013 | 门店余额不足无法下单 |
| 934014 | 运力公司返回了非法金额 |
| 934015 | 余额扣减失败 |
| 934016 | 订单不存在 |
| 934017 | 订单处在不能被取消的状态 |
| 934018 | 订单已取消，请勿重复操作 |
| 934019 | 超出运力支持的配送范围 |
| 934019 | 沙箱环境下单接口返回934019 用户超出配送范围 解决方法：使用顺丰的沙箱环境环境需要固定的收件人信息（达达没有要求） 收件人信息如下：收件人姓名：顺丰同城 收件人手机：13881979410 收件地址：北京市海淀区学清嘉创大厦A座15层 |
| 934020 | 商品超重 |
| 934021 | 门店不存在 |
| 934022 | 账号类型不可以为个人账号 |
| 934023 | 小程序类型必须为普通小程序 |
| 934999 | 内部系统错误 |

---

### 更新门店

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_updatestore.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keys | [object](#Body__keys) | 是 | 门店编号 |
| content | [object](#Body__content) | 是 | 更新内容 |

**Body.keys Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wx\_store\_id | string | 否 | 微信门店编号 wx\_store\_id和out\_store\_id二选一 |
| out\_store\_id | string | 否 | 自定义门店编号 wx\_store\_id和out\_store\_id二选一 |

**Body.content Object Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| store\_name | string | 否 | 门店名称 | - |
| order\_pattern | string | 否 | 运力偏好 | - |
| service\_trans\_prefer | string | 否 | 优先使用的运力ID,order\_pattern = 2时必填 | [枚举值](#Enum_Body__content__service_trans_prefer) |
| address\_info | [object](#Body__content__address_info) | 否 | 门店地址信息 | - |

**Body.content.address_info Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| province | string | 是 | 省/自治区/直辖市。xxx省,xxx自治区,xxx市 |
| city | string | 是 | 地级市。xxx市 |
| area | string | 是 | 县/县级市/区。xxx区, xxx县 |
| street | string | 否 | 街道。xxx街道 |
| house | string | 是 | 具体门牌号或详细地址。xxxx号 |
| lat | double | 是 | 门店所在地纬度 |
| lng | double | 是 | 门店所在地经度 |
| phone | string | 是 | 门店联系电话。11位手机号或11位带区号的固话:020-8080880 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | 错误码。0:请求成功，其他：请求失败 |
| errmsg | string | ok | 错误信息。 |

**Body.content.service_trans_prefer Enum**

| 枚举值 | 描述 |
| --- | --- |
| DADA | 达达 |
| SFTC | 顺丰同城 |

**物品类型列表**

| 物品类型 | 类型名称 |
| --- | --- |
| 1 | 快餐 |
| 2 | 药品 |
| 3 | 百货 |
| 6 | 生鲜 |
| 8 | 酒品 |
| 12 | 文件 |
| 13 | 蛋糕 |
| 14 | 鲜花 |
| 15 | 数码 |
| 16 | 服装 |
| 17 | 汽配 |
| 18 | 珠宝 |
| 32 | 饮料 |
| 36 | 证照 |
| 55 | 宠物用品 |
| 56 | 母婴用品 |
| 57 | 美妆用品 |
| 58 | 家居建材 |
| 99 | 其他 |

**运力列表**

| 运力名称 | 运力ID |
| --- | --- |
| 达达 | DADA |
| 顺丰同城 | SFTC |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 请求成功 |
| 48001 | api unauthorized。原因是小程序没有获得同城配送接口权限，在小程序管理后台开通【同城配送】后即可 |
| 61007 | api is unauthorized to component。此小程序没有授权当前服务商调用接口权限，服务商需获得小程序的51接口权限集 |
| 934000 | 其他逻辑错误 |
| 934001 | 请求参数有误，详细看错误提示 |
| 934002 | 订单已存在，且订单在处理中,请勿重复添加 |
| 934003 | 运力ID错误 |
| 934005 | 运力预创建订单错误 |
| 934006 | 有在途订单，暂不能退款，请等待配送完成 |
| 934007 | 不是在途订单 |
| 934008 | 门店ID和APPID不匹配 |
| 934009 | 不支持该门店所在城市 |
| 934010 | 重复创建门店，请更换out\_store\_id |
| 934011 | 请求签名错误 |
| 934011 | signature is needed, please refer document for help [https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting\_started/api\_signature.html]([https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)。 原因是接口没有带签名验证信息，可以参照[微信服务端api签名指南](https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)的指引开发，同时社区内也有同行分享的[php](https://developers.weixin.qq.com/community/develop/article/doc/00028ca675c708b23f100b8e161013)和[java](https://developers.weixin.qq.com/community/develop/article/doc/000e68b8038ed8796f00f6c2f68c13)的开发实践经验。 |
| 934012 | appid和access\_token不匹配 |
| 934013 | 门店余额不足无法下单 |
| 934014 | 运力公司返回了非法金额 |
| 934015 | 余额扣减失败 |
| 934016 | 订单不存在 |
| 934017 | 订单处在不能被取消的状态 |
| 934018 | 订单已取消，请勿重复操作 |
| 934019 | 超出运力支持的配送范围 |
| 934019 | 沙箱环境下单接口返回934019 用户超出配送范围 解决方法：使用顺丰的沙箱环境环境需要固定的收件人信息（达达没有要求） 收件人信息如下：收件人姓名：顺丰同城 收件人手机：13881979410 收件地址：北京市海淀区学清嘉创大厦A座15层 |
| 934020 | 商品超重 |
| 934021 | 门店不存在 |
| 934022 | 账号类型不可以为个人账号 |
| 934023 | 小程序类型必须为普通小程序 |
| 934999 | 内部系统错误 |

---

### 门店运费充值

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_storecharge.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| wx\_store\_id | string | 否 | 微信门店编号 pay\_mode = PAY\_MODE\_STORE时必传，不传pay\_mode时必传wx\_store\_id | - |
| service\_trans\_id | string | 是 | 运力ID | [枚举值](#Enum_Body__service_trans_id) |
| amount | number | 是 | 充值金额 单位：分, 50元起充 | - |
| pay\_mode | string | 否 | 充值主体 门店：PAY\_MODE\_STORE；小程序:PAY\_MODE\_APP；服务商：PAY\_MODE\_COMPONENT，不传pay\_mode默认pay\_mode=PAY\_MODE\_STORE | - |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | 错误码。0:请求成功，其他：请求失败 |
| errmsg | string | [错误信息](#apierrcode) |
| payurl | string | 充值页面地址，请求成功时返回 |
| appid | string | 小程序appid，请求成功时返回 |
| wx\_store\_id | string | 微信门店编号，请求成功时返回 |

**Body.service_trans_id Enum**

| 枚举值 | 描述 |
| --- | --- |
| DADA | 达达 |
| SFTC | 顺丰同城 |

**物品类型列表**

| 物品类型 | 类型名称 |
| --- | --- |
| 1 | 快餐 |
| 2 | 药品 |
| 3 | 百货 |
| 6 | 生鲜 |
| 8 | 酒品 |
| 12 | 文件 |
| 13 | 蛋糕 |
| 14 | 鲜花 |
| 15 | 数码 |
| 16 | 服装 |
| 17 | 汽配 |
| 18 | 珠宝 |
| 32 | 饮料 |
| 36 | 证照 |
| 55 | 宠物用品 |
| 56 | 母婴用品 |
| 57 | 美妆用品 |
| 58 | 家居建材 |
| 99 | 其他 |

**运力列表**

| 运力名称 | 运力ID |
| --- | --- |
| 达达 | DADA |
| 顺丰同城 | SFTC |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 请求成功 |
| 48001 | api unauthorized。原因是小程序没有获得同城配送接口权限，在小程序管理后台开通【同城配送】后即可 |
| 61007 | api is unauthorized to component。此小程序没有授权当前服务商调用接口权限，服务商需获得小程序的51接口权限集 |
| 934000 | 其他逻辑错误 |
| 934001 | 请求参数有误，详细看错误提示 |
| 934002 | 订单已存在，且订单在处理中,请勿重复添加 |
| 934003 | 运力ID错误 |
| 934005 | 运力预创建订单错误 |
| 934006 | 有在途订单，暂不能退款，请等待配送完成 |
| 934007 | 不是在途订单 |
| 934008 | 门店ID和APPID不匹配 |
| 934009 | 不支持该门店所在城市 |
| 934010 | 重复创建门店，请更换out\_store\_id |
| 934011 | 请求签名错误 |
| 934011 | signature is needed, please refer document for help [https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting\_started/api\_signature.html]([https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)。 原因是接口没有带签名验证信息，可以参照[微信服务端api签名指南](https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)的指引开发，同时社区内也有同行分享的[php](https://developers.weixin.qq.com/community/develop/article/doc/00028ca675c708b23f100b8e161013)和[java](https://developers.weixin.qq.com/community/develop/article/doc/000e68b8038ed8796f00f6c2f68c13)的开发实践经验。 |
| 934012 | appid和access\_token不匹配 |
| 934013 | 门店余额不足无法下单 |
| 934014 | 运力公司返回了非法金额 |
| 934015 | 余额扣减失败 |
| 934016 | 订单不存在 |
| 934017 | 订单处在不能被取消的状态 |
| 934018 | 订单已取消，请勿重复操作 |
| 934019 | 超出运力支持的配送范围 |
| 934019 | 沙箱环境下单接口返回934019 用户超出配送范围 解决方法：使用顺丰的沙箱环境环境需要固定的收件人信息（达达没有要求） 收件人信息如下：收件人姓名：顺丰同城 收件人手机：13881979410 收件地址：北京市海淀区学清嘉创大厦A座15层 |
| 934020 | 商品超重 |
| 934021 | 门店不存在 |
| 934022 | 账号类型不可以为个人账号 |
| 934023 | 小程序类型必须为普通小程序 |
| 934999 | 内部系统错误 |

---

### 门店运费退款

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_store_refund.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| wx\_store\_id | string | 否 | 微信门店编号（pay\_mode = PAY\_MODE\_STORE时必传，不传pay\_mode时必传wx\_store\_id） | - |
| pay\_mode | string | 否 | 充值/扣费主体，不传pay\_mode默认pay\_mode=PAY\_MODE\_STORE | [枚举值](#Enum_Body__pay_mode) |
| service\_trans\_id | string | 是 | 运力ID | - |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | 错误码（0:请求成功，其他：请求失败） |
| errmsg | string | [错误描述](#apierrcode) |
| appid | string | 小程序appid |
| wx\_store\_id | string | 微信门店编号 |
| refund\_amount | number | 退款金额（单位：分） |

**Body.pay_mode Enum**

| 枚举值 | 描述 |
| --- | --- |
| PAY\_MODE\_STORE | 门店 |
| PAY\_MODE\_APP | 小程序 |
| PAY\_MODE\_COMPONENT | 服务商 |

---

### 门店运费流水查询

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_queryflow.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| wx\_store\_id | string | 是 | 微信门店编号 | - |
| flow\_type | number | 是 | 流水类型 1:充值流水， 2:消费流水，3:退款流水 | - |
| service\_trans\_id | string | 否 | 运力ID | [枚举值](#Enum_Body__service_trans_id) |
| begin\_time | number | 否 | 开始时间戳，不传默认返回最近90天的数据 | - |
| end\_time | number | 否 | 结束时间戳，不传默认返回最近90天的数据 | - |
| pay\_mode | string | 是 | 扣费主体。门店:PAY\_MODE STORE；小程序:PAY\_MODE APP；服务商:PAY\_MODE\_COMPONENT | - |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| flow\_list | [objarray](#Res__flow_list<Array>) | 流水数组。以下信息在请求成功时返回 |
| total\_pay\_amt | number | 总支付金额 |
| total\_refund\_amt | number | 总退款金额 |
| total\_deduct\_amt | number | 总违约金，消费流水返回 |

**Res.flow_list(Array) Object Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| flow\_type | number | 流水类型。1:充值流水，2:消费流水，3:退款流水 | - |
| appid | string | appid | - |
| wx\_store\_id | string | 微信门店ID | - |
| pay\_order\_id | string | 充值订单号（订单ID） | - |
| service\_trans\_id | string | 运力ID | - |
| pay\_amount | number | 支付金额 | - |
| pay\_time | number | 支付时间，时间戳类型 | - |
| pay\_status | string | 支付状态，FAIL：支付失败 SUCCESS:支付成功 | - |
| create\_time | number | 订单创建时间，时间戳类型 | - |
| consume\_deadline | number | 有效截止日期，时间戳类型 | - |
| refund\_time | number | 退款时间，时间戳类型。当flow\_type=3退款流水时返回 | - |
| refund\_amount | number | 退款金额，时间戳类型，单位：分。运单被取消后产生的退款，当flow\_type=3/2，退款流水/消费流水时返回 | - |
| openid | string | 用户openid。下单用户的openid，当flow\_type=2消费流水时返回 | - |
| delivery\_status | number | 运单状态，当flow\_type=2消费流水时返回 | [枚举值](#Enum_Res__flow_list<Array>__delivery_status) |
| refund\_status | string | 退款状态，PROCESSING:退款处理中，SUCCESS:退款成功。当flow\_type=2消费流水时返回 | - |
| deduct\_amount | number | 扣除违约金。运单被取消后产生的违约金，单位：分。当flow\_type=2消费流水时返回 | - |
| bill\_id | string | 运单ID，运力公司的订单ID。当flow\_type=2消费流水时返回 | - |
| delivery\_finished\_time | number | 运单完成配送的时间，时间戳类型。当flow\_type=2消费流水时返回 | - |

**Body.service_trans_id Enum**

| 枚举值 | 描述 |
| --- | --- |
| DADA | 达达 |
| SFTC | 顺丰同城 |

**Res.flow_list(Array).delivery_status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 10000 | 订单创建成功 |
| 20000 | 商家取消订单 |
| 20001 | 配送方取消订单 |
| 30000 | 配送员接单 |
| 40000 | 配送员到店 |
| 50000 | 配送中 |
| 60000 | 配送员撤单 |
| 70000 | 配送完成 |
| 90000 | 配送异常 |

**物品类型列表**

| 物品类型 | 类型名称 |
| --- | --- |
| 1 | 快餐 |
| 2 | 药品 |
| 3 | 百货 |
| 6 | 生鲜 |
| 8 | 酒品 |
| 12 | 文件 |
| 13 | 蛋糕 |
| 14 | 鲜花 |
| 15 | 数码 |
| 16 | 服装 |
| 17 | 汽配 |
| 18 | 珠宝 |
| 32 | 饮料 |
| 36 | 证照 |
| 55 | 宠物用品 |
| 56 | 母婴用品 |
| 57 | 美妆用品 |
| 58 | 家居建材 |
| 99 | 其他 |

**运力列表**

| 运力名称 | 运力ID |
| --- | --- |
| 达达 | DADA |
| 顺丰同城 | SFTC |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 请求成功 |
| 48001 | api unauthorized。原因是小程序没有获得同城配送接口权限，在小程序管理后台开通【同城配送】后即可 |
| 61007 | api is unauthorized to component。此小程序没有授权当前服务商调用接口权限，服务商需获得小程序的51接口权限集 |
| 934000 | 其他逻辑错误 |
| 934001 | 请求参数有误，详细看错误提示 |
| 934002 | 订单已存在，且订单在处理中,请勿重复添加 |
| 934003 | 运力ID错误 |
| 934005 | 运力预创建订单错误 |
| 934006 | 有在途订单，暂不能退款，请等待配送完成 |
| 934007 | 不是在途订单 |
| 934008 | 门店ID和APPID不匹配 |
| 934009 | 不支持该门店所在城市 |
| 934010 | 重复创建门店，请更换out\_store\_id |
| 934011 | 请求签名错误 |
| 934011 | signature is needed, please refer document for help [https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting\_started/api\_signature.html]([https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)。 原因是接口没有带签名验证信息，可以参照[微信服务端api签名指南](https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)的指引开发，同时社区内也有同行分享的[php](https://developers.weixin.qq.com/community/develop/article/doc/00028ca675c708b23f100b8e161013)和[java](https://developers.weixin.qq.com/community/develop/article/doc/000e68b8038ed8796f00f6c2f68c13)的开发实践经验。 |
| 934012 | appid和access\_token不匹配 |
| 934013 | 门店余额不足无法下单 |
| 934014 | 运力公司返回了非法金额 |
| 934015 | 余额扣减失败 |
| 934016 | 订单不存在 |
| 934017 | 订单处在不能被取消的状态 |
| 934018 | 订单已取消，请勿重复操作 |
| 934019 | 超出运力支持的配送范围 |
| 934019 | 沙箱环境下单接口返回934019 用户超出配送范围 解决方法：使用顺丰的沙箱环境环境需要固定的收件人信息（达达没有要求） 收件人信息如下：收件人姓名：顺丰同城 收件人手机：13881979410 收件地址：北京市海淀区学清嘉创大厦A座15层 |
| 934020 | 商品超重 |
| 934021 | 门店不存在 |
| 934022 | 账号类型不可以为个人账号 |
| 934023 | 小程序类型必须为普通小程序 |
| 934999 | 内部系统错误 |

---

### 门店余额查询

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_balancequery.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wx\_store\_id | string | 否 | 微信门店编号。pay\_mode = PAY\_MODE\_STORE时必传，不传pay\_mode时必传wx\_store\_id |
| service\_trans\_id | string | 否 | 运力ID。查询门店在指定运力ID充值的余额，不指定则查询全部 |
| pay\_mode | string | 否 | 充值/扣费主体。门店：PAY\_MODE\_STORE；小程序:PAY\_MODE\_APP；服务商：PAY\_MODE\_COMPONENT，不传pay\_mode默认pay\_mode=PAY\_MODE\_STORE |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | [错误码](#apierrcode) |
| errmsg | string | ok | 错误信息。 |
| wx\_store\_id | string |  | 门店ID。以下信息在请求成功时返回 |
| appid | string | - | appid |
| all\_balance | number | - | 总余额 |
| balance\_detail | [object](#Res__balance_detail) | - | 余额详情 |

**Res.balance_detail Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| balance | number | 余额 |
| service\_trans\_id | string | 运力ID |
| service\_trans\_name | string | 运力名称 |
| order\_list | [object](#Res__balance_detail__order_list) | 充值订单详情。当前生效的充值且余额没有被消费完的充值订单详情，订单充值后，没有被消费完会自动退款。 |

**Res.balance_detail.order_list Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| payorder\_id | string | 充值订单号 |
| charge\_amt | number | 充值金额 |
| unused\_amt | number | 未使用的余额 |
| begin\_time | number | 充值生效时间，时间戳类型 |
| end\_time | number | 失效时间，时间戳类型，超过该时间，余额没有被消费完会退款 |

**物品类型列表**

| 物品类型 | 类型名称 |
| --- | --- |
| 1 | 快餐 |
| 2 | 药品 |
| 3 | 百货 |
| 6 | 生鲜 |
| 8 | 酒品 |
| 12 | 文件 |
| 13 | 蛋糕 |
| 14 | 鲜花 |
| 15 | 数码 |
| 16 | 服装 |
| 17 | 汽配 |
| 18 | 珠宝 |
| 32 | 饮料 |
| 36 | 证照 |
| 55 | 宠物用品 |
| 56 | 母婴用品 |
| 57 | 美妆用品 |
| 58 | 家居建材 |
| 99 | 其他 |

**运力列表**

| 运力名称 | 运力ID |
| --- | --- |
| 达达 | DADA |
| 顺丰同城 | SFTC |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 请求成功 |
| 48001 | api unauthorized。原因是小程序没有获得同城配送接口权限，在小程序管理后台开通【同城配送】后即可 |
| 61007 | api is unauthorized to component。此小程序没有授权当前服务商调用接口权限，服务商需获得小程序的51接口权限集 |
| 934000 | 其他逻辑错误 |
| 934001 | 请求参数有误，详细看错误提示 |
| 934002 | 订单已存在，且订单在处理中,请勿重复添加 |
| 934003 | 运力ID错误 |
| 934005 | 运力预创建订单错误 |
| 934006 | 有在途订单，暂不能退款，请等待配送完成 |
| 934007 | 不是在途订单 |
| 934008 | 门店ID和APPID不匹配 |
| 934009 | 不支持该门店所在城市 |
| 934010 | 重复创建门店，请更换out\_store\_id |
| 934011 | 请求签名错误 |
| 934011 | signature is needed, please refer document for help [https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting\_started/api\_signature.html]([https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)。 原因是接口没有带签名验证信息，可以参照[微信服务端api签名指南](https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)的指引开发，同时社区内也有同行分享的[php](https://developers.weixin.qq.com/community/develop/article/doc/00028ca675c708b23f100b8e161013)和[java](https://developers.weixin.qq.com/community/develop/article/doc/000e68b8038ed8796f00f6c2f68c13)的开发实践经验。 |
| 934012 | appid和access\_token不匹配 |
| 934013 | 门店余额不足无法下单 |
| 934014 | 运力公司返回了非法金额 |
| 934015 | 余额扣减失败 |
| 934016 | 订单不存在 |
| 934017 | 订单处在不能被取消的状态 |
| 934018 | 订单已取消，请勿重复操作 |
| 934019 | 超出运力支持的配送范围 |
| 934019 | 沙箱环境下单接口返回934019 用户超出配送范围 解决方法：使用顺丰的沙箱环境环境需要固定的收件人信息（达达没有要求） 收件人信息如下：收件人姓名：顺丰同城 收件人手机：13881979410 收件地址：北京市海淀区学清嘉创大厦A座15层 |
| 934020 | 商品超重 |
| 934021 | 门店不存在 |
| 934022 | 账号类型不可以为个人账号 |
| 934023 | 小程序类型必须为普通小程序 |
| 934999 | 内部系统错误 |

---

### 查询运费

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_preaddorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wx\_store\_id | string | 是 | 微信门店编号 |
| user\_name | string | 是 | 收件人姓名 |
| user\_phone | string | 是 | 收件人手机号 |
| user\_lng | number | 是 | 收件用户位置经度 |
| user\_lat | number | 是 | 收件用户位置维度 |
| user\_address | string | 是 | 收件用户详细地市 |
| cargo\_name | string | 是 | 商品名称 |
| cargo | [object](#Body__cargo) | 是 | 商品重量 |
| use\_sandbox | number | 是 | 是否使用沙箱。1:使用沙箱环境 |

**Body.cargo Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cargo\_name | string | 是 | 商品名称 |
| cargo\_weight | number | 是 | 商品总重量，单位：克 |
| cargo\_price | number | 是 | 商品总价格，单位：分 |
| cargo\_type | number | 是 | 商品类型，详情见其他说明物品类型列表 |
| cargo\_num | number | 是 | 商品数量 |

**物品类型列表**

| 物品类型 | 类型名称 |
| --- | --- |
| 1 | 快餐 |
| 2 | 药品 |
| 3 | 百货 |
| 6 | 生鲜 |
| 8 | 酒品 |
| 12 | 文件 |
| 13 | 蛋糕 |
| 14 | 鲜花 |
| 15 | 数码 |
| 16 | 服装 |
| 17 | 汽配 |
| 18 | 珠宝 |
| 32 | 饮料 |
| 36 | 证照 |
| 55 | 宠物用品 |
| 56 | 母婴用品 |
| 57 | 美妆用品 |
| 58 | 家居建材 |
| 99 | 其他 |

**运力列表**

| 运力名称 | 运力ID |
| --- | --- |
| 达达 | DADA |
| 顺丰同城 | SFTC |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 请求成功 |
| 48001 | api unauthorized。原因是小程序没有获得同城配送接口权限，在小程序管理后台开通【同城配送】后即可 |
| 61007 | api is unauthorized to component。此小程序没有授权当前服务商调用接口权限，服务商需获得小程序的51接口权限集 |
| 934000 | 其他逻辑错误 |
| 934001 | 请求参数有误，详细看错误提示 |
| 934002 | 订单已存在，且订单在处理中,请勿重复添加 |
| 934003 | 运力ID错误 |
| 934005 | 运力预创建订单错误 |
| 934006 | 有在途订单，暂不能退款，请等待配送完成 |
| 934007 | 不是在途订单 |
| 934008 | 门店ID和APPID不匹配 |
| 934009 | 不支持该门店所在城市 |
| 934010 | 重复创建门店，请更换out\_store\_id |
| 934011 | 请求签名错误 |
| 934011 | signature is needed, please refer document for help [https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting\_started/api\_signature.html]([https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)。 原因是接口没有带签名验证信息，可以参照[微信服务端api签名指南](https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)的指引开发，同时社区内也有同行分享的[php](https://developers.weixin.qq.com/community/develop/article/doc/00028ca675c708b23f100b8e161013)和[java](https://developers.weixin.qq.com/community/develop/article/doc/000e68b8038ed8796f00f6c2f68c13)的开发实践经验。 |
| 934012 | appid和access\_token不匹配 |
| 934013 | 门店余额不足无法下单 |
| 934014 | 运力公司返回了非法金额 |
| 934015 | 余额扣减失败 |
| 934016 | 订单不存在 |
| 934017 | 订单处在不能被取消的状态 |
| 934018 | 订单已取消，请勿重复操作 |
| 934019 | 超出运力支持的配送范围 |
| 934019 | 沙箱环境下单接口返回934019 用户超出配送范围 解决方法：使用顺丰的沙箱环境环境需要固定的收件人信息（达达没有要求） 收件人信息如下：收件人姓名：顺丰同城 收件人手机：13881979410 收件地址：北京市海淀区学清嘉创大厦A座15层 |
| 934020 | 商品超重 |
| 934021 | 门店不存在 |
| 934022 | 账号类型不可以为个人账号 |
| 934023 | 小程序类型必须为普通小程序 |
| 934999 | 内部系统错误 |

---

### 创建配送单

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_addorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| wx\_store\_id | string | 是 | 微信门店编号 | - |
| store\_order\_id | string | 是 | 门店订单编号。同一个门店订单编号要保证唯一，相同的订单号会重入 | - |
| user\_openid | string | 是 | 收货用户openid | - |
| user\_lng | number | 是 | 收货用户地址经度 | - |
| user\_lat | number | 是 | 收货用户地址维度 | - |
| user\_address | string | 是 | 收货用户详细地址 | - |
| user\_name | string | 是 | 收货用户姓名 | - |
| user\_phone | string | 是 | 收货用户电话。11位手机号或11位带区号的固话:020-8080880 | - |
| order\_seq | string | 否 | 订单序号。用于配送员快速寻找到匹配的商品 | - |
| verify\_code\_type | string | 否 | 验证码类型 | [枚举值](#Enum_Body__verify_code_type) |
| order\_detail\_path | string | 是 | 跳转商家订单页面路径。物流轨迹页面跳转到商家小程序的订单页面路径参数，期望向用户展示商品订单详情 | - |
| callback\_url | string | 否 | 订单状态回调地址。回调协议详细查看下方其他说明。 | - |
| use\_sandbox | number | 否 | 1:使用沙箱环境; 使用测试沙箱环境，不需要充值运费就可以生成测试订单 | - |
| cargo | [object](#Body__cargo) | 否 | 商品信息 | - |

**Body.cargo Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cargo\_name | string | 是 | 商品名称 |
| cargo\_weight | number | 是 | 商品重量，单位：克 |
| cargo\_price | number | 是 | 商品价格，单位：分 |
| cargo\_type | number | 是 | 商品类型，详情见其他说明物品类型列表 |
| cargo\_num | number | 是 | 商品数量 |
| item\_list | [object](#Body__cargo__item_list) | 是 | 物品列表，物品的图片和名称等 |

**Body.cargo.item_list Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| item\_name | string | 是 | 物品名称 |
| item\_pic\_url | string | 是 | 物品图片 |
| count | number | 是 | 物品数量 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| wx\_store\_id | string | 微信门店编号。以下字段在请求成功时返回 |
| wx\_order\_id | string | 微信订单编号 |
| store\_order\_id | string | 门店订单编号 |
| service\_trans\_id | string | 配送运力 |
| distance | number | 配送距离，单位：米 |
| trans\_order\_id | string | 运力订单号 |
| waybill\_id | string | 运力配送单号，是否返回取决于运力 |
| fee | number | 配送费，单位：分 |
| fetch\_code | string | 取货码 |
| order\_seq | string | 取货序号 |

**Body.verify_code_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 不生成 |
| 1 | 生成取货码 |
| 2 | 生成收货码 |
| 3 | 两者都生成 |

**回调协议**

| 字段 | 字段名 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- | --- |
| appid | appid | string | 是 | 下单小程序appid |
| wx\_store\_id | 微信门店id | string | 是 |  |
| wx\_order\_id | 微信订单号 | string | 是 |  |
| store\_order\_id | 门店订单号 | string | 是 |  |
| order\_status | 订单状态 | uint32 | 是 | 详情看下方订单状态列表 |
| status\_change\_time | 订单状态变更时间 | uint32 | 是 | 秒级时间戳格式 |
| timestamp | 消息推送时间 | uint32 | 是 | 秒级时间戳格式 |
| service\_trans\_id | 运力ID | string | 是 |  |
| sign | 签名值 | string | 是 | 生成方式详见回调报文示例里的签名步骤说明 |

**订单状态列表**

| 状态类型 | 状态名称 |
| --- | --- |
| 10000 | 订单创建成功 |
| 20000 | 商家取消订单 |
| 20001 | 配送方取消订单 |
| 30000 | 配送员接单 |
| 40000 | 配送员到店 |
| 50000 | 配送中 |
| 60000 | 配送员撤单 |
| 70000 | 配送完成 |
| 90000 | 配送异常 |

**物品类型列表**

| 物品类型 | 类型名称 |
| --- | --- |
| 1 | 快餐 |
| 2 | 药品 |
| 3 | 百货 |
| 6 | 生鲜 |
| 8 | 酒品 |
| 12 | 文件 |
| 13 | 蛋糕 |
| 14 | 鲜花 |
| 15 | 数码 |
| 16 | 服装 |
| 17 | 汽配 |
| 18 | 珠宝 |
| 32 | 饮料 |
| 36 | 证照 |
| 55 | 宠物用品 |
| 56 | 母婴用品 |
| 57 | 美妆用品 |
| 58 | 家居建材 |
| 99 | 其他 |

**运力列表**

| 运力名称 | 运力ID |
| --- | --- |
| 达达 | DADA |
| 顺丰同城 | SFTC |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 请求成功 |
| 48001 | api unauthorized。原因是小程序没有获得同城配送接口权限，在小程序管理后台开通【同城配送】后即可 |
| 61007 | api is unauthorized to component。此小程序没有授权当前服务商调用接口权限，服务商需获得小程序的51接口权限集 |
| 934000 | 其他逻辑错误 |
| 934001 | 请求参数有误，详细看错误提示 |
| 934002 | 订单已存在，且订单在处理中,请勿重复添加 |
| 934003 | 运力ID错误 |
| 934005 | 运力预创建订单错误 |
| 934006 | 有在途订单，暂不能退款，请等待配送完成 |
| 934007 | 不是在途订单 |
| 934008 | 门店ID和APPID不匹配 |
| 934009 | 不支持该门店所在城市 |
| 934010 | 重复创建门店，请更换out\_store\_id |
| 934011 | 请求签名错误 |
| 934011 | signature is needed, please refer document for help [https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting\_started/api\_signature.html]([https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)。 原因是接口没有带签名验证信息，可以参照[微信服务端api签名指南](https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)的指引开发，同时社区内也有同行分享的[php](https://developers.weixin.qq.com/community/develop/article/doc/00028ca675c708b23f100b8e161013)和[java](https://developers.weixin.qq.com/community/develop/article/doc/000e68b8038ed8796f00f6c2f68c13)的开发实践经验。 |
| 934012 | appid和access\_token不匹配 |
| 934013 | 门店余额不足无法下单 |
| 934014 | 运力公司返回了非法金额 |
| 934015 | 余额扣减失败 |
| 934016 | 订单不存在 |
| 934017 | 订单处在不能被取消的状态 |
| 934018 | 订单已取消，请勿重复操作 |
| 934019 | 超出运力支持的配送范围 |
| 934019 | 沙箱环境下单接口返回934019 用户超出配送范围 解决方法：使用顺丰的沙箱环境环境需要固定的收件人信息（达达没有要求） 收件人信息如下：收件人姓名：顺丰同城 收件人手机：13881979410 收件地址：北京市海淀区学清嘉创大厦A座15层 |
| 934020 | 商品超重 |
| 934021 | 门店不存在 |
| 934022 | 账号类型不可以为个人账号 |
| 934023 | 小程序类型必须为普通小程序 |
| 934999 | 内部系统错误 |

---

### 查询配送单

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_queryorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wx\_store\_id | string | 否 | 微信门店编号.wx\_store\_id和store\_order\_id需要成对出现 |
| store\_order\_id | string | 否 | wx\_store\_id和store\_order\_id需要成对出现 |
| wx\_order\_id | string | 否 | 可以单独使用wx\_order\_id查询 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| wx\_order\_id | string | 微信订单号 |
| store\_order\_id | string | 门店订单号 |
| wx\_store\_id | string | 微信门店编号 |
| order\_status | number | 订单状态 |
| appid | string | appid |
| user\_openid | string | 收件用户openid |
| service\_trans\_id | string | 运力ID |
| delivery\_no | string | 运力订单号 |
| distance | double | 配送距离，单位：米 |
| actualfee | number | 实际支付费用，单位：分 |
| deductfee | number | 违约金，单位：分 |
| create\_time | number | 发单时间 |
| accept\_time | number | 配送员接单时间，时间戳 |
| finish\_time | number | 配送员送达时间，时间戳 |
| fetch\_time | number | 配送员取货时间，时间戳 |
| cancel\_time | number | 取消时间，时间戳 |
| expected\_finish\_time | number | 预期送达时间 |
| fetch\_code | string | 取货码，商家验证 |
| recv\_code | string | 收货码，收货人验证 |
| order\_seq | string | 订单序号，用于配送员识别 |
| transporter\_info | [object](#Res__transporter_info) | 配送员信息 |
| store\_info | [object](#Res__store_info) | 门店信息 |
| receiver\_info | [object](#Res__receiver_info) | 收货人信息 |
| cargo\_info | [object](#Res__cargo_info) | 商品信息 |

**Res.transporter_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| transporter\_name | string | 配送员姓名 |
| transporter\_phone | string | 配送员电话 |

**Res.store_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| store\_name | string | 门店名称 |
| wx\_store\_id | string | 门店编号 |
| address | string | 门店详细地址 |
| lng | double | 门店经度 |
| lat | double | 门店维度 |
| phone\_num | string | 门店电话 |

**Res.receiver_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| receiver\_name | string | 收件人姓名 |
| address | string | 收件人详细地址 |
| phone\_num | string | 收件人电话 |
| lng | double | 收件地址经度 |
| lat | double | 收件地址维度 |

**Res.cargo_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| cargo\_name | string | 商品名称 |
| cargo\_weight | number | 商品总重量，单位：克 |
| cargo\_price | number | 商品总价格，单位：分 |
| cargo\_type | number | 商品类型，详情见其他说明物品类型列表 |
| cargo\_num | number | 商品数量 |
| item\_list | [object](#Res__cargo_info__item_list) | 商品详情 |

**Res.cargo_info.item_list Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| item\_name | string | 物品名称 |
| item\_pic\_url | string | 物品图片 |
| num | number | 物品数量 |

**物品类型列表**

| 物品类型 | 类型名称 |
| --- | --- |
| 1 | 快餐 |
| 2 | 药品 |
| 3 | 百货 |
| 6 | 生鲜 |
| 8 | 酒品 |
| 12 | 文件 |
| 13 | 蛋糕 |
| 14 | 鲜花 |
| 15 | 数码 |
| 16 | 服装 |
| 17 | 汽配 |
| 18 | 珠宝 |
| 32 | 饮料 |
| 36 | 证照 |
| 55 | 宠物用品 |
| 56 | 母婴用品 |
| 57 | 美妆用品 |
| 58 | 家居建材 |
| 99 | 其他 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 请求成功 |
| 48001 | api unauthorized。原因是小程序没有获得同城配送接口权限，在小程序管理后台开通【同城配送】后即可 |
| 61007 | api is unauthorized to component。此小程序没有授权当前服务商调用接口权限，服务商需获得小程序的51接口权限集 |
| 934000 | 其他逻辑错误 |
| 934001 | 请求参数有误，详细看错误提示 |
| 934002 | 订单已存在，且订单在处理中,请勿重复添加 |
| 934003 | 运力ID错误 |
| 934005 | 运力预创建订单错误 |
| 934006 | 有在途订单，暂不能退款，请等待配送完成 |
| 934007 | 不是在途订单 |
| 934008 | 门店ID和APPID不匹配 |
| 934009 | 不支持该门店所在城市 |
| 934010 | 重复创建门店，请更换out\_store\_id |
| 934011 | 请求签名错误 |
| 934011 | signature is needed, please refer document for help [https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting\_started/api\_signature.html]([https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)。 原因是接口没有带签名验证信息，可以参照[微信服务端api签名指南](https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)的指引开发，同时社区内也有同行分享的[php](https://developers.weixin.qq.com/community/develop/article/doc/00028ca675c708b23f100b8e161013)和[java](https://developers.weixin.qq.com/community/develop/article/doc/000e68b8038ed8796f00f6c2f68c13)的开发实践经验。 |
| 934012 | appid和access\_token不匹配 |
| 934013 | 门店余额不足无法下单 |
| 934014 | 运力公司返回了非法金额 |
| 934015 | 余额扣减失败 |
| 934016 | 订单不存在 |
| 934017 | 订单处在不能被取消的状态 |
| 934018 | 订单已取消，请勿重复操作 |
| 934019 | 超出运力支持的配送范围 |
| 934019 | 沙箱环境下单接口返回934019 用户超出配送范围 解决方法：使用顺丰的沙箱环境环境需要固定的收件人信息（达达没有要求） 收件人信息如下：收件人姓名：顺丰同城 收件人手机：13881979410 收件地址：北京市海淀区学清嘉创大厦A座15层 |
| 934020 | 商品超重 |
| 934021 | 门店不存在 |
| 934022 | 账号类型不可以为个人账号 |
| 934023 | 小程序类型必须为普通小程序 |
| 934999 | 内部系统错误 |

---

### 取消配送单

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_cancelorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| wx\_store\_id | string | 否 | 微信门店编号.wx\_store\_id和store\_order\_id需要成对出现 | - |
| store\_order\_id | string | 否 | wx\_store\_id和store\_order\_id需要成对出现 | - |
| wx\_order\_id | string | 否 | 可以单独使用wx\_order\_id取消订单 | - |
| cancel\_reason\_id | number | 是 | 取消原因 | [枚举值](#Enum_Body__cancel_reason_id) |
| cancel\_reason | string | 否 | 取消原因描述 | - |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| wx\_store\_id | string | 微信门店编号。以下字段在请求成功时返回 |
| wx\_order\_id | string | 微信订单号 |
| store\_order\_id | string | 门店订单号 |
| order\_status | number | 订单状态，详情看其他说明订单状态列表 |
| appid | string | 小程序appid |
| deductfee | number | 违约金。取消配送途中的订单，需要扣减违约金 |

**Body.cancel_reason_id Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 不需要了 |
| 2 | 信息填错 |
| 3 | 无人接单 |
| 99 | 其他 |

**订单状态列表**

| 状态类型 | 状态名称 |
| --- | --- |
| 10000 | 订单创建成功 |
| 20000 | 商家取消订单 |
| 20001 | 配送方取消订单 |
| 30000 | 配送员接单 |
| 40000 | 配送员到店 |
| 50000 | 配送中 |
| 60000 | 配送员撤单 |
| 70000 | 配送完成 |
| 90000 | 配送异常 |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 请求成功 |
| 48001 | api unauthorized。原因是小程序没有获得同城配送接口权限，在小程序管理后台开通【同城配送】后即可 |
| 61007 | api is unauthorized to component。此小程序没有授权当前服务商调用接口权限，服务商需获得小程序的51接口权限集 |
| 934000 | 其他逻辑错误 |
| 934001 | 请求参数有误，详细看错误提示 |
| 934002 | 订单已存在，且订单在处理中,请勿重复添加 |
| 934003 | 运力ID错误 |
| 934005 | 运力预创建订单错误 |
| 934006 | 有在途订单，暂不能退款，请等待配送完成 |
| 934007 | 不是在途订单 |
| 934008 | 门店ID和APPID不匹配 |
| 934009 | 不支持该门店所在城市 |
| 934010 | 重复创建门店，请更换out\_store\_id |
| 934011 | 请求签名错误 |
| 934011 | signature is needed, please refer document for help [https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting\_started/api\_signature.html]([https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)。 原因是接口没有带签名验证信息，可以参照[微信服务端api签名指南](https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)的指引开发，同时社区内也有同行分享的[php](https://developers.weixin.qq.com/community/develop/article/doc/00028ca675c708b23f100b8e161013)和[java](https://developers.weixin.qq.com/community/develop/article/doc/000e68b8038ed8796f00f6c2f68c13)的开发实践经验。 |
| 934012 | appid和access\_token不匹配 |
| 934013 | 门店余额不足无法下单 |
| 934014 | 运力公司返回了非法金额 |
| 934015 | 余额扣减失败 |
| 934016 | 订单不存在 |
| 934017 | 订单处在不能被取消的状态 |
| 934018 | 订单已取消，请勿重复操作 |
| 934019 | 超出运力支持的配送范围 |
| 934019 | 沙箱环境下单接口返回934019 用户超出配送范围 解决方法：使用顺丰的沙箱环境环境需要固定的收件人信息（达达没有要求） 收件人信息如下：收件人姓名：顺丰同城 收件人手机：13881979410 收件地址：北京市海淀区学清嘉创大厦A座15层 |
| 934020 | 商品超重 |
| 934021 | 门店不存在 |
| 934022 | 账号类型不可以为个人账号 |
| 934023 | 小程序类型必须为普通小程序 |
| 934999 | 内部系统错误 |

---

### 设置扣费主体

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_setpaymode.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appid | string | 是 | 小程序appid。必须要和access\_token匹配 |
| pay\_mode | string | 是 | 扣费主体。门店：PAY\_MODE\_STORE；小程序:PAY\_MODE\_APP；服务商：PAY\_MODE\_COMPONENT |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 请求成功 |
| 48001 | api unauthorized。原因是小程序没有获得同城配送接口权限，在小程序管理后台开通【同城配送】后即可 |
| 61007 | api is unauthorized to component。此小程序没有授权当前服务商调用接口权限，服务商需获得小程序的51接口权限集 |
| 934000 | 其他逻辑错误 |
| 934001 | 请求参数有误，详细看错误提示 |
| 934002 | 订单已存在，且订单在处理中,请勿重复添加 |
| 934003 | 运力ID错误 |
| 934005 | 运力预创建订单错误 |
| 934006 | 有在途订单，暂不能退款，请等待配送完成 |
| 934007 | 不是在途订单 |
| 934008 | 门店ID和APPID不匹配 |
| 934009 | 不支持该门店所在城市 |
| 934010 | 重复创建门店，请更换out\_store\_id |
| 934011 | 请求签名错误 |
| 934011 | signature is needed, please refer document for help [https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting\_started/api\_signature.html]([https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)。 原因是接口没有带签名验证信息，可以参照[微信服务端api签名指南](https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)的指引开发，同时社区内也有同行分享的[php](https://developers.weixin.qq.com/community/develop/article/doc/00028ca675c708b23f100b8e161013)和[java](https://developers.weixin.qq.com/community/develop/article/doc/000e68b8038ed8796f00f6c2f68c13)的开发实践经验。 |
| 934012 | appid和access\_token不匹配 |
| 934013 | 门店余额不足无法下单 |
| 934014 | 运力公司返回了非法金额 |
| 934015 | 余额扣减失败 |
| 934016 | 订单不存在 |
| 934017 | 订单处在不能被取消的状态 |
| 934018 | 订单已取消，请勿重复操作 |
| 934019 | 超出运力支持的配送范围 |
| 934019 | 沙箱环境下单接口返回934019 用户超出配送范围 解决方法：使用顺丰的沙箱环境环境需要固定的收件人信息（达达没有要求） 收件人信息如下：收件人姓名：顺丰同城 收件人手机：13881979410 收件地址：北京市海淀区学清嘉创大厦A座15层 |
| 934020 | 商品超重 |
| 934021 | 门店不存在 |
| 934022 | 账号类型不可以为个人账号 |
| 934023 | 小程序类型必须为普通小程序 |
| 934999 | 内部系统错误 |

---

### 查询扣费主体

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_getpaymode.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appid | string | 是 | 小程序appid。必须要和access\_token匹配 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| pay\_mode | string | 扣费主体。门店：PAY\_MODE\_STORE；小程序:PAY\_MODE\_APP；服务商：PAY\_MODE\_COMPONENT |
| pay\_appid | string | 扣费appid。扣费主体为小程序时返回 |
| pay\_component\_appid | string | 扣费component\_appid。扣费主体为服务商时返回 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 请求成功 |
| 48001 | api unauthorized。原因是小程序没有获得同城配送接口权限，在小程序管理后台开通【同城配送】后即可 |
| 61007 | api is unauthorized to component。此小程序没有授权当前服务商调用接口权限，服务商需获得小程序的51接口权限集 |
| 934000 | 其他逻辑错误 |
| 934001 | 请求参数有误，详细看错误提示 |
| 934002 | 订单已存在，且订单在处理中,请勿重复添加 |
| 934003 | 运力ID错误 |
| 934005 | 运力预创建订单错误 |
| 934006 | 有在途订单，暂不能退款，请等待配送完成 |
| 934007 | 不是在途订单 |
| 934008 | 门店ID和APPID不匹配 |
| 934009 | 不支持该门店所在城市 |
| 934010 | 重复创建门店，请更换out\_store\_id |
| 934011 | 请求签名错误 |
| 934011 | signature is needed, please refer document for help [https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting\_started/api\_signature.html]([https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)。 原因是接口没有带签名验证信息，可以参照[微信服务端api签名指南](https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)的指引开发，同时社区内也有同行分享的[php](https://developers.weixin.qq.com/community/develop/article/doc/00028ca675c708b23f100b8e161013)和[java](https://developers.weixin.qq.com/community/develop/article/doc/000e68b8038ed8796f00f6c2f68c13)的开发实践经验。 |
| 934012 | appid和access\_token不匹配 |
| 934013 | 门店余额不足无法下单 |
| 934014 | 运力公司返回了非法金额 |
| 934015 | 余额扣减失败 |
| 934016 | 订单不存在 |
| 934017 | 订单处在不能被取消的状态 |
| 934018 | 订单已取消，请勿重复操作 |
| 934019 | 超出运力支持的配送范围 |
| 934019 | 沙箱环境下单接口返回934019 用户超出配送范围 解决方法：使用顺丰的沙箱环境环境需要固定的收件人信息（达达没有要求） 收件人信息如下：收件人姓名：顺丰同城 收件人手机：13881979410 收件地址：北京市海淀区学清嘉创大厦A座15层 |
| 934020 | 商品超重 |
| 934021 | 门店不存在 |
| 934022 | 账号类型不可以为个人账号 |
| 934023 | 小程序类型必须为普通小程序 |
| 934999 | 内部系统错误 |

---

### 查询支持同城配送的城市

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_getcity.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| service\_trans\_id | string | 否 | 返回指定运力的支持城市信息。SFTC:顺丰同城，DADA:达达，不传则返回所有结果 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| support\_list | [object](#Res__support_list) | 运力支持的城市信息 |

**Res.support_list Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| service\_trans\_id | string | 运力ID |
| city\_list | [objarray](#Res__support_list__city_list<Array>) | 城市列表 |

**Res.support_list.city_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| city\_code | number | 城市行政区域编码 |
| city\_name | string | 城市名称 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 请求成功 |
| 48001 | api unauthorized。原因是小程序没有获得同城配送接口权限，在小程序管理后台开通【同城配送】后即可 |
| 61007 | api is unauthorized to component。此小程序没有授权当前服务商调用接口权限，服务商需获得小程序的51接口权限集 |
| 934000 | 其他逻辑错误 |
| 934001 | 请求参数有误，详细看错误提示 |
| 934002 | 订单已存在，且订单在处理中,请勿重复添加 |
| 934003 | 运力ID错误 |
| 934005 | 运力预创建订单错误 |
| 934006 | 有在途订单，暂不能退款，请等待配送完成 |
| 934007 | 不是在途订单 |
| 934008 | 门店ID和APPID不匹配 |
| 934009 | 不支持该门店所在城市 |
| 934010 | 重复创建门店，请更换out\_store\_id |
| 934011 | 请求签名错误 |
| 934011 | signature is needed, please refer document for help [https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting\_started/api\_signature.html]([https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)。 原因是接口没有带签名验证信息，可以参照[微信服务端api签名指南](https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)的指引开发，同时社区内也有同行分享的[php](https://developers.weixin.qq.com/community/develop/article/doc/00028ca675c708b23f100b8e161013)和[java](https://developers.weixin.qq.com/community/develop/article/doc/000e68b8038ed8796f00f6c2f68c13)的开发实践经验。 |
| 934012 | appid和access\_token不匹配 |
| 934013 | 门店余额不足无法下单 |
| 934014 | 运力公司返回了非法金额 |
| 934015 | 余额扣减失败 |
| 934016 | 订单不存在 |
| 934017 | 订单处在不能被取消的状态 |
| 934018 | 订单已取消，请勿重复操作 |
| 934019 | 超出运力支持的配送范围 |
| 934019 | 沙箱环境下单接口返回934019 用户超出配送范围 解决方法：使用顺丰的沙箱环境环境需要固定的收件人信息（达达没有要求） 收件人信息如下：收件人姓名：顺丰同城 收件人手机：13881979410 收件地址：北京市海淀区学清嘉创大厦A座15层 |
| 934020 | 商品超重 |
| 934021 | 门店不存在 |
| 934022 | 账号类型不可以为个人账号 |
| 934023 | 小程序类型必须为普通小程序 |
| 934999 | 内部系统错误 |

---

### 模拟回调接口

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_mocknotify.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wx\_order\_id | string | 否 | 微信订单号，可以单独使用wx\_order\_id |
| wx\_store\_id | string | 否 | 门店ID wx\_store\_id和store\_order\_id需要成对出现 |
| store\_order\_id | string | 否 | 门店订单号 wx\_store\_id和store\_order\_id需要成对出现 |
| order\_status | number | 是 | 订单状态，详见其他说明订单状态列表 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**回调协议**

| 字段 | 字段名 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- | --- |
| appid | appid | string | 是 | 下单小程序appid |
| wx\_store\_id | 微信门店id | string | 是 |  |
| wx\_order\_id | 微信订单号 | string | 是 |  |
| store\_order\_id | 门店订单号 | string | 是 |  |
| order\_status | 订单状态 | uint32 | 是 | 详情看下方订单状态列表 |
| status\_change\_time | 订单状态变更时间 | uint32 | 是 | 秒级时间戳格式 |
| timestamp | 消息推送时间 | uint32 | 是 | 秒级时间戳格式 |
| service\_trans\_id | 运力ID | string | 是 |  |
| sign | 签名值 | string | 是 | 生成方式详见回调报文示例里的签名步骤说明 |

**订单状态列表**

| 状态类型 | 状态名称 |
| --- | --- |
| 10000 | 订单创建成功 |
| 20000 | 商家取消订单 |
| 20001 | 配送方取消订单 |
| 30000 | 配送员接单 |
| 40000 | 配送员到店 |
| 50000 | 配送中 |
| 60000 | 配送员撤单 |
| 70000 | 配送完成 |
| 90000 | 配送异常 |

**物品类型列表**

| 物品类型 | 类型名称 |
| --- | --- |
| 1 | 快餐 |
| 2 | 药品 |
| 3 | 百货 |
| 6 | 生鲜 |
| 8 | 酒品 |
| 12 | 文件 |
| 13 | 蛋糕 |
| 14 | 鲜花 |
| 15 | 数码 |
| 16 | 服装 |
| 17 | 汽配 |
| 18 | 珠宝 |
| 32 | 饮料 |
| 36 | 证照 |
| 55 | 宠物用品 |
| 56 | 母婴用品 |
| 57 | 美妆用品 |
| 58 | 家居建材 |
| 99 | 其他 |

**运力列表**

| 运力名称 | 运力ID |
| --- | --- |
| 达达 | DADA |
| 顺丰同城 | SFTC |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 请求成功 |
| 48001 | api unauthorized。原因是小程序没有获得同城配送接口权限，在小程序管理后台开通【同城配送】后即可 |
| 61007 | api is unauthorized to component。此小程序没有授权当前服务商调用接口权限，服务商需获得小程序的51接口权限集 |
| 934000 | 其他逻辑错误 |
| 934001 | 请求参数有误，详细看错误提示 |
| 934002 | 订单已存在，且订单在处理中,请勿重复添加 |
| 934003 | 运力ID错误 |
| 934005 | 运力预创建订单错误 |
| 934006 | 有在途订单，暂不能退款，请等待配送完成 |
| 934007 | 不是在途订单 |
| 934008 | 门店ID和APPID不匹配 |
| 934009 | 不支持该门店所在城市 |
| 934010 | 重复创建门店，请更换out\_store\_id |
| 934011 | 请求签名错误 |
| 934011 | signature is needed, please refer document for help [https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting\_started/api\_signature.html]([https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)。 原因是接口没有带签名验证信息，可以参照[微信服务端api签名指南](https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/getting_started/api_signature.html)的指引开发，同时社区内也有同行分享的[php](https://developers.weixin.qq.com/community/develop/article/doc/00028ca675c708b23f100b8e161013)和[java](https://developers.weixin.qq.com/community/develop/article/doc/000e68b8038ed8796f00f6c2f68c13)的开发实践经验。 |
| 934012 | appid和access\_token不匹配 |
| 934013 | 门店余额不足无法下单 |
| 934014 | 运力公司返回了非法金额 |
| 934015 | 余额扣减失败 |
| 934016 | 订单不存在 |
| 934017 | 订单处在不能被取消的状态 |
| 934018 | 订单已取消，请勿重复操作 |
| 934019 | 超出运力支持的配送范围 |
| 934019 | 沙箱环境下单接口返回934019 用户超出配送范围 解决方法：使用顺丰的沙箱环境环境需要固定的收件人信息（达达没有要求） 收件人信息如下：收件人姓名：顺丰同城 收件人手机：13881979410 收件地址：北京市海淀区学清嘉创大厦A座15层 |
| 934020 | 商品超重 |
| 934021 | 门店不存在 |
| 934022 | 账号类型不可以为个人账号 |
| 934023 | 小程序类型必须为普通小程序 |
| 934999 | 内部系统错误 |

---

### 用户手机状态查询

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/msgpush/api_deliveryuserquery.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phone | string | 是 | 手机号 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| exist | number | 用户是否绑定 0-未绑定 1-已绑定 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 40014/40001 | 无效accesstoken |
| 40097 | 参数错误 |
| 41001 | accesstoken不存在 |
| 42001 | accesstoken过期 |
| 150004 | 运力配置不存在 |
| 932001 | 反查运单系统错误 |
| 932002 | 反查运单逻辑错误 |
| 932003 | 反查运单获取到的运单数据异常 |

---

### 推送已绑定物流轨迹信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/msgpush/api_deliverypathnotify.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sender | [object](#Body__sender) | 是 | 寄件人 |
| receiver | [object](#Body__receiver) | 是 | 收件人 |
| waybill\_id | string | 是 | 运单号 |
| path | [object](#Body__path) | 是 | 当前需要推送消息的轨迹 |
| create\_time | number | 是 | 运单创建时间，unix时间戳（秒） |

**Body.sender Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 姓名（收件人必传，寄件人非必传） |
| phone | string | 否 | 电话（收件人必传，寄件人非必传） |
| province | string | 是 | 省 |
| city | string | 是 | 市 |
| area | string | 是 | 区/县 |
| street | string | 否 | 街道 |
| address | string | 否 | 地址 |
| id | string | 否 | 地址id |

**Body.receiver Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 姓名（收件人必传，寄件人非必传） |
| phone | string | 否 | 电话（收件人必传，寄件人非必传） |
| province | string | 是 | 省 |
| city | string | 是 | 市 |
| area | string | 是 | 区/县 |
| street | string | 否 | 街道 |
| address | string | 否 | 地址 |
| id | string | 否 | 地址id |

**Body.path Object Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| action\_time | number | 是 | 轨迹变化Unix时间戳 | - |
| action\_type | number | 是 | 轨迹变化类型，与普通单保持一致，参见下方其他说明action\_type定义 | [枚举值](#Enum_Body__path__action_type) |
| action\_msg | string | 是 | 轨迹变化具体信息说明，展示在快递轨迹详情页中 | - |
| pickup\_courier\_name | string | 否 | 取件员姓名,当分配取件员成功时返回 | - |
| pickup\_courier\_phone | string | 否 | 取件员电话,当分配取件员成功时返回 | - |
| delivery\_courier\_name | string | 否 | 派件员姓名,当分配派件员成功时返回 | - |
| delivery\_courier\_phone | string | 否 | 派件员电话,当分配派件员成功时返回 | - |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| exist | number | 用户是否绑定 0-未绑定 1-已绑定 |

**Body.path.action_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| 90001 | 揽件前阶段-网点接单 |
| 90002 | 揽件前阶段-分配业务员 |
| 90003 | 揽件前阶段-重新分配业务员 |
| 90010 | 揽件前阶段-待支付 |
| 90011 | 揽件前阶段-已支付 |
| 100001 | 揽件阶段-揽件成功 |
| 100002 | 揽件阶段-揽件失败 |
| 200001 | 运输阶段-更新运输轨迹 |
| 300002 | 派送阶段-派送中 |
| 300003 | 派送阶段-签收成功 |
| 300004 | 派送阶段-签收失败 |
| 300005 | 派送阶段-第三方代收入库 |
| 300006 | 派送阶段-第三方代收快递员取出 |
| 300007 | 派送阶段-代签收 |
| 400001 | 异常阶段-订单取消 |
| 400002 | 异常阶段-订单滞留 |
| 400003 | 异常阶段-订单退回 |
| 400004 | 异常阶段-订单拒收 |
| 400005 | 异常阶段-问题件 |
| 500001 | 兜底状态-其他未分类状态纳入本action\_type |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 40014/40001 | 无效accesstoken |
| 40097 | 参数错误 |
| 41001 | accesstoken不存在 |
| 42001 | accesstoken过期 |
| 150004 | 运力配置不存在 |
| 932001 | 反查运单系统错误 |
| 932002 | 反查运单逻辑错误 |
| 932003 | 反查运单获取到的运单数据异常 |

---

<!-- pages: 40 -->
