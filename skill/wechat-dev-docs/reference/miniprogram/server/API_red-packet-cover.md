# 小程序服务端 API 结构化参考 — API/red-packet-cover

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 获取微信红包封面

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/red-packet-cover/api_getredpacketcoverurl.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 可领取用户的openid |
| ctoken | string | 是 | 在红包封面平台获取发放ctoken（需要指定可以发放的appid） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |
| data | [object](#Res__data) | 指定用户可以领取的链接（带鉴权的链接） |

**Res.data Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| url | string | 指定用户可以领取的链接（带鉴权的链接） |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 9600001 | 参数缺失 openid |  |
| 9600002 | 参数缺失 ctoken |  |
| 9600003 | 系统错误 |  |
| 9600004 | ctoken 错误 |  |
| 9600005 | openid 错误 |  |
| 9600006 | 小程序不在配置列表中 |  |
| 9600007 | 小程序与openid不对应 |  |

---

<!-- pages: 1 -->
