# 小程序服务端 API 结构化参考 — API/operation

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 查询域名配置

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/operation/api_getdomaininfo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | string | 否 | 查询配置域名的类型, 可选值如下： 1. getbizdomain 返回业务域名 2. getserverdomain 返回服务器域名 3. 不指明返回全部 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| requestdomain | array | request合法域名列表 |
| wsrequestdomain | array | socket合法域名列表 |
| uploaddomain | array | uploadFile合法域名列表 |
| downloaddomain | array | downloadFile合法域名列表 |
| udpdomain | array | udp合法域名列表 |
| bizdomain | array | 业务域名列表 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取性能数据

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/operation/api_getperformance.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cost\_time\_type | number | 是 | 可选值 1（启动总耗时）， 2（下载耗时），3（初次渲染耗时） |
| default\_start\_time | number | 是 | 查询开始时间 |
| default\_end\_time | number | 是 | 查询结束时间 |
| device | string | 是 | 系统平台，可选值 "@\_all:"（全部），1（IOS）， 2（android） |
| is\_download\_code | string | 是 | 是否下载代码包，当 type 为 1 的时候才生效，可选值 "@\_all:"（全部），1（是）， 2（否） |
| scene | string | 是 | 访问来源，当 type 为 1 或者 2 的时候才生效，通过 getSceneList 接口获取 |
| networktype | string | 是 | 网络环境, 当 type 为 2 的时候才生效，可选值 "@\_all:"，wifi, 4g, 3g, 2g |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| default\_time\_data | string | 错误查询数据(json字符串，结构如下所述的 strbody) |
| compare\_time\_data | string | 比较数据 |

