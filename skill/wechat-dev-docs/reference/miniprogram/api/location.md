# 微信小程序 API 结构化参考 — location

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.stopLocationUpdate(Object object)

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.stopLocationUpdate.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.startLocationUpdateBackground(Object object)

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.startLocationUpdateBackground.html

**国内主体开放类目**

| 一级类目/主体类型 | 二级类目 | 应用场景 |
| --- | --- | --- |
| 电商平台 | / | 在小程序内提供线下商超导览、导航服务 |
| 商家自营 | / | 在小程序内提供线下商超导览、导航服务 |
| 交通服务 | / | 代驾服务、打车出行、城市共享交通、实时导航服务等 |
| 生活服务 | 跑腿、共享服务 | 含有B端小程序配送服务，基于地理位置共享工具类服务 |
| 物流服务 | 收件/派件、查件、邮政、装卸搬运、快递柜、货物运输 | 提供B端小程序快递/货物收发服务 |
| 餐饮服务 | 点餐平台、外卖平台 | 提供B端小程序餐饮配送服务、线下门店实时导航 |
| 工具 | 健康管理 | 基于实时地理位置提供身体管理记录等服务 |
| 旅游 | 景区服务、住宿服务 | 在小程序内提供景区导航、导览服务、酒店导航服务 |
| 政务民生 | / | 提供政务单位相关业务 |
| 政府主体账号 | / | 提供政务单位相关业务 |

**海外主体开放类目**

| 一级类目/主体类型 | 二级类目 | 应用场景 |
| --- | --- | --- |
| 交通服务 | / | 代驾服务、打车出行、城市共享交通、实时导航服务等 |
| 生活服务 | 家政、外送 | 含有B端小程序配送服务，基于地理位置导航上门服务 |
| 快递业与邮政 | / | 提供B端小程序快递/货物收发服务 |
| 餐饮服务 | 外卖点餐 | 提供B端小程序餐饮配送服务、线下门店实时导航 |
| 跨境电商 | / | 在小程序内提供线下商超导览、导航服务 |
| 本地服务 | 电商平台、服装/鞋/箱包、玩具、家电/数码/手机、美妆/洗护、珠宝/饰品/眼镜/钟表、运动/户外/乐器、鲜花/园艺/工艺品、家居/家饰/家纺、办公/文具、机械/电子器件、酒、食品、百货/超市/便利店、宠物食品/用品 | 在小程序内提供线下商超导览、导航服务 |

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| type | string | gcj02 | 否 | wgs84 返回 gps 坐标，gcj02 返回可用于 wx.openLocation 的坐标 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.startLocationUpdate(Object object)

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.startLocationUpdate.html

**国内主体开放类目**

| 一级类目/主体类型 | 二级类目 | 应用场景 |
| --- | --- | --- |
| 电商平台 | / | 售卖商品线下发货、收货、送货服务 |
| 商家自营 | / | 提供售卖商品线下发货、收货、送货服务、线下商超导览、导航服务 |
| 医疗服务 | 公立医疗机构、三级私立医疗机构、其他私立医疗机构、就医服务、其他医学健康服务、药品（非处方药）销售、非处方药销售平台、医疗器械生产企业、医疗器械自营、医疗器械经营销售平台、互联网医院血液、干细胞服务、临床试验 | 1、实际物品/药品接收服务 2、基于地理位置取号并现场报到、附近医院导航等服务 |
| 交通服务 | / | 代驾服务、租车网点导航等相关服务 |
| 生活服务 | / | 上门服务作业等线下场景 |
| 物流服务 | 收件/派件、查件、邮政、装卸搬运、快递柜、货物运输 | 快递/货物收发服务 |
| 餐饮服务 | 点餐平台、外卖平台 | 线下送餐服务 |
| 工具 | 天气、信息查询 | 与地理位置相关的服务，比如潮汐查询、海拔查询、天气查询等 |
| 金融 | 保险 | 提供线下网点预约、基于地理位置取号并现场报到、附近网点导航等服务 |
| 旅游 | 景区服务 | 提供景区导航、导览服务 |
| 政务民生 | / | 提供政务单位相关业务 |
| 政府主体账号 | / | 提供政务单位相关业务 |

