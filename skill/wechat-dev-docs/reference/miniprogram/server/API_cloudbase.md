# 小程序服务端 API 结构化参考 — API/cloudbase

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 触发云函数

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/functions/api_invokecloudfunction.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 云开发环境 ID，用于指定要触发云函数的环境 |
| name | string | 是 | 云函数名称，即要触发的云函数的函数名 |
| req\_data | string | 是 | 传递给云函数的输入参数，为 JSON 字符串格式。具体结构由开发者根据云函数业务逻辑自定义定义 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | 错误码，0 表示成功，其他值表示失败 |
| errmsg | string | 错误信息，成功时返回 "ok" |
| resp\_data | string | 云函数返回的数据，为 JSON 字符串格式。内容由云函数业务逻辑决定 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40014 | invalid access\_token | 不合法的 access\_token ，请开发者认真比对 access\_token 的有效性（如是否过期），或查看是否正在为恰当的公众号调用接口 |
| 40101 | missing parameter | 缺少必填参数 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 43002 | require POST method | 需要 POST 请求 |
| 44002 | empty post data | POST 的数据包为空。post请求body参数不能为空。 |
| 85088 | no qbase privilege | 该APP未开通云开发 |

---

### 延时调用云函数

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/functions/api_adddelayedfunctiontask.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 环境ID |
| function\_name | string | 是 | 函数名称 |
| data | string | 是 | 发送的数据包，格式必须为JSONString |
| delay\_time | number | 是 | 延迟时间，单位：秒，合法范围：6秒-30天 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -501000 | Param Invalid: env check invalid be filterd |  |
| -1000 | system error | 系统错误 |

**7. 适用范围**

| 小程序 | 小游戏 | 第三方平台 |
| --- | --- | --- |
| ✔ | ✔ | 〇 |

---

### 数据库插入记录

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/database/api_adddatabaseitem.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 云环境ID |
| query | string | 是 | 数据库操作语句 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| id\_list | array | 插入成功的数据集合主键\_id |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1000 | system error | 系统错误 |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 0 | ok | ok |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40014 | invalid access\_token | 不合法的 access\_token ，请开发者认真比对 access\_token 的有效性（如是否过期），或查看是否正在为恰当的公众号调用接口 |
| 40097 | invalid args | 参数错误 |
| 40101 | missing parameter | 缺少必填参数 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 43002 | require POST method | 需要 POST 请求 |
| 44002 | empty post data | POST 的数据包为空 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 85088 | no qbase privilege | 该APP未开通云开发 |

---

### 数据库聚合

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/database/api_aggregatedatabase.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 云环境ID |
| query | string | 是 | 数据库操作语句 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| data | array | 记录数组 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -501000 | 未知错误 | 请提工单反馈 |
| -1000 | system error | 系统错误 |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 0 | ok | ok |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40014 | invalid access\_token | 不合法的 access\_token ，请开发者认真比对 access\_token 的有效性（如是否过期），或查看是否正在为恰当的公众号调用接口 |
| 40097 | invalid args | 参数错误 |
| 40101 | missing parameter | 缺少必填参数 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 43002 | require POST method | 需要 POST 请求 |
| 44002 | empty post data | POST 的数据包为空 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 85088 | no qbase privilege | 该APP未开通云开发 |

---

### 新增集合

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/database/api_adddatabasecollection.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 云环境ID |
| collection\_name | string | 是 | 集合名称 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -501000 | 未知错误 | 请提工单联系我们 |
| -1000 | system error | 系统错误 |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 0 | ok | ok |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40014 | invalid access\_token | 不合法的 access\_token ，请开发者认真比对 access\_token 的有效性（如是否过期），或查看是否正在为恰当的公众号调用接口 |
| 40097 | invalid args | 参数错误 |
| 40101 | missing parameter | 缺少必填参数 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 43002 | require POST method | 需要 POST 请求 |
| 44002 | empty post data | POST 的数据包为空 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 85088 | no qbase privilege | 该APP未开通云开发 |

---

### 删除集合

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/database/api_deletedatabasecollection.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 云环境ID |
| collection\_name | string | 是 | 集合名称 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1000 | system error | 系统错误 |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 0 | ok | ok |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40014 | invalid access\_token | 不合法的 access\_token ，请开发者认真比对 access\_token 的有效性（如是否过期），或查看是否正在为恰当的公众号调用接口 |
| 40097 | invalid args | 参数错误 |
| 40101 | missing parameter | 缺少必填参数 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 43002 | require POST method | 需要 POST 请求 |
| 44002 | empty post data | POST 的数据包为空 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 85088 | no qbase privilege | 该APP未开通云开发 |

