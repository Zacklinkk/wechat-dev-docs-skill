# 微信小程序 API 结构化参考 — payment

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.requestVirtualPayment(Object object)

基础库 2.19.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestVirtualPayment.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | signData | Object |  | 是 | 具体支付参数见signData, 该参数需以string形式传递, 例如signData: '{"offerId":"123","buyQuantity":1,"env":0,"currencyType":"CNY","productId":"testproductId","goodsPrice":10,"outTradeNo":"xxxxxx","attach":"testdata"}' |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | offerId | string |  | 是 | mp-支付基础配置中的offerid | |  | buyQuantity | number |  | 是 | 购买数量 | |  | env | number |  | 否 | 环境配置, 0 正式环境, 1 沙箱环境, 默认为 0 | |  | currencyType | string |  | 是 | 币种 | |  | | 合法值 | 说明 | | --- | --- | | CNY | 人民币 | | | | | | |  | productId | string |  | 否 | 道具ID, \*\*该字段仅mode=short\_series\_goods时需要必填\*\* | |  | goodsPrice | number |  | 否 | 道具单价(分), \*\*该字段仅mode=short\_series\_goods时需要必填\*\*, 用来校验价格与后台道具价格是否一致, 避免用户在业务商城页看到的价格与实际价格不一致导致投诉 | |  | activitySellingPrice | number |  | 否 | 道具优惠价格（分），\*\*非必填，该字段需与goodsPrice一起传入\*\*。如用户使用优惠券、积分等，需要以低于道具价格下单时可传入，传入后该价格即为实际下单价格。 | |  | outTradeNo | string |  | 是 | 业务订单号, 每个订单号只能使用一次, 重复使用会失败(极端情况不保证唯一, 不建议业务强依赖唯一性). 要求8-32个字符内, 只能是数字、大小写字母、符号 \_-|\*@组成, 不能以下划线(\_)开头 | |  | attach | string |  | 是 | 透传数据, 发货通知时会透传给开发者 | | | | | |
|  | mode | string |  | 是 | 支付的类型, 不同的支付类型有各自额外要传的附加参数 |
|  | | 合法值 | 说明 | | --- | --- | | short\_series\_goods | 道具直购 | | short\_series\_coin | 代币充值 | | | | | |
|  | paySig | string |  | 是 | 支付签名, 详见[《签名详解》](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/industry/virtual-payment.html) |
|  | signature | string |  | 是 | 用户态签名, 详见[《签名详解》](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/industry/virtual-payment.html) |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | offerId | string |  | 是 | mp-支付基础配置中的offerid |
|  | buyQuantity | number |  | 是 | 购买数量 |
|  | env | number |  | 否 | 环境配置, 0 正式环境, 1 沙箱环境, 默认为 0 |
|  | currencyType | string |  | 是 | 币种 |
|  | | 合法值 | 说明 | | --- | --- | | CNY | 人民币 | | | | | |
|  | productId | string |  | 否 | 道具ID, \*\*该字段仅mode=short\_series\_goods时需要必填\*\* |
|  | goodsPrice | number |  | 否 | 道具单价(分), \*\*该字段仅mode=short\_series\_goods时需要必填\*\*, 用来校验价格与后台道具价格是否一致, 避免用户在业务商城页看到的价格与实际价格不一致导致投诉 |
|  | activitySellingPrice | number |  | 否 | 道具优惠价格（分），\*\*非必填，该字段需与goodsPrice一起传入\*\*。如用户使用优惠券、积分等，需要以低于道具价格下单时可传入，传入后该价格即为实际下单价格。 |
|  | outTradeNo | string |  | 是 | 业务订单号, 每个订单号只能使用一次, 重复使用会失败(极端情况不保证唯一, 不建议业务强依赖唯一性). 要求8-32个字符内, 只能是数字、大小写字母、符号 \_-|\*@组成, 不能以下划线(\_)开头 |
|  | attach | string |  | 是 | 透传数据, 发货通知时会透传给开发者 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| CNY | 人民币 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| short\_series\_goods | 道具直购 |
| short\_series\_coin | 代币充值 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 调用成功信息 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |
| errCode | number | 错误码 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1001 |  | 参数错误 |
| -1 |  | 支付失败 |
| -2 |  | 支付取消 |
| -4 |  | 风控拦截 |
| -5 |  | 开通签约结果未知 |
| -15001 |  | 参数错误,具体原因见err\_msg |
| -15002 |  | outTradeNo重复使用,请换新单号重试 |
| -15003 |  | 系统错误 |
| -15004 |  | currencyType错误,目前只能填CNY |
| -15005 |  | 用户态签名signature错误 |
| -15006 |  | 支付签名paySig错误 |
| -15007 |  | session\_key过期 |
| -15008 |  | 二级商户进件未完成 |
| -15009 |  | 代币未发布 |
| -15010 |  | 道具productId未发布 |
| -15011 |  | 现网版本的env只能是0,不能填1(沙盒环境) |
| -15012 |  | 调用米大师失败导致关单,请换新单号重试 |
| -15013 |  | goodsPrice道具价格错误 |
| -15014 |  | 道具/代币发布未生效，禁止下单，大概10分钟后生效 |
| -15016 |  | signData格式有问题 |
| -15017 |  | 此商家涉嫌违规，收款功能已被限制，暂无法支付。商家可以登录微信商户平台/微信支付商家助手小程序查看原因和解决方案 |
| -15018 |  | 代币或者道具productId审核不通过 |
| -15019 |  | 调微信报商户受限,商家可以登录微信商户平台/微信支付商家助手小程序查看原因和解决方案 |
| -15020 |  | 操作过快，请稍候再试 |
| -15021 |  | 小程序被限频交易 |

