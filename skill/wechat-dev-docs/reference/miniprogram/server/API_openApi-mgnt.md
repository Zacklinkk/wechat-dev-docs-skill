# 小程序服务端 API 结构化参考 — API/openApi-mgnt

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 查询API调用额度

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/openApi-mgnt/api_getapiquota.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[component\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getcomponentaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cgi\_path | string | 是 | api的请求地址，例如"/cgi-bin/message/custom/send";不要前缀“https://api.weixin.qq.com” ，也不要漏了"/",否则都会76003的报错 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | 返回码 |
| errmsg | string | [错误信息](#apierrcode) |
| quota | [object](#Res__quota) | quota详情 |
| rate\_limit | [object](#Res__rate_limit) | 普通调用频率限制 |
| component\_rate\_limit | [object](#Res__component_rate_limit) | 代调用频率限制 |

**Res.quota Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| daily\_limit | number | 当天该账号可调用该接口的次数 |
| used | number | 当天已经调用的次数 |
| remain | number | 当天剩余调用次数 |

**Res.rate_limit Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| call\_count | number | 周期内可调用数量，单位 次 |
| refresh\_second | number | 更新周期，单位 秒 |

**Res.component_rate_limit Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| call\_count | number | 周期内可调用数量，单位 次 |
| refresh\_second | number | 更新周期，单位 秒 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok | ok |
| 76021 | cgi\_path not found, please check | cgi\_path填错了 |
| 76022 | could not use this cgi\_path，no permission | 当前调用接口使用的token与api所属账号不符，详情可看注意事项的说明 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 | 微信小店 | 联盟带货机构 | 带货助手 | 小店供货商 | 第三方平台 | 移动应用 | 网站应用 | 视频号助手 | 多端应用 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | 〇 | ✔ | ✔ | ✔ | ✔ |

---

### 重置API调用次数

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/openApi-mgnt/api_clearquota.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[component\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getcomponentaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appid | string | 是 | 要被清空的账号的appid |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok | ok |
| 40013 | invalid appid | 不合法的 AppID ，请开发者检查 AppID 的正确性，避免异常字符，注意大小写 |
| 48006 | forbid to clear quota because of reaching the limit | api 禁止清零调用次数，因为清零次数达到上限 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 | 微信小店 | 联盟带货机构 | 带货助手 | 小店供货商 | 第三方平台 | 移动应用 | 网站应用 | 视频号助手 | 多端应用 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | 〇 | ✔ | ✔ | ✔ | ✔ |

---

### 重置指定API调用次数

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/openApi-mgnt/api_clearapiquota.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[component\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getcomponentaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| cgi\_path | string | 是 | /channels/ec/basics/info/get | api的请求地址，cgi\_path 必须以"/channels/ec/"开头，不要前缀"https://api.weixin.qq.com"，也不要漏了"/" |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | access\_token 无效或不为最新获取的 access\_token，请开发者确认access\_token的有效性 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 42001 | access\_token expired | access\_token 超时，请检查 access\_token 的有效期，请参考基础支持 - 获取 access\_token 中，对 access\_token 的详细机制说明 |
| 44002 | empty post data | POST 的数据包为空。post请求body参数不能为空。 |
| 45009 | reach max api daily quota limit | 超出接口每日调用限制 |
| 50002 | user limited | 用户受限，可能是用户帐号被冻结或注销 |
| 76021 | cgi\_path not found, please check | cgi\_path填错了 |
| 76022 | could not use this cgi\_path，no permission | 当前调用接口使用的token与api所属账号不符，详情可看注意事项的说明 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 | 微信小店 | 联盟带货机构 | 带货助手 | 小店供货商 | 第三方平台 | 移动应用 | 网站应用 | 视频号助手 | 多端应用 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | 〇 | ✔ | ✔ | ✔ | ✔ |

---

### 使用AppSecret重置API调用次数

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/openApi-mgnt/api_clearquotabyappsecret.html

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appid | string | 是 | 要被清空的账号的appid |
| appsecret | string | 是 | 唯一凭证密钥，即 AppSecret |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40013 | invalid appid | 不合法的 AppID ，请开发者检查 AppID 的正确性，避免异常字符，注意大小写 |
| 41002 | appid missing | 缺少 appid 参数 |
| 41004 | appsecret missing | 缺少 secret 参数 |
| 48006 | forbid to clear quota because of reaching the limit | api 禁止清零调用次数，因为清零次数达到上限 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 | 微信小店 | 联盟带货机构 | 带货助手 | 小店供货商 | 移动应用 | 网站应用 | 视频号助手 | 多端应用 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |

---

### 查询rid信息

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/openApi-mgnt/api_getridinfo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[component\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getcomponentaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rid | string | 是 | 调用接口报错返回的rid |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | 返回码 |
| errmsg | string | [错误信息](#apierrcode) |
| request | [object](#Res__request) | 该rid对应的请求详情 |

**Res.request Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| invoke\_time | number | 发起请求的时间戳 |
| cost\_in\_ms | number | 请求毫秒级耗时 |
| request\_url | string | 请求的URL参数 |
| request\_body | string | post请求的请求参数 |
| response\_body | string | 接口请求返回参数 |
| client\_ip | string | 接口请求的客户端ip |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok | ok |
| 76001 | rid not found | rid不存在 |
| 76002 | rid is error | rid为空或者格式错误 |
| 76003 | could not query this rid,no permission | 当前账号无权查询该rid，该rid属于其他账号调用所产生 |
| 76004 | rid time is error | rid过期，仅支持持续7天内的rid |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 | 微信小店 | 联盟带货机构 | 带货助手 | 小店供货商 | 第三方平台 | 移动应用 | 网站应用 | 视频号助手 | 多端应用 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | 〇 | ✔ | ✔ | ✔ | ✔ |

---

### 网络通信检测

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/openApi-mgnt/api_callbackcheck.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[component\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getcomponentaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 | 枚举 |
| --- | --- | --- | --- | --- | --- |
| action | string | 是 | all | 检测动作：dns(域名解析)/ping(ping检测)/all(全部) | - |
| check\_operator | string | 是 | DEFAULT | 检测运营商：CHINANET(电信)/UNICOM(联通)/CAP(腾讯)/DEFAULT(自动) | CHINANET UNICOM CAP DEFAULT |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| dns | [objarray](#Res__dns<Array>) | DNS解析结果列表 |
| ping | [objarray](#Res__ping<Array>) | PING检测结果列表 |

**Res.dns(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ip | string | 解析出来的ip |
| real\_operator | string | ip对应的运营商 |

**Res.ping(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ip | string | ping的ip，执行命令为ping ip –c 1-w 1 -q |
| from\_operator | string | ping的源头的运营商，由请求中的check\_operator控制 |
| package\_loss | string | ping的丢包率，0%表示无丢包，100%表示全部丢包。因为目前仅发送一个ping包，因此取值仅有0%或者100%两种可能。 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40201 | invalid url | 未设置回调URL |
| 40202 | invalid action | 不正确的action参数 |
| 40203 | invalid check\_operator | 不正确的运营商参数 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 | 微信小店 | 联盟带货机构 | 带货助手 | 小店供货商 | 第三方平台 | 移动应用 | 网站应用 | 视频号助手 | 多端应用 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | 〇 | ✔ | ✔ | ✔ | ✔ |

---

### 获取微信API服务器IP

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/openApi-mgnt/api_getapidomainip.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[component\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getcomponentaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ip\_list | array | 微信服务器IP地址列表 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40013 | invalid appid | 不合法的 AppID ，请开发者检查 AppID 的正确性，避免异常字符，注意大小写 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 | 微信小店 | 联盟带货机构 | 带货助手 | 小店供货商 | 第三方平台 | 移动应用 | 网站应用 | 视频号助手 | 多端应用 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | 〇 | ✔ | ✔ | ✔ | ✔ |

---

### 获取微信推送服务器IP

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/openApi-mgnt/api_getcallbackip.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[component\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getcomponentaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ip\_list | string | 微信服务器IP地址列表 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40013 | invalid appid | 无效的AppID |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 | 微信小店 | 联盟带货机构 | 带货助手 | 小店供货商 | 第三方平台 | 移动应用 | 网站应用 | 视频号助手 | 多端应用 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | 〇 | ✔ | ✔ | ✔ | ✔ |

---

<!-- pages: 8 -->
