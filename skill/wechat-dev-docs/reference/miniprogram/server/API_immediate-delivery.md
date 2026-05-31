# 小程序服务端 API 结构化参考 — API/immediate-delivery

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 获取已支持的配送公司列表

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-business/api_getallimmedelivery.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| resultcode | number | 运力返回的错误码 |
| resultmsg | string | 运力返回的错误描述 |
| list | [objarray](#Res__list<Array>) | 配送公司列表 |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| delivery\_id | string | 配送公司Id |
| delivery\_name | string | 配送公司名称 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 预下配送单

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-business/api_preaddorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shopid | string | 是 | 商家id， 由配送公司分配的appkey |
| shop\_order\_id | string | 是 | 唯一标识订单的 ID，由商户生成, 不超过128字节 |
| delivery\_id | string | 是 | 配送公司ID |
| openid | string | 是 | 下单用户的openid |
| sender | [object](#Body__sender) | 是 | 发件人信息，闪送、顺丰同城急送必须填写，美团配送、达达，若传了shop\_no的值可不填该字段 |
| receiver | [object](#Body__receiver) | 是 | 收件人信息 |
| cargo | [object](#Body__cargo) | 是 | 货物信息 |
| order\_info | [object](#Body__order_info) | 是 | 订单信息 |
| shop | [object](#Body__shop) | 是 | 商品信息，会展示到物流通知消息中 |
| delivery\_sign | string | 是 | 用配送公司提供的appSecret加密的校验串说明 |
| shop\_no | string | 是 | 商家门店编号，在配送公司登记，美团、闪送必填 |
| sub\_biz\_id | string | 是 | 子商户id，区分小程序内部多个子商户 |

**Body.sender Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 姓名，最长不超过256个字符 |
| city | string | 是 | 城市名称，如广州市 |
| address | string | 是 | 地址(街道、小区、大厦等，用于定位) |
| address\_detail | string | 是 | 地址详情(楼号、单元号、层号) |
| phone | string | 是 | 电话/手机号，最长不超过64个字符 |
| lng | number | 是 | 经度（火星坐标或百度坐标，和 coordinate\_type 字段配合使用，确到小数点后6位 |
| lat | number | 是 | 纬度（火星坐标或百度坐标，和 coordinate\_type 字段配合使用，精确到小数点后6位） |
| coordinate\_type | number | 否 | 坐标类型，0：火星坐标（高德，腾讯地图均采用火星坐标） 1：百度坐标 |

**Body.receiver Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 姓名，最长不超过256个字符 |
| city | string | 是 | 城市名称，如广州市 |
| address | string | 是 | 地址(街道、小区、大厦等，用于定位) |
| address\_detail | string | 是 | 地址详情(楼号、单元号、层号) |
| phone | string | 是 | 电话/手机号，最长不超过64个字符 |
| lng | number | 是 | 经度（火星坐标或百度坐标，和 coordinate\_type 字段配合使用，确到小数点后6位 |
| lat | number | 是 | 纬度（火星坐标或百度坐标，和 coordinate\_type 字段配合使用，精确到小数点后6位） |
| coordinate\_type | number | 否 | 坐标类型，0：火星坐标（高德，腾讯地图均采用火星坐标） 1：百度坐标 |

**Body.cargo Object Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| goods\_value | number | 是 | 货物价格，单位为元，精确到小数点后两位（如果小数点后位数多于两位，则四舍五入保留两位小数），范围为(0-5000] | - |
| goods\_height | number | 否 | 货物高度，单位为cm，精确到小数点后两位（如果小数点后位数多于两位，则四舍五入保留两位小数），范围为(0-45] | - |
| goods\_width | number | 否 | 货物宽度，单位为cm，精确到小数点后两位（如果小数点后位数多于两位，则四舍五入保留两位小数），范围为(0-50] | - |
| goods\_length | number | 否 | 货物长度，单位为cm，精确到小数点后两位（如果小数点后位数多于两位，则四舍五入保留两位小数），范围为(0-65] | - |
| goods\_weight | number | 是 | 货物重量，单位为kg，精确到小数点后两位（如果小数点后位数多于两位，则四舍五入保留两位小数），范围为(0-50] | - |
| goods\_detail | [object](#Body__cargo__goods_detail) | 否 | 货物详情，最长不超过10240个字符 | - |
| goods\_pickup\_info | string | 否 | 货物取货信息，用于骑手到店取货，最长不超过100个字符 | - |
| cargo\_first\_class | string | 是 | 品类一级类目, | [枚举值](#Enum_Body__cargo__cargo_first_class) |
| cargo\_second\_class | string | 是 | 品类二级类目 | - |

**Body.order_info Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delivery\_service\_code | string | 否 | 配送服务代码 不同配送公司自定义, 顺丰和达达不填 |
| expected\_delivery\_time | number | 否 | 期望派单时间(达达支持，表示达达系统调度时间, 到那个时间才会有状态更新的回调通知)，unix-timestamp, 比如1586342180 |
| order\_type | number | 否 | 订单类型, 0: 即时单 1 预约单，如预约单，需要设置expected\_delivery\_time或expected\_finish\_time或expected\_pick\_time |
| poi\_seq | string | 否 | 门店订单流水号，建议提供，方便骑手门店取货，最长不超过32个字符 |
| note | string | 否 | 备注，最长不超过200个字符 |
| order\_time | number | 否 | 用户下单付款时间, 顺丰必填, 比如1555220757 |
| is\_insured | number | 否 | 是否保价，0，非保价，1.保价 |
| declared\_value | number | 否 | 保价金额，单位为元，精确到分 |
| tips | number | 否 | 小费，单位为元, 下单一般不加小费 |
| is\_direct\_delivery | number | 否 | 是否选择直拿直送（0：不需要；1：需要。选择直拿直送后，同一时间骑手只能配送此订单至完成，配送费用也相应高一些，闪送必须选1，达达可选0或1，其余配送公司不支持直拿直送） |
| cash\_on\_delivery | number | 否 | 骑手应付金额，单位为元，精确到分 |
| cash\_on\_pickup | number | 否 | 骑手应收金额，单位为元，精确到分 |
| rider\_pick\_method | number | 否 | 物流流向，1：从门店取件送至用户；2：从用户取件送至门店 |
| is\_finish\_code\_needed | number | 否 | 收货码（0：不需要；1：需要。收货码的作用是：骑手必须输入收货码才能完成订单妥投） |
| is\_pickup\_code\_needed | number | 否 | 取货码（0：不需要；1：需要。取货码的作用是：骑手必须输入取货码才能从商家取货） |
| expected\_finish\_time | number | 否 | 期望送达时间(美团、顺丰同城急送支持），unix-timestamp, 比如1586342180 |
| expected\_pick\_time | number | 否 | 期望取件时间（闪送、顺丰同城急送支持，闪送需要设置两个小时后的时间，顺丰同城急送只需传expected\_finish\_time或expected\_pick\_time其中之一即可，同时都传则以expected\_finish\_time为准），unix-timestamp, 比如1586342180 |

**Body.shop Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wxa\_path | string | 否 | 商家小程序的路径，建议为订单页面 |
| img\_url | string | 否 | 商品缩略图 url；shop.detail\_list为空则必传，shop.detail\_list非空可不传。 |
| goods\_name | string | 否 | 商品名称, 不超过128字节；shop.detail\_list为空则必传，shop.detail\_list非空可不传。 |
| goods\_count | number | 否 | 商品数量；shop.detail\_list为空则必传。shop.detail\_list非空可不传，默认取shop.detail\_list的size |
| wxa\_appid | string | 否 | 该参数在【即时配送】的[addLocalOrder](api_addlocalorder)接口才生效。若结算方式为：第三方向配送公司统一结算，商户后续和第三方结算，则该参数必填；在该结算模式下，第三方用自己的开发小程序替授权商户发起下单，并将授权小程序的appid给平台，后续配送通知中可回流授权商户小程序。 |

**Body.cargo.goods_detail Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| goods | [objarray](#Body__cargo__goods_detail__goods<Array>) | 是 | 货物列表 |

**Body.cargo.goods_detail.goods(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| good\_count | number | 是 | 货物数量 |
| good\_name | string | 是 | 货品名称 |
| good\_price | number | 否 | 货品单价，精确到小数点后两位（如果小数点后位数多于两位，则四舍五入保留两位小数） |
| good\_unit | string | 否 | 货品单位，最长不超过20个字符 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| resultcode | number | 运力返回的错误码 |
| resultmsg | string | 运力返回的错误描述 |
| fee | number | 实际运费(单位：元)，运费减去优惠券费用 |
| deliverfee | number | 运费(单位：元) |
| couponFee | number | 优惠券费用(单位：元) |
| tips | number | 小费(单位：元) |
| insurancefee | number | 保价费(单位：元) |
| distance | number | 配送距离(单位：米)预计骑手接单时间，单位秒，比如5分钟，就填300, 无法预计填0 |
| delivery\_token | string | 配送公司可以返回此字段，当用户下单时候带上这个字段，保证在一段时间内运费不变 |
| dispatch\_duration | number | 预计骑手接单时间，单位秒，比如5分钟，就填300, 无法预计填0 |

**Body.cargo.cargo_first_class Enum**

| 枚举值 | 描述 |
| --- | --- |
| 美食夜宵 | 零食小吃 香锅/烤鱼 西餐 日韩料理 海鲜/烧烤 快餐/地方菜 小龙虾 披萨 |
| 甜品饮料 | 甜品 奶茶果汁 咖啡 面包/糕点 冰淇淋 |
| 蛋糕 | 蛋糕 |
| 日用百货 | 便利店 水站/奶站 零食/干果 五金日用 粮油调味 文具店 酒水行 地方特产 进口食品 宠物用品 超市 书店 宠物食品用品 办公家居用品 |
| 果蔬生鲜 | 果蔬 海鲜水产 冷冻速食 |
| 鲜花 | 鲜花 |
| 医药健康 | 送药 器材器具 |
| 美妆护肤 | 日化美妆 |
| 母婴 | 孕婴用品 |
| 文件或票务 | 保单 票务文件 政府文件 证件 |
| 服饰鞋帽 | 服饰鞋帽综合 |
| 洗涤 | 脏衣服收 干净衣服派 |
| 珠宝奢侈品 | 珠宝饰品 奢侈品 |
| 家居家装 | 家具 装修建材 厨房卫浴 |
| 数码产品 | 数码产品 |
| 配件器材 | 配件器材 |
| 电商 | 电视购物 线上商城 |
| 现场勘查 | 现场勘查 |
| 快递业务 | 快递配送 |
| 其他 | 其他 |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 拉取已绑定账号

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-business/api_getbindaccount.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| resultcode | number | 运力返回的错误码 |
| resultmsg | string | 力返回的错误描述 |
| shop\_list | [objarray](#Res__shop_list<Array>) | 绑定的商家签约账号列表 |

**Res.shop_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| shopid | string | 商家id |
| delivery\_id | string | 配送公司Id |
| audit\_result | number | 审核状态.0表示审核通过；1表示审核中；2表示审核不通过。 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 预取消配送单

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-business/api_precancelorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shopid | string | 是 | 商家id， 由配送公司分配的appkey |
| shop\_order\_id | string | 是 | 唯一标识订单的 ID，由商户生成 |
| delivery\_id | string | 是 | 快递公司ID |
| waybill\_id | string | 是 | 配送单id |
| cancel\_reason\_id | number | 否 | 取消原因Id |
| cancel\_reason | string | 否 | 取消原因 |
| shop\_no | string | 是 | 商家门店编号，在配送公司登记，闪送shop\_no必填，值为店铺id |
| delivery\_sign | string | 是 | 用配送公司提供的appSecret加密的校验串说明 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| resultcode | number | 运力返回的错误码 |
| resultmsg | string | 运力返回的错误描述 |
| deduct\_fee | number | 预计扣除的违约金(单位：元)，精确到分 |
| desc | string | 说明 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

---

### 申请开通即时配送

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-business/api_opendelivery.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| resultcode | number | 运力返回的错误码 |
| resultmsg | string | 运力返回的错误描述 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 发起绑定请求

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-business/api_bindlocalaccount.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delivery\_id | string | 是 | 配送公司ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| resultcode | number | 运力返回的错误码 |
| resultmsg | string | 运力返回的错误描述 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

---

### 重新下单

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-business/api_reorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shopid | string | 是 | 商家id，由配送公司分配的appkey |
| shop\_order\_id | string | 是 | 唯一标识订单的 ID，由商户生成, 不超过128字节 |
| delivery\_id | string | 是 | 配送公司ID |
| openid | string | 是 | 下单用户的openid |
| sender | [object](#Body__sender) | 是 | 发件人信息，顺丰同城急送必须填写，美团配送、达达、闪送，若传了shop\_no的值可不填该字段 |
| receiver | [object](#Body__receiver) | 是 | 收件人信息 |
| cargo | [object](#Body__cargo) | 是 | 货物信息 |
| order\_info | [object](#Body__order_info) | 是 | 订单信息 |
| shop | [object](#Body__shop) | 是 | 商品信息，会展示到物流通知消息中 |
| delivery\_token | string | 是 | 预下单接口返回的参数，配送公司可保证在一段时间内运费不变 |
| delivery\_sign | string | 是 | 用配送公司提供的appSecret加密的校验串说明 |
| shop\_no | string | 是 | 商家门店编号，在配送公司登记，如果只有一个门店，美团闪送必填, 值为店铺id |
| sub\_biz\_id | string | 否 | 子商户id，区分小程序内部多个子商户 |

**Body.sender Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 姓名，最长不超过256个字符 |
| city | string | 是 | 城市名称，如广州市 |
| address | string | 是 | 地址(街道、小区、大厦等，用于定位) |
| address\_detail | string | 是 | 地址详情(楼号、单元号、层号) |
| phone | string | 是 | 电话/手机号，最长不超过64个字符 |
| lng | number | 是 | 经度（火星坐标或百度坐标，和 coordinate\_type 字段配合使用，确到小数点后6位 |
| lat | number | 是 | 纬度（火星坐标或百度坐标，和 coordinate\_type 字段配合使用，精确到小数点后6位） |
| coordinate\_type | number | 否 | 坐标类型，0：火星坐标（高德，腾讯地图均采用火星坐标） 1：百度坐标 |

**Body.receiver Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 姓名，最长不超过256个字符 |
| city | string | 是 | 城市名称，如广州市 |
| address | string | 是 | 地址(街道、小区、大厦等，用于定位) |
| address\_detail | string | 是 | 地址详情(楼号、单元号、层号) |
| phone | string | 是 | 电话/手机号，最长不超过64个字符 |
| lng | number | 是 | 经度（火星坐标或百度坐标，和 coordinate\_type 字段配合使用，确到小数点后6位 |
| lat | number | 是 | 纬度（火星坐标或百度坐标，和 coordinate\_type 字段配合使用，精确到小数点后6位） |
| coordinate\_type | number | 否 | 坐标类型，0：火星坐标（高德，腾讯地图均采用火星坐标） 1：百度坐标 |

**Body.cargo Object Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| goods\_value | number | 是 | 货物价格，单位为元，精确到小数点后两位（如果小数点后位数多于两位，则四舍五入保留两位小数），范围为(0-5000] | - |
| goods\_height | number | 否 | 货物高度，单位为cm，精确到小数点后两位（如果小数点后位数多于两位，则四舍五入保留两位小数），范围为(0-45] | - |
| goods\_width | number | 否 | 货物宽度，单位为cm，精确到小数点后两位（如果小数点后位数多于两位，则四舍五入保留两位小数），范围为(0-50] | - |
| goods\_length | number | 否 | 货物长度，单位为cm，精确到小数点后两位（如果小数点后位数多于两位，则四舍五入保留两位小数），范围为(0-65] | - |
| goods\_weight | number | 是 | 货物重量，单位为kg，精确到小数点后两位（如果小数点后位数多于两位，则四舍五入保留两位小数），范围为(0-50] | - |
| goods\_detail | [object](#Body__cargo__goods_detail) | 否 | 货物详情，最长不超过10240个字符 | - |
| goods\_pickup\_info | string | 否 | 货物取货信息，用于骑手到店取货，最长不超过100个字符 | - |
| cargo\_first\_class | string | 是 | 品类一级类目 | [枚举值](#Enum_Body__cargo__cargo_first_class) |
| cargo\_second\_class | string | 是 | 品类二级类目 | - |

**Body.order_info Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delivery\_service\_code | string | 否 | 配送服务代码 不同配送公司自定义, 顺丰和达达不填 |
| expected\_delivery\_time | number | 否 | 期望派单时间(达达支持，表示达达系统调度时间, 到那个时间才会有状态更新的回调通知)，unix-timestamp, 比如1586342180 |
| order\_type | number | 否 | 订单类型, 0: 即时单 1 预约单，如预约单，需要设置expected\_delivery\_time或expected\_finish\_time或expected\_pick\_time |
| poi\_seq | string | 否 | 门店订单流水号，建议提供，方便骑手门店取货，最长不超过32个字符 |
| note | string | 否 | 备注，最长不超过200个字符 |
| order\_time | number | 否 | 用户下单付款时间, 顺丰必填, 比如1555220757 |
| is\_insured | number | 否 | 是否保价，0，非保价，1.保价 |
| declared\_value | number | 否 | 保价金额，单位为元，精确到分 |
| tips | number | 否 | 小费，单位为元, 下单一般不加小费 |
| is\_direct\_delivery | number | 否 | 是否选择直拿直送（0：不需要；1：需要。选择直拿直送后，同一时间骑手只能配送此订单至完成，配送费用也相应高一些，闪送必须选1，达达可选0或1，其余配送公司不支持直拿直送） |
| cash\_on\_delivery | number | 否 | 骑手应付金额，单位为元，精确到分 |
| cash\_on\_pickup | number | 否 | 骑手应收金额，单位为元，精确到分 |
| rider\_pick\_method | number | 否 | 物流流向，1：从门店取件送至用户；2：从用户取件送至门店 |
| is\_finish\_code\_needed | number | 否 | 收货码（0：不需要；1：需要。收货码的作用是：骑手必须输入收货码才能完成订单妥投） |
| is\_pickup\_code\_needed | number | 否 | 取货码（0：不需要；1：需要。取货码的作用是：骑手必须输入取货码才能从商家取货） |
| expected\_finish\_time | number | 否 | 期望送达时间(美团、顺丰同城急送支持），unix-timestamp, 比如1586342180 |
| expected\_pick\_time | number | 否 | 期望取件时间（闪送、顺丰同城急送支持，闪送需要设置两个小时后的时间，顺丰同城急送只需传expected\_finish\_time或expected\_pick\_time其中之一即可，同时都传则以expected\_finish\_time为准），unix-timestamp, 比如1586342180 |

**Body.shop Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wxa\_path | string | 否 | 商家小程序的路径，建议为订单页面 |
| img\_url | string | 否 | 商品缩略图 url；shop.detail\_list为空则必传，shop.detail\_list非空可不传。 |
| goods\_name | string | 否 | 商品名称, 不超过128字节；shop.detail\_list为空则必传，shop.detail\_list非空可不传。 |
| goods\_count | number | 否 | 商品数量；shop.detail\_list为空则必传。shop.detail\_list非空可不传，默认取shop.detail\_list的size |
| wxa\_appid | string | 否 | 该参数在【即时配送】的[addLocalOrder](api_addlocalorder)接口才生效。若结算方式为：第三方向配送公司统一结算，商户后续和第三方结算，则该参数必填；在该结算模式下，第三方用自己的开发小程序替授权商户发起下单，并将授权小程序的appid给平台，后续配送通知中可回流授权商户小程序。 |

**Body.cargo.goods_detail Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| goods | [objarray](#Body__cargo__goods_detail__goods<Array>) | 是 | 货物列表 |

**Body.cargo.goods_detail.goods(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| good\_count | number | 是 | 货物数量 |
| good\_name | string | 是 | 货品名称 |
| good\_price | number | 否 | 货品单价，精确到小数点后两位（如果小数点后位数多于两位，则四舍五入保留两位小数） |
| good\_unit | string | 否 | 货品单位，最长不超过20个字符 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| resultcode | number | 运力返回的错误码 | - |
| resultmsg | string | 运力返回的错误描述 | - |
| fee | number | 实际运费(单位：元)，运费减去优惠券费用 | - |
| deliverfee | number | 运费(单位：元) | - |
| couponfee | number | 优惠券费用(单位：元) | - |
| tips | number | 小费(单位：元) | - |
| insurancfee | number | 保价费(单位：元) | - |
| distance | number | 配送距离(整数单位：米) | - |
| waybill\_id | string | 配送单号 | - |
| order\_status | number | 配送状态 | [枚举值](#Enum_Res__order_status) |
| finish\_code | number | 收货码 | - |
| pickup\_code | number | 取货码 | - |
| dispatch\_duration | number | 预计骑手接单时间，单位秒，比如5分钟，就填300, 无法预计填0 | - |

**Body.cargo.cargo_first_class Enum**

| 枚举值 | 描述 |
| --- | --- |
| 美食夜宵 | 零食小吃 香锅/烤鱼 西餐 日韩料理 海鲜/烧烤 快餐/地方菜 小龙虾 披萨 |
| 甜品饮料 | 甜品 奶茶果汁 咖啡 面包/糕点 冰淇淋 |
| 蛋糕 | 蛋糕 |
| 日用百货 | 便利店 水站/奶站 零食/干果 五金日用 粮油调味 文具店 酒水行 地方特产 进口食品 宠物用品 超市 书店 宠物食品用品 办公家居用品 |
| 果蔬生鲜 | 果蔬 海鲜水产 冷冻速食 |
| 鲜花 | 鲜花 |
| 医药健康 | 送药 器材器具 |
| 美妆护肤 | 日化美妆 |
| 母婴 | 孕婴用品 |
| 文件或票务 | 保单 票务文件 政府文件 证件 |
| 服饰鞋帽 | 服饰鞋帽综合 |
| 洗涤 | 脏衣服收 干净衣服派 |
| 珠宝奢侈品 | 珠宝饰品 奢侈品 |
| 家居家装 | 家具 装修建材 厨房卫浴 |
| 数码产品 | 数码产品 |
| 配件器材 | 配件器材 |
| 电商 | 电视购物 线上商城 |
| 现场勘查 | 现场勘查 |
| 快递业务 | 快递配送 |
| 其他 | 其他 |

**Res.order_status Enum**

| 枚举值 | 描述 |
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

**5. 注意事项**

| 服务通知 | 对应的order\_status值 |
| --- | --- |
| 骑手已接单 | 102 |
| 骑手已取货，配送中 | 202或301 |
| 配送已完成 | 302 |
| 配送异常 | 203、204、205、303、304、305、501、502 |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

---

### 模拟更新配送单状态

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-business/api_realmockupdateorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shopid | string | 是 | 商家id |
| shop\_order\_id | string | 是 | 唯一标识订单的 ID，由商户生成 |
| order\_status | number | 是 | 配送状态，详见[order\_status 枚举值](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/industry/immediate-delivery/order_status.html) |
| action\_time | number | 是 | 状态变更时间点，Unix秒级时间戳 |
| action\_msg | string | 否 | 附加信息 |
| delivery\_sign | string | 是 | 用配送公司提供的appSecret加密的校验串说明 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| resultcode | number | 运力返回的错误码 |
| resultmsg | string | 运力返回的错误描述 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

---

### 模拟配送公司更新配送单状态

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-business/api_mockupdateorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| shopid | string | 是 | 商家id, 必须是 "test\_shop\_id" | - |
| shop\_order\_id | string | 是 | 唯一标识订单的 ID，由商户生成 | - |
| order\_status | number | 是 | 配送状态 | [枚举值](#Enum_Body__order_status) |
| action\_time | number | 是 | 状态变更时间点，Unix秒级时间戳 | - |
| action\_msg | string | 否 | 附加信息 | - |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| resultcode | number | 运力返回的错误码 |
| resultmsg | string | 运力返回的错误描述 |

**Body.order_status Enum**

| 枚举值 | 描述 |
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

**5. 注意事项**

| 服务通知 | 对应的order\_status值 |
| --- | --- |
| 骑手已接单 | 102 |
| 骑手已取货，配送中 | 202或301 |
| 配送已完成 | 302 |
| 配送异常 | 203、204、205、303、304、305、501、502 |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 拉取配送单信息

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-business/api_getlocalorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shopid | string | 是 | 商家id， 由配送公司分配的appkey |
| shop\_order\_id | string | 是 | 唯一标识订单的 ID，由商户生成 |
| shop\_no | string | 是 | 商家门店编号， 在配送公司登记，如果只有一个门店，可以不填 |
| delivery\_sign | string | 是 | 用配送公司提供的appSecret加密的校验串，见注意事项 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| resultcode | number | 运力返回的错误码 | - |
| resultmsg | string | 运力返回的错误描述 | - |
| order\_status | number | 配送状态 | [枚举值](#Enum_Res__order_status) |
| waybill\_id | string | 配送单号 | - |
| rider\_name | string | 骑手姓名 | - |
| rider\_phone | string | 骑手电话 | - |
| rider\_lng | number | 骑手位置经度, 配送中时返回 | - |
| rider\_lat | number | 骑手位置纬度, 配送中时返回 | - |
| reach\_time | number | 预计还剩多久送达时间, 配送中时返回，单位秒， 已取货配送中需返回，比如5分钟后送达，填300 | - |

**Res.order_status Enum**

| 枚举值 | 描述 |
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

**5. 注意事项**

| 服务通知 | 对应的order\_status值 |
| --- | --- |
| 骑手已接单 | 102 |
| 骑手已取货，配送中 | 202或301 |
| 配送已完成 | 302 |
| 配送异常 | 203、204、205、303、304、305、501、502 |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 930555 | 微信平台系统错误 |  |
| 930556 | 配送公司超时 |  |
| 930557 | 配送公司系统错误 |  |
| 930558 | 配送公司逻辑错误 |  |
| 930559 | openid无效 |  |
| 930560 | 未绑定的商户号 |  |
| 930561 | 参数错误 |  |
| 930562 | 配送单已经存在 |  |
| 930563 | 配送单不存在 |  |
| 930564 | 调用无配额 |  |
| 930565 | 配送单已结束 |  |
| 9300535 | shop字段商品缩略图 url、商品名称为空或者非法，或者商品数量为0 |  |

---

### 异常件退回商家确认

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-business/api_abnormalconfirm.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shopid | string | 是 | 商家id，由配送公司分配的appkey |
| shop\_order\_id | string | 是 | 唯一标识订单的 ID，由商户生成 |
| waybill\_id | string | 是 | 配送单id |
| delivery\_sign | string | 是 | 用配送公司提供的appSecret加密的校验串，见注意事项 |
| shop\_no | string | 是 | 商家门店编号，在配送公司登记，闪送必填，值为店铺id |
| remark | string | 否 | 备注 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| resultcode | number | 运力返回的错误码 |
| resultmsg | string | 运力返回的错误描述 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 930555 | 微信平台系统错误 |  |
| 930556 | 配送公司超时 |  |
| 930557 | 配送公司系统错误 |  |
| 930558 | 配送公司逻辑错误 |  |
| 930559 | openid无效 |  |
| 930560 | 未绑定的商户号 |  |
| 930561 | 参数错误 |  |
| 930562 | 配送单已经存在 |  |
| 930563 | 配送单不存在 |  |
| 930564 | 调用无配额 |  |
| 930565 | 配送单已结束 |  |
| 9300535 | shop字段商品缩略图 url、商品名称为空或者非法，或者商品数量为0 |  |

---

### 取消配送单

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-business/api_cancellocalorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shopid | string | 是 | 商家id， 由配送公司分配的appkey |
| shop\_order\_id | string | 是 | 唯一标识订单的 ID，由商户生成 |
| delivery\_id | string | 是 | 快递公司ID |
| waybill\_id | string | 否 | 配送单id（顺丰同城必填） |
| cancel\_reason\_id | number | 是 | 取消原因Id。1表示暂时不需要邮寄；2表示价格不合适；3表示订单信息有误，重新下单；4表示骑手取货不及时；5表示骑手配送不及时；6表示其他原因( 如果选择6，需要填写取消原因，否则不需要填写 ) |
| cancel\_reason | string | 是 | 取消原因 |
| shop\_no | string | 是 | 商家门店编号，如果只有一个门店，闪送shop\_no必填，值为店铺id |
| delivery\_sign | string | 是 | 用配送公司提供的appSecret加密的校验串，见注意事项 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| resultcode | number | 运力返回的错误码 |
| resultmsg | string | 运力返回的错误描述 |
| deduct\_fee | number | 扣除的违约金(单位：元)，精确到分 |
| desc | string | 说明 |

**cancel_reason_id 取消原因Id的合法值**

| 值 | 说明 |
| --- | --- |
| 1 | 暂时不需要邮寄 |
| 2 | 价格不合适 |
| 3 | 订单信息有误，重新下单 |
| 4 | 骑手取货不及时 |
| 5 | 骑手配送不及时 |
| 6 | 其他原因( 如果选择6，需要填写取消原因，否则不需要填写 ) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 930555 | 微信平台系统错误 |  |
| 930556 | 配送公司超时 |  |
| 930557 | 配送公司系统错误 |  |
| 930558 | 配送公司逻辑错误 |  |
| 930559 | openid无效 |  |
| 930560 | 未绑定的商户号 |  |
| 930561 | 参数错误 |  |
| 930562 | 配送单已经存在 |  |
| 930563 | 配送单不存在 |  |
| 930564 | 调用无配额 |  |
| 930565 | 配送单已结束 |  |
| 9300535 | shop字段商品缩略图 url、商品名称为空或者非法，或者商品数量为0 |  |

---

### 添加小费

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-business/api_addtips.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shopid | string | 是 | 商家id， 由配送公司分配的appkey |
| shop\_order\_id | string | 是 | 唯一标识订单的 ID，由商户生成 |
| waybill\_id | string | 是 | 配送单id |
| tips | number | 是 | 小费金额(单位：元) 各家配送公司最大值不同 |
| remark | string | 是 | 备注 |
| delivery\_sign | string | 是 | 用配送公司提供的appSecret加密的校验串说明 |
| shop\_no | string | 是 | 商家门店编号，在配送公司登记，如果只有一个门店，闪送shop\_no必填，值为店铺id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| resultcode | number | 运力返回的错误码 |
| resultmsg | string | 运力返回的错误描述 |

**4. 注意事项**

| 配送公司 | 加小费规则 |
| --- | --- |
| 顺丰同城急送 | 支持加小费，小费规则：骑手接单前可加小费，上限10次，200元封顶 |
| 闪送 | 支持加小费，小费规则：骑手接单前可加小费，需按固定档位加小费，档位为2、3、5、10、15、20、50、100 |
| 美团配送 | 不支持加小费 |
| 达达配送 | 支持加小费，小费规则：骑手接单前可加小费，小费金额以最新一次为准，同一单新增的小费额须大于上一次的小费额，小费不可以超过货值，上限30元 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

---

### 添加配送单

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-business/api_addlocalorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shopid | string | 是 | 商家id，由配送公司分配的appkey |
| shop\_order\_id | string | 是 | 唯一标识订单的 ID，由商户生成, 不超过128字节 |
| delivery\_id | string | 是 | 配送公司ID |
| openid | string | 是 | 下单用户的openid |
| sender | [object](#Body__sender) | 是 | 发件人信息，顺丰同城急送必须填写，美团配送、达达、闪送，若传了shop\_no的值可不填该字段 |
| receiver | [object](#Body__receiver) | 是 | 收件人信息 |
| cargo | [object](#Body__cargo) | 是 | 货物信息 |
| order\_info | [object](#Body__order_info) | 是 | 订单信息 |
| shop | [object](#Body__shop) | 是 | 商品信息，会展示到物流通知消息中 |
| delivery\_token | string | 是 | 预下单接口返回的参数，配送公司可保证在一段时间内运费不变 |
| delivery\_sign | string | 是 | 用配送公司提供的appSecret加密的校验串，见注意事项 |
| shop\_no | string | 是 | 商家门店编号，在配送公司登记，如果只有一个门店，美团闪送必填, 值为店铺id |
| sub\_biz\_id | string | 否 | 子商户id，区分小程序内部多个子商户 |

**Body.sender Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 姓名，最长不超过256个字符 |
| city | string | 是 | 城市名称，如广州市 |
| address | string | 是 | 地址(街道、小区、大厦等，用于定位) |
| address\_detail | string | 是 | 地址详情(楼号、单元号、层号) |
| phone | string | 是 | 电话/手机号，最长不超过64个字符 |
| lng | number | 是 | 经度（火星坐标或百度坐标，和 coordinate\_type 字段配合使用，确到小数点后6位 |
| lat | number | 是 | 纬度（火星坐标或百度坐标，和 coordinate\_type 字段配合使用，精确到小数点后6位） |
| coordinate\_type | number | 否 | 坐标类型，0：火星坐标（高德，腾讯地图均采用火星坐标） 1：百度坐标 |

**Body.receiver Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 姓名，最长不超过256个字符 |
| city | string | 是 | 城市名称，如广州市 |
| address | string | 是 | 地址(街道、小区、大厦等，用于定位) |
| address\_detail | string | 是 | 地址详情(楼号、单元号、层号) |
| phone | string | 是 | 电话/手机号，最长不超过64个字符 |
| lng | number | 是 | 经度（火星坐标或百度坐标，和 coordinate\_type 字段配合使用，确到小数点后6位 |
| lat | number | 是 | 纬度（火星坐标或百度坐标，和 coordinate\_type 字段配合使用，精确到小数点后6位） |
| coordinate\_type | number | 否 | 坐标类型，0：火星坐标（高德，腾讯地图均采用火星坐标） 1：百度坐标 |

**Body.cargo Object Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| goods\_value | number | 是 | 货物价格，单位为元，精确到小数点后两位（如果小数点后位数多于两位，则四舍五入保留两位小数），范围为(0-5000] | - |
| goods\_height | number | 否 | 货物高度，单位为cm，精确到小数点后两位（如果小数点后位数多于两位，则四舍五入保留两位小数），范围为(0-45] | - |
| goods\_width | number | 否 | 货物宽度，单位为cm，精确到小数点后两位（如果小数点后位数多于两位，则四舍五入保留两位小数），范围为(0-50] | - |
| goods\_length | number | 否 | 货物长度，单位为cm，精确到小数点后两位（如果小数点后位数多于两位，则四舍五入保留两位小数），范围为(0-65] | - |
| goods\_weight | number | 是 | 货物重量，单位为kg，精确到小数点后两位（如果小数点后位数多于两位，则四舍五入保留两位小数），范围为(0-50] | - |
| goods\_detail | [object](#Body__cargo__goods_detail) | 否 | 货物详情，最长不超过10240个字符 | - |
| goods\_pickup\_info | string | 否 | 货物取货信息，用于骑手到店取货，最长不超过100个字符 | - |
| cargo\_first\_class | string | 是 | 品类一级类目 | [枚举值](#Enum_Body__cargo__cargo_first_class) |
| cargo\_second\_class | string | 是 | 品类二级类目 | - |

**Body.order_info Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delivery\_service\_code | string | 否 | 配送服务代码 不同配送公司自定义, 顺丰和达达不填 |
| expected\_delivery\_time | number | 否 | 期望派单时间(达达支持，表示达达系统调度时间, 到那个时间才会有状态更新的回调通知)，unix-timestamp, 比如1586342180 |
| order\_type | number | 否 | 订单类型, 0: 即时单 1 预约单，如预约单，需要设置expected\_delivery\_time或expected\_finish\_time或expected\_pick\_time |
| poi\_seq | string | 否 | 门店订单流水号，建议提供，方便骑手门店取货，最长不超过32个字符 |
| note | string | 否 | 备注，最长不超过200个字符 |
| order\_time | number | 否 | 用户下单付款时间, 顺丰必填, 比如1555220757 |
| is\_insured | number | 否 | 是否保价，0，非保价，1.保价 |
| declared\_value | number | 否 | 保价金额，单位为元，精确到分 |
| tips | number | 否 | 小费，单位为元, 下单一般不加小费 |
| is\_direct\_delivery | number | 否 | 是否选择直拿直送（0：不需要；1：需要。选择直拿直送后，同一时间骑手只能配送此订单至完成，配送费用也相应高一些，闪送必须选1，达达可选0或1，其余配送公司不支持直拿直送） |
| cash\_on\_delivery | number | 否 | 骑手应付金额，单位为元，精确到分 |
| cash\_on\_pickup | number | 否 | 骑手应收金额，单位为元，精确到分 |
| rider\_pick\_method | number | 否 | 物流流向，1：从门店取件送至用户；2：从用户取件送至门店 |
| is\_finish\_code\_needed | number | 否 | 收货码（0：不需要；1：需要。收货码的作用是：骑手必须输入收货码才能完成订单妥投） |
| is\_pickup\_code\_needed | number | 否 | 取货码（0：不需要；1：需要。取货码的作用是：骑手必须输入取货码才能从商家取货） |
| expected\_finish\_time | number | 否 | 期望送达时间(美团、顺丰同城急送支持），unix-timestamp, 比如1586342180 |
| expected\_pick\_time | number | 否 | 期望取件时间（闪送、顺丰同城急送支持，闪送需要设置两个小时后的时间，顺丰同城急送只需传expected\_finish\_time或expected\_pick\_time其中之一即可，同时都传则以expected\_finish\_time为准），unix-timestamp, 比如1586342180 |

**Body.shop Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wxa\_path | string | 否 | 商家小程序的路径，建议为订单页面 |
| img\_url | string | 否 | 商品缩略图 url；shop.detail\_list为空则必传，shop.detail\_list非空可不传。 |
| goods\_name | string | 否 | 商品名称, 不超过128字节；shop.detail\_list为空则必传，shop.detail\_list非空可不传。 |
| goods\_count | number | 否 | 商品数量；shop.detail\_list为空则必传。shop.detail\_list非空可不传，默认取shop.detail\_list的size |
| wxa\_appid | string | 否 | 该参数在【即使配送】的addOrder接口才生效。若结算方式为：第三方向配送公司统一结算，商户后续和第三方结算，则该参数必填；在该结算模式下，第三方用自己的开发小程序替授权商户发起下单，并将授权小程序的appid给平台，后续配送通知中可回流授权商户小程序。 |

**Body.cargo.goods_detail Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| goods | [objarray](#Body__cargo__goods_detail__goods<Array>) | 是 | 货物列表 |

**Body.cargo.goods_detail.goods(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| good\_count | number | 是 | 货物数量 |
| good\_name | string | 是 | 货品名称 |
| good\_price | number | 否 | 货品单价，精确到小数点后两位（如果小数点后位数多于两位，则四舍五入保留两位小数） |
| good\_unit | string | 否 | 货品单位，最长不超过20个字符 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| resultcode | number | 运力返回的错误码 | - |
| resultmsg | string | 运力返回的错误描述 | - |
| fee | number | 实际运费(单位：元)，运费减去优惠券费用 | - |
| deliverfee | number | 运费(单位：元) | - |
| couponfee | number | 优惠券费用(单位：元) | - |
| tips | number | 小费(单位：元) | - |
| insurancfee | number | 保价费(单位：元) | - |
| distance | number | 配送距离(整数单位：米) | - |
| waybill\_id | string | 配送单号 | - |
| order\_status | number | 配送状态。 | [枚举值](#Enum_Res__order_status) |
| finish\_code | number | 收货码 | - |
| pickup\_code | number | 取货码 | - |
| dispatch\_duration | number | 预计骑手接单时间，单位秒，比如5分钟，就填300, 无法预计填0 | - |

**Body.cargo.cargo_first_class Enum**

| 枚举值 | 描述 |
| --- | --- |
| 美食夜宵 | 零食小吃 香锅/烤鱼 西餐 日韩料理 海鲜/烧烤 快餐/地方菜 小龙虾 披萨 |
| 甜品饮料 | 甜品 奶茶果汁 咖啡 面包/糕点 冰淇淋 |
| 蛋糕 | 蛋糕 |
| 日用百货 | 便利店 水站/奶站 零食/干果 五金日用 粮油调味 文具店 酒水行 地方特产 进口食品 宠物用品 超市 书店 宠物食品用品 办公家居用品 |
| 果蔬生鲜 | 果蔬 海鲜水产 冷冻速食 |
| 鲜花 | 鲜花 |
| 医药健康 | 送药 器材器具 |
| 美妆护肤 | 日化美妆 |
| 母婴 | 孕婴用品 |
| 文件或票务 | 保单 票务文件 政府文件 证件 |
| 服饰鞋帽 | 服饰鞋帽综合 |
| 洗涤 | 脏衣服收 干净衣服派 |
| 珠宝奢侈品 | 珠宝饰品 奢侈品 |
| 家居家装 | 家具 装修建材 厨房卫浴 |
| 数码产品 | 数码产品 |
| 配件器材 | 配件器材 |
| 电商 | 电视购物 线上商城 |
| 现场勘查 | 现场勘查 |
| 快递业务 | 快递配送 |
| 其他 | 其他 |

**Res.order_status Enum**

| 枚举值 | 描述 |
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

**5. 注意事项**

| 服务通知 | 对应的order\_status值 |
| --- | --- |
| 骑手已接单 | 102 |
| 骑手已取货，配送中 | 202或301 |
| 配送已完成 | 302 |
| 配送异常 | 203、204、205、303、304、305、501、502 |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 930555 | 微信平台系统错误 |  |
| 930556 | 配送公司超时 |  |
| 930557 | 配送公司系统错误 |  |
| 930558 | 配送公司逻辑错误 |  |
| 930559 | openid无效 |  |
| 930560 | 未绑定的商户号 |  |
| 930561 | 参数错误 |  |
| 930562 | 配送单已经存在 |  |
| 930563 | 配送单不存在 |  |
| 930564 | 调用无配额 |  |
| 930565 | 配送单已结束 |  |
| 9300535 | shop字段商品缩略图 url、商品名称为空或者非法，或者商品数量为0 |  |

---

### 更新配送单状态

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-provider/api_updateorder.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| wx\_token | string | 是 | [下单事件](../../../event_push/express/provider/Request_an_order_event)中推送的token字段 | - |
| order\_status | number | 是 | 订单状态 | [枚举值](#Enum_Body__order_status) |
| waybill\_id | string | 是 | 配送单id | - |
| action\_msg | string | 否 | 附加信息 | - |
| action\_time | number | 是 | 状态变更时间点，Unix秒级时间戳 | - |
| agent | [object](#Body__agent) | 否 | 骑手信息, 骑手接单时需返回 | - |
| shopid | string | 是 | 商家id， 由配送公司分配，可以是dev\_id或者appkey | - |
| shop\_order\_id | string | 是 | 唯一标识订单的 ID，由商户生成 | - |
| shop\_no | string | 否 | 商家门店编号， 在配送公司侧登记 | - |
| wxa\_path | string | 是 | 配送公司小程序跳转路径，用于用户收到消息会间接跳转到这个页面 | - |
| expected\_delivery\_time | number | 否 | 预计送达时间戳， 骑手接单时需返回 | - |

**Body.agent Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 骑手姓名 |
| phone | string | 是 | 骑手电话 |
| is\_phone\_encrypted | number | 否 | 电话是否加密。默认是0不加密，1表示加密。 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| resultcode | number | [错误码](#apierrcode) |
| resultmsg | string | [错误描述](#apierrcode) |

**Body.order_status Enum**

| 枚举值 | 描述 |
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

**5. 注意事项**

| 服务通知 | 对应的order\_status值 |
| --- | --- |
| 骑手已接单 | 102 |
| 骑手已取货，配送中 | 202或301 |
| 配送已完成 | 302 |
| 配送异常 | 203、204、205、303、304、305、501、502 |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

---

<!-- pages: 15 -->
