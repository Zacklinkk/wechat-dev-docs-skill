# 小程序服务端 API 结构化参考 — API/mp-access-token

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 获取接口调用凭据

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-access-token/api_getaccesstoken.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| appid | string | 是 | AppID | 账号的唯一凭证，即 AppID，点此查看[如何获取Appid](https://developers.weixin.qq.com/doc/oplatform/developers/dev/appid) |
| secret | string | 是 | AppSecret | 唯一凭证密钥，即 AppSecret，点此查看[如何获取AppSecret](https://developers.weixin.qq.com/doc/oplatform/developers/dev/appid) |
| grant\_type | string | 是 | client\_credential | 填写 client\_credential |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| access\_token | string | 获取到的凭证 |
| expires\_in | number | 凭证有效时间，单位：秒。目前是7200秒之内的值。 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40002 | invalid grant\_type | 不合法的凭证类型 |
| 40013 | invalid appid | 不合法的 AppID ，请开发者检查 AppID 的正确性，避免异常字符，注意大小写 |
| 40125 | 不合法的 secret | 请检查 secret 的正确性，避免异常字符，注意大小写 |
| 40164 | 调用接口的IP地址不在白名单中 | 请在接口IP白名单中进行设置 |
| 40243 | AppSecret已被冻结，请解冻后再次调用。 | 点此查看[如何解冻AppSecret](https://developers.weixin.qq.com/doc/oplatform/developers/dev/appid) |
| 41004 | appsecret missing | 缺少 secret 参数 |
| 50004 | 禁止使用 token 接口 |  |
| 50007 | 账号已冻结 |  |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 | 微信小店 | 联盟带货机构 | 带货助手 | 小店供货商 | 移动应用 | 网站应用 | 视频号助手 | 多端应用 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |

---

### 获取稳定版接口调用凭据

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-access-token/api_getstableaccesstoken.html

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| grant\_type | string | 是 | 填写 client\_credential |
| appid | string | 是 | 账号的唯一凭证，即 AppID，点此查看[如何获取Appid](https://developers.weixin.qq.com/doc/oplatform/developers/dev/appid.html) |
| secret | string | 是 | 唯一凭证密钥，即 AppSecret，点此查看[如何获取AppSecret](https://developers.weixin.qq.com/doc/oplatform/developers/dev/appid.html) |
| force\_refresh | boolean | 否 | 默认使用 false。1. force\_refresh = false 时为普通调用模式，access\_token 有效期内重复调用该接口不会更新 access\_token；2. 当force\_refresh = true 时为强制刷新模式，会导致上次获取的 access\_token 失效，并返回新的 access\_token |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| access\_token | string | 获取到的凭证 |
| expires\_in | number | 凭证有效时间，单位：秒。目前是7200秒之内的值。 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 0 | ok | ok |
| 40002 | invalid grant\_type | 不合法的凭证类型 |
| 40013 | invalid appid | 不合法的 AppID ，请开发者检查 AppID 的正确性，避免异常字符，注意大小写 |
| 40125 | invalid appsecret | 无效的appsecret，请检查appsecret的正确性 |
| 40164 | invalid ip  not in whitelist | 将ip添加到ip白名单列表即可 |
| 41002 | appid missing | 缺少 appid 参数 |
| 41004 | appsecret missing | 缺少 secret 参数 |
| 43002 | require POST method | 需要 POST 请求 |
| 45009 | reach max api daily quota limit | 调用超过天级别频率限制。可调用clear\_quota接口恢复调用额度。 |
| 45011 | api minute-quota reach limit  mustslower  retry next minute | API 调用太频繁，请稍候再试 |
| 89503 | 此次调用需要管理员确认，请耐心等候 |  |
| 89506 | 该IP调用求请求已被公众号管理员拒绝，请24小时后再试，建议调用前与管理员沟通确认 |  |
| 89507 | 该IP调用求请求已被公众号管理员拒绝，请1小时后再试，建议调用前与管理员沟通确认 |  |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 | 微信小店 | 联盟带货机构 | 带货助手 | 小店供货商 | 移动应用 | 网站应用 | 视频号助手 | 多端应用 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |

---

<!-- pages: 2 -->
