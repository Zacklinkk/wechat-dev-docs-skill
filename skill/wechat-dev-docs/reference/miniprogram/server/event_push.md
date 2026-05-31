# 小程序服务端 API 结构化参考 — event_push

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 授权用户信息变更

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/platform/authorized_user_information_changes.html

**请求体 Request Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| ToUserName | string | 小程序的UserName | - |
| FromUserName | string | 平台推送服务UserName | - |
| MsgType | string | 默认为：Event | - |
| Event | string | 事件名称 | [枚举值](#Enum_Body__Event) |
| CreateTime | number | 发送时间 | - |
| OpenID | string | 授权用户OpenID | - |
| AppID | string | 小程序的AppID | - |
| RevokeInfo | string | 用户撤回的授权信息 | [枚举值](#Enum_Body__RevokeInfo) |
| PluginID | string | 插件场景用户撤回，插件的AppID | - |
| OpenPID | string | 插件场景用户撤回，撤回用户的OpenPID | - |

**Body.Event Enum**

| 枚举值 | 描述 |
| --- | --- |
| user\_info\_modified | 用户资料变更 |
| user\_authorization\_revoke | 用户撤回 |
| user\_authorization\_cancellation | 用户完成注销 |

**Body.RevokeInfo Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 车牌号 |
| 2 | 地址 |
| 3 | 发票信息 |
| 4 | 蓝牙 |
| 5 | 麦克风 |
| 6 | 昵称和头像 |
| 7 | 摄像头 |
| 8 | 手机号 |
| 12 | 微信运动步数 |
| 13 | 位置信息 |
| 14 | 选中的图片或视频 |
| 15 | 选中的文件 |
| 16 | 邮箱地址 |
| 18 | 选择的位置信息 |
| 19 | 昵称输入键盘中选择的微信昵称 |
| 20 | 获取用户头像组件中选择的微信头像 |

---

### 小程序违规处罚信息通知

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/platform/Penalty_for_Violation.html

**请求体 Request Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| Event | string | 事件名称 | [枚举值](#Enum_Body__Event) |
| event\_type | number | 事件类型 | - |
| punish\_id | string | 违规处罚ID，用于唯一标识每次违规 | - |
| appid | string | 被处罚小程序的AppID | - |
| punish\_time | number | 违规时间（UNIX时间戳） | - |
| illegal\_reason | string | 违规原因 | - |
| illegal\_content | string | 违规内容 | - |
| rule\_name | string | 违反规则名称 | - |
| rule\_url | string | 违反规则链接 | - |
| adjust\_guide\_url | string | 违规申诉及整改指引链接 | - |
| detail | string | 违规处罚详情，字段内容为JSON字符串，JSON具体结构取决于event\_type，请参照下方说明对该字段中包含的JSON字符串进行正确的解析 | - |

**Body.Event Enum**

| 枚举值 | 描述 |
| --- | --- |
| wxa\_punish\_event | 小程序违规处罚事件 |

**4. 注意事项**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| warned\_type | number | 警告类型。1 |
| rectify\_deadline | number | 警告的截止时间(UNIX时间戳) |
| warned\_function\_names | array<string> | 警告要封禁的功能项列表，如需获取列表中每个功能项的封禁时长，可直接在warned\_ban\_days的对应索引处获得，warned\_function\_names和warned\_ban\_days总是一一对应。（该字段仅当warned\_type=2时生效） |
| warned\_ban\_days | array<number> | 警告封禁的天数列表。当warned\_type=1时则该列表仅有一项，代表警告要封禁小程序账号的天数。当warned\_type=2时列表中的每一项分别代表warned\_function\_names中对应索引处的功能项被警告要封禁的天数。当warned\_type=3时则该列表仅有一项，代表警告要下架小程序的天数。注 |

**4. 注意事项**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| banned\_days | array<number> | 功能项被封禁的天数列表，列表中的每一项分别代表banned\_function\_names中对应索引处的功能项被封禁的天数。注 |
| banned\_function\_names | array<string> | 被封禁的功能项列表，如需获取列表中每个功能项的封禁时长，可直接在banned\_days的对应索引处获得，banned\_days和banned\_function\_names总是一一对应。 |

**4. 注意事项**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| suspended\_days | number | 下架天数。注 |

**4. 注意事项**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| banned\_days | number | 账号封禁天数。注 |

**4. 注意事项**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| path | string | 封禁的页面路径 |

---

### logistics.onCancelOrder

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/Cancel_order_event.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 快递公司小程序 UserName |
| FromUserName | string | 下单用户的 OpenID |
| CreateTime | number | 事件时间，Unix 时间戳 |
| MsgType | string | 消息类型，固定为 event |
| Event | string | 事件类型，固定为 cancel\_waybill |
| OrderID | string | 唯一标识订单的 ID，由商户生成 |
| BizID | string | 商户 ID |
| BizPwd | string | 商户密码 |
| ShopAppID | string | 商户的小程序 AppID |
| WayBillID | string | 运单 ID，从微信号段中生成 |

**消息返回**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| ToUserName | string |  | 是 | 原样返回请求中的 FromUserName |
| FromUserName | string |  | 是 | 快递公司小程序 UserName |
| CreateTime | number |  | 是 | 事件时间，Unix 时间戳 |
| MsgType | string |  | 是 | 消息类型，固定为 event |
| Event | string |  | 是 | 事件类型，固定为 cancel\_waybill，不区分大小写 |
| BizID | string |  | 是 | 商户ID，请原样返回 |
| OrderID | string |  | 是 | 唯一标识订单的ID，由商户生成。请原样返回 |
| WayBillID | string |  | 是 | 运单ID，请原样返回 |
| ResultCode | number |  | 是 | 处理结果错误码 |
| ResultMsg | string |  | 是 | 处理结果详情 |

**消息返回**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 0 | 取消成功 |  |
| -1 | 其他错误 |  |
| 30001 | 参数错误（BizID、OrderID、WayBillID不存在） |  |
| 30002 | 已经揽收，不可取消 |  |
| 30003 | 无效单（如已经取消过、或签收超过一定时间），不可取消 |  |
| 30004 | 快递不支持取消运单 |  |

---

### logistics.onCheckBusiness

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/Review_merchant_events.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 快递公司小程序 UserName |
| FromUserName | string | 微信团队的 OpenID （固定值） |
| CreateTime | number | 事件时间，Unix 时间戳 |
| MsgType | string | 消息类型，固定为 event |
| Event | string | 事件类型，固定为 check\_biz，不区分大小写 |
| BizID | string | 商户ID，即商户在快递注册的客户编码或月结账户名 |
| BizPwd | string | BizID 对应的密码 |
| ShopAppID | string | 商户的小程序 AppID |
| ShopName | string | 商户名称，即小程序昵称（仅EMS可用） |
| ShopTelphone | string | 商户联系电话（仅EMS可用） |
| ShopContact | string | 商户联系人姓名（仅EMS可用） |
| ServiceName | string | 预开通的服务类型名称（仅EMS可用） |
| SenderAddress | string | 商户发货地址（仅EMS可用） |
| SenderProvince | string | 商户发货省份（仅EMS可用） |
| SenderCity | string | 商户发货城市（仅EMS可用） |
| SenderArea | string | 商户发货区域（仅EMS可用） |

**消息返回**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| ToUserName | string |  | 是 | 原样返回请求中的 FromUserName |
| FromUserName | string |  | 是 | 快递公司小程序 UserName |
| CreateTime | number |  | 是 | 事件时间，Unix时间戳 |
| MsgType | string |  | 是 | 消息类型，固定为event |
| Event | string |  | 是 | 事件类型，固定为check\_biz，不区分大小写 |
| BizID | string |  | 是 | 商户ID |
| ResultCode | number |  | 是 | 处理结果错误码 |
| ResultMsg | string |  | 是 | 处理结果详情 |
| Quota | number |  | 是 | 商户可用余额，0 表示无可用余额 |

**消息返回**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 0 | 审核通过 |  |
| -1 | 其他错误 |  |
| 10001 | 客户编码或者月结账户不存在 |  |
| 10002 | 客户密码不正确 |  |

---

### logistics.onAddOrder

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/Request_an_order_event.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 快递公司小程序 UserName |
| FromUserName | string | 微信团队的 OpenID （固定值） |
| CreateTime | number | 事件时间，Unix时间戳 |
| MsgType | string | 消息类型，固定为 event |
| Event | string | 事件类型，固定为 add\_waybill，不区分大小写 |
| Token | string | 订单 Token。请保存该 Token，调用[更新运单轨迹](../../../API/express/express-by-provider/api_updatepath)时需要传入 |
| OrderID | string | 唯一标识订单的 ID，由商户生成。快递需要保证相同的 OrderID 生成相同的运单ID。 |
| BizID | string | 商户 ID，即商户在快递注册的客户编码或月结账户名 |
| BizPwd | string | BizID 对应的密码 |
| ShopAppID | string | 商户的小程序 AppID |
| WayBillID | string | 运单 ID，从微信号段中生成。若为 0，则表示需要快递来生成运单 ID。 |
| Remark | string | 快递备注，会打印到面单上，比如"易碎物品" |
| Sender | Array.<Object> | 发件人信息 |
| Receiver | Array.<Object> | 收件人信息 |
| Cargo | Array.<Object> | 包裹信息 |
| Insured | Array.<Object> | 保价信息 |
| Service | Array.<Object> | 服务类型 |

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| Name | string | 发件人姓名 |
| Tel | string | 发件人座机号码 |
| Mobile | string | 发件人手机号码 |
| Company | string | 发件人公司名 |
| PostCode | string | 发件人邮编 |
| Country | string | 发件人所在国家，默认为"中国" |
| Province | string | 发件人省份，比如"广东省" |
| City | string | 发件人地区/市，比如"广州市" |
| Area | string | 发件人区/县，比如"海珠区" |
| Address | string | 发件人详细地址，比如"XX路XX号XX大厦XX" |

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| Name | string | 收件人姓名 |
| Tel | string | 收件人座机号码 |
| Mobile | string | 收件人手机号码 |
| Company | string | 收件人公司名 |
| PostCode | string | 收件人邮编 |
| Country | string | 收件人所在国家，默认为"中国" |
| Province | string | 收件人省份，比如"广东省" |
| City | string | 收件人地区/市，比如"广州市" |
| Area | string | 收件人区/县，比如"海珠区" |
| Address | string | 收件人详细地址，比如"XX路XX号XX大厦XX" |

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| Weight | number | 货物总重量，比如1.2，单位是千克(kg) |
| Space\_X | number | 货物长度，比如20.5，单位是厘米(cm) |
| Space\_Y | number | 货物宽度，比如15.0，单位是厘米(cm) |
| Space\_Z | number | 货物高度，比如10.0，单位是厘米(cm) |
| Count | number | 货物数量，一般为1 |

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| UseInsured | number | 是否保价，0 表示不保价，1 表示保价 |
| InsuredValue | number | 保价金额，单位是分，比如: 10000 表示 100 元 |

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| ServiceType | number | 服务类型ID，详见[已经支持的快递公司基本信息](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/industry/express/business/expressinfo.html) |
| ServiceName | string | 服务名称，详见[已经支持的快递公司基本信息](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/industry/express/business/expressinfo.html) |

**消息返回**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| ToUserName | string |  | 是 | 原样返回请求中的 FromUserName |
| FromUserName | string |  | 是 | 快递公司小程序 UserName |
| CreateTime | number |  | 是 | 事件时间，Unix 时间戳 |
| MsgType | string |  | 是 | 消息类型，固定为 event |
| Event | string |  | 是 | 事件类型，固定为 add\_waybill |
| Token | string |  | 是 | 传入的 Token，原样返回 |
| OrderID | string |  | 是 | 传入的唯一标识订单的 ID，由商户生成，原样返回 |
| BizID | string |  | 是 | 商户 ID，原样返回 |
| WayBillID | string |  | 是 | 运单 ID |
| ResultCode | number |  | 是 | 处理结果错误码 |
| ResultMsg | string |  | 是 | 处理结果的详细信息 |
| WaybillData | string |  | 是 | 集包地、三段码、大头笔等信息，用于生成面单信息。详见后文返回值说明 |

**消息返回**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 0 | 下单成功 |  |
| -1 | 其他错误 |  |
| 10001 | 客户编码或者月结账户不存在 |  |
| 10002 | 客户密码不正确 |  |
| 20001 | 运单 ID 不正确（仅适用于微信生成运单 ID 的情况） |  |
| 20002 | 发件人信息不完整（包括姓名、电话、地址等不完整） |  |
| 20003 | 发件人地址不可达或者发货地址不在服务范围 |  |
| 20004 | 收件人信息不完整（包括姓名、电话、地址等不完整） |  |
| 20005 | 收件人地址不可达或者收货地址不在服务范围 |  |
| 20006 | 货物数量、重量、尺寸不正确或者不合理 |  |
| 20007 | 商户余额不足，需要充值后再进行下单 |  |
| 20008 | 保价信息不正确（金额不合理或者快递不支持） |  |
| 20009 | 服务信息不正确 |  |

---

### 查询商户余额

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/Query_merchant_balance_events.html

**请求体 Request Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 快递公司小程序 UserName |
| FromUserName | string | 微信团队的 OpenID （固定值） |
| CreateTime | number | 事件时间，Unix时间戳 |
| MsgType | string | 消息类型，固定为 event |
| Event | string | 事件类型，固定为 get\_quota，不区分大小写 |
| BizID | string | 商户ID，即商户在快递注册的客户编码或月结账户名 |
| BizPwd | string | BizID 对应的密码 |
| ShopAppID | string | 商户小程序的 AppID |

**返回体 Response Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| ToUserName | string | 是 | 原样返回请求中的 FromUserName | - |
| FromUserName | string | 是 | 快递公司小程序 UserName | - |
| CreateTime | number | 是 | 事件时间，Unix时间戳 | - |
| MsgType | string | 是 | 消息类型，固定为event | - |
| Event | string | 是 | 事件类型，固定为get\_quota，不区分大小写 | - |
| BizID | string | 是 | 商户ID | - |
| ResultCode | number | 是 | 处理结果错误码 | [枚举值](#Enum_Res__ResultCode) |
| ResultMsg | string | 是 | 处理结果详情 | - |
| Quota | number | 是 | 商户可用余额，0 表示无可用余额 | - |

**Res.ResultCode Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 查询成功 |
| -1 | 其他错误 |
| 10001 | 客户编码或者月结账户不存在 |
| 10002 | 客户密码不正确 |

---

### 查询订单状态

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/check_order_status.html

**请求体 Request Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 快递公司小程序UserName |
| FromUserName | string | 微信团队的OpenID（固定值） |
| CreateTime | number | 事件时间，Unix时间戳如1599823049 |
| MsgType | string | 消息类型，固定为event |
| Event | string | 事件类型，固定为waybill\_notify\_query，不区分大小写 |
| WaybillId | string | 运单号 |
| SenderPhone | string | 寄件人手机号 |
| ReceiverPhone | string | 收件人手机号 |

**返回体 Response Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ToUserName | string | 是 | 原样返回请求中的FromUserName |
| FromUserName | string | 是 | 快递公司小程序UserName |
| CreateTime | number | 是 | 事件时间，Unix时间戳 |
| MsgType | string | 是 | 消息类型，固定为event |
| Event | string | 是 | 事件类型，固定为waybill\_notify\_query，不区分大小写 |
| ResultCode | number | 是 | 处理结果错误码，成功时返回0，异常时由运力自定义 |
| ResultMsg | string | 是 | 处理结果的详细信息，错误提示 |
| Path | [objarray](#Res__Path<Array>) | 是 | 所有物流轨迹 |
| WaybillCreateTime | number | 是 | 运单创建时间，秒级时间戳如1599823049 |

**Res.Path(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ActionTime | number | 是 | 轨迹变化Unix时间戳，如1599823049 |
| ActionType | number | 是 | 轨迹变化类型，与普通单保持一致，参见action\_type定义 |
| ActionMsg | string | 是 | 轨迹变化具体信息说明，展示在快递轨迹详情页中。若有手机号码，则直接写11位手机号码。使用UTF-8编码。 |
| PickupCourierName | string | 否 | 取件员姓名,当分配取件员成功时返回 |
| PickupCourierPhone | string | 否 | 取件员电话,当分配取件员成功时返回 |
| DeliveryCourierName | string | 否 | 派件员姓名,当分配派件员成功时返回 |
| DeliveryCourierPhone | string | 否 | 派件员电话,当分配派件员成功时返回 |

---

### 运力下单

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/shipping_capacity_order.html

**请求体 Request Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| ToUserName | string | 快递公司小程序UserName | - |
| FromUserName | string | 微信团队的OpenID（固定值） | - |
| CreateTime | number | 事件时间，Unix时间戳 | - |
| MsgType | string | 消息类型，固定为event | - |
| Event | string | 事件类型，固定为add\_single\_waybill，不区分大小写 | - |
| Token | string | 订单Token。请保存该Token，更新运单轨迹时需要传入，长度需预留256个字符 | - |
| WXAppId | string | 商户微信小程序的appid | - |
| OrderID | string | 商户订单ID，可以使用token而不用这个字段 | - |
| Sender | [object](#Body__Sender) | 发件人信息 | - |
| Receiver | [object](#Body__Receiver) | 收件人信息 | - |
| GoodDetail | [object](#Body__GoodDetail) | 物品详情 | - |
| Insured | [object](#Body__Insured) | 保价信息 | - |
| ExpectStartTime | number | 期望上门取件起始时间 | - |
| ExpectEndTime | number | 期望上门取件结束时间 | - |
| Settingment | number | 结算方式默认0现结，1到付,2月结,3支付分 | - |
| CompanyID | string | 中通大客户CompanyID，结算方式为2，且选中通时需填 | - |
| Account | string | 月结账号，结算方式为2时需填 | - |
| AccountPwd | string | 月结账号密码结算方式为2时需填 | - |
| Remark | string | 备注信息 | - |
| PickUpStartTime | number | 上门时间段（开始时间） | - |
| PickUpEndTime | number | 上门时间段（结束时间） | - |
| Scene | number | 场景值 | [枚举值](#Enum_Body__Scene) |

**Body.Sender Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Name | string | 收件人姓名 |
| Tel | string | 收件人座机号码 |
| Mobile | string | 收件人手机号码 |
| Province | string | 省份，比如"广东省" |
| City | string | 地区/市，比如"广州市" |
| Area | string | 区/县，比如"海珠区" |
| Street | string | 街道，比如新港中路 |
| Address | string | 详细地址，比如"XX路XX号XX大厦XX" |
| Id | string | 地址id |

**Body.Receiver Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Name | string | 收件人姓名 |
| Tel | string | 收件人座机号码 |
| Mobile | string | 收件人手机号码 |
| Province | string | 省份，比如"广东省" |
| City | string | 地区/市，比如"广州市" |
| Area | string | 区/县，比如"海珠区" |
| Street | string | 街道，比如新港中路 |
| Address | string | 详细地址，比如"XX路XX号XX大厦XX" |
| Id | string | 地址id |

**Body.GoodDetail Object Payload**

| 参数名 | 类型 | 示例 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| Weight | number | 1 | 货物总重量，比如1.2，单位是千克(kg) | - |
| Special | number | 0 | 物品类型，见物品类型说明 | [枚举值](#Enum_Body__GoodDetail__Special) |

**Body.Insured Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| UseInsured | number | 是否保价，0表示不保价，1表示保价 |
| InsuredValue | number | 保价金额，单位是分，比如:10000表示100元 |

**返回体 Response Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ToUserName | string | 是 | 原样返回请求中的FromUserName |
| FromUserName | string | 是 | 快递公司小程序UserName |
| CreateTime | number | 是 | 事件时间，Unix时间戳 |
| MsgType | string | 是 | 消息类型，固定为event |
| Event | string | 是 | 事件类型，固定为add\_single\_waybill，不区分大小写 |
| ResultCode | number | 是 | 处理结果错误码 |
| ResultMsg | string | 否 | 处理结果的详细信息 |
| WayBillID | string | 否 | 运单ID，如果不能立即返回，可以在打印面单时候回调通知微信端 |
| EstimatedDeliveryTime | string | 否 | 预计送达时间，格式：yyyy-mm-dd |
| JumpPath | string | 否 | 下单成功后跳转的地址（appid需要联系微信进行登记配置） |
| PickCode | string | 否 | 取件码 |

**Body.Scene Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | C端散单 |
| 2 | B端退货 |
| 3 | B端发货 |

**Body.GoodDetail.Special Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 文件类 |
| 1 | 电子产品类(包括家用电器) |
| 2 | 办公用品类,服装鞋帽，箱包类 |
| 3 | 化妆品，美容产品类 |
| 4 | 珠宝，手表，眼镜，贵重饰品类 |
| 5 | 食品，保健药品类 |
| 6 | 工艺品类(包括瓷器，茶具，烹饪用品) |
| 7 | 玩具乐器类 |
| 8 | 其他类 |

---

### 取消订单

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/cancel_order.html

**请求体 Request Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| ToUserName | string | 快递公司小程序 UserName | - |
| FromUserName | string | 微信团队的 OpenID （固定值） | - |
| CreateTime | number | 事件时间，Unix时间戳 | - |
| MsgType | string | 消息类型，固定为 event | - |
| Event | string | 事件类型，固定为 cancel\_single\_waybill，不区分大小写 | - |
| Token | string | 下单接口传的Token | - |
| WXAppId | string | 商户在微信端的appid | - |
| OrderID | string | 商户订单 ID，可以使用token而不用这个字段 | - |
| WayBillID | string | 运单 ID，不一定有 | - |
| CancelID | number | 取消原因Id | [枚举值](#Enum_Body__CancelID) |
| CancelReason | string | 取消原因说明 | - |

**返回体 Response Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ToUserName | string | 是 | 原样返回请求中的 FromUserName |
| FromUserName | string | 是 | 快递公司小程序 UserName |
| CreateTime | number | 是 | 事件时间，Unix 时间戳 |
| MsgType | string | 是 | 消息类型，固定为 event |
| Event | string | 是 | 事件类型，固定为 cancel\_single\_waybill，不区分大小写 |
| ResultCode | number | 是 | 处理结果错误码 |
| ResultMsg | string | 否 | 处理结果的详细信息 |

**Body.CancelID Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 不想寄了 |
| 2 | 下错单 |
| 3 | 重复下单 |
| 4 | 运费太贵 |
| 5 | 无人联系 |
| 6 | 取件太慢 |
| 7 | 态度差 |
| 8 | 其他原因 |

---

### 通过收发件地址查询标准运费

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/check_standard_shipping.html

**请求体 Request Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 快递公司小程序 UserName |
| FromUserName | string | 微信团队的 OpenID （固定值） |
| CreateTime | number | 事件时间，Unix时间戳 |
| MsgType | string | 消息类型，固定为 event |
| Event | string | 事件类型，固定为 query\_single\_waybill\_fee，不区分大小写 |
| Sender | [object](#Body__Sender) | 发件人信息 |
| Receiver | [object](#Body__Receiver) | 收件人信息 |
| GoodDetail | [object](#Body__GoodDetail) | 物品详情 |
| Scene | number | 1 C端散单, 2 B端退货, 3 B端发货 |

**Body.Sender Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Name | string | 收件人姓名 |
| Tel | string | 收件人座机号码 |
| Mobile | string | 收件人手机号码 |
| Province | string | 省份，比如"广东省" |
| City | string | 地区/市，比如"广州市" |
| Area | string | 区/县，比如"海珠区" |
| Street | string | 街道，比如新港中路 |
| Address | string | 详细地址，比如"XX路XX号XX大厦XX" |

**Body.Receiver Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Name | string | 收件人姓名 |
| Tel | string | 收件人座机号码 |
| Mobile | string | 收件人手机号码 |
| Province | string | 省份，比如"广东省" |
| City | string | 地区/市，比如"广州市" |
| Area | string | 区/县，比如"海珠区" |
| Street | string | 街道，比如新港中路 |
| Address | string | 详细地址，比如"XX路XX号XX大厦XX" |

**Body.GoodDetail Object Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| Weight | number | 货物总重量，比如1.2，单位是千克(kg) | - |
| Special | number | 物品类型，见物品类型说明 | [枚举值](#Enum_Body__GoodDetail__Special) |

**返回体 Response Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ToUserName | string | 是 | 原样返回请求中的FromUserName |
| FromUserName | string | 是 | 快递公司小程序UserName |
| CreateTime | number | 是 | 事件时间，Unix时间戳 |
| MsgType | string | 是 | 消息类型，固定为event |
| Event | string | 是 | 事件类型，固定为query\_single\_waybill，不区分大小写 |
| ResultCode | number | 是 | 处理结果错误码 |
| ResultMsg | string | 否 | 处理结果的详细信息 |
| WayBillID | string | 否 | 运单ID，已生成时必填 |
| Sender | object<addr> | 否 | 发件人信息 |
| Receiver | object<addr> | 否 | 收件人信息 |
| GoodDetail | object<gooddetail> | 否 | 物品详情 |
| Insured | object<insured> | 否 | 保价信息 |
| PathInfo | object<path> | 否 | 轨迹信息 |
| Fee | number | 否 | 运单所需要支付的费用，单位分，费用确定时必填 |
| OriginalFee | number | 否 | 原价，单位分 |
| OnlinePay | number | 是 | 是否支持在线支付，0-不支持，1-支持在线支付 |
| PayResult | number | 是 | 支付结果 0-未支付 1-线上支付完成 2-线下支付完成 |

**Body.GoodDetail.Special Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 文件类 |
| 1 | 电子产品类(包括家用电器) |
| 2 | 办公用品类,服装鞋帽，箱包类 |
| 3 | 化妆品，美容产品类 |
| 4 | 珠宝，手表，眼镜，贵重饰品类 |
| 5 | 食品，保健药品类 |
| 6 | 工艺品类(包括瓷器，茶具，烹饪用品) |
| 7 | 玩具乐器类 |
| 8 | 其他类 |

---

### 查询运单

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/query_waybill.html

**请求体 Request Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 快递公司小程序UserName |
| FromUserName | string | 微信团队的OpenID（固定值） |
| CreateTime | number | 事件时间，Unix时间戳 |
| MsgType | string | 消息类型，固定为event |
| Event | string | 事件类型，固定为query\_single\_waybill，不区分大小写 |
| Token | string | 订单Token，下单时传入的值 |
| WXAppId | string | 下单的小程序的appid |
| WaybillId | string | 运单号，运力方如有更新会同步带上 |
| OrderID | string | 订单ID，可以使用token而不用这个字段 |

**返回体 Response Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ToUserName | string | 是 | 原样返回请求中的FromUserName |
| FromUserName | string | 是 | 快递公司小程序UserName |
| CreateTime | number | 是 | 事件时间，Unix时间戳 |
| MsgType | string | 是 | 消息类型，固定为event |
| Event | string | 是 | 事件类型，固定为query\_single\_waybill，不区分大小写 |
| ResultCode | number | 是 | 处理结果错误码 |
| ResultMsg | string | 否 | 处理结果的详细信息 |
| WayBillID | string | 否 | 运单ID，已生成时必填 |
| Sender | [object](#Res__Sender) | 否 | 发件人信息 |
| Receiver | [object](#Res__Receiver) | 否 | 收件人信息 |
| GoodDetail | [object](#Res__GoodDetail) | 否 | 物品详情 |
| Insured | [object](#Res__Insured) | 否 | 保价信息 |
| PathInfo | [object](#Res__PathInfo) | 否 | 轨迹信息 |
| Fee | number | 否 | 运单所需要支付的费用，单位分，费用确定时必填 |
| OriginalFee | number | 否 | 原价，单位分 |
| OnlinePay | number | 是 | 是否支持在线支付，0-不支持，1-支持在线支付 |
| PayResult | number | 是 | 支付结果 0-未支付 1-线上支付完成 2-线下支付完成 |

**Res.Sender Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| Name | string | 是 | 收件人姓名 |
| Tel | string | 是 | 收件人座机号码 |
| Mobile | string | 是 | 收件人手机号码 |
| Province | string | 是 | 省份，比如"广东省" |
| City | string | 是 | 地区/市，比如"广州市" |
| Area | string | 是 | 区/县，比如"海珠区" |
| Street | string | 否 | 街道，比如新港中路 |
| Address | string | 是 | 详细地址，比如"XX路XX号XX大厦XX" |

**Res.Receiver Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| Name | string | 是 | 收件人姓名 |
| Tel | string | 是 | 收件人座机号码 |
| Mobile | string | 是 | 收件人手机号码 |
| Province | string | 是 | 省份，比如"广东省" |
| City | string | 是 | 地区/市，比如"广州市" |
| Area | string | 是 | 区/县，比如"海珠区" |
| Street | string | 否 | 街道，比如新港中路 |
| Address | string | 是 | 详细地址，比如"XX路XX号XX大厦XX" |

**Res.GoodDetail Object Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| Weight | number | 是 | 货物总重量，比如1.2，单位是千克(kg) | - |
| Special | number | 是 | 物品类型，见物品类型说明 | [枚举值](#Enum_Res__GoodDetail__Special) |

**Res.Insured Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| UseInsured | number | 否 | 是否保价，0表示不保价，1表示保价，默认0 |
| InsuredValue | number | 否 | 保价金额，单位是分，比如:10000表示100元 |

**Res.PathInfo Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path\_info | [objarray](#Res__PathInfo__path_info<Array>) | 是 | 轨迹内容 |

**Res.PathInfo.path_info(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| action\_time | number | 是 | 轨迹变化Unix时间戳 | - |
| action\_type | number | 是 | 轨迹变化类型，与普通单保持一致，参见附录action\_type定义 | [枚举值](#Enum_Res__PathInfo__path_info<Array>__action_type) |
| action\_msg | string | 是 | 轨迹变化具体信息说明，展示在快递轨迹详情页中。若有手机号码，则直接写11位手机号码。使用UTF-8编码。 | - |
| pickup\_courier\_name | string | 否 | 取件员姓名,当分配取件员成功时返回 | - |
| pickup\_courier\_phone | string | 否 | 取件员电话,当分配取件员成功时返回 | - |
| delivery\_courier\_name | string | 否 | 派件员姓名,当分配派件员成功时返回 | - |
| delivery\_courier\_phone | string | 否 | 派件员电话,当分配派件员成功时返回 | - |

**Res.GoodDetail.Special Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 文件类 |
| 1 | 电子产品类(包括家用电器) |
| 2 | 办公用品类,服装鞋帽，箱包类 |
| 3 | 化妆品，美容产品类 |
| 4 | 珠宝，手表，眼镜，贵重饰品类 |
| 5 | 食品，保健药品类 |
| 6 | 工艺品类(包括瓷器，茶具，烹饪用品) |
| 7 | 玩具乐器类 |
| 8 | 其他类 |

**Res.PathInfo.path_info(Array).action_type Enum**

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

### 查询所在城市的预约时间段

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/check_reservation.html

**请求体 Request Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 快递公司小程序 UserName |
| FromUserName | string | 微信团队的 OpenID （固定值） |
| CreateTime | number | 事件时间，Unix时间戳 |
| MsgType | string | 消息类型，固定为 event |
| Event | string | 事件类型，固定为 waybill\_query\_expect\_time\_range，不区分大小写 |
| WXAppId | string | 商户在微信端的appid |
| Province | string | 省份，比如"广东省" |
| City | string | 地区/市，比如"广州市" |
| Area | string | 区/县，比如"海珠区" |
| Street | string | 街道 |
| Address | string | 详细地址 |
| Id | string | 地址id |

**返回体 Response Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ToUserName | string | 是 | 原样返回请求中的 FromUserName |
| FromUserName | string | 是 | 快递公司小程序 UserName |
| CreateTime | number | 是 | 事件时间，Unix 时间戳 |
| MsgType | string | 是 | 消息类型，固定为 event |
| Event | string | 是 | 事件类型，固定为waybill\_query\_expect\_time\_range，不区分大小写 |
| ResultCode | number | 是 | 处理结果错误码 |
| ResultMsg | string | 否 | 处理结果的详细信息 |
| ExpectTimeRange | number | 是 | 预约时间段，比如1或者2，单位小时（此字段废弃不再使用） |
| ValidTimeRange | [objarray](#Res__ValidTimeRange<Array>) | 是 | 可预约时间段 |
| Asap | [object](#Res__Asap) | 否 | 是否可下单后2小时内上门，无此参数返回表示不支持 |

**Res.ValidTimeRange(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| StartTime | number | 是 | 开始时间，小时数（24小时制） |
| EndTime | number | 是 | 结束时间，小时数（24小时制） |
| DayDelta | number | 否 | 天数，0-表示今天 1表示明天 2-表示后天，默认是0 |
| Status | number | 否 | 状态 0-可预约 1-约满，默认可预约 |

**Res.Asap Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| StartTime | number | 是 | 开始时间，小时数（24小时制） |
| EndTime | number | 是 | 结束时间，小时数（24小时制） |
| DayDelta | number | 否 | 天数，0-表示今天 1表示明天 2-表示后天，默认是0 |
| Status | number | 否 | 状态 0-可预约 1-约满，默认可预约 |

---

### 运单轨迹更新事件

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/logistics.onPathUpdate.html

**请求体 Request Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 小程序的原始ID |
| FromUserName | string | 发送者的openid |
| CreateTime | number | 消息创建时间（整型） |
| MsgType | string | 固定 event |
| Event | string | 固定 add\_express\_path |
| DeliveryID | string | 快递公司ID |
| WayBillId | string | 运单ID |
| OrderId | string | 订单ID |
| Version | number | 轨迹版本号（整型） |
| Count | number | 轨迹节点数（整型） |
| Actions | [objarray](#Body__Actions<Array>) | 轨迹列表 |

**Body.Actions(Array) Object Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| ActionTime | number | 轨迹节点 Unix 时间戳 | - |
| ActionType | number | 轨迹节点类型 | [枚举值](#Enum_Body__Actions<Array>__ActionType) |
| ActionMsg | string | 轨迹节点详情 | - |

**Body.Actions(Array).ActionType Enum**

| 枚举值 | 描述 |
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

---

### 支付完成通知

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/payment_completion_notification.html

**请求体 Request Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 快递公司小程序 UserName |
| FromUserName | string | 微信团队的 OpenID （固定值） |
| CreateTime | number | 事件时间，Unix时间戳 |
| MsgType | string | 消息类型，固定为 event |
| Event | string | 事件类型，固定为 notify\_single\_waybill\_pay，不区分大小写 |
| Token | string | 下单接口传的Token |
| WXAppId | string | 商户在微信端的appid |
| OrderID | string | 商户订单 ID，可以使用token而不用这个字段 |
| WayBillID | string | 运单 ID |
| Fee | number | 支付金额，单位分 |
| OriginalFee | number | 原价，单位分 |
| PayOrderId | string | 支付订单号 |
| PayFinishTime | number | 支付成功时间，10位时间戳 |

**返回体 Response Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ToUserName | string | 是 | 原样返回请求中的 FromUserName |
| FromUserName | string | 是 | 快递公司小程序 UserName |
| CreateTime | number | 是 | 事件时间，Unix 时间戳 |
| MsgType | string | 是 | 消息类型，固定为 event |
| Event | string | 是 | 事件类型，固定为 query\_single\_waybill\_pay，不区分大小写 |
| ResultCode | number | 是 | 处理结果错误码 |
| ResultMsg | string | 否 | 处理结果的详细信息 |

---

### 给小哥评价

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/rate_my_brother.html

**请求体 Request Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 快递公司小程序 UserName |
| FromUserName | string | 微信团队的 OpenID （固定值） |
| CreateTime | number | 事件时间，Unix时间戳 |
| MsgType | string | 消息类型，固定为 event |
| Event | string | 事件类型，固定为 waybill\_evaluate\_agent，不区分大小写 |
| Token | string | 下单接口传的Token |
| WXAppId | string | 商户在微信端的appid |
| OrderID | string | 商户订单ID，可以使用token而不用这个字段 |
| WayBillID | string | 运单 ID |
| CourierType | number | 0, 取件员，1.派件员 |
| Score | number | 1-5分，最低1分，最高5分 |

**返回体 Response Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ToUserName | string | 是 | 原样返回请求中的 FromUserName |
| FromUserName | string | 是 | 快递公司小程序 UserName |
| CreateTime | number | 是 | 事件时间，Unix 时间戳 |
| MsgType | string | 是 | 消息类型，固定为 event |
| Event | string | 是 | 事件类型，固定为 waybill\_evaluate\_agent，不区分大小写 |
| ResultCode | number | 是 | 处理结果错误码 |
| ResultMsg | string | 否 | 处理结果的详细信息 |

---

### 用户投诉

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/user_complaints.html

**请求体 Request Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| ToUserName | string | 快递公司小程序 UserName | - |
| FromUserName | string | 微信团队的 OpenID （固定值） | - |
| CreateTime | number | 事件时间，Unix时间戳 | - |
| MsgType | string | 消息类型，固定为 event | - |
| Event | string | 事件类型，固定为 waybill\_complaint，不区分大小写 | - |
| Token | string | 下单接口传的Token | - |
| WXAppId | string | 商户在微信端的appid | - |
| OrderID | string | 商户订单 ID，可以使用token而不用这个字段 | - |
| WayBillID | string | 运单 ID | - |
| ComplainType | number | 投诉类型 | [枚举值](#Enum_Body__ComplainType) |
| Content | string | 投诉内容 | - |
| Pic | string | 多张投诉材料图片链接，竖线分割，比如: url1 | - |
| Name | string | 联系人姓名 | - |
| Phone | string | 联系人电话 | - |

**返回体 Response Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ToUserName | string | 是 | 原样返回请求中的 FromUserName |
| FromUserName | string | 是 | 快递公司小程序 UserName |
| CreateTime | number | 是 | 事件时间，Unix 时间戳 |
| MsgType | string | 是 | 消息类型，固定为 event |
| Event | string | 是 | 事件类型，固定为 waybill\_complaint，不区分大小写 |
| ResultCode | number | 是 | 处理结果错误码 |
| ResultMsg | string | 否 | 处理结果的详细信息 |

**Body.ComplainType Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1004 | 快件延误 |
| 1005 | 快件丢失 |
| 1006 | 快件破损短少 |
| 1007 | 服务态度 |
| 1008 | 其他 |

---

### logistics.onBindResultUpdate

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/business/Bind_merchant_review_result_update_event.html

---

### 理赔结果推送

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/business/claim_settlement_result.html

**请求体 Request Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| OrderNo | string | 支付单号 | - |
| Status | number | 保单状态 | [枚举值](#Enum_Body__Status) |
| FinishTime | number | 理赔成功时间 | - |
| PayFailReason | string | 理赔失败原因 | - |

**Body.Status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 5 | 理赔成功 |
| 6 | 理赔失败 |

---

### onOrderStatus

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/deliver/deliver_by_business/Delivery_order_delivery_status_update_notification_interface.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 快递公司小程序 UserName |
| FromUserName | string | 微信团队的 OpenID （固定值） |
| CreateTime | number | 事件时间，Unix时间戳 |
| MsgType | string | 消息类型，固定为 event |
| Event | string | 事件类型，固定为 update\_waybill\_status，不区分大小写 |
| shopid | string | 商家id， 由配送公司分配的appkey |
| shop\_order\_id | string | 唯一标识订单的 ID，由商户生成 |
| shop\_no | string | 商家门店编号， 在配送公司侧登记 |
| waybill\_id | string | 配送单id |
| action\_time | number | Unix时间戳 |
| order\_status | number | 配送状态，详见下方的order\_status 枚举值 |
| action\_msg | string | 附加信息 |
| agent | Object | 骑手信息 |

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| name | string | 骑手姓名 |
| phone | string | 骑手电话 |
| reach\_time | number | 预计送达时间戳, 配送中返回 |

**Object**

| 值 | 说明 |
| --- | --- |
| 101 | 配送公司接单阶段——等待分配骑手，即初始状态 |
| 102 | 配送公司接单阶段——分配骑手成功 |
| 103 | 配送公司接单阶段——商家取消订单， 订单结束 |
| 201 | 骑手取货阶段——骑手到店开始取货 |
| 202 | 骑手取货阶段——取货成功 |
| 203 | 骑手取货阶段——取货失败，商家取消订单， 订单结束 |
| 204 | 骑手取货阶段——取货失败，骑手因自身原因取消订单， 订单结束 |
| 205 | 骑手取货阶段——取货失败，骑手因商家原因取消订单， 订单结束 |
| 301 | 骑手配送阶段——配送中 |
| 302 | 骑手配送阶段——配送成功， 订单结束 |
| 303 | 骑手配送阶段——商家取消订单，配送物品开始返还商家 |
| 304 | 骑手配送阶段——无法联系收货人，配送物品开始返还商家 |
| 305 | 骑手配送阶段——收货人拒收，配送物品开始返还商家 |
| 401 | 骑手返回配送货品阶段——货品返还商户成功， 订单结束 |
| 501 | 因运力系统原因取消， 订单结束 |
| 502 | 因不可抗拒因素（天气，道路管制等原因）取消，订单结束 |

**Object**

| 服务通知 | 对应的order\_status值 |
| --- | --- |
| 骑手已接单 | 102 |
| 骑手已取货，配送中 | 202或301 |
| 配送已完成 | 302 |
| 配送异常 | 203、204、205、303、304、305、501、502 |

**消息返回**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| ToUserName | string |  | 是 | 原样返回请求中的 FromUserName |
| FromUserName | string |  | 是 | 快递公司小程序 UserName |
| CreateTime | number |  | 是 | 事件时间，Unix时间戳 |
| MsgType | string |  | 是 | 消息类型，固定为 event |
| Event | string |  | 是 | 事件类型，固定为 update\_waybill\_status，不区分大小写 |
| resultcode | number |  | 是 | 错误码 |
| resultmsg | string |  | 是 | 错误描述 |

---

### immediateDelivery.onMockUpdateOrder

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/deliver/deliver_by_provider/Simulate_update_order_status_interface.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 快递公司小程序 UserName |
| FromUserName | string | 微信团队的 OpenID （固定值） |
| CreateTime | number | 事件时间，Unix时间戳 |
| MsgType | string | 消息类型，固定为 event |
| Event | string | 事件类型，固定为 mock\_update\_order\_status，不区分大小写 |
| shopid | string | 商家id， 由配送公司分配，可以是dev\_id或者appkey |
| shop\_order\_id | string | 唯一标识订单的 ID，由商户生成 |
| shop\_no | string | 商家门店编号， 在配送公司侧登记 |
| waybill\_id | string | 配送单id |
| delivery\_sign | string | 用配送公司侧提供的appSecret加密的校验串 |
| order\_status | number | 订单状态，详见下方的order\_status 枚举值 |
| action\_time | number | 状态变更时间点，Unix秒级时间戳 |
| action\_msg | string | 附加信息（选填） |

**Object**

| 值 | 说明 |
| --- | --- |
| 101 | 配送公司接单阶段——等待分配骑手，即初始状态 |
| 102 | 配送公司接单阶段——分配骑手成功 |
| 103 | 配送公司接单阶段——商家取消订单， 订单结束 |
| 201 | 骑手取货阶段——骑手到店开始取货 |
| 202 | 骑手取货阶段——取货成功 |
| 203 | 骑手取货阶段——取货失败，商家取消订单， 订单结束 |
| 204 | 骑手取货阶段——取货失败，骑手因自身原因取消订单， 订单结束 |
| 205 | 骑手取货阶段——取货失败，骑手因商家原因取消订单， 订单结束 |
| 301 | 骑手配送阶段——配送中 |
| 302 | 骑手配送阶段——配送成功， 订单结束 |
| 303 | 骑手配送阶段——商家取消订单，配送物品开始返还商家 |
| 304 | 骑手配送阶段——无法联系收货人，配送物品开始返还商家 |
| 305 | 骑手配送阶段——收货人拒收，配送物品开始返还商家 |
| 401 | 骑手返回配送货品阶段——货品返还商户成功， 订单结束 |
| 501 | 因运力系统原因取消， 订单结束 |
| 502 | 因不可抗拒因素（天气，道路管制等原因）取消，订单结束 |

**Object**

| 服务通知 | 对应的order\_status值 |
| --- | --- |
| 骑手已接单 | 102 |
| 骑手已取货，配送中 | 202或301 |
| 配送已完成 | 302 |
| 配送异常 | 203、204、205、303、304、305、501、502 |

**消息返回**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| ToUserName | string |  | 是 | 原样返回请求中的 FromUserName |
| FromUserName | string |  | 是 | 快递公司小程序 UserName |
| CreateTime | number |  | 是 | 事件时间，Unix时间戳 |
| MsgType | string |  | 是 | 消息类型，固定为 event |
| Event | string |  | 是 | 事件类型，固定为 mock\_update\_order\_status，不区分大小写 |
| resultcode | number |  | 是 | 错误码 |
| resultmsg | string |  | 是 | 错误描述 |

---

### immediateDelivery.onOrderCancel

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/deliver/deliver_by_provider/Cancel_order_operation.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 快递公司小程序 UserName |
| FromUserName | string | 微信团队的 OpenID （固定值） |
| CreateTime | number | 事件时间，Unix时间戳 |
| MsgType | string | 消息类型，固定为 event |
| Event | string | 事件类型，固定为 transport\_cancel\_order，不区分大小写 |
| shopid | string | 商家id， 由配送公司分配，可以是dev\_id或者appkey |
| shop\_order\_id | string | 唯一标识订单的 ID，由商户生成 |
| shop\_no | string | 商家门店编号， 在配送公司侧登记 |
| waybill\_id | string | 配送单id |
| delivery\_sign | string | 用配送公司侧提供的appSecret加密的校验串 |
| cancel\_reason\_id | number | 取消原因id |
| cancel\_reason | string | 取消原因 |

**Object**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 1 | 暂时不需要邮寄 |  |
| 2 | 价格不合适 |  |
| 3 | 订单信息有误，重新下单 |  |
| 4 | 骑手取货不及时 |  |
| 5 | 骑手配送不及时 |  |
| 6 | 其他原因( 如果选择6，需要填写取消原因，否则不需要填写 ) |  |

**消息返回**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| ToUserName | string |  | 是 | 原样返回请求中的 FromUserName |
| FromUserName | string |  | 是 | 快递公司小程序 UserName |
| CreateTime | number |  | 是 | 事件时间，Unix时间戳 |
| MsgType | string |  | 是 | 消息类型，固定为 event |
| Event | string |  | 是 | 事件类型，固定为 transport\_cancel\_order，不区分大小写 |
| resultcode | number |  | 是 | 错误码 |
| resultmsg | string |  | 是 | 错误描述 |
| deduct\_fee | number |  | 是 | 扣除的违约金(单位：元)，可能没有 |
| desc | string |  | 是 | 扣费说明 |

---

### immediateDelivery.onOrderConfirmReturn

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/deliver/deliver_by_provider/Exceptionally_delivered_merchant_receipt_confirmation.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 快递公司小程序 UserName |
| FromUserName | string | 微信团队的 OpenID （固定值） |
| CreateTime | number | 事件时间，Unix时间戳 |
| MsgType | string | 消息类型，固定为 event |
| Event | string | 事件类型，固定为 transport\_confirm\_return\_to\_biz，不区分大小写 |
| shopid | string | 商家id， 由配送公司分配，可以是dev\_id或者appkey |
| shop\_order\_id | string | 唯一标识订单的 ID，由商户生成 |
| shop\_no | string | 商家门店编号， 在配送公司侧登记 |
| waybill\_id | string | 配送单id |
| delivery\_sign | string | 用配送公司侧提供的appSecret加密的校验串 |

**消息返回**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| ToUserName | string |  | 是 | 原样返回请求中的 FromUserName |
| FromUserName | string |  | 是 | 快递公司小程序 UserName |
| CreateTime | number |  | 是 | 事件时间，Unix时间戳 |
| MsgType | string |  | 是 | 消息类型，固定为 event |
| Event | string |  | 是 | 事件类型，固定为 transport\_confirm\_return\_to\_biz，不区分大小写 |
| resultcode | number |  | 是 | 错误码 |
| resultmsg | string |  | 是 | 错误描述 |

---

### immediateDelivery.onOrderPreCancel

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/deliver/deliver_by_provider/Precancellation_of_orders.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 快递公司小程序 UserName |
| FromUserName | string | 微信团队的 OpenID （固定值） |
| CreateTime | number | 事件时间，Unix时间戳 |
| MsgType | string | 消息类型，固定为 event |
| Event | string | 事件类型，固定为 transport\_precancel\_order，不区分大小写 |
| shopid | string | 商家id， 由配送公司分配，可以是dev\_id或者appkey |
| shop\_order\_id | string | 唯一标识订单的 ID，由商户生成 |
| shop\_no | string | 商家门店编号， 在配送公司侧登记 |
| waybill\_id | string | 配送单id |
| delivery\_sign | string | 用配送公司侧提供的appSecret加密的校验串 |
| cancel\_reason\_id | number | 取消原因id |
| cancel\_reason | string | 取消原因 |

**Object**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 1 | 暂时不需要邮寄 |  |
| 2 | 价格不合适 |  |
| 3 | 订单信息有误，重新下单 |  |
| 4 | 骑手取货不及时 |  |
| 5 | 骑手配送不及时 |  |
| 6 | 其他原因( 如果选择6，需要填写取消原因，否则不需要填写 ) |  |

**消息返回**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| ToUserName | string |  | 是 | 原样返回请求中的 FromUserName |
| FromUserName | string |  | 是 | 快递公司小程序 UserName |
| CreateTime | number |  | 是 | 事件时间，Unix时间戳 |
| MsgType | string |  | 是 | 消息类型，固定为 event |
| Event | string |  | 是 | 事件类型，固定为 transport\_precancel\_order，不区分大小写 |
| resultcode | number |  | 是 | 错误码 |
| resultmsg | string |  | 是 | 错误描述 |
| deduct\_fee | number |  | 是 | 预计扣除的违约金(单位：元)，可能没有 |
| desc | string |  | 是 | 扣费说明 |

---

### immediateDelivery.onOrderQuery

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/deliver/deliver_by_provider/Check_order_status.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 快递公司小程序 UserName |
| FromUserName | string | 微信团队的 OpenID （固定值） |
| CreateTime | number | 事件时间，Unix时间戳 |
| MsgType | string | 消息类型，固定为 event |
| Event | string | 事件类型，固定为 transport\_query\_order\_status，不区分大小写 |
| shopid | string | 商家id， 由配送公司分配，可以是dev\_id或者appkey |
| shop\_order\_id | string | 唯一标识订单的 ID，由商户生成 |
| shop\_no | string | 商家门店编号， 在配送公司侧登记 |
| waybill\_id | string | 配送单id |
| delivery\_sign | string | 用配送公司侧提供的appSecret加密的校验串 |

**消息返回**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| ToUserName | string |  | 是 | 原样返回请求中的 FromUserName |
| FromUserName | string |  | 是 | 快递公司小程序 UserName |
| CreateTime | number |  | 是 | 事件时间，Unix时间戳 |
| MsgType | string |  | 是 | 消息类型，固定为 event |
| Event | string |  | 是 | 事件类型，固定为 transport\_query\_order\_status，不区分大小写 |
| resultcode | number |  | 是 | 错误码 |
| resultmsg | string |  | 是 | 错误描述 |
| order\_status | number |  | 是 | 当前订单状态，详见下方order\_status 枚举值 |
| action\_msg | string |  | 否 | 附加信息 |
| waybill\_id | string |  | 是 | 配送单id |

**消息返回**

| 值 | 说明 |
| --- | --- |
| 101 | 配送公司接单阶段——等待分配骑手，即初始状态 |
| 102 | 配送公司接单阶段——分配骑手成功 |
| 103 | 配送公司接单阶段——商家取消订单， 订单结束 |
| 201 | 骑手取货阶段——骑手到店开始取货 |
| 202 | 骑手取货阶段——取货成功 |
| 203 | 骑手取货阶段——取货失败，商家取消订单， 订单结束 |
| 204 | 骑手取货阶段——取货失败，骑手因自身原因取消订单， 订单结束 |
| 205 | 骑手取货阶段——取货失败，骑手因商家原因取消订单， 订单结束 |
| 301 | 骑手配送阶段——配送中 |
| 302 | 骑手配送阶段——配送成功， 订单结束 |
| 303 | 骑手配送阶段——商家取消订单，配送物品开始返还商家 |
| 304 | 骑手配送阶段——无法联系收货人，配送物品开始返还商家 |
| 305 | 骑手配送阶段——收货人拒收，配送物品开始返还商家 |
| 401 | 骑手返回配送货品阶段——货品返还商户成功， 订单结束 |
| 501 | 因运力系统原因取消， 订单结束 |
| 502 | 因不可抗拒因素（天气，道路管制等原因）取消，订单结束 |

**消息返回**

| 服务通知 | 对应的order\_status值 |
| --- | --- |
| 骑手已接单 | 102 |
| 骑手已取货，配送中 | 202或301 |
| 配送已完成 | 302 |
| 配送异常 | 203、204、205、303、304、305、501、502 |

---

### 媒资上传完成事件

如果开发者是小程序商家，请移步：消息推送

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/mini_drama/asset_upload_completion_event.html

| 属性 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| media\_id | number | 是 | 媒资id。 |
| source\_context | string | 否 | 透传上传接口中开发者设置的值。 |
| errcode | number | 是 | 错误码，上传失败时该值非0。 |
| errmsg | string | 否 | 错误提示。 |

---

### 审核状态事件

如果开发者是小程序商家，请移步：消息推送

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/mini_drama/drama_review_status_event.html

| 属性 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| drama\_id | number | 是 | 剧目id。 |
| audit\_detail | DramaAuditDetail | 是 | 剧目审核结果，单独每一集的审核结果可以根据drama\_id查询剧集详情得到。 |

---

### 付费管理订单用量告警事件

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/charge/charge_mp_service_quota_notify.html

**请求体 Request Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| event\_type | number | 事件类型，固定值 3 |
| appid | string | 小程序AppID |
| spu\_id | number | 购买的商品的SPU\_ID |
| spu\_name | string | 购买的商品的SPU\_NAME |
| total\_quota | number | 所购 SPU 当前总的用量 |
| total\_used\_quota | number | 所购 SPU 当前总已使用的用量 |

---

### 付费管理订单有效期告警事件

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/charge/charge_mp_service_validity_notify.html

**请求体 Request Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| event\_type | number | 事件类型，固定值 4 |
| appid | string | 小程序AppID |
| spu\_id | number | 购买的商品的SPU\_ID |
| spu\_name | string | 购买的商品的SPU\_NAME |
| validity\_end\_time | string | 购买的SPU的有效期到期时间 |

---

### 评价管理差评通知事件

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/guarantee/negative.html

**请求体 Request Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 商家小程序名称 |
| FromUserName | string | 微信团队的 OpenID(固定值) |
| CreateTime | number | 事件时间,Unix时间戳 |
| MsgType | string | 消息类型，固定为event |
| Event | string | 事件类型，固定为 wxa\_comment\_bad\_score |
| result | [object](#Body__result) | 结果对象 |

**Body.result Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| comment\_id | string | 评价 ID |

---

### 长期订阅状态通知

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/liveplayer/status_synchronization.html

**请求体 Request Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| ToUserName | string | 小程序的原始ID | - |
| FromUserName | string | 发送者的openid | - |
| CreateTime | number | 消息创建时间（整型） | - |
| MsgType | string | 固定 event | - |
| Event | string | 固定 wxalive\_follow\_notify | - |
| room\_id | number | 房间号 | - |
| user\_openid | string | 订阅者的openid | - |
| time | number | 订阅的时间戳 | - |
| live\_status | number | 阅或者取消订阅时直播间状态，取值： | [枚举值](#Enum_Body__live_status) |
| action | string | 订阅行为 | [枚举值](#Enum_Body__action) |

**Body.live_status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 101 | 直播中 |
| 102 | 未开始 |
| 103 | 已结束 |

**Body.action Enum**

| 枚举值 | 描述 |
| --- | --- |
| add\_follow | 订阅 |
| del\_follow | 取消订阅 |

---

### 长期订阅群发结果通知

本文档描述服务器端接收的消息或事件，详细说明参见消息推送。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/event_push/liveplayer/longterm_subscription.html

**请求体 Request Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 小程序的原始ID |
| FromUserName | string | 发送者的OpenId |
| CreateTime | number | 消息创建时间（整型） |
| MsgType | string | 固定 event |
| Event | string | 固定 wxalive\_push\_message\_notify |
| message\_id | string | 群发消息的标识ID |
| room\_id | number | 房间号 |
| total\_count | number | 群发消息user\_openid的总数 |
| success\_count | number | 群发消息成功数量 |
| openid\_error\_count | number | openid错误数量 |
| relation\_error\_count | number | 用户未关注此小程序导致出错数量 |
| user\_recv\_limit\_count | number | 用户接收消息超出限制导致出错数量 |
| internal\_error\_count | number | 其他错误数量 |

---

<!-- pages: 31 -->
