# 小程序服务端 API 结构化参考 — API/cityservice

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 获取城市服务限定页面链接

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cityservice/basic/api_cityserviceservicehomepath.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| page\_type | number | 是 | 获取城市服务路径类型 | [枚举值](#Enum_Body__page_type) |
| src\_channel | number | 是 | 跳转来源渠道 | [枚举值](#Enum_Body__src_channel) |
| need\_path\_type | number | 否 | 获取h5 URL需填写1（OpenSDK不需要填写） | - |
| device\_type | number | 否 | 获取h5 URL需填写2（OpenSDK不需要填写） | - |
| city\_name | string | 否 | 城市名称，page\_type为1、3、5时必填（城市名称以地级市为准） | - |
| content\_name | string | 否 | 专题页名称，page\_type为3时必填 | - |
| ext\_params | [objarray](#Body__ext_params<Array>) | 否 | 附加参数，包括关键字等其他参数，page\_type为5时必填 | - |
| service\_id | number | 否 | 服务id，page\_type为0时必填 | - |
| params | string | 否 | 透传参数，page\_type为0时必填 必须为一个json数组，每个object包括两个成员key和value。key的值是透传的字段名,value的值是透传参数的值。 例如，[{\"key\":\"type\",\"value\":\"11\"}]表示将type=11通过城市服务主页透传到第三方。 限制：透传参数个数最多为10个;key和value的值必须为字符串;key的值不能重复。key=city,表示用户所在城市,如广州. | - |
| city\_id | string | 否 | 用户所在城市id(需与腾讯内部要是同一套编码)，page\_type为0时可传 | - |

**Body.ext_params(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 关键字的key名称置顶位keyword |
| value | string | 是 | 服务列表名称（以城市服务的标签名称为准） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |
| path | string | 结果路径 |
| business\_type | string | 类型 |
| app\_id | string | 小程序 id，page\_type为5时返回 |
| username | string | 原始id，page\_type为5时返回 |
| query\_string | string | path的参数，page\_type为0时返回 |

**Body.page_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 服务主页 |
| 1 | 首页 |
| 3 | 专题页 |
| 5 | 服务列表页 |

**Body.src_channel Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 公众号 |
| 1 | 小程序 |
| 2 | 短信 |
| 3 | 其他 |
| 5 | 厂商 |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 83200 | no exist service |

---

### 消息通路发消息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cityservice/basic/api_cityservice_sendmsgdata.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户唯一标识 |
| biz\_template\_id | string | 是 | 城市服务分配给公众号的模板id |
| result\_page\_style\_id | string | 否 | 结果页样式id，含结果页必填 |
| deal\_msg\_style\_id | string | 否 | 办事记录样式id，含办事记录必填 |
| card\_style\_id | string | 否 | 页卡样式id，含页卡必填 |
| order\_no | string | 是 | 订单号，同一订单号的办事记录会合并 |
| url | string | 否 | 跳转链接，用于服务通知、结果页、待办提醒，。含结果页必填 |
| data | [object](#Body__data) | 是 | 模板json数据，对象信息请按照模板要求，其中color字段只对服务通知有效。如为数组时可用[ ]括起字段内数据。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| result\_page\_url | string | 需跳转至该url，替代原有的服务结果页面。如未传入result\_page\_style\_id，则调用后result\_page\_url返回为空。 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**4. 注意事项**

| 提示信息 | 说明 |
| --- | --- |
| 中文显示错误 | 字符集未用utf8 |
| 参数错误 | json参数错误 |
| 非本人，页面打开失败 | 非本人openid；或登录态获取失败 |
| 请在微信内打开 | 需在微信内打开页面 |
| 系统错误 | 其他错误 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 40097 | 1.参数错误。2.或openid不来自有“消息通路”api权限的公众号 |
| 48001 | api未授权 |
| 82020 | 未关注公众号的用户，从未在城市服务访问过服务 |
| 82021 | 未关注公众号的用户，未在近30天内通过城市服务访问服务 |
| 82022 | 未关注公众号的用户，通过城市服务访问服务后，30天内被下发数超过10次（医疗行业超过20次） |
| 82023 | 未关注公众号的用户，1个小时内被下发次数超过5次 |
| 82024 | order\_no异常，例如所有用户的业务订单号都用同一个 |
| 82025 | URL无效 |
| 82026 | 1.服务已下线。2.或服务在审核中且审核期超过了30天 |

---

### 校验实名信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cityservice/basic/api_checkrealnameinfo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户在业务方下的openid，与申请权限时提供的业务方的小程序appid保持一致 |
| real\_name | string | 是 | 需要校验的姓名 |
| cred\_id | string | 是 | 需要校验的证件号 |
| cred\_type | string | 是 | 默认为1，即身份证，目前暂只支持身份证 |
| code | string | 是 | 通过小程序回跳获取的code参数 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| errcode | number | [错误码](#apierrcode) | - |
| errmsg | string | [错误描述](#apierrcode) | - |
| verify\_openid | string | openid 验证结果，有多个结果时用分号;连接 | [枚举值](#Enum_Res__verify_openid) |
| verify\_real\_name | string | real\_name 校验结果，当verify\_openid 为V\_OP\_NM\_MA 时返回 | [枚举值](#Enum_Res__verify_real_name) |

**Res.verify_openid Enum**

| 枚举值 | 描述 |
| --- | --- |
| V\_OP\_NA | 用户暂未实名认证 |
| V\_OP\_NM\_MA | 用户与姓名匹配 |
| V\_OP\_NM\_UM | 用户与姓名不匹配 |

**Res.verify_real_name Enum**

| 枚举值 | 描述 |
| --- | --- |
| V\_NM\_ID\_MA | 姓名与证件号匹配 |
| V\_NM\_ID\_UM | 姓名与证件号不匹配 |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 1005 | invalid appid |
| 80111 | 实名校验code不存在 |
| 80113 | 无效code |

---

### 仿原生跳转

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cityservice/basic/api_transportcode_getbusinessview.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| path\_type | number | 是 | 需要跳转的页面 | [枚举值](#Enum_Body__path_type) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |
| business\_type | string | 业务类型 |
| query\_string | string | 调用仿原生小程序时使用的参数 |
| expire\_at | number | 返回 query\_string 的到期时间（uinx时间戳） |

**Body.path_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 新用户首页/欢迎页（开通乘车码，包含“成功开通乘车码” |
| 1 | 乘车码页 |
| 2 | 已开通路线 |
| 3 | 个人中心 |
| 4 | 我的乘车记录 |
| 5 | 帮助 |
| 6 | 欠费记录 |

---

### 消息推送接口

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cityservice/medicalassistant/api_cityservice_sendchannelmsg.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| status | number | 是 | 1501001 | 消息子状态(如：1501001-预约挂号成功通知) |
| open\_id | string | 是 | osdjkfhsdlkfjhdslkjfh | 用户openid(公众号/小程序) |
| order\_id | string | 是 | order\_123456 | 业务方生成的唯一订单ID |
| msg\_id | string | 是 | msg\_0001 | 消息唯一标识(需保证同用户同order\_id下唯一) |
| app\_id | string | 是 | wx23dde3xd34569cba | 公众号appid(需开通就医助手) |
| business\_id | number | 是 | 150 | 固定值150 |
| business\_info | [object](#Body__business_info) | 否 |  | 业务字段(不同status对应不同结构) |

**Body.business_info Object Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| pat\_hospital\_id | string | 是 | - | 用户在该医院就诊卡号 |
| pat\_name | string | 是 | - | 用户姓名 |
| doc\_name | string | 否 | - | 医生姓名，如果暂无具体分配的医生，则填医生级别（如主治医生） |
| department\_name | string | 是 | - | 科室名称，含楼栋楼层（如果有） |
| department\_location | string | 否 | - | 科室位置 |
| appointment\_time | string | 是 | 2023-06-07 10:30-11:00 | 预约时间 |
| memo | string | 否 | - | 就医须知 |
| redirect\_page | [object](#Body__business_info__redirect_page) | 否 | - | 医院跳转页面信息 |
| elder\_redirect\_page | [object](#Body__business_info__redirect_page) | 否 | - | 医院适老化页面的跳转信息 |

**Body.business_info.redirect_page Object Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| page\_type | string | 否 | 页面路径类型，如果有redirect\_page字段需要填，则必填page\_type; 否则不用填 | [枚举值](#Enum_Body__business_info__redirect_page__page_type) |
| url | string | 否 | 网页网址，page\_type为web类型时必填，url需为业务域名 | - |
| app\_id | string | 否 | 小程序appid，page\_type为小程序时必填，小程序类型时需与当前账号关联主体 | - |
| fullpath | string | 否 | 小程序路径，page\_type为小程序时必填 | - |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**Body.business_info.redirect_page.page_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| web | 网页 |
| mini\_program | 小程序 |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok | 成功 |
| 40001 | invalid credential | 不合法的access\_token |

---

### 查询用户实名API

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cityservice/elderMedical/api_cityservice_getmedrealname.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| app\_id | string | 是 | 业务方appid |
| open\_id | string | 是 | 微信用户openid |
| wxmed\_authcode | string | 是 | 实名信息code，对应url中的wxmed\_authcode，有效期10分钟 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| cipher\_real\_name | string | 加密后的实名信息，base64后的加密信息 |
| cipher\_algorithm | string | 加密算法，默认：AES\_256\_ECB\_PKCS7Padding |
| key\_version | number | 实名信息加密key版本号，初始版本号为0，用于识别后续密钥更换升级 |
| app\_id | string | 业务方appid |
| open\_id | string | 微信用户openid |

**4. 注意事项**

| 字段 | 字段名 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- | --- |
| real\_name | 姓名 | string | 是 |  |
| id\_card\_no | 证件号 | string | 是 |  |
| id\_card\_type | 证件类型 | int32 | 是 | 1 居民身份证； 4 澳门居民往来内地通行证； 5 台湾居民往来内地通行证； 6香港居民往来内地通行证。 |
| phone | 电话号码 | string | 是 |  |
| timestamp | 时间戳 | int64 | 是 |  |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok | ok |
| 11200 | wxmed\_authcode expired |  |

---

### 查询用户是否开通

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cityservice/elderMedical/api_cityservice_getmsgrelation.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| business\_id | string | 是 | 130 | 业务id，长辈就医业务填130 |
| open\_id | string | 是 | - | 微信用户openid |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| errcode | number | 返回码 | - |
| errmsg | string | 返回说明 | - |
| is\_subscribed | boolean | 是否订阅 | [枚举值](#Enum_Res__is_subscribed) |

**Res.is_subscribed Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 已开通 |
| 0 | 未开通 |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok | ok |

---

### 查询所有公告

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cityservice/elderMedical/api_intp_eldermed_gethospnoticelist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| app\_id | string | 是 | 业务方公众号的appid | - |
| notice\_type | number | 是 | 公告类型 | [枚举值](#Enum_Body__notice_type) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| notice\_list | [objarray](#Res__notice_list<Array>) | 公告列表 |
| preview\_openid | array | 可以预览草稿的用户 openid |

**Res.notice_list(Array) Object Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| notice\_id | number | 公告ID | - |
| content | string | 公告内容 | - |
| status | string | 公告状态 | [枚举值](#Enum_Res__notice_list<Array>__status) |

**Body.notice_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 挂号前的就医须知 |
| 2 | 来院须知 |

**Res.notice_list(Array).status Enum**

| 枚举值 | 描述 |
| --- | --- |
| DRAFT | 草稿 |
| PUBLIC | 发布 |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok | ok |

---

### 公告草稿预览设置

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cityservice/elderMedical/api_previewhopsnotice.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| app\_id | string | 是 | 业务方公众号的appid | - |
| notice\_type | number | 是 | 公告类型 | [枚举值](#Enum_Body__notice_type) |
| notice\_id | string | 是 | 公告ID | - |
| preview\_username | string | 是 | 可以预览公告的微信号 | - |
| operation | number | 是 | 操作类型 | [枚举值](#Enum_Body__operation) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| notice\_id | number | 草稿ID |

**Body.notice_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 挂号前的就医须知 |
| 2 | 来院须知 |

**Body.operation Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 删除预览权限 |
| 2 | 添加预览权限 |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok | ok |

---

### 正式发布公告

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cityservice/elderMedical/api_intp_eldermed_publichopsnotice.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| app\_id | string | 是 | 业务方公众号的appid | - |
| notice\_type | number | 是 | 公告类型 | [枚举值](#Enum_Body__notice_type) |
| notice\_id | number | 是 | 公告ID | - |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| notice\_id | number | 公告ID |

**Body.notice_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 挂号前的就医须知 |
| 2 | 来院须知 |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | OK | OK |

---

### 添加公告草稿

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/cityservice/elderMedical/api_sethopsnotice.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| app\_id | string | 是 | 业务方公众号的appid | - |
| notice\_type | number | 是 | 公告类型 | [枚举值](#Enum_Body__notice_type) |
| notice\_content | string | 是 | 公告内容，长度限制3000个字符，\*\*支持富文本\*\*，图片用标签的方式嵌入富文本内，具体可看下文 | - |
| notice\_id | number | 否 | 公告ID，不传notice\_id则新增一条草稿，传notice\_id不新增，会覆盖指定草稿的内容 | - |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| notice\_id | number | 草稿ID |

**Body.notice_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 挂号前的就医须知 |
| 2 | 来院须知 |

---

<!-- pages: 11 -->
