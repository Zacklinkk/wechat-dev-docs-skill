# 小程序服务端 API 结构化参考 — API/B2b

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 开通流程

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/store_assistant/api_retailbusinessapply.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| goods\_type\_list | array | 是 | 主营商品类型。 可选项："食品", "饮料", "乳制品", "酒水", "生鲜果蔬", "调味品", "日化个护", "文具", "鞋服/配饰", "家居", "母婴/玩具", "数码3C", "其他" |
| goods\_sale\_list | array | 是 | 主要线下销售渠道。 可选项："杂货店", "便利店", "超市", "餐饮店", "母婴店", "烟酒店", "其他" |
| cover\_num | string | 是 | 门店覆盖数。 可选项："0-5千", "5千-1万", "1万-10万", "10万-50万", "50万以上" |
| service\_list | array | 是 | 所需服务类型。 可选项："门店订货", "门店促销", "门店活动执行", "门店直播", "其他" |
| description | string | 是 | 小程序方案概述。长度限制：21-100字 |
| contact\_name | string | 是 | 联系人姓名。长度限制：1-7字。 |
| contact\_phone | string | 是 | 联系人手机号 |
| contact\_email | string | 是 | 联系人邮箱 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number |  | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 成功开通 |
| 9404201 | 无效的主营商品类型 |
| 9404202 | 无效的主要线下销售渠道 |
| 9404203 | 无效的门店覆盖数 |
| 9404204 | 无效的所需服务类型 |
| 9404205 | 无效的小程序方案概述 |
| 9404206 | 无效的联系人姓名 |
| 9404207 | 无效的联系人手机号 |
| 9404208 | 无效的联系人邮箱 |
| 9404209 | 该账号不满足申请条件 |
| 9404210 | 已申请，请耐心等待 |

---

### 预录入门店信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/store_assistant/api_batchcreateretail.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| retail\_info\_list | [objarray](#Body__retail_info_list<Array>) | 是 | 门店信息列表。每次调用最多可导入 100 个门店 |

