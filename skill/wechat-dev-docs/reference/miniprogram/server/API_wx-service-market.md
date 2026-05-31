# 小程序服务端 API 结构化参考 — API/wx-service-market

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 调用服务市场接口

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/wx-service-market/api_invokeservice.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| service | string | 是 | 服务 ID，在每个接口详情页面中均可以找到服务id，请查看文档末尾截图 |
| api | string | 是 | 接口名；在每个接口详情页面中均可以找到api name，请查看文档末尾截图 |
| data | string | 是 | 服务提供方接口定义的 JSON 格式的数据，请看每个服务的接口文档详情 |
| client\_msg\_id | string | 是 | 随机字符串 ID，调用方请求的唯一标识 |
| async | boolean | 否 | 是否是异步API，当是异步调用时，必须填true |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| data | string | 回包信息 |
| request\_id | string | 异步调用才会返回，唯一id |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 43002 | require POST method | 方法调用错误，请用 post 方法调用 |
| 44002 | empty post data | POST 的数据包为空。post请求body参数不能为空。 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;参数需以 JSON 字符串格式写在post请求的 body 中，请检查修正后重试 |
| 9301001 | invalid parameter | 修改入参后重试 |
| 9301002 | call api service failed | 函数调用失败，检查参数后重试 |
| 9301003 | internal exception | 系统失败 |
| 9301010 | consumption failure | 扣费失败，可能费用为0，需要重新购买/重试 |
| 9301011 |  | 频率限制 |
| 9301012 | service timeout | 服务访问超时，检查参数后重试 |
| 9301014 |  | RequestID |
| 9301015 |  | 后端尚未处理完成 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 | 移动应用 | 视频号助手 |
| --- | --- | --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |

---

### 异步获取处理数据

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/wx-service-market/api_servicemarketretrieve.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request\_id | string | 是 | 调用接口[invokeService](api_invokeservice)接口返回的request\_id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| data | string | 回包信息 |
| request\_id | string | 唯一id |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok | 成功 |
| 9301001 |  | 参数错误 |
| 9301002 | call api service failed | 调用后端服务失败 |
| 9301003 | internal exception | 系统失败 |
| 9301010 | consumption failure | 配额不足 |
| 9301011 |  | 频率限制 |
| 9301012 |  | 服务处理超时 |
| 9301014 |  | RequestID |
| 9301015 |  | 后端尚未处理完成 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 | 移动应用 | 视频号助手 |
| --- | --- | --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |

---

<!-- pages: 2 -->
