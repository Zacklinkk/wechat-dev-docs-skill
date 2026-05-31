# 小程序服务端 API 结构化参考 — API/hardware-device

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 发送设备消息

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/hardware-device/api_sendhardwaredevicemessage.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| template\_id | string | 是 | 所需下发的订阅模板id |
| sn | string | 是 | 设备唯一序列号。由厂商分配，长度不能超过128字节。字符只接受数字，大小写字母，下划线（\_）和连字符（-）。 |
| page | string | 是 | 点击模板卡片后的跳转页面，仅限本小程序内的页面。支持带参数,（示例index?foo=bar）。该字段不填则模板无跳转。 |
| to\_openid\_list | array | 是 | 接收者（用户）的 openid 列表 |
| miniprogram\_state | string | 否 | 跳转小程序类型：developer为开发版；trial为体验版；formal为正式版；默认为正式版 |
| modelId | string | 是 | 设备型号 id ，通过注册设备获得。 |
| data | string | 是 | 这是个object，不是string。模板内容，格式形如 { "key1": { "value": "xxx" }, "key2": { "value": "xxx" } } ，value 为枚举值。 |
| lang | string | 是 | 进入小程序查看”的语言类型，支持zh\_CN(简体中文)、en\_US(英文)、zh\_HK(繁体中文)、zh\_TW(繁体中文)，默认为zh\_CN |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40037 | invalid template\_id | 不合法的 template\_id |
| 41030 | invalid page | page路径不正确，需要保证在现网版本小程序中存在，与app.json保持一致 |
| 43101 | user refuse to accept the msg | 用户拒绝接受消息，如果用户之前曾经订阅过，则表示用户取消了订阅关系 |
| 47003 | argument invalid! | 模板参数不准确，可能为空或者不满足规则，errmsg会提示具体是哪个字段出错 |

---

### 获取设备票据

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/hardware-device/api_getsnticket.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sn | string | 是 | sn 设备唯一序列号。由厂商分配，长度不能超过128字节。字符只接受数字，大小写字母，下划线（\_）和连字符（-）。 |
| model\_id | string | 是 | 设备型号 id ，通过注册设备获得。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| sn\_ticket | string | 设备票据，5分钟内有效。 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 9800001 | sn长度不能超过128字节 |  |
| 9800002 | sn包含非法字符，请参考文档 |  |
| 9800003 | model\_id检查不通过 |  |

---

### 创建设备组

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/hardware-device/api_createiotgroupid.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model\_id | string | 是 | 设备型号的唯一标识。 |
| group\_name | string | 是 | 设备组的名称（创建时时决定，无法修改） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| group\_id | string | 设备组的唯一标识 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 43002 | require POST method | 方法调用错误，请用 post 方法调用 |
| 44002 | empty post data | POST 的数据包为空。post请求body参数不能为空。 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;参数需以 JSON 字符串格式写在post请求的 body 中，请检查修正后重试 |
| 9800003 | model\_id检查不通过 | 检查model\_id |
| 9800012 | group\_name 不合法，长度应为 1-32 字节 | 检查 group\_name 字段 |

---