---

### wx.requestPluginPayment(Object object)

基础库 2.22.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestPluginPayment.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | version | string |  | 是 | 插件版本 |
|  | | 合法值 | 说明 | | --- | --- | | develop | 开发版 | | trial | 体验版 | | release | 正式版 | | | | | |
|  | fee | number |  | 是 | 需要显示在页面中的金额，单位为分 |
|  | paymentArgs | Object |  | 是 | 任意数据，传递给功能页中的响应函数 |
|  | currencyType | string | CNY | 否 | 需要显示在页面中的货币符号的代码 |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| develop | 开发版 |
| trial | 体验版 |
| release | 正式版 |

---

### wx.requestPayment(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestPayment.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | timeStamp | string |  | 是 | 时间戳，从 1970 年 1 月 1 日 00:00:00 至今的秒数，即当前的时间 |
|  | nonceStr | string |  | 是 | 随机字符串，长度为32个字符以下 |
|  | package | string |  | 是 | 统一下单接口返回的 prepay\_id 参数值，提交格式如：prepay\_id=\*\*\* |
|  | signType | string | MD5 | 否 | 签名算法，应与后台下单时的值一致 |
|  | | 合法值 | 说明 | | --- | --- | | MD5 | 仅在 v2 版本接口适用 | | HMAC-SHA256 | 仅在 v2 版本接口适用 | | RSA | 仅在 v3 版本接口适用 | | | | | |
|  | paySign | string |  | 是 | 签名，具体见微信支付文档 |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| MD5 | 仅在 v2 版本接口适用 |
| HMAC-SHA256 | 仅在 v2 版本接口适用 |
| RSA | 仅在 v3 版本接口适用 |

---

### wx.requestMerchantTransfer(Object object)

基础库 3.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestMerchantTransfer.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| mchId | string |  | 是 | 商户号 |
| subMchId | string |  | 否 | 子商户号，服务商模式下必填 |
| appId | string |  | 否 | 商户 appId，普通模式下必填，服务商模式下，appId 和 subAppId 二选一填写 |
| subAppId | string |  | 否 | 子商户 appId，服务商模式下，appId 和 subAppId 二选一填写 |
| package | string |  | 是 | 商家转账付款单跳转收款页 pkg 信息,商家转账付款单受理成功时返回给商户 |
| openId | string |  | 否 | 收款用户 openId， 对应传入的商户 appId 下，某用户的 openId |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.requestCommonPayment(Object object)