**4. 注意事项**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| ref\_date | string | 日期 |
| cost\_time\_type | number | 意思同参数里面的 cost\_time\_type |
| cost\_time | number | 耗时(毫秒) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取访问来源

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/operation/api_getscenelist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| scene | [objarray](#Res__scene<Array>) | 访问来源 |

**Res.scene(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| name | string | 来源中文名 |
| value | string | number |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 507010 | 没有发布的小程序不能使用告警功能 |  |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取客户端版本

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/operation/api_getversionlist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| cvlist | [objarray](#Res__cvlist<Array>) | 版本列表 |

**Res.cvlist(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| type | number | 查询类型 1 代表客户端，2 代表服务直达 |
| client\_version\_list | array | 版本列表 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 查询实时日志

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/operation/api_realtimelogsearch.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| date | string | 是 | YYYYMMDD格式的日期，仅支持最近7天 |
| begintime | number | 是 | 开始时间，必须是 date 指定日期的时间 |
| endtime | number | 是 | 结束时间，必须是 date 指定日期的时间 |
| start | number | 否 | 开始返回的数据下标，用作分页，默认为0 |
| limit | number | 否 | 返回的数据条数，用作分页，默认为20 |
| traceId | string | 否 | 小程序启动的唯一ID，按 TraceId 查询会展示该次小程序启动过程的所有页面的日志。 |
| url | string | 否 | 小程序页面路径，例如pages/index/index |
| id | string | 否 | 用户微信号或者OpenId |
| filterMsg | string | 否 | 开发者通过setFileterMsg/addFilterMsg指定的 filterMsg 字段 |
| level | number | 否 | 日志等级，返回大于等于 level 等级的日志，level的定义为2（Info）、4（Warn）、8（Error），如果指定为4，则返回大于等于4的日志，即返回 Warn 和Error日志 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| data | [object](#Res__data) | 返回的日志数据和日志条数总量 |

**Res.data Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| list | [objarray](#Res__data__list<Array>) | 返回的日志数据列表 |
| total | number | 日志条数总量 |

**Res.data.list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| level | number | 日志等级，是 msg 数组里面的所有 level 字段的或操作得到的结果。例如 msg 数组里有两条日志，Info（值为2）和Warn（值为4），则 level 值为6 |
| libraryVersion | string | 基础库版本 |
| clientVersion | string | 客户端版本 |
| id | string | 微信用户OpenID |
| timestamp | number | 打日志的 Unix 时间戳 |
| platform | number | 1 安卓 2 IOS |
| url | string | 小程序页面链接 |
| msg | [objarray](#Res__data__list<Array>__msg<Array>) | 日志内容数组，log.info等的内容存在这里 |
| traceid | string | 小程序启动的唯一ID，按 TraceId 查询会展示该次小程序启动过程的所有页面的日志 |
| filterMsg | string | filterMsg |

**Res.data.list(Array).msgObject Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| time | number | log.info调用的时间 |
| msg | array | log.info调用的内容，每个参数分别是数组的一项 |
| level | number | log.info调用的日志等级 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 200002 | 参数错误，date、begintime、endtime必填。date只能是最近三天的日期，endtime必须大于begintime |  |
| 200007 | 无权限 |  |
| 200010 | 操作过于频繁，目前限制每分钟50次 |  |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取用户反馈列表

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/operation/api_getfeedback.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| type | number | 否 | 反馈类型，默认拉取全部类型，详细定义见下面 |
| page | number | 是 | 分页的页数，从1开始 |
| num | number | 是 | 分页拉取的数据数量 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| list | [objarray](#Res__list<Array>) | 反馈列表 |
| total\_num | number | 总条数 |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| record\_id | number | record\_id |
| create\_time | number | 创建时间 |
| content | string | content |
| phone | string | 联系方式：手机或邮箱 |
| openid | string | openid |
| nickname | string | 反馈用户昵称 |
| head\_url | string | 反馈用户头像 |
| type | number | type |
| mediaIds | array | 图片实体id |

**反馈类型 type 的定义**

| 值 | 说明 |
| --- | --- |
| 1 | 无法打开小程序 |
| 2 | 小程序闪退 |
| 3 | 卡顿 |
| 4 | 黑屏白屏 |
| 5 | 死机 |
| 6 | 界面错位 |
| 7 | 界面加载慢 |
| 8 | 其他异常 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取mediaId图片

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/operation/api_getfeedbackmedia.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| record\_id | number | 是 | 用户反馈信息的 record\_id, 可通过 [getFeedback](api_getfeedback) 获取 |
| media\_id | string | 是 | 图片的 mediaId |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | 错误码。如果成功，则直接返回图片实体，不返回errcode |
| errmsg | string | 错误信息。如果成功，则直接返回图片实体，不返回errsmg |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 46001 | 不存在 mediaid 对应的数据 | 开发者自查 mediaid 是否正确 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 查询js错误详情

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/operation/api_getjserrdetail.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startTime | string | 是 | 开始时间， 格式 "xxxx-xx-xx" |
| endTime | string | 是 | 结束时间，格式 “xxxx-xx-xx” |
| errorMsgMd5 | string | 是 | 错误信息的md5 |
| errorStackMd5 | string | 是 | errorStack的Md5信息 |
| appVersion | string | 是 | 小程序版本 "0"代表全部， 例如：“2.0.18” |
| sdkVersion | string | 是 | 基础库版本 "0"表示所有版本，例如 "2.14.1" |
| osName | string | 是 | 系统类型 "0"【全部】，"1" 【安卓】，"2" 【IOS】，"3"【其他】 |
| clientVersion | string | 是 | 客户端版本 "0"表示所有版本， 例如 "7.0.22" |
| openid | string | 是 | 发生错误的用户 openId |
| offset | number | 是 | 分页起始值 |
| limit | number | 是 | 一次拉取最大值 |
| desc | string | 是 | 排序规则 "0" 升序, "1" 降序 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| data | [objarray](#Res__data<Array>) | 错误列表 |
| totalCount | number | 总条数 |

**Res.data(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Count | string | 数量 |
| sdkVersion | string | sdkVersion |
| ClientVersion | string | ClientVersion |
| errorStackMd5 | string | errorStackMd5 |
| TimeStamp | string | 时间戳 |
| appVersion | string | appVersion |
| errorMsgMd5 | string | errorMsgMd5 |
| errorMsg | string | errorMsg |
| errorStack | string | errorStack |
| Ds | string | 日期 |
| OsName | string | OsName |
| openId | string | openId |
| pluginversion | string | pluginversion |
| appId | string | appId |
| DeviceModel | string | DeviceModel |
| source | string | source |
| route | string | route |
| nickname | string | 昵称 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -3 | 系统繁忙 | 请稍后再试 |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 查询错误列表

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/operation/api_getjserrlist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appVersion | string | 是 | 小程序版本 "0"代表全部， 例如：“2.0.18” |
| errType | string | 是 | 错误类型 "0"【全部】，"1"【业务代码错误】，"2"【插件错误】，"3"【系统框架错误】 |
| startTime | string | 是 | 开始时间， 格式 "xxxx-xx-xx" |
| endTime | string | 是 | 结束时间，格式 “xxxx-xx-xx” |
| keyword | string | 是 | 从错误中搜索关键词，关键词过滤 |
| openid | string | 是 | 发生错误的用户 openId |
| orderby | string | 是 | 排序字段 "uv", "pv" 二选一 |
| desc | string | 是 | 排序规则 "1" orderby字段降序，"2" orderby字段升序 |
| offset | number | 是 | 分页起始值 |
| limit | number | 是 | 一次拉取最大值， 最大 30 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| data | [objarray](#Res__data<Array>) | 错误列表 |
| totalCount | number | 总条数 |

**Res.data(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errorMsgMd5 | string | errorMsgMd5 |
| errorMsg | string | errorMsg |
| uv | number | uv |
| pv | number | pv |
| errorStackMd5 | string | errorStackMd5 |
| errorStack | string | errorStack |
| pvPercent | string | pvPercent |
| uvPercent | string | uvPercent |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 20011 | 频率限制 | 请稍后再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取分阶段发布详情

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/operation/api_getgrayreleaseplan.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | 错误时间 |
| gray\_release\_plan | [object](#Res__gray_release_plan) | 分阶段发布计划详情 |

**Res.gray_release_plan Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| status | number | 0:初始状态 1:执行中 2:暂停中 3:执行完毕 4:被删除 |
| create\_timestamp | number | 分阶段发布计划的创建时间 |
| gray\_percentage | number | 当前的灰度比例 |
| support\_debuger\_first | boolean | true表示支持按项目成员灰度 |
| support\_experiencer\_first | boolean | true表示支持按体验成员灰度 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

---

<!-- pages: 10 -->
