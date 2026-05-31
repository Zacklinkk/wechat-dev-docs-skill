# 微信小游戏 API 结构化参考 — location

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.getLocation(Object object)

从基础库3.0.1开始，本接口停止维护，请使用wx.getFuzzyLocation代替

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/location/wx.getLocation.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| type | string | wgs84 | 否 | wgs84 返回 gps 坐标，gcj02 返回可用于 wx.openLocation 的坐标 |  |
| altitude | boolean | false | 否 | 传入 true 会返回高度信息，由于获取高度需要较高精确度，会减慢接口返回速度 | [1.6.0](../../guide/runtime/client-lib/compatibility.html) |
| isHighAccuracy | boolean | false | 否 | 开启高精度定位 | [2.9.0](../../guide/runtime/client-lib/compatibility.html) |
| highAccuracyExpireTime | number |  | 否 | 高精度定位超时时间(ms)，指定时间内返回最高精度，该值3000ms以上高精度定位才有效果 | [2.9.0](../../guide/runtime/client-lib/compatibility.html) |
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
| altitude | number | 高度，单位 m | [1.2.0](../../guide/runtime/client-lib/compatibility.html) |
| verticalAccuracy | number | 垂直精度，单位 m（Android 无法获取，返回 0） | [1.2.0](../../guide/runtime/client-lib/compatibility.html) |
| horizontalAccuracy | number | 水平精度，单位 m | [1.2.0](../../guide/runtime/client-lib/compatibility.html) |

---

### wx.getFuzzyLocation(Object object)

基础库 2.25.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/location/wx.getFuzzyLocation.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | type | string | wgs84 | 否 | 返回的坐标类型 |
|  | | 合法值 | 说明 | | --- | --- | | wgs84 | 返回 gps 坐标 | | gcj02 | 返回 gcj02 坐标 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| wgs84 | 返回 gps 坐标 |
| gcj02 | 返回 gcj02 坐标 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| latitude | number | 纬度，范围为 -90~90，负数表示南纬 |
| longitude | number | 经度，范围为 -180~180，负数表示西经 |

---

<!-- pages: 2 -->