基础库 2.19.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestCommonPayment.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | mode | string |  | 是 | 支付的类型 |
|  | | 合法值 | 说明 | | --- | --- | | retail\_pay\_goods | B2b支付 | | retail\_pay\_indirect\_goods | 间接支付 | | retail\_pay\_combined\_goods | 合单支付 | | retail\_pay\_goods\_new | 多渠道B2b支付 | | | | | |
|  | signData | Object |  | 是 | 具体支付参数见signData, 该参数需以string形式传递, 例如signData: '{"mchid":"1234567890","out\_trade\_no":"test1244","description":"测试测试","amount":{"order\_amount":1,"currency":"CNY"},"attach":"test\_attach","env":1}' |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | mchid | string |  | 是 | 由微信支付生成并下发的商户号。示例值：1230000109 | |  | out\_trade\_no | string |  | 是 | 商户系统内部订单号，只能是数字、大小写字母\_-\*且在同一个商户号下唯一，长度限制为[6,32]。示例值：1217752501201407033233368018 | |  | description | string |  | 是 | 商品描述。示例值：Image形象店-深圳腾大-QQ公仔 | |  | amount | Object |  | 是 | 订单金额信息。 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | product\_amount | number |  | 否 | 订单所有商品的原价总和，单位为分。示例值：1000 | |  | freight | number |  | 否 | 订单运费，单位为分。示例值：200 | |  | discount | number |  | 否 | 订单总计优惠金额，单位为分。示例值：500 | |  | other\_fee | number |  | 否 | 订单其他费用总金额，单位为分。示例值：600 | |  | order\_amount | number |  | 是 | 订单总需支付金额，也即是真正下单总金额，单位为分。示例值：1300 | |  | currency | string |  | 否 | 货币类型。示例值：CNY | |  | | 合法值 | 说明 | | --- | --- | | CNY | 人民币 | | | | | | | | | | | |  | attach | string |  | 否 | 附加数据，在查询API和支付通知中原样返回，可作为自定义参数使用，实际情况下只有支付完成状态才会返回该字段。示例值：test\_attach | |  | product\_info | Object |  | 否 | 订单详细商品信息列表。 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | spu\_id | string |  | 是 | 商户系统内该商品的spuid。示例值：spu123456 | |  | sku\_id | string |  | 是 | 商户系统内该商品的skuid。示例值：sku123 | |  | title | string |  | 是 | 商品标题。示例值：QQ长鹅 | |  | path | string |  | 是 | 商户商品详请页小程序路径。示例值：pages/index | |  | head\_img | string |  | 是 | 商品主图的url，大小建议64\*64。示例值：https://mp.weixin.qq.com/123 | |  | category | string |  | 是 | 商户侧该商品所属的类目。示例值：玩偶 | |  | sku\_attr | string |  | 是 | 商户系统内该商品的sku属性。示例值：50cm | |  | org\_price | number |  | 是 | 该商品原价，单位为分。示例值：5000 | |  | sale\_price | number |  | 是 | 该商品售价，单位为分。示例值：4000 | |  | quantity | number |  | 是 | 用户购买该商品的数量。示例值：5 | | | | | | |  | delivery\_type | number |  | 否 | 配送方式。示例值：2 | |  | | 合法值 | 说明 | | --- | --- | | 1 | 同城配送 | | 2 | 快递配送 | | 3 | 门店自提 | | 4 | 无需配送与提货 | | | | | | |  | env | number |  | 是 | 下单环境。示例值：0 | |  | | 合法值 | 说明 | | --- | --- | | 0 | 生产环境/现网环境 | | 1 | 沙箱环境/测试环境 | | | | | | |  | requestPaymentInfo | Object |  | 否 | B2b间连支付场景下，调用requestPaymentInfo的参数 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | timeStamp | string |  | 否 | 时间戳，从 1970 年 1 月 1 日 00:00:00 至今的秒数，即当前的时间 | |  | nonceStr | string |  | 否 | 随机字符串，长度为32个字符以下 | |  | package | string |  | 否 | 统一下单接口返回的 prepay\_id 参数值，提交格式如：prepay\_id=\*\*\* | |  | signType | string |  | 否 | 签名算法，应与后台下单时的值一致 | |  | paySign | string |  | 否 | 签名，具体见微信支付文档 | | | | | | | | | | |
|  | paySig | string |  | 是 | 支付签名, 详见[《签名详解》](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/industry/virtual-payment.html) |
|  | signature | string |  | 是 | 用户态签名, 详见[《签名详解》](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/industry/virtual-payment.html) |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| retail\_pay\_goods | B2b支付 |
| retail\_pay\_indirect\_goods | 间接支付 |
| retail\_pay\_combined\_goods | 合单支付 |
| retail\_pay\_goods\_new | 多渠道B2b支付 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | mchid | string |  | 是 | 由微信支付生成并下发的商户号。示例值：1230000109 |
|  | out\_trade\_no | string |  | 是 | 商户系统内部订单号，只能是数字、大小写字母\_-\*且在同一个商户号下唯一，长度限制为[6,32]。示例值：1217752501201407033233368018 |
|  | description | string |  | 是 | 商品描述。示例值：Image形象店-深圳腾大-QQ公仔 |
|  | amount | Object |  | 是 | 订单金额信息。 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | product\_amount | number |  | 否 | 订单所有商品的原价总和，单位为分。示例值：1000 | |  | freight | number |  | 否 | 订单运费，单位为分。示例值：200 | |  | discount | number |  | 否 | 订单总计优惠金额，单位为分。示例值：500 | |  | other\_fee | number |  | 否 | 订单其他费用总金额，单位为分。示例值：600 | |  | order\_amount | number |  | 是 | 订单总需支付金额，也即是真正下单总金额，单位为分。示例值：1300 | |  | currency | string |  | 否 | 货币类型。示例值：CNY | |  | | 合法值 | 说明 | | --- | --- | | CNY | 人民币 | | | | | | | | | | |
|  | attach | string |  | 否 | 附加数据，在查询API和支付通知中原样返回，可作为自定义参数使用，实际情况下只有支付完成状态才会返回该字段。示例值：test\_attach |
|  | product\_info | Object |  | 否 | 订单详细商品信息列表。 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | spu\_id | string |  | 是 | 商户系统内该商品的spuid。示例值：spu123456 | |  | sku\_id | string |  | 是 | 商户系统内该商品的skuid。示例值：sku123 | |  | title | string |  | 是 | 商品标题。示例值：QQ长鹅 | |  | path | string |  | 是 | 商户商品详请页小程序路径。示例值：pages/index | |  | head\_img | string |  | 是 | 商品主图的url，大小建议64\*64。示例值：https://mp.weixin.qq.com/123 | |  | category | string |  | 是 | 商户侧该商品所属的类目。示例值：玩偶 | |  | sku\_attr | string |  | 是 | 商户系统内该商品的sku属性。示例值：50cm | |  | org\_price | number |  | 是 | 该商品原价，单位为分。示例值：5000 | |  | sale\_price | number |  | 是 | 该商品售价，单位为分。示例值：4000 | |  | quantity | number |  | 是 | 用户购买该商品的数量。示例值：5 | | | | | |
|  | delivery\_type | number |  | 否 | 配送方式。示例值：2 |
|  | | 合法值 | 说明 | | --- | --- | | 1 | 同城配送 | | 2 | 快递配送 | | 3 | 门店自提 | | 4 | 无需配送与提货 | | | | | |
|  | env | number |  | 是 | 下单环境。示例值：0 |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 生产环境/现网环境 | | 1 | 沙箱环境/测试环境 | | | | | |
|  | requestPaymentInfo | Object |  | 否 | B2b间连支付场景下，调用requestPaymentInfo的参数 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | timeStamp | string |  | 否 | 时间戳，从 1970 年 1 月 1 日 00:00:00 至今的秒数，即当前的时间 | |  | nonceStr | string |  | 否 | 随机字符串，长度为32个字符以下 | |  | package | string |  | 否 | 统一下单接口返回的 prepay\_id 参数值，提交格式如：prepay\_id=\*\*\* | |  | signType | string |  | 否 | 签名算法，应与后台下单时的值一致 | |  | paySign | string |  | 否 | 签名，具体见微信支付文档 | | | | | |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | product\_amount | number |  | 否 | 订单所有商品的原价总和，单位为分。示例值：1000 |
|  | freight | number |  | 否 | 订单运费，单位为分。示例值：200 |
|  | discount | number |  | 否 | 订单总计优惠金额，单位为分。示例值：500 |
|  | other\_fee | number |  | 否 | 订单其他费用总金额，单位为分。示例值：600 |
|  | order\_amount | number |  | 是 | 订单总需支付金额，也即是真正下单总金额，单位为分。示例值：1300 |
|  | currency | string |  | 否 | 货币类型。示例值：CNY |
|  | | 合法值 | 说明 | | --- | --- | | CNY | 人民币 | | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| CNY | 人民币 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | spu\_id | string |  | 是 | 商户系统内该商品的spuid。示例值：spu123456 |
|  | sku\_id | string |  | 是 | 商户系统内该商品的skuid。示例值：sku123 |
|  | title | string |  | 是 | 商品标题。示例值：QQ长鹅 |
|  | path | string |  | 是 | 商户商品详请页小程序路径。示例值：pages/index |
|  | head\_img | string |  | 是 | 商品主图的url，大小建议64\*64。示例值：https://mp.weixin.qq.com/123 |
|  | category | string |  | 是 | 商户侧该商品所属的类目。示例值：玩偶 |
|  | sku\_attr | string |  | 是 | 商户系统内该商品的sku属性。示例值：50cm |
|  | org\_price | number |  | 是 | 该商品原价，单位为分。示例值：5000 |
|  | sale\_price | number |  | 是 | 该商品售价，单位为分。示例值：4000 |
|  | quantity | number |  | 是 | 用户购买该商品的数量。示例值：5 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 1 | 同城配送 |
| 2 | 快递配送 |
| 3 | 门店自提 |
| 4 | 无需配送与提货 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 0 | 生产环境/现网环境 |
| 1 | 沙箱环境/测试环境 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | timeStamp | string |  | 否 | 时间戳，从 1970 年 1 月 1 日 00:00:00 至今的秒数，即当前的时间 |
|  | nonceStr | string |  | 否 | 随机字符串，长度为32个字符以下 |
|  | package | string |  | 否 | 统一下单接口返回的 prepay\_id 参数值，提交格式如：prepay\_id=\*\*\* |
|  | signType | string |  | 否 | 签名算法，应与后台下单时的值一致 |
|  | paySign | string |  | 否 | 签名，具体见微信支付文档 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 调用成功信息 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |
| errno | number | 错误码 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1000 |  | 系统错误 |
| 1022 |  | 参数json格式非法 |
| 702001 |  | 参数错误，具体原因见errMsg |
| 702002 |  | 用户态签名错误 |
| 702003 |  | 支付签名错误 |
| 702004 |  | mode不合法 |
| 702005 |  | out\_trade\_no重复，请更换新单号重试 |
| 702006 |  | 二级商户进件未完成 |
| 702007 |  | 用户未授权给品牌 |
| 702008 |  | 正式版小程序只能用生产环境下单 |
| 702009 |  | B2b授权关系校验不通过 |

