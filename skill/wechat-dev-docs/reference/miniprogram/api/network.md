# 微信小程序 API 结构化参考 — network

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### RequestTask wx.request(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | url | string |  | 是 | 开发者服务器接口地址 |  |
|  | data | string/object/ArrayBuffer |  | 否 | 请求的参数 |  |
|  | header | Object |  | 否 | 设置请求的 header，header 中不能设置 Referer。 `content-type` 默认为 `application/json` |  |
|  | timeout | number |  | 否 | 超时时间，单位为毫秒。默认值为 60000 | [2.10.0](../../../framework/compatibility.html) |
|  | method | string | GET | 否 | HTTP 请求方法 |  |
|  | | 合法值 | 说明 | | --- | --- | | OPTIONS | HTTP 请求 OPTIONS | | GET | HTTP 请求 GET | | HEAD | HTTP 请求 HEAD | | POST | HTTP 请求 POST | | PUT | HTTP 请求 PUT | | DELETE | HTTP 请求 DELETE | | TRACE | HTTP 请求 TRACE | | CONNECT | HTTP 请求 CONNECT | | | | | | |
|  | dataType | string | json | 否 | 返回的数据格式。值为 `json` 时，返回的数据为 JSON，返回后会对返回的数据进行一次 `JSON.parse`；其他值则不对返回的内容进行 `JSON.parse` |  |
|  | responseType | string | text | 否 | 响应的数据类型 | [1.7.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | text | 响应的数据为文本 | | arraybuffer | 响应的数据为 ArrayBuffer | | | | | | |
|  | useHighPerformanceMode | boolean | true | 否 | 使用高性能模式。从基础库 v3.5.0 开始在 Android 端默认开启，其他端暂不生效。该模式下有更优的网络性能表现，更多信息请查看下方说明。 | [3.3.3](../../../framework/compatibility.html) |
|  | enableHttp2 | boolean | false | 否 | 开启 http2 | [2.10.4](../../../framework/compatibility.html) |
|  | enableProfile | boolean | true | 否 | 是否开启 profile。iOS 和 Android 端默认开启，其他端暂不支持。开启后可在接口回调的 res.profile 中查看性能调试信息。 |  |
|  | enableQuic | boolean | false | 否 | 是否开启 Quic/h3 协议（iOS 微信目前使用 gQUIC-Q43；Android 微信在 v8.0.54 前使用 gQUIC-Q43，v8.0.54 开始使用 IETF QUIC，即 h3 协议；PC微信使用 IETF QUIC，即 h3 协议） | [2.10.4](../../../framework/compatibility.html) |
|  | enableCache | boolean | false | 否 | 开启 Http 缓存 | [2.10.4](../../../framework/compatibility.html) |
|  | enableHttpDNS | boolean | false | 否 | 是否开启 HttpDNS 服务。如开启，需要同时填入 httpDNSServiceId 。 HttpDNS 用法详见 [移动解析HttpDNS](../../../framework/ability/HTTPDNS.html) | [2.19.1](../../../framework/compatibility.html) |
|  | httpDNSServiceId | string |  | 否 | HttpDNS 服务商 Id。 HttpDNS 用法详见 [移动解析HttpDNS](../../../framework/ability/HTTPDNS.html) | [2.19.1](../../../framework/compatibility.html) |
|  | httpDNSTimeout | number | 60000 | 否 | HttpDNS 超时时间。HttpDNS解析时间超过该值时不再走HttpDNS，本次请求将回退到localDNS。默认为 60000 毫秒。 HttpDNS 用法详见 [移动解析HttpDNS](../../../framework/ability/HTTPDNS.html) | [3.8.9](../../../framework/compatibility.html) |
|  | enableHttpDNSFallback | boolean | true | 否 | 是否开启 HttpDNS 兜底。开启时，HttpDNS 服务查询失败会回退到 localDNS；关闭时，HttpDNS 服务查询失败将直接报错，不回退到 localDNS。默认为 true。 HttpDNS 用法详见 [移动解析HttpDNS](../../../framework/ability/HTTPDNS.html) | [3.16.2](../../../framework/compatibility.html) |
|  | enableChunked | boolean | false | 否 | 开启 transfer-encoding chunked。 | [2.20.2](../../../framework/compatibility.html) |
|  | forceCellularNetwork | boolean | false | 否 | 强制使用蜂窝网络发送请求 | [2.21.0](../../../framework/compatibility.html) |
|  | redirect | string | follow | 否 | 重定向拦截策略。（目前安卓、iOS、开发者工具已支持，PC端将在后续支持） | [3.2.2](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | follow | 不拦截重定向，即客户端自动处理重定向 | | manual | 拦截重定向。开启后，当 http 状态码为 3xx 时客户端不再自动重定向，而是触发 onHeadersReceived 回调，并结束本次 request 请求。可通过 onHeadersReceived 回调中的 header.Location 获取重定向的 url | | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| OPTIONS | HTTP 请求 OPTIONS |
| GET | HTTP 请求 GET |
| HEAD | HTTP 请求 HEAD |
| POST | HTTP 请求 POST |
| PUT | HTTP 请求 PUT |
| DELETE | HTTP 请求 DELETE |
| TRACE | HTTP 请求 TRACE |
| CONNECT | HTTP 请求 CONNECT |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| text | 响应的数据为文本 |
| arraybuffer | 响应的数据为 ArrayBuffer |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| follow | 不拦截重定向，即客户端自动处理重定向 |
| manual | 拦截重定向。开启后，当 http 状态码为 3xx 时客户端不再自动重定向，而是触发 onHeadersReceived 回调，并结束本次 request 请求。可通过 onHeadersReceived 回调中的 header.Location 获取重定向的 url |

**Object object**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | data | string/Object/Arraybuffer | 开发者服务器返回的数据 |  |
|  | statusCode | number | 开发者服务器返回的 HTTP 状态码 |  |
|  | header | Object | 开发者服务器返回的 HTTP Response Header | [1.2.0](../../../framework/compatibility.html) |
|  | cookies | Array.<string> | 开发者服务器返回的 cookies，格式为字符串数组 | [2.10.0](../../../framework/compatibility.html) |
|  | profile | Object | 网络请求过程中一些调试信息，[查看详细说明](/miniprogram/dev/framework/performance/network.html)。目前仅 iOS 和 Android 端支持，其他端暂不支持。 | [2.10.4](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | invokeStart | number | 调用接口的时间。 | [3.8.10](../../../framework/compatibility.html) | |  | httpDNSDomainLookUpStart | number | httpDNS 开始查询的时间。仅当开启 httpDNS 功能时返回该字段。目前仅wx.request接口支持 | [3.8.9](../../../framework/compatibility.html) | |  | httpDNSDomainLookUpEnd | number | httpDNS 完成查询的时间。仅当开启 httpDNS 功能时返回该字段。目前仅wx.request接口支持 | [3.8.9](../../../framework/compatibility.html) | |  | queueStart | number | 开始排队的时间。达到并行上限时才需要排队。 | [3.8.10](../../../framework/compatibility.html) | |  | queueEnd | number | 结束排队的时间。达到并行上限时才需要排队。如果未发生排队，则该字段和 queueStart 字段值相同 | [3.8.10](../../../framework/compatibility.html) | |  | redirectStart | number | 第一个 HTTP 重定向发生时的时间。有跳转且是同域名内的重定向才算，否则值为 0 |  | |  | redirectEnd | number | 最后一个 HTTP 重定向完成时的时间。有跳转且是同域名内部的重定向才算，否则值为 0 |  | |  | fetchStart | number | 组件准备好使用 HTTP 请求抓取资源的时间，这发生在检查本地缓存之前 |  | |  | domainLookUpStart | number | Local DNS 域名查询开始的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 fetchStart 值相等 |  | |  | domainLookUpEnd | number | Local DNS 域名查询完成的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 fetchStart 值相等 |  | |  | connectStart | number | HTTP（TCP） 开始建立连接的时间，如果是持久连接，则与 fetchStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接开始的时间 |  | |  | connectEnd | number | HTTP（TCP） 完成建立连接的时间（完成握手），如果是持久连接，则与 fetchStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接完成的时间。注意这里握手结束，包括安全连接建立完成、SOCKS 授权通过 |  | |  | SSLconnectionStart | number | SSL建立连接的时间,如果不是安全连接,则值为 0 |  | |  | SSLconnectionEnd | number | SSL建立完成的时间,如果不是安全连接,则值为 0 |  | |  | requestStart | number | HTTP请求读取真实文档开始的时间（完成建立连接），包括从本地读取缓存。连接错误重连时，这里显示的也是新建立连接的时间 |  | |  | requestEnd | number | HTTP请求读取真实文档结束的时间 |  | |  | responseStart | number | HTTP 开始接收响应的时间（获取到第一个字节），包括从本地读取缓存 |  | |  | responseEnd | number | HTTP 响应全部接收完成的时间（获取到最后一个字节），包括从本地读取缓存 |  | |  | rtt | number | 当次请求连接过程中实时 rtt |  | |  | estimate\_nettype | number | 评估的网络状态 unknown, offline, slow 2g, 2g, 3g, 4g, last/0, 1, 2, 3, 4, 5, 6 |  | |  | httpRttEstimate | number | 协议层根据多个请求评估当前网络的 rtt（仅供参考） |  | |  | transportRttEstimate | number | 传输层根据多个请求评估的当前网络的 rtt（仅供参考） |  | |  | downstreamThroughputKbpsEstimate | number | 评估当前网络下载的kbps |  | |  | throughputKbps | number | 当前网络的实际下载kbps |  | |  | peerIP | string | 当前请求的IP |  | |  | port | number | 当前请求的端口 |  | |  | socketReused | boolean | 是否复用连接 |  | |  | sendBytesCount | number | 发送的字节数 |  | |  | receivedBytedCount | number | 收到字节数 |  | |  | protocol | string | 使用协议类型，有效值：http1.1, h2, quic, unknown |  | |  | usingHighPerformanceMode | boolean | 是否走到了高性能模式。基础库 v3.3.4 起支持。 |  | | | | |
|  | exception | Object | 网络请求过程中的一些异常信息，例如httpdns超时等 | [3.0.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | retryCount | number | 本次请求底层重试次数 | |  | reasons | Array.<Object> | 本次请求底层失败信息，所有失败信息均符合Errno错误码 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | errMsg | string | 错误原因 | |  | errno | string | 错误码 | | | | | | | |
|  | useHttpDNS | boolean | 最终请求是否使用了HttpDNS解析的IP。仅当enableHttpDNS传true时返回此字段。如果开启enableHttpDNS但最终请求未使用HttpDNS解析的IP，可在exception查看原因。 | [3.4.10](../../../framework/compatibility.html) |

**Object object**

|  | 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | invokeStart | number | 调用接口的时间。 | [3.8.10](../../../framework/compatibility.html) |
|  | httpDNSDomainLookUpStart | number | httpDNS 开始查询的时间。仅当开启 httpDNS 功能时返回该字段。目前仅wx.request接口支持 | [3.8.9](../../../framework/compatibility.html) |
|  | httpDNSDomainLookUpEnd | number | httpDNS 完成查询的时间。仅当开启 httpDNS 功能时返回该字段。目前仅wx.request接口支持 | [3.8.9](../../../framework/compatibility.html) |
|  | queueStart | number | 开始排队的时间。达到并行上限时才需要排队。 | [3.8.10](../../../framework/compatibility.html) |
|  | queueEnd | number | 结束排队的时间。达到并行上限时才需要排队。如果未发生排队，则该字段和 queueStart 字段值相同 | [3.8.10](../../../framework/compatibility.html) |
|  | redirectStart | number | 第一个 HTTP 重定向发生时的时间。有跳转且是同域名内的重定向才算，否则值为 0 |  |
|  | redirectEnd | number | 最后一个 HTTP 重定向完成时的时间。有跳转且是同域名内部的重定向才算，否则值为 0 |  |
|  | fetchStart | number | 组件准备好使用 HTTP 请求抓取资源的时间，这发生在检查本地缓存之前 |  |
|  | domainLookUpStart | number | Local DNS 域名查询开始的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 fetchStart 值相等 |  |
|  | domainLookUpEnd | number | Local DNS 域名查询完成的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 fetchStart 值相等 |  |
|  | connectStart | number | HTTP（TCP） 开始建立连接的时间，如果是持久连接，则与 fetchStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接开始的时间 |  |
|  | connectEnd | number | HTTP（TCP） 完成建立连接的时间（完成握手），如果是持久连接，则与 fetchStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接完成的时间。注意这里握手结束，包括安全连接建立完成、SOCKS 授权通过 |  |
|  | SSLconnectionStart | number | SSL建立连接的时间,如果不是安全连接,则值为 0 |  |
|  | SSLconnectionEnd | number | SSL建立完成的时间,如果不是安全连接,则值为 0 |  |
|  | requestStart | number | HTTP请求读取真实文档开始的时间（完成建立连接），包括从本地读取缓存。连接错误重连时，这里显示的也是新建立连接的时间 |  |
|  | requestEnd | number | HTTP请求读取真实文档结束的时间 |  |
|  | responseStart | number | HTTP 开始接收响应的时间（获取到第一个字节），包括从本地读取缓存 |  |
|  | responseEnd | number | HTTP 响应全部接收完成的时间（获取到最后一个字节），包括从本地读取缓存 |  |
|  | rtt | number | 当次请求连接过程中实时 rtt |  |
|  | estimate\_nettype | number | 评估的网络状态 unknown, offline, slow 2g, 2g, 3g, 4g, last/0, 1, 2, 3, 4, 5, 6 |  |
|  | httpRttEstimate | number | 协议层根据多个请求评估当前网络的 rtt（仅供参考） |  |
|  | transportRttEstimate | number | 传输层根据多个请求评估的当前网络的 rtt（仅供参考） |  |
|  | downstreamThroughputKbpsEstimate | number | 评估当前网络下载的kbps |  |
|  | throughputKbps | number | 当前网络的实际下载kbps |  |
|  | peerIP | string | 当前请求的IP |  |
|  | port | number | 当前请求的端口 |  |
|  | socketReused | boolean | 是否复用连接 |  |
|  | sendBytesCount | number | 发送的字节数 |  |
|  | receivedBytedCount | number | 收到字节数 |  |
|  | protocol | string | 使用协议类型，有效值：http1.1, h2, quic, unknown |  |
|  | usingHighPerformanceMode | boolean | 是否走到了高性能模式。基础库 v3.3.4 起支持。 |  |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | retryCount | number | 本次请求底层重试次数 |
|  | reasons | Array.<Object> | 本次请求底层失败信息，所有失败信息均符合Errno错误码 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | errMsg | string | 错误原因 | |  | errno | string | 错误码 | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | errMsg | string | 错误原因 |
|  | errno | string | 错误码 |

**Object object**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | errMsg | String | 错误信息 |  |
|  | errno | Number | errno 错误码，错误码的详细说明参考 [Errno错误码](../../../framework/usability/PublicErrno.html) | [2.24.0](../../../framework/compatibility.html) |
|  | exception | Object | 网络请求过程中的一些异常信息，例如httpdns超时等 | [3.8.10](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | retryCount | number | 本次请求底层重试次数 | |  | reasons | Array.<Object> | 本次请求底层失败信息，所有失败信息均符合Errno错误码 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | errMsg | string | 错误原因 | |  | errno | string | 错误码 | | | | | | | |
|  | useHttpDNS | boolean | 最终请求是否使用了HttpDNS解析的IP。仅当enableHttpDNS传true时返回此字段。如果开启enableHttpDNS但最终请求未使用HttpDNS解析的IP，可在exception查看原因。 | [3.8.10](../../../framework/compatibility.html) |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | retryCount | number | 本次请求底层重试次数 |
|  | reasons | Array.<Object> | 本次请求底层失败信息，所有失败信息均符合Errno错误码 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | errMsg | string | 错误原因 | |  | errno | string | 错误码 | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | errMsg | string | 错误原因 |
|  | errno | string | 错误码 |

---

### RequestTask

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/request/RequestTask.html

---

### RequestTask.abort()

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/request/RequestTask.abort.html

---

### RequestTask.offChunkReceived(function listener)

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/request/RequestTask.offChunkReceived.html

---

### RequestTask.offHeadersReceived(function listener)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/request/RequestTask.offHeadersReceived.html

---

### RequestTask.onChunkReceived(function listener)

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/request/RequestTask.onChunkReceived.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | ArrayBuffer | 返回的chunk buffer |

---

### RequestTask.onHeadersReceived(function listener)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/request/RequestTask.onHeadersReceived.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| header | Object | 开发者服务器返回的 HTTP Response Header |
| statusCode | Number | 开发者服务器返回的 HTTP 状态码 （目前开发者工具上不会返回 statusCode 字段，可用真机查看该字段，后续将会支持） |
| cookies | Array.<string> | 开发者服务器返回的 cookies，格式为字符串数组 |

---

### DownloadTask wx.downloadFile(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/download/wx.downloadFile.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| url | string |  | 是 | 下载资源的 url |  |
| header | Object |  | 否 | HTTP 请求的 Header，Header 中不能设置 Referer |  |
| timeout | number | 60000 | 否 | 超时时间，单位为毫秒，默认值为 60000 即一分钟。 | [2.10.0](../../../framework/compatibility.html) |
| filePath | string |  | 否 | 指定文件下载后存储的路径 (本地路径) | [1.8.0](../../../framework/compatibility.html) |
| enableProfile | boolean | true | 否 | 是否开启 profile。iOS 和 Android 端默认开启，其他端暂不支持。开启后可在接口回调的 res.profile 中查看性能调试信息。 |  |
| enableHttp2 | boolean | false | 否 | 是否开启 http2 | [2.10.4](../../../framework/compatibility.html) |
| enableQuic | boolean | false | 否 | 是否开启 Quic/h3 协议（iOS 微信目前使用 gQUIC-Q43；Android 微信在 v8.0.54 前使用 gQUIC-Q43，v8.0.54 开始使用 IETF QUIC，即 h3 协议；PC微信使用 IETF QUIC，即 h3 协议） | [2.10.4](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | tempFilePath | string | 临时文件路径 (本地路径)。没传入 filePath 指定文件存储路径时会返回，下载后的文件会存储到一个临时文件 |  |
|  | filePath | string | 用户文件路径 (本地路径)。传入 filePath 时会返回，跟传入的 filePath 一致 |  |
|  | statusCode | number | 开发者服务器返回的 HTTP 状态码 |  |
|  | profile | Object | 网络请求过程中一些调试信息，[查看详细说明](/miniprogram/dev/framework/performance/network.html)。目前 iOS 和 Android 端支持。 | [2.10.4](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | invokeStart | number | 调用接口的时间。 | [3.8.10](../../../framework/compatibility.html) | |  | httpDNSDomainLookUpStart | number | httpDNS 开始查询的时间。仅当开启 httpDNS 功能时返回该字段。目前仅wx.request接口支持 | [3.8.9](../../../framework/compatibility.html) | |  | httpDNSDomainLookUpEnd | number | httpDNS 完成查询的时间。仅当开启 httpDNS 功能时返回该字段。目前仅wx.request接口支持 | [3.8.9](../../../framework/compatibility.html) | |  | queueStart | number | 开始排队的时间。达到并行上限时才需要排队。 | [3.8.10](../../../framework/compatibility.html) | |  | queueEnd | number | 结束排队的时间。达到并行上限时才需要排队。如果未发生排队，则该字段和 queueStart 字段值相同 | [3.8.10](../../../framework/compatibility.html) | |  | redirectStart | number | 第一个 HTTP 重定向发生时的时间。有跳转且是同域名内的重定向才算，否则值为 0 |  | |  | redirectEnd | number | 最后一个 HTTP 重定向完成时的时间。有跳转且是同域名内部的重定向才算，否则值为 0 |  | |  | fetchStart | number | 组件准备好使用 HTTP 请求抓取资源的时间，这发生在检查本地缓存之前 |  | |  | domainLookUpStart | number | Local DNS 域名查询开始的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 fetchStart 值相等 |  | |  | domainLookUpEnd | number | Local DNS 域名查询完成的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 fetchStart 值相等 |  | |  | connectStart | number | HTTP（TCP） 开始建立连接的时间，如果是持久连接，则与 fetchStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接开始的时间 |  | |  | connectEnd | number | HTTP（TCP） 完成建立连接的时间（完成握手），如果是持久连接，则与 fetchStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接完成的时间。注意这里握手结束，包括安全连接建立完成、SOCKS 授权通过 |  | |  | SSLconnectionStart | number | SSL建立连接的时间,如果不是安全连接,则值为 0 |  | |  | SSLconnectionEnd | number | SSL建立完成的时间,如果不是安全连接,则值为 0 |  | |  | requestStart | number | HTTP请求读取真实文档开始的时间（完成建立连接），包括从本地读取缓存。连接错误重连时，这里显示的也是新建立连接的时间 |  | |  | requestEnd | number | HTTP请求读取真实文档结束的时间 |  | |  | responseStart | number | HTTP 开始接收响应的时间（获取到第一个字节），包括从本地读取缓存 |  | |  | responseEnd | number | HTTP 响应全部接收完成的时间（获取到最后一个字节），包括从本地读取缓存 |  | |  | rtt | number | 当次请求连接过程中实时 rtt |  | |  | estimate\_nettype | number | 评估的网络状态 unknown, offline, slow 2g, 2g, 3g, 4g, last/0, 1, 2, 3, 4, 5, 6 |  | |  | httpRttEstimate | number | 协议层根据多个请求评估当前网络的 rtt（仅供参考） |  | |  | transportRttEstimate | number | 传输层根据多个请求评估的当前网络的 rtt（仅供参考） |  | |  | downstreamThroughputKbpsEstimate | number | 评估当前网络下载的kbps |  | |  | throughputKbps | number | 当前网络的实际下载kbps |  | |  | peerIP | string | 当前请求的IP |  | |  | port | number | 当前请求的端口 |  | |  | socketReused | boolean | 是否复用连接 |  | |  | sendBytesCount | number | 发送的字节数 |  | |  | receivedBytedCount | number | 收到字节数 |  | |  | protocol | string | 使用协议类型，有效值：http1.1, h2, quic, unknown |  | |  | usingHighPerformanceMode | boolean | 是否走到了高性能模式。基础库 v3.3.4 起支持。 |  | | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | invokeStart | number | 调用接口的时间。 | [3.8.10](../../../framework/compatibility.html) |
|  | httpDNSDomainLookUpStart | number | httpDNS 开始查询的时间。仅当开启 httpDNS 功能时返回该字段。目前仅wx.request接口支持 | [3.8.9](../../../framework/compatibility.html) |
|  | httpDNSDomainLookUpEnd | number | httpDNS 完成查询的时间。仅当开启 httpDNS 功能时返回该字段。目前仅wx.request接口支持 | [3.8.9](../../../framework/compatibility.html) |
|  | queueStart | number | 开始排队的时间。达到并行上限时才需要排队。 | [3.8.10](../../../framework/compatibility.html) |
|  | queueEnd | number | 结束排队的时间。达到并行上限时才需要排队。如果未发生排队，则该字段和 queueStart 字段值相同 | [3.8.10](../../../framework/compatibility.html) |
|  | redirectStart | number | 第一个 HTTP 重定向发生时的时间。有跳转且是同域名内的重定向才算，否则值为 0 |  |
|  | redirectEnd | number | 最后一个 HTTP 重定向完成时的时间。有跳转且是同域名内部的重定向才算，否则值为 0 |  |
|  | fetchStart | number | 组件准备好使用 HTTP 请求抓取资源的时间，这发生在检查本地缓存之前 |  |
|  | domainLookUpStart | number | Local DNS 域名查询开始的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 fetchStart 值相等 |  |
|  | domainLookUpEnd | number | Local DNS 域名查询完成的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 fetchStart 值相等 |  |
|  | connectStart | number | HTTP（TCP） 开始建立连接的时间，如果是持久连接，则与 fetchStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接开始的时间 |  |
|  | connectEnd | number | HTTP（TCP） 完成建立连接的时间（完成握手），如果是持久连接，则与 fetchStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接完成的时间。注意这里握手结束，包括安全连接建立完成、SOCKS 授权通过 |  |
|  | SSLconnectionStart | number | SSL建立连接的时间,如果不是安全连接,则值为 0 |  |
|  | SSLconnectionEnd | number | SSL建立完成的时间,如果不是安全连接,则值为 0 |  |
|  | requestStart | number | HTTP请求读取真实文档开始的时间（完成建立连接），包括从本地读取缓存。连接错误重连时，这里显示的也是新建立连接的时间 |  |
|  | requestEnd | number | HTTP请求读取真实文档结束的时间 |  |
|  | responseStart | number | HTTP 开始接收响应的时间（获取到第一个字节），包括从本地读取缓存 |  |
|  | responseEnd | number | HTTP 响应全部接收完成的时间（获取到最后一个字节），包括从本地读取缓存 |  |
|  | rtt | number | 当次请求连接过程中实时 rtt |  |
|  | estimate\_nettype | number | 评估的网络状态 unknown, offline, slow 2g, 2g, 3g, 4g, last/0, 1, 2, 3, 4, 5, 6 |  |
|  | httpRttEstimate | number | 协议层根据多个请求评估当前网络的 rtt（仅供参考） |  |
|  | transportRttEstimate | number | 传输层根据多个请求评估的当前网络的 rtt（仅供参考） |  |
|  | downstreamThroughputKbpsEstimate | number | 评估当前网络下载的kbps |  |
|  | throughputKbps | number | 当前网络的实际下载kbps |  |
|  | peerIP | string | 当前请求的IP |  |
|  | port | number | 当前请求的端口 |  |
|  | socketReused | boolean | 是否复用连接 |  |
|  | sendBytesCount | number | 发送的字节数 |  |
|  | receivedBytedCount | number | 收到字节数 |  |
|  | protocol | string | 使用协议类型，有效值：http1.1, h2, quic, unknown |  |
|  | usingHighPerformanceMode | boolean | 是否走到了高性能模式。基础库 v3.3.4 起支持。 |  |

---

### DownloadTask

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/download/DownloadTask.html

---

### DownloadTask.abort()

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/download/DownloadTask.abort.html

---

### DownloadTask.offHeadersReceived(function listener)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/download/DownloadTask.offHeadersReceived.html

---

### DownloadTask.offProgressUpdate(function listener)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/download/DownloadTask.offProgressUpdate.html

---

### DownloadTask.onHeadersReceived(function listener)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/download/DownloadTask.onHeadersReceived.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| header | Object | 开发者服务器返回的 HTTP Response Header |

---

### DownloadTask.onProgressUpdate(function listener)

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/download/DownloadTask.onProgressUpdate.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| progress | number | 下载进度百分比 |
| totalBytesWritten | number | 已经下载的数据长度，单位 Bytes |
| totalBytesExpectedToWrite | number | 预期需要下载的数据总长度，单位 Bytes |

---

### UploadTask wx.uploadFile(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/upload/wx.uploadFile.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| url | string |  | 是 | 开发者服务器地址 |  |
| filePath | string |  | 是 | 要上传文件资源的路径 (本地路径) |  |
| name | string |  | 是 | 文件对应的 key，开发者在服务端可以通过这个 key 获取文件的二进制内容 |  |
| header | Object |  | 否 | HTTP 请求 Header，Header 中不能设置 Referer |  |
| formData | Object |  | 否 | HTTP 请求中其他额外的 form data |  |
| timeout | number |  | 否 | 超时时间，单位为毫秒 | [2.10.0](../../../framework/compatibility.html) |
| enableProfile | boolean | true | 否 | 是否开启 profile。iOS 和 Android 端默认开启，其他端暂不支持。开启后可在接口回调的 res.profile 中查看性能调试信息。 | [3.5.0](../../../framework/compatibility.html) |
| enableHttp2 | boolean | false | 否 | 是否开启 http2 | [2.10.4](../../../framework/compatibility.html) |
| enableQuic | boolean | false | 否 | 是否开启 Quic/h3 协议（iOS 微信目前使用 gQUIC-Q43；Android 微信在 v8.0.54 前使用 gQUIC-Q43，v8.0.54 开始使用 IETF QUIC，即 h3 协议；PC微信使用 IETF QUIC，即 h3 协议） | [2.10.4](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | data | string | 开发者服务器返回的数据 |  |
|  | statusCode | number | 开发者服务器返回的 HTTP 状态码 |  |
|  | profile | Object | 网络请求过程中一些调试信息，[查看详细说明](/miniprogram/dev/framework/performance/network.html)。目前 iOS 和 Android 端支持。 | [3.5.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | invokeStart | number | 调用接口的时间。 | [3.8.10](../../../framework/compatibility.html) | |  | httpDNSDomainLookUpStart | number | httpDNS 开始查询的时间。仅当开启 httpDNS 功能时返回该字段。目前仅wx.request接口支持 | [3.8.9](../../../framework/compatibility.html) | |  | httpDNSDomainLookUpEnd | number | httpDNS 完成查询的时间。仅当开启 httpDNS 功能时返回该字段。目前仅wx.request接口支持 | [3.8.9](../../../framework/compatibility.html) | |  | queueStart | number | 开始排队的时间。达到并行上限时才需要排队。 | [3.8.10](../../../framework/compatibility.html) | |  | queueEnd | number | 结束排队的时间。达到并行上限时才需要排队。如果未发生排队，则该字段和 queueStart 字段值相同 | [3.8.10](../../../framework/compatibility.html) | |  | redirectStart | number | 第一个 HTTP 重定向发生时的时间。有跳转且是同域名内的重定向才算，否则值为 0 |  | |  | redirectEnd | number | 最后一个 HTTP 重定向完成时的时间。有跳转且是同域名内部的重定向才算，否则值为 0 |  | |  | fetchStart | number | 组件准备好使用 HTTP 请求抓取资源的时间，这发生在检查本地缓存之前 |  | |  | domainLookUpStart | number | Local DNS 域名查询开始的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 fetchStart 值相等 |  | |  | domainLookUpEnd | number | Local DNS 域名查询完成的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 fetchStart 值相等 |  | |  | connectStart | number | HTTP（TCP） 开始建立连接的时间，如果是持久连接，则与 fetchStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接开始的时间 |  | |  | connectEnd | number | HTTP（TCP） 完成建立连接的时间（完成握手），如果是持久连接，则与 fetchStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接完成的时间。注意这里握手结束，包括安全连接建立完成、SOCKS 授权通过 |  | |  | SSLconnectionStart | number | SSL建立连接的时间,如果不是安全连接,则值为 0 |  | |  | SSLconnectionEnd | number | SSL建立完成的时间,如果不是安全连接,则值为 0 |  | |  | requestStart | number | HTTP请求读取真实文档开始的时间（完成建立连接），包括从本地读取缓存。连接错误重连时，这里显示的也是新建立连接的时间 |  | |  | requestEnd | number | HTTP请求读取真实文档结束的时间 |  | |  | responseStart | number | HTTP 开始接收响应的时间（获取到第一个字节），包括从本地读取缓存 |  | |  | responseEnd | number | HTTP 响应全部接收完成的时间（获取到最后一个字节），包括从本地读取缓存 |  | |  | rtt | number | 当次请求连接过程中实时 rtt |  | |  | estimate\_nettype | number | 评估的网络状态 unknown, offline, slow 2g, 2g, 3g, 4g, last/0, 1, 2, 3, 4, 5, 6 |  | |  | httpRttEstimate | number | 协议层根据多个请求评估当前网络的 rtt（仅供参考） |  | |  | transportRttEstimate | number | 传输层根据多个请求评估的当前网络的 rtt（仅供参考） |  | |  | downstreamThroughputKbpsEstimate | number | 评估当前网络下载的kbps |  | |  | throughputKbps | number | 当前网络的实际下载kbps |  | |  | peerIP | string | 当前请求的IP |  | |  | port | number | 当前请求的端口 |  | |  | socketReused | boolean | 是否复用连接 |  | |  | sendBytesCount | number | 发送的字节数 |  | |  | receivedBytedCount | number | 收到字节数 |  | |  | protocol | string | 使用协议类型，有效值：http1.1, h2, quic, unknown |  | |  | usingHighPerformanceMode | boolean | 是否走到了高性能模式。基础库 v3.3.4 起支持。 |  | | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | invokeStart | number | 调用接口的时间。 | [3.8.10](../../../framework/compatibility.html) |
|  | httpDNSDomainLookUpStart | number | httpDNS 开始查询的时间。仅当开启 httpDNS 功能时返回该字段。目前仅wx.request接口支持 | [3.8.9](../../../framework/compatibility.html) |
|  | httpDNSDomainLookUpEnd | number | httpDNS 完成查询的时间。仅当开启 httpDNS 功能时返回该字段。目前仅wx.request接口支持 | [3.8.9](../../../framework/compatibility.html) |
|  | queueStart | number | 开始排队的时间。达到并行上限时才需要排队。 | [3.8.10](../../../framework/compatibility.html) |
|  | queueEnd | number | 结束排队的时间。达到并行上限时才需要排队。如果未发生排队，则该字段和 queueStart 字段值相同 | [3.8.10](../../../framework/compatibility.html) |
|  | redirectStart | number | 第一个 HTTP 重定向发生时的时间。有跳转且是同域名内的重定向才算，否则值为 0 |  |
|  | redirectEnd | number | 最后一个 HTTP 重定向完成时的时间。有跳转且是同域名内部的重定向才算，否则值为 0 |  |
|  | fetchStart | number | 组件准备好使用 HTTP 请求抓取资源的时间，这发生在检查本地缓存之前 |  |
|  | domainLookUpStart | number | Local DNS 域名查询开始的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 fetchStart 值相等 |  |
|  | domainLookUpEnd | number | Local DNS 域名查询完成的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 fetchStart 值相等 |  |
|  | connectStart | number | HTTP（TCP） 开始建立连接的时间，如果是持久连接，则与 fetchStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接开始的时间 |  |
|  | connectEnd | number | HTTP（TCP） 完成建立连接的时间（完成握手），如果是持久连接，则与 fetchStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接完成的时间。注意这里握手结束，包括安全连接建立完成、SOCKS 授权通过 |  |
|  | SSLconnectionStart | number | SSL建立连接的时间,如果不是安全连接,则值为 0 |  |
|  | SSLconnectionEnd | number | SSL建立完成的时间,如果不是安全连接,则值为 0 |  |
|  | requestStart | number | HTTP请求读取真实文档开始的时间（完成建立连接），包括从本地读取缓存。连接错误重连时，这里显示的也是新建立连接的时间 |  |
|  | requestEnd | number | HTTP请求读取真实文档结束的时间 |  |
|  | responseStart | number | HTTP 开始接收响应的时间（获取到第一个字节），包括从本地读取缓存 |  |
|  | responseEnd | number | HTTP 响应全部接收完成的时间（获取到最后一个字节），包括从本地读取缓存 |  |
|  | rtt | number | 当次请求连接过程中实时 rtt |  |
|  | estimate\_nettype | number | 评估的网络状态 unknown, offline, slow 2g, 2g, 3g, 4g, last/0, 1, 2, 3, 4, 5, 6 |  |
|  | httpRttEstimate | number | 协议层根据多个请求评估当前网络的 rtt（仅供参考） |  |
|  | transportRttEstimate | number | 传输层根据多个请求评估的当前网络的 rtt（仅供参考） |  |
|  | downstreamThroughputKbpsEstimate | number | 评估当前网络下载的kbps |  |
|  | throughputKbps | number | 当前网络的实际下载kbps |  |
|  | peerIP | string | 当前请求的IP |  |
|  | port | number | 当前请求的端口 |  |
|  | socketReused | boolean | 是否复用连接 |  |
|  | sendBytesCount | number | 发送的字节数 |  |
|  | receivedBytedCount | number | 收到字节数 |  |
|  | protocol | string | 使用协议类型，有效值：http1.1, h2, quic, unknown |  |
|  | usingHighPerformanceMode | boolean | 是否走到了高性能模式。基础库 v3.3.4 起支持。 |  |

---

### UploadTask

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/upload/UploadTask.html

---

### UploadTask.abort()

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/upload/UploadTask.abort.html

---

### UploadTask.offHeadersReceived(function listener)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/upload/UploadTask.offHeadersReceived.html

---

### UploadTask.offProgressUpdate(function listener)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/upload/UploadTask.offProgressUpdate.html

---

### UploadTask.onHeadersReceived(function listener)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/upload/UploadTask.onHeadersReceived.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| header | Object | 开发者服务器返回的 HTTP Response Header |

---

### UploadTask.onProgressUpdate(function listener)

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/upload/UploadTask.onProgressUpdate.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| progress | number | 上传进度百分比 |
| totalBytesSent | number | 已经上传的数据长度，单位 Bytes |
| totalBytesExpectedToSend | number | 预期需要上传的数据总长度，单位 Bytes |

---

### wx.sendSocketMessage(Object object)

推荐使用SocketTask的方式去管理 webSocket 链接，每一条链路的生命周期都更加可控，同时存在多个 webSocket 的链接的情况下使用 wx 前缀的方法可能会带来一些和预期不一致的情况。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.sendSocketMessage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| data | string/ArrayBuffer |  | 是 | 需要发送的内容 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.onSocketOpen(function listener)

推荐使用SocketTask的方式去管理 webSocket 链接，每一条链路的生命周期都更加可控，同时存在多个 webSocket 的链接的情况下使用 wx 前缀的方法可能会带来一些和预期不一致的情况。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.onSocketOpen.html

**function listener**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| header | object | 连接成功的 HTTP 响应 Header | [2.0.0](../../../framework/compatibility.html) |

---

### wx.onSocketMessage(function listener)

推荐使用SocketTask的方式去管理 webSocket 链接，每一条链路的生命周期都更加可控，同时存在多个 webSocket 的链接的情况下使用 wx 前缀的方法可能会带来一些和预期不一致的情况。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.onSocketMessage.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | string/ArrayBuffer | 服务器返回的消息 |

---

### wx.onSocketError(function listener)

推荐使用SocketTask的方式去管理 webSocket 链接，每一条链路的生命周期都更加可控，同时存在多个 webSocket 的链接的情况下使用 wx 前缀的方法可能会带来一些和预期不一致的情况。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.onSocketError.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |

---

### wx.onSocketClose(function listener)

推荐使用SocketTask的方式去管理 webSocket 链接，每一条链路的生命周期都更加可控，同时存在多个 webSocket 的链接的情况下使用 wx 前缀的方法可能会带来一些和预期不一致的情况。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.onSocketClose.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| code | number | 一个数字值表示关闭连接的状态号，表示连接被关闭的原因。 |
| reason | string | 一个可读的字符串，表示连接被关闭的原因。 |

---

### SocketTask wx.connectSocket(Object object)

推荐使用SocketTask的方式去管理 webSocket 链接，每一条链路的生命周期都更加可控，同时存在多个 webSocket 的链接的情况下使用 wx 前缀的方法可能会带来一些和预期不一致的情况。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.connectSocket.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| url | string |  | 是 | 开发者服务器 wss 接口地址 |  |
| header | Object |  | 否 | HTTP Header，Header 中不能设置 Referer |  |
| protocols | Array.<string> |  | 否 | 子协议数组 | [1.4.0](../../../framework/compatibility.html) |
| tcpNoDelay | boolean | false | 否 | 建立 TCP 连接的时候的 TCP\_NODELAY 设置 | [2.4.0](../../../framework/compatibility.html) |
| perMessageDeflate | boolean | false | 否 | 是否开启压缩扩展 | [2.8.0](../../../framework/compatibility.html) |
| timeout | number |  | 否 | 超时时间，单位为毫秒 | [2.10.0](../../../framework/compatibility.html) |
| forceCellularNetwork | boolean | false | 否 | 强制使用蜂窝网络发送请求 | [2.29.0](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### wx.closeSocket(Object object)

推荐使用SocketTask的方式去管理 webSocket 链接，每一条链路的生命周期都更加可控，同时存在多个 webSocket 的链接的情况下使用 wx 前缀的方法可能会带来一些和预期不一致的情况。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.closeSocket.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 1000（表示正常关闭连接） | 否 | 一个数字值表示关闭连接的状态号，表示连接被关闭的原因。 |
| reason | string |  | 否 | 一个可读的字符串，表示连接被关闭的原因。这个字符串必须是不长于 123 字节的 UTF-8 文本（不是字符）。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### SocketTask

基础库 1.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/SocketTask.html

---

### SocketTask.close(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/SocketTask.close.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 1000（表示正常关闭连接） | 否 | 一个数字值表示关闭连接的状态号，表示连接被关闭的原因。 |
| reason | string |  | 否 | 一个可读的字符串，表示连接被关闭的原因。这个字符串必须是不长于 123 字节的 UTF-8 文本（不是字符）。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### SocketTask.onClose(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/SocketTask.onClose.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| code | number | 一个数字值表示关闭连接的状态号，表示连接被关闭的原因。 |
| reason | string | 一个可读的字符串，表示连接被关闭的原因。 |

---

### SocketTask.onError(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/SocketTask.onError.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |

---

### SocketTask.onMessage(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/SocketTask.onMessage.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | string/ArrayBuffer | 服务器返回的消息 |

---

### SocketTask.onOpen(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/SocketTask.onOpen.html

**function listener**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | header | object | 连接成功的 HTTP 响应 Header | [2.0.0](../../../framework/compatibility.html) |
|  | profile | Object | 网络请求过程中一些调试信息 | [2.10.4](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | fetchStart | number | 组件准备好使用 SOCKET 建立请求的时间，这发生在检查本地缓存之前 | |  | domainLookUpStart | number | DNS 域名查询开始的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 fetchStart 值相等 | |  | domainLookUpEnd | number | DNS 域名查询完成的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 fetchStart 值相等 | |  | connectStart | number | 开始建立连接的时间，如果是持久连接，则与 fetchStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接开始的时间 | |  | connectEnd | number | 完成建立连接的时间（完成握手），如果是持久连接，则与 fetchStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接完成的时间。注意这里握手结束，包括安全连接建立完成、SOCKS 授权通过 | |  | rtt | number | 单次连接的耗时，包括 connect ，tls | |  | handshakeCost | number | 握手耗时 | |  | cost | number | 上层请求到返回的耗时 | | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | fetchStart | number | 组件准备好使用 SOCKET 建立请求的时间，这发生在检查本地缓存之前 |
|  | domainLookUpStart | number | DNS 域名查询开始的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 fetchStart 值相等 |
|  | domainLookUpEnd | number | DNS 域名查询完成的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 fetchStart 值相等 |
|  | connectStart | number | 开始建立连接的时间，如果是持久连接，则与 fetchStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接开始的时间 |
|  | connectEnd | number | 完成建立连接的时间（完成握手），如果是持久连接，则与 fetchStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接完成的时间。注意这里握手结束，包括安全连接建立完成、SOCKS 授权通过 |
|  | rtt | number | 单次连接的耗时，包括 connect ，tls |
|  | handshakeCost | number | 握手耗时 |
|  | cost | number | 上层请求到返回的耗时 |

---

### SocketTask.send(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/SocketTask.send.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| data | string/ArrayBuffer |  | 是 | 需要发送的内容 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.stopLocalServiceDiscovery(Object object)

基础库 2.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.stopLocalServiceDiscovery.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | errMsg | string | 错误信息 |
|  | | 合法值 | 说明 | | --- | --- | | task not found | 在当前没有处在搜索服务中的情况下调用 stopLocalServiceDiscovery | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| task not found | 在当前没有处在搜索服务中的情况下调用 stopLocalServiceDiscovery |

---

### wx.startLocalServiceDiscovery(Object object)

基础库 2.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.startLocalServiceDiscovery.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| serviceType | string |  | 是 | 要搜索的服务类型 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | errMsg | string | 错误信息 |
|  | | 合法值 | 说明 | | --- | --- | | invalid param | serviceType 为空 | | scan task already exist | 在当前 startLocalServiceDiscovery 发起的搜索未停止的情况下，再次调用 startLocalServiceDiscovery | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| invalid param | serviceType 为空 |
| scan task already exist | 在当前 startLocalServiceDiscovery 发起的搜索未停止的情况下，再次调用 startLocalServiceDiscovery |

---

### wx.onLocalServiceResolveFail(function listener)

基础库 2.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.onLocalServiceResolveFail.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| serviceType | string | 服务的类型 |
| serviceName | string | 服务的名称 |

---

### wx.onLocalServiceLost(function listener)

基础库 2.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.onLocalServiceLost.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| serviceType | string | 服务的类型 |
| serviceName | string | 服务的名称 |

---

### wx.onLocalServiceFound(function listener)

基础库 2.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.onLocalServiceFound.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| serviceType | string | 服务的类型 |
| serviceName | string | 服务的名称 |
| ip | string | 服务的 ip 地址 |
| port | number | 服务的端口 |

---

### wx.onLocalServiceDiscoveryStop(function listener)

基础库 2.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.onLocalServiceDiscoveryStop.html

---

### wx.offLocalServiceResolveFail(function listener)

基础库 2.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.offLocalServiceResolveFail.html

---

### wx.offLocalServiceLost(function listener)

基础库 2.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.offLocalServiceLost.html

---

### wx.offLocalServiceFound(function listener)

基础库 2.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.offLocalServiceFound.html

---

### wx.offLocalServiceDiscoveryStop(function listener)

基础库 2.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.offLocalServiceDiscoveryStop.html

---

### TCPSocket wx.createTCPSocket(Object object)

基础库 2.18.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/wx.createTCPSocket.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | type | string | ipv4 | 否 | 套接字族，必须是 IPv4 或者 IPv6，默认是 IPv4 | [3.6.4](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | ipv4 | IPv4 | | ipv6 | IPv6 | | | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| ipv4 | IPv4 |
| ipv6 | IPv6 |

---

### TCPSocket

基础库 2.18.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| -1 |  | 系统错误 |
| -2 |  | socket接口错误，可参考系统的socket错误码 |
| -3 |  | 发送失败，无接口权限 |
| -4 |  | 链接失败 |
| 1 |  | 发送失败，参数错误，address不合法 |
| 2 |  | 发送失败，参数错误，port不合法 |
| 3 |  | 绑定wifi网络失败，BSSID不合法 |
| 4 |  | 绑定wifi网络失败，系统错误 |
| 5 |  | 绑定wifi网络失败，该接口仅在安卓平台支持 |
| 6 |  | 绑定wifi网络失败，低版本安卓不支持该接口 |

---

### TCPSocket.bindWifi(Object options)

基础库 2.25.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.bindWifi.html

**Object options**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| BSSID | string |  | 是 | 当前 wifi 网络的 BSSID ，可通过 wx.getConnectedWifi 获取 |

---

### TCPSocket.close()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.close.html

---

### TCPSocket.connect(Object options)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.connect.html

**Object options**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| address | string |  | 是 | 套接字要连接的地址 |  |
| port | number |  | 是 | 套接字要连接的端口 |  |
| timeout | number | 2 | 否 | 套接字要连接的超时时间，默认为 2s |  |
| enableHttpDNS | boolean | false | 否 | 是否开启 HttpDNS 服务。如开启，需要同时填入 httpDNSServiceId 。 HttpDNS 用法详见 [移动解析HttpDNS](../../../framework/ability/HTTPDNS.html) | [3.4.0](../../../framework/compatibility.html) |
| httpDNSServiceId | string |  | 否 | HttpDNS 服务商 Id。 HttpDNS 用法详见 [移动解析HttpDNS](../../../framework/ability/HTTPDNS.html) | [3.4.0](../../../framework/compatibility.html) |

---

### TCPSocket.offBindWifi(function listener)

基础库 2.25.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.offBindWifi.html

---

### TCPSocket.offClose(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.offClose.html

---

### TCPSocket.offConnect(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.offConnect.html

---

### TCPSocket.offError(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.offError.html

---

### TCPSocket.offMessage(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.offMessage.html

---

### TCPSocket.onBindWifi(function listener)

基础库 2.25.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.onBindWifi.html

---

### TCPSocket.onClose(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.onClose.html

---

### TCPSocket.onConnect(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.onConnect.html

**function listener**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | useHttpDNS | boolean | 本次连接是否使用了 HttpDNS | [3.4.0](../../../framework/compatibility.html) |
|  | exception | Object | 网络请求过程中的一些异常信息（例如：TCPSocket.connect 传了 enableHttpDNS: true，但最终未使用 HttpDNS 时，exception 就会说明未使用 HttpDNS 的原因） | [3.4.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | reasons | Array.<Object> | 异常信息 | [3.4.0](../../../framework/compatibility.html) | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | errMsg | string | 错误原因 | |  | errno | string | 错误码 | | | | | | | | |
|  | remoteInfo | Object | 发送端地址信息（目前仅iOS和Android端支持） | [3.4.1](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | address | string | 发送消息的 socket 的地址 | [3.4.1](../../../framework/compatibility.html) | |  | family | string | 使用的协议族，为 IPv4 或者 IPv6 | [3.4.1](../../../framework/compatibility.html) | |  | port | number | 端口号 | [3.4.1](../../../framework/compatibility.html) | | | | |
|  | localInfo | Object | 接收端地址信息（目前仅iOS和Android端支持） | [3.4.1](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | address | string | 接收消息的 socket 的地址 | [3.4.1](../../../framework/compatibility.html) | |  | family | string | 使用的协议族，为 IPv4 或者 IPv6 | [3.4.1](../../../framework/compatibility.html) | |  | port | number | 端口号 | [3.4.1](../../../framework/compatibility.html) | | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | reasons | Array.<Object> | 异常信息 | [3.4.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | errMsg | string | 错误原因 | |  | errno | string | 错误码 | | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | errMsg | string | 错误原因 |
|  | errno | string | 错误码 |

**function listener**

|  | 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | address | string | 发送消息的 socket 的地址 | [3.4.1](../../../framework/compatibility.html) |
|  | family | string | 使用的协议族，为 IPv4 或者 IPv6 | [3.4.1](../../../framework/compatibility.html) |
|  | port | number | 端口号 | [3.4.1](../../../framework/compatibility.html) |

**function listener**

|  | 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | address | string | 接收消息的 socket 的地址 | [3.4.1](../../../framework/compatibility.html) |
|  | family | string | 使用的协议族，为 IPv4 或者 IPv6 | [3.4.1](../../../framework/compatibility.html) |
|  | port | number | 端口号 | [3.4.1](../../../framework/compatibility.html) |

---

### TCPSocket.onError(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.onError.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |

---

### TCPSocket.onMessage(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.onMessage.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | message | ArrayBuffer | 收到的消息 |
|  | remoteInfo | Object | 发送端地址信息 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | address | string | 发送消息的 socket 的地址 | |  | family | string | 使用的协议族，为 IPv4 或者 IPv6 | |  | port | number | 端口号 | | | |
|  | localInfo | Object | 接收端地址信息 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | address | string | 接收消息的 socket 的地址 | |  | family | string | 使用的协议族，为 IPv4 或者 IPv6 | |  | port | number | 端口号 | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | address | string | 发送消息的 socket 的地址 |
|  | family | string | 使用的协议族，为 IPv4 或者 IPv6 |
|  | port | number | 端口号 |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | address | string | 接收消息的 socket 的地址 |
|  | family | string | 使用的协议族，为 IPv4 或者 IPv6 |
|  | port | number | 端口号 |

---

### TCPSocket.write(string|ArrayBuffer data)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.write.html

---

### UDPSocket wx.createUDPSocket(string type, Object options)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/wx.createUDPSocket.html

---

### UDPSocket

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| -1 |  | 系统错误 |
| -2 |  | socket接口错误，可参考系统的socket错误码 |
| -3 |  | 发送失败，无接口权限 |
| 1 |  | 发送失败，参数错误，address不合法 |
| 2 |  | 发送失败，参数错误，port不合法 |

---

### number UDPSocket.bind(number port)

小程序插件：支持，需要小程序基础库版本不低于2.11.1

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.bind.html

---

### UDPSocket.close()

小程序插件：支持，需要小程序基础库版本不低于2.11.1

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.close.html

---

### UDPSocket.connect(Object object)

基础库 2.15.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.connect.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| address | string |  | 是 | 要发消息的地址 |
| port | number |  | 是 | 要发送消息的端口号 |

---

### UDPSocket.offClose(function listener)

小程序插件：支持，需要小程序基础库版本不低于2.11.1

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.offClose.html

---

### UDPSocket.offError(function listener)

小程序插件：支持，需要小程序基础库版本不低于2.11.1

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.offError.html

---

### UDPSocket.offListening(function listener)

小程序插件：支持，需要小程序基础库版本不低于2.11.1

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.offListening.html

---

### UDPSocket.offMessage(function listener)

小程序插件：支持，需要小程序基础库版本不低于2.11.1

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.offMessage.html

---

### UDPSocket.onClose(function listener)

小程序插件：支持，需要小程序基础库版本不低于2.11.1

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.onClose.html

---

### UDPSocket.onError(function listener)

小程序插件：支持，需要小程序基础库版本不低于2.11.1

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.onError.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |

---

### UDPSocket.onListening(function listener)

小程序插件：支持，需要小程序基础库版本不低于2.11.1

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.onListening.html

---

### UDPSocket.onMessage(function listener)

小程序插件：支持，需要小程序基础库版本不低于2.11.1

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.onMessage.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | message | ArrayBuffer | 收到的消息。消息长度需要小于4096。 |
|  | remoteInfo | Object | 发送端地址信息 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | address | string | 发送消息的 socket 的地址 | |  | family | string | 使用的协议族，为 IPv4 或者 IPv6 | |  | port | number | 端口号 | |  | size | number | message 的大小，单位：字节 | | | |
|  | localInfo | Object | 接收端地址信息，2.18.0 起支持 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | address | string | 接收消息的 socket 的地址 | |  | family | string | 使用的协议族，为 IPv4 或者 IPv6 | |  | port | number | 端口号 | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | address | string | 发送消息的 socket 的地址 |
|  | family | string | 使用的协议族，为 IPv4 或者 IPv6 |
|  | port | number | 端口号 |
|  | size | number | message 的大小，单位：字节 |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | address | string | 接收消息的 socket 的地址 |
|  | family | string | 使用的协议族，为 IPv4 或者 IPv6 |
|  | port | number | 端口号 |

---

### UDPSocket.send(Object object)

小程序插件：支持，需要小程序基础库版本不低于2.11.1

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.send.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| address | string |  | 是 | 要发消息的地址。在基础库 <= 2.9.3 版本必须是和本机同网段的 IP 地址，或安全域名列表内的域名地址；之后版本可以是任意 IP 和域名 |
| port | number |  | 是 | 要发送消息的端口号 |
| message | string/ArrayBuffer |  | 是 | 要发送的数据 |
| offset | number | 0 | 否 | 发送数据的偏移量，仅当 message 为 ArrayBuffer 类型时有效 |
| length | number | message.byteLength | 否 | 发送数据的长度，仅当 message 为 ArrayBuffer 类型时有效 |
| setBroadcast | boolean | false | 否 | 向指定地址发消息时，是否要开启广播，基础库 2.24.0 开始支持 |

---

### UDPSocket.setTTL(number ttl)

基础库 2.18.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.setTTL.html

---

### UDPSocket.write(Object object)

基础库 2.15.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.write.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| address | string |  | 是 | 要发消息的地址。在基础库 <= 2.9.3 版本必须是和本机同网段的 IP 地址，或安全域名列表内的域名地址；之后版本可以是任意 IP 和域名 |
| port | number |  | 是 | 要发送消息的端口号 |
| message | string/ArrayBuffer |  | 是 | 要发送的数据 |
| offset | number | 0 | 否 | 发送数据的偏移量，仅当 message 为 ArrayBuffer 类型时有效 |
| length | number | message.byteLength | 否 | 发送数据的长度，仅当 message 为 ArrayBuffer 类型时有效 |
| setBroadcast | boolean | false | 否 | 向指定地址发消息时，是否要开启广播，基础库 2.24.0 开始支持 |

---

<!-- pages: 77 -->
