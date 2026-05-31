# 小程序服务端 API 结构化参考 — API/charge

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 查询购买资源包的用量情况

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/charge/api_getusagedetail.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| spuId | string | 是 | 商品SPU ID |
| offset | number | 是 | 分页偏移量，从0开始 |
| limit | number | 是 | 每页个数，最大20 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| effectiveUse | string | 累计用量（64位数字），用于资源包类商品 |
| effectiveAll | string | 资源总量（64位数字），用于资源包类商品（已废弃） |
| all | string | 资源可用总量（64位数字），用于资源包类商品。详情见其他说明 |
| startServiceTime | number | 订阅开始时间戳（单位：秒），用于订阅类商品 |
| endServiceTime | number | 订阅结束时间戳（单位：秒），用于订阅类商品 |
| total | number | 用量详情列表总数 |
| detailList | [objarray](#Res__detailList<Array>) | 用量详情列表 |

**Res.detailList(Array) Object Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| pkgId | string | 资源包ID | - |
| status | number | 资源包状态 | [枚举值](#Enum_Res__detailList<Array>__status) |
| startTime | number | 额度有效期开始时间戳（单位：秒） | - |
| endTime | number | 额度有效期至结束时间戳（单位：秒） | - |
| all | string | 额度容量（64位数字 | - |
| used | string | 使用额度（64位数字） | - |
| spuId | string | 额度来源的商品SPU ID（64位数字） | - |
| skuId | string | 额度来源的商品SKU ID（64位数字） | - |
| source | number | 额度来源 | [枚举值](#Enum_Res__detailList<Array>__source) |

**Res.detailList(Array).status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 生效中 |
| 2 | 未生效 |
| 3 | 已失效 |

**Res.detailList(Array).source Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 体验额度 |
| 2 | 付费购买 |
| 3 | 服务商分配 |
| 4 | 其他 |
| 5 | 其他 |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 10120002 | 参数错误 |
| 10120003 | limit参数过大，调小limit的数值 |

---

### 获取小程序某个付费能力的最近用量数据

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/charge/api_getrecentaverageusage.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| spuId | string | 是 | 商品SPU ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| averageData | number | 最近月平均用量，经模糊化处理，非精确值。 注意：当averageData返回值为50时，语义为小程序最近平均用量小于等于50次/月，并不是特指精确等于每月50次。 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 10120002 | 参数错误 |
| 10120700 | spuId非法 |
| 10122000 | 该商品没有最近使用数据 |

---

<!-- pages: 2 -->
