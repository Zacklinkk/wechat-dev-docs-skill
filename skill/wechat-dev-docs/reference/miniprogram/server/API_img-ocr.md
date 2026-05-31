# 小程序服务端 API 结构化参考 — API/img-ocr

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 图片智能裁剪

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/img-ocr/img/api_imgaicrop.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOCKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| img\_url | string | 否 | ENCODE\_URL | 要检测的图片 url，传这个则不用传 img 参数。 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| img | formdata | 否 | 图片文件，小于2M |
| ratios | string | 否 | 宽高比；如果提供多个宽高比，请以英文逗号“,”分隔，最多支持5个宽高比 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| results | [objarray](#Res__results<Array>) | 智能裁剪结果 |
| img\_size | [object](#Res__img_size) | 图片大小 |

**Res.results(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| crop\_left | number | 左上角x |
| crop\_top | number | 左上角y |
| crop\_right | number | 右下角x |
| crop\_bottom | number | 右下角y |

**Res.img_size Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| w | number | 宽度 |
| h | number | 高度 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统错误 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 101000 | invalid image url | 图片URL错误 |
| 101002 | invalid image data | 图片数据无效 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 |
| --- | --- | --- |
| ✔ | 仅认证 | 仅认证 |

---

### 二维码/条码识别

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/img-ocr/img/api_imgqrcode.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| img\_url | string | 否 | https://example.com/img.jpg | 图片URL地址 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| img | formdata | 否 | 图片文件，限制小于 2 M |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| code\_results | [objarray](#Res__code_results<Array>) | 处理结果 |
| img\_size | [object](#Res__img_size) | 图片大小 |

**Res.code_results(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| type\_name | string | 码的类型 |
| data | string | 码的信息 |
| pos | [object](#Res__code_results<Array>__pos) | 码的坐标 |

**Res.img_size Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| w | number | 宽度 |
| h | number | 高度 |

**Res.code_results(Array).pos Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| left\_top | [object](#Res__code_results<Array>__pos__left_top) | 左上角位置 |
| right\_top | [object](#Res__code_results<Array>__pos__right_top) | 右上角位置 |
| right\_bottom | [object](#Res__code_results<Array>__pos__right_bottom) | 右下角位置 |
| left\_bottom | [object](#Res__code_results<Array>__pos__left_bottom) | 左下角位置 |

**Res.code_results(Array).pos.left_top Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| x | number | x坐标 |
| y | number | y坐标 |

**Res.code_results(Array).pos.right_top Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| x | number | x坐标 |
| y | number | y坐标 |

**Res.code_results(Array).pos.right_bottom Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| x | number | x坐标 |
| y | number | y坐标 |

**Res.code_results(Array).pos.left_bottom Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| x | number | x坐标 |
| y | number | y坐标 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统错误 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 101000 | invalid image url | 图片URL错误 |
| 101002 | invalid image data | 图片数据无效 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 |
| --- | --- | --- |
| ✔ | 仅认证 | 仅认证 |

---

### 图片高清化

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/img-ocr/img/api_imgsuperresolution.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| img\_url | - | 否 | 图片链接 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| img | formdata | 否 | 图片文件 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| media\_id | string | media id |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 |
| --- | --- | --- |
| ✔ | 仅认证 | 仅认证 |

---

### 通用印刷体识别

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/img-ocr/ocr/api_commocr.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOCKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| img\_url | string | 否 | ENCODE\_URL | 要检测的图片 url，传这个则不用传 img 参数。 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| img | formdata | 否 | form-data 中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img\_url。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |
| items | [objarray](#Res__items<Array>) | 识别结果 |
| img\_size | [object](#Res__img_size) | 图片大小 |

**Res.items(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| pos | [object](#Res__items<Array>__pos) | 位置信息 |

**Res.img_size Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| w | number | 宽度 |
| h | number | 高度 |

**Res.items(Array).pos Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| left\_top | [object](#Res__items<Array>__pos__left_top) | 左上角位置 |
| right\_top | [object](#Res__items<Array>__pos__right_top) | 右上角位置 |
| right\_bottom | [object](#Res__items<Array>__pos__right_bottom) | 右下角位置 |
| left\_bottom | [object](#Res__items<Array>__pos__left_bottom) | 左下角位置 |

**Res.items(Array).pos.left_top Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| x | number | x坐标 |
| y | number | y坐标 |

**Res.items(Array).pos.right_top Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| x | number | x坐标 |
| y | number | y坐标 |

**Res.items(Array).pos.right_bottom Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| x | number | x坐标 |
| y | number | y坐标 |

**Res.items(Array).pos.left_bottom Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| x | number | x坐标 |
| y | number | y坐标 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 101000 | invalid image url |  |
| 101002 | decode image failed | 图片大小超过限制，resp\_type = 0: 2MB，resp\_type = 1: 10MB |
| 101003 | not enough market quota |  |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 |
| --- | --- | --- |
| ✔ | 仅认证 | 仅认证 |

---

### 行驶证识别

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/img-ocr/ocr/api_drivingocr.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOCKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| img\_url | string | 否 | ENCODE\_URL | 要检测的图片 url，传这个则不用传 img 参数。 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| img | formdata | 是 | form-data 中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img\_url。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| plate\_num | string | 车牌号码 |
| vehicle\_type | string | 车辆类型 |
| owner | string | 所有人 |
| addr | string | 住址 |
| use\_character | string | 使用性质 |
| model | string | 品牌型号 |
| vin | string | 车辆识别代号 |
| engine\_num | string | 发动机号码 |
| register\_date | string | 注册日期 |
| issue\_date | string | 发证日期 |
| plate\_num\_b | string | 车牌号码 |
| record | string | 号牌 |
| passengers\_num | string | 核定载人数 |
| total\_quality | string | 总质量 |
| prepare\_quality | string | 整备质量 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 101000 | invalid image url |  |
| 101003 | not enough market quota |  |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 |
| --- | --- | --- |
| ✔ | 仅认证 | 仅认证 |

---

### 银行卡识别

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/img-ocr/ocr/api_bankcardocr.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOCKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| img\_url | string | 否 | ENCODE\_URL | 要检测的图片 url，传这个则不用传 img 参数。 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| img | formdata | 是 | form-data 中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img\_url。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| number | string | 银行卡号 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 101000 | invalid image url |  |
| 101001 | certificate not found |  |
| 101003 | not enough market quota |  |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 |
| --- | --- | --- |
| ✔ | 仅认证 | 仅认证 |

---

### 营业执照识别

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/img-ocr/ocr/api_bizlicenseocr.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOCKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| img\_url | string | 否 | ENCODE\_URL | 要检测的图片 url，传这个则不用传 img 参数。 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| img | formdata | 是 | form-data 中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img\_url。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| reg\_num | string | 注册号 |
| serial | string | 编号 |
| legal\_representative | string | 法定代表人姓名 |
| enterprise\_name | string | 企业名称 |
| type\_of\_organization | string | 组成形式 |
| address | string | 经营场所/企业住所 |
| type\_of\_enterprise | string | 公司类型 |
| business\_scope | string | 经营范围 |
| registered\_capital | string | 注册资本 |
| paid\_in\_capital | string | 实收资本 |
| valid\_period | string | 营业期限 |
| registered\_date | string | 注册日期/成立日期 |
| cert\_position | [object](#Res__cert_position) | 营业执照位置 |
| img\_size | [object](#Res__img_size) | 图片大小 |

**Res.cert_position Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| pos | [object](#Res__cert_position__pos) | 位置信息 |

**Res.img_size Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| w | number | 宽度 |
| h | number | 高度 |

**Res.cert_position.pos Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| left\_top | [object](#Res__cert_position__pos__left_top) | 左上角位置 |
| right\_top | [object](#Res__cert_position__pos__right_top) | 右上角位置 |
| right\_bottom | [object](#Res__cert_position__pos__right_bottom) | 右下角位置 |
| left\_bottom | [object](#Res__cert_position__pos__left_bottom) | 左下角位置 |

**Res.cert_position.pos.left_top Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| x | number | x坐标 |
| y | number | y坐标 |

**Res.cert_position.pos.right_top Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| x | number | x坐标 |
| y | number | y坐标 |

**Res.cert_position.pos.right_bottom Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| x | number | x坐标 |
| y | number | y坐标 |

**Res.cert_position.pos.left_bottom Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| x | number | x坐标 |
| y | number | y坐标 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 101000 | invalid image url |  |
| 101001 | certificate not found |  |
| 101002 | decode image failed | 图片大小超过限制，resp\_type = 0: 2MB，resp\_type = 1: 10MB |
| 101003 | not enough market quota |  |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 |
| --- | --- | --- |
| ✔ | 仅认证 | 仅认证 |

---

### 驾驶证识别

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/img-ocr/ocr/api_drivinglicenseocr.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOCKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| img\_url | string | 否 | ENCODE\_URL | 要检测的图片 url，传这个则不用传 img 参数。 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| img | formdata | 是 | form-data 中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img\_url。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| id\_num | string | 证号 |
| name | string | 姓名 |
| sex | string | 性别 |
| address | string | 地址 |
| birth\_date | string | 出生日期 |
| issue\_date | string | 初次领证日期 |
| car\_class | string | 准驾车型 |
| valid\_from | string | 有效期限起始日 |
| valid\_to | string | 有效期限终止日 |
| official\_seal | string | 印章文构 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 101000 | invalid image url |  |
| 101003 | not enough market quota |  |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 |
| --- | --- | --- |
| ✔ | 仅认证 | 仅认证 |

---

### 身份证识别

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/img-ocr/ocr/api_idcardocr.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOCKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| img\_url | string | 否 | ENCODE\_URL | 要检测的图片 url，传这个则不用传 img 参数。 |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| img | formdata | 否 | form-data 中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img\_url。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| type | string | 正面或背面，Front / Back |
| name | string | 正面返回，姓名 |
| id | string | 正面返回，身份证号 |
| valid\_date | string | 背面返回，有效期 |
| addr | string | 正面返回，地址 |
| gender | string | 正面返回，性别 |
| nationality | string | 正面返回，民族 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统错误 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 101000 | invalid image url | 图片URL错误 |
| 101001 | certificate not found | 未检测到证件 |
| 101002 | decode image failed | 图片大小超过限制，resp\_type = 0: 2MB，resp\_type = 1: 10MB |
| 101003 | not enough market quota |  |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 |
| --- | --- | --- |
| ✔ | 仅认证 | 仅认证 |

---

<!-- pages: 9 -->
