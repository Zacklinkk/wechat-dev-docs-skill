# 小程序服务端 API 结构化参考 — API/sec-center

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 文本内容安全识别

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/sec-center/sec-check/api_msgseccheck.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | string | 是 | 需检测的文本内容，文本字数的上限为2500字，需使用UTF-8编码 |
| version | number | 是 | 接口版本号，2.0版本为固定值2 |
| scene | number | 是 | 场景枚举值（1 资料；2 评论；3 论坛；4 社交日志） |
| openid | string | 是 | 用户的openid（用户需在近两小时访问过小程序） |
| title | string | 否 | 文本标题，需使用UTF-8编码 |
| nickname | string | 否 | 用户昵称，需使用UTF-8编码 |
| signature | string | 否 | 个性签名，该参数仅在资料类场景有效(scene=1)，需使用UTF-8编码 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| detail | [objarray](#Res__detail<Array>) | 详细检测结果 |
| trace\_id | string | 唯一请求标识，标记单次请求 |
| result | [object](#Res__result) | 综合结果 |

**Res.detail(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| strategy | string | 策略类型 |
| errcode | number | 错误码，仅当该值为0时，该项结果有效 |
| suggest | string | 建议，有risky、pass、review三种值 |
| label | number | 命中标签枚举值，100 正常；10001 广告；20001 时政；20002 色情；20003 辱骂；20006 违法犯罪；20008 欺诈；20012 低俗；20013 版权；21000 其他 |
| keyword | string | 命中的自定义关键词 |
| prob | number | 0-100，代表置信度，越高代表越有可能属于当前返回的标签（label） |

**Res.result Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| suggest | string | 建议，有risky、pass、review三种值 |
| label | number | 命中标签枚举值，100 正常；10001 广告；20001 时政；20002 色情；20003 辱骂；20006 违法犯罪；20008 欺诈；20012 低俗；20013 版权；21000 其他 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | access\_token 无效或不为最新获取的 access\_token，请开发者确认access\_token的有效性 |
| 40003 | invalid openid | 不合法的 OpenID ，请开发者确认 OpenID 的有效性 |
| 40129 | invalid scene | 场景值错误（目前支持场景 1 资料；2 评论；3 论坛；4 社交日志） |
| 43002 | require POST method | 方法调用错误，请用 post 方法调用 |
| 43104 | The openid does not match the appid | appid与 openid 不匹配 |
| 44002 | empty post data | POST 的数据包为空。post请求body参数不能为空。 |
| 44991 | reach max api minute frequence | 超出接口每分钟调用限制 |
| 45009 | reach max api daily quota limit | 超出接口每日调用限制 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 61010 | code is expired | 用户访问记录超时（用户未在近两小时访问小程序） |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 多媒体内容安全识别

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/sec-center/sec-check/api_mediacheckasync.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| media\_url | string | 是 | 要检测的图片或音频的url，支持图片格式包括jpg, jpeg, png, bmp, gif（取首帧），支持的音频格式包括mp3, aac, ac3, wma, flac, vorbis, opus, wav |
| media\_type | number | 是 | 1:音频;2:图片 |
| version | number | 是 | 接口版本号，2.0版本为固定值2 |
| scene | number | 是 | 场景枚举值（1 资料；2 评论；3 论坛；4 社交日志） |
| openid | string | 是 | 用户的openid（用户需在近两小时访问过小程序） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| trace\_id | string | 唯一请求标识，标记单次请求，用于匹配异步推送结果 |

**4. 注意事项**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 小程序的username |
| FromUserName | string | 平台推送服务UserName |
| CreateTime | number | 发送时间 |
| MsgType | string | 默认为：event |
| Event | string | 默认为：wxa\_media\_check |
| appid | string | 小程序的appid |
| trace\_id | string | 任务id |
| version | number | 可用于区分接口版本 |
| errcode | number | 错误码，仅当该值为0时，结果有效。该值为-1008时表示下载错误，请检查媒体链接是否有效。 |
| result | object | 综合结果 |
| detail | array | 详细检测结果 |

**4. 注意事项**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| suggest | string | 建议，有risky、pass、review三种值 |
| label | number | 命中标签枚举值，100 正常；20001 时政；20002 色情；20006 违法犯罪；21000 其他 |

**4. 注意事项**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| strategy | string | 策略类型 |
| errcode | number | 错误码，仅当该值为0时，该项结果有效 |
| suggest | string | 建议，有risky、pass、review三种值 |
| label | number | 命中标签枚举值，100 正常；20001 时政；20002 色情；20006 违法犯罪；21000 其他 |
| prob | number | 0-100，代表置信度，越高代表越有可能属于当前返回的标签（label） |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | access\_token 无效或不为最新获取的 access\_token，请开发者确认access\_token的有效性 |
| 40003 | invalid openid | 不合法的 OpenID ，请开发者确认 OpenID 的有效性 |
| 40004 | invalid media type | media type错误（目前支持多媒体类型 1 音频；2 图片） |
| 43104 | The openid does not match the appid | appid与 openid 不匹配 |
| 44991 | reach max api minute frequence | 超出接口每分钟调用限制 |
| 45009 | reach max api daily quota limit | 超出接口每日调用限制 |
| 61010 | code is expired | 用户访问记录超时（用户未在近两小时访问小程序） |
| 87020 | repeat request limit exceeded | 重复请求超出接口调用限制 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取用户安全等级

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/sec-center/safety-control-capability/api_getuserriskrank.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appid | string | 是 | 小程序appid |
| openid | string | 是 | 用户的openid |
| scene | number | 是 | 场景值，0:注册，1:营销作弊, 2:UGC |
| mobile\_no | string | 否 | 用户手机号 |
| client\_ip | string | 是 | 用户访问源ip |
| email\_address | string | 否 | 用户邮箱地址 |
| extended\_info | string | 否 | 额外补充信息 |
| is\_test | boolean | 否 | 默认值false。false：正式调用，true：测试调用 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| risk\_rank | number | 用户风险等级，合法值为0,1,2,3,4，数字越大风险越高。 |
| unoin\_id | number | 唯一请求标识，标记单次请求 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | access\_token 无效或不为最新获取的 access\_token，请开发者确认access\_token的有效性 |
| 40003 | invalid openid | 不合法的 OpenID ，请开发者确认 OpenID 的有效性 |
| 40129 | invalid scene | 场景值错误（目前支持场景 0 注册；1 营销作弊；2 UGC） |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 43002 | require POST method | 方法调用错误，请用 post 方法调用 |
| 43104 | The openid does not match the appid | appid与 openid 不匹配 |
| 44002 | empty post data | POST 的数据包为空。post请求body参数不能为空。 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;参数需以 JSON 字符串格式写在post请求的 body 中，请检查修正后重试 |
| 48001 | api unauthorized | 小程序无该 api 权限，可在mp.weixin.qq.com开通接口权限 |
| 61007 | api is unauthorized to component | 小程序尚未将对应的权限集授权给第三方平台 |
| 61010 | code is expired | 用户访问记录超时（用户未在近两小时访问小程序） |
| 61080 | the service of getuserriskrank is unavailable now | 当前用户安全服务不可用 |
| 61081 | get riskrank too frequently | 用户安全接口调用过于频繁 |
| 9410009 | the quota is not enough;please apply again! | 测试额度已耗尽 |

---

<!-- pages: 3 -->
