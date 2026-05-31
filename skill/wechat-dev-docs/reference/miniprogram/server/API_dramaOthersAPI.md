# 小程序服务端 API 结构化参考 — API/dramaOthersAPI

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 播放原始视频-推荐位控制接口

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/dramaOthersAPI/api_setplayerdramarecmdswitch.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| entry\_type | number | 是 | 2002 | 此处填2002（当需要控制推荐位时，可选值为：1-剧结束 2-选集最右侧推荐 3-剧集profile页相关推荐） |
| switch\_status | boolean | 是 | true | true-打开 false-关闭，没有打开过的都默认为关闭（当需要控制推荐位时：true-打开 false-关闭，1-剧结束&3-剧集profile页默认打开） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误，请重试 |
| 0 | 成功 |
| 1 | 不存在 |
| 2 | 参数错误 |
| 21000 | 该剧未授权播放，请通过后台api进行授权 |
| 21001 | 用户加密的sessionkey不存在 |
| 21002 | 商家的加密包未进行base64编码 |
| 21003 | 解密商家加密包失败，请确认是否按接入文档中给出的加密方案加密或sessionkey要使用当前用户最新的 |
| 21004 | 商家加密前的明文不是合法的json格式或者字段类型不对，请按接入文档排查 |
| 21005 | 商家加密中的必填参数值(openid、src\_appid及drama\_id)为空 |
| 21006 | 播放器的入参与商家加密包中的参数值不匹配 |
| 21007 | 加密包中的openid无效 |
| 21008 | 21008 开发者未开启预拉取 |
| 21009 | 21009 商家流量不足 |

---