---

### wx.requestAppleSubscribeSign(Object object)

基础库 3.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestAppleSubscribeSign.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | signData | Object |  | 是 | 具体支付参数见signData, 该参数需以string形式传递, 例如signData: '{"offerId":"123","productId":"testproductId","goodsPrice":10,"attach":"testdata"}' |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | offerId | string |  | 是 | mp-支付基础配置中的offerid | |  | productId | string |  | 是 | 订阅道具 ID（需已配置为双端可用） | |  | goodsPrice | number |  | 是 | 道具单价(分), 用来校验价格与后台道具价格是否一致, 避免用户在业务商城页看到的价格与实际价格不一致导致投诉 | |  | activitySellingPrice | number |  | 否 | 首开优惠价格（分）。不填=原价签约；填大于0=优惠价签约（首开此价格，续费恢复原价）；填0=免费试用签约（首开 0 元，续费恢复原价） | |  | attach | string |  | 是 | 透传数据, 签约成功通知/发货通知时透传给开发者 | | | | | |
|  | paySig | string |  | 是 | 支付签名, 详见[《签名详解》](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/virtual-payment.html) |
|  | signature | string |  | 是 | 用户态签名, 详见[《签名详解》](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/virtual-payment.html) |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | offerId | string |  | 是 | mp-支付基础配置中的offerid |
|  | productId | string |  | 是 | 订阅道具 ID（需已配置为双端可用） |
|  | goodsPrice | number |  | 是 | 道具单价(分), 用来校验价格与后台道具价格是否一致, 避免用户在业务商城页看到的价格与实际价格不一致导致投诉 |
|  | activitySellingPrice | number |  | 否 | 首开优惠价格（分）。不填=原价签约；填大于0=优惠价签约（首开此价格，续费恢复原价）；填0=免费试用签约（首开 0 元，续费恢复原价） |
|  | attach | string |  | 是 | 透传数据, 签约成功通知/发货通知时透传给开发者 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1001 |  | 参数错误 |
| -1 |  | 支付失败 |
| -2 |  | 支付取消 |
| -4 |  | 风控拦截 |
| -5 |  | 开通签约结果未知 |
| -15001 |  | 参数错误,具体原因见err\_msg |
| -15002 |  | outTradeNo重复使用,请换新单号重试 |
| -15003 |  | 系统错误 |
| -15004 |  | currencyType错误,目前只能填CNY |
| -15005 |  | 用户态签名signature错误 |
| -15006 |  | 支付签名paySig错误 |
| -15007 |  | session\_key过期 |
| -15008 |  | 二级商户进件未完成 |
| -15009 |  | 代币未发布 |
| -15010 |  | 道具productId未发布 |
| -15011 |  | 现网版本的env只能是0,不能填1(沙盒环境) |
| -15012 |  | 调用米大师失败导致关单,请换新单号重试 |
| -15013 |  | goodsPrice道具价格错误 |
| -15014 |  | 道具/代币发布未生效，禁止下单，大概10分钟后生效 |
| -15016 |  | signData格式有问题 |
| -15017 |  | 此商家涉嫌违规，收款功能已被限制，暂无法支付。商家可以登录微信商户平台/微信支付商家助手小程序查看原因和解决方案 |
| -15018 |  | 代币或者道具productId审核不通过 |
| -15019 |  | 调微信报商户受限,商家可以登录微信商户平台/微信支付商家助手小程序查看原因和解决方案 |
| -15020 |  | 操作过快，请稍候再试 |
| -15021 |  | 小程序被限频交易 |

