# 小程序服务端 API 结构化参考 — ad

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 回传广告数据（ad.addUserAction）

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/ad/Return_advertising_data.html

**云调用使用说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| contentType | string |  | 是 | 数据类型，传入 MIME Type |
| value | Buffer |  | 是 | 文件 Buffer |

**云调用使用说明**

| 属性 | 类型 | 位置 | 说明 |
| --- | --- | --- | --- |
| xxx | string | URL 参数 | ... |
| yyy | number | JSON body | ... |

**云调用使用说明**

| 属性 | 类型 | 位置 | 说明 |
| --- | --- | --- | --- |
| xxx | string | URL 参数 | ... |
| media | buffer | FormData | 图片 buffer |

---

### 广告数据源查询（ad.getUserActionSets）

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/ad/Advertising_data_source_query.html

**云调用使用说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| contentType | string |  | 是 | 数据类型，传入 MIME Type |
| value | Buffer |  | 是 | 文件 Buffer |

**云调用使用说明**

| 属性 | 类型 | 位置 | 说明 |
| --- | --- | --- | --- |
| xxx | string | URL 参数 | ... |
| yyy | number | JSON body | ... |

**云调用使用说明**

| 属性 | 类型 | 位置 | 说明 |
| --- | --- | --- | --- |
| xxx | string | URL 参数 | ... |
| media | buffer | FormData | 图片 buffer |

---

### 广告创建数据源（ad.addUserActionSet）

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/ad/Advertisement_creation_data_source.html

**云调用使用说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| contentType | string |  | 是 | 数据类型，传入 MIME Type |
| value | Buffer |  | 是 | 文件 Buffer |

**云调用使用说明**

| 属性 | 类型 | 位置 | 说明 |
| --- | --- | --- | --- |
| xxx | string | URL 参数 | ... |
| yyy | number | JSON body | ... |

**云调用使用说明**

| 属性 | 类型 | 位置 | 说明 |
| --- | --- | --- | --- |
| xxx | string | URL 参数 | ... |
| media | buffer | FormData | 图片 buffer |

---

### 广告数据源报表查询（ad.getUserActionSetReports）

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/ad/Advertising_data_source_report_query.html

**云调用使用说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| contentType | string |  | 是 | 数据类型，传入 MIME Type |
| value | Buffer |  | 是 | 文件 Buffer |

**云调用使用说明**

| 属性 | 类型 | 位置 | 说明 |
| --- | --- | --- | --- |
| xxx | string | URL 参数 | ... |
| yyy | number | JSON body | ... |

**云调用使用说明**

| 属性 | 类型 | 位置 | 说明 |
| --- | --- | --- | --- |
| xxx | string | URL 参数 | ... |
| media | buffer | FormData | 图片 buffer |

---

<!-- pages: 4 -->
