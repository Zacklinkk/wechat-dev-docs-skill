# 小程序服务端 API 结构化参考 — API/wxsearch

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 搜一搜数据推送

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/wxsearch/api_submitpages.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pages | [objarray](#Body__pages<Array>) | 是 | 请求提交的小程序页面信息数组，一次可提交多个页面的信息。（注意：path+query标识唯一一个页面，微信侧会使用这个信息构造唯一id） |

**Body.pages(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 以pages/开头的小程序页面路径。 |
| query | string | 是 | 小程序页面请求参数 |
| data\_list | [objarray](#Body__pages<Array>__data_list<Array>) | 是 | 小程序页面的数据，一个页面可以同时提交多个结构化信息 |

**Body.pages(Array).data_listObject Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| @type | string | 是 | 数据结构类型，用于标识目标业务系统 | [枚举值](#Enum_Body__pages<Array>__data_list<Array>__@type) |
| update | number | 是 | 更新字段；内容更新按照新增处理，如果页面路径（path+query）相同，微信会做覆盖更新。 | [枚举值](#Enum_Body__pages<Array>__data_list<Array>__update) |
| content\_id | string | 是 | 数据方自定义 id | - |
| page\_type | number | 是 | 页面类型，固定填2 | - |
| h5\_url | string | 否 | H5链接，推荐填写，如果该页面有对应的H5链接，则填上 | - |
| title | string | 是 | 标题，长度建议在20个字 | - |
| abstract | array | 否 | 摘要，添加摘要有利于召回 | - |
| referer | string | 否 | HTTP Referer，如果图片有防盗链逻辑，需要设置referer头，用于图片下载 | - |
| cover\_img\_url | string | 否 | 封面图URL，图片url访问如果有有效期，建议设置为15天以上 | - |
| mainbody | string | 是 | 正文，不可带有html标签 | - |
| author | [object](#Body__pages<Array>__data_list<Array>__author) | 否 | 作者信息，推荐医疗类填写医生信息 | - |
| video | [objarray](#Body__pages<Array>__data_list<Array>__video<Array>) | 否 | 视频 | - |
| time\_publish | number | 是 | 发布时间，unix时间戳，单位秒 | - |
| time\_modify | number | 是 | 更新时间，unix时间戳，单位秒 | - |
| extra\_info | [object](#Body__pages<Array>__data_list<Array>__extra_info) | 否 | 补充字段，通用字段无法满足要求时，需要额外补充的字段，具体字段内容需要与微信协商 | - |

**Body.pages(Array).data_list.author Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| author\_name | string | 是 | 作者名字 |
| author\_title | string | 否 | 作者职务 |
| author\_portrait | string | 否 | 作者头像URL，头像尺寸不低于36px\*36px。图片url访问如果有有效期，建议设置为15天以上 |

**Body.pages(Array).data_list.videoObject Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| video\_title | string | 否 | 视频标题，如不填，则视为与页面标题一致 |
| video\_length | number | 是 | 视频时长，单位为秒，优先五分钟内短视频 |
| video\_img | string | 是 | 视频封面图URL，尺寸不低于686px\*288px。图片url访问如果有有效期，建议设置为15天以上 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**Body.pages(Array).data_list.@type Enum**

| 枚举值 | 描述 |
| --- | --- |
| wxsearch\_cpdata | 正式数据，对应搜一搜正式环境，可被用户检索到 |
| wxsearch\_testcpdata | 审核数据，对应搜一搜数据审核环境，用于数据审核及格式校验，不在搜索结果中展示 |

**Body.pages(Array).data_list.update Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 新增 |
| 3 | 删除 |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40066 | invalid url | 小程序url配置了sitemap disallow |
| 40211 | invalid scope\_data | 数据结构校验失败，附带进一步错误字段，如unexpected instance type: /content\_id，表示content\_id类型错误。 |
| 40212 | invalid query | 不合法query |
| 40219 | pages is empty | pages参数为空 |
| 45002 | content size out of limit | http请求包过大，建议拆分或使用压缩 |
| 47001 | data format error | http请求包不是合法Json |
| 47004 | submit pages count more than each quota | 每次提交的页面数超过1000（备注：每次提交页面数应小于或等于1000, 增量数据推荐单条推送） |
| 47006 | submit pages count reach daily limit, please try tomorrow | 当天提交页面数达到了配额上限，请明天再试（备注：每日限额页面数为50w） |
| 85083 | search status is banned | 小程序的搜索功能被禁用 |
| 85091 | search status was turned off | 小程序的搜索开关被关闭。请访问设置页面打开 |
| 108001 | system error | 系统失败，重试即可，请求中的页面可能部分成功 |
| 108002 | page size out of limit | 单个页面大小超过阈值（最大为1M） |
| 108003 | permission denied | 审核数据前，需提交申请；推送正式数据前，需等待审核通过 |

---

<!-- pages: 1 -->