---

### wx.openHKOfflinePayView(Object object)

基础库 3.4.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.openHKOfflinePayView.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | timeStamp | string |  | 是 | 时间戳，从 1970 年 1 月 1 日 00:00:00 至今的秒数，即当前的时间 |
|  | nonceStr | string |  | 是 | 随机字符串，长度为32个字符以下 |
|  | package | string |  | 是 | 业务数据包，开发者目前无需感知，直接传空字符串即可 |
|  | signType | string | SHA1 | 否 | 签名算法，应与后台下单时的值一致，目前仅支持 SHA1 |
|  | | 合法值 | 说明 | | --- | --- | | SHA1 | SHA1签名算法 | | | | | |
|  | paySign | string |  | 是 | 签名，具体见微信支付文档 |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| SHA1 | SHA1签名算法 |

---

### wx.jumpToOfflinePay(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.jumpToOfflinePay.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| appId | string |  | 是 | 公众号 ID，商户注册具有支付权限的公众号成功后即可获得 |
| timeStamp | string |  | 是 | 时间戳，从 1970 年 1 月 1 日 00:00:00 至今的秒数，即当前的时间 |
| nonceStr | string |  | 是 | 随机字符串，长度为 32 个字符以下 |
| package | string |  | 是 | 扩展字符串，需要带入商户号信息，例如：mch\_id=123456789 |
| signType | string |  | 是 | 签名方式，目前仅支持 SHA1 |
| paySign | string |  | 是 | 签名，具体签名方案参照微信公众号支付帮助文档 |
| queryStr | string |  | 是 | JSON 格式字符串（需 urlencode），包含 biz\_scene、recommend\_bank\_type、recommend\_bind\_serial |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### GlobalPayment wx.createGlobalPayment(Object object)