### 查询设备组信息

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/hardware-device/api_getiotgroupinfo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| group\_id | string | 是 | 设备组的唯一标识 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| group\_name | string | 设备名称 |
| device\_list | [objarray](#Res__device_list<Array>) | 设备列表 |
| model\_id | string | 设备型号的唯一标识 |
| model\_type | string | 设备类型 |

**Res.device_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| model\_id | string | 设备型号 id。通过微信公众平台注册设备获得。 |
| sn | string | 设备唯一序列号。由厂商分配。 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 43002 | require POST method | 方法调用错误，请用 post 方法调用 |
| 44002 | empty post data | POST 的数据包为空。post请求body参数不能为空。 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;参数需以 JSON 字符串格式写在post请求的 body 中，请检查修正后重试 |
| 9800013 | group\_id不合法 | 检查group\_id |

---

### 设备组添加设备

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/hardware-device/api_addiotgroupdevice.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| group\_id | string | 是 | 设备组的唯一标识 |
| device\_list | [objarray](#Body__device_list<Array>) | 是 | 设备列表 |
| force\_add | boolean | 否 | 是否强制更新设备列表，等于 true 时将已存在其它设备组中的设备移除并添加到当前设备组，慎用。 |

**Body.device_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model\_id | string | 是 | 设备型号 id。通过微信公众平台注册设备获得。 |
| sn | string | 是 | 设备唯一序列号。由厂商分配。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| device\_list | [objarray](#Res__device_list<Array>) | 设备列表 |

**Res.device_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| model\_id | string | 设备型号 id。通过微信公众平台注册设备获得。 |
| sn | string | 设备唯一序列号。由厂商分配。 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 43002 | require POST method | 方法调用错误，请用 post 方法调用 |
| 44002 | empty post data | POST 的数据包为空。post请求body参数不能为空。 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;参数需以 JSON 字符串格式写在post请求的 body 中，请检查修正后重试 |
| 9800013 | group\_id不合法 | 检查group\_id |
| 9800014 | 设备类型与设备组不符合 | 检查model id的设备类型 |
| 9800015 | 该设备已存在于设备组 | 检查该sn是否已添加 |
| 9800016 | 设备组中设备数到达上限 | 检查设备组中的设备个数 |
| 9800018 | 该设备已经属于另一个设备组 | 检查设备是否已添加 |
| 9800044 | 已扩容至最大设备数量 | 检查组内的设备数量 |

---

### 设备组删除设备

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/hardware-device/api_removeiotgroupdevice.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| group\_id | string | 是 | 设备组的唯一标识 |
| device\_list | [objarray](#Body__device_list<Array>) | 是 | 设备列表 |

**Body.device_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model\_id | string | 是 | 设备型号 id。通过微信公众平台注册设备获得。 |
| sn | string | 是 | 设备唯一序列号。由厂商分配。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| device\_list | [objarray](#Res__device_list<Array>) | 设备列表 |

**Res.device_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| model\_id | string | 设备型号唯一标识 |
| sn | string | 设备的唯一标识 |
| errcode | number | 错误码 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 43002 | require POST method | 方法调用错误，请用 post 方法调用 |
| 44002 | empty post data | POST 的数据包为空。post请求body参数不能为空。 |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;参数需以 JSON 字符串格式写在post请求的 body 中，请检查修正后重试 |
| 9800013 | group\_id不合法 | 检查group\_id |
| 9800017 | 该设备不属于设备组 | 检查设备是否添加到设备组中 |

---

### 查询license资源包列表

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/hardware-device/api_getlicensepkglist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pkg\_type | number | 是 | 资源包类型，0：测试体验包，1：A 类设备，2：B 类设备，3：C 类设备，4：D 类设备，5：E类设备 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| pkg\_list | [objarray](#Res__pkg_list<Array>) | 资源包列表 |
| max\_active\_number | number | 最大激活码序号，已废弃。 |

**Res.pkg_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| pkg\_id | string | 资源包 ID |
| pkg\_type | number | 资源包类型 |
| start\_time | number | 资源包下单时间 |
| end\_time | number | 资源包过期时间 |
| pkg\_status | number | 资源包状态，1为已生效，2为未生效，3为已过期 |
| used | number | 已使用额度 |
| all | number | 资源包总量 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok | ok |

---

### 激活设备license

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/hardware-device/api_activelicensedevice.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device\_list | [objarray](#Body__device_list<Array>) | 是 | 待激活的设备列表 |
| pkg\_type | number | 是 | 资源包类型，0：测试体验包（默认），1：A 类设备，2：B 类设备，3：C 类设备，4：D 类设备，5：E类设备 |

**Body.device_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model\_id | string | 是 | 设备型号 id。通过微信公众平台注册设备获得。 |
| sn | string | 是 | 设备唯一序列号。由厂商分配。 |
| active\_number | number | 是 | 激活码序号，任意 uint32 整数（需与之前使用过的不重复）。主要用于防止重复请求导致重复激活。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| device\_list | [objarray](#Res__device_list<Array>) | 设备列表 |

**Res.device_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| model\_id | string | 设备型号唯一标识 |
| sn | string | 设备的唯一标识 |
| expire\_time | number | 设备的过期时间 |
| errcode | number | 错误码 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok | ok |
| 9800020 | 设备数超出限制 | 检查设备数量 |
| 9800020 | 设备数超出限制 | 检查设备数量 |
| 9800037 | 激活码序号已使用 | 更换激活码序号 |
| 9800038 | 设备有效期超出限制 | 检查设备有效期 |
| 9800039 | 资源包余额不足 | 检查资源包余额 |
| 9800040 | 资源包类型和设备类型不匹配 | 检查设备类型 |

---

### 查询设备激活详情

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/hardware-device/api_getlicensedeviceinfo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device\_list | [objarray](#Body__device_list<Array>) | 是 | 设备列表 |

**Body.device_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model\_id | string | 是 | 设备型号 id。通过微信公众平台注册设备获得。 |
| sn | string | 是 | 设备唯一序列号。由厂商分配。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| device\_list | [objarray](#Res__device_list<Array>) | 设备列表 |

**Res.device_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| model\_id | string | 设备型号唯一标识 |
| sn | string | 设备的唯一标识 |
| expire\_time | number | 设备的过期时间 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok | ok |

---

<!-- pages: 9 -->
