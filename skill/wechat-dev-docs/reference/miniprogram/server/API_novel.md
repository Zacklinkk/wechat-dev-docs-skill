# 小程序服务端 API 结构化参考 — API/novel

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 创建作品

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_createbook.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 是 | 作品名，示例值："斗破苍穹"。长度限制1-30字。 |
| intro | string | 是 | 作品简介。长度限制1-500字。 |
| cover\_media\_id | string | 是 | 封面图 media\_id，通过[新增临时素材接口](../../kf-mgnt/kf-message/api_uploadtempmedia)上传得到 |
| author | string | 是 | 作者名。长度限制1-100字。 |
| first\_category\_id | number | 是 | 一级类型id。可选类型见[小说作品类型](https://docs.qq.com/sheet/DVUtkTkhRSEN1aEhC?tab=BB08J2) |
| second\_category\_id | number | 是 | 二级类型id |
| third\_category\_id | number | 是 | 三级类型id |
| complete\_status | number | 是 | 完结状态，1：连载中，2：已完结 |
| original\_id | string | 否 | 提供方作品主键，可用于去重。长度限制0-255字节。 |
| chapter\_order\_method | number | 否 | 章节排序方式，0：追加，1：seq 递增。默认值：0。 |
| custom\_info | string | 否 | 自定义信息。长度限制0-128字节。 |
| keyword\_list | array | 否 | 题材关键词。最多传入3个关键词，每个关键词长度限制1-4字。 |
| awesome\_paragraph | string | 否 | 精彩片段。需为本书内容，长度限制400-1000字。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| book\_id | string | 作品id。非定长，不超过 64 字节。 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

### 编辑作品

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_updatebook.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| book\_id | string | 是 | 作品id |
| title | string | 否 | 作品名。长度限制1-30字。 |
| intro | string | 否 | 作品简介。长度限制1-500字。 |
| cover\_media\_id | string | 否 | 封面图 media\_id，通过 新增临时素材上传得到。 |
| author | string | 否 | 作者名。长度限制1-100字。 |
| first\_category\_id | number | 否 | 一级类型id。可选类型见 小说作品类型 |
| second\_category\_id | number | 否 | 二级类型id |
| third\_category\_id | number | 否 | 三级类型id |
| complete\_status | number | 否 | 完结状态，1：连载中，2：已完结 |
| chapter\_id\_list | array | 否 | 按照预期顺序传入章节id |
| need\_volume | boolean | 否 | 是否需要分卷 |
| volume\_list | [objarray](#Body__volume_list<Array>) | 否 | 分卷信息 |
| chapter\_order\_method | number | 否 | 章节排序方式，0：追加，1：seq 递增 |
| custom\_info | string | 否 | 自定义信息。长度限制0-128字节。 |
| update\_keyword | boolean | 否 | 是否更新题材关键词 |
| keyword\_list | array | 否 | 题材关键词。最多传入3个关键词，每个关键词长度限制1-4字。 |
| awesome\_paragraph | string | 否 | 精彩片段。需为本书内容，长度限制400-1000字。 |

**Body.volume_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volume\_title | string | 是 | 分卷名。长度限制1-100字。 |
| start\_index | number | 是 | 分卷起始章节下标，取值范围 [0, 章节总数) |
| end\_index | number | 是 | 分卷截止章节下标，取值范围 [起始章节下标, 章节总数) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

### 删除作品

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_deletebook.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| book\_id | string | 是 | 作品id |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number |  | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

### 获取作品列表

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_listbook.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| limit | number | 否 | 分页拉取的最大返回结果数。取值范围 1-100，默认值：100 |
| offset | number | 否 | 分页拉取的起始偏移量，默认值：0。offset 和 last\_id 二选一，优先使用 last\_id。 |
| last\_id | number | 否 | 分页 id。首次调用填 0，后续调用填上次返回参数里的 last\_id。offset 和 last\_id 二选一，优先使用 last\_id。 |
| need\_edited\_data | boolean | 否 | true：编辑版信息，false：发布版信息。默认值：false |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number |  | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| book\_list | [objarray](#Res__book_list<Array>) | - | 作品信息列表 |
| total\_cnt | number | - | 作品总数 |
| last\_id | number | - | 分页 id。仅当请求参数有设置 last\_id 且作品信息列表不为空时才有该字段 |

**Res.book_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| book\_id | string | 作品id |
| title | number | 作品名 |
| intro | string | 作品简介 |
| cover\_url | string | 封面图url |
| author | string | 作者名 |
| first\_category\_id | number | 一级类型id |
| second\_category\_id | number | 二级类型id |
| third\_category\_id | number | 三级类型id |
| complete\_status | number | 完结状态，1：连载中，2：已完结 |
| upload\_scene | number | 上传场景，1：本地上传，2：API上传 |
| chapter\_cnt | number | 章节数量 |
| volume\_cnt | number | 分卷数量 |
| total\_word\_cnt | number | 作品总字数 |
| audit\_info | [object](#Res__book_list<Array>__audit_info) | 审核信息。未发起审核不返回该字段。 |
| create\_time | number | 创建时间戳 |
| original\_id | string | 提供方作品主键 |
| chapter\_order\_method | number | 章节排序方式，0：追加，1：seq 递增 |
| custom\_info | string | 自定义信息 |
| ban\_status | number | 管控状态，0：正常，1：下架 |

**Res.book_list(Array).audit_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| audit\_status | number | 0：未提审，1：审核中，2：审核不通过，3：审核通过 |
| create\_time | number | 提审时间戳 |
| audit\_time | number | 审核时间戳 |
| reason | string | 审核原因 |
| suggestion | string | 修改建议。审核不通过时才会有该字段 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

### 获取作品信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_getbook.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| book\_id | string | 否 | 作品id，与提供方作品主键二选一，优先使用该字段 |
| need\_edited\_data | boolean | 否 | true：编辑版信息，false：发布版信息。默认值：false |
| original\_id | string | 否 | 提供方作品主键，与作品id二选一 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| book | [objarray](#Res__book<Array>) | - | 作品信息 |

**Res.book(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| book\_id | string | 作品id |
| title | string | 作品名 |
| intro | string | 作品简介 |
| cover\_url | string | 封面图url |
| author | string | 作者名 |
| first\_category\_id | number | 一级类型id |
| first\_category\_name | string | 一级类型名 |
| second\_category\_id | number | 二级类型id |
| second\_category\_name | string | 二级类型名 |
| third\_category\_id | number | 三级类型id |
| third\_category\_name | string | 三级类型名 |
| complete\_status | number | 完结状态，1：连载中，2：已完结 |
| upload\_scene | number | 上传场景，1：本地上传，2：API上传 |
| chapter\_cnt | number | 章节数 |
| volume\_cnt | number | 分卷数 |
| volume\_list | [objarray](#Res__book<Array>__volume_list<Array>) | 分卷信息 |
| total\_word\_cnt | number | 作品总字数 |
| audit\_info | [object](#Res__book<Array>__audit_info) | 审核信息。未发起审核不返回该字段。 |
| create\_time | number | 创建时间戳 |
| original\_id | string | 提供方作品主键 |
| chapter\_order\_method | number | 章节排序方式，0：追加，1：seq 递增 |
| custom\_info | string | 自定义信息 |
| ban\_status | number | 管控状态，0：正常，1：下架 |

**Res.book(Array).volume_listObject Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| volume\_title | string | 分卷名 |
| start\_index | number | 分卷起始章节下标 |
| end\_index | number | 分卷截止章节下标 |

**Res.book(Array).audit_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| audit\_status | number | 0：未提审，1：审核中，2：审核不通过，3：审核通过 |
| create\_time | number | 提审时间戳 |
| audit\_time | number | 审核时间戳 |
| reason | string | 审核原因 |
| suggestion | string | 修改建议。审核不通过时才会有该字段 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

### 上传章节

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_createchapter.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| book\_id | string | 是 | 作品id |
| chapter | [object](#Body__chapter) | 是 | 章节信息 |

**Body.chapter Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| chapter\_title | string | 是 | 章节标题。长度限制 1-80 字。 |
| content | string | 是 | 章节内容。长度限制 1-20000 字。 |
| original\_id | string | 否 | 提供方章节主键，可用于去重。长度限制 0-255 字节。 |
| seq | number | 否 | 章节相对顺序，可非连续递增，默认值：0。详见注意事项。 |
| custom\_info | string | 否 | 自定义信息。长度限制 0-128 字节 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| chapter\_id | string | - | 章节id。非定长，不超过 64 字节。 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

### 批量上传章节

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_batchcreatechapter.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| book\_id | string | 是 | 作品id |
| chapter\_list | [objarray](#Body__chapter_list<Array>) | 是 | 章节信息，单次最多上传 10 章。 |

**Body.chapter_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| chapter\_title | string | 是 | 章节标题。长度限制 1-80 字。 |
| content | string | 是 | 章节内容。长度限制 1-20000 字。 |
| original\_id | string | 否 | 提供方章节主键，可用于去重。长度限制 0-255 字节。 |
| seq | number | 否 | 章节相对顺序，可非连续递增，默认值：0。详见注意事项。 |
| custom\_info | string | 否 | 自定义信息。长度限制 0-128 字节 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| chapter\_id | array | - | 章节id。非定长，不超过 64 字节。 |
| conflict\_original\_id\_list | array | - | 冲突的章节主键列表 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

### 删除章节

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_deletechapter.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| book\_id | string | 是 | 作品id |
| chapter\_id | string | 是 | 章节id |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

### 替换章节

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_replacechapter.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| book\_id | string | 是 | 作品id |
| chapter\_id | string | 是 | 章节id |
| new\_chapter\_title | string | 是 | 新章节标题。长度限制 1-80 字。 |
| new\_content | string | 是 | 新章节内容。长度限制 1-20000 字。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| new\_chapter\_id | string | - | 替换后新章节id |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

### 获取章节列表

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_listchapter.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| book\_id | string | 是 | 作品id |
| need\_edited\_data | boolean | 否 | true：编辑版信息，false：发布版信息。默认值：false |
| limit | number | 否 | 分页拉取的最大返回结果数。默认值：10；最大值：100 |
| offset | number | 否 | 分页拉取的起始偏移量，默认值：0 |
| volume\_index | number | 否 | 分卷下标，若设置则只返回指定卷的章节列表 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| chapter\_list | [objarray](#Res__chapter_list<Array>) | - | 章节信息列表 |
| total\_cnt | number | - | 章节总数 |

**Res.chapter_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| chapter\_id | string | 章节id |
| chapter\_title | string | 章节标题 |
| word\_cnt | number | 字数 |
| create\_time | number | 创建时间戳 |
| audit\_info | [object](#Res__chapter_list<Array>__audit_info) | 审核信息 |
| volume\_index | number | 所属分卷下标，-1 表示不属于任何分卷 |
| original\_id | string | 提供方章节主键 |
| seq | number | 章节相对顺序 |
| custom\_info | string | 自定义信息 |
| ban\_status | number | 管控状态，0：正常，1：下架 |

**Res.chapter_list(Array).audit_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| audit\_status | number | 0：未提审，1：审核中，2：审核不通过，3：审核通过 |
| create\_time | number | 提审时间戳 |
| audit\_time | number | 审核时间戳 |
| reason | string | 审核原因 |
| suggestion | string | 修改建议。审核不通过时才会有该字段 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

### 获取章节信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_getchapter.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| book\_id | string | 否 | 作品id |
| chapter\_id | string | 否 | 章节id |
| need\_edited\_data | boolean | 否 | true：编辑版信息，false：发布版信息。默认值：false |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| chapter | [object](#Res__chapter) | - | 章节信息 |

**Res.chapter Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| chapter\_id | string | 章节id |
| chapter\_title | string | 章节标题 |
| word\_cnt | number | 字数 |
| create\_time | number | 创建时间戳 |
| audit\_info | [object](#Res__chapter__audit_info) | 审核信息 |
| volume\_index | number | 所属分卷下标，-1 表示不属于任何分卷 |
| original\_id | string | 提供方章节主键 |
| seq | number | 章节相对顺序 |
| custom\_info | string | 自定义信息 |
| ban\_status | number | 管控状态，0：正常，1：下架 |

**Res.chapter.audit_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| audit\_status | number | 0：未提审，1：审核中，2：审核不通过，3：审核通过 |
| create\_time | number | 提审时间戳 |
| audit\_time | number | 审核时间戳 |
| reason | string | 审核原因 |
| suggestion | string | 修改建议。审核不通过时才会有该字段 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

### 调整章节顺序

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_reorderchapter.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| book\_id | string | 是 | 作品id |
| chapter\_id | string | 是 | 章节id |
| target\_chapter\_id | string | 是 | 目标章节id |
| operation | number | 是 | 排序操作，1：交换，2：插入到目标章节之前，3：插入到目标章节之后 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

### 调整章节相对顺序

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_updatechapterseq.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| book\_id | string | 是 | 作品id |
| chapter\_seq\_list | [objarray](#Body__chapter_seq_list<Array>) | 是 | 章节 seq 列表 |

**Body.chapter_seq_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| chapter\_id | string | 是 | 章节id |
| seq | number | 是 | 章节相对顺序，可非连续递增 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

### 作品提审

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_auditbook.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| book\_id | string | 是 | 作品id |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

### 新增账号-小说授权

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/auth/api_addbookauth.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| books | [objarray](#Body__books<Array>) | 是 | books |

**Body.books(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| book\_id | string | 是 | 作品id |
| grantee\_appid | string | 是 | 被授权账号appid |
| expire\_time | number | 是 | 授权到期时间unix时间戳，单位秒，按CST时区 可支持设置的最大值： 2147483646 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | 错误码。 因为新增授权可以一次增加多条授权关系，所以返回数据里 errcode 会有内外两个字段，外层 errcode 表示本次调用整体成功/失败，内层 errcode 表示每条授权关系是成功/失败。 具体可以看返回数据的示例 |
| results | [objarray](#Res__results<Array>) | results |

**Res.results(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | 内层errcode，表示每条授权关系是成功/失败 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

### 查看主授权关系列表-查看被授权关系列表

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/auth/api_querybookauth.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | number | 否 | 填 0 或者不设置: 查授权列表, 填 1: 查被授权列表（查看被授权关系列表时必填） |
| offset | number | 是 | 结果数据偏移位置 从 0 开始，用于翻页 |
| count | number | 是 | 获取记录的数量, 上限一次 30 条，用于翻页 |
| is\_sum | boolean | 否 | 填 true，返回总数，填 false 不返回（查看被授权关系列表时无需填写） |
| book\_id | string | 否 | 过滤出等于该 book\_id 的授权结果（查看被授权关系列表时无需填写） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | 错误码。 |
| results | [objarray](#Res__results<Array>) | results |

**Res.results(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| book\_id | string | 作品id |
| grantor\_appid | string | 主授权账号appid |
| grantee\_appid | string | 被授权账号appid |
| expire\_time | number | 授权到期时间，unix时间戳，单位秒，按CST时区 |
| sum | number | 总数，is\_sum = true 返回（（查看被授权关系列表时不返回） |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

### 删除指定的授权关系

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/auth/api_delbookauth.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| book\_id | string | 是 | 作品id |
| grantee\_appid | string | 是 | 被授权账号appid |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | 错误码。 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

### 新增账号-账号授权

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/auth/api_addbookauthbyappid.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| infos | [objarray](#Body__infos<Array>) | 是 | 被授权账号列表。上限一次 20 条 |

**Body.infos(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| grantee\_appid | string | 是 | 被授权账号appid |
| expire\_time | number | 是 | 授权到期时间，unix时间戳，单位秒，按CST时区 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | 错误码。 因为新增授权可以一次增加多条授权关系，所以返回数据里 `errcode` 会有内外两个字段，外层 `errcode` 表示本次调用整体成功/失败，内层 `errcode` 表示每条授权关系是成功/失败。 具体可以看返回数据的示例 |
| errmsg | string | [错误信息](#apierrcode) |
| results | array | 授权结果列表 |

---

### 查看账号主授权关系列表

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/auth/api_querybookauthv2.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | number | 否 | 填 0 或者不设置: 查授权列表, 填 1: 查被授权列表 |
| count | number | 是 | 获取记录的数量, 上限一次 100 条，用于分页 |
| cursor | string | 否 | 分页游标。不填或填空字符串，标识从第一页开始查询。后一页查询填充上一页响应的next\_cursor字段值 |
| grantor\_appid | string | 否 | 用于查询指定授权方授权给当前账户的小说列表，当查询指定授权方所授权的小说列表时需要传 |
| book\_ids | array | 否 | 用于查询指定小说的授权信息，上限一次 30 条。查询指定小说的授权信息场景下需要传递此参数。优先级高于 grantor\_appid，当 book\_ids 不为空时，grantor\_appid 参数无效。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| appid\_results | [objarray](#Res__appid_results<Array>) | 被授权方列表, 结果按授权过期时间从早到晚排序 |
| next\_cursor | string | 下一页游标 |

**Res.appid_results(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| grantor\_appid | string | 主授权账号appid |
| grantee\_appid | string | 被授权账号appid |
| expire\_time | number | 授权到期时间，unix时间戳，单位秒，按CST时区 |
| book\_id | string | 作品id，查询指定授权方授权给当前账户的小说列表时会返回 |

---

### 删除指定的账号授权关系

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/auth/api_delbookauthbyappid.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| grantee\_appid | string | 是 | 被授权账号appid |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

---

### 预览设置修改

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/preview/api_setpreviewsetting.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| book\_id | string | 是 | 作品id |
| default\_words | number | 是 | 默认预览字数 |
| chapter\_index | number | 否 | 章节索引，从 0 开始，未设置的章节将使用 default\_words 作为预览字数 |
| words | number | 否 | 章节字数 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

### 预览设置获取

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/preview/api_getpreviewsetting.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| book\_id | string | 是 | 作品id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| setting | [object](#Res__setting) | setting |

**Res.setting Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| book\_id | string | 作品id |
| default\_words | number | 默认预览字数 |
| chapter\_setting | [objarray](#Res__setting__chapter_setting<Array>) | chapter\_setting |

**Res.setting.chapter_setting(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| chapter\_index | number | 章节索引，从 0 开始,未设置的章节将使用 default\_words 作为预览字数 |
| words | number | 章节字数 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

### 读后推荐

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/other/api_novelreadersetrecmdnovel.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recmd\_type | number | 是 | 推荐小说的类型：1-android(付费小说) 2-ios(全文免费小说) |
| book\_id\_list | array | 是 | 推荐小说的 book\_id 数组 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 10140001 | 无效参数 |
| 10140002 | 请使用 utf-8 编码 |
| 10140003 | 无效的作品名 |
| 10140004 | 无效的作品简介 |
| 10140005 | 无效的封面图 |
| 10140006 | 无效的作者 |
| 10140007 | 无效的作品类型 |
| 10140008 | 无效的完结状态 |
| 10140009 | 无效的上传场景 |
| 10140010 | 无效的章节下标列表，请检查是否有重复或未覆盖所有章节 |
| 10140011 | 无效的章节ID列表，请检查是否有重复、不属于该作品的章节ID或未覆盖所有章节 |
| 10140012 | 无效的分卷列表，请检查分卷标题是否规范，区间是否存在交集或未覆盖所有章节 |
| 10140013 | 缺少章节信息 |
| 10140014 | 章节信息过多 |
| 10140015 | 缺少作品ID |
| 10140016 | 作品ID过多 |
| 10140017 | 无效的分页最大结果数 |
| 10140018 | 无效的章节标题 |
| 10140019 | 无效的章节内容 |
| 10140020 | 无效的排序操作 |
| 10140021 | 无效的章节排序方式 |
| 10140022 | 缺少章节seq |
| 10140023 | 请求参数中存在重复的提供方主键 |
| 10140024 | 无效的提供方主键 |
| 10140025 | 无效的优先级 |
| 10140026 | 无效的自定义信息 |
| 10141001 | 找不到对应信息 |
| 10141002 | 不允许操作 |
| 10141003 | 作品正在审核中 |
| 10141004 | 添加审核信息失败 |
| 10141005 | 太多检查不通过项 |
| 10141006 | 作品未审核通过，无法发布 |
| 10141007 | 作品缺少章节 |
| 10141008 | 作品分卷信息需要更新 |
| 10141009 | 提供方主键冲突 |
| 10141010 | 该接口与当前作品的章节排序方式不兼容，如需调用请先修改章节排序方式 |
| 10145001 | 操作结果为空 |
| 10145002 | 调用系统失败 |
| 10145003 | 缺少入参 |
| 10145004 | 授权作品ID无效 |
| 10145005 | 授权者不是小说类目 |
| 10145006 | 被授权者不是小说类目 |
| 10145007 | 过期的时间信息/或者授权的时间异常 |
| 10145008 | 一次提交授权的作品太多或者太少(count = 0 or count > 20) |
| 10145009 | 一次查询授权列表拉取的count太多(count > 100) |
| 10145010 | 添加的授权记录有部分失败 |
| 10145011 | appid无效 |
| 10145012 | 授权者和被授权者不能相同 |

---

<!-- pages: 23 -->