基础库 3.7.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.createGlobalPayment.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| mchRegion | string |  | 是 | 根据每笔订单实际的交易地区，提供地区编码，不同地区可能匹配不同的支付方式，参考 ISO3166二位字母代码标准，大写。 |
| isSandbox | string | false | 否 | true为开发环境，false为生产环境。不传入该参数，则默认为false，即生产环境。 |

---

### GlobalPayment

全球收银对象 GlobalPayment

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/payment/GlobalPayment.html

---

### Promise GlobalPayment.abort()

基础库 3.7.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/payment/GlobalPayment.abort.html

---

### Promise GlobalPayment.openMethodPicker(Object object)

基础库 3.7.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/payment/GlobalPayment.openMethodPicker.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | amount | Object |  | 是 | 交易金额对象 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | total | number |  | 是 | 交易金额，采用ISO4217标准中的最小货币单位进行表达，该值为整数，没有小数点。 | |  | currency | string |  | 是 | 交易币种，货币的符号采用ISO4217，3位大写字符进行表达。 | | | | | |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | total | number |  | 是 | 交易金额，采用ISO4217标准中的最小货币单位进行表达，该值为整数，没有小数点。 |
|  | currency | string |  | 是 | 交易币种，货币的符号采用ISO4217，3位大写字符进行表达。 |

---

### Promise GlobalPayment.requestGlobalPayment(Object object)

基础库 3.7.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/payment/GlobalPayment.requestGlobalPayment.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| prepayInfo | string |  | 是 | 预支付信息 |
| paymentId | string |  | 是 | ISO4217标准中的最小货币单位进行表达，该值为整数，没有小数点。 |

---

<!-- pages: 13 -->
