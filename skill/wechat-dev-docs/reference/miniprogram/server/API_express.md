# 小程序服务端 API 结构化参考 — API/express

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 绑定/解绑物流账号

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-business/api_bindaccount.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | bind表示绑定，unbind表示解除绑定 |
| biz\_id | string | 是 | 快递公司客户编码 |
| delivery\_id | string | 是 | 快递公司ID |
| password | string | 否 | 快递公司客户密码 |
| remark\_content | string | 否 | 备注内容（提交EMS审核需要） 格式要求： 电话：xxxxx 联系人：xxxxx 服务类型：xxxxx 发货地址：xxxx |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 获取所有绑定的物流账号

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-business/api_getallaccount.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| count | number | 账号数量 |
| list | [objarray](#Res__list<Array>) | 账号列表 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| biz\_id | string | 快递公司客户编码 |
| delivery\_id | string | 快递公司ID |
| create\_time | number | 账号绑定时间 |
| update\_time | number | 账号更新时间 |
| status\_code | number | 绑定状态 |
| alias | string | 账号别名 |
| remark\_wrong\_msg | string | 账号绑定失败的错误信息（EMS审核结果） |
| remark\_content | string | 账号绑定时的备注内容（提交EMS审核需要） |
| quota\_num | number | 电子面单余额 |
| quota\_update\_time | number | 电子面单余额更新时间 |
| service\_type | [objarray](#Res__list<Array>__service_type<Array>) | 该绑定帐号支持的服务类型 |

**Res.list(Array).service_typeObject Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| service\_type | number | service\_type |
| service\_name | string | 服务类型名称 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 获取支持的快递公司列表

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-business/api_getalldelivery.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| count | number | 快递公司数量 |
| data | [objarray](#Res__data<Array>) | 快递公司信息列表 |

**Res.data(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| delivery\_id | string | 快递公司 ID |
| delivery\_name | string | 快递公司名称 |
| can\_use\_cash | number | 是否支持散单, 1表示支持 |
| can\_get\_quota | number | 是否支持查询面单余额, 1表示支持 |
| service\_type | [objarray](#Res__data<Array>__service_type<Array>) | 支持的服务类型 |
| cash\_biz\_id | string | 散单对应的bizid，当can\_use\_cash=1时有效 |

**Res.data(Array).service_typeObject Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| service\_type | number | service\_type |
| service\_name | string | 服务类型名称 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 取消运单

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-business/api_cancelorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 否 | 用户openid，当add\_source=2时无需填写（不发送物流服务通知） |
| delivery\_id | string | 是 | 快递公司ID，参见[getAllDelivery](api_getalldelivery) |
| waybill\_id | string | 是 | 运单ID |
| order\_id | string | 是 | 订单 ID，需保证全局唯一 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| delivery\_resultcode | number | 运力返回的错误码 |
| delivery\_resultmsg | string | 运力返回的错误信息 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 配置面单打印员

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-business/api_updateprinter.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 是 | 打印员 openid |
| update\_type | string | 是 | 更新类型。bind表示绑定；unbind表示解除绑定。 |
| tagid\_list | string | 否 | 用于平台型小程序设置入驻方的打印员面单打印权限，同一打印员最多支持10个tagid，使用半角逗号分隔，中间不加空格，如填写123,456，表示该打印员可以拉取到tagid为123和456的下的单，非平台型小程序无需填写该字段 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 获取电子面单余额

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-business/api_getquota.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delivery\_id | string | 是 | 快递公司ID，参见[getAllDelivery](api_getalldelivery) |
| biz\_id | string | 是 | 快递公司客户编码 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| quota\_num | number | 电子面单余额 |
| errcode | number | 接口报错时返回，错误码 |
| errmsg | string | 接口报错时返回，错误信息 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 获取运单数据

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-business/api_getorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| order\_id | string | 是 | 订单 ID，需保证全局唯一 |
| openid | string | 否 | 该参数仅在getOrder接口生效，batchGetOrder接口不生效。用户openid，当add\_source=2时无需填写（不发送物流服务通知） |
| delivery\_id | string | 是 | 快递公司ID，参见[getAllDelivery](api_getalldelivery), 必须和waybill\_id对应 |
| waybill\_id | string | 否 | 运单ID |
| print\_type | number | 否 | 该参数仅在[getOrder](api_getorder)接口生效，[batchGetOrder](api_batchgetorder)接口不生效。获取打印面单类型【1：一联单，0：二联单】，默认获取二联单 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| print\_html | string | 运单 html 的 BASE64 结果 |
| waybill\_data | [objarray](#Res__waybill_data<Array>) | 运单信息 |
| order\_id | string | 订单ID |
| delivery\_id | string | 快递公司ID |
| waybill\_id | string | 运单号 |
| order\_status | number | 运单状态, 0正常，1取消 |

**Res.waybill_data(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| key | string | 运单信息 key |
| value | string | 运单信息 value |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 模拟更新订单状态

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-business/api_testupdateorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| biz\_id | string | 是 | 商户id,需填test\_biz\_id |
| order\_id | string | 是 | 订单号 |
| delivery\_id | string | 是 | 快递公司id,需填TEST |
| waybill\_id | string | 是 | 运单号 |
| action\_time | number | 是 | 轨迹变化 Unix 时间戳 |
| action\_type | number | 是 | 轨迹变化类型,详情查看下方其他说明 |
| action\_msg | string | 是 | 轨迹变化具体信息说明,使用UTF-8编码 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**action_type 的合法值**

| 值 | 说明 |
| --- | --- |
| 100001 | 揽件阶段-揽件成功 |
| 100002 | 揽件阶段-揽件失败 |
| 100003 | 揽件阶段-分配业务员 |
| 200001 | 运输阶段-更新运输轨迹 |
| 300002 | 派送阶段-开始派送 |
| 300003 | 派送阶段-签收成功 |
| 300004 | 派送阶段-签收失败 |
| 400001 | 异常阶段-订单取消 |
| 400002 | 异常阶段-订单滞留 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

---

### 获取打印员

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-business/api_getprinter.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| count | number | 打印员数量 |
| openid | array | 打印员openid |
| tagid\_list | array | tagid列表 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 查询运单轨迹

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-business/api_getpath.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| openid | string | 否 | 用户openid，当add\_source=2时无需填写（不发送物流服务通知） |
| delivery\_id | string | 是 | 快递公司ID，参见[getAllDelivery](api_getalldelivery) |
| waybill\_id | string | 是 | 运单ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| openid | string | 用户openid |
| delivery\_id | string | 快递公司 ID |
| waybill\_id | string | 运单 ID |
| path\_item\_num | number | 轨迹节点数量 |
| path\_item\_list | [objarray](#Res__path_item_list<Array>) | 轨迹节点列表 |

**Res.path_item_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| action\_time | number | 轨迹节点 Unix 时间戳 |
| action\_type | number | 轨迹节点类型，详情见下文 |
| action\_msg | string | 轨迹节点详情 |

**action_type 轨迹节点类型的合法值**

| 值 | 说明 |
| --- | --- |
| 100001 | 揽件阶段-揽件成功 |
| 100002 | 揽件阶段-揽件失败 |
| 100003 | 揽件阶段-分配业务员 |
| 200001 | 运输阶段-更新运输轨迹 |
| 300002 | 派送阶段-开始派送 |
| 300003 | 派送阶段-签收成功 |
| 300004 | 派送阶段-签收失败 |
| 400001 | 异常阶段-订单取消 |
| 400002 | 异常阶段-订单滞留 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 批量获取运单数据

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-business/api_batchgetorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| order\_list | [objarray](#Body__order_list<Array>) | 是 | 订单列表, 最多不能超过100个 |

**Body.order_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| order\_id | string | 是 | 订单 ID，需保证全局唯一 |
| delivery\_id | string | 是 | 快递公司ID，参见[getAllDelivery](api_getalldelivery), 必须和waybill\_id对应 |
| waybill\_id | string | 否 | 运单ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| order\_list | [objarray](#Res__order_list<Array>) | 运单列表 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**Res.order_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | 错误码 |
| errmsg | string | 错误信息 |
| print\_html | string | 运单 html 的 BASE64 结果 |
| waybill\_data | [objarray](#Res__order_list<Array>__waybill_data<Array>) | 运单信息 |
| order\_id | string | 订单ID |
| delivery\_id | string | 快递公司ID |
| waybill\_id | string | 运单号 |
| order\_status | number | 运单状态, 0正常，1取消 |

**Res.order_list(Array).waybill_dataObject Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| key | string | 运单信息 key |
| value | string | 运单信息 value |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 生成运单

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-business/api_addorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| order\_id | string | 是 | 订单ID，须保证全局唯一，不超过512字节 |
| openid | string | 是 | 用户openid，当add\_source=2时无需填写（不发送物流服务通知） |
| delivery\_id | string | 是 | 快递公司ID，参见[getAllDelivery](api_getalldelivery) |
| biz\_id | string | 是 | 快递客户编码或者现付编码 |
| custom\_remark | string | 否 | 快递备注信息，比如"易碎物品"，不超过1024字节 |
| tagid | number | 否 | 订单标签id，用于平台型小程序区分平台上的入驻方，tagid须与入驻方账号一一对应，非平台型小程序无需填写该字段 |
| add\_source | number | 是 | 订单来源，0为小程序订单，2为App或H5订单，填2则不发送物流服务通知 |
| wx\_appid | string | 否 | App或H5的appid，add\_source=2时必填，需和开通了物流助手的小程序绑定同一open帐号 |
| sender | [object](#Body__sender) | 是 | 发件人信息 |
| receiver | [object](#Body__receiver) | 是 | 收件人信息 |
| cargo | [object](#Body__cargo) | 是 | 包裹信息，将传递给快递公司 |
| shop | [object](#Body__shop) | 是 | 商品信息，会展示到物流服务通知和电子面单中 |
| insured | [object](#Body__insured) | 是 | 保价信息 |
| service | [object](#Body__service) | 是 | 服务类型 |
| expect\_time | number | 否 | Unix 时间戳, 单位秒，顺丰必须传。 预期的上门揽件时间，0表示已事先约定取件时间；否则请传预期揽件时间戳，需大于当前时间，收件员会在预期时间附近上门。例如expect\_time为“1557989929”，表示希望收件员将在2019年05月16日14:58:49-15:58:49内上门取货。说明：若选择 了预期揽件时间，请不要自己打单，由上门揽件的时候打印。如果是下顺丰散单，则必传此字段，否则不会有收件员上门揽件。 |
| take\_mode | number | 否 | 分单策略，【0：线下网点签约，1：总部签约结算】，不传默认线下网点签约。目前支持圆通。 |

**Body.sender Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 否 | 发/收件人姓名，不超过64字节 |
| tel | string | 否 | 发/收件人座机号码，若不填写则必须填写 mobile，不超过32字节 |
| mobile | string | 否 | 发/收件人手机号码，若不填写则必须填写 tel，不超过32字节 |
| company | string | 否 | 发/收件人公司名称，不超过64字节 |
| post\_code | string | 否 | 发/收件人邮编，不超过10字节 |
| country | string | 否 | 发/收件人国家，不超过64字节 |
| province | string | 否 | 发/收件人省份，比如："广东省"，不超过64字节 |
| city | string | 否 | 发/收件人市/地区，比如："广州市"，不超过64字节 |
| area | string | 否 | 发/收件人区/县，比如："海珠区"，不超过64字节 |
| address | string | 否 | 发/收件人详细地址，比如："XX路XX号XX大厦XX"，不超过512字节 |

**Body.receiver Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 否 | 发/收件人姓名，不超过64字节 |
| tel | string | 否 | 发/收件人座机号码，若不填写则必须填写 mobile，不超过32字节 |
| mobile | string | 否 | 发/收件人手机号码，若不填写则必须填写 tel，不超过32字节 |
| company | string | 否 | 发/收件人公司名称，不超过64字节 |
| post\_code | string | 否 | 发/收件人邮编，不超过10字节 |
| country | string | 否 | 发/收件人国家，不超过64字节 |
| province | string | 否 | 发/收件人省份，比如："广东省"，不超过64字节 |
| city | string | 否 | 发/收件人市/地区，比如："广州市"，不超过64字节 |
| area | string | 否 | 发/收件人区/县，比如："海珠区"，不超过64字节 |
| address | string | 否 | 发/收件人详细地址，比如："XX路XX号XX大厦XX"，不超过512字节 |

**Body.cargo Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 包裹数量, 默认为1 |
| weight | number | 是 | 货物总重量，比如1.2，单位是千克(kg) |
| space\_x | number | 是 | 货物长度，比如20.0，单位是厘米(cm) |
| space\_y | number | 是 | 货物宽度，比如15.0，单位是厘米(cm) |
| space\_z | number | 是 | 货物高度，比如10.0，单位是厘米(cm) |
| detail\_list | [objarray](#Body__cargo__detail_list<Array>) | 是 | 货物总重量，单位是千克(kg) |

**Body.shop Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wxa\_path | string | 否 | 商家小程序的路径，建议为订单页面 |
| img\_url | string | 否 | 商品缩略图 url；shop.detail\_list为空则必传，shop.detail\_list非空可不传。 |
| goods\_name | string | 否 | 商品名称, 不超过128字节；shop.detail\_list为空则必传，shop.detail\_list非空可不传。 |
| goods\_count | number | 否 | 商品数量；shop.detail\_list为空则必传。shop.detail\_list非空可不传，默认取shop.detail\_list的size |
| detail\_list | [object](#Body__shop__detail_list) | 否 | 商品详情列表，适配多商品场景，用以消息落地页展示。（新规范，新接入商家建议用此字段） |

**Body.insured Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| use\_insured | number | 否 | 是否保价，0 表示不保价，1 表示保价 |
| insured\_value | number | 否 | 保价金额，单位是分，比如: 10000 表示 100 元 |

**Body.service Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| service\_type | number | 是 | 服务类型ID，详见[已经支持的快递公司基本信息](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/industry/express/business/introduction) |
| service\_name | string | 是 | 服务名称，详见[已经支持的快递公司基本信息](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/industry/express/business/introduction) |

**Body.cargo.detail_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 商品名，不超过128字节 |
| count | number | 是 | 商品数量 |

**Body.shop.detail_list Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| goods\_name | string | 是 | 商品名称 |
| goods\_img\_url | string | 是 | 商品图片url |
| goods\_desc | string | 是 | 商品详情 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | 微信侧错误码，下单失败时返回 |
| errmsg | string | 微信侧错误信息，下单失败时返回 |
| order\_id | string | 订单ID，下单成功时返回 |
| waybill\_id | string | 运单ID，下单成功时返回 |
| delivery\_resultcode | number | 快递侧错误码，下单失败时返回 |
| delivery\_resultmsg | string | 快递侧错误信息，下单失败时返回 |
| waybill\_data | [objarray](#Res__waybill_data<Array>) | 运单信息，下单成功时返回 |

**Res.waybill_data(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| key | string | 运单信息 key |
| value | string | 运单信息 value |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40003 | invalid openid | 不合法的 OpenID ，请开发者确认 OpenID （该用户）是否已关注公众号，或是否是其他公众号的 OpenID |
| 47001 | data format error | 解析 JSON/XML 内容错误;post 数据中参数缺失;检查修正后重试。 |
| 930559 | invaild openid | 沙盒环境openid无效 |
| 930561 | args error | 参数错误 |
| 930564 | quota run out | 沙盒环境调用无配额 |
| 9300501 | Delivery side error | 快递侧逻辑错误，详细原因需要看 delivery\_resultcode。请先确认一下编码方式，python建议 json.dumps(b, ensure\_ascii=False)，php建议 json\_encode($arr, JSON\_UNESCAPED\_UNICODE) |
| 9300502 | Delivery side sys error | 快递公司系统错误 |
| 9300503 | Specified delivery id is not registerred | delivery\_id 不存在 |
| 9300510 | invalid service type | service\_type 不存在 |
| 9300525 | biz id not bind | bizid未绑定 |
| 9300526 | arg size exceed limit | 参数字段长度不正确 |
| 9300531 | invalid biz\_id or password | bizid无效 或者密码错误 |
| 9300534 | invalid shop args | access\_token与openid参数不匹配 |
| 9300535 | invalid shop args | shop字段商品缩略图 url、商品名称为空或者非法，或者商品数量为0 |
| 9300536 | invalid wxa\_appid | add\_source=2时，wx\_appid无效 |

---

### 更新商户审核结果

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-provider/api_updatebusiness.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shop\_app\_id | string | 是 | 商户的小程序AppID，即审核商户事件中的 ShopAppID |
| biz\_id | string | 是 | 商户账户 |
| result\_code | number | 是 | 审核结果，0 表示审核通过，其他表示审核失败 |
| result\_msg | string | 否 | 审核错误原因，仅 result\_code 不等于 0 时需要设置 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 更新运单轨迹

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-provider/api_updatepath.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | string | 是 | 商户侧下单事件中推送的 Token 字段 |
| waybill\_id | string | 是 | 运单 ID |
| action\_time | number | 是 | 轨迹变化 Unix 时间戳 |
| action\_type | number | 是 | 轨迹变化类型，详情见下文 |
| action\_msg | string | 是 | 轨迹变化具体信息说明，展示在快递轨迹详情页中。若有手机号码，则直接写11位手机号码。使用UTF-8编码。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**action_type 轨迹变化类型的合法值**

| 值 | 说明 |
| --- | --- |
| 100001 | 揽件阶段-揽件成功 |
| 100002 | 揽件阶段-揽件失败 |
| 100003 | 揽件阶段-分配业务员 |
| 200001 | 运输阶段-更新运输轨迹 |
| 300002 | 派送阶段-开始派送 |
| 300003 | 派送阶段-签收成功 |
| 300004 | 派送阶段-签收失败 |
| 400001 | 异常阶段-订单取消 |
| 400002 | 异常阶段-订单滞留 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 预览面单模板

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-provider/api_previewtemplate.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| waybill\_id | string | 是 | 运单 ID |
| waybill\_template | string | 是 | 面单 HTML 模板内容（需经 Base64 编码） |
| waybill\_data | string | 是 | 面单数据。详情参考[下单事件返回值中的 WaybillData](../../../event_push/express/provider/Request_an_order_event) |
| custom | [object](#Body__custom) | 是 | 商户下单数据，格式是商户侧下单[addOrder](../express-by-business/api_addorder) 接口中的请求体 |

**Body.custom Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| order\_id | string | 是 | 订单ID，须保证全局唯一，不超过512字节 |
| openid | string | 是 | 用户openid，当add\_source=2时无需填写（不发送物流服务通知） |
| delivery\_id | string | 是 | 快递公司ID，参见[getAllDelivery](../express-by-business/api_getalldelivery) |
| biz\_id | string | 是 | 快递客户编码或者现付编码 |
| custom\_remark | string | 否 | 快递备注信息，比如"易碎物品"，不超过1024字节 |
| tagid | number | 否 | 订单标签id，用于平台型小程序区分平台上的入驻方，tagid须与入驻方账号一一对应，非平台型小程序无需填写该字段 |
| add\_source | number | 是 | 订单来源，0为小程序订单，2为App或H5订单，填2则不发送物流服务通知 |
| wx\_appid | string | 否 | App或H5的appid，add\_source=2时必填，需和开通了物流助手的小程序绑定同一open帐号 |
| sender | [object](#Body__custom__sender) | 是 | 发件人信息 |
| receiver | [object](#Body__custom__receiver) | 是 | 收件人信息 |
| cargo | [object](#Body__custom__cargo) | 是 | 包裹信息，将传递给快递公司 |
| shop | [object](#Body__custom__shop) | 是 | 商品信息，会展示到物流服务通知和电子面单中 |
| insured | [object](#Body__custom__insured) | 是 | 保价信息 |
| service | [object](#Body__custom__service) | 是 | 服务类型 |
| expect\_time | number | 否 | Unix 时间戳, 单位秒，顺丰必须传。 预期的上门揽件时间，0表示已事先约定取件时间；否则请传预期揽件时间戳，需大于当前时间，收件员会在预期时间附近上门。例如expect\_time为“1557989929”，表示希望收件员将在2019年05月16日14:58:49-15:58:49内上门取货。说明：若选择 了预期揽件时间，请不要自己打单，由上门揽件的时候打印。如果是下顺丰散单，则必传此字段，否则不会有收件员上门揽件。 |
| take\_mode | number | 否 | 分单策略，【0：线下网点签约，1：总部签约结算】，不传默认线下网点签约。目前支持圆通。 |

**Body.custom.sender Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 否 | 发/收件人姓名，不超过64字节 |
| tel | string | 否 | 发/收件人座机号码，若不填写则必须填写 mobile，不超过32字节 |
| mobile | string | 否 | 发/收件人手机号码，若不填写则必须填写 tel，不超过32字节 |
| company | string | 否 | 发/收件人公司名称，不超过64字节 |
| post\_code | string | 否 | 发/收件人邮编，不超过10字节 |
| country | string | 否 | 发/收件人国家，不超过64字节 |
| province | string | 否 | 发/收件人省份，比如："广东省"，不超过64字节 |
| city | string | 否 | 发/收件人市/地区，比如："广州市"，不超过64字节 |
| area | string | 否 | 发/收件人区/县，比如："海珠区"，不超过64字节 |
| address | string | 否 | 发/收件人详细地址，比如："XX路XX号XX大厦XX"，不超过512字节 |

**Body.custom.receiver Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 否 | 发/收件人姓名，不超过64字节 |
| tel | string | 否 | 发/收件人座机号码，若不填写则必须填写 mobile，不超过32字节 |
| mobile | string | 否 | 发/收件人手机号码，若不填写则必须填写 tel，不超过32字节 |
| company | string | 否 | 发/收件人公司名称，不超过64字节 |
| post\_code | string | 否 | 发/收件人邮编，不超过10字节 |
| country | string | 否 | 发/收件人国家，不超过64字节 |
| province | string | 否 | 发/收件人省份，比如："广东省"，不超过64字节 |
| city | string | 否 | 发/收件人市/地区，比如："广州市"，不超过64字节 |
| area | string | 否 | 发/收件人区/县，比如："海珠区"，不超过64字节 |
| address | string | 否 | 发/收件人详细地址，比如："XX路XX号XX大厦XX"，不超过512字节 |

**Body.custom.cargo Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 包裹数量, 默认为1 |
| weight | number | 是 | 货物总重量，比如1.2，单位是千克(kg) |
| space\_x | number | 是 | 货物长度，比如20.0，单位是厘米(cm) |
| space\_y | number | 是 | 货物宽度，比如15.0，单位是厘米(cm) |
| space\_z | number | 是 | 货物高度，比如10.0，单位是厘米(cm) |
| detail\_list | [objarray](#Body__custom__cargo__detail_list<Array>) | 是 | 货物总重量，单位是千克(kg) |

**Body.custom.cargo.detail_list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 商品名，不超过128字节 |
| count | number | 是 | 商品数量 |

**Body.custom.shop Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wxa\_path | string | 否 | 商家小程序的路径，建议为订单页面 |
| img\_url | string | 否 | 商品缩略图 url；shop.detail\_list为空则必传，shop.detail\_list非空可不传。 |
| goods\_name | string | 否 | 商品名称, 不超过128字节；shop.detail\_list为空则必传，shop.detail\_list非空可不传。 |
| goods\_count | number | 否 | 商品数量；shop.detail\_list为空则必传。shop.detail\_list非空可不传，默认取shop.detail\_list的size |
| wxa\_appid | string | 否 | 该参数在【即时配送】的[addLocalOrder](../../immediate-delivery/deliver-by-business/api_addlocalorder)接口才生效。若结算方式为：第三方向配送公司统一结算，商户后续和第三方结算，则该参数必填；在该结算模式下，第三方用自己的开发小程序替授权商户发起下单，并将授权小程序的appid给平台，后续配送通知中可回流授权商户小程序。 |

**Body.custom.insured Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| use\_insured | number | 否 | 是否保价，0 表示不保价，1 表示保价 |
| insured\_value | number | 否 | 保价金额，单位是分，比如: 10000 表示 100 元 |

**Body.custom.service Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| service\_type | number | 是 | 服务类型ID，详见[已经支持的快递公司基本信息](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/industry/express/business/introduction) |
| service\_name | string | 是 | 服务名称，详见[已经支持的快递公司基本信息](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/industry/express/business/introduction) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| waybill\_id | string | 运单 ID |
| rendered\_waybill\_template | string | 渲染后的面单 HTML 文件（已经过 Base64 编码） |

**4. 注意事项**

| key | value |
| --- | --- |
| sys.waybillid | 运单 ID |
| sys.wxaappid | 商户小程序 APPID |
| waybilldata.\* | [下单事件](../../../event_push/express/provider/Request_an_order_event)返回中的WaybillData，快递侧自定义的数据 |
| custom.\* | 是[商户侧下单](../express-by-business/api_addorder) API 中传入的字段 |
| custom.order\_id | 唯一标识订单的 ID，由商户传入 |
| custom.custom\_remark | 快递备注，会打印到面单的自定义区，比如"易碎物品" |
| custom.sender.name | 发件人名字 |
| custom.sender.tel | 发件人座机号码 |
| custom.sender.mobile | 发件人手机号码 |
| custom.sender.company | 发件人公司名 |
| custom.sender.post\_code | 发件人邮编 |
| custom.sender.country | 发件人所在国家 |
| custom.sender.province | 发件人省份 |
| custom.sender.city | 发件人地区/市 |
| custom.sender.area | 发件人区/县 |
| custom.sender.address | 发件人详细地址 |
| custom.receiver.name | 收件人名字 |
| custom.receiver.tel | 收件人座机号码 |
| custom.receiver.mobile | 收件人手机号码 |
| custom.receiver.company | 收件人公司名 |
| custom.receiver.post\_code | 收件人邮编 |
| custom.receiver.country | 收件人所在国家 |
| custom.receiver.province | 收件人省份 |
| custom.receiver.city | 收件人地区/市 |
| custom.receiver.area | 收件人区/县 |
| custom.receiver.address | 收件人详细地址 |
| custom.cargo.count | 包裹数量 |
| custom.cargo.weight | 包裹总重量，单位是千克(kg) |
| custom.cargo.space\_x | 包裹长度，单位是厘米(cm) |
| custom.cargo.space\_y | 包裹宽度，单位是厘米(cm) |
| custom.cargo.space\_z | 包裹高度，单位是厘米(cm) |
| custom.shop.goods\_name | 商品名称 |
| custom.shop.goods\_count | 商品数量 |
| custom.insured.use\_insured | 是否使用保价 |
| custom.insured.insured\_value | 报价金额，单位是分 |
| custom.service.service\_type | 服务类型 ID |
| custom.service.service\_name | 服务名称 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40199 | waybill\_id not found | 运单 ID 不存在，未查到运单 |
| 9300502 | Delivery side sys error | 快递公司系统错误 |
| 9300507 | invalid token  can't decryption ordecryption result is different from the plaintext | Token 不正确 |
| 9300512 | invalid waybill template format | 模板格式错误，渲染失败 |

---

### 获取面单联系人信息

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-provider/api_getcontact.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | string | 是 | 商户侧[下单事件](../../../event_push/express/provider/Request_an_order_event)中推送的 Token 字段 |
| waybill\_id | string | 是 | 运单 ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| waybill\_id | string | 运单 ID |
| sender | [object](#Res__sender) | 发件人信息 |
| receiver | [object](#Res__receiver) | 收件人信息 |

**Res.sender Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| name | string | 用户姓名 |
| tel | string | 座机号码 |
| mobile | string | 手机号码 |
| address | string | 地址，已经将省市区信息合并 |

**Res.receiver Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| name | string | 用户姓名 |
| tel | string | 座机号码 |
| mobile | string | 手机号码 |
| address | string | 地址，已经将省市区信息合并 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

---

### 运力取消订单

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-provider/api_scatterdeliverycancel.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | string | 是 | 商户侧下单事件中推送的 Token 字段 |
| reason | string | 是 | 取消的原因 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

---

### 运力更新需支付的运费

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-provider/api_scatterupdateorderfee.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | string | 是 | 商户侧下单事件中推送的 Token 字段 |
| waybill\_id | string | 是 | 运单 ID |
| need\_pay | number | 是 | 是否需要用户在线支付， 0不需要，1需要，2需要(支付分) |
| fee | number | 是 | 需要支付的金额（一般等于original\_fee，如有优惠则填最终需要支付的金额），单位分 |
| original\_fee | number | 是 | 原价（base\_fee+insured\_fee+other\_fee），单位分 |
| base\_fee | number | 是 | 运费，单位分 |
| insured\_fee | number | 否 | 保价费，单位分 |
| other\_fee | number | 否 | 其他费用，单位分 |
| remark | number | 否 | 其他费用备注 |
| pay\_goods\_name | string | 否 | 商品名称（对应微信支付商品详情页上的商品名称） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

---

### 运力公司退款

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-provider/api_scatterdeliveryrefund.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | string | 是 | 下单时的Token字段 |
| fee | number | 是 | 退款金额，单位分 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

---

### 对账单下载

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-provider/api_scatter_get_bill.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| date | string | 是 | 下载对账单的时间，格式为YYYYMMDD |
| type | string | 是 | 下载对账单的类型 ALL-所以账单 SUCCESS-成功支付账单 REFUND-退款账单 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

---

### 运力返回用户投诉处理结果

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-provider/api_scatterupdatecomplainresult.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证 |
| token | string | 是 | 商户侧下单事件中推送的 Token 字段 |
| waybill\_id | string | 是 | 运单 ID |
| result | string | 是 | 处理结果 |
| desc | string | 是 | 处理结果说明 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

---

### 运力更新订单状态

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-provider/api_scatterupdateorderstatus.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| token | string | 是 | 商户侧下单事件中推送的Token字段 | - |
| waybill\_id | string | 否 | 运单ID | - |
| action\_time | number | 是 | 轨迹变化Unix时间戳 | - |
| action\_type | number | 是 | 轨迹变化类型，与普通单保持一致，参见附录action\_type定义 | [枚举值](#Enum_Body__action_type) |
| action\_msg | string | 是 | 轨迹变化具体信息说明，展示在快递轨迹详情页中。若有手机号码，则直接写11位手机号码。使用UTF-8编码。 | - |
| pickup\_courier\_name | string | 是 | 取件员姓名 | - |
| pickup\_courier\_phone | string | 是 | 取件员电话 | - |
| delivery\_courier\_name | string | 是 | 派件员姓名 | - |
| delivery\_courier\_phone | string | 是 | 派件员电话 | - |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**Body.action_type Enum**

| 枚举值 | 描述 |
| --- | --- |
| 90001 | 揽件前阶段-网点接单 |
| 90002 | 揽件前阶段-分配业务员 |
| 90003 | 揽件前阶段-重新分配业务员 |
| 90010 | 揽件前阶段-待支付 |
| 90011 | 揽件前阶段-已支付 |
| 100001 | 揽件阶段-揽件成功 |
| 100002 | 揽件阶段-揽件失败 |
| 200001 | 运输阶段-更新运输轨迹 |
| 300002 | 派送阶段-派送中 |
| 300003 | 派送阶段-签收成功 |
| 300004 | 派送阶段-签收失败 |
| 300005 | 派送阶段-第三方代收入库 |
| 300006 | 派送阶段-第三方代收快递员取出 |
| 300007 | 派送阶段-代签收 |
| 400001 | 异常阶段-订单取消 |
| 400002 | 异常阶段-订单滞留 |
| 400003 | 异常阶段-订单退回 |
| 400004 | 异常阶段-订单拒收 |
| 400005 | 异常阶段-问题件 |
| 500001 | 兜底状态-其他未分类状态纳入本action\_type |

---

<!-- pages: 22 -->