**Body.retail_info_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mobile\_phone | string | 是 | 手机号 |
| retail\_name | string | 是 | 门店名称。长度限制 1-100 个字符，一个中文字等于 2 个字符 |
| retail\_type | string | 否 | 一级门店类型。可选项："杂货店"、"便利店"、"超市"、"餐饮店"、"母婴店"、"烟酒店"、"其他" |
| sub\_retail\_type | string | 否 | 二级门店类型。一级类型为 "其他" 时必填 |
| address\_province | string | 是 | 门店地址，省 |
| address\_city | string | 是 | 门店地址，市 |
| address\_region | string | 是 | 门店地址，区县 |
| address\_street | string | 是 | 门店地址，街道详细地址 |
| registration\_number | string | 是 | 营业执照注册号 |
| biz\_name | string | 否 | 企业名称 |
| corporation\_name | string | 否 | 法人姓名 |
| latitude | number | 否 | 纬度 |
| longitude | number | 否 | 经度 |
| business\_type | array | 否 | 一级主营商品。可选项："食品饮料", "餐饮", "生鲜果蔬（含鲜花）", "烟酒", "鞋服内衣", "个护美妆", "3C数码", "家用电器", "汽修/汽配", "医药/医疗器械", "家装/五金/建材", "家居家纺", "文具玩具", "母婴", "宠物", "其他" |
| other\_business\_type | string | 否 | 二级主营商品。一级主营商品包含 "其他" 时必填 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| num\_success | number | num\_success |
| num\_failure | number | num\_failure |
| failure\_record\_list | [objarray](#Res__failure_record_list<Array>) | failure\_record\_list |

**Res.failure_record_list(Array) Object Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| mobile\_phone | string | 手机号 | - |
| registration\_number | string | 营业执照注册号 | - |
| failure\_code | number | failure\_code | [枚举值](#Enum_Res__failure_record_list<Array>__failure_code) |

**Res.failure_record_list(Array).failure_code Enum**

| 枚举值 | 描述 |
| --- | --- |
| 2 | 无效的手机号 |
| 3 | 无效的门店类型 |
| 4 | 地址解析失败 |
| 5 | 手机号已被录入门店信息 |
| 6 | 无效的门店名称（长度限制为 1-100 个字符，一个中文字等于 2 个字符） |
| 7 | 无效的主营商品 |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统繁忙，请稍后重试 |
| 0 | 成功 |
| 40001 | invalid credential, access\_token is invalid or not latest。 token 无效 |
| 41001 | access\_token missing |
| 47001 | data format error |
| 48001 | api unauthorized 小程序无该 api 权限，反馈给对接人开通 |
| 61004 | access clientip is not registered, not in ip-white-list |
| 61007 | api is unauthorized to component |
| 9404000 | 上传数量过多 |
| 9404001 | 门店信息参数缺失 |

---

### 门店信息查询

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/store_assistant/api_getretailinfo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 否 | 门店管理员/员工 openid。与手机号二选一，若都填写，优先使用 openid |
| mobile\_phone | string | 否 | 手机号 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| mobile\_phone | string | 手机号 |
| retail\_type | string | 一级门店类型 |
| sub\_retail\_type | string | 二级门店类型 |
| retail\_address | string | 门店地址 |
| retail\_name | string | 门店名称 |
| identification | string | 营业执照注册号 |
| principal | string | 企业名称 |
| legal\_person\_name | string | 法人姓名 |
| openid | string | 门店管理员/员工 openid。手机号查询时返回管理员 openid |
| role | string | 角色。1：管理员，2：员工。手机号查询时返回管理员 |
| status | number | 认证状态。1：已完成认证 |
| auth\_time | number | 认证时间戳 |
| grant\_time | number | 授权时间戳 |
| longitude | number | 经度。门店定位信息，若门店未提交定位信息，则返回值里无该字段 |
| latitude | number | 纬度。门店定位信息，若门店未提交定位信息，则返回值里无该字段 |
| business\_type | array | 一级主营商品 |
| other\_business\_type | string | 二级主营商品 |
| staff\_list | [objarray](#Res__staff_list<Array>) | 员工列表，包含管理员 |

**Res.staff_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| openid | string | 管理员/员工 openid |
| role | number | 角色。1：管理员，2：员工 |
| create\_time | number | 员工加入时间，管理员无该字段 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 |  |
| 0 | 成功 |
| 40001 | invalid credential, access\_token is invalid or not latest。token 无效 |
| 41001 | access\_token missing |
| 42001 | access\_token expired |
| 47001 | data format error |
| 48001 | api unauthorized 小程序无该api权限，反馈给对接人开通 |
| 61004 | access clientip is not registered, not in ip-white-list |
| 61007 | api is unauthorized to component |
| 9404101 | 非法参数 |
| 9404102 | 该店主不存在、未认证或者未授权给你 |
| 9404103 | 请求过于频繁，请稍后重试 |

---

### 全量授权门店查询

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/store_assistant/api_getretailopenidlist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| limit | number | 是 | 分页拉取最大返回结果数。取值范围：1-100 |
| page\_context | string | 是 | 分页上下文。每轮遍历的首次调用传空值，后续调用填上一次调用返回参数的 page\_context |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| openid\_list | array | openid 列表 |
| page\_context | string | 分页上下文 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 成功 |
| 40001 | invalid credential, access\_token is invalid or not latest。token 无效 |
| 48001 | api unauthorized 小程序无该api权限，反馈给对接人开通 |
| 61007 | api is unauthorized to component |
| 9404151 | 无效的分页拉取最大返回结果数 |
| 9404152 | 无效的分页上下文 |

---

### 模板消息列表及下发

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/notify/api_retailnotifybusiness.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | number | 是 | 枚举值参考[B2b门店助手模板消息汇总列表](https://docs.qq.com/sheet/DUnhCS01URmdobExD?tab=BB08J2) 注：对于keyword.DATA等”模板消息参数值内容限制说明“参见该链接：[模板消息--微信开放文档](https://developers.weixin.qq.com/doc/service/guide/product/template_message/Template_Message_Interface) |
| to\_user\_list | array | 是 | 门店负责人openid列表，最多一次发送200个openid |
| content | string | 否 | 消息内容，为json格式的字符串，不同类型对应的字符串示例见模板列表 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 40003 | 存在错误的openid! |
| 9403000 | 消息类型错误! |
| 9403001 | 消息字段的内容过长! |
| 9403002 | 消息字段的内容违规! |
| 9403003 | 发送的微信号太多! |

---

### 消息效果数据

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/notify/api_getretailmessagelist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 分页起始位置，从0开始计数，用于分页查询，默认值为0 |
| offset | number | 是 | 每页返回的数据条数上限，最大值为1000，默认值为20 |
| begin\_date | string | 是 | 开始时间，格式为“xxxx-yy-zz”的字符串，例如：“2024-08-01” |
| end\_date | string | 是 | 结束时间，格式为“xxxx-yy-zz”的字符串，例如：“2024-08-10” |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| total\_num | number | 查询到数据总数 |
| data\_line | [objarray](#Res__data_line<Array>) | 数据列表 |

**Res.data_line(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| msg\_id | number | 消息id |
| msg\_type | number | 消息类型 |
| date | string | 消息日期 |
| msg\_time | string | 消息发送时间 |
| send\_uv | number | 发送人数 |
| entry\_uv | number | 进入人数 |
| business\_msg\_id | string | 自定义msg\_id |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -1 | 系统错误 |
| 0 | 成功 |
| 40079 | 日期格式错误 |
| 45165 | offset格式错误或超过最大限制 |

---

### 商户号进件

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_retailregistermch.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id\_doc\_type\_num | number | 是 | 法人证件类型。 0-默认即大陆身份证，1-大陆身份证，2-其他国家或地区居民护照，3-中国香港居民来往内地通行证，4-中国澳门居民–来往内地通行证，5-中国台湾居民–来往大陆通行证，6-外国人居留证（仅开通微信支付时支持），7-港澳居民证（仅开通微信支付时支持），8-台湾居民证（仅开通微信支付时支持） [ 注：当前仅微信支付方式支持后三种证件类型，即仅当 open\_type = 0 时, id\_doc\_type\_num 可选填 6、7、8 ] |
| id\_card\_info | [object](#Body__id_card_info) | 否 | 经营者/法人身份证信息。当id\_doc\_type\_num为0和1时必填 |
| id\_doc\_info | [object](#Body__id_doc_info) | 否 | 经营者/法人其他类型证件信息。当id\_doc\_type\_num不为0和1时必填 |
| account\_info | [object](#Body__account_info) | 是 | 结算银行账户 |
| contact\_info | [object](#Body__contact_info) | 是 | 超级管理员信息 |
| business\_license | [object](#Body__business_license) | 是 | 营业执照 |
| merchant\_shortname | string | 是 | 商户名缩写 |
| organization\_type | boolean | 是 | 主体类型。个体户-0，企业-1 |
| qualification | [object](#Body__qualification) | 是 | 行业特殊资质资料。 |
| business\_addition\_desc | string | 否 | 补充说明。示例值：特殊情况，说明原因 |
| business\_addition\_pics | string | 否 | 补充材料 材料图片id可通过[上传商户图片API](api_retailuploadmchfile)获取获取。如有多张图片，请拼接成一张后上传。 |
| open\_type | number | 是 | 开通支付方式。 只开通微信支付-0 同时开通微信支付和银行转账-1 |
| ext\_register\_info | [object](#Body__ext_register_info) | 是 | 补充信息 |
| client\_ip | string | 是 | 商户 ip 地址。支持 iPv4 和 iPv6 |

**Body.id_card_info Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id\_card\_copy | string | 是 | 身份证人像面照片id, 通过[上传商户图片API](api_retailuploadmchfile)获取 |
| id\_card\_national | string | 是 | 身份证国徽面照片id, 通过[上传商户图片API](api_retailuploadmchfile)获取 |
| id\_card\_name | string | 是 | 身份证姓名 |
| id\_card\_number | string | 是 | 身份证号码 |
| id\_card\_valid\_time | string | 是 | 身份证有效期限, 格式如"2026-06-06"、"长期" |
| id\_card\_address | string | 是 | 身份证地址 |
| id\_card\_valid\_time\_begin | string | 是 | 身份证有效期开始日期, 格式如"2026-06-06" |

**Body.id_doc_info Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id\_doc\_name | string | 是 | 证件姓名 |
| id\_doc\_number | string | 是 | 证件号码 |
| id\_doc\_copy | string | 是 | 证件正面照片，通过[上传商户图片API](api_retailuploadmchfile)获取 |
| doc\_period\_end | string | 是 | 证件结束日期，格式如"2022-06-06"、"长期" |
| doc\_period\_begin | string | 是 | 证件有效期开始时间，格式如"2022-06-06" |
| id\_doc\_address | string | 是 | 证件居住地址 |
| id\_doc\_copy\_back | string | 是 | 证件反面照片，通过[上传商户图片API](api_retailuploadmchfile)获取 |

**Body.account_info Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bank\_account\_type | string | 是 | 账户类型，若主体为企业/党政、机关及事业单位/其他组织，可填"74"，表示对公账户；若主体为"小微/个人卖家"，可填"75"，表示对私账户；若主体为个体工商户，可填"74"或"75" 【附】银行信息相关参考： [省市区编号对照表](https://pay.weixin.qq.com/doc/v3/partner/4012082815) [开户银行全称对照表](https://pay.weixin.qq.com/doc/v3/partner/4012082812) [开户银行对照表](https://pay.weixin.qq.com/doc/v3/partner/4012082813) |
| account\_bank | string | 是 | 开户银行，比如"工商银行" |
| account\_name | string | 否 | 开户名称 |
| bank\_address\_code | string | 是 | 开户银行省市编码，例如"110000" |
| bank\_branch\_id | string | 否 | 开户银行联行号，开户银行全称（含支行）和开户银行联行号二选一 |
| bank\_name | string | 是 | 开户银行全称（含支行） |
| account\_number | string | 是 | 银行帐号 |

**Body.contact_info Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| contact\_type | string | 是 | 主体为"小微/个人卖家"，可填"65"; 主体为"个体工商户/企业/党政、机关及事业单位/其他组织"，可填"65"表示经营者/法人，或者"66"表示经办人。 |
| contact\_name | string | 是 | 超级管理员姓名 |
| contact\_id\_doc\_type | string | 是 | 超级管理员证件类型 当超级管理员类型是经办人时，请上传超级管理员证件类型。 // 中国大陆居民-身份证 "IDENTIFICATION\_TYPE\_MAINLAND\_IDCARD" // 其他国家或地区居民-护照 "IDENTIFICATION\_TYPE\_OVERSEA\_PASSPORT" // 中国香港居民–来往内地通行证 "IDENTIFICATION\_TYPE\_HONGKONG" // 中国澳门居民–来往内地通行证 "IDENTIFICATION\_TYPE\_MACAO" // 中国台湾居民–来往大陆通行证 "IDENTIFICATION\_TYPE\_TAIWAN" // 外国人居留证（仅开通微信支付时支持） "IDENTIFICATION\_TYPE\_FOREIGN\_RESIDENT" // 港澳居民证（仅开通微信支付时支持） "IDENTIFICATION\_TYPE\_HONGKONG\_MACAO\_RESIDENT" // 台湾居民证（仅开通微信支付时支持） "IDENTIFICATION\_TYPE\_TAIWAN\_RESIDENT" |
| contact\_id\_card\_number | string | 是 | 超级管理员身份证件号码 |
| contact\_id\_doc\_copy | string | 是 | 超级管理员证件正面照片id，当超级管理员类型是经办人时，请上传超级管理员证件的正面照片。 |
| contact\_id\_doc\_copy\_back | string | 是 | 超级管理员证件反面照片,当超级管理员类型是经办人时，请上传超级管理员证件的反面照片。 |
| contact\_id\_doc\_period\_begin | string | 是 | 超级管理员证件有效期开始时间 当超级管理员类型是经办人时，请上传证件有效期开始时间。 |
| contact\_id\_doc\_period\_end | string | 是 | 级管理员证件有效期结束时间 当超级管理员类型是经办人时，请上传证件有效期结束时间。 |
| business\_authorization\_letter | string | 是 | 业务办理授权函。1、当超级管理员类型是经办人时，请上传业务办理授权函。2、请参照示例图打印业务办理授权函，全部信息需打印，不支持手写商户信息，并加盖公章。 |
| mobile\_phone | string | 是 | 超级管理员手机, |
| contact\_email | string | 是 | 超级管理员邮箱,主体类型为"小微商户/个人卖家"可选填，其他主体需必填。 |

**Body.business_license Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| business\_license\_copy | string | 是 | 证件扫描件图片id，可通过[上传商户图片API](api_retailuploadmchfile)获取 |
| business\_license\_number | string | 是 | 证件注册号 |
| merchant\_name | string | 是 | 商户名称 |
| legal\_person | string | 是 | 经营者/法定代表人姓名 |
| company\_address | string | 否 | 注册地址，主体为"党政、机关及事业单位/其他组织"时必填，请填写登记证书的注册地址。 |
| business\_time | string | 否 | 营业期限，主体为"党政、机关及事业单位/其他组织"时必填。 |
| cert\_type | string | 否 | 1、主体为"政府机关/事业单位/社会组织"时，请上传登记证书类型。 2、主体为"个体工商户/企业"时，不填。 当主体为事业单位时，填枚举值："CERTIFICATE\_TYPE\_2388", 表示事业单位法人证书； 当主体为政府机关，填枚举值："CERTIFICATE\_TYPE\_2389"，表示统一社会信用代码证书 |

**Body.qualification Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| qualification\_type | string | 是 | 行业特殊资质类型，如"速送", 详情见[《行业对应特殊资质》](https://kf.qq.com/faq/220228qEfuAz220228bMFji6.html) |
| qualifications | string | 否 | 行业特殊资料, 字符串数组构成的字符串，示例值:"["jTpGmxUX3FBWVQ5NJInE4d2I6\_H7I4"]"。详情见[《行业对应特殊资质》](https://kf.qq.com/faq/220228qEfuAz220228bMFji6.html)，在需要上传时必填。 |

**Body.ext_register_info Object Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| door\_head\_file\_id | string | 是 | : string, 企业门头照 id，可通过上传商户资料 api 获取 - : string, - : string, - : string, - : string, - contact\_id\_doc\_address: string, 经办人证件地址，当超级管理员为经办人时补充填写 | - |
| store\_file\_id | string | 是 | 商城截图 id, 可通过[上传商户图片API](api_retailuploadmchfile)获取 | - |
| online\_pay\_file\_id | string | 是 | 确认订单付款界面截图 id，可通过[上传商户图片API](api_retailuploadmchfile)获取 | - |
| merchant\_scale | string | 是 | 企业规模，枚举值 | [枚举值](#Enum_Body__ext_register_info__merchant_scale) |
| authorization\_letter\_file\_id | string | 否 | 银行转账授权书图片 id，当同时开通银行转账（open\_type = 1）且超级管理员为经办人时填写。授权书见 [示例](https://mqq-imgcache.gtimg.cn/tbep/entrustment_b2b/b2b_protocol_250701.pdf)，图片 id 可通过[上传商户图片API](api_retailuploadmchfile)获取。 | - |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| order\_no | string | 进件申请单号 可用于查询进件状态 |

**Body.ext_register_info.merchant_scale Enum**

| 枚举值 | 描述 |
| --- | --- |
| LARGE | 大型企业 2000 人以上 |
| MIDDLE | 中型企业 150 至 2000 人 |
| SMALL | 小型企业 15 至 150 人 |
| TINY | 微型企业 15 人以下 |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 90000 | 商户主体已经处于进件中 |
| 90001 | 主体类型不符要求 |
| 90003 | 提交频繁 |
| 90004 | 证件类型不符 |
| 90005 | 该商户主体进件数目达到上限 |
| 222229 | 进件申请字段填写不完整 |
| 9403200 | id\_doc\_type\_num字段超出范围 |

---

### 上传商户图片

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_retailuploadmchfile.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file\_name | string | 是 | 文件名 |
| file | bytes | 是 | 文件二进制流的 Base64 编码 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| file\_id | string | 文件 id |

---

### 查询商户号开通状态

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_retailgetmchorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| out\_registration\_id | string | 否 | 订单号，某个特定的进件订单号（不填则表示拉出当前小程序的所有进件单） |
| page\_index | number | 否 | 分页拉取偏移 |
| page\_size | number | 否 | 分页拉取总量限制 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| list | [objarray](#Res__list<Array>) | 订单列表 |
| total | number | 返回订单总数 |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| status | number | 0-初始化 1-资料校验中 2-待账户验证 3-审核中 4-已驳回 5-待签约 6-完成 7-已冻结 8-已作废 9-完成前平台额外准备 |
| inner\_resp | [object](#Res__list<Array>__inner_resp) | inner\_resp |
| wqf\_register\_statement | [object](#Res__list<Array>__wqf_register_statement) | 银行转账开通状态，仅开通银行转账（即 open\_type = 1）时返回 |
| wx\_pay\_rate | number | 微信支付技术服务费率，万分比，比如 40 指的是 0.40% |
| wqf\_certified\_rate | number | 银行转账技术服务费率，开通银行转账后返回，万分比，比如 40 指的是 0.40% |
| bind\_scene\_status | number | 与小程序关联状态 1-关联申请中 2-关联失败 3-待商户号超管同意 4-待小程序超管同意 5-关联中 6-已关联 |

**Res.list(Array).inner_resp Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| sub\_merchant\_registration\_status | [object](#Res__list<Array>__inner_resp__sub_merchant_registration_status) | 申请状态 |

**Res.list(Array).inner_resp.sub_merchant_registration_status Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| applyment\_state | string | 申请状态： CHECKING: 资料校验中 ACCOUNT\_NEED\_VERIFY: 待账户验证 AUDITING: 审核中 REJECTED: 已驳回 NEED\_SIGN: 待签约 FINISH: 完成 FROZEN: 已冻结 CANCELED: 已作废。 示例值: FINISH 长度限制[1,32] |
| applyment\_state\_desc | string | 申请状态描述。示例值: "完成" 长度限制[1,1024] |
| sign\_state | string | 签约状态： 1. UNSIGNED: 未签约。 该状态下，电商平台可查询获取签约链接，引导二级商户的超级管理员完成签约； 2. SIGNED: 已签约。 指二级商户的超级管理员已完成签约。注意：若申请单被驳回，商户修改了商户主体名称、法人名称、超级管理员信息、主体类型等信息，则需要重新签约。 3. NOT\_SIGNABLE: 不可签约。 该状态下，暂不支持超级管理员签约。一般为申请单处于已驳回、已冻结、机器校验中状态，无法签约。 示例值: SIGNED  长度限制[1,16] |
| sign\_url | string | 签约链接： 1. 当申请状态为 NEED\_SIGN 或 签约状态为 UNSIGNED 时返回，该链接为永久有效； 2. 申请单中的超级管理员，需用已实名认证的微信扫码打开，完成签约。 示例值: https://pay.weixin.qq.com/public/apply4ec\_sign/s?applymentId=2000002126198476&sign=b207b673049a32c858f3aa0bd7d27c7ec 长度限制[1,256] |
| sub\_mchid | string | 电商平台二级商户号。当申请状态为 NEED\_SIGN 或 FINISH 时才返回。 示例值: 1542488631 长度限制[1,32] |
| account\_validation | [object](#Res__list<Array>__inner_resp__sub_merchant_registration_status__account_validation) | 汇款账户验证信息。当申请状态为 ACCOUNT\_NEED\_VERIFY 时有返回。可根据指引汇款，完成账户验证。 |
| audit\_detail | [objarray](#Res__list<Array>__inner_resp__sub_merchant_registration_status__audit_detail<Array>) | 驳回原因详情。各项资料的审核情况。当申请状态为 REJECTED 或 FROZEN 时才返回。 |
| legal\_validation\_url | string | 法人验证链接： 1. 当申请状态为 ACCOUNT\_NEED\_VERIFY，且通过系统校验的申请单，将返回链接。 2. 建议将链接转为二维码展示，让商户法人用微信扫码打开，完成账户验证。 注：商户申请单进入审核状态后，微信侧会校验法人证件号码是否跟营业执照匹配，若匹配，返回该字段；若不匹配，不支持法人扫码验证，不返回该字段。 示例值: http://pay.weixin.qq.com/public/apply4ec\_sign/s?applymentId=2000002126198476&sign=b207b673049a32c858f3aa0bd7d27c7ec 长度限制[1,256] |

**Res.list(Array).inner_resp.sub_merchant_registration_status.account_validation Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| account\_name | string | 账户名称 |
| account\_no | string | 账号 |
| pay\_amount | number | 支付金额 |
| destination\_account\_number | string | 目的账号 |
| destination\_account\_name | string | 目的账户名 |
| destination\_account\_bank | string | 目的银行 |
| city | string | 城市 |
| remark | string | 标志 |
| deadline | string | 截止日期 |

**Res.list(Array).inner_resp.sub_merchant_registration_status.audit_detailObject Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| param\_name | string | 参数名称 |
| reject\_reason | string | 驳回理由 |

**Res.list(Array).wqf_register_statement Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| wqf\_register\_state | number | 银行转账开通状态： 0: 未开通 1: 开通中 2: 开通成功 3: 开通失败，可尝试重新[申请开通银行转账](api_registeronlywqf) 4: 申请驳回，商户需[跳转银行转账页面](api_createwqflink)，完善信息后重新提交。 5: 申请开通中（已开通微信支付，申请开通银行转账的场景） 6: 申请开通失败（已开通微信支付，申请开通银行转账的场景） |
| wqf\_register\_state\_desc | string | 银行转账开通状态描述。示例值: "待完善信息" |
| request\_no | string | 银行转账开通单号。仅当银行转账进入开通状态（开通中、开通成功、开通失败、申请驳回）时返回，可用于获取跳转链接 示例值: "MSE123" |

---

### 申请开通银行转账

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_registeronlywqf.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| out\_registration\_id | string | 是 | 订单号，原有进件订单号 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**wqf_register_statement**

| 返回参数 | 参数名 | 类型 | 必填 | 描述 | 枚举值 |
| --- | --- | --- | --- | --- | --- |
| 银行转账开通状态 | wqf\_register\_state | uint32 | 是 | 银行转账开通状态 | 0: 未开通；1: 开通中；2: 开通成功；3: 开通失败，可尝试重新申请开通银行转账；4: 申请驳回，商户需跳转银行转账页面，完善信息后重新提交；5: 申请开通中（已开通微信支付，申请开通银行转账的场景）；6: 申请开通失败（已开通微信支付，申请开通银行转账的场景） |
| 银行转账开通状态描述 | wqf\_register\_state\_desc | string | 是 | 银行转账开通状态描述 | 示例值: "待完善信息" |
| 银行转账开通单号 | request\_no | string | 否 | 银行转账开通单号，仅当银行转账进入开通状态（开通中、开通成功、开通失败、申请驳回）时返回，可用于获取跳转链接 | 示例值: "MSE123" |

---

### 跳转银行转账页面

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_createwqflink.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request\_no | string | 是 | 银行转账开通单号 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |
| url | string | - | url |
| expire\_time | string | - | expire\_time |

---

### 获取小程序下所有商户的信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_getmchinfo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| mch\_list | [objarray](#Res__mch_list<Array>) | 商户列表 |
| total | number | 总数 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**Res.mch_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| sub\_mchid | string | string 商户号 注：有商户号不代表已开通成功，当 wxpay\_status 值为 “完成” 才能使用。 string - string - string string string |
| company\_name | string | 企业名称 |
| bank\_name | string | 开户银行 |
| bank\_account | string | 银行账号 脱敏处理，仅保留前两位和后两位，中间用 \* 代替。 |
| wxpay\_status | string | 微信支付开通状态。枚举： - 完成前平台额外准备 - 完成 |
| bank\_transfer\_status | string | 银行转账开通状态。枚举： - 未开通 - 开通中 - 开通成功 - 开通失败 - 申请驳回 |

---

### 报名微信支付技术服务费优惠活动

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_setmchprofitrate.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sub\_mchid | string | 是 | 商户号 |
| profit\_rate | number | 是 | 费率 万分比，比如 40 指的是 0.40% |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 11 | 缺少设置费率的权限 |
| 12 | 不在可以设置费率的时间范围内 |
| 13 | 费率只能下调 |
| 14 | 费率不在范围内调 |

---

### 报名银行转账技术服务费优惠活动

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_updatewqfchargefee.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sub\_mchid | string | 是 | 商户号 |
| certified\_charge\_fee\_numerator | number | 是 | 认证费率分子 认证门店的费率分子，分母统一为10000，certified\_charge\_fee\_numerator 取值范围应该大于等于22，小于等于40。 示例：费率千四（4/1000）, certified\_charge\_fee\_numerator = 40 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| merchant\_name | string | 商户名称 |
| certified\_charge\_fee\_numerator | number | 认证费率分子。 认证的门店的费率分子，分母统一为10000。 示例：费率千四（4/1000）, certified\_charge\_fee\_numerator = 40 |
| uncertified\_charge\_fee\_numerator | number | 未认证的费率分子。 未认证的费率分子，分母统一为10000。 示例：费率千六（6/1000）, uncertified\_charge\_fee\_numerator = 60 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 2 | 参数填写错误 |
| 14 | 设置费率不在合法范围内 |

---

### 查询银行转账的技术服务费率

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_getwqfchargefee.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sub\_mchid | string | 是 | 商户号 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| merchant\_name | string | 商户名称 |
| certified\_charge\_fee\_numerator | number | 认证费率分子。 认证的门店的费率分子，分母统一为10000。 示例：费率千四（4/1000）, certified\_charge\_fee\_numerator = 40 |
| uncertified\_charge\_fee\_numerator | number | 未认证的费率分子。 未认证的费率分子，分母统一为10000。 示例：费率千六（6/1000）, uncertified\_charge\_fee\_numerator = 60 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 1 | 尚未开通银行转账 |
| 2 | 参数填写错误 |

---

### 查询订单

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_getorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | pay\_sig | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mchid | string | 是 | 商户号 |
| out\_trade\_no | string | 否 | 商户订单号。长度限制[6,32]。商户系统内部订单号，只能是数字、大小写字母\_-\*且在同一个商户号下唯一 示例值：1217752501201407033233368018（与order\_id二选一填写） |
| order\_id | string | 否 | B2b支付订单号。长度限制[1,32]。B2b支付生成的订单号 示例值：o202307291423123564754773（与out\_trade\_no二选一填写） |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| appid | string | - | 小程序ID。长度限制[1,32]。商户申请的小程序对应的appid 示例值：wx8888888888888888 |
| mchid | string | - | 微信商户号。长度限制[1,32]。由微信支付生成并下发的商户号。 示例值：1230000109 |
| out\_trade\_no | string | - | 商户订单号。长度限制[6,32]。商户系统内部订单号，只能是数字、大小写字母\_-\*且在同一个商户号下唯一 示例值：1217752501201407033233368018 |
| order\_id | string | - | B2b支付订单号。长度限制[1,32]。B2b支付生成的订单号 示例值：o202307291423123564754773 |
| pay\_status | string | - | 订单状态，长度限制[1,32]。枚举值 ORDER\_INIT：订单初始化 ORDER\_PRE\_PAY：订单预下单成功，待支付 ORDER\_PAY\_SUCC：订单支付成功 ORDER\_CLOSE：订单已关闭 ORDER\_REFUND\_PROCESSING：订单正在退款中 ORDER\_REFUND：订单已有退款 示例值：ORDER\_PAY\_SUCC |
| pay\_time | string | - | 支付完成时间。长度限制[1,32]。支付完成时间，标准北京时间，时区为东八区，格式为yyyy-MM-dd HH:mm:ss 示例值：2023-07-20 17:04:28 |
| attach | string | - | 附加数据。长度限制[1,128]。在查询API和支付通知中原样返回，可作为自定义参数使用，实际情况下只有支付完成状态才会返回该字段。 示例值：自定义数据 |
| payer\_openid | string | - | 支付者。用户在直连商户appid下的唯一标识。 示例值：oUpF8uMuAJO\_M2pxb1Q9zNjWeS6o |
| amount | [object](#Res__amount) | - | 订单金额。订单金额信息，仅支持人民币 |
| wxpay\_transaction\_id | string | - | 微信支付订单号。微信支付生成的订单号（合单支付场景不返回） 示例值：2123191423123564754773 |
| env | number | - | 订单环境。订单环境 0：正式环境 1：沙箱环境 示例值：0 |
| settle\_status | number | - | 结算状态。长度限制[1,32]。枚举值 0：未结算 1：结算中 2：结算完成 示例值：0 |
| settle\_finish\_time | string | - | 结算完成时间。结算完成时间，当结算状态为结算完成时有返回，标准北京时间，时区为东八区，格式为yyyy-MM-dd HH:mm:ss 示例值：2025-01-01 00:00:00 |
| platform\_profit\_percent | number | - | 技术服务费率。技术服务费率，万分比（比如 60 指的是 0.60%），当结算状态为结算完成时有返回 示例值：60 |
| platform\_profit\_fee | number | - | 技术服务费。技术服务费，单位为分，当结算状态为结算完成时有返回 示例值：6 |
| bank\_type | string | - | 银行类型。支付类型说明。仅支付方式为微信支付且订单支付成功后返回，格式为银行简码\_具体类型(DEBIT借记卡/CREDIT信用卡/ECNY数字人民币)，例如ICBC\_DEBIT代表工商银行借记卡，非银行卡支付类型(例如余额/零钱通等)统一为OTHERS，具体请参考[《银行类型对照表》](https://pay.weixin.qq.com/doc/v3/merchant/4012076355)。 示例值：ICBC\_DEBIT |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**Res.amount Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| order\_amount | number | 订单总金额。订单总需支付金额，也即是真正下单总金额，单位为分 示例值：1300 |
| payer\_amount | number | 用户支付金额。用户支付金额，单位为分（指使用优惠券的情况下，这里等于总金额-优惠券金额，目前暂不支持优惠券） 示例值：1300 |
| currency | string | 货币类型。货币类型，仅支持人民币"CNY" 示例值：CNY |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 9403200 | 参数为空或非法 detail:[支付签名[pay\_sig]校验失败] |
| 9403201 | 数据不存在。订单不存在，请检查入参 |
| 9403203 | 商户未完成建档 detail:[获取商户号信息失败，请确认商户号是否开通成功] |

---

### 关闭订单

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_closeb2border.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | pay\_sig | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mchid | string | 是 | 微信商户号。长度限制[1,32]。由微信支付生成并下发的商户号。 示例值：1230000109 |
| out\_trade\_no | string | 否 | 商户订单号。长度限制[6,32]。原支付交易对应的商户订单号。商户订单号和B2b支付订单号必填其一 示例值：1217752501201407033233368018 |
| order\_id | string | 否 | B2b支付订单号。长度限制[1,32]。原支付交易对应的B2b支付订单号。商户订单号和B2b支付订单号必填其一 示例值：o202307291423123564754773 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 10004 | 关单失败 | 通过调用[查询订单api](api_getorder)确认订单最新状态 |
| 10711 | 订单状态无法调用关单，请刷新查看订单状态或稍后重试 | 通过调用[查询订单api](api_getorder)确认订单最新状态 |
| 9403203 | 商户未完成建档 detail:[获取商户号信息失败，请确认商户号是否开通成功] |  |

---

### 退款

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_refundorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | pay\_sig | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| mchid | string | 是 | 1230000109 | 微信商户号。长度限制[1,32]。由微信支付生成并下发的商户号。 |
| out\_trade\_no | string | 否 | 1217752501201407033233368018 | 商户订单号。长度限制[6,32]。原支付交易对应的商户订单号。商户订单号和B2b支付订单号必填其一 |
| order\_id | string | 否 | o202307291423123564754773 | B2b支付订单号。长度限制[1,32]。原支付交易对应的B2b支付订单号。商户订单号和B2b支付订单号必填其一 |
| out\_refund\_no | string | 是 | 12177525012014070332321235 | 商户退款单号。长度限制[6, 32] 。商户系统内部退款单号，商户系统内部唯一，只能是数字、大小写字母\_-\*，同一退款单号多次请求只退一笔。 |
| refund\_amount | number | 是 | 888 | 退款金额。单位为分，只能为整数，不能超过原订单支付金额。 |
| refund\_from | number | 是 | 1 | 退款来源，枚举值 1：人工客服退款 2：用户自己退款 3：其他 |
| refund\_reason | number | 否 | 3 | 退款原因。枚举值 0：暂无描述 1：产品问题 2：售后问题 3：意愿问题 4：价格问题 5：其他原因 |
| description | string | 否 | 抱枕 | 退款商品描述。长度限制[1,127] |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| refund\_id | string | r202307281444591411763685 | B2b支付退款单号。长度限制[1, 32] |
| out\_refund\_no | string | 12177525012014070332321235 | 商户退款单号。长度限制[6, 32]。户系统内部退款单号，商户系统内部唯一，只能是数字、大小写字母\_-\*，同一退款单号多次请求只退一笔。 |
| order\_id | string | o202307291423123564754773 | B2b支付订单号。长度限制[1,32]。原支付交易对应的B2b支付订单号 |
| out\_trade\_no | string | o202307291423123564754773 | 商户订单号。长度限制[1,32]。原支付交易对应的B2b支付订单号 |
| errcode | number | 0 | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**退款通知**

| 参数名 | 变量 | 类型[长度限制] | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| 小程序原始ID | ToUserName | string | 是 | 小程序原始ID |
| 事件消息openid | FromUserName | string | 是 | 微信官方的openid。示例值：oUpF8uMuAJO\_M2pxb1Q9zNjWeS6o |
| 消息发送时间 | CreateTime | int64 | 是 | 消息发送时间戳。示例值：1698643478 |
| 消息类型 | MsgType | string | 是 | 消息类型，固定为event。示例值：event |
| 事件类型 | Event | string | 是 | 事件类型，固定为retail\_refund\_notify。示例值：retail\_refund\_notify |
| 小程序ID | appid | string[1,32] | 是 | 商户申请的小程序对应的appid。示例值：wx8888888888888888 |
| 微信商户号 | mchid | string[1,32] | 是 | 由微信支付生成并下发的商户号。示例值：1230000109 |
| 商户退款单号 | out\_refund\_no | string[6, 32] | 是 | 商户系统内部退款单号，商户系统内部唯一，只能是数字、大小写字母\_-\*，同一退款单号多次请求只退一笔。示例值：12177525012014070332321235 |
| B2b支付退款单号 | refund\_id | string[1, 32] | 否 | B2b支付退款单号。示例值：r202307281444591411763685 |
| 商户订单号 | out\_trade\_no | string[6,32] | 是 | 商户系统内部订单号，只能是数字、大小写字母\_-\*且在同一个商户号下唯一。示例值：1217752501201407033233368018 |
| B2b支付订单号 | order\_id | string[1,32] | 是 | B2b支付生成的订单号。示例值：o202307291423123564754773 |
| 退款金额 | refund\_amount | int64 | 是 | 退款金额，单位为分，只能为整数，不能超过原订单支付金额。示例值：888 |
| 订单总金额 | order\_amount | int64 | 是 | 订单总支付金额，单位为分。示例值：1300 |
| 退款来源 | refund\_from | string | 是 | 退款来源，枚举值 1：人工客服退款 2：用户自己退款 3：其他。示例值：1 |
| 退款原因 | refund\_reason | string | 否 | 退款原因，枚举值 0：暂无描述 1：产品问题 2：售后问题 3：意愿问题 4：价格问题 5：其他原因。示例值：3 |
| 退款创建时间 | create\_time | string[1, 32] | 是 | 退款受理时间，标准北京时间，时区为东八区，格式为yyyy-MM-dd HH:mm:ss。示例值：2023-07-30 17:04:23 |
| 退款成功时间 | refund\_time | string[1, 32] | 否 | 退款成功时间，当退款状态为退款成功时有返回，标准北京时间，时区为东八区，格式为yyyy-MM-dd HH:mm:ss。示例值：2023-07-30 17:04:28 |
| 退款状态 | refund\_status | string[1, 32] | 是 | 仅退款成功或失败时通知，枚举值：REFUND\_SUCC：退款成功；REFUND\_FAIL：退款失败；示例值：REFUND\_SUCC |
| 微信支付退款单号 | wxpay\_refund\_id | string[1, 32] | 否 | 微信支付退款单号。示例值：1235481444591411763685 |
| 订单环境 | env | int32 | 是 | 订单环境 0：正式环境 1：沙箱环境。示例值：0 |
| 交易渠道类型 | pay\_channel | int32 | 是 | 交易渠道类型 0：微信支付 1：银行转账。示例值：0 |
| 退款说明 | refund\_desc | string[1, 256] | 否 | 退款说明。示例值：账户资金不足，请待充足后重新发起 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 10604 | 单笔订单的退款频率过高 | 在一分钟内只能发起一次退款，请稍后重试 |
| 9403200 | 参数为空或不合法。 | 按照文档要求传参，根据返回的具体错误描述检查参数 |
| 9403201 | 数据不存在 | 订单不存在，请检查入参 |
| 9403202 | 退款单已受理 | 请调用查询退款接口确认退款请求 |
| 9403203 | 建档未完成，还不能发起支付或退款 | 请完成建档签约流程 |
| 9403205 | 订单无法退款（订单状态不对或超过160天） | 请检查订单状态或订单时间 |
| 9403206 | 退款状态未知，请商户2分钟后主动查询退款状态 | 请2分钟后调用查询退款接口确认退款状态 |
| 9403208 | 该订单正在退款中，请等待退款完成再发起新的退款 | 请等待退款完成再发起新的退款 |
| 9403209 | 不允许结算前退款 | 请等待订单结算后再退款 |

---

### 查询退款

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_getrefund.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | pay\_sig | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| mchid | string | 是 | 1230000109 | 微信商户号。长度限制[1,32]。由微信支付生成并下发的商户号。 |
| out\_refund\_no | string | 是 | 12177525012014070332321235 | 商户退款单号。长度限制[6, 32] 。商户系统内部退款单号，商户系统内部唯一，只能是数字、大小写字母\_-\*，同一退款单号多次请求只退一笔。 |
| refund\_id | string | 否 | r202307281444591411763685 | B2b支付退款单号。长度限制[1,32]。商户退款单号和B2b支付退款单号必填其一 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| refund\_id | string | r202307281444591411763685 | B2b支付退款单号。长度限制[1, 32]。 |
| out\_refund\_no | string | 12177525012014070332321235 | 商户退款单号。长度限制[6, 32] 是 商户系统内部退款单号，商户系统内部唯一，只能是数字、大小写字母\_-\*，同一退款单号多次请求只退一笔。 |
| order\_id | string | o202307291423123564754773 | B2b支付订单号。长度限制[1,32]。原支付交易对应的B2b支付订单号 |
| out\_trade\_no | string | 1217752501201407033233368018 | 商户订单号。长度限制[6,32]。原支付交易对应的商户订单号 |
| create\_time | string | 2023-07-30 17:04:23 | 退款创建时间。长度限制[1, 32]。退款受理时间，标准北京时间，时区为东八区，格式为yyyy-MM-dd HH:mm:ss。 |
| refund\_time | string | 2023-07-30 17:04:28 | 退款成功时间。长度限制[1, 32] 。当退款状态为退款成功时有返回，标准北京时间，时区为东八区，格式为yyyy-MM-dd HH:mm:ss。 |
| refund\_status | string | REFUND\_SUCC | 退款状态。长度限制[1, 32]。退款单状态，枚举值： REFUND\_INIT：退款单初始化 REFUND\_PROCESSING：退款处理中 REFUND\_SUCC：退款成功 REFUND\_FAIL：退款失败 |
| refund\_desc | string | 账户资金不足，请待充足后重新发起 | 退款说明。长度限制[1, 256]。 |
| amount | [object](#Res__amount) | - | 金额信息。金额详细信息，仅支持人民币 |
| wxpay\_refund\_id | string | 1235481444591411763685 | 微信支付退款单号。长度限制[1, 32] |
| reverse\_sett\_state | number | 0 | 技术服务费回退状态，枚举值： 0：技术服务费未回退 1：技术服务费回退处理中 2：技术服务费回退成功 3：无需回退技术服务费 |
| reverse\_sett\_finish\_time | string | 2023-07-30 17:04:28 | 技术服务费回退完成时间，当技术服务费回退状态为成功时有返回，标准北京时间，时区为东八区，格式为yyyy-MM-dd HH:mm:ss |
| platform\_profit\_percent | number | 60 | 技术服务费率，万分比（比如 60 指的是 0.60%），当技术服务费回退状态为成功时有返回 |
| reverse\_sett\_amt | number | - | 回退技术服务费，单位为分，当技术服务费回退状态为成功时有返回 |
| refund\_channel\_info | [object](#Res__refund_channel_info) | - | 退款渠道信息，仅支付方式为微信支付且订单退款成功后返回 |
| description | string | 抱枕 | 退款商品描述。 |
| errcode | number | - | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**Res.amount Object Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| order\_amount order\_amount | number | 1300 | 订单总金额，单位为分 |
| refund\_amount | number | 100 | 退款金额，单位为分，可以做部分退款 |
| currency | string | CNY | 货币类型，仅支持人民币"CNY" |

**Res.refund_channel_info Object Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| channel | string | ORIGINAL | 退款渠道。订单退款渠道，有以下枚举： ORIGINAL: 原路退款 BALANCE: 退回到余额 OTHER\_BALANCE: 原账户异常退到其他余额账户 |
| user\_received\_account | string | 100 | 退款入账账户。当前退款单的退款入账方，取值有以下几种情况： 1）退回银行卡：{银行名称}{卡类型}{卡尾号} 2）退回支付用户零钱：支付用户零钱 3）退还商户：商户基本账户商户结算银行账户 4）退回支付用户零钱通：支付用户零钱通 5）退回支付用户银行电子账户：支付用户银行电子账户 6）退回支付用户零花钱：支付用户零花钱 7）退回用户经营账户：用户经营账户 8）退回支付用户来华零钱包：支付用户来华零钱包 9）退回企业支付商户：企业支付商户 |
| funds\_account | string | AVAILABLE | 资金账户。退款所使用资金对应的资金账户类型，有以下枚举： AVAILABLE: 可提现金额账户 UNAVAILABLE: 待结算金额账户 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 10604 | 单笔订单的退款频率过高 | 在一分钟内只能发起一次退款，请稍后重试 |
| 61004 | access clientip is not registered requestIP: XXX | 若是第三方平台代调用接口，将IP添加到第三方平台的白名单列表，查看[排错指南](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/troubleshooting/TroubleShooting.html) |
| 9403200 | 参数为空或不合法。 | 按照文档要求传参，根据返回的具体错误描述检查参数 |
| 9403201 | 数据不存在。订单不存在，请检查入参 |  |
| 9403201 | 数据不存在 | 订单不存在，请检查入参 |
| 9403202 | 退款单已受理 | 请调用查询退款接口确认退款请求 |
| 9403203 | 建档未完成，还不能发起支付或退款 | 请完成建档签约流程 |
| 9403205 | 订单无法退款（订单状态不对或超过160天） | 请检查订单状态或订单时间 |
| 9403206 | 退款状态未知，请商户2分钟后主动查询退款状态 | 请2分钟后调用查询退款接口确认退款状态 |
| 9403208 | 该订单正在退款中，请等待退款完成再发起新的退款 | 请等待退款完成再发起新的退款 |
| 9403209 | 不允许结算前退款 | 请等待订单结算后再退款 |

---

### 获取密钥AppKey

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_getappkey.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| mchid | string | 是 | 1230000109 | 微信商户号。长度限制[1,32]。由微信支付生成并下发的商户号。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| appkey | string | - | 现网AppKey。由平台生成并下发的现网应用密钥。 |
| sandbox\_appkey | string |  | 沙箱AppKey。由平台生成并下发的沙箱应用密钥。 |
| errcode | number | 0 | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

---

### 接口下载交易账单与资金账单

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_downloadbill.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | pay\_sig | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| mchid | string | 是 | - | 商户号 |
| bill\_date | string | 是 | 20231102 | 账单日期，格式:yyyymmdd |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| success\_bill\_url | string | 微信支付渠道支付成功订单下载链接，包括支付成功时间在当天的订单 |
| refund\_bill\_url | string | 微信支付渠道退款单下载链接，发起退款成功在当天的退款单 |
| all\_bill\_url | string | 包括微信支付渠道支付成功和退款单的下载链接 |
| fund\_bill\_url | string | 微信支付渠道的资金账单下载链接 |
| ended\_day\_avail\_amt | number | 日终账户可提现金额 |
| ended\_day\_frozen\_amt | number | 日终账户待结算金额 |
| ended\_day\_total\_amt | number | 日终账户总金额，等于日终账户可提现金额+日终账户待结算金额 |
| profit\_sharing\_bill\_url | string | 分账成功订单下载链接，包括分账成功时间在当天的订单 |
| profit\_refund\_bill\_url | string | 分账回退单下载链接，发起分账回退成功在当天的退款单 |
| bankpay\_fund\_bill\_url | string | 银行转账渠道资金帐单下载链接 |

**4. 注意事项**

| 字段名 | 说明 | 示例 |
| --- | --- | --- |
| 交易时间 | 指该笔交易的支付成功时间或发起退款成功时间（注：不是退款成功时间），格式为yyyy-MM-DD HH:MM:SS | 2023-10-23 09:00:00 |
| 公众账号ID | 发起该笔交易时使用的小程序appid | wxab8acb865bb11234 |
| 交易商户号 | 进行交易收款的微信支付子商户号，8~10位数字 | 1234567890 |
| 微信订单号 | 微信小程序平台为该笔订单分配的订单号 |  |
| 商户订单号 | 商户传入的该笔订单商户订单号，对应下单接口里的out\_trade\_no字段 |  |
| 用户标识 | 微信为支付用户在公众账号ID(appid)下分配的唯一标识(openid) |  |
| 交易状态 | 识该笔明细数据的类型：SUCCESS，支付成功，说明该行数据为一笔支付成功的订单；REFUND，转入退款，说明该行数据为一笔发起退款成功的退款单 | SUCCESS |
| 微信退款单号 | 微信小程序平台为该笔退款分配的退款单号，如果该行数据为订单（交易状态SUCCESS）则展示0 |  |
| 商户退款单号 | 商户发起退款时填入的商户退款单号，如果该行数据为订单（交易状态SUCCESS）则展示0 |  |
| 退款金额 | 该笔退款单参与计费的应结算金额（申请退款金额-免充值券退款金额），如果该行数据为订单则展示为0.00，非负数、单位元，保留到小数点后2位 | 6.66 |
| 退款状态 | 生成账单文件时该笔退款的状态、出账后不会更新，如果该行数据为订单（交易状态SUCCESS），则留空 。SUCCESS：退款成功；PROCESSING：退款处理中 |  |
| 商品名称 | 商户传入的该笔订单（或该笔退款对应的订单）的商品名称，对应下单接口里的body字段,目前都为空 |  |
| 商户数据包 | 商户传入的该笔订单（或该笔退款对应的订单）的商户数据包，对应下单接口里的attach字段，不传时留空 |  |
| 技术服务费 | 该笔订单/退款对应的技术服务费费金额，订单对应正数、退款对应负数，单位元，保留小数点后2位 | 0.01 |
| 技术服务费费率 | 该笔交易收取技术服务费所使用的费率，百分数 0.22% |  |
| 订单金额 | 该笔订单的支付金额，如果该行数据为退款或撤销则填0.00，单位元，保留到小数点后2位 | 2.33 |
| 申请退款金额 | 商户发起退款的金额，包括退给用户的金额、充值券退款金额、免充值券退款金额，如果该行数据订单则填0.00，单位元，保留到小数点后2位 | 2.22 |
| 结算状态 | 生成账单文件时该笔订单的结算状态、出账后不会更新。该笔订单的结算状态：SUCCESS:已结算；NO\_SETTLE:未结算；SETTLING:结算中 |  |
| 结算时间 | 结算的时间，在结算状态为"已结算"的时候展示，格式为yyyy-MM-DD HH:MM:SS | 2023-10-23 02:00:00 |
| 交易渠道类型 | 订单的支付方式，仅当前商户号开通了银行转账时携带此字段。1：微信支付；2：银行转账 | 1 |

**4. 注意事项**

| 字段名 | 说明 | 示例 |
| --- | --- | --- |
| 记账时间 | 格式为yyyy-MM-DD HH:MM:SS | 2023-10-23 09:00:00 |
| B2b支付业务单号 | 展示该笔资金变动来自的业务。交易业务：展示支付单号；退款业务：展示退款单号；提现业务：展示提现单号 |  |
| 资金流水单号 | 该笔资金变动的系统单号 |  |
| 业务名称 |  |  |
| 业务类型 |  |  |
| 收支类型 |  |  |
| 收支金额(元) | 该笔资金变动的金额 |  |
| 账户结余(元) | 展示该笔资金变动后，剩余的账户总金额 |  |

**4. 注意事项**

| 业务名称 | 业务类型 | 收支类型 |
| --- | --- | --- |
| 交易 | 交易 | 收入 |
| 退款 | 退款 | 支出 |
| 交易 | 交易结算扣除手续费 | 支出 |
| 退款 | 已结算退款返还手续费 | 收入 |
| 提现 | 提现 | 支出 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 61004 | access clientip is not registered requestIP: XXX | 若是第三方平台代调用接口，将IP添加到第三方平台的白名单列表，查看[排错指南](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/troubleshooting/TroubleShooting.html) |
| 9403200 | 参数为空或非法 detail:[支付签名[pay\_sig]校验失败] |  |
| 9403201 | 数据不存在。订单不存在，请检查入参 |  |
| 9403203 | 商户未完成建档 detail:[获取商户号信息失败，请确认商户号是否开通成功] |  |

---

### 查询账户余额

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_getmchbalance.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | pay\_sig | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| mchid | string | 是 | 1230000109 | 微信商户号。长度限制[1,32]。由微信支付生成并下发的商户号。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| balance\_list | [objarray](#Res__balance_list<Array>) | - | 账户资金。商户号的账户资金 |
| errcode | number | 0 | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**Res.balance_list(Array) Object Payload**

| 参数名 | 类型 | 示例 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| balance\_type | string | BALANCE\_TYPE\_AVAILABLE | 资金类型。 | [枚举值](#Enum_Res__balance_list<Array>__balance_type) |
| amount | string | 0.00 | 金额值。单位为元 | - |
| currency | string | CNY | 货币类型 | - |

**Res.balance_list(Array).balance_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| BALANCE\_TYPE\_AVAILABLE | 可提现金额 |
| BALANCE\_TYPE\_FROZEN | 待结算金额 |

---

### 发起手动提现

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_manualwithdraw.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | pay\_sig | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| mchid | string | 是 | 1230000109 | 微信商户号。长度限制[1,32]。由微信支付生成并下发的商户号。 提现金额， 示例值： 是 商户外部提现单号，同一个商户号下唯一，只允许数字和大小写字母\_-\*，长度要求为[6,32]。 示例值：aaa123 |
| withdraw\_amount | number | 是 | 100 | 提现金额，单位为分，金额需大于0。 |
| out\_withdraw\_no | string | 是 | aaa123 | 外部提现单号。长度限制[6,32]。商户外部提现单号，同一个商户号下唯一，只允许数字和大小写字母\_-\* |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

---

### 查询提现状态

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_querywithdraw.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | pay\_sig | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| mchid | string | 是 | 1230000109 | 微信商户号。长度限制[1,32]。由微信支付生成并下发的商户号。 提现金额， 示例值： 是 商户外部提现单号，同一个商户号下唯一，只允许数字和大小写字母\_-\*，长度要求为[6,32]。 示例值：aaa123 |
| out\_withdraw\_no | string | 是 | aaa123 | 外部提现单号。长度限制[6,32]。商户发起提现时传入的外部提现单号。 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| out\_withdraw\_no | string | aaa123 | 外部提现单号。长度限制[6,32]。商户发起提现时传入的外部提现单号。 | - |
| withdraw\_amount | number | 100 | 提现金额 | - |
| status | string | WITHDRAW\_SUCC | 提现状态 | [枚举值](#Enum_Res__status) |
| fail\_reason | string | 申请提现金额小于留存额 | 提现失败原因（仅当提现状态为 WITHDRAW\_FAIL 时返回） | - |
| errcode | number | 0 | [错误码](#apierrcode) | - |
| errmsg | string | ok | [错误信息](#apierrcode) | - |

**Res.status Enum**

| 枚举值 | 描述 |
| --- | --- |
| WITHDRAW\_INIT | 初始化 |
| WITHDRAW\_PROCESSING | 进行中 |
| WITHDRAW\_SUCC | 成功 |
| WITHDRAW\_FAIL | 失败 |
| WITHDRAW\_REFUND | 提现退票（银行回退） |

---

### 微信支付自动提现接口

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_setautowithdraw.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | pay\_sig | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 | 枚举 |
| --- | --- | --- | --- | --- | --- |
| mchid | string | 是 | 1230000109 | 微信商户号。长度限制[1,32]。由微信支付生成并下发的商户号。 | - |
| status | number | 否 | 1 | 自动提现状态。是否开启自动提现 | [枚举值](#Enum_Body__status) |
| retain\_amt | number | 否 | 500000 | 留存额。账户留存金额，单位为分。每天根据昨日"可提现金额"账户的日终余额减去留存额，发起提现并到账。若发起提现申请时，"可提现金额账户"的当前余额少于昨日日终余额，则提现失败，返回余额不足的错误。 | - |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**Body.status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 开启自动提现功能 |
| 2 | 关闭自动提现功能 |

**5. 注意事项**

| 提现金额规则 | 设置留存额规则 |
| --- | --- |
| 【日终账户余额】前一日的日终可提现账户余额减留存额 | 设置留存额以防提现后账户余额不足，影响退款业务，请根据业务实际情况进行设置。  当系统自动发起提现时，若当前可提现金额<前一日日终可提现金额-留存额，则提现会失败 |

---

### 添加分账方

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_addprofitsharingaccount.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | pay\_sig | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| profit\_sharing\_relation\_type | string | 是 | 分账接收方关系类型 | [枚举值](#Enum_Body__profit_sharing_relation_type) |
| payee\_type | string | 是 | 分账接收方类型 | [枚举值](#Enum_Body__payee_type) |
| payee\_id | string | 是 | 分账接收方标识。 根据payee\_type填入openid或商户号： 当payee\_type="PAYEE\_TYPE\_EXTERNAL\_USER"时填openid； 当payee\_type="PAYEE\_TYPE\_EXTERNAL\_MERCHANT"时填商户号 | - |
| payee\_name | string | 否 | 分账接收方名称（分账接收方为商户号时必填）。 payee\_type="PAYEE\_TYPE\_EXTERNAL\_MERCHANT"时，填写商户名称 | - |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**Body.profit_sharing_relation_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| RELATION\_TYPE\_SUPPLIER | 供应商 |
| RELATION\_TYPE\_DISTRIBUTOR | 分销商 |
| RELATION\_TYPE\_SERVICE\_PROVIDER | 服务商 |
| RELATION\_TYPE\_PLATFORM | 平台 |
| RELATION\_TYPE\_OTHERS | 其他 |

**Body.payee_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| PAYEE\_TYPE\_EXTERNAL\_USER | 外部用户 |
| PAYEE\_TYPE\_EXTERNAL\_MERCHANT | 外部商户 |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 210001 | 添加分账方频繁 |
| 210002 | 添加分账方传入环境参数错误 |
| 210003 | 添加分账方传入账户类型错误 |
| 210004 | 重复添加分账方 |
| 210006 | 单个小程序绑定的分账方超过上限 |

---

### 删除分账方

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_delprofitsharingaccount.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | pay\_sig | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| payee\_type | string | 是 | 分账接收方类型 | [枚举值](#Enum_Body__payee_type) |
| payee\_id | string | 是 | 分账接收方标识。 根据payee\_type填入openid或商户号： 当payee\_type="PAYEE\_TYPE\_EXTERNAL\_USER"时填openid； 当payee\_type="PAYEE\_TYPE\_EXTERNAL\_MERCHANT"时填商户号； | - |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**Body.payee_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| PAYEE\_TYPE\_EXTERNAL\_USER | 外部用户 |
| PAYEE\_TYPE\_EXTERNAL\_MERCHANT | 外部商户 |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 210001 | 删除分账方频繁 |
| 210002 | 删除分账方传入环境参数错误 |
| 210003 | 分账接受方已被删除 |
| 210005 | 分账账户不存在 |
| 210007 | 删除分账方传入账户类型错误 |

---

### 查询分账方

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_queryprofitsharingaccount.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | pay\_sig | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 否 | 分账方数据起始位置的偏移量，默认值为0 |
| limit | number | 否 | 返回分账方数据的最大条数，默认值为10 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | - |
| errmsg | string | - |
| account\_list | [objarray](#Res__account_list<Array>) | 包含多个RetailProfitSharingAccountInfo对象 |

**Res.account_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| sharing\_account\_type | string | 枚举值："PAYEE\_TYPE\_EXTERNAL\_USER" - 外部用户；"PAYEE\_TYPE\_EXTERNAL\_MERCHANT" - 外部商户；（与添加分账方 API 中的 payee\_type 对应） |
| sharing\_account | string | 类型为外部用户时，表示个人 openid；类型为外部商户时，表示商户号；（与添加分账方 API 中的 payee\_id 对应） |
| add\_time | number | - |
| update\_time | number | - |
| name | string | 类型为外部商户时，返回对应的商户名称 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 1 | 查询不到可用分账方 |

---

### 请求分账

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_createprofitsharingorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | pay\_sig | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mchid | string | 是 | 子商户id。在B2b小程序中进件完成返回的子商户 id |
| out\_trade\_no | string | 是 | 支付单 id。在B2b小程序中下单的订单 id |
| profit\_fee | number | 是 | 分账费用。单位:分，不超过支付单本身的金额 |
| receiver\_type | string | 是 | 分账接收方类型。同添加分账方时填入的内容 |
| receiver\_account | string | 是 | 分账接收方账号。同添加分账方时填入的内容 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errmsg | string |  | [错误码](#apierrcode) |
| errcode | number | ok | [错误信息](#apierrcode) |

**4. 注意事项**

| 订单分账状态 | 申请退款金额 | 退款前提 | 退款出款账户 |
| --- | --- | --- | --- |
| 订单标记为需要分账 | 申请全额退款 | 1、需要先调“完成分账”接口，将订单剩余冻结资金从“待结算金额”账户全部解冻至“可提现金额”账户  2、“可提现金额”账户余额≥申请退款金额，支付单扣除手续费将在退款成功后返还 | “可提现金额”账户 |
|  | 申请部分退款 | 当申请退款金额≤订单未分账冻结金额，直接可退 | “待结算金额”账户 |
|  |  | 1、当申请退款金额＞订单未分账冻结金额，需要先调“完成分账”接口，将订单剩余冻结资金从“待结算金额”账户全部解冻至“可提现金额”账户   2、“可提现金额”账户余额≥申请退款金额，支付单扣除手续费将在退款成功后返还 | “可提现金额”账户 |
| 订单已完结分账 | 申请全额/部分退款 | “可提现金额”账户余额≥申请退款金额，支付单扣除手续费将在退款成功后返还 | “可提现金额”账户 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 10031 | 不存在对应的账单执行第三方分账 | 检查out\_trade\_no是否为对应商户号下交易成功的订单 |
| 10032 | 分账比例超过账单最大限制 |  |
| 10034 | 请等待后重试 |  |
| 10037 | 重复发起分账 |  |

---

### 查询分账结果

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_queryprofitsharingorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | pay\_sig | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| out\_trade\_no | string | 是 | 支付单 id。在B2b小程序中下单的订单 id |
| receiver\_type | string | 是 | 分账接收方类型。同添加分账方时填入的内容 |
| receiver\_account | string | 是 | 分账接收方账号。同添加分账方时填入的内容 |
| mchid | string | 是 | 商户号 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| order\_status | number | 分帐状态 | [枚举值](#Enum_Res__order_status) |
| errcode | number | [错误码](#apierrcode) | - |
| errmsg | string | 错误信息（若 order\_status 不为成功，且 errmsg 非空，可参考具体原因： S\_NO\_ENOUGH\_MONEY：分账余额不足。可能是分账金额超过可分账余额，或者订单已过期解冻。建议调用查询分账余额接口检查。 ACCOUNT\_ABNORMAL： 收款方账号异常。解决异常后，分帐单会自动扭转成功。 S\_TOO\_MANY\_PROFIT\_TIMES：分账次数过多，超过50次。 S\_ALREADY\_FINISHED（分账已完结）：表示该笔订单的分账已经被系统自动完结，无法再发起分账。原因是订单经过多次退款后，冻结资金已不足以支撑分账操作） | - |

**Res.order_status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 初始化 |
| 2 | 成功 |
| 3 | 失败 |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 10038 | 未发起第三方分账 |

---

### 查询分账剩余金额

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_queryprofitsharingremainamt.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | pay\_sig | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mchid | string | 是 | 子商户id。在B2b小程序中进件完成返回的子商户 id |
| out\_trade\_no | string | 是 | 订单 id。在B2b小程序中下单的订单 id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| remain\_amt | number | 冻结金额，单位：分 |

---

### 完成分账

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_finishprofitsharingorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | pay\_sig | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mchid | string | 是 | 子商户id。在B2b小程序中进件完成返回的子商户 id |
| out\_trade\_no | string | 是 | 订单 id。在B2b小程序中下单的订单 id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 10034 | 请等待后重试 |
| 10036 | 该笔支付单已经分账完成 |

---

### 请求分账回退

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_refundprofitsharing.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | pay\_sig | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| out\_trade\_no | string | 是 | 订单 id。在B2b小程序中下单的订单 id |
| out\_refund\_no | string | 是 | 退款单 id。在B2b小程序中下单的退款单 id |
| payee\_type | string | 是 | 退款分账方类型。同添加分账方时填入的内容 |
| payee\_id | string | 是 | 退款分账方 id。同添加分账方时填入的内容 |
| mchid | string | 是 | 商户号 id。发起这笔订单的商户号 |
| refund\_amt | number | 是 | 退款金额。退款金额，单位为分 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**4. 注意事项**

| 订单分账状态 | 申请退款金额 | 退款前提 | 退款出款账户 |
| --- | --- | --- | --- |
| 订单标记为需要分账 | 申请全额退款 | 1、需要先调“完成分账”接口，将订单剩余冻结资金从“待结算金额”账户全部解冻至“可提现金额”账户  2、“可提现金额”账户余额≥申请退款金额，支付单扣除手续费将在退款成功后返还 | “可提现金额”账户 |
|  | 申请部分退款 | 当申请退款金额≤订单未分账冻结金额，直接可退 | “待结算金额”账户 |
|  |  | 1、当申请退款金额＞订单未分账冻结金额，需要先调“完成分账”接口，将订单剩余冻结资金从“待结算金额”账户全部解冻至“可提现金额”账户   2、“可提现金额”账户余额≥申请退款金额，支付单扣除手续费将在退款成功后返还 | “可提现金额”账户 |
| 订单已完结分账 | 申请全额/部分退款 | “可提现金额”账户余额≥申请退款金额，支付单扣除手续费将在退款成功后返还 | “可提现金额”账户 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 10044 | 分账回退金额超过分账时金额 |
| 10045 | 该退款单已发起过第三方分账回退 |

---

### 查询分账回退结果

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_queryrefundprofitsharingorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| pay\_sig | string | 是 | pay\_sig | 支付签名 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| out\_trade\_no | string | 是 | 订单 id。在B2b小程序中下单后返回的订单 id |
| out\_refund\_no | string | 是 | 退款单 id。在B2b小程序中下单后返回的退款单 id |
| mchid | string | 是 | 商户号 id。发起这笔订单的商户号 |
| payee\_type | string | 是 | 退款分账方类型。同添加分账方时填入的内容 |
| payee\_id | string | 是 | 退款分账方 id。同添加分账方时填入的内容 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| errcode | number | [错误码](#apierrcode) | - |
| errmsg | string | [错误信息](#apierrcode) | - |
| order\_status | number | 订单状态 | [枚举值](#Enum_Res__order_status) |

**Res.order_status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 分账退回中 |
| 2 | 分账退回完成 |
| 3 | 分账退回失败 |

---

<!-- pages: 34 -->
