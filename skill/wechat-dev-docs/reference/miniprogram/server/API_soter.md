# 小程序服务端 API 结构化参考 — API/soter

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 生物认证秘钥签名验证

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/soter/api_verifysignature.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 用户 openid |
| json\_string | string | 是 | 通过 [wx.startSoterAuthentication](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/soter/wx.startSoterAuthentication.html) 成功回调获得的 resultJSON 字段 |
| json\_signature | string | 是 | 通过 [wx.startSoterAuthentication](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/soter/wx.startSoterAuthentication.html) 成功回调获得的 resultJSONSignature 字段 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| is\_ok | boolean | 验证结果 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 |
| --- | --- | --- |
| ✔ | ✔ | ✔ |

---

<!-- pages: 1 -->
