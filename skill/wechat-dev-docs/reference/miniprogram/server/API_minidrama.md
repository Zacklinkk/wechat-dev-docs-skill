# 小程序服务端 API 结构化参考 — API/minidrama

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 单个文件上传

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_fileupload/api_singlefileupload.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| media\_name | string | 是 | 我的演艺 - 第1集 | 文件名，需按照“剧目名 - 对应剧集数”格式命名文件 |
| media\_type | string | 是 | MP4 | 视频格式，支持：MP4，TS，MOV，MXF，MPG，FLV，WMV，AVI，M4V，F4V，MPEG，3GP，ASF，MKV |
| media\_data | buffer | 是 | - | 视频文件内容，二进制。 |
| cover\_type | string | 否 | JPG | 视频封面图格式，支持：JPG、JPEG、PNG、BMP、TIFF、AI、CDR、EPS、TIF |
| cover\_data | buffer | 否 | - | 视频封面图文件内容，二进制。 |
| source\_context | string | 否 | - | 来源上下文，会在上传完成事件中透传给开发者。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| media\_id | number | - | 媒体文件id。 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 拉取上传

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_fileupload/api_pullupload.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| media\_name | string | 是 | 我的演艺 - 第1集 | 文件名，需按照“剧目名 - 对应剧集数”格式命名文件 |
| media\_url | string | 是 | https://developers.weixin.qq.com/test.mp4 | 视频 URL |
| cover\_url | string | 否 | https://developers.weixin.qq.com/test.jpg | 封面图URL |
| source\_context | string | 否 | - | 来源上下文，会在上传完成事件中透传给开发者。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| task\_id | number | - | 拉取上传任务id。 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 查询任务

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_fileupload/api_gettask.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task\_id | number | 是 | 任务id |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| task\_info | [object](#Res__task_info) | - | 任务信息 |

**Res.task_info Object Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| id | number | 任务id | - |
| task\_type | number | 任务类型 | [枚举值](#Enum_Res__task_info__task_type) |
| status | number | 任务状态 | [枚举值](#Enum_Res__task_info__status) |
| errcode | number | 任务错误码，0表示成功，其它表示失败 | - |
| errmsg | string | 任务错误原因 | - |
| create\_time | number | 创建时间，时间戳 | - |
| finish\_time | number | 完成时间，时间戳 | - |
| media\_id | number | 媒体文件id | - |

**Res.task_info.task_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 拉取上传任务 |

**Res.task_info.status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 等待中 |
| 2 | 正在处理 |
| 3 | 已完成 |
| 4 | 失败 |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 申请分片上传

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_fileupload/api_applyupload.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| media\_name | string | 是 | 我的演艺 - 第1集 | 文件名，需按照“剧目名 - 对应剧集数”格式命名文件 |
| media\_type | string | 是 | MP4 | 视频格式，支持：MP4，TS，MOV，MXF，MPG，FLV，WMV，AVI，M4V，F4V，MPEG，3GP，ASF，MKV |
| cover\_type | string | 否 | JPG | 封面图图片格式，支持：JPG、JPEG、PNG、BMP、TIFF、AI、CDR、EPS、TIF |
| source\_context | string | 否 | - | 来源上下文，会在上传完成事件中透传给开发者。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| upload\_id | string | 本次分片上传的唯一标识 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 上传分片

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_fileupload/api_uploadpart.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| upload\_id | string | 是 | 一次分片上传的唯一标识，由[申请分片](api_applyupload)上传接口返回。 |
| part\_number | number | 是 | 本次上传的分片的编号，范围在 1 - 100。 |
| resource\_type | number | 是 | 指定该分片属于视频还是图片的枚举值：1. 视频，2. 图片。 |
| data | binary | 是 | 文件内容分片，二进制。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| etag | string | 根据分片内容生成的标识。 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 确认上传

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_fileupload/api_commitupload.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| upload\_id | string | 是 | 一次分片上传的唯一标识，由申请分片上传接口返回。 |
| media\_part\_infos | [object](#Body__media_part_infos) | 是 | 本次分片上传中媒体文件每个分片的信息。 |
| cover\_part\_infos | [object](#Body__cover_part_infos) | 否 | 本次分片上传中封面图片文件每个分片的信息。 |

**Body.media_part_infos Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| part\_number | number | 是 | 分片编号。 |
| etag | string | 是 | 使用上传分片接口上传成功后返回的 etag 的值 |

**Body.cover_part_infos Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| part\_number | number | 否 | 分片编号。 |
| etag | string | 否 | 使用上传分片接口上传成功后返回的 etag 的值 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| media\_id | number | - | 媒体文件id |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 获取媒资列表

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_media/api_listmedia.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| drama\_id | number | 否 | 根据剧目id获取剧集信息 |
| media\_name | string | 否 | 媒资文件名，支持精确匹配、模糊匹配。文件太多时使用该参数进行模糊匹配可能无法得到结果，推荐使用 media\_name\_fuzzy 参数 |
| media\_name\_fuzzy | string | 否 | 媒资文件名，模糊匹配 |
| start\_time | number | 否 | 媒资上传时间>=start\_time |
| end\_time | number | 否 | 媒资上传时间 |
| limit | number | 否 | 分页拉取的最大返回结果数。最大值：100 |
| offset | number | 否 | 分页拉取的起始偏移量 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| media\_info\_list | [objarray](#Res__media_info_list<Array>) | 媒资信息列表 |

**Res.media_info_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| media\_id | number | 媒资文件id |
| create\_time | number | 上传时间，时间戳 |
| expire\_time | number | 过期时间，时间戳 |
| drama\_id | number | 所属剧目id |
| file\_size | string | 媒资文件大小，单位：字节 |
| duration | number | 播放时长，单位：秒 |
| name | string | 媒资文件名 |
| description | string | 描述 |
| cover\_url | string | 封面图临时链接 |
| original\_url | string | 原始视频临时链接 |
| mp4\_url | string | mp4格式临时链接 |
| hls\_url | string | hls格式临时链接 |
| audit\_detail | [object](#Res__media_info_list<Array>__audit_detail) | 审核信息 |

**Res.media_info_list(Array).audit_detail Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| status | number | 0为无效值；1为审核中；2为审核驳回；3为审核通过；4为驳回重填。需要注意可能存在单个剧集的状态为审核通过，但是剧目整体是未通过的情况，而能不能获取播放链接取决于剧目的审核状态 |
| create\_time | number | 提审时间戳 |
| audit\_time | number | 审核时间戳 |
| reason | string | 审核备注，该值可能为空 |
| evidence\_material\_id\_list | array | 审核证据截图id列表，截图id可以用作[获取永久素材](https://developers.weixin.qq.com/doc/service/api/material/permanent/api_getmaterial)接口的参数来获得截图内容 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 获取媒资详细信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_media/api_getmedia.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| media\_id | number | 是 | 媒资文件id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| media\_info | [object](#Res__media_info) | 媒体文件id。 |

**Res.media_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| media\_id | number | 媒资文件id |
| create\_time | number | 上传时间，时间戳 |
| expire\_time | number | 过期时间，时间戳 |
| drama\_id | number | 所属剧目id |
| file\_size | string | 媒资文件大小，单位：字节 |
| duration | number | 播放时长，单位：秒 |
| name | string | 媒资文件名 |
| description | string | 描述 |
| cover\_url | string | 封面图临时链接 |
| original\_url | string | 原始视频临时链接 |
| mp4\_url | string | mp4格式临时链接 |
| hls\_url | string | hls格式临时链接 |
| audit\_detail | [object](#Res__media_info__audit_detail) | 审核信息 |

**Res.media_info.audit_detail Object Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| status | number | 审核状态，需要注意可能存在单个剧集的状态为审核通过，但是剧目整体是未通过的情况，而能不能获取播放链接取决于剧目的审核状态 | [枚举值](#Enum_Res__media_info__audit_detail__status) |
| create\_time | number | 提审时间戳 | - |
| audit\_time | number | 审核时间戳 | - |
| reason | string | 审核备注。该值可能为空 | - |
| evidence\_material\_id\_list | array | 审核证据截图id列表，截图id可以用作[获取永久素材](https://developers.weixin.qq.com/doc/service/api/material/permanent/api_getmaterial)接口的参数来获得截图内容 | - |

**Res.media_info.audit_detail.status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 无效值 |
| 1 | 审核中 |
| 2 | 审核驳回 |
| 3 | 审核通过 |
| 4 | 驳回重填 |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 获取媒资播放链接

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_media/api_getmedialink.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| media\_id | number | 是 | 媒资文件id |
| t | number | 是 | 播放地址的过期时间戳。有效的时间最长不能超过2小时后 |
| us | string | 否 | 链接标识。平台默认会生成一个仅包含小写字母和数字的字符串用于增强链接的唯一性(如us=647488c4792c15185b8fd2a6)。如开发者需要增加自己的标识，比如区分播放的渠道，可使用该参数，该参数最终的值是"开发者标识-平台标识"（如开发者传入abcd，则最终的临时链接中us=abcd-647488c4792c15185b8fd2a6） |
| exper | number | 否 | 试看时长，单位：秒，最大值不能超过视频长度 |
| rlimit | number | 否 | 最多允许多少个不同 IP 的终端播放，以十进制表示，最大值为9，不填表示不做限制。当限制 URL 只能被1个人播放时，建议 rlimit 不要严格限制成1（例如可设置为3），因为移动端断网后重连 IP 可能改变 |
| whref | string | 否 | 允许访问的域名列表，支持1条 - 10条，用半角逗号分隔。域名前不要带协议名（http://和https://），域名为前缀匹配（如填写 abc.com，则 abc.com/123 和 abc.com.cn也会匹配），且支持通配符（如 \*.abc.com） |
| bkref | string | 否 | 禁止访问的域名列表，支持1条 - 10条，用半角逗号分隔。域名前不要带协议名（http://和https://），域名为前缀匹配（如填写 abc.com，则 abc.com/123 和 abc.com.cn也会匹配），且支持通配符（如 \*.abc.com） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| media\_info | [object](#Res__media_info) | 媒体播放信息 |

**Res.media_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| media\_id | number | 媒资文件id |
| duration | number | 播放时长，单位：秒 |
| name | string | 媒资文件名 |
| description | string | 描述 |
| cover\_url | string | 封面图临时链接 |
| mp4\_url | string | mp4格式临时链接 |
| hls\_url | string | hls格式临时链接 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 删除媒资

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_media/api_deletemedia.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| media\_id | number | 是 | 媒资文件id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 剧目提审

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/auditdrama/api_auditdrama.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| drama\_id | number | 是 | 剧目id，首次提审不需要填该参数，重新提审时必填 |
| name | string | 是 | 剧目名称，首次提审时必填，重新提审时根据是否需要修改选填。 |
| media\_count | number | 是 | 剧集数目。首次提审时必填， 重新提审时可不填，如要填写也要和第一次提审时一样。 |
| media\_id\_list | numarray | 是 | 剧集媒资media\_id列表。首次提审时必填，而且元素个数必须与media\_count一致。重新提审时为可选，如果剧集有内容有变化，可以通过新的列表替换未通过的剧集（推荐使用replace\_media\_list进行替换，避免顺序和原列表不一致）。 |
| description | string | 是 | 剧目简介，可填写200个字符。 |
| recommendations | string | 否 | 剧目推荐语，可填写30个字符。 |
| cover\_material\_id | string | 是 | 剧目海报临时material\_id。首次提审时必填，重新提审时根据是否需要修改选填。 |
| promotion\_poster\_material\_id | string | 否 | 推广海报临时material\_id。 |
| producer | string | 是 | 剧目制作方 。首次提审时必填，重新提审时根据是否需要修改选填。 |
| authorized\_material\_id | string | 否 | 不申请版权保护时必填，权利声明/播放授权材料material\_id。 需上传[《权利声明及不侵权承诺函》](https://res.wx.qq.com/op_res/0eyDEkj2p1wShKp0275Tc1DmiSk0Qo9QGOhN_M7BXMb-r9GAjD9Lxjq9WQ5nlLiTd4qdl0uPwJPKdk0WyfyrRQ) 注：(1) 剧目制作方/版权方与账号主体一致时，请上传附件1（需签章）； (2) 剧目制作方/版权方与账号主体不一致时，请上传附件2或完整的播放授权材料（需签章）。 |
| qualification\_type | number | 是 | 剧目资质：1-取得《网络剧片发行许可证》或重点节目备案号；2-未取得《网络剧片发行许可证》或重点节目备案，且制作成本小于100万元 注： 1、 （1）剧目资质=1：需上传“网络剧片发行许可证”或“广电备案系统截图”，平台会在视频播放环节展示备案号水印； （2）剧目资质=2：制作成本在100万以内，需上传《成本配置比例情况报告》。剧目经平台审核后由平台下发备案号（备案号仅适用微信小程序平台）并在视频播放环节展示备案号水印。 2、2024年5月27日前发起提审的剧目可支持修改，且同一剧目仅支持修改一次。 |
| registration\_number | string | 否 | 剧目备案号，当qualification\_type=1时必填。根据提供的剧目资质证明文件填写对应的网络剧片发行许可证编号或剧目备案号。如：(沪)网剧审字(2023)第001号 或 V123456788888888 |
| qualification\_certificate\_material\_id | string | 否 | 剧目资质证明文件，当qualification\_type=1时必填。请提供网络剧片发行许可证或广电备案系统截图。[查看截图示例](https://res.wx.qq.com/op_res/X9CuqeIgGZSRP_sI5elvBrSySOz_zV_lR3msHDuzL6jU8hDlIBJ4O82XD7VPVSGMgQpMenlGak5DBsvKHjcYZw) |
| cost\_commitment\_letter\_material\_id | string | 否 | 《成本配置比例情况报告》material\_id，当qualification\_type=2时必填。2026年1月14日00:00起提审需使用新模板。[点击下载旧模板](https://res.wx.qq.com/op_res/8q_kSHE63wbMvg6E5JJMrkIIGJiOOuH5VBccpsz5XxJsHIZQ15KaWbVFUMJskisNEIYnpY6Z9cnrKBp1Fr4pIQ)，[点击下载新模板](https://res.wx.qq.com/op_res/F0TQYnsCpdzIUXDGgP7rHCoeeWYDxu_mRNt3iA6a9BU_J5JchXBQEs_LO-0pxRV_VTbKcVN8Ulz8oO2R0ZrHDw) |
| cost\_of\_production | number | 否 | 剧目制作成本（单位：万元），当qualification\_type=2时必填。请填写“1-99” 的整数（如非整数将截断取整），数值需与《成本配置比例情况报告》中对应剧目制作成本一致。 |
| expedited | number | 否 | 填1表示审核加急，0或不填为不加急。每天有5次加急机会。该字段在首次提审时才有效，重新提审时会沿用首次提审时的属性，重新提审不会扣次数。最终是否为加急单，可以根据[drama\_info\_list.expedited](api_listdramas)属性(1表示审核加急，0或空为非加急审核)判断 |
| actor\_list | [object](#Body__actor_list) | 否 | 演员信息，需填写2-5位演员。当drama\_type=2时必填，当drama\_type=1和3时无需填写。 |
| other\_material\_material\_id | string | 否 | 其他材料material\_id，如涉及互动短剧，请上传完整剧情走线示意图。 |
| replace\_media\_list | [objarray](#Body__replace_media_list<Array>) | 否 | 用于重新提审时替换审核不通过的剧集。 |
| copyright | [object](#Body__copyright) | 是 | 版权保护相关。 |
| drama\_type | number | 是 | 剧目类型，1-漫剧；2-真人。新增3-数字真人（2026年4月20日11:00起生效） 注： 1.漫剧：指基于漫画、动画或绘图风格制作的剧目，不涉及真人出演。提审流程无需上传对应的演职人员信息。 2.真人：指由真实演员出演、使用实景拍摄或特效辅助制作的剧目。提审流程需上传对应的演职人员信息。 3.数字真人：指基于计算机图形技术与人工智能算法生成的、具有逼真人类外观及行为表现的虚拟角色出演的剧目。提审流程无需上传对应的演职人员信息。 4.漫剧和数字真人均无需填写「actor\_list-演员信息」字段 |
| content\_declared | number | 否 | AI内容声明，1-视频包含AI生成的内容；0或不传-视频不包含AI生成的内容 |

**Body.actor_list Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| actor | [objarray](#Body__actor_list__actor<Array>) | 是 | 演员列表 |

**Body.replace_media_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| old | number | 否 | 旧的剧集media\_id |
| new | number | 否 | 新的剧集media\_id |

**Body.copyright Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| copyright\_role | number | 是 | 提审主体身份，1. 剧目制作方; 2. 授权播出方或版权方。 |
| apply\_for\_copyright\_protection | number | 是 | 是否申请版权保护，0. 不申请; 1. 申请。不申请时必须上传权利声明/播放授权材料。 |
| copyright\_verification | string | 否 | 版权验证方式：1. 基于版权证明材料; 2. 基于版权授权关系。 （2024年12月30日00:00起，apply\_for\_copyright\_protection=1时必填。） |
| proof\_of\_production | array | 否 | 剧目制作证明材料临时 material\_id，最多支持上传 4 个。（apply\_for\_copyright\_protection=1时必填。 2024年12月30日00:00起，apply\_for\_copyright\_protection=1且copyright\_verification=2时无需填写。 ） 注： 剧目类型=真人，需提供以下任一材料： 1. 剧目制作合同； 2. 作品登记证书； 3. 两份或以上主创人员的聘用合同（如：导演合同+主演合同）。 剧目类型=漫剧/数字真人，支持上述材料，或以下任一材料： 1. 剧本采买合同； 2. 后期制作工程文件，如：剪辑、特效图层工程等； 3. 可信时间戳认证证书。 |
| purchase\_or\_broadcast\_authorization\_certificate | array | 否 | 版权采买/播出授权证明材料临时 material\_id，最多支持上传 4 个。 提审身份非剧目制作方时请上传： 1. 版权采买证明材料 (提审身份为版权方/授权播出方时需提供)； 2. 播出授权材料 (提审身份为授权播出方时需提供) （apply\_for\_copyright\_protection=1时选填。） |

**Body.actor_list.actor(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 演员姓名，格式要求：可填写30个字符，支持输入中文、英文和· |
| photo\_material\_id | string | 是 | 演员照片临时material\_id |
| role | string | 是 | 饰演角色，格式要求：可填写30个字符，支持输入中文、英文及，。；”“？、—《》！（）-· |
| profile | string | 是 | 演员简介，填写内容可参考：生日、星座、籍贯、身高、毕业院校、历史/代表作品、获奖信息、成就等(以上要素需至少满足3项或涵盖任一要素且不少于20字）。 格式要求：可填写100个字符，支持输入中文、英文、阿拉伯数字及，。：；“”？、—《》！（）-· |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| drama\_id | number | 剧目id。 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 获取剧目列表

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/auditdrama/api_listdramas.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| limit | number | 否 | 分页拉取的最大返回结果数。最大值：100。 |
| offset | number | 否 | 分页拉取的起始偏移量。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| drama\_info\_list | [objarray](#Res__drama_info_list<Array>) | 媒体文件id |

**Res.drama_info_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| drama\_id | number | 剧目id。 |
| create\_time | number | 创建时间，时间戳。 |
| name | string | 剧名。 |
| cover\_url | string | 剧目海报链接，根据提审时提交的cover\_material\_id转存得到。 |
| media\_count | number | 剧集数目。 |
| producer | string | 制作方 。 |
| playwright | string | 编剧。 |
| description | string | 剧目简介。 |
| production\_license | string | 广播电视节目制作经营许可证。 |
| audit\_detail | [object](#Res__drama_info_list<Array>__audit_detail) | 审核状态。 |
| media\_list | [objarray](#Res__drama_info_list<Array>__media_list<Array>) | 剧集信息列表。 |
| expedited | number | 1表示审核加急，0或空为非加急审核 |
| recommendations | string | 剧目推荐语。 |
| promotion\_poster | string | 推广海报。 |
| actor\_list | [object](#Res__drama_info_list<Array>__actor_list) | 演员信息。 |
| status | number | 剧目状态。0为正常可播；1为审核中；2为审核失败；3为平台下架 |

**Res.drama_info_list(Array).audit_detail Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| status | number | 0为无效值；1为审核中；2为最终失败；3为审核通过；4为驳回重填 |
| audit\_type | number | 事件通知接口才返回：0为首次提审；1为再次提审；2为替换剧集提审；3为修改剧目基本信息审核。 |
| create\_time | number | 提审时间戳。 |
| audit\_time | number | 审核时间戳。 |

**Res.drama_info_list(Array).media_listObject Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| media\_id | number | 媒资文件id。 |

**Res.drama_info_list(Array).actor_list Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| actor | [objarray](#Res__drama_info_list<Array>__actor_list__actor<Array>) | 演员列表 |

**Res.drama_info_list(Array).actor_list.actorObject Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| name | string | 演员姓名，格式要求：可填写30个字符，支持输入中文、英文和· |
| photo\_material\_id | string | 演员照片临时material\_id |
| role | string | 饰演角色，格式要求：可填写30个字符，支持输入中文、英文及，。；”“？、—《》！（）-· |
| profile | string | 演员简介，填写内容可参考：生日、星座、籍贯、身高、毕业院校、历史/代表作品、获奖信息、成就等(以上要素需至少满足3项或涵盖任一要素且不少于20字）。 格式要求：可填写100个字符，支持输入中文、英文、阿拉伯数字及，。：；“”？、—《》！（）-· |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 获取剧目信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/auditdrama/api_getdrama.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| drama\_id | number | 是 | 剧目id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| drama\_info | [object](#Res__drama_info) | 剧目信息 |

**Res.drama_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| drama\_id | number | 剧目id。 |
| create\_time | number | 创建时间，时间戳。 |
| name | string | 剧名。 |
| cover\_url | string | 剧目海报链接，根据提审时提交的cover\_material\_id转存得到。 |
| media\_count | number | 剧集数目。 |
| producer | string | 制作方 。 |
| playwright | string | 编剧。 |
| description | string | 剧目简介。 |
| production\_license | string | 广播电视节目制作经营许可证。 |
| audit\_detail | [object](#Res__drama_info__audit_detail) | 审核状态。 |
| media\_list | [objarray](#Res__drama_info__media_list<Array>) | 剧集信息列表。 |
| expedited | number | 1表示审核加急，0或空为非加急审核 |
| recommendations | string | 剧目推荐语。 |
| promotion\_poster | string | 推广海报。 |
| actor\_list | [object](#Res__drama_info__actor_list) | 演员信息。 |
| status | number | 剧目状态。0为正常可播；1为审核中；2为审核失败；3为平台下架 |

**Res.drama_info.audit_detail Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| status | number | 0为无效值；1为审核中；2为最终失败；3为审核通过；4为驳回重填 |
| audit\_type | number | 事件通知接口才返回：0为首次提审；1为再次提审；2为替换剧集提审；3为修改剧目基本信息审核。 |
| create\_time | number | 提审时间戳。 |
| audit\_time | number | 审核时间戳。 |

**Res.drama_info.media_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| media\_id | number | 媒资文件id。 |

**Res.drama_info.actor_list Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| actor | [objarray](#Res__drama_info__actor_list__actor<Array>) | 演员列表 |

**Res.drama_info.actor_list.actor(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| name | string | 演员姓名，格式要求：可填写30个字符，支持输入中文、英文和· |
| photo\_material\_id | string | 演员照片临时material\_id |
| role | string | 饰演角色，格式要求：可填写30个字符，支持输入中文、英文及，。；”“？、—《》！（）-· |
| profile | string | 演员简介，填写内容可参考：生日、星座、籍贯、身高、毕业院校、历史/代表作品、获奖信息、成就等(以上要素需至少满足3项或涵盖任一要素且不少于20字）。 格式要求：可填写100个字符，支持输入中文、英文、阿拉伯数字及，。：；“”？、—《》！（）-· |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 提交替换剧集审核

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/auditdrama/api_submitreplacemedias.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| drama\_id | number | 是 | 剧目id |
| replace\_media\_list | [objarray](#Body__replace_media_list<Array>) | 是 | 替换的剧集信息。 |

**Body.replace_media_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| old | number | 否 | 旧的剧集media\_id |
| new | number | 否 | 新的剧集media\_id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 替换审核通过的剧集

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/auditdrama/api_replacedramamedia.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| drama\_id | number | 是 | 剧目id |
| old\_media\_id | number | 是 | 旧剧集meida\_id |
| new\_media\_id | number | 是 | 新剧集meida\_id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 修改剧目基本信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/auditdrama/api_submitmodifydramabasicinforeq.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| drama\_id | number | 是 | 剧目id |
| description | string | 否 | 剧目简介，支持填写200个字符。 |
| cover\_material\_id | string | 否 | 剧目海报临时material\_id。 |
| recommendations | string | 否 | 剧目推荐语。 |
| promotion\_poster\_material\_id | string | 否 | 推广海报临时material\_id。 |
| alternate\_name | string | 否 | 备用剧名。 |
| actor\_list | [object](#Body__actor_list) | 否 | 演员信息。如果需要修改，请填写所有的演员信息。 |
| qualification\_type | number | 否 | 剧目资质：1-取得《网络剧片发行许可证》或重点节目备案号；2-未取得《网络剧片发行许可证》或重点节目备案，且制作成本小于30万元 注： 1、 （1）剧目资质=1：需上传“网络剧片发行许可证”或“广电备案系统截图”，平台会在视频播放环节展示备案号水印； （2）剧目资质=2：制作成本在100万以内，需上传《成本配置比例情况报告》。剧目经平台审核后由平台下发备案号（备案号仅适用微信小程序平台）并在视频播放环节展示备案号水印。 2、2024年5月27日前发起提审的剧目可支持修改，且同一剧目仅支持修改一次。 |
| registration\_number | string | 否 | 剧目备案号，当qualification\_type=1时必填。根据提供的剧目资质证明文件填写对应的网络剧片发行许可证编号或剧目备案号。如：(沪)网剧审字(2023)第001号 或 V123456788888888 |
| qualification\_certificate\_material\_id | string | 否 | 剧目资质证明文件，当qualification\_type=1时必填。请提供网络剧片发行许可证或广电备案系统截图。[查看截图示例](https://res.wx.qq.com/op_res/X9CuqeIgGZSRP_sI5elvBrSySOz_zV_lR3msHDuzL6jU8hDlIBJ4O82XD7VPVSGMgQpMenlGak5DBsvKHjcYZw) |
| cost\_of\_production | number | 否 | 剧目制作成本（单位：万元），当qualification\_type=2时必填。请填写“1-99” 的整数（如非整数将截断取整），数值需与《成本配置比例情况报告》中对应剧目制作成本一致。 |
| cost\_commitment\_letter\_material\_id | string | 否 | 《成本配置比例情况报告》material\_id，当qualification\_type=2时必填。2026年1月14日00:00起提审需使用新模板。[点击下载旧模板](https://res.wx.qq.com/op_res/8q_kSHE63wbMvg6E5JJMrkIIGJiOOuH5VBccpsz5XxJsHIZQ15KaWbVFUMJskisNEIYnpY6Z9cnrKBp1Fr4pIQ)，[点击下载新模板](https://res.wx.qq.com/op_res/F0TQYnsCpdzIUXDGgP7rHCoeeWYDxu_mRNt3iA6a9BU_J5JchXBQEs_LO-0pxRV_VTbKcVN8Ulz8oO2R0ZrHDw) |
| other\_material\_material\_id | string | 否 | 其他材料material\_id，如涉及互动短剧，请上传完整剧情走线示意图。 |
| producer | string | 否 | 剧目制作方。apply\_for\_copyright\_protection =1时必填，否则无需填写。 |
| copyright | [object](#Body__copyright) | 否 | 版权保护相关。apply\_for\_copyright\_protection =1时必填，否则无需填写 。 |

**Body.actor_list Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| actor | [objarray](#Body__actor_list__actor<Array>) | 是 | 演员列表 |

**Body.copyright Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| copyright\_role | number | 是 | 提审主体身份，1. 剧目制作方; 2. 授权播出方或版权方。 number 必填 number 选填。 2024年12月30日00:00起，apply\_for\_copyright\_protection=1时必填。 |
| apply\_for\_copyright\_protection | number | 是 | 是否申请版权保护，0. 不申请; 1. 申请。不申请时必须上传权利声明/播放授权材料。 |
| copyright\_verification | string | 否 | 版权验证方式：1. 基于版权证明材料; 2. 基于版权授权关系。 （2024年12月30日00:00起，apply\_for\_copyright\_protection=1时必填。） |
| proof\_of\_production | array | 否 | 剧目制作证明材料临时 material\_id，最多支持上传 4 个。（apply\_for\_copyright\_protection=1时必填。 2024年12月30日00:00起，apply\_for\_copyright\_protection=1且copyright\_verification=2时无需填写。 ） |
| purchase\_or\_broadcast\_authorization\_certificate | array | 否 | 版权采买/播出授权证明材料临时 material\_id，最多支持上传 4 个。 提审身份非剧目制作方时请上传： 1. 版权采买证明材料 (提审身份为版权方/授权播出方时需提供)； 2. 播出授权材料 (提审身份为授权播出方时需提供) （apply\_for\_copyright\_protection=1时选填。） |

**Body.actor_list.actor(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 演员姓名，格式要求：可填写30个字符，支持输入中文、英文和· |
| photo\_material\_id | string | 是 | 演员照片临时material\_id |
| role | string | 是 | 饰演角色，格式要求：可填写30个字符，支持输入中文、英文及，。；”“？、—《》！（）-· |
| profile | string | 是 | 演员简介，填写内容可参考：生日、星座、籍贯、身高、毕业院校、历史/代表作品、获奖信息、成就等(以上要素需至少满足3项或涵盖任一要素且不少于20字）。 格式要求：可填写100个字符，支持输入中文、英文、阿拉伯数字及，。：；“”？、—《》！（）-· |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 查询剧目审核信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/auditdrama/api_getdramalatestauditinfo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| drama\_id | number | 是 | 剧目id |
| audit\_type | number | 是 | 审核类型。0为首次提审；1为再次提审；2为替换剧集提审；3为修改剧目基本信息审核。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| audit\_detail | [object](#Res__audit_detail) | - | 审核信息，区别于[getdrama接口](api_getdrama)的audit\_detail，getdrama接口的audit\_type仅表示audit\_type=0或1的审核信息。 |

**Res.audit_detail Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| status | number | 0为无效值；1为审核中；2为最终失败；3为审核通过；4为驳回重填 |
| audit\_type | number | 事件通知接口才返回：0为首次提审；1为再次提审；2为替换剧集提审；3为修改剧目基本信息审核。 |
| create\_time | number | 提审时间戳。 |
| audit\_time | number | 审核时间戳。 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 查询CDN用量数据

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/usagedata/api_getcdnusagedata.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start\_time | number | 是 | 起始时间戳。 |
| end\_time | number | 是 | 截止时间戳。 |
| data\_interval | string | 是 | 用量数据的时间粒度，单位：分钟，取值有：5：5 分钟粒度，返回指定查询时间内5分钟粒度的明细数据。60：小时粒度，返回指定查询时间内1小时粒度的数据。1440：天粒度，返回指定查询时间内1天粒度的数据。默认值为1440，返回天粒度的数据。 |
| query\_type | number | 否 | 查询类型，0：通用播放流量和短剧播放器定向流量；1：短剧播放器定向流量；2：通用播放流量。默认值为0。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| data\_interval | number | - | 时间粒度，单位：分钟。 |
| item\_list | [objarray](#Res__item_list<Array>) | - | CDN 统计数据。 |

**Res.item_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| time | number | 数据所在时间区间的开始时间戳。 |
| value | number | 数据大小，单位：字节。 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 查询CDN日志下载链接列表

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/usagedata/api_getcdnlogs.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start\_time | number | 是 | 起始时间戳。 |
| end\_time | number | 是 | 结束时间戳，必须大于起始时间，起始到结束时间的跨度不要超过48小时（end\_time-start\_time<=48h） |
| ‌~~limit~~ | number | 否 | 2024年3月29日起废弃。‌~~分页拉取的最大返回结果数。默认值：100；最大值：1000~~ |
| ‌~~offset~~ | number | 否 | 2024年3月29日起废弃。‌~~分页拉取的起始偏移量。默认值：0~~ |
| query\_type | number | 否 | 查询类型，0：通用播放流量和短剧播放器定向流量；1：短剧播放器定向流量；2：通用播放流量。默认值为0。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| total\_count | number | - | 日志下载链接总数量。 |
| domestic\_cdn\_logs | [object](#Res__domestic_cdn_logs) | - | 国内CDN节点的日志下载列表。 |

**Res.domestic_cdn_logs Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| date | number | 日志所属日期。 |
| name | number | 日志名称。 |
| url | number | 日志下载链接，24小时内下载有效。 |
| start\_time | number | 日志起始时间。 |
| end\_time | number | 日志结束时间 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 查询流量包详情

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/usagedata/api_listpackages.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| status | number | 是 | 按流量包状态过滤，取值有：0-不过滤，1-有效的，2-无效的，3-过期的 |
| offset | number | 是 | 偏移值，分页请求用 |
| limit | number | 是 | 分页大小，最大值为100 |
| query\_type | number | 否 | 查询类型，0：通用流量；1：定向流量。默认值为0 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| total\_count | number | - | 当前查询条件下的流量包总数 |
| package\_list | [objarray](#Res__package_list<Array>) | - | 流量包详情列表 |

**Res.package_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| start\_time | number | 有效期起始时间 |
| end\_time | number | 有效期截止时间 |
| used | number | 流量包已消耗流量的数值（MB） |
| all | number | 流量包总额（MB），剩余流量=流量包总额-已消耗流量 |
| order\_id | string | 订单号 |
| status | number | 流量包状态，参考请求参数status中的说明 |
| is\_deleted | number | 是否已删除（失效），例如已退款 |
| package\_id | string | 流量包编号 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 查询被授权信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/authorizedrama/api_getauthorizedobjects.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authorizer\_appid | string | 否 | 授权方小程序id。不填表示查询所有授权方。 |
| offset | number | 否 | 偏移值，分页请求用。默认0。 |
| limit | number | 否 | 分页大小，默认100，最大值为1000。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| total\_count | number | - | 当前查询条件下的记录总数 |
| objects | [objarray](#Res__objects<Array>) | - | 被授权信息 |

**Res.objects(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| drama\_id | number | 授权的剧目ID |
| authorizer\_appid | string | 授权方小程序id |
| authorized\_time | number | 授权时间戳 |
| authz\_expire\_time | number | 授权到期时间戳。0表示长期有效。 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 增加剧目授权

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/authorizedrama/api_authorizedrama.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| drama\_id | numarray | 是 | 授权的剧目ID |
| authorized | string | 是 | 被授权方小程序id。 |
| authz\_expire\_time | number | 否 | 不传或者传0，表示永久有效；否则表示授权到期的时间戳 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| result | [objarray](#Res__result<Array>) | - | 剧目的授权结果。 |

**Res.result(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| drama\_id | number | 剧目ID。 |
| errcode | number | 错误码。 |
| errmsg | string | 错误原因。 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 解除剧目授权

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/authorizedrama/api_deauthorizedrama.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| drama\_id | numarray | 是 | 解除授权剧目ID。 |
| authorized\_appid | string | 是 | 被授权方小程序id。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| result | [objarray](#Res__result<Array>) | - | 剧目的解除授权结果。 |

**Res.result(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| drama\_id | number | 授权剧目 id |
| errcode | number | 该剧目授权时的错误码 |
| errmsg | number | 该剧目授权时的错误原因 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 查询授权信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/authorizedrama/api_getauthorizeobjects.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| drama\_id | number | 否 | 查询的剧目ID。不填表示查询所有剧目。 |
| authorized\_appid | string | 否 | 查询的被授权方小程序id。不填表示查询所有被授权方。 |
| offset | number | 否 | 偏移值，分页请求用。默认0。 |
| limit | number | 否 | 分页大小，默认100，最大值为1000。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| total\_count | number | - | 当前查询条件下的记录总数 |
| objects | [objarray](#Res__objects<Array>) | - | 授权信息 |

**Res.objects(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| drama\_id | number | 授权的剧目ID |
| authorized\_appid | string | 被授权方小程序id |
| authorized\_time | number | 授权时间戳 |
| authz\_expire\_time | number | 授权到期时间戳。0表示长期有效。 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 增加账号授权

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/authorizeapp/api_authorizeapp.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authorized\_appid | string | 是 | 被授权方小程序id。 |
| authz\_expire\_time | number | 否 | 不传或者传0，表示永久有效；否则表示授权到期的时间戳。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 解除账号授权

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/authorizeapp/api_deauthorizeapp.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authorized\_appid | string | 是 | 被授权方小程序id。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 查询账号授权信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/authorizeapp/api_getauthorizeapps.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| objects | [objarray](#Res__objects<Array>) | - | 授权信息 |

**Res.objects(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| authorized\_appid | string | 被授权方小程序id |
| authorized\_time | number | 授权时间戳 |
| authz\_expire\_time | number | 授权到期时间戳。0表示长期有效。 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 查询被授权信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/authorizeapp/api_getauthorizedobjects.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authorizer\_appid | string | 否 | 授权方小程序id。不填表示查询所有授权方。 |
| offset | number | 否 | 偏移值，分页请求用。默认0。 |
| limit | number | 否 | 分页大小，默认100，最大值为1000。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| total\_count | number | - | 当前查询条件下的记录总数 |
| objects | [objarray](#Res__objects<Array>) | - | 被授权信息 |

**Res.objects(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| drama\_id | number | 授权的剧目ID |
| authorizer\_appid | string | 授权方小程序id |
| authorized\_time | number | 授权时间戳 |
| authz\_expire\_time | number | 授权到期时间戳。0表示长期有效。 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 增加版权授权

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/authorizecopyright/api_authorizecopyright.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authorization\_type | number | 是 | 授权类型：1. 授权给主体；2. 授权给小程序； |
| authorized\_appid | string | 否 | 被授权方小程序id，`authorization\_type` 为 2 时必填。 |
| authorized\_subject\_cert\_no | string | 否 | 被授权方主体证件号，必须为统一社会信用代码，`authorization\_type` 为 1 时必填。 |
| drama\_ids | numarray | 否 | 要授权的受版权保护的剧目 id，最多 100 个。 |
| expire\_time | number | 否 | 不传或者传 0，表示永久有效；否则表示授权到期的时间戳。如果指定授权到期时间，授权时长不能小于 7 天（从当前时间算起）。默认值为 0。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| result | [objarray](#Res__result<Array>) | - | 授权的结果 |

**Res.result(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| drama\_id | number | 授权剧目 id |
| errcode | number | 该剧目授权时的错误码 |
| errmsg | string | 该剧目授权时的错误原因 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 解除版权授权

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/authorizecopyright/api_deauthorizecopyright.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authorization\_type | number | 是 | 被授权方授权类型：1. 主体；2. 小程序； |
| authorized\_appid | string | 否 | 被授权方小程序id，`authorization\_type` 为 2 时必填。 |
| authorized\_subject\_cert\_no | string | 否 | 被授权方主体证件号，必须为统一社会信用代码，`authorization\_type` 为 1 时必填。 |
| drama\_ids | numarray | 否 | 要解除授权的受版权保护的剧目 id，最多 100 个 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| result | [objarray](#Res__result<Array>) | - | 解除授权的结果 |

**Res.result(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| drama\_id | number | 授权剧目 id |
| errcode | number | 该剧目授权时的错误码 |
| errmsg | string | 该剧目授权时的错误原因 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 查询版权授权信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/authorizecopyright/api_getcopyrightauthorizationlist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authorization\_type | number | 否 | 授权类型：1. 授权给主体；2. 授权给小程序。不填默认值为 0，表示查询全部。 |
| authorized\_appid | string | 否 | 被授权方小程序id，authorization\_type 为 2 时必填。 |
| authorized\_subject\_cert\_no | string | 否 | 被授权方主体证件号，必须为统一社会信用代码，authorization\_type 为 1 时必填。 |
| drama\_id | number | 否 | 授权剧目 id。不填默认值为 0，表示查询全部。 |
| offset | number | 否 | 偏移值，分页请求用。默认 0。 |
| limit | number | 否 | 分页大小，默认 100，最大值为 1000。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| list | [objarray](#Res__list<Array>) | - | 授权信息 |
| total\_count | number | - | 总数 |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| authorizer\_appid | string | 授权方小程序 id |
| authorization\_type | number | 授权类型 |
| authorized\_appid | string | 被授权方小程序 id |
| authorized\_subject\_cert\_no | string | 被授权方主体证件号 |
| drama\_id | number | 授权剧目 id |
| authorized\_time | number | 授权时间戳 |
| expire\_time | number | 授权到期时间戳，0 表示长期有效 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

### 查询被版权授权信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/authorizecopyright/api_getcopyrightauthorizedlist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authorizer\_appid | string | 否 | 授权方小程序id，不填表示查全部。 |
| offset | number | 否 | 偏移值，分页请求用。默认 0。 |
| limit | number | 否 | 分页大小，默认 100，最大值为 1000。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| list | [objarray](#Res__list<Array>) | - | 被授权信息 |
| total\_count | number | - | 总数 |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| authorizer\_appid | string | 授权方小程序 id |
| authorization\_type | number | 授权类型 |
| authorized\_appid | string | 被授权方小程序 id |
| authorized\_subject\_cert\_no | string | 被授权方主体证件号 |
| drama\_id | number | 授权剧目 id |
| authorized\_time | number | 授权时间戳 |
| expire\_time | number | 授权到期时间戳，0 表示长期有效 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -2 | 初始化未完成，请稍后再试 |
| -1 | 系统错误 |
| 43002 | HTTP请求必须使用POST方法 |
| 44002 | POST内容为空 |
| 47001 | 输入格式错误 |
| 47003 | 参数不符合要求 |
| 10090001 | 视频类型不支持 |
| 10090002 | 图片类型不支持 |
| 10090003 | 图片URL无效 |
| 10090005 | resource\_type无效 |
| 10090038 | 被授权账号没有【文娱-微短剧】类目 |
| 10090039 | 已经被解除授权 |
| 10090040 | 剧集已经被占用 |
| 10090041 | 剧目名称不符合规范 |
| 10090042 | 剧集名称不符合规范 |
| 10090043 | 不存在授权关系 |
| 10093011 | 操作失败 |
| 10093014 | 参数错误（包括参数格式、类型等错误） |
| 10093023 | 操作过于频繁 |
| 10093030 | 资源不存在 |

---

<!-- pages: 32 -->
