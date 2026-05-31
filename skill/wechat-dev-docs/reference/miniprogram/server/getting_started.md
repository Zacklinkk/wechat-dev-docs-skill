# 小程序服务端 API 结构化参考 — getting_started

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 服务端 API 签名加密指南

微信开放平台的接口通信鉴权体系，使用了数据加密与签名的机制，防止数据泄漏与篡改，且具备不可否认性。开发者可在小程序管理后台API安全模块，为应用配置密钥与公钥，以此来保障开发者应用和微信开放平台交互的安全性。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/getting_started/api_signature.html

**3.1 加密请求**

| 参数 | 类型 | 默认值 | 必填 | 备注 |
| --- | --- | --- | --- | --- |
| iv | string |  | 是 | 初始向量，为16字节base64字符串（解码后为12字节随机字符串） |
| data | string |  | 是 | 加密后的密文，使用base64编码 |
| authtag | string |  | 是 | GCM模式输出的认证信息，使用base64编码 |

**3.1 加密请求**

| 参数 | 说明 |
| --- | --- |
| urlpath | 当前请求API的URL路径，包含URL协议信息，不包括URL参数（URL Query） |
| appid | 当前小程序的Appid |
| timestamp | 加密时的时间戳，需要与HTTP请求头`Wechatmp-TimeStamp`的时间戳一致 |
| sn | 使用的对称密钥编号，需要在MP平台密钥管理页面获取 |

**3.1 加密请求**

| 参数 | 类型 | 默认值 | 必填 | 备注 |
| --- | --- | --- | --- | --- |
| data | 原字段类型 |  | 是 | 原请求字段，包含URL参数、POST参数，不包含AccessToken |
| \_n | string |  | 是 | 随机字符串，推荐使用16-32字节非固定长度随机base64字符串 |
| \_appid | string |  | 是 | 当前小程序的Appid |
| \_timestamp | number |  | 是 | 加密时的时间戳，需要与HTTP请求头`Wechatmp-TimeStamp`的时间戳一致 |

**3.2 加密请求签名**

| HEADER名 | 默认值 | 必填 | 备注 |
| --- | --- | --- | --- |
| Wechatmp-Appid |  | 是 | 当前小程序的Appid |
| Wechatmp-TimeStamp |  | 是 | 签名时时间戳 |
| Wechatmp-Signature |  | 是 | 签名数据，使用base64编码 |

**3.2 加密请求签名**

| 参数 | 说明 |
| --- | --- |
| urlpath | 当前请求API的URL，不包括URL参数（URL Query），需要带HTTP协议头 |
| appid | 当前小程序的Appid |
| timestamp | 签名时的时间戳，即请求头`Wechatmp-TimeStamp`的值 |
| postdata | 当前请求的POST数据 |

**4.1 验签**

| HEADER名 | 默认值 | 必填 | 备注 |
| --- | --- | --- | --- |
| Wechatmp-Appid |  | 是 | 当前小程序的Appid |
| Wechatmp-TimeStamp |  | 是 | 签名时时间戳 |
| Wechatmp-Serial |  | 是 | 平台证书编号，在MP管理页面获取，**非证书内序列号** |
| Wechatmp-Signature |  | 是 | 平台证书签名数据，使用base64编码 |
| Wechatmp-Serial-Deprecated |  | 否 | 即将失效的平台证书编号，**非证书内序列号**，仅在证书更换周期内出现 |
| Wechatmp-Signature-Deprecated |  | 否 | 即将失效的平台证书签名数据，仅在证书更换周期内出现，使用base64编码 |

**4.1 验签**

| 参数 | 说明 |
| --- | --- |
| urlpath | 当前请求API的URL，不包括URL参数（URL Query），需要带HTTP协议头 |
| appid | 当前小程序的Appid |
| timestamp | 签名时的时间戳，即响应头`Wechatmp-TimeStamp`的值 |
| respdata | 当前响应的数据 |

**五、错误码**

| 错误码 | 错误码取值 | 解决方案 |
| --- | --- | --- |
| 40230 | API\_Missing\_Wechatmp\_Serial | 缺少Wechatmp\_Serial |
| 40231 | API\_Missing\_Wechatmp\_Timestamp | 缺少Wechatmp\_Timestamp |
| 40232 | API\_Missing\_Wechatmp\_Signature | 缺少Wechatmp\_Signature |
| 40233 | API\_Missing\_Wechatmp\_Appid | 缺少Wechatmp\_Appid |
| 40234 | API\_Invalid\_Signature | 签名错误 |
| 40235 | API\_Invalid\_Encrypt | 错误的加密 |
| 40236 | API\_Invalid\_Wechatmp\_Appid | 无效的Wechatmp\_Appid |
| 40237 | API\_Invalid\_Wechatmp\_Appidmatch | Wechatmp\_Appid和Token不匹配 |
| 40238 | API\_NoExist\_DevSecretSym | 开发者未设置对称密钥 |
| 40239 | API\_NoExist\_DevSecretAsym | 开发者未设置公钥 |
| 40240 | API\_Expired\_Wechatmp\_Timestamp | 超时的数据 |

---

<!-- pages: 1 -->
