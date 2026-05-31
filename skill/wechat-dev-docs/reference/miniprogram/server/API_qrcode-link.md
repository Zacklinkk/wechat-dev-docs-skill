# 小程序服务端 API 结构化参考 — API/qrcode-link

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 获取小程序码

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/qrcode-link/qr-code/api_getqrcode.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 扫码进入的小程序页面路径，最大长度 1024 个字符，不能为空，scancode\_time为系统保留参数，不允许配置；对于小游戏，可以只传入 query 部分，来实现传参效果，如：传入 "?foo=bar"，即可在 wx.getLaunchOptionsSync 接口中的 query 参数获取到 {foo:"bar"}。 |
| width | number | 否 | 二维码的宽度，单位 px。默认值为430，最小 280px，最大 1280px |
| auto\_color | boolean | 否 | 默认值false；自动配置线条颜色，如果颜色依然是黑色，则说明不建议配置主色调 |
| line\_color | [object](#Body__line_color) | 否 | 默认值{"r":0,"g":0,"b":0} ；auto\_color 为 false 时生效，使用 rgb 设置颜色 例如 {"r":"xxx","g":"xxx","b":"xxx"} 十进制表示 |
| is\_hyaline | boolean | 否 | 默认值false；是否需要透明底色，为 true 时，生成透明底色的小程序码 |
| env\_version | string | 否 | 要打开的小程序版本。正式版为 "release"，体验版为 "trial"，开发版为 "develop"。默认是正式版。 |

**Body.line_color Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| r | - | 是 | 默认值{"r":0,"g":0,"b":0} ；auto\_color 为 false 时生效，使用 rgb 设置颜色 例如 {"r":"xxx","g":"xxx","b":"xxx"} 十进制表示 |
| g | - | 是 | 默认值{"r":0,"g":0,"b":0} ；auto\_color 为 false 时生效，使用 rgb 设置颜色 例如 {"r":"xxx","g":"xxx","b":"xxx"} 十进制表示 |
| b | - | 是 | 默认值{"r":0,"g":0,"b":0} ；auto\_color 为 false 时生效，使用 rgb 设置颜色 例如 {"r":"xxx","g":"xxx","b":"xxx"} 十进制表示 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| buffer | buffer | 图片 Buffer |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40097 | invalid args | 参数错误 |
| 40159 | invalid length for path  or thedata is not json string | path 不能为空，且长度不能大于1024 |
| 45029 | qrcode count out of limit | 生成码个数总和到达最大个数限制 |
| 85096 | not allow include scancode\_time field | scancode\_time为系统保留参数，不允许配置 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取不限制的小程序码

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/qrcode-link/qr-code/api_getunlimitedqrcode.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scene | string | 是 | 最大32个可见字符，只支持数字，大小写英文以及部分特殊字符：!#$&'()\*+,/:;=?@-.\_~，其它字符请自行编码为合法字符（因不支持%，中文无法使用 urlencode 处理，请使用其他编码方式） |
| page | string | 否 | 默认是主页，页面 page，例如 pages/index/index，根路径前不要填加 /，不能携带参数（参数请放在scene字段里），如果不填写这个字段，默认跳主页面。scancode\_time为系统保留参数，不允许配置 |
| check\_path | boolean | 否 | 默认是true，检查page 是否存在，为 true 时 page 必须是已经发布的小程序存在的页面（否则报错）；为 false 时允许小程序未发布或者 page 不存在， 但page 有数量上限（60000个）请勿滥用。 |
| env\_version | string | 否 | 要打开的小程序版本。正式版为 "release"，体验版为 "trial"，开发版为 "develop"。默认是正式版。 |
| width | number | 否 | 默认430，二维码的宽度，单位 px，最小 280px，最大 1280px |
| auto\_color | boolean | 否 | 自动配置线条颜色，如果颜色依然是黑色，则说明不建议配置主色调，默认 false |
| line\_color | [object](#Body__line_color) | 否 | 默认是{"r":0,"g":0,"b":0} 。auto\_color 为 false 时生效，使用 rgb 设置颜色 例如 {"r":"xxx","g":"xxx","b":"xxx"} 十进制表示 |
| is\_hyaline | boolean | 否 | 默认是false，是否需要透明底色，为 true 时，生成透明底色的小程序 |

**Body.line_color Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| r | - | 是 | 默认值{"r":0,"g":0,"b":0} ；auto\_color 为 false 时生效，使用 rgb 设置颜色 例如 {"r":"xxx","g":"xxx","b":"xxx"} 十进制表示 |
| g | - | 是 | 默认值{"r":0,"g":0,"b":0} ；auto\_color 为 false 时生效，使用 rgb 设置颜色 例如 {"r":"xxx","g":"xxx","b":"xxx"} 十进制表示 |
| b | - | 是 | 默认值{"r":0,"g":0,"b":0} ；auto\_color 为 false 时生效，使用 rgb 设置颜色 例如 {"r":"xxx","g":"xxx","b":"xxx"} 十进制表示 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| buffer | buffer | 图片 Buffer |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40097 | invalid args | 参数错误 |
| 40129 | invalid scene | 最大32个可见字符，只支持数字，大小写英文以及部分特殊字符：!#$&'()\*+,/:;=?@-.\_~，其它字符请自行编码为合法字符（因不支持%，中文无法使用 urlencode 处理，请使用其他编码方式） |
| 40169 | invalid length for scene  or thedata is not json string | scene 不合法 |
| 41030 | invalid page | page路径不正确：根路径前不要填加 /，不能携带参数（参数请放在scene字段里），需要保证在现网版本小程序中存在，与app.json保持一致。 设置check\_path=false可不检查page参数。 |
| 85096 | not allow include scancode\_time field | scancode\_time为系统保留参数，不允许配置 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取小程序二维码

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/qrcode-link/qr-code/api_createqrcode.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 扫码进入的小程序页面路径，最大长度 128 个字符，不能为空；对于小游戏，可以只传入 query 部分，来实现传参效果，如：传入 "?foo=bar"，即可在 wx.getLaunchOptionsSync 接口中的 query 参数获取到 {foo:"bar"}。scancode\_time为系统保留参数，不允许配置。 |
| width | number | 否 | 二维码的宽度，单位 px。最小 280px，最大 1280px;默认是430 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| buffer | formdata | 图片 Buffer |
| errcode | string | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40159 | invalid length for path, or the data is not json string | path 不能为空，且长度不能大于 128 字节 |
| 45029 | qrcode count out of limit | 生成码个数总和到达最大个数限制 |
| 85096 | page or path not allow include scancode\_time field | scancode\_time为系统保留参数，不允许配置 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 查询scheme码

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/qrcode-link/url-scheme/api_queryscheme.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scheme | string | 否 | 小程序 scheme 码。支持加密 scheme 和明文 scheme |
| query\_type | number | 否 | 查询类型。默认值0，查询 scheme 码信息：0， 查询每天剩余访问次数：1 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| scheme\_info | [object](#Res__scheme_info) | scheme 信息 |
| quota\_info | [object](#Res__quota_info) | quota 配置 |

**Res.scheme_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| appid | string | 小程序 appid |
| path | string | 小程序页面路径 |
| query | string | 小程序页面query |
| create\_time | number | 创建时间，为 Unix 时间戳 |
| expire\_time | number | 到期失效时间，为 Unix 时间戳，0 表示永久生效 |
| env\_version | string | 要打开的小程序版本。正式版为"release"，体验版为"trial"，开发版为"develop" |

**Res.quota_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| remain\_visit\_quota | number | URL Scheme（加密+明文）/加密 URL Link 单天剩余访问次数 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 0 | ok | ok |
| 40002 | invalid grant\_type | 暂无生成权限（非个人主体小程序无权限，未申请 NFC 能力的小程序无权限） |
| 40097 | invalid args | 参数错误 |
| 40165 | invalid weapp pagepath | 参数path填写错误，更正后重试 |
| 40212 | invalid query | 参数query填写错误 ，query格式遵循URL标准，即k1=v1&k2=v2 |
| 85402 | invalid env\_version | 参数env\_version填写错误，更正后重试 |
| 85403 | not found | scheme/url link不存在 |
| 85405 | appid or path not support plain scheme | 小程序 appid 或者 path 未开启明文 scheme |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取加密scheme码

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/qrcode-link/url-scheme/api_generatescheme.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jump\_wxa | [object](#Body__jump_wxa) | 否 | 跳转到的目标小程序信息。 |
| expire\_time | number | 否 | 到期失效的 scheme 码的失效时间，为 Unix 时间戳。生成的到期失效 scheme 码在该时间前有效。最长有效期为30天。is\_expire 为 true 且 expire\_type 为 0 时必填 |
| expire\_type | number | 否 | 默认值0，到期失效的 scheme 码失效类型，失效时间：0，失效间隔天数：1 |
| expire\_interval | number | 否 | 到期失效的 scheme 码的失效间隔天数。生成的到期失效 scheme 码在该间隔时间到达前有效。最长间隔天数为30天。is\_expire 为 true 且 expire\_type 为 1 时必填 |

**Body.jump_wxa Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 否 | 通过 scheme 码进入的小程序页面路径，必须是已经发布的小程序存在的页面，不可携带 query。path 为空时会跳转小程序主页。 |
| query | string | 否 | 通过 scheme 码进入小程序时的 query，最大1024个字符，只支持数字，大小写英文以及部分特殊字符：`!#$&'()\*+,/:;=?@-.\_~%`` |
| env\_version | string | 否 | 默认值"release"。要打开的小程序版本。正式版为"release"，体验版为"trial"，开发版为"develop"，仅在微信外打开时生效。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| openlink | string | 生成的小程序 scheme 码 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40002 | invalid grant\_type | 暂无生成权限（个人主体小程序无权限，或者NFC 能力的小程序未申请权限） |
| 40013 | invalid appid | 生成权限被封禁 |
| 40165 | invalid weapp pagepath | 参数path填写错误，更正后重试 |
| 40212 | invalid query | 参数query填写错误 ，query格式遵循URL标准，即k1=v1&k2=v2 |
| 44990 | reach max api second frequence limit | 频率过快，超过100次/秒；降低调用频率 |
| 44993 | reach max api day frequence limit | 单天生成加密 URL Scheme+URL Link 数量超过上限50万 |
| 85079 | miniprogram has no online release | 小程序没有线上版本，即小程序尚未发布，不可进行该操作 |
| 85401 | time limit between 1min and 30days | 参数expire\_time填写错误，时间间隔大于1分钟且小于30天，更正后重试 |
| 85402 | invalid env\_version | 参数env\_version填写错误，更正后重试 |
| 85406 | daily visit limit | URL Scheme（加密+明文）/加密 URL Link 单天累加访问次数超过上限 |
| 85407 | no scheme permission | 暂无生成权限 |
| 85408 | appid banned | 生成权限被封禁 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取NFC的小程序scheme

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/qrcode-link/url-scheme/api_generatenfcscheme.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jump\_wxa | [object](#Body__jump_wxa) | 否 | 跳转到的目标小程序信息。 |
| model\_id | string | 是 | scheme对应的设备model\_id |
| sn | string | 否 | scheme对应的设备sn，仅一机一码时填写 |

**Body.jump_wxa Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 否 | 通过 scheme 码进入的小程序页面路径，必须是已经发布的小程序存在的页面，不可携带 query。path 为空时会跳转小程序主页 |
| query | string | 否 | 通过 scheme 码进入小程序时的 query，最大1024个字符，只支持数字，大小写英文以及部分特殊字符：`!#$&'()\*+,/:;=?@-.\_~%`` |
| env\_version | string | 否 | 要打开的小程序版本。正式版为"release"，体验版为"trial"，开发版为"develop"，仅在微信外打开时生效 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| openlink | string | 生成的小程序 scheme 码 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40002 | 暂无生成权限（非个人主体小程序无权限，未申请 NFC 能力的小程序无权限） |  |
| 40013 | 生成权限被封禁 |  |
| 40165 | invalid weapp pagepath | 参数path填写错误，更正后重试 |
| 40212 | invalid query | 参数query填写错误 ，query格式遵循URL标准，即k1=v1&k2=v2 |
| 44990 | reach max api second frequence limit | 频率过快，超过100次/秒；降低调用频率 |
| 44993 | reach max api day frequence limit | 单天生成Scheme+URL Link数量超过上限50万 |
| 85079 | miniprogram has no online release | 小程序没有线上版本，即小程序尚未发布，不可进行该操作 |
| 85402 | invalid env\_version | 参数env\_version填写错误，更正后重试 |
| 9800003 | model\_id检查不通过 |  |
| 9800007 | 此model\_id尚未获得该能力，请能力申请通过后再试 |  |
| 9800008 | 能力类型为一机一码，sn不能为空 |  |
| 9800009 | 能力类型为一型一码，sn需为空 |  |

---

### 获取加密URLLink

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/qrcode-link/url-link/api_generateurllink.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 否 | 通过 URL Link 进入的小程序页面路径，必须是已经发布的小程序存在的页面，不可携带 query 。path 为空时会跳转小程序主页 |
| query | string | 否 | 通过 URL Link 进入小程序时的query，最大1024个字符，只支持数字，大小写英文以及部分特殊字符：!#$&'()\*+,/:;=?@-.\_~% |
| expire\_type | number | 否 | 默认值0.小程序 URL Link 失效类型，失效时间：0，失效间隔天数：1 |
| expire\_time | number | 否 | 到期失效的 URL Link 的失效时间，为 Unix 时间戳。生成的到期失效 URL Link 在该时间前有效。最长有效期为30天。expire\_type 为 0 必填 |
| expire\_interval | number | 否 | 到期失效的URL Link的失效间隔天数。生成的到期失效URL Link在该间隔时间到达前有效。最长间隔天数为30天。expire\_type 为 1 必填 |
| cloud\_base | [object](#Body__cloud_base) | 否 | 云开发静态网站自定义 H5 配置参数，可配置中转的云开发 H5 页面。不填默认用官方 H5 页面 |
| env\_version | string | 否 | 默认值"release"。要打开的小程序版本。正式版为 "release"，体验版为"trial"，开发版为"develop"，仅在微信外打开时生效。 |

**Body.cloud_base Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| env | string | 是 | 云开发环境 |
| domain | string | 否 | 静态网站自定义域名，不填则使用默认域名 |
| path | string | 否 | 云开发静态网站 H5 页面路径，不可携带 query |
| query | string | 否 | 云开发静态网站 H5 页面 query 参数，最大 1024 个字符，只支持数字，大小写英文以及部分特殊字符：`!#$&'()\*+,/:;=?@-.\_~%`` |
| resource\_appid | string | 否 | 第三方批量代云开发时必填，表示创建该 env 的 appid （小程序/第三方平台） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| url\_link | string | 生成的小程序 URL Link |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40002 | invalid grant\_type | 暂无生成权限（个人主体小程序无权限，或者NFC 能力的小程序未申请权限） |
| 40013 | invalid appid | 生成权限被封禁 |
| 40165 | invalid weapp pagepath | 参数path填写错误，更正后重试 |
| 40212 | invalid query | 参数query填写错误 ，query格式遵循URL标准，即k1=v1&k2=v2 |
| 44990 | reach max api second frequence limit | 频率过快，超过100次/秒；降低调用频率 |
| 44993 | reach max api day frequence limit | 单天生成加密 URL Scheme+URL Link 数量超过上限50万 |
| 85079 | miniprogram has no online release | 小程序没有线上版本，即小程序尚未发布，不可进行该操作 |
| 85088 | 未开通云开发 | 请先开通云开发 |
| 85401 | time limit between 1min and 30days | 参数expire\_time填写错误，时间间隔大于1分钟且小于30天，更正后重试 |
| 85402 | invalid env\_version | 参数env\_version填写错误，更正后重试 |
| 85406 | daily visit limit | URL Scheme（加密+明文）/加密 URL Link 单天累加访问次数超过上限 |
| 85407 | no scheme permission | 暂无生成权限 |
| 85408 | appid banned | 生成权限被封禁 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 查询加密URLLink

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/qrcode-link/url-link/api_queryurllink.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url\_link | string | 否 | 小程序加密 url\_link。 |
| query\_type | number | 否 | 查询类型。默认值0，查询 url\_link 信息：0， 查询每天剩余访问次数：1 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| url\_link\_info | [object](#Res__url_link_info) | url\_link 配置 |
| quota\_info | [object](#Res__quota_info) | quota 配置 |

**Res.url_link_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| appid | string | 小程序 appid |
| path | string | 小程序页面路径 |
| query | string | 小程序页面query |
| create\_time | number | 创建时间，为 Unix 时间戳 |
| expire\_time | number | 到期失效时间，为 Unix 时间戳，0 表示永久生效 |
| env\_version | string | 要打开的小程序版本。正式版为"release"，体验版为"trial"，开发版为"develop" |

**Res.quota_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| remain\_visit\_quota | number | URL Scheme（加密+明文）/加密 URL Link 单天剩余访问次数 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40097 | invalid args | 参数错误 |
| 85403 | not found | scheme/url link不存在 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取ShortLink

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/qrcode-link/short-link/api_generateshortlink.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| page\_url | string | 是 | 通过 Short Link 进入的小程序页面路径，必须是已经发布的小程序存在的页面，可携带 query，最大1024个字符 |
| page\_title | string | 否 | 短链标题，可自定义，不能包含违法信息，超过20字符会用... 截断代替 |
| is\_permanent | boolean | 否 | 默认值false。生成的 Short Link 类型，短期有效：false，永久有效：true |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| errcode | number | [错误码](#apierrcode) | [枚举值](#Enum_Res__errcode) |
| errmsg | string | [错误信息](#apierrcode) | - |
| link | string | 生成的小程序 Short Link | - |

**Res.errcode Enum**

| 枚举值 | 描述 |
| --- | --- |
| 40001 | invalid credential access\_token isinvalid or not latest； 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40066 | invalid url；url不存在，即，已发布小程序没有对应url |
| 40225 | invalid page title；无效的页面标题 |
| 85400 | reach max long time quota limit；长期有效Scheme或short link达到生成上限10万，不可再生成。 |
| 45009 | 单天生成Short Link数量超过上限1000万 |
| 43104 | this appid does not have permission；没有调用权限，参考api权限限制 |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40066 | invalid url | url不存在，即，已发布小程序没有对应url |
| 40225 | invalid page title | 无效的页面标题 |
| 43104 | this appid does not have permission | 没有调用权限，目前只开放给电商类目（具体包含以下一级类目：电商平台、商家自营、跨境电商） |
| 45009 | 单天生成Short Link数量超过上限1000万 |  |
| 85400 | reach max long time quota limit | 长期有效Scheme或short link达到生成上限10万，不可再生成。 |

---

<!-- pages: 9 -->