**海外主体开放类目**

| 一级类目/主体类型 | 二级类目 | 应用场景 |
| --- | --- | --- |
| 出行与交通 | / | 代驾服务、租车网点导航等相关服务 |
| 快递业与邮政 | / | 快递/货物收发服务 |
| 餐饮 | 外卖点餐 | 线下送餐服务 |
| 出行与交通 | / | 代驾服务、租车网点导航等相关服务 |
| 跨境电商 | / | 提供售卖商品线下发货、收货服务、线下商超导览、导航服务 |
| 本地服务 | 电商平台、服装/鞋/箱包、玩具、家电/数码/手机、美妆/洗护、珠宝/饰品/眼镜/钟表、运动/户外/乐器、鲜花/园艺/工艺品、家居/家饰/家纺、办公/文具、机械/电子器件、酒、食品、百货/超市/便利店、宠物食品/用品 | 提供售卖商品线下发货、线下收货服务、线下商超导览、导航服务 |
| 生活服务 | 家政、外送 | 上门服务作业等线下场景 |

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| type | string | 坐标，gcj02 | 否 | wgs84 返回 gps 坐标，gcj02 返回可用于 wx.openLocation 的坐标 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.openLocation(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.openLocation.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| latitude | number |  | 是 | 纬度，范围为-90~90，负数表示南纬。使用 gcj02 国测局坐标系 |
| longitude | number |  | 是 | 经度，范围为-180~180，负数表示西经。使用 gcj02 国测局坐标系 |
| scale | number | 18 | 否 | 缩放比例，范围5~18 |
| name | string |  | 否 | 位置名 |
| address | string |  | 否 | 地址的详细说明 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.onLocationChangeError(function listener)

基础库 2.19.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.onLocationChangeError.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errCode | number | 错误码 |

---

### wx.onLocationChange(function listener)

基础库 2.8.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.onLocationChange.html

**国内主体开放类目**

| 一级类目/主体类型 | 二级类目 | 应用场景 |
| --- | --- | --- |
| 电商平台 | / | 售卖商品线下发货、收货、送货服务 |
| 商家自营 | / | 提供售卖商品线下发货、收货、送货服务、线下商超导览、导航服务 |
| 医疗服务 | 公立医疗机构、三级私立医疗机构、其他私立医疗机构、就医服务、其他医学健康服务、药品（非处方药）销售、非处方药销售平台、医疗器械生产企业、医疗器械自营、医疗器械经营销售平台、互联网医院血液、干细胞服务、临床试验 | 1、实际物品/药品接收服务 2、基于地理位置取号并现场报到、附近医院导航等服务 |
| 交通服务 | / | 代驾服务、租车网点导航等相关服务 |
| 生活服务 | / | 上门服务作业等线下场景 |
| 物流服务 | 收件/派件、查件、邮政、装卸搬运、快递柜、货物运输 | 快递/货物收发服务 |
| 餐饮服务 | 点餐平台、外卖平台 | 线下送餐服务 |
| 工具 | 天气、信息查询 | 与地理位置相关的服务，比如潮汐查询、海拔查询、天气查询等 |
| 金融 | 保险 | 提供线下网点预约、基于地理位置取号并现场报到、附近网点导航等服务 |
| 旅游 | 景区服务 | 提供景区导航、导览服务 |
| 政务民生 | / | 提供政务单位相关业务 |
| 政府主体账号 | / | 提供政务单位相关业务 |

**海外主体开放类目**

| 一级类目/主体类型 | 二级类目 | 应用场景 |
| --- | --- | --- |
| 出行与交通 | / | 代驾服务、租车网点导航等相关服务 |
| 快递业与邮政 | / | 快递/货物收发服务 |
| 餐饮 | 外卖点餐 | 线下送餐服务 |
| 出行与交通 | / | 代驾服务、租车网点导航等相关服务 |
| 跨境电商 | / | 提供售卖商品线下发货、收货服务、线下商超导览、导航服务 |
| 本地服务 | 电商平台、服装/鞋/箱包、玩具、家电/数码/手机、美妆/洗护、珠宝/饰品/眼镜/钟表、运动/户外/乐器、鲜花/园艺/工艺品、家居/家饰/家纺、办公/文具、机械/电子器件、酒、食品、百货/超市/便利店、宠物食品/用品 | 提供售卖商品线下发货、线下收货服务、线下商超导览、导航服务 |
| 生活服务 | 家政、外送 | 上门服务作业等线下场景 |

**function listener**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| latitude | number | 纬度，范围为 -90~90，负数表示南纬。使用 gcj02 国测局坐标系 |  |
| longitude | number | 经度，范围为 -180~180，负数表示西经。使用 gcj02 国测局坐标系 |  |
| speed | number | 速度，单位 m/s |  |
| accuracy | number | 位置的精确度 |  |
| altitude | number | 高度，单位 m | [1.2.0](../../framework/compatibility.html) |
| verticalAccuracy | number | 垂直精度，单位 m（Android 无法获取，返回 0） | [1.2.0](../../framework/compatibility.html) |
| horizontalAccuracy | number | 水平精度，单位 m | [1.2.0](../../framework/compatibility.html) |

---

### wx.offLocationChangeError(function listener)

基础库 2.19.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.offLocationChangeError.html

---

### wx.offLocationChange(function listener)

基础库 2.8.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.offLocationChange.html

---

### wx.getLocation(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.getLocation.html

**国内主体开放类目**

| 一级类目/主体类型 | 二级类目 | 应用场景 |
| --- | --- | --- |
| 电商平台 | / | 售卖商品线下发货、线下收货服务 |
| 商家自营 | / | 提供售卖商品线下发货、线下收货服务、线下商超导览、导航服务 |
| 医疗服务 | 公立医疗机构、三级私立医疗机构、其他私立医疗机构、就医服务、其他医学健康服务、药品（非处方药）销售、非处方药销售平台、医疗器械生产企业、医疗器械自营、医疗器械经营销售平台、互联网医院血液、干细胞服务、临床试验 | 1、实际物品/药品接收服务 2、基于地理位置取号并现场报到、附近医院导航等服务 |
| 交通服务 | / | 代驾服务、租车网点导航等相关服务 |
| 生活服务 | / | 上门服务作业等线下场景 |
| 物流服务 | 收件/派件、查件、邮政、装卸搬运、快递柜、货物运输 | 快递/货物收发服务 |
| 餐饮服务 | 点餐平台、外卖平台、餐饮服务场所/餐饮服务管理企业 | 线下送餐服务 |
| 工具 | 天气、信息查询、办公、设备管理 | 与地理位置相关的服务，比如潮汐查询、海拔查询、天气查询、智能穿戴、智能门禁、与地理位置相关的打卡服务等 |
| 金融 | 银行、非金融机构自营小额贷款/融资担保/商业保理、保险 | 提供线下网点预约、基于地理位置取号并现场报到、附近网点导航等服务 |
| 旅游 | 景区服务、住宿服务 | 提供景区导航、导览服务、酒店导航服务 |
| 汽车服务 | 维修保养、汽车用品、汽车经销商/4S店、汽车厂商、汽车预售、二手车 | 提供汽车售卖、维保洗美服务、查找附近的维修点/洗车网点等导航服务 |
| IT科技 | 基础电信运营商、电信业务代理商 | 提供运营商线下网点的预约、基于地理位置取号并现场报到、网点导航等服务 |
| 房地产服务 | 物业管理、房屋中介、房屋装修 | 提供房地产开发商及物业公司门店导览导航服务 |
| 政务民生 | / | 提供政务单位相关业务 |
| 政府主体账号 | / | 提供政务单位相关业务 |

**海外主体开放类目**

| 一级类目/主体类型 | 二级类目 | 应用场景 |
| --- | --- | --- |
| 出行与交通 | / | 代驾服务、租车网点导航等相关服务 |
| 快递业与邮政 | / | 快递/货物收发服务 |
| 餐饮 | 外卖点餐 | 线下送餐服务 |
| 出行与交通 | / | 代驾服务、租车网点导航等相关服务 |
| 跨境电商 | / | 提供售卖商品线下发货、收货服务、线下商超导览、导航服务 |
| 本地服务 | 电商平台、服装/鞋/箱包、玩具、家电/数码/手机、美妆/洗护、珠宝/饰品/眼镜/钟表、运动/户外/乐器、鲜花/园艺/工艺品、家居/家饰/家纺、办公/文具、机械/电子器件、酒、食品、百货、超市/便利店、宠物食品/用品 | 提供售卖商品线下发货、线下收货服务、线下商超导览、导航服务 |
| 生活服务 | 家政、外送、票务 | 上门服务作业、景区导览服务等线下场景 |
| 旅游 | 酒店服务 | 提供酒店位置导航服务 |

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| type | string | wgs84 | 否 | wgs84 返回 gps 坐标，gcj02 返回可用于 wx.openLocation 的坐标 |  |
| altitude | boolean | false | 否 | 传入 true 会返回高度信息，由于获取高度需要较高精确度，会减慢接口返回速度 | [1.6.0](../../framework/compatibility.html) |
| isHighAccuracy | boolean | false | 否 | 开启高精度定位 | [2.9.0](../../framework/compatibility.html) |
| highAccuracyExpireTime | number |  | 否 | 高精度定位超时时间(ms)，指定时间内返回最高精度，该值3000ms以上高精度定位才有效果 | [2.9.0](../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| latitude | number | 纬度，范围为 -90~90，负数表示南纬 |  |
| longitude | number | 经度，范围为 -180~180，负数表示西经 |  |
| speed | number | 速度，单位 m/s |  |
| accuracy | number | 位置的精确度，反应与真实位置之间的接近程度，可以理解成10即与真实位置相差10m，越小越精确 |  |
| altitude | number | 高度，单位 m | [1.2.0](../../framework/compatibility.html) |
| verticalAccuracy | number | 垂直精度，单位 m（Android 无法获取，返回 0） | [1.2.0](../../framework/compatibility.html) |
| horizontalAccuracy | number | 水平精度，单位 m | [1.2.0](../../framework/compatibility.html) |

---

### wx.getFuzzyLocation(Object object)

基础库 2.25.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.getFuzzyLocation.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | type | string | wgs84 | 否 | 返回的坐标类型 |
|  | | 合法值 | 说明 | | --- | --- | | wgs84 | 返回 gps 坐标 | | gcj02 | 返回 gcj02 坐标，可用于 wx.openLocation | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| wgs84 | 返回 gps 坐标 |
| gcj02 | 返回 gcj02 坐标，可用于 wx.openLocation |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| latitude | number | 纬度，范围为 -90~90，负数表示南纬 |
| longitude | number | 经度，范围为 -180~180，负数表示西经 |

---

### wx.choosePoi(Object object)

为确保选择地理位置接口的合理使用，位置接口调整参考选择地理位置接口调整公告

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.choosePoi.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| type | number | 选择城市时，值为 1，选择精确位置时，值为 2 |
| city | number | 城市名称 |
| name | string | 位置名称 |
| address | string | 详细地址 |
| latitude | number | 纬度，浮点数，范围为-90~90，负数表示南纬。使用 gcj02 国测局坐标系（即将废弃） |
| longitude | number | 经度，浮点数，范围为-180~180，负数表示西经。使用 gcj02 国测局坐标系（即将废弃） |

---

### wx.chooseLocation(Object object)

为确保选择地理位置接口的合理使用，位置接口调整参考选择地理位置接口调整公告

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.chooseLocation.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| latitude | number |  | 否 | 目标地纬度 | [2.9.0](../../framework/compatibility.html) |
| longitude | number |  | 否 | 目标地经度 | [2.9.0](../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| name | string | 位置名称 |
| address | string | 详细地址 |
| latitude | number | 纬度，浮点数，范围为-90~90，负数表示南纬。使用 gcj02 国测局坐标系 |
| longitude | number | 经度，浮点数，范围为-180~180，负数表示西经。使用 gcj02 国测局坐标系 |

---

<!-- pages: 12 -->