---

### 获取集合信息

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/database/api_getdatabasecollection.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 云环境ID |
| limit | number | 否 | 获取数量限制 |
| offset | number | 否 | 偏移量 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| collections | [objarray](#Res__collections<Array>) | 集合信息 |
| pager | [object](#Res__pager) | 分页信息 |

**Res.collections(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| name | string | 集合名 |
| count | number | 表中文档数量 |
| size | number | 表的大小（即表中文档总大小），单位：字节 |
| index\_count | number | 索引数量 |
| index\_size | number | 索引占用大小，单位：字节 |

**Res.pager Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Offset | number | 偏移 |
| Limit | number | 单次查询限制 |
| Total | number | 符合查询条件的记录总数 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1000 | system error | 系统错误 |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 0 | ok | ok |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40014 | invalid access\_token | 不合法的 access\_token ，请开发者认真比对 access\_token 的有效性（如是否过期），或查看是否正在为恰当的公众号调用接口 |
| 40097 | invalid args | 参数错误 |
| 40101 | missing parameter | 缺少必填参数 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 43002 | require POST method | 需要 POST 请求 |
| 44002 | empty post data | POST 的数据包为空 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 85088 | no qbase privilege | 该APP未开通云开发 |

---

### 统计集合记录数

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/database/api_getdatabasecount.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 云环境ID |
| query | string | 是 | 数据库操作语句 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| count | number | 记录数量 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1000 | system error | 系统错误 |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 0 | ok | ok |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40014 | invalid access\_token | 不合法的 access\_token ，请开发者认真比对 access\_token 的有效性（如是否过期），或查看是否正在为恰当的公众号调用接口 |
| 40097 | invalid args | 参数错误 |
| 40101 | missing parameter | 缺少必填参数 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 43002 | require POST method | 需要 POST 请求 |
| 44002 | empty post data | POST 的数据包为空 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 85088 | no qbase privilege | 该APP未开通云开发 |

---

### 数据库删除记录

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/database/api_deletedatabaseitem.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 云环境ID |
| query | string | 是 | 数据库操作语句 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| deleted | number | 删除记录数量 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1000 | system error | 系统错误 |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 0 | ok | ok |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40014 | invalid access\_token | 不合法的 access\_token ，请开发者认真比对 access\_token 的有效性（如是否过期），或查看是否正在为恰当的公众号调用接口 |
| 40097 | invalid args | 参数错误 |
| 40101 | missing parameter | 缺少必填参数 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 43002 | require POST method | 需要 POST 请求 |
| 44002 | empty post data | POST 的数据包为空 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 85088 | no qbase privilege | 该APP未开通云开发 |

---

### 数据库导出

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/database/api_exportdatabaseitem.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| env | string | 是 | 云环境ID | - |
| file\_path | string | 是 | 导出文件路径（文件会导出到公共的云存储中，可使用[getDownloadTcbFileLink接口](../storage/api_getdownloadtcbfilelink)获取下载链接） | - |
| file\_type | number | 是 | 导出文件类型，文件格式参考[importDatabaseItem接口](api_importdatabaseitem)的文件格式部分 | [枚举值](#Enum_Body__file_type) |
| query | string | 是 | 导出条件 | - |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| job\_id | number | 导出任务ID，使用[getDatabaseMigrateStatus接口](api_getdatabasemigratestatus)查询导出结果，获取文件下载链接。 |

**Body.file_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | JSON |
| 2 | CSV |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1000 | system error | 系统错误 |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 0 | ok | ok |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40014 | invalid access\_token | 不合法的 access\_token ，请开发者认真比对 access\_token 的有效性（如是否过期），或查看是否正在为恰当的公众号调用接口 |
| 40097 | invalid args | 参数错误 |
| 40101 | missing parameter | 缺少必填参数 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 43002 | require POST method | 需要 POST 请求 |
| 44002 | empty post data | POST 的数据包为空 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 85088 | no qbase privilege | 该APP未开通云开发 |

---

### 数据库导入

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/database/api_importdatabaseitem.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 云环境ID |
| collection\_name | string | 是 | 导入 collection 名 |
| file\_path | string | 是 | 导入文件路径(导入文件需先上传到同环境的存储中，可使用开发者工具或 [getUploadTcbFileLink接口](../storage/api_getuploadtcbfilelink)上传） |
| file\_type | number | 是 | 导入文件类型。1表示JSON。2表示CSV |
| stop\_on\_error | boolean | 是 | 是否在遇到错误时停止导入 |
| conflict\_mode | number | 是 | 冲突处理模式。1表示INSERT。2表示UPSERT。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| job\_id | number | 导入任务ID，可使用[getDatabaseMigrateStatus接口](api_getdatabasemigratestatus)查询导入进度及结果 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -501000 |  |  |
| -1000 | system error | 系统错误 |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 0 | ok | ok |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40014 | invalid access\_token | 不合法的 access\_token ，请开发者认真比对 access\_token 的有效性（如是否过期），或查看是否正在为恰当的公众号调用接口 |
| 40097 | invalid args | 参数错误 |
| 40101 | missing parameter | 缺少必填参数 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 43002 | require POST method | 需要 POST 请求 |
| 44002 | empty post data | POST 的数据包为空 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 85088 | no qbase privilege | 该APP未开通云开发 |

---

### 数据库迁移状态查询

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/database/api_getdatabasemigratestatus.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 云环境ID |
| job\_id | number | 是 | 迁移任务ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| status | string | 导出状态 |
| record\_success | number | 导出成功记录数 |
| record\_fail | number | 导出失败记录数 |
| error\_msg | string | 导出错误信息 |
| file\_url | string | 导出文件下载地址 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1000 | system error | 系统错误 |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 0 | ok | ok |
| 40014 | invalid access\_token | 不合法的 access\_token ，请开发者认真比对 access\_token 的有效性（如是否过期），或查看是否正在为恰当的公众号调用接口 |
| 40097 | invalid args | 参数错误 |
| 40101 | missing parameter | 缺少必填参数 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 43002 | require POST method | 需要 POST 请求 |
| 44002 | empty post data | POST 的数据包为空 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 85088 | no qbase privilege | 该APP未开通云开发 |

---

### 数据库查询记录

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/database/api_getdatabaserecord.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 云环境ID |
| query | string | 是 | 数据库操作语句 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| pager | [object](#Res__pager) | 分页信息 |
| data | array | 记录数组 |

**Res.pager Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Offset | number | 偏移 |
| Limit | number | 单次查询限制 |
| Total | number | 符合查询条件的记录总数 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1000 | system error | 系统错误 |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40014 | invalid access\_token | 不合法的 access\_token ，请开发者认真比对 access\_token 的有效性（如是否过期），或查看是否正在为恰当的公众号调用接口 |
| 40097 | invalid args | 参数错误 |
| 40101 | missing parameter | 缺少必填参数 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 43002 | require POST method | 需要 POST 请求 |
| 44002 | empty post data | POST 的数据包为空 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 85088 | no qbase privilege | 该APP未开通云开发 |

---

### 数据库更新记录

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/database/api_updatedatabaserecord.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 云环境ID |
| query | string | 是 | 数据库操作语句 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| matched | number | 更新条件匹配到的结果数 |
| modified | number | 修改的记录数，注意：使用set操作新插入的数据不计入修改数目 |
| id | string | 新插入记录的id，注意：只有使用set操作新插入数据时这个字段会有值 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1000 | system error | 系统错误 |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 0 | ok | ok |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40014 | invalid access\_token | 不合法的 access\_token ，请开发者认真比对 access\_token 的有效性（如是否过期），或查看是否正在为恰当的公众号调用接口 |
| 40097 | invalid args | 参数错误 |
| 40101 | missing parameter | 缺少必填参数 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 43002 | require POST method | 需要 POST 请求 |
| 44002 | empty post data | POST 的数据包为空 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 85088 | no qbase privilege | 该APP未开通云开发 |

---

### 更新数据库索引

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/database/api_updatedatabaseindexs.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 云环境ID |
| collection\_name | string | 是 | 集合名称 |
| create\_indexes | [objarray](#Body__create_indexes<Array>) | 是 | 新增索引 |
| drop\_indexes | [objarray](#Body__drop_indexes<Array>) | 是 | 删除索引 |

**Body.create_indexes(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 索引名 |
| unique | boolean | 是 | 是否唯一 |
| keys | [objarray](#Body__create_indexes<Array>__keys<Array>) | 是 | 索引字段 |

**Body.drop_indexes(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 索引名 |
| unique | boolean | 是 | 是否唯一 |
| keys | [objarray](#Body__drop_indexes<Array>__keys<Array>) | 是 | 索引字段 |

**Body.create_indexes(Array).keysObject Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 字段名 |
| direction | string | 是 | 字段排序 |

**Body.drop_indexes(Array).keysObject Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 字段名 |
| direction | string | 是 | 字段排序 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1000 | system error | 系统错误 |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 0 | ok | ok |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40014 | invalid access\_token | 不合法的 access\_token ，请开发者认真比对 access\_token 的有效性（如是否过期），或查看是否正在为恰当的公众号调用接口 |
| 40097 | invalid args | 参数错误 |
| 40101 | missing parameter | 缺少必填参数 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 43002 | require POST method | 需要 POST 请求 |
| 44002 | empty post data | POST 的数据包为空 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 85088 | no qbase privilege | 该APP未开通云开发 |

---

### 获取文件上传链接

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/storage/api_getuploadtcbfilelink.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 云环境ID |
| path | string | 是 | 上传路径 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| url | string | 上传url |
| token | string | token |
| authorization | string | authorization |
| file\_id | string | 文件ID |
| cos\_file\_id | string | cos文件ID |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1000 | system error | 系统错误 |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 0 | ok | ok |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40014 | invalid access\_token | 不合法的 access\_token ，请开发者认真比对 access\_token 的有效性（如是否过期），或查看是否正在为恰当的公众号调用接口 |
| 40097 | invalid args | 参数错误 |
| 40101 | missing parameter | 缺少必填参数 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 43002 | require POST method | 需要 POST 请求 |
| 44002 | empty post data | POST 的数据包为空 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 85088 | no qbase privilege | 该APP未开通云开发 |

---

### 获取文件下载链接

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/storage/api_getdownloadtcbfilelink.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 环境id |
| file\_list | [objarray](#Body__file_list<Array>) | 是 | 文件列表 |

**Body.file_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileid | string | 是 | 文件id |
| max\_age | number | 是 | 下载链接有效期 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| file\_list | [objarray](#Res__file_list<Array>) | 文件列表 |

**Res.file_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| fileid | string | 文件ID |
| download\_url | string | 下载链接 |
| status | number | 状态码 |
| errmsg | string | 该文件错误信息 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -501007 | 参数有误，具体原因参考 errmsg |  |
| -501002 | 云资源通用错误：云端响应超时 |  |
| -501000 | 未知错误 | 请提工单反馈 |
| -1000 | system error | 系统错误 |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 0 | ok | ok |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40014 | invalid access\_token | 不合法的 access\_token ，请开发者认真比对 access\_token 的有效性（如是否过期），或查看是否正在为恰当的公众号调用接口 |
| 40097 | invalid args | 参数错误 |
| 40101 | missing parameter | 缺少必填参数 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 43002 | require POST method | 需要 POST 请求 |
| 44002 | empty post data | POST 的数据包为空 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 85088 | no qbase privilege | 该APP未开通云开发 |

---

### 删除文件

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/storage/api_deletetcbcloudfile.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 云环境ID |
| fileid\_list | array | 是 | 文件 ID 列表 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| delete\_list | [objarray](#Res__delete_list<Array>) | 文件列表 |

**Res.delete_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| fileid | string | 文件id |
| status | number | 状态 |
| errmsg | string | 错误信息 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -501002 | 云资源通用错误：云端响应超时 |  |
| -1000 | system error | 系统错误 |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 0 | ok | ok |
| 40014 | invalid access\_token | 不合法的 access\_token ，请开发者认真比对 access\_token 的有效性（如是否过期），或查看是否正在为恰当的公众号调用接口 |
| 40097 | invalid args | 参数错误 |
| 40101 | missing parameter | 缺少必填参数 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 43002 | require POST method | 需要 POST 请求 |
| 44002 | empty post data | POST 的数据包为空 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 85088 | no qbase privilege | 该APP未开通云开发 |

---

### 发送短信v2

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/others/api_newsendcloudbasesms.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 环境 ID |
| url\_link | string | 是 | URL Link |
| template\_id | string | 是 | 短信模版 ID。(844110: 营销类短信模版 ID) |
| template\_param\_list | array | 是 | 短信模版变量数组 |
| phone\_number\_list | array | 是 | 手机号列表，单次请求最多支持 1000 个境内手机号，手机号必须以+86开头 |
| use\_short\_name | boolean | 是 | 是否使用小程序简称 |
| resource\_appid | string | 是 | 资源方appid，第三方代开发时可填第三方appid或小程序appid，应为所填环境所属的账号APPID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| send\_status\_list | [objarray](#Res__send_status_list<Array>) | 开放数据列表 |

**Res.send_status_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| serial\_no | string | 发送流水号 |
| phone\_number | string | 手机号码 |
| code | string | 短信请求错误码 |
| message | string | 短信请求错误码描述 |
| iso\_code | string | 国家码或地区码 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -607004 | 无效的 URL Link |  |
| -601033 | 仅支持非个人主体小程序 |  |
| -601032 | 小程序昵称不能为空 |  |
| -601027 | 无效的环境 ID | 检查环境 ID 是否填写正确 |
| -501007 | 参数有误，具体原因参考 errmsg |  |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 发送短信

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/others/api_sendcloudbasesms.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 环境 ID |
| phone\_number\_list | array | 是 | 手机号列表，单次请求最多支持 1000 个境内手机号，手机号必须以+86开头 |
| sms\_type | number | 是 | 短信类型，营销类短信：Marketing；通知类短信：Notification |
| template\_id | string | 是 | sms\_type="Notification" 时必填，模版 ID |
| content | string | 是 | sms\_type="Marketing" 时必填，自定义短信内容，一条短信最多为70个字。可自定义内容最多为 30 个字符，详情参考短信规则 |
| path | string | 是 | sms\_type="Marketing" 时必填，云开发静态网站 path，不需要指定域名，例如/index.html |
| template\_param\_list | array | 是 | sms\_type="Notification" 时必填，短信模版变量数组 |
| use\_short\_name | boolean | 是 | 是否使用小程序简称 |
| resource\_appid | string | 是 | 资源方appid，第三方代开发时可填第三方appid或小程序appid，应为所填环境所属的账号APPID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| send\_status\_list | [objarray](#Res__send_status_list<Array>) | 开放数据列表 |

**Res.send_status_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| serial\_no | string | 发送流水号 |
| phone\_number | string | 手机号码 |
| code | string | 短信请求错误码 |
| message | string | 短信请求错误码描述 |
| iso\_code | string | 国家码或地区码 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -607004 | 无效的 URL Link |  |
| -607001 | 无效的静态网站 Path | 检查静态网站 Path 是否填写正确 |
| -601033 | 仅支持非个人主体小程序 |  |
| -601032 | 小程序昵称不能为空 |  |
| -601028 | 没有开通静态网站 | 请在微信开发者工具开通静态网站（云开发/设置/拓展功能） |
| -601027 | 无效的环境 |  |
| -601027 | 无效的环境 ID | 检查环境 ID 是否填写正确 |
| -501007 | 参数有误，具体原因参考 errmsg |  |
| -501007 | 参数有误，具体原因参考 errmsg |  |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 创建发短信任务

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/others/api_createsendsmstask.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 环境 ID |
| file\_url | string | 是 | 短信 CSV 文件地址CodeUri |
| template\_id | string | 是 | 短信模版 ID 默认值：844110（销类短信模版 ID) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| query\_id | string | 查询 ID |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -601033 | 仅支持非个人主体小程序 |
| -601032 | 小程序昵称不能为空 |
| -601028 | 该环境没有开通静态网站 |
| -601027 | 无效的环境 |
| -501007 | 参数有误，具体原因参考 errmsg |
| -1 | 系统繁忙，此时请开发者稍候再试 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 云开发上报接口

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/others/api_cloudbasereportapi.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| report\_action | string | 是 | 上报动作，目前支持（sendSmsTask：发送短信；openH5：H5 打开） |
| env\_id | string | 是 | [环境 ID](https://developers.weixin.qq.com/miniprogram/dev/wxcloud/basis/quickstart.html) |
| activity\_id | string | 是 | 活动 ID |
| task\_id | string | 是 | 任务 ID【report\_action 取 sendSmsTask 时必填】 |
| phone\_count | string | 是 | 下发手机号数量【report\_action 取 sendSmsTask 时必填】 |
| channel\_id | string | 是 | 渠道 ID（云开发 CMS 使用 \_cms\_sms\_）【report\_action 取 openH5 时必填】 |
| session\_id | string | 是 | 会话 ID【report\_action 取 openH5 时必填】 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 查询短信记录

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/others/api_describesmsrecords.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| EnvId | string | 是 | 环境 ID |
| StartDate | string | 是 | 开始日期, 如:2021-01-01 |
| EndDate | string | 是 | 结束日期, 如2021-01-07 |
| Mobile | string | 是 | 电话号码 |
| QueryId | string | 是 | 查询ID |
| PageNumber | number | 是 | 页码(1开始) |
| PageSize | number | 是 | 每页条目数 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| SmsRecords | [objarray](#Res__SmsRecords<Array>) | 发送记录列表 |
| TotalCount | number | 记录总数 |
| RequestId | string | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**Res.SmsRecords(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Mobile | string | 手机号码 |
| Content | string | 短信内容 |
| ContentSize | number | 短信内容长度 |
| Fee | number | 计费条数 |
| CreateTime | string | 发送时间 |
| ReceivedTime | string | 用户接收时间 |
| Status | string | sent(成功), error(失败) |
| Remarks | string | 备注 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 85088 | no qbase privilege | 该APP未开通云开发 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 描述扩展上传文件信息

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/others/api_describeextensionuploadinfo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ExtensionFiles | [objarray](#Body__ExtensionFiles<Array>) | 是 | 待上传的文件列表 |

**Body.ExtensionFiles(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| FileType | string | 是 | 文件类型。枚举值 FUNCTION：函数代码 STATIC：静态托管代码 SMS：短信文件 |
| FileName | string | 是 | 文件名，长度不超过24 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| FilesData | [objarray](#Res__FilesData<Array>) | 待上传文件的信息数组 |
| RequestId | string | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。 |

**Res.FilesData(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| CodeUri | string | 模板里使用的地址 |
| UploadUrl | string | 上传文件的临时地址，含签名 |
| CustomKey | string | 自定义密钥。如果为空，则表示不需要加密 |
| MaxSize | number | 文件大小限制，单位M，客户端上传前需要主动检查文件大小，超过限制的文件会被删除。 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取云开发数据

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/others/api_getcloudbasestatistics.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | string | 是 | 获取动作，目前支持（smsMarketingOverviewData：短信营销概览数据；smsMarketingConversionData：短信营销转化数据；smsMarketingRealTimeData：短信营销实时数据） |
| begin\_date | number | 是 | 开始时间戳 |
| end\_date | number | 是 | 结束时间戳 |
| page\_limit | number | 是 | 分页 limit【action 取 smsMarketingOverviewData、smsMarketingConversionData 时必填】 |
| page\_offset | number | 是 | 分页 offset【action 取 smsMarketingOverviewData、smsMarketingConversionData 时必填】 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| data\_column | [objarray](#Res__data_column<Array>) | 数据列定义 |
| data\_value | [objarray](#Res__data_value<Array>) | 数据行 |
| total\_num | number | 总行数 |

**Res.data_column(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| col\_id | string | 列 id |
| col\_name | string | 列名 |
| col\_data\_type | string | 数据类型（0:string；1:number；2:double） |

**Res.data_value(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| data\_value | array | 数据值 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 10011 | 没有数据 |  |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取cloudID对应的数据

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/others/api_getopendata.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| openid | string | 否 | 用户openid（敏感信息需要传入） |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cloudid\_list | array | 是 | CloudID 列表 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| data\_list | [objarray](#Res__data_list<Array>) | 开放数据列表 |

**Res.data_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| cloud\_id | string | cloud id |
| json | string | 数据详情 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ |

---

### 获取实时语音签名

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/others/api_getcloudbasevoipsign.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| group\_id | string | 是 | 游戏房间的标识 |
| timestamp | number | 是 | 生成这个随机字符串的 UNIX 时间戳（精确到秒） |
| nonce | string | 是 | 随机字符串，长度应小于 128 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| signature | string | 签名 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ |

---

### 获取腾讯云API调用凭证

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/others/api_getcloudtoken.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lifespan | number | 是 | 有效期（单位为秒，最大7200） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| secretid | string | secretid |
| secretkey | string | secretkey |
| token | string | token |
| expired\_time | number | 过期时间戳 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1000 | system error | 系统错误 |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 0 | ok | ok |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40014 | invalid access\_token | 不合法的 access\_token ，请开发者认真比对 access\_token 的有效性（如是否过期），或查看是否正在为恰当的公众号调用接口 |
| 40097 | invalid args | 参数错误 |
| 40101 | missing parameter | 缺少必填参数 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 43002 | require POST method | 需要 POST 请求 |
| 44002 | empty post data | POST 的数据包为空 |
| 45009 | reach max api daily quota limit | 调用超过天级别频率限制。可调用clear\_quota接口恢复调用额度。 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 85088 | no qbase privilege | 该APP未开通云开发 |

---

<!-- pages: 28 -->
