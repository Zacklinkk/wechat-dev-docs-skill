# 微信小游戏 API 结构化参考 — midas-payment

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.requestMidasPaymentGameItem(Object object)

基础库 2.19.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/midas-payment/wx.requestMidasPaymentGameItem.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | signData | Object |  | 是 | **支付原串** 具体支付参数见下面的signData，需要将数据以json格式传递 signData例子: '{"mode":"goods","offerId":"123","buyQuantity":1,"env":0,"currencyType":"CNY","platform":"android","zoneId":"1","productId":"testproductId","goodsPrice":10,"outTradeNo":"xxxxxx","attach":"testdata"}' |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | mode | string |  | 是 | **支付的类型** 不同的支付类型有各自额外要传的附加参数 | |  | offerId | string |  | 是 | **在米大师侧申请的应用id** mp-支付基础配置中的offerid | |  | buyQuantity | number |  | 是 | **购买数量** | |  | env | number | 0 | 否 | **环境配置** | |  | | 合法值 | 说明 | | --- | --- | | 0 | 米大师正式环境 | | 1 | 米大师沙箱环境 | | | | | | |  | currencyType | string |  | 是 | **币种** | |  | | 合法值 | 说明 | | --- | --- | | CNY | 人民币 | | | | | | |  | platform | string | android | 否 | **平台** | |  | | 合法值 | 说明 | | --- | --- | | android | 安卓 | | | | | | |  | zoneId | string | 1 | 否 | **分区ID** | |  | productId | string |  | 是 | **道具ID** | |  | goodsPrice | number |  | 是 | **道具单价（分）** 用来校验价格与后台道具价格是否一致，避免用户在业务商城页看到的价格与实际价格不一致导致投诉 | |  | outTradeNo | string |  | 是 | **业务订单号** 每个订单号只能使用一次，重复使用会失败（极端情况不保证唯一，不建议业务强依赖唯一性）。 要求32个字符内，只能是数字、大小写字母、符号 \_-|\*@组成，不能以下划线(\_)开头。 若没有传入，则平台会自动填充一个，并以下划线开头。 | |  | attach | string |  | 否 | **透传数据** 发货通知时会透传给开发者 | | | | | |
|  | paySig | string |  | 是 | **支付签名** pay\_sig参数的签名算法，使用**“mp-支付基础配置”**中的**AppKey**对支付的请求进行签名，代表请求经过开发者服务端的支付模块发起。签名算法伪代码为： paySig = to\_hex(hmac\_sha256(appKey,'requestMidasPaymentGameItem' + '&' + signData)) 具体可见代码示例中的支付签名代码实现 |
|  | signature | string |  | 是 | **用户态签名** signature参数签名算法参考[用户态签名](https://developers.weixin.qq.com/minigame/dev/guide/open-ability/signature.html#%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95%E6%80%81%E7%AD%BE%E5%90%8D) 可参考[calc\_signature](https://docs.qq.com/doc/DVUN0QWJja0J5c2x4) |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | mode | string |  | 是 | **支付的类型** 不同的支付类型有各自额外要传的附加参数 |
|  | offerId | string |  | 是 | **在米大师侧申请的应用id** mp-支付基础配置中的offerid |
|  | buyQuantity | number |  | 是 | **购买数量** |
|  | env | number | 0 | 否 | **环境配置** |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 米大师正式环境 | | 1 | 米大师沙箱环境 | | | | | |
|  | currencyType | string |  | 是 | **币种** |
|  | | 合法值 | 说明 | | --- | --- | | CNY | 人民币 | | | | | |
|  | platform | string | android | 否 | **平台** |
|  | | 合法值 | 说明 | | --- | --- | | android | 安卓 | | | | | |
|  | zoneId | string | 1 | 否 | **分区ID** |
|  | productId | string |  | 是 | **道具ID** |
|  | goodsPrice | number |  | 是 | **道具单价（分）** 用来校验价格与后台道具价格是否一致，避免用户在业务商城页看到的价格与实际价格不一致导致投诉 |
|  | outTradeNo | string |  | 是 | **业务订单号** 每个订单号只能使用一次，重复使用会失败（极端情况不保证唯一，不建议业务强依赖唯一性）。 要求32个字符内，只能是数字、大小写字母、符号 \_-|\*@组成，不能以下划线(\_)开头。 若没有传入，则平台会自动填充一个，并以下划线开头。 |
|  | attach | string |  | 否 | **透传数据** 发货通知时会透传给开发者 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 0 | 米大师正式环境 |
| 1 | 米大师沙箱环境 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| CNY | 人民币 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| android | 安卓 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| -1 |  | 系统失败 |
| -2 |  | 支付取消 |
| -6 |  | 下单参数类型不对 |
| -15001 |  | 虚拟支付接口错误码，缺少参数 |
| -15002 |  | 虚拟支付接口错误码，参数不合法 |
| -15003 |  | 虚拟支付接口错误码，订单重复 |
| -15004 |  | 虚拟支付接口错误码，后台错误 |
| -15005 |  | 虚拟支付接口错误码，appId权限被封禁 |
| -15006 |  | 虚拟支付接口错误码，货币类型不支持 |
| -15007 |  | 虚拟支付接口错误码，订单已支付 |
| -15009 |  | 虚拟支付接口错误码，由于健康系统限制，本次支付已超过限额（这种错误情况会有默认弹窗提示） |
| -15010 |  | 虚拟支付接口错误码，正式版小游戏不允许在沙箱环境支付 |
| -15011 |  | 请求的数据类型错误 |
| -15012 |  | SIGNATURE错误 |
| -15013 |  | 代币未发布 |
| -15014 |  | paysig错误 |
| -15015 |  | sessionkey过期 |
| -15016 |  | 道具价格错误 |
| -15017 |  | 订单已关闭 |
| 1 |  | 虚拟支付接口错误码，用户取消支付 |
| 2 |  | 虚拟支付接口错误码，客户端错误,判断到小程序在用户处于支付中时,又发起了一笔支付请求 |
| 3 |  | 虚拟支付接口错误码，Android独有错误：用户使用GooglePlay支付，而手机未安装GooglePlay |
| 4 |  | 虚拟支付接口错误码，用户操作系统支付状态异常 |
| 5 |  | 虚拟支付接口错误码，操作系统错误 |
| 6 |  | 虚拟支付接口错误码，其他错误 |
| 7 |  | 虚拟支付接口错误码，支付取消 |
| 1000 |  | 参数错误 |
| 1001 |  | 分区未发布 |
| 1003 |  | 代币/分区未发布或者对应商户号被封禁或者米大师Portal错误,请先确保虚拟支付2.0代币和分区已发布，然后自查商户号封禁情况https://kf.qq.com/faq/190523Mb6VRJ190523RV363E.html，对应的商户号可以在mp-虚拟支付2.0-基础配置-微信支付账号信息中查询 |
| 3017/-15012 |  | 道具id非法 |
| 701001 |  | ios禁止支付 |

---

### wx.requestMidasPayment(Object object)

基础库 2.19.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/midas-payment/wx.requestMidasPayment.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | mode | string |  | 是 | 支付的类型，不同的支付类型有各自额外要传的附加参数。 |
|  | | 合法值 | 说明 | | --- | --- | | game | 购买游戏币 | | | | | |
|  | env | number | 0 | 否 | 环境配置 |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 米大师正式环境 | | 1 | 米大师沙箱环境 | | | | | |
|  | offerId | string |  | 是 | 在米大师侧申请的应用 id |
|  | currencyType | string |  | 是 | 币种 |
|  | | 合法值 | 说明 | | --- | --- | | CNY | 人民币 | | | | | |
|  | platform | string |  | 否 | 申请接入时的平台，platform 与应用id有关。 |
|  | | 合法值 | 说明 | | --- | --- | | android | android | | | | | |
|  | buyQuantity | number |  | 否 | 购买数量。mode=game 时必填。购买数量。详见 [buyQuantity 限制说明](#buyquantity-限制说明)。 |
|  | zoneId | string | 1 | 否 | 分区 ID |
|  | outTradeNo | string |  | 是 | 业务订单号，每个订单号只能使用一次，重复使用会失败。开发者需要确保该订单号在对应游戏下的唯一性，平台会尽可能校验该唯一性约束，但极端情况下可能会跳过对该约束的校验。要求32个字符内，只能是数字、大小写字母、符号\_-|\*组成，不能以下划线（)开头。建议每次调用wx.requestMidasPayment都换新的outTradeNo。若没有传入，则平台会自动填充一个，并以下划线开头 |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| game | 购买游戏币 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 0 | 米大师正式环境 |
| 1 | 米大师沙箱环境 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| CNY | 人民币 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| android | android |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 调用成功信息 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |
| errCode | number | 错误码 |
| errno | number | 错误码 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| -1 |  | 系统失败 |
| -2 |  | 支付取消 |
| -6 |  | 下单参数类型不对 |
| -15001 |  | 虚拟支付接口错误码，缺少参数 |
| -15002 |  | 虚拟支付接口错误码，参数不合法 |
| -15003 |  | 虚拟支付接口错误码，订单重复 |
| -15004 |  | 虚拟支付接口错误码，后台错误 |
| -15005 |  | 虚拟支付接口错误码，appId权限被封禁 |
| -15006 |  | 虚拟支付接口错误码，货币类型不支持 |
| -15007 |  | 虚拟支付接口错误码，订单已支付 |
| -15009 |  | 虚拟支付接口错误码，由于健康系统限制，本次支付已超过限额（这种错误情况会有默认弹窗提示） |
| -15010 |  | 虚拟支付接口错误码，正式版小游戏不允许在沙箱环境支付 |
| -15011 |  | 请求的数据类型错误 |
| -15012 |  | SIGNATURE错误 |
| -15013 |  | 代币未发布 |
| -15014 |  | paysig错误 |
| -15015 |  | sessionkey过期 |
| -15016 |  | 道具价格错误 |
| -15017 |  | 订单已关闭 |
| 1 |  | 虚拟支付接口错误码，用户取消支付 |
| 2 |  | 虚拟支付接口错误码，客户端错误,判断到小程序在用户处于支付中时,又发起了一笔支付请求 |
| 3 |  | 虚拟支付接口错误码，Android独有错误：用户使用GooglePlay支付，而手机未安装GooglePlay |
| 4 |  | 虚拟支付接口错误码，用户操作系统支付状态异常 |
| 5 |  | 虚拟支付接口错误码，操作系统错误 |
| 6 |  | 虚拟支付接口错误码，其他错误 |
| 7 |  | 虚拟支付接口错误码，支付取消 |
| 1000 |  | 参数错误 |
| 1001 |  | 分区未发布 |
| 1003 |  | 代币/分区未发布或者对应商户号被封禁或者米大师Portal错误,请先确保虚拟支付2.0代币和分区已发布，然后自查商户号封禁情况https://kf.qq.com/faq/190523Mb6VRJ190523RV363E.html，对应的商户号可以在mp-虚拟支付2.0-基础配置-微信支付账号信息中查询 |
| 3017/-15012 |  | 道具id非法 |
| 701001 |  | ios禁止支付 |

**buyQuantity 限制说明**

| 价格等级（单位：人民币） |
| --- |
| 1 |
| 3 |
| 6 |
| 8 |
| 12 |
| 18 |
| 25 |
| 30 |
| 40 |
| 45 |
| 50 |
| 60 |
| 68 |
| 73 |
| 78 |
| 88 |
| 98 |
| 108 |
| 118 |
| 128 |
| 148 |
| 168 |
| 188 |
| 198 |
| 328 |
| 648 |
| 998 |
| 1998 |
| 2998 |

---

### wx.requestMidasFriendPayment(Object object)

接口已废弃

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/midas-payment/wx.requestMidasFriendPayment.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | mode | string |  | 是 | 支付的类型，不同的支付类型有各自额外要传的附加参数 |
|  | | 合法值 | 说明 | | --- | --- | | game | 购买游戏币 | | | | | |
|  | env | number |  | 是 | 环境配置 |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 米大师正式环境 | | 1 | 米大师沙箱环境 | | | | | |
|  | offerId | string |  | 是 | 在米大师侧申请的应用 id |
|  | currencyType | string |  | 是 | 币种 |
|  | | 合法值 | 说明 | | --- | --- | | CNY | 人民币 | | | | | |
|  | platform | string |  | 是 | 申请接入时的平台，platform 与应用id有关。 |
|  | | 合法值 | 说明 | | --- | --- | | android | Android平台 | | | | | |
|  | buyQuantity | number |  | 是 | 购买数量。mode=game 时必填。购买数量。详见 [buyQuantity 限制说明](#buyQuantity限制说明)。 |
|  | zoneId | string |  | 是 | 分区 ID |
|  | outTradeNo | string |  | 是 | 开发者业务订单号，每个订单号只能使用一次，重复使用会失败。要求32个字符内，只能是数字、大小写字母、符号 `_-|*@` |
|  | nonceStr | string |  | 是 | 随机字符串，长度应小于 128 |
|  | timeStamp | number |  | 是 | 生成这个随机字符串的 UNIX 时间戳（精确到秒） |
|  | signature | string |  | 是 | 签名 |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| game | 购买游戏币 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 0 | 米大师正式环境 |
| 1 | 米大师沙箱环境 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| CNY | 人民币 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| android | Android平台 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |
| encryptedData | string | 包括敏感数据在内的完整转发信息的加密数据，详细见[加密数据解密算法](../../guide/open-ability/signature.html) |
| iv | string | 加密算法的初始向量，详细见[加密数据解密算法](../../guide/open-ability/signature.html) |
| cloudID | string | 敏感数据对应的云 ID，开通[云开发](../../wxcloud/basis/getting-started.html)的小程序才会返回，可通过云调用直接获取开放数据，详细见[云调用直接获取开放数据](../../guide/open-ability/signature.html#method-cloud) |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1000 |  | mode错误 |
| -15005 |  | 索要权限被封禁（索要功能不可用） |
| -10073011 |  | 参数错误（具体错误见errMsg） |
| -10073003 |  | outTradeNo业务单号重复 |
| -10073012 |  | 索要单已支付 |
| -10073013 |  | 索要单已超时 |
| -10073014 |  | 签名错误 |
| -10073015 |  | 索要功能不可用 |

**buyQuantity限制说明**

| 价格等级（单位：人民币） |
| --- |
| 1 |
| 3 |
| 6 |
| 8 |
| 12 |
| 18 |
| 25 |
| 30 |
| 40 |
| 45 |
| 50 |
| 60 |
| 68 |
| 73 |
| 78 |
| 88 |
| 98 |
| 108 |
| 118 |
| 128 |
| 148 |
| 168 |
| 188 |
| 198 |
| 328 |
| 648 |
| 998 |
| 1998 |
| 2998 |

---

### wx.checkIsSupportMidasPayment(Object object)

基础库 3.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/midas-payment/wx.checkIsSupportMidasPayment.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | errMsg | String | 调用结果信息，格式为 "checkIsSupportMidasPayment:ok" |
|  | data | Object | 支付支持信息对象 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | err\_code | Number | 错误码，0 表示成功 | |  | err\_msg | String | 错误信息，"success" 表示成功 | |  | allow\_pay | Boolean | 是否支持支付，true 表示支持，false 表示不支持 | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | err\_code | Number | 错误码，0 表示成功 |
|  | err\_msg | String | 错误信息，"success" 表示成功 |
|  | allow\_pay | Boolean | 是否支持支付，true 表示支持，false 表示不支持 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | String | 错误信息 |

---

<!-- pages: 4 -->