### 刷剧剧目设置

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/dramaOthersAPI/api_developersetflushdrama.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| list | [objarray](#Body__list<Array>) | 是 | list |

**Body.list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src\_appid | string | 是 | 提审方小程序的appid |
| drama\_id | string | 是 | 提审的剧目id |
| drama\_name | string | 是 | 短剧名称 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number |  | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误，请重试 |
| 0 | 成功 |
| 1 | 不存在 |
| 2 | 参数错误 |
| 21000 | 该剧未授权播放，请通过后台api进行授权 |
| 21001 | 用户加密的sessionkey不存在 |
| 21002 | 商家的加密包未进行base64编码 |
| 21003 | 解密商家加密包失败，请确认是否按接入文档中给出的加密方案加密或sessionkey要使用当前用户最新的 |
| 21004 | 商家加密前的明文不是合法的json格式或者字段类型不对，请按接入文档排查 |
| 21005 | 商家加密中的必填参数值(openid、src\_appid及drama\_id)为空 |
| 21006 | 播放器的入参与商家加密包中的参数值不匹配 |
| 21007 | 加密包中的openid无效 |
| 21008 | 21008 开发者未开启预拉取 |
| 21009 | 21009 商家流量不足 |

---

### 推荐剧目

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/dramaOthersAPI/api_developersetrecmddrama.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| entry\_type | number | 是 | 1-剧结束 2-选集最右侧推荐 3-剧集profile页相关推荐 |
| src\_appid | string | 否 | 提审方小程序的appid |
| drama\_id | string | 否 | 提审的剧目id |
| list | [objarray](#Body__list<Array>) | 否 | list |

**Body.list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src\_appid | string | 是 | 提审方小程序的appid |
| drama\_id | string | 是 | 提审的剧目id |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number |  | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误，请重试 |
| 0 | 成功 |
| 1 | 不存在 |
| 2 | 参数错误 |
| 21000 | 该剧未授权播放，请通过后台api进行授权 |
| 21001 | 用户加密的sessionkey不存在 |
| 21002 | 商家的加密包未进行base64编码 |
| 21003 | 解密商家加密包失败，请确认是否按接入文档中给出的加密方案加密或sessionkey要使用当前用户最新的 |
| 21004 | 商家加密前的明文不是合法的json格式或者字段类型不对，请按接入文档排查 |
| 21005 | 商家加密中的必填参数值(openid、src\_appid及drama\_id)为空 |
| 21006 | 播放器的入参与商家加密包中的参数值不匹配 |
| 21007 | 加密包中的openid无效 |
| 21008 | 21008 开发者未开启预拉取 |
| 21009 | 21009 商家流量不足 |

---

### 短剧上架

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/dramaOthersAPI/api_developerpublishdrama.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| list | [objarray](#Body__list<Array>) | 是 | list |

**Body.list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src\_appid | string | 是 | 提审方小程序的appid |
| drama\_id | string | 是 | 提审的剧目id |
| drama\_name | string | 是 | 短剧名称 |
| publish\_time | number | 是 | 上架时间戳（秒级别） |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number |  | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误，请重试 |
| 0 | 成功 |
| 1 | 不存在 |
| 2 | 参数错误 |
| 21000 | 该剧未授权播放，请通过后台api进行授权 |
| 21001 | 用户加密的sessionkey不存在 |
| 21002 | 商家的加密包未进行base64编码 |
| 21003 | 解密商家加密包失败，请确认是否按接入文档中给出的加密方案加密或sessionkey要使用当前用户最新的 |
| 21004 | 商家加密前的明文不是合法的json格式或者字段类型不对，请按接入文档排查 |
| 21005 | 商家加密中的必填参数值(openid、src\_appid及drama\_id)为空 |
| 21006 | 播放器的入参与商家加密包中的参数值不匹配 |
| 21007 | 加密包中的openid无效 |
| 21008 | 21008 开发者未开启预拉取 |
| 21009 | 21009 商家流量不足 |

---

### 获取已上架短剧

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/dramaOthersAPI/api_developergetpublisheddrama.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| list | [objarray](#Res__list<Array>) | list |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| src\_appid | string | 提审方小程序的appid |
| drama\_id | string | 提审的剧目id |
| publish\_time | number | 上架时间戳（秒级别） |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误，请重试 |
| 0 | 成功 |
| 1 | 不存在 |
| 2 | 参数错误 |
| 21000 | 该剧未授权播放，请通过后台api进行授权 |
| 21001 | 用户加密的sessionkey不存在 |
| 21002 | 商家的加密包未进行base64编码 |
| 21003 | 解密商家加密包失败，请确认是否按接入文档中给出的加密方案加密或sessionkey要使用当前用户最新的 |
| 21004 | 商家加密前的明文不是合法的json格式或者字段类型不对，请按接入文档排查 |
| 21005 | 商家加密中的必填参数值(openid、src\_appid及drama\_id)为空 |
| 21006 | 播放器的入参与商家加密包中的参数值不匹配 |
| 21007 | 加密包中的openid无效 |
| 21008 | 21008 开发者未开启预拉取 |
| 21009 | 21009 商家流量不足 |

---

### 设置短剧变现类型

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/dramaOthersAPI/api_developersetiaadrama.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| list | [objarray](#Body__list<Array>) | 是 | list |

**Body.list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src\_appid | string | 是 | 提审方小程序的appid |
| drama\_id | string | 是 | 提审的剧目id |
| iaa\_type | number | 是 | 短剧变现类型。 1-纯IAA；2-纯IAP；3-IAAP混合变现 |
| vip\_flag | number | 是 | 是否存在会员功能。 1-有；2-无 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number |  | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误，请重试 |
| 0 | 成功 |
| 1 | 不存在 |
| 2 | 参数错误 |
| 21000 | 该剧未授权播放，请通过后台api进行授权 |
| 21001 | 用户加密的sessionkey不存在 |
| 21002 | 商家的加密包未进行base64编码 |
| 21003 | 解密商家加密包失败，请确认是否按接入文档中给出的加密方案加密或sessionkey要使用当前用户最新的 |
| 21004 | 商家加密前的明文不是合法的json格式或者字段类型不对，请按接入文档排查 |
| 21005 | 商家加密中的必填参数值(openid、src\_appid及drama\_id)为空 |
| 21006 | 播放器的入参与商家加密包中的参数值不匹配 |
| 21007 | 加密包中的openid无效 |
| 21008 | 21008 开发者未开启预拉取 |
| 21009 | 21009 商家流量不足 |

---

### 获取短剧变现类型

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/dramaOthersAPI/api_developergetiaadrama.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| list | [objarray](#Body__list<Array>) | 是 | list |

**Body.list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src\_appid | string | 是 | 提审方小程序的appid |
| drama\_id | string | 是 | 提审的剧目id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| list | [objarray](#Res__list<Array>) | list |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| src\_appid | string | 提审方小程序的appid |
| drama\_id | string | 提审的剧目id |
| iaa\_type | number | 短剧变现类型。 1-纯IAA；2-纯IAP；3-IAAP混合变现 |
| vip\_flag | number | 是否存在会员功能。 1-有；2-无 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误，请重试 |
| 0 | 成功 |
| 1 | 不存在 |
| 2 | 参数错误 |
| 21000 | 该剧未授权播放，请通过后台api进行授权 |
| 21001 | 用户加密的sessionkey不存在 |
| 21002 | 商家的加密包未进行base64编码 |
| 21003 | 解密商家加密包失败，请确认是否按接入文档中给出的加密方案加密或sessionkey要使用当前用户最新的 |
| 21004 | 商家加密前的明文不是合法的json格式或者字段类型不对，请按接入文档排查 |
| 21005 | 商家加密中的必填参数值(openid、src\_appid及drama\_id)为空 |
| 21006 | 播放器的入参与商家加密包中的参数值不匹配 |
| 21007 | 加密包中的openid无效 |
| 21008 | 21008 开发者未开启预拉取 |
| 21009 | 21009 商家流量不足 |

---

### 批处理短剧合作推广计划

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/dramaOthersAPI/api_batchprocessdramapromotion.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action\_type | number | 是 | 操作类型。1-加入计划；2-查询计划；3-退出计划 |
| list | [objarray](#Body__list<Array>) | 是 | 短剧数组 |

**Body.list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src\_appid | string | 是 | 提审方小程序的appid |
| drama\_id | string | 是 | 提审的剧目id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| list | [objarray](#Res__list<Array>) | 短剧数组 |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| src\_appid | string | 提审方小程序的appid |
| drama\_id | string | 提审的剧目id |
| status | number | 短剧状态。 0-未加入计划；1-审核中；2-审核通过；3-审核拒绝；4-退出计划中；5-已被下架 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误，请重试 |
| 0 | 成功 |
| 1 | 不存在 |
| 2 | 参数错误 |
| 21000 | 该剧未授权播放，请通过后台api进行授权 |
| 21001 | 用户加密的sessionkey不存在 |
| 21002 | 商家的加密包未进行base64编码 |
| 21003 | 解密商家加密包失败，请确认是否按接入文档中给出的加密方案加密或sessionkey要使用当前用户最新的 |
| 21004 | 商家加密前的明文不是合法的json格式或者字段类型不对，请按接入文档排查 |
| 21005 | 商家加密中的必填参数值(openid、src\_appid及drama\_id)为空 |
| 21006 | 播放器的入参与商家加密包中的参数值不匹配 |
| 21007 | 加密包中的openid无效 |
| 21008 | 21008 开发者未开启预拉取 |
| 21009 | 21009 商家流量不足 |

---

### 获取短剧合作推广活动

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/dramaOthersAPI/api_getfinderevent.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event\_id\_list | array | 否 | 筛选短剧合作推广活动 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| finder\_event\_list | [objarray](#Res__finder_event_list<Array>) | 推广计划数组 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**Res.finder_event_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| encrypted\_event\_id | string | 活动id |
| event\_name | string | 活动名 |
| event\_url | string | 活动链接 |
| src\_appid | string | 提审小程序id |
| drama\_id | string | 提审剧目id |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误，请重试 |
| 0 | 成功 |
| 1 | 不存在 |
| 2 | 参数错误 |
| 21000 | 该剧未授权播放，请通过后台api进行授权 |
| 21001 | 用户加密的sessionkey不存在 |
| 21002 | 商家的加密包未进行base64编码 |
| 21003 | 解密商家加密包失败，请确认是否按接入文档中给出的加密方案加密或sessionkey要使用当前用户最新的 |
| 21004 | 商家加密前的明文不是合法的json格式或者字段类型不对，请按接入文档排查 |
| 21005 | 商家加密中的必填参数值(openid、src\_appid及drama\_id)为空 |
| 21006 | 播放器的入参与商家加密包中的参数值不匹配 |
| 21007 | 加密包中的openid无效 |
| 21008 | 21008 开发者未开启预拉取 |
| 21009 | 21009 商家流量不足 |

---

<!-- pages: 9 -->
