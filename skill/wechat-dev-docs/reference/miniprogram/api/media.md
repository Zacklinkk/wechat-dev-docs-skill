# 微信小程序 API 结构化参考 — media

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### MapContext wx.createMapContext(string mapId, Object this)

小程序插件：支持，需要小程序基础库版本不低于1.9.6

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/wx.createMapContext.html

---

### MapContext

相关文档:map

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.html

**visualLayerEvent**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| layerId | String | 图层 id |
| eventType | String | 事件类型 |
| eventInfo | String | 事件信息 |

**markerClusterCreate**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| clusters | `Array<ClusterInfo>` | 聚合簇数据 |

**markerClusterClick**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| cluster | ClusterInfo | 聚合簇 |

**markerClusterClick**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| clusterId | Number | 聚合簇的 id |
| center | LatLng | 聚合簇的坐标 |
| markerIds | `Array<Number>` | 该聚合簇内的点标记数据数组 |

**markerCollisionStatusChange**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| show | `Array<Number>` | 碰撞时隐藏后又显示的 `markerIds` |
| hide | `Array<Number>` | 碰撞时被隐藏的 `markerIds` |

---

### MapContext.addArc(Object object)

基础库 2.22.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.addArc.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | id | number |  | 是 | 圆弧 id |
|  | start | Object |  | 是 | 起始点 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | longitude | number |  | 是 | 经度 | |  | latitude | number |  | 是 | 纬度 | | | | | |
|  | end | Object |  | 是 | 终点 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | longitude | number |  | 是 | 经度 | |  | latitude | number |  | 是 | 纬度 | | | | | |
|  | pass | Object |  | 否 | 途经点 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | longitude | number |  | 是 | 经度 | |  | latitude | number |  | 是 | 纬度 | | | | | |
|  | angle | number | 0 | 否 | 夹角角度 |
|  | width | number | 5 | 否 | 线宽 |
|  | color | number | #000000 | 否 | 线的颜色 |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | longitude | number |  | 是 | 经度 |
|  | latitude | number |  | 是 | 纬度 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | longitude | number |  | 是 | 经度 |
|  | latitude | number |  | 是 | 纬度 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | longitude | number |  | 是 | 经度 |
|  | latitude | number |  | 是 | 纬度 |

---

### MapContext.addCustomLayer(Object object)

基础库 2.12.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.addCustomLayer.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| layerId | string |  | 是 | 个性化图层id |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### MapContext.addGroundOverlay(Object object)

基础库 2.14.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.addGroundOverlay.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | id | Number |  | 是 | 图片图层 id |
|  | src | String |  | 是 | 图片路径，支持网络图片、临时路径、代码包路径 |
|  | bounds | Object |  | 是 | 图片覆盖的经纬度范围 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | southwest | Object |  | 是 | 西南角经纬度 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | longitude | number |  | 是 | 经度 | |  | latitude | number |  | 是 | 纬度 | | | | | | |  | northeast | Object |  | 是 | 东北角经纬度 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | longitude | number |  | 是 | 经度 | |  | latitude | number |  | 是 | 纬度 | | | | | | | | | | |
|  | visible | Boolean | true | 否 | 是否可见 |
|  | zIndex | Number | 1 | 否 | 图层绘制顺序 |
|  | opacity | Number | 1 | 否 | 图层透明度 |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | southwest | Object |  | 是 | 西南角经纬度 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | longitude | number |  | 是 | 经度 | |  | latitude | number |  | 是 | 纬度 | | | | | |
|  | northeast | Object |  | 是 | 东北角经纬度 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | longitude | number |  | 是 | 经度 | |  | latitude | number |  | 是 | 纬度 | | | | | |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | longitude | number |  | 是 | 经度 |
|  | latitude | number |  | 是 | 纬度 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | longitude | number |  | 是 | 经度 |
|  | latitude | number |  | 是 | 纬度 |

---

### MapContext.addMarkers(Object object)

基础库 2.13.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.addMarkers.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| markers | Array |  | 是 | 同传入 map 组件的 marker 属性 |
| clear | boolean | false | 否 | 是否先清空地图上所有 marker |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### MapContext.addVisualLayer(Object object)

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.addVisualLayer.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| layerId | String |  | 是 | 可视化图层id（[创建图层指引](https://lbs.qq.com/dev/console/layers/layerEdit)) |
| interval | Number | 0 | 否 | 刷新周期，单位秒 |
| zIndex | Number | 1 | 否 | 图层绘制顺序 |
| opacity | Number | 1 | 否 | 图层透明度 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### MapContext.eraseLines(Object object)

基础库 2.5.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.eraseLines.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | lines | Array.<Object> |  | 是 | 要擦除的线段数组。详见 [polyline 属性](../../../component/map.html#polyline)。 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | id | number |  | 是 | 线段的 id。 | |  | index | number |  | 是 | 指定线段的某一段，线段起点 index 为 0 | |  | point | Object |  | 是 | 指定线段某一段中的点 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | longitude | number |  | 是 | 经度 | |  | latitude | number |  | 是 | 纬度 | | | | | | |  | clear | boolean | true | 否 | 为 true 时擦除，false 时置灰 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | id | number |  | 是 | 线段的 id。 |
|  | index | number |  | 是 | 指定线段的某一段，线段起点 index 为 0 |
|  | point | Object |  | 是 | 指定线段某一段中的点 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | longitude | number |  | 是 | 经度 | |  | latitude | number |  | 是 | 纬度 | | | | | |
|  | clear | boolean | true | 否 | 为 true 时擦除，false 时置灰 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | longitude | number |  | 是 | 经度 |
|  | latitude | number |  | 是 | 纬度 |

---

### MapContext.executeVisualLayerCommand(Object object)

基础库 2.26.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.executeVisualLayerCommand.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| layerId | string |  | 是 | 可视化图层id |
| command | string |  | 是 | 图层指令 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 调用结果 |
| data | string | SDK 返回的 JSON 数据 |

---

### MapContext.fromScreenLocation(Object object)

基础库 2.14.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.fromScreenLocation.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| x | Number |  | 是 | x 坐标值 |
| y | Number |  | 是 | y 坐标值 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| latitude | number | 纬度 |
| longitude | number | 经度 |

---

### MapContext.getCenterLocation(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.getCenterLocation.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| iconPath | string |  | 否 | 图标路径，支持网络路径、本地路径、代码包路径 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| longitude | number | 经度 |
| latitude | number | 纬度 |

---

### MapContext.getRegion(Object object)

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.getRegion.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | southwest | Object | 西南角经纬度 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | longitude | number | 经度 | |  | latitude | number | 纬度 | | | |
|  | northeast | Object | 东北角经纬度 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | longitude | number | 经度 | |  | latitude | number | 纬度 | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | longitude | number | 经度 |
|  | latitude | number | 纬度 |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | longitude | number | 经度 |
|  | latitude | number | 纬度 |

---

### MapContext.getRotate(Object object)

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.getRotate.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| rotate | number | 旋转角 |

---

### MapContext.getScale(Object object)

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.getScale.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| scale | number | 缩放值 |

---

### MapContext.getSkew(Object object)

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.getSkew.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| skew | number | 倾斜角 |

---

### MapContext.includePoints(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.includePoints.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | points | Array.<Object> |  | 是 | 要显示在可视区域内的坐标点列表 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | longitude | number |  | 是 | 经度 | |  | latitude | number |  | 是 | 纬度 | | | | | |
|  | padding | Array.<number> |  | 否 | 坐标点形成的矩形边缘到地图边缘的距离，单位像素。格式为[上,右,下,左]。开发者工具暂不支持padding参数。 |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | longitude | number |  | 是 | 经度 |
|  | latitude | number |  | 是 | 纬度 |

---

### MapContext.initMarkerCluster(Object object)

基础库 2.13.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.initMarkerCluster.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| enableDefaultStyle | boolean | true | 否 | 启用默认的聚合样式 |
| zoomOnClick | boolean | true | 否 | 点击已经聚合的标记点时是否实现聚合分离 |
| gridSize | number | 60 | 否 | 聚合算法的可聚合距离，即距离小于该值的点会聚合至一起，以像素为单位 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### MapContext.moveAlong(Object object)

基础库 2.13.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.moveAlong.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| markerId | number |  | 是 | 指定 marker |
| path | Array |  | 是 | 移动路径的坐标串，坐标点格式 `{longitude, latitude}` |
| autoRotate | boolean | true | 否 | 根据路径方向自动改变 marker 的旋转角度 |
| duration | number |  | 是 | 平滑移动的时间 |
| precision | Object |  | 是 | 平滑移动触发 map 组件 interpolatepoint 事件的插值精度，单位为 m。默认不触发。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### MapContext.moveToLocation(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.moveToLocation.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| longitude | number |  | 否 | 经度 | [2.8.0](../../../framework/compatibility.html) |
| latitude | number |  | 否 | 纬度 | [2.8.0](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### MapContext.on(string event, function callback)

基础库 2.13.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.on.html

**visualLayerEvent**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| layerId | String | 图层 id |
| eventType | String | 事件类型 |
| eventInfo | String | 事件信息 |

**markerClusterCreate**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| clusters | `Array&lt;ClusterInfo&gt;` | 聚合簇数据 |

**markerClusterClick**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| cluster | ClusterInfo | 聚合簇 |

**markerClusterClick**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| clusterId | Number | 聚合簇的 id |
| center | LatLng | 聚合簇的坐标 |
| markerIds | `Array&lt;Number&gt;` | 该聚合簇内的点标记数据数组 |

**markerCollisionStatusChange**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| show | `Array&lt;Number&gt;` | 碰撞时隐藏后又显示的 `markerIds` |
| hide | `Array&lt;Number&gt;` | 碰撞时被隐藏的 `markerIds` |

**string event**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| markerClusterCreate |  |  |
| markerClusterClick |  |  |
| visualLayerEvent |  |  |
| markerCollisionStatusChange |  |  |

---

### MapContext.openMapApp(Object object)

基础库 2.14.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.openMapApp.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | longitude | Number |  | 是 | 目的地经度 |
|  | latitude | Number |  | 是 | 目的地纬度 |
|  | destination | String |  | 是 | 目的地名称 |
|  | preferApplication | String |  | 否 | 指定推荐使用的地图 App |
|  | | 合法值 | 说明 | | --- | --- | | baidu | 百度地图 | | google | 谷歌地图 | | amap | 高德地图 | | tencent | 腾讯地图 | | petal | 花瓣地图 | | apple | 苹果地图 | | | | | |
|  | poiId | Object |  | 否 | 传递给地图App的poi参数 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | baidu | String |  | 否 | 百度地图 | |  | google | String |  | 否 | 谷歌地图 | |  | amap | String |  | 否 | 高德地图 | |  | tencent | String |  | 否 | 腾讯地图 | |  | petal | String |  | 否 | 花瓣地图 | |  | apple | String |  | 否 | 苹果地图 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| baidu | 百度地图 |
| google | 谷歌地图 |
| amap | 高德地图 |
| tencent | 腾讯地图 |
| petal | 花瓣地图 |
| apple | 苹果地图 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | baidu | String |  | 否 | 百度地图 |
|  | google | String |  | 否 | 谷歌地图 |
|  | amap | String |  | 否 | 高德地图 |
|  | tencent | String |  | 否 | 腾讯地图 |
|  | petal | String |  | 否 | 花瓣地图 |
|  | apple | String |  | 否 | 苹果地图 |

---

### MapContext.removeArc(Object object)

基础库 2.22.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.removeArc.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| id | number |  | 是 | 圆弧 id |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### MapContext.removeCustomLayer(Object object)

基础库 2.12.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.removeCustomLayer.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| layerId | string |  | 是 | 个性化图层id |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### MapContext.removeGroundOverlay(Object object)

基础库 2.14.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.removeGroundOverlay.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| id | String |  | 是 | 图片图层 id |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### MapContext.removeMarkers(Object object)

基础库 2.13.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.removeMarkers.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| markerIds | Array |  | 是 | marker 的 id 集合。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### MapContext.removeVisualLayer(Object object)

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.removeVisualLayer.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| layerId | string |  | 是 | 可视化图层id |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### MapContext.setBoundary(Object object)

基础库 2.22.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.setBoundary.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | southwest | Object |  | 是 | 西南角经纬度 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | longitude | number |  | 是 | 经度 | |  | latitude | number |  | 是 | 纬度 | | | | | |
|  | northeast | Object |  | 是 | 东北角经纬度 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | longitude | number |  | 是 | 经度 | |  | latitude | number |  | 是 | 纬度 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | longitude | number |  | 是 | 经度 |
|  | latitude | number |  | 是 | 纬度 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | longitude | number |  | 是 | 经度 |
|  | latitude | number |  | 是 | 纬度 |

---

### MapContext.setCenterOffset(Object object)

基础库 2.10.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.setCenterOffset.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| offset | Array.<number> |  | 是 | 偏移量，两位数组 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### MapContext.setLocMarkerIcon(Object object)

基础库 2.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.setLocMarkerIcon.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| iconPath | string |  | 否 | 图标路径，支持网络路径、本地路径、代码包路径 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### MapContext.toScreenLocation(Object object)

基础库 2.14.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.toScreenLocation.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| latitude | Number |  | 是 | 纬度 |
| longitude | Number |  | 是 | 经度 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| x | number | x 坐标值 |
| y | number | y 坐标值 |

---

### MapContext.translateMarker(Object object)

从基础库3.11.2开始，本接口停止维护，请使用 建议使用MapContext.moveAlong代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.translateMarker.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | markerId | number |  | 是 | 指定 marker |  |
|  | destination | Object |  | 是 | 指定 marker 移动到的目标点 |  |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | longitude | number |  | 是 | 经度 | |  | latitude | number |  | 是 | 纬度 | | | | | | |
|  | autoRotate | boolean |  | 是 | 移动过程中是否自动旋转 marker |  |
|  | rotate | number |  | 是 | marker 的旋转角度 |  |
|  | moveWithRotate | boolean | false | 否 | 平移和旋转同时进行 | [2.13.0](../../../framework/compatibility.html) |
|  | duration | number | 1000 | 否 | 动画持续时长，平移与旋转分别计算 |  |
|  | animationEnd | function |  | 否 | 动画结束回调函数 |  |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | longitude | number |  | 是 | 经度 |
|  | latitude | number |  | 是 | 纬度 |

---

### MapContext.updateGroundOverlay(Object object)

基础库 2.14.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.updateGroundOverlay.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | id | String |  | 是 | 图片图层 id |
|  | src | String |  | 是 | 图片路径，支持网络图片、临时路径、代码包路径 |
|  | bounds | Object |  | 是 | 图片覆盖的经纬度范围 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | southwest | Object |  | 是 | 西南角经纬度 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | longitude | number |  | 是 | 经度 | |  | latitude | number |  | 是 | 纬度 | | | | | | |  | northeast | Object |  | 是 | 东北角经纬度 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | longitude | number |  | 是 | 经度 | |  | latitude | number |  | 是 | 纬度 | | | | | | | | | | |
|  | visible | Boolean | true | 否 | 是否可见 |
|  | zIndex | Number | 1 | 否 | 图层绘制顺序 |
|  | opacity | Number | 1 | 否 | 图层透明度 |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | southwest | Object |  | 是 | 西南角经纬度 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | longitude | number |  | 是 | 经度 | |  | latitude | number |  | 是 | 纬度 | | | | | |
|  | northeast | Object |  | 是 | 东北角经纬度 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | longitude | number |  | 是 | 经度 | |  | latitude | number |  | 是 | 纬度 | | | | | |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | longitude | number |  | 是 | 经度 |
|  | latitude | number |  | 是 | 纬度 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | longitude | number |  | 是 | 经度 |
|  | latitude | number |  | 是 | 纬度 |

---

### wx.saveImageToPhotosAlbum(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.saveImageToPhotosAlbum.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| filePath | string |  | 是 | 图片文件路径，可以是临时文件路径或永久文件路径 (本地路径) ，不支持网络路径 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.previewMedia(Object object)

基础库 2.12.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.previewMedia.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | sources | Array.<Object> |  | 是 | 需要预览的资源列表 |  |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | url | String |  | 是 | 图片或视频的地址 | |  | type | String | image | 否 | 资源的类型，默认为图片 | |  | | 合法值 | 说明 | | --- | --- | | image | 图片 | | video | 视频 | | | | | | |  | poster | string |  | 否 | 视频的封面图片 | | | | | | |
|  | current | number | 0 | 否 | 当前显示的资源序号 |  |
|  | showmenu | boolean | true | 否 | 是否显示长按菜单。 | [2.13.0](../../../framework/compatibility.html) |
|  | referrerPolicy | string | no-referrer | 否 | `origin`: 发送完整的referrer; `no-referrer`: 不发送。格式固定为 `https://servicewechat.com/{appid}/{version}/page-frame.html`，其中 {appid} 为小程序的 appid，{version} 为小程序的版本号，版本号为 0 表示为开发版、体验版以及审核版本，版本号为 devtools 表示为开发者工具，其余为正式版本； | [2.13.0](../../../framework/compatibility.html) |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | url | String |  | 是 | 图片或视频的地址 |
|  | type | String | image | 否 | 资源的类型，默认为图片 |
|  | | 合法值 | 说明 | | --- | --- | | image | 图片 | | video | 视频 | | | | | |
|  | poster | string |  | 否 | 视频的封面图片 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| image | 图片 |
| video | 视频 |

**支持长按识别的码**

| 类型 | 说明 | 最低版本 |
| --- | --- | --- |
| 小程序码 |  |  |
| 微信个人码 | 不支持小游戏 | [2.18.0](../../../framework/compatibility.html) |
| 企业微信个人码 | 不支持小游戏 | [2.18.0](../../../framework/compatibility.html) |
| 普通群码 | 指仅包含微信用户的群，不支持小游戏 | [2.18.0](../../../framework/compatibility.html) |
| 互通群码 | 指既有微信用户也有企业微信用户的群，不支持小游戏 | [2.18.0](../../../framework/compatibility.html) |
| 公众号二维码 | 不支持小游戏 | [2.18.0](../../../framework/compatibility.html) |

---

### wx.previewImage(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.previewImage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| urls | Array.<string> |  | 是 | 需要预览的图片链接列表。[2.2.3](../../../framework/compatibility.html) 起支持云文件ID。 |  |
| showmenu | boolean | true | 否 | 是否显示长按菜单。 | [2.13.0](../../../framework/compatibility.html) |
| current | string | urls 的第一张 | 否 | 当前显示图片的链接 |  |
| referrerPolicy | string | no-referrer | 否 | `origin`: 发送完整的referrer; `no-referrer`: 不发送。格式固定为 `https://servicewechat.com/{appid}/{version}/page-frame.html`，其中 {appid} 为小程序的 appid，{version} 为小程序的版本号，版本号为 0 表示为开发版、体验版以及审核版本，版本号为 devtools 表示为开发者工具，其余为正式版本； | [2.13.0](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**支持长按识别的码**

| 类型 | 说明 | 最低版本 |
| --- | --- | --- |
| 小程序码 |  |  |
| 微信个人码 |  | [2.18.0](../../../framework/compatibility.html) |
| 企业微信个人码 |  | [2.18.0](../../../framework/compatibility.html) |
| 普通群码 | 指仅包含微信用户的群 | [2.18.0](../../../framework/compatibility.html) |
| 互通群码 | 指既有微信用户也有企业微信用户的群 | [2.18.0](../../../framework/compatibility.html) |
| 公众号二维码 |  | [2.18.0](../../../framework/compatibility.html) |

---

### wx.getImageInfo(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.getImageInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| src | string |  | 是 | 图片的路径，支持网络路径、本地路径、代码包路径 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | width | number | 图片原始宽度，单位px。不考虑旋转。 |  |
|  | height | number | 图片原始高度，单位px。不考虑旋转。 |  |
|  | path | string | 图片的本地路径 |  |
|  | orientation | string | [拍照时设备方向](http://sylvana.net/jpegcrop/exif_orientation.html) | [1.9.90](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | up | 默认方向（手机横持拍照），对应 Exif 中的 1。或无 orientation 信息。 | | up-mirrored | 同 up，但镜像翻转，对应 Exif 中的 2 | | down | 旋转180度，对应 Exif 中的 3 | | down-mirrored | 同 down，但镜像翻转，对应 Exif 中的 4 | | left-mirrored | 同 left，但镜像翻转，对应 Exif 中的 5 | | right | 顺时针旋转90度，对应 Exif 中的 6 | | right-mirrored | 同 right，但镜像翻转，对应 Exif 中的 7 | | left | 逆时针旋转90度，对应 Exif 中的 8 | | | | |
|  | type | string | 图片格式 | [1.9.90](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | unknown | 未知格式 | | jpeg | jpeg压缩格式 | | png | png压缩格式 | | gif | gif压缩格式 | | tiff | tiff压缩格式 | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| up | 默认方向（手机横持拍照），对应 Exif 中的 1。或无 orientation 信息。 |
| up-mirrored | 同 up，但镜像翻转，对应 Exif 中的 2 |
| down | 旋转180度，对应 Exif 中的 3 |
| down-mirrored | 同 down，但镜像翻转，对应 Exif 中的 4 |
| left-mirrored | 同 left，但镜像翻转，对应 Exif 中的 5 |
| right | 顺时针旋转90度，对应 Exif 中的 6 |
| right-mirrored | 同 right，但镜像翻转，对应 Exif 中的 7 |
| left | 逆时针旋转90度，对应 Exif 中的 8 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| unknown | 未知格式 |
| jpeg | jpeg压缩格式 |
| png | png压缩格式 |
| gif | gif压缩格式 |
| tiff | tiff压缩格式 |

---

### wx.editImage(Object object)

基础库 2.22.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.editImage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| src | string |  | 是 | 图片路径，图片的路径，支持本地路径、代码包路径 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempFilePath | string | 编辑后图片的临时文件路径 (本地路径) |

---

### wx.cropImage(Object object)

基础库 2.26.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.cropImage.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | src | string |  | 是 | 图片路径，图片的路径，支持本地路径、代码包路径 |
|  | cropScale | string |  | 是 | 裁剪比例 |
|  | | 合法值 | 说明 | | --- | --- | | 16:9 | 宽高比为16比9 | | 9:16 | 宽高比为9比16 | | 4:3 | 宽高比为4比3 | | 3:4 | 宽高比为3比4 | | 5:4 | 宽高比为5比4 | | 4:5 | 宽高比为4比5 | | 1:1 | 宽高比为1比1 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 16:9 | 宽高比为16比9 |
| 9:16 | 宽高比为9比16 |
| 4:3 | 宽高比为4比3 |
| 3:4 | 宽高比为3比4 |
| 5:4 | 宽高比为5比4 |
| 4:5 | 宽高比为4比5 |
| 1:1 | 宽高比为1比1 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempFilePath | string | 编辑后图片的临时文件路径 (本地路径) |

---

### wx.compressImage(Object object)

基础库 2.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.compressImage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| src | string |  | 是 | 图片路径，图片的路径，支持本地路径、代码包路径 |  |
| quality | number | 80 | 否 | 压缩质量，范围0～100，数值越小，质量越低，压缩率越高（仅对jpg有效）。 |  |
| compressedWidth | number |  | 否 | 压缩后图片的宽度，单位为px，若不填写则默认以compressedHeight为准等比缩放。 | [2.26.0](../../../framework/compatibility.html) |
| compressedHeight | number |  | 否 | 压缩后图片的高度，单位为px，若不填写则默认以compressedWidth为准等比缩放 | [2.26.0](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempFilePath | string | 压缩后图片的临时文件路径 (本地路径) |

---

### wx.chooseMessageFile(Object object)

基础库 2.5.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.chooseMessageFile.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | count | number |  | 是 | 最多可以选择的文件个数，可以 0～100 |  |
|  | type | string | 'all' | 否 | 所选的文件的类型 |  |
|  | | 合法值 | 说明 | | --- | --- | | all | 从所有文件选择 | | video | 只能选择视频文件 | | image | 只能选择图片文件 | | file | 可以选择除了图片和视频之外的其它的文件 | | | | | | |
|  | extension | Array.<string> |  | 否 | 根据文件拓展名过滤，仅 type==file 时有效。每一项都不能是空字符串。默认不过滤。 | [2.6.0](../../../framework/compatibility.html) |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| all | 从所有文件选择 |
| video | 只能选择视频文件 |
| image | 只能选择图片文件 |
| file | 可以选择除了图片和视频之外的其它的文件 |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | tempFiles | Array.<Object> | 返回选择的文件的本地临时文件对象数组 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | path | string | 本地临时文件路径 (本地路径) | |  | size | number | 本地临时文件大小，单位 B | |  | name | string | 选择的文件名称 | |  | type | string | 选择的文件类型 | |  | | 合法值 | 说明 | | --- | --- | | video | 选择了视频文件 | | image | 选择了图片文件 | | file | 选择了除图片和视频的文件 | | | | |  | time | number | 选择的文件的会话发送时间，Unix时间戳，工具暂不支持此属性 | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | path | string | 本地临时文件路径 (本地路径) |
|  | size | number | 本地临时文件大小，单位 B |
|  | name | string | 选择的文件名称 |
|  | type | string | 选择的文件类型 |
|  | | 合法值 | 说明 | | --- | --- | | video | 选择了视频文件 | | image | 选择了图片文件 | | file | 选择了除图片和视频的文件 | | | |
|  | time | number | 选择的文件的会话发送时间，Unix时间戳，工具暂不支持此属性 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| video | 选择了视频文件 |
| image | 选择了图片文件 |
| file | 选择了除图片和视频的文件 |

---

### wx.chooseImage(Object object)

从基础库2.21.0开始，本接口停止维护，请使用wx.chooseMedia代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.chooseImage.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | count | number | 9 | 否 | 最多可以选择的图片张数 |
|  | sizeType | Array.<string> | ['original', 'compressed'] | 否 | 所选的图片的尺寸 |
|  | | 合法值 | 说明 | | --- | --- | | original | 原图 | | compressed | 压缩图 | | | | | |
|  | sourceType | Array.<string> | ['album', 'camera'] | 否 | 选择图片的来源 |
|  | | 合法值 | 说明 | | --- | --- | | album | 从相册选图 | | camera | 使用相机 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| original | 原图 |
| compressed | 压缩图 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| album | 从相册选图 |
| camera | 使用相机 |

**Object object**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | tempFilePaths | Array.<string> | 图片的本地临时文件路径列表 (本地路径) |  |
|  | tempFiles | Array.<Object> | 图片的本地临时文件列表 | [1.2.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | path | string | 本地临时文件路径 (本地路径) | |  | size | number | 本地临时文件大小，单位 B | | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | path | string | 本地临时文件路径 (本地路径) |
|  | size | number | 本地临时文件大小，单位 B |

---

### wx.saveVideoToPhotosAlbum(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.saveVideoToPhotosAlbum.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| filePath | string |  | 是 | 视频文件路径，可以是临时文件路径也可以是永久文件路径 (本地路径) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.openVideoEditor(Object object)

基础库 2.12.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.openVideoEditor.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| filePath | string |  | 是 | 视频源的路径，只支持本地路径 |  |
| minDuration | string |  | 是 | 视频裁剪的最小长度 | [2.16.1](../../../framework/compatibility.html) |
| maxDuration | string |  | 是 | 视频裁剪的最大长度 | [2.16.1](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| duration | number | 剪辑后生成的视频文件的时长，单位毫秒（ms） |
| size | number | 剪辑后生成的视频文件大小，单位字节数（byte） |
| tempFilePath | string | 编辑后生成的视频文件的临时路径 |
| tempThumbPath | string | 编辑后生成的缩略图文件的临时路径 |

---

### wx.getVideoInfo(Object object)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.getVideoInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| src | string |  | 是 | 视频文件路径，可以是临时文件路径也可以是永久文件路径 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | orientation | string | 画面方向 |
|  | | 合法值 | 说明 | | --- | --- | | up | 默认 | | down | 180度旋转 | | left | 逆时针旋转90度 | | right | 顺时针旋转90度 | | up-mirrored | 同up，但水平翻转 | | down-mirrored | 同down，但水平翻转 | | left-mirrored | 同left，但垂直翻转 | | right-mirrored | 同right，但垂直翻转 | | | |
|  | type | string | 视频格式 |
|  | duration | number | 视频长度 |
|  | size | number | 视频大小，单位 kB |
|  | height | number | 视频的长，单位 px |
|  | width | number | 视频的宽，单位 px |
|  | fps | number | 视频帧率 |
|  | bitrate | number | 视频码率，单位 kbps |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| up | 默认 |
| down | 180度旋转 |
| left | 逆时针旋转90度 |
| right | 顺时针旋转90度 |
| up-mirrored | 同up，但水平翻转 |
| down-mirrored | 同down，但水平翻转 |
| left-mirrored | 同left，但垂直翻转 |
| right-mirrored | 同right，但垂直翻转 |

---

### VideoContext wx.createVideoContext(string id, Object this)

小程序插件：支持，需要小程序基础库版本不低于1.9.6

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.createVideoContext.html

---

### wx.compressVideo(Object object)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.compressVideo.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | src | string |  | 是 | 视频文件路径，可以是临时文件路径也可以是永久文件路径 |
|  | quality | string |  | 否 | 压缩质量 |
|  | | 合法值 | 说明 | | --- | --- | | low | 低 | | medium | 中 | | high | 高 | | | | | |
|  | bitrate | number |  | 是 | 码率，单位 kbps |
|  | fps | number |  | 是 | 帧率 |
|  | resolution | number |  | 是 | 相对于原视频的分辨率比例，取值范围(0, 1] |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| low | 低 |
| medium | 中 |
| high | 高 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempFilePath | string | 压缩后的临时文件地址 |
| size | number | 压缩后的大小，单位 kB |

---

### wx.chooseVideo(Object object)

从基础库2.21.0开始，本接口停止维护，请使用wx.chooseMedia代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.chooseVideo.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | sourceType | Array.<string> | ['album', 'camera'] | 否 | 视频选择的来源 |  |
|  | | 合法值 | 说明 | | --- | --- | | album | 从相册选择视频 | | camera | 使用相机拍摄视频 | | | | | | |
|  | compressed | boolean | true | 否 | 是否压缩所选择的视频文件 | [1.6.0](../../../framework/compatibility.html) |
|  | maxDuration | number | 60 | 否 | 拍摄视频最长拍摄时间，单位秒 |  |
|  | camera | string | 'back' | 否 | 默认拉起的是前置或者后置摄像头。部分 Android 手机下由于系统 ROM 不支持无法生效 |  |
|  | | 合法值 | 说明 | | --- | --- | | back | 默认拉起后置摄像头 | | front | 默认拉起前置摄像头 | | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| album | 从相册选择视频 |
| camera | 使用相机拍摄视频 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| back | 默认拉起后置摄像头 |
| front | 默认拉起前置摄像头 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempFilePath | string | 选定视频的临时文件路径 (本地路径) |
| duration | number | 选定视频的时间长度 |
| size | number | 选定视频的数据量大小 |
| height | number | 返回选定视频的高度 |
| width | number | 返回选定视频的宽度 |

---

### wx.chooseMedia(Object object)

基础库 2.10.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.chooseMedia.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | count | number | 9 | 否 | 最多可以选择的文件个数，基础库2.25.0前，最多可支持9个文件，2.25.0及以后最多可支持20个文件 |
|  | mediaType | Array.<string> | ['image', 'video'] | 否 | 文件类型 |
|  | | 合法值 | 说明 | | --- | --- | | image | 只能拍摄图片或从相册选择图片 | | video | 只能拍摄视频或从相册选择视频 | | mix | 可同时选择图片和视频 | | | | | |
|  | sourceType | Array.<string> | ['album', 'camera'] | 否 | 图片和视频选择的来源 |
|  | | 合法值 | 说明 | | --- | --- | | album | 从相册选择 | | camera | 使用相机拍摄 | | | | | |
|  | maxDuration | number | 10 | 否 | 拍摄视频最长拍摄时间，单位秒。时间范围为 3s 至 60s 之间。不限制相册。 |
|  | sizeType | Array.<string> | ['original', 'compressed'] | 否 | 是否压缩所选文件，基础库2.25.0前仅对 mediaType 为 image 时有效，2.25.0及以后对全量 mediaType 有效 |
|  | camera | string | 'back' | 否 | 仅在 sourceType 为 camera 时生效，使用前置或后置摄像头 |
|  | | 合法值 | 说明 | | --- | --- | | back | 使用后置摄像头 | | front | 使用前置摄像头 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| image | 只能拍摄图片或从相册选择图片 |
| video | 只能拍摄视频或从相册选择视频 |
| mix | 可同时选择图片和视频 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| album | 从相册选择 |
| camera | 使用相机拍摄 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| back | 使用后置摄像头 |
| front | 使用前置摄像头 |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | tempFiles | Array.<Object> | 本地临时文件列表 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | tempFilePath | string | 本地临时文件路径 (本地路径) | |  | size | number | 本地临时文件大小，单位 B | |  | duration | number | 视频的时间长度 | |  | height | number | 视频的高度 | |  | width | number | 视频的宽度 | |  | thumbTempFilePath | string | 视频缩略图临时文件路径 | |  | fileType | string | 文件类型 | |  | | 合法值 | 说明 | | --- | --- | | image | 图片 | | video | 视频 | | | | | | |
|  | type | string | 文件类型，有效值有 image 、video、mix |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | tempFilePath | string | 本地临时文件路径 (本地路径) |
|  | size | number | 本地临时文件大小，单位 B |
|  | duration | number | 视频的时间长度 |
|  | height | number | 视频的高度 |
|  | width | number | 视频的宽度 |
|  | thumbTempFilePath | string | 视频缩略图临时文件路径 |
|  | fileType | string | 文件类型 |
|  | | 合法值 | 说明 | | --- | --- | | image | 图片 | | video | 视频 | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| image | 图片 |
| video | 视频 |

---

### wx.checkDeviceSupportHevc(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.checkDeviceSupportHevc.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| supportHevc | Boolean | 设备是否支持 H.265 编码 |

---

### VideoContext

相关文档:video 组件

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.html

---

### VideoContext.exitBackgroundPlayback()

基础库 2.14.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.exitBackgroundPlayback.html

---

### VideoContext.exitCasting()

基础库 2.32.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.exitCasting.html

---

### VideoContext.exitFullScreen()

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.exitFullScreen.html

---

### VideoContext.exitPictureInPicture(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.exitPictureInPicture.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### VideoContext.hideStatusBar()

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.hideStatusBar.html

---

### VideoContext.pause()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.pause.html

---

### VideoContext.play()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.play.html

---

### VideoContext.playbackRate(number rate)

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.playbackRate.html

---

### VideoContext.reconnectCasting()

基础库 2.32.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.reconnectCasting.html

---

### VideoContext.requestBackgroundPlayback()

基础库 2.14.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.requestBackgroundPlayback.html

---

### VideoContext.requestFullScreen(Object object)

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.requestFullScreen.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | direction | number |  | 否 | 设置全屏时视频的方向，不指定则根据宽高比自动判断。 | [1.7.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 正常竖向 | | 90 | 屏幕逆时针90度 | | -90 | 屏幕顺时针90度 | | | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 0 | 正常竖向 |
| 90 | 屏幕逆时针90度 |
| -90 | 屏幕顺时针90度 |

---

### VideoContext.seek(number position)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.seek.html

---

### VideoContext.sendDanmu(Object data)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.sendDanmu.html

**Object data**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| text | string |  | 是 | 弹幕文字 |
| color | string |  | 否 | 弹幕颜色 |

---

### VideoContext.showStatusBar()

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.showStatusBar.html

---

### VideoContext.startCasting()

基础库 2.32.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.startCasting.html

---

### VideoContext.stop()

基础库 1.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.stop.html

---

### VideoContext.switchCasting()

基础库 2.32.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.switchCasting.html

---

### wx.stopVoice(Object object)

从基础库1.6.0开始，本接口停止维护，请使用wx.createInnerAudioContext代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.stopVoice.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.setInnerAudioOption(Object object)

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.setInnerAudioOption.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| mixWithOther | boolean | true | 否 | 是否与其他音频混播，设置为 true 之后，不会终止其他应用或微信内的音乐 |
| obeyMuteSwitch | boolean | true | 否 | （仅在 iOS 生效）是否遵循静音开关，设置为 false 之后，即使是在静音模式下，也能播放声音 |
| speakerOn | boolean | true | 否 | true 代表用扬声器播放，false 代表听筒播放，默认值为 true。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.playVoice(Object object)

从基础库1.6.0开始，本接口停止维护，请使用wx.createInnerAudioContext代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.playVoice.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| filePath | string |  | 是 | 需要播放的语音文件的文件路径 (本地路径) |  |
| duration | number | 60 | 否 | 指定播放时长，到达指定的播放时长后会自动停止播放，单位：秒 | [1.6.0](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### wx.pauseVoice(Object object)

从基础库1.6.0开始，本接口停止维护，请使用wx.createInnerAudioContext代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.pauseVoice.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.getAvailableAudioSources(Object object)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.getAvailableAudioSources.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | audioSources | Array.<string> | 支持的音频输入源列表，可在 [RecorderManager.start()](../recorder/RecorderManager.start.html) 接口中使用。返回值定义参考 https://developer.android.com/reference/kotlin/android/media/MediaRecorder.AudioSource |
|  | | 合法值 | 说明 | | --- | --- | | auto | 自动设置，默认使用手机麦克风，插上耳麦后自动切换使用耳机麦克风，所有平台适用 | | buildInMic | 手机麦克风，仅限 iOS | | headsetMic | 耳机麦克风，仅限 iOS | | mic | 麦克风（没插耳麦时是手机麦克风，插耳麦时是耳机麦克风），仅限 Android | | camcorder | 同 mic，适用于录制音视频内容，仅限 Android | | voice\_communication | 同 mic，适用于实时沟通，仅限 Android | | voice\_recognition | 同 mic，适用于语音识别，仅限 Android | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| auto | 自动设置，默认使用手机麦克风，插上耳麦后自动切换使用耳机麦克风，所有平台适用 |
| buildInMic | 手机麦克风，仅限 iOS |
| headsetMic | 耳机麦克风，仅限 iOS |
| mic | 麦克风（没插耳麦时是手机麦克风，插耳麦时是耳机麦克风），仅限 Android |
| camcorder | 同 mic，适用于录制音视频内容，仅限 Android |
| voice\_communication | 同 mic，适用于实时沟通，仅限 Android |
| voice\_recognition | 同 mic，适用于语音识别，仅限 Android |

---

### WebAudioContext wx.createWebAudioContext()

基础库 2.19.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.createWebAudioContext.html

---

### MediaAudioPlayer wx.createMediaAudioPlayer()

基础库 2.13.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.createMediaAudioPlayer.html

---

### InnerAudioContext wx.createInnerAudioContext(Object object)

基础库 1.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.createInnerAudioContext.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| useWebAudioImplement | boolean | false | 否 | 是否使用 WebAudio 作为底层音频驱动，默认关闭。对于短音频、播放频繁的音频建议开启此选项，开启后将获得更优的性能表现。由于开启此选项后也会带来一定的内存增长，因此对于长音频建议关闭此选项。 | [2.19.0](../../../framework/compatibility.html) |

---

### AudioContext wx.createAudioContext(string id, Object this)

从基础库1.6.0开始，本接口停止维护，请使用wx.createInnerAudioContext代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.createAudioContext.html

---

### AudioBuffer

基础库 2.19.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioBuffer.html

---

### AudioBuffer.copyFromChannel()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioBuffer.copyFromChannel.html

---

### AudioBuffer.copyToChannel(Float32Array source, number channelNumber, number startInChannel)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioBuffer.copyToChannel.html

---

### Float32Array AudioBuffer.getChannelData(number channel)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioBuffer.getChannelData.html

---

### AudioContext

AudioContext实例，可通过wx.createAudioContext获取。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioContext.html

---

### AudioContext.pause()

从基础库1.6.0开始，本接口停止维护，请使用wx.createInnerAudioContext代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioContext.pause.html

---

### AudioContext.play()

从基础库1.6.0开始，本接口停止维护，请使用wx.createInnerAudioContext代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioContext.play.html

---

### AudioContext.seek(number position)

从基础库1.6.0开始，本接口停止维护，请使用wx.createInnerAudioContext代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioContext.seek.html

---

### AudioContext.setSrc(string src)

从基础库1.6.0开始，本接口停止维护，请使用wx.createInnerAudioContext代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioContext.setSrc.html

---

### AudioListener

空间音频监听器，代表在一个音频场景内唯一的位置和方向信息。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioListener.html

---

### AudioParam

基础库 2.19.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioParam.html

---

### BufferSourceNode

音频源节点，通过WebAudioContext.createBufferSource方法获得。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/BufferSourceNode.html

---

### BufferSourceNode.connect(AudioNode|AudioParam destination)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/BufferSourceNode.connect.html

---

### BufferSourceNode.disconnect()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/BufferSourceNode.disconnect.html

---

### BufferSourceNode.start(number when, number offset, number duration)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/BufferSourceNode.start.html

---

### BufferSourceNode.stop(number when)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/BufferSourceNode.stop.html

---

### InnerAudioContext

InnerAudioContext 实例，可通过wx.createInnerAudioContext接口获取实例。注意，音频播放过程中，可能被系统中断，可通过wx.onAudioInterruptionBegin、wx.onAudioInterruptionEnd事件来处理这种情况。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.html

**支持格式**

| 格式 | iOS | Android |
| --- | --- | --- |
| flac | x | √ |
| m4a | √ | √ |
| ogg | x | √ |
| ape | x | √ |
| amr | x | √ |
| wma | x | √ |
| wav | √ | √ |
| mp3 | √ | √ |
| mp4 | x | √ |
| aac | √ | √ |
| aiff | √ | x |
| caf | √ | x |

---

### InnerAudioContext.destroy()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.destroy.html

---

### InnerAudioContext.offCanplay(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.offCanplay.html

---

### InnerAudioContext.offEnded(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.offEnded.html

---

### InnerAudioContext.offError(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.offError.html

---

### InnerAudioContext.offPause(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.offPause.html

---

### InnerAudioContext.offPlay(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.offPlay.html

---

### InnerAudioContext.offSeeked(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.offSeeked.html

---

### InnerAudioContext.offSeeking(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.offSeeking.html

---

### InnerAudioContext.offStop(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.offStop.html

---

### InnerAudioContext.offTimeUpdate(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.offTimeUpdate.html

---

### InnerAudioContext.offWaiting(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.offWaiting.html

---

### InnerAudioContext.onCanplay(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.onCanplay.html

---

### InnerAudioContext.onEnded(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.onEnded.html

---

### InnerAudioContext.onError(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.onError.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | errMsg | string |  |
|  | errCode | number |  |
|  | | 合法值 | 说明 | | --- | --- | | 10001 | 系统错误 | | 10002 | 网络错误 | | 10003 | 文件错误 | | 10004 | 格式错误 | | -1 | 未知错误 | | | |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| 10001 | 系统错误 |
| 10002 | 网络错误 |
| 10003 | 文件错误 |
| 10004 | 格式错误 |
| -1 | 未知错误 |

---

### InnerAudioContext.onPause(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.onPause.html

---

### InnerAudioContext.onPlay(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.onPlay.html

---

### InnerAudioContext.onSeeked(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.onSeeked.html

---

### InnerAudioContext.onSeeking(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.onSeeking.html

---

### InnerAudioContext.onStop(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.onStop.html

---

### InnerAudioContext.onTimeUpdate(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.onTimeUpdate.html

---

### InnerAudioContext.onWaiting(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.onWaiting.html

---

### InnerAudioContext.pause()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.pause.html

---

### InnerAudioContext.play()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.play.html

---

### InnerAudioContext.seek(number position)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.seek.html

---

### InnerAudioContext.stop()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.stop.html

---

### MediaAudioPlayer

MediaAudioPlayer 实例，可通过wx.createMediaAudioPlayer接口获取实例。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/MediaAudioPlayer.html

---

### Promise MediaAudioPlayer.addAudioSource(VideoDecoder source)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/MediaAudioPlayer.addAudioSource.html

---

### Promise MediaAudioPlayer.destroy()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/MediaAudioPlayer.destroy.html

---

### Promise MediaAudioPlayer.removeAudioSource(VideoDecoder source)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/MediaAudioPlayer.removeAudioSource.html

---

### Promise MediaAudioPlayer.start()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/MediaAudioPlayer.start.html

---

### Promise MediaAudioPlayer.stop()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/MediaAudioPlayer.stop.html

---

### WebAudioContext

基础库 2.19.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.html

---

### Promise WebAudioContext.close()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.close.html

---

### AnalyserNode WebAudioContext.createAnalyser()

基础库 2.22.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createAnalyser.html

---

### BiquadFilterNode WebAudioContext.createBiquadFilter()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createBiquadFilter.html

---

### AudioBuffer WebAudioContext.createBuffer(number numOfChannels, number length, number sampleRate)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createBuffer.html

---

### BufferSourceNode WebAudioContext.createBufferSource()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createBufferSource.html

---

### ChannelMergerNode WebAudioContext.createChannelMerger(number numberOfInputs)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createChannelMerger.html

---

### ChannelSplitterNode WebAudioContext.createChannelSplitter(number numberOfOutputs)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createChannelSplitter.html

---

### ConstantSourceNode WebAudioContext.createConstantSource()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createConstantSource.html

---

### DelayNode WebAudioContext.createDelay(number maxDelayTime)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createDelay.html

---

### DynamicsCompressorNode WebAudioContext.createDynamicsCompressor()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createDynamicsCompressor.html

---

### GainNode WebAudioContext.createGain()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createGain.html

---

### IIRFilterNode WebAudioContext.createIIRFilter(Array.<number> feedforward, Array.<number> feedback)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createIIRFilter.html

---

### OscillatorNode WebAudioContext.createOscillator()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createOscillator.html

---

### PannerNode WebAudioContext.createPanner()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createPanner.html

---

### PeriodicWaveNode WebAudioContext.createPeriodicWave(Float32Array real, Float32Array imag, object constraints)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createPeriodicWave.html

**object constraints**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| disableNormalization | boolean |  | 否 | 如果指定为true则禁用标准化，默认为false |

---

### ScriptProcessorNode WebAudioContext.createScriptProcessor(number bufferSize, number numberOfInputChannels, number numberOfOutputChannels)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createScriptProcessor.html

---

### WaveShaperNode WebAudioContext.createWaveShaper()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createWaveShaper.html

---

### AudioBuffer WebAudioContext.decodeAudioData(ArrayBuffer audioData, function successCallback, function errorCallback)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.decodeAudioData.html

---

### Promise WebAudioContext.resume()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.resume.html

---

### Promise WebAudioContext.suspend()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.suspend.html

---

### WebAudioContextNode

一类音频处理模块，不同的Node具备不同的功能，如GainNode(音量调整)等。一个WebAudioContextNode可以通过上下文来创建。 目前已经支持以下Node： IIRFilterNode WaveShaperNode ConstantSourceNode ChannelMergerNode OscillatorNode GainNode BiquadFilterNode PeriodicWaveNode BufferSourceNode ChannelSplitterNode ChannelMergerNode DelayNode DynamicsCompressorNode ScriptProcessorNode PannerNode AnalyserNode

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContextNode.html

---

### wx.stopBackgroundAudio(Object object)

从基础库1.2.0开始，本接口停止维护，请使用wx.getBackgroundAudioManager代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.stopBackgroundAudio.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.seekBackgroundAudio(Object object)

从基础库1.2.0开始，本接口停止维护，请使用wx.getBackgroundAudioManager代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.seekBackgroundAudio.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| position | number |  | 是 | 音乐位置，单位：秒 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.playBackgroundAudio(Object object)

从基础库1.2.0开始，本接口停止维护，请使用wx.getBackgroundAudioManager代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.playBackgroundAudio.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| dataUrl | string |  | 是 | 音乐链接，目前支持的格式有 m4a, aac, mp3, wav |
| title | string |  | 否 | 音乐标题 |
| coverImgUrl | string |  | 否 | 封面URL |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.pauseBackgroundAudio(Object object)

从基础库1.2.0开始，本接口停止维护，请使用wx.getBackgroundAudioManager代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.pauseBackgroundAudio.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.onBackgroundAudioStop(function listener)

从基础库1.2.0开始，本接口停止维护，请使用wx.getBackgroundAudioManager代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.onBackgroundAudioStop.html

---

### wx.onBackgroundAudioPlay(function listener)

从基础库1.2.0开始，本接口停止维护，请使用wx.getBackgroundAudioManager代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.onBackgroundAudioPlay.html

---

### wx.onBackgroundAudioPause(function listener)

从基础库1.2.0开始，本接口停止维护，请使用wx.getBackgroundAudioManager代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.onBackgroundAudioPause.html

---

### wx.getBackgroundAudioPlayerState(Object object)

从基础库1.2.0开始，本接口停止维护，请使用wx.getBackgroundAudioManager代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.getBackgroundAudioPlayerState.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | duration | number | 选定音频的长度（单位：s），只有在音乐播放中时返回 |
|  | currentPosition | number | 选定音频的播放位置（单位：s），只有在音乐播放中时返回 |
|  | status | number | 播放状态 |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 暂停中 | | 1 | 播放中 | | 2 | 没有音乐播放 | | | |
|  | downloadPercent | number | 音频的下载进度百分比，只有在音乐播放中时返回 |
|  | dataUrl | string | 歌曲数据链接，只有在音乐播放中时返回 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 0 | 暂停中 |
| 1 | 播放中 |
| 2 | 没有音乐播放 |

---

### BackgroundAudioManager wx.getBackgroundAudioManager()

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.getBackgroundAudioManager.html

---

### BackgroundAudioManager

BackgroundAudioManager 实例，可通过wx.getBackgroundAudioManager获取。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/BackgroundAudioManager.html

---

### BackgroundAudioManager.onCanplay(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/BackgroundAudioManager.onCanplay.html

---

### BackgroundAudioManager.onEnded(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/BackgroundAudioManager.onEnded.html

---

### BackgroundAudioManager.onError(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/BackgroundAudioManager.onError.html

---

### BackgroundAudioManager.onNext(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/BackgroundAudioManager.onNext.html

---

### BackgroundAudioManager.onPause(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/BackgroundAudioManager.onPause.html

---

### BackgroundAudioManager.onPlay(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/BackgroundAudioManager.onPlay.html

---

### BackgroundAudioManager.onPrev(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/BackgroundAudioManager.onPrev.html

---

### BackgroundAudioManager.onSeeked(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/BackgroundAudioManager.onSeeked.html

---

### BackgroundAudioManager.onSeeking(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/BackgroundAudioManager.onSeeking.html

---

### BackgroundAudioManager.onStop(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/BackgroundAudioManager.onStop.html

---

### BackgroundAudioManager.onTimeUpdate(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/BackgroundAudioManager.onTimeUpdate.html

---

### BackgroundAudioManager.onWaiting(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/BackgroundAudioManager.onWaiting.html

---

### BackgroundAudioManager.pause()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/BackgroundAudioManager.pause.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 10001 |  | 系统错误 |
| 10002 |  | 网络错误 |
| 10003 |  | 文件错误，请检查是否responseheader是否缺少Content-Length |
| 10004 |  | 格式错误 |
| -1 |  | 未知错误 |

---

### BackgroundAudioManager.play()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/BackgroundAudioManager.play.html

---

### BackgroundAudioManager.seek(number currentTime)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/BackgroundAudioManager.seek.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 10001 |  | 系统错误 |
| 10002 |  | 网络错误 |
| 10003 |  | 文件错误，请检查是否responseheader是否缺少Content-Length |
| 10004 |  | 格式错误 |
| -1 |  | 未知错误 |

---

### BackgroundAudioManager.stop()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/BackgroundAudioManager.stop.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 10001 |  | 系统错误 |
| 10002 |  | 网络错误 |
| 10003 |  | 文件错误，请检查是否responseheader是否缺少Content-Length |
| 10004 |  | 格式错误 |
| -1 |  | 未知错误 |

---

### LivePusherContext wx.createLivePusherContext()

基础库 1.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/wx.createLivePusherContext.html

---

### LivePlayerContext wx.createLivePlayerContext(string id, Object this)

基础库 1.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/wx.createLivePlayerContext.html

---

### LivePlayerContext

相关文档:live-player 组件

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.html

---

### LivePlayerContext.exitBackgroundPlayback()

基础库 2.14.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.exitBackgroundPlayback.html

---

### LivePlayerContext.exitCasting(Object object)

基础库 2.32.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.exitCasting.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePlayerContext.exitFullScreen(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.exitFullScreen.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePlayerContext.exitPictureInPicture(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.exitPictureInPicture.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePlayerContext.mute(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.mute.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePlayerContext.pause(Object object)

基础库 1.9.90 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.pause.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePlayerContext.play(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.play.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePlayerContext.reconnectCasting(Object object)

基础库 2.32.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.reconnectCasting.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePlayerContext.requestBackgroundPlayback()

基础库 2.14.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.requestBackgroundPlayback.html

---

### LivePlayerContext.requestFullScreen(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.requestFullScreen.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | direction | number | 0 | 否 | 设置全屏时的方向 |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 正常竖向 | | 90 | 屏幕逆时针90度 | | -90 | 屏幕顺时针90度 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 0 | 正常竖向 |
| 90 | 屏幕逆时针90度 |
| -90 | 屏幕顺时针90度 |

---

### LivePlayerContext.resume(Object object)

基础库 1.9.90 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.resume.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePlayerContext.snapshot(Object object)

基础库 2.7.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.snapshot.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | quality | string | raw | 否 | 图片的质量 | [2.10.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | raw | 原图 | | compressed | 压缩图 | | | | | | |
|  | sourceType | string | stream | 否 | 截取的源类型 | [2.25.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | stream | 截取视频源 | | view | 截取渲染后的画面 | | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| raw | 原图 |
| compressed | 压缩图 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| stream | 截取视频源 |
| view | 截取渲染后的画面 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempImagePath | string | 图片文件的临时路径 (本地路径) |
| width | string | 图片的宽度 |
| height | string | 图片的高度 |

---

### LivePlayerContext.startCasting(Object object)

基础库 2.32.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.startCasting.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePlayerContext.stop(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.stop.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePlayerContext.switchCasting(Object object)

基础库 2.32.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.switchCasting.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext

相关文档:live-pusher 组件

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.html

---

### LivePusherContext.applyBlusherStickMakeup(Object object)

基础库 2.14.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.applyBlusherStickMakeup.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| alpha | number |  | 是 | 上色程度 0-1 |
| path | string |  | 是 | 左腮红资源路径 |
| blendMode | string |  | 是 |  |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.applyEyeBrowMakeup(Object object)

基础库 2.14.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.applyEyeBrowMakeup.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| alpha | number |  | 是 | 上色程度 0-1 |
| blendMode | string |  | 是 |  |
| shrinkRate | number |  | 是 |  |
| path | string |  | 是 |  |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.applyEyeShadowMakeup(Object object)

基础库 2.14.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.applyEyeShadowMakeup.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| alpha | number |  | 是 | 上色程度 0-1 |
| path | string |  | 是 | 眼影资源路径 |
| blendMode | string |  | 是 |  |
| shimmerPosition | string |  | 否 | 细致效果图片资源路径 |
| shimmerPositionMD5 | string |  | 否 | 细致效果图片资源 md5 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.applyFaceContourMakeup(Object object)

基础库 2.14.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.applyFaceContourMakeup.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| alpha | number |  | 是 |  |
| path | string |  | 是 | 高光资源路径 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.applyFilter(Object object)

基础库 2.14.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.applyFilter.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| path | string |  | 是 | 滤镜资源路径 |
| alpha | number |  | 是 | 滤镜效果透明度，范围是 0-1 |
| md5 | string |  | 否 | 滤镜资源 md5 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.applyLipStickMakeup(Object object)

基础库 2.14.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.applyLipStickMakeup.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| alpha | number |  | 是 | 上色程度 0-1 |
| blendMode | string |  | 是 |  |
| path | string |  | 是 |  |
| faceModel | string |  | 是 |  |
| shimmerType | string |  | 是 |  |
| shimmerPath | string |  | 是 |  |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.applySticker(Object object)

基础库 2.14.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.applySticker.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | type | string |  | 是 | 贴纸类型 |
|  | stickers | Array.<Object> |  | 是 | 贴纸类型 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | title | string |  | 是 | 贴纸名称 | |  | path | string |  | 是 | 贴纸资源路径。资源必须为一个资源文件夹路径或一个压缩包路径，文件夹或压缩包内的贴纸资源必须按照 `{title}_{index}.{ext}` 格式命名。其中 `{title}` 为贴纸名称；`{index}` 为帧序号，从0开始；`{ext}` 为拓展名。 | |  | len | number |  | 是 | 贴纸帧数 | |  | id | string |  | 否 | 贴纸ID | |  | pos | Array.<string> |  | 否 | 贴纸位置，格式为 [x1,y1,x2,y2] 。当 `type` 为 `'2D'` 或 `'front'` 时必填。仅 2D 贴纸和前景贴纸有效 | |  | md5 | string |  | 否 | 贴纸资源 md5 | |  | active | number | -1 | 否 | 贴纸触发动作 | |  | | 合法值 | 说明 | | --- | --- | | -1 | 循环播放 | | 10 | 张嘴 | | 11 | 噘嘴/kiss | | 12 | 眨/闭左眼 | | 13 | 眨/闭右眼 | | 14 | 眨/闭眼 | | 15 | 挑眉毛 | | 16 | 左右摇头 | | 17 | 上下点头 | | 100 | 比心 | | 101 | 张开手掌 | | 102 | 剪刀手/比耶/胜利 | | 103 | 握拳 | | 104 | 数字1 | | 105 | 我爱你 | | 106 | 点赞 | | 107 | OK | | 108 | Rock&Roll | | 109 | 数字6 | | 110 | 数字8 | | 111 | 暂不支持（留空） | | 112 | 双手抱拳/恭喜发财 | | | | | | |  | segtype | number | 0 | 否 | 背景贴纸展示位置。仅背景贴纸有效 | |  | | 合法值 | 说明 | | --- | --- | | 0 | 背景贴纸 | | 1 | 只在人像区域显示的贴纸 | | | | | | | | | | |
|  | templateTransSet | Object |  | 否 |  |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | title | string |  | 是 | 贴纸名称 |
|  | path | string |  | 是 | 贴纸资源路径。资源必须为一个资源文件夹路径或一个压缩包路径，文件夹或压缩包内的贴纸资源必须按照 `{title}_{index}.{ext}` 格式命名。其中 `{title}` 为贴纸名称；`{index}` 为帧序号，从0开始；`{ext}` 为拓展名。 |
|  | len | number |  | 是 | 贴纸帧数 |
|  | id | string |  | 否 | 贴纸ID |
|  | pos | Array.<string> |  | 否 | 贴纸位置，格式为 [x1,y1,x2,y2] 。当 `type` 为 `'2D'` 或 `'front'` 时必填。仅 2D 贴纸和前景贴纸有效 |
|  | md5 | string |  | 否 | 贴纸资源 md5 |
|  | active | number | -1 | 否 | 贴纸触发动作 |
|  | | 合法值 | 说明 | | --- | --- | | -1 | 循环播放 | | 10 | 张嘴 | | 11 | 噘嘴/kiss | | 12 | 眨/闭左眼 | | 13 | 眨/闭右眼 | | 14 | 眨/闭眼 | | 15 | 挑眉毛 | | 16 | 左右摇头 | | 17 | 上下点头 | | 100 | 比心 | | 101 | 张开手掌 | | 102 | 剪刀手/比耶/胜利 | | 103 | 握拳 | | 104 | 数字1 | | 105 | 我爱你 | | 106 | 点赞 | | 107 | OK | | 108 | Rock&Roll | | 109 | 数字6 | | 110 | 数字8 | | 111 | 暂不支持（留空） | | 112 | 双手抱拳/恭喜发财 | | | | | |
|  | segtype | number | 0 | 否 | 背景贴纸展示位置。仅背景贴纸有效 |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 背景贴纸 | | 1 | 只在人像区域显示的贴纸 | | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| -1 | 循环播放 |
| 10 | 张嘴 |
| 11 | 噘嘴/kiss |
| 12 | 眨/闭左眼 |
| 13 | 眨/闭右眼 |
| 14 | 眨/闭眼 |
| 15 | 挑眉毛 |
| 16 | 左右摇头 |
| 17 | 上下点头 |
| 100 | 比心 |
| 101 | 张开手掌 |
| 102 | 剪刀手/比耶/胜利 |
| 103 | 握拳 |
| 104 | 数字1 |
| 105 | 我爱你 |
| 106 | 点赞 |
| 107 | OK |
| 108 | Rock&Roll |
| 109 | 数字6 |
| 110 | 数字8 |
| 111 | 暂不支持（留空） |
| 112 | 双手抱拳/恭喜发财 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 0 | 背景贴纸 |
| 1 | 只在人像区域显示的贴纸 |

---

### LivePusherContext.clearFilters(Object object)

基础库 2.14.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.clearFilters.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.clearMakeups(Object object)

基础库 2.14.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.clearMakeups.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.clearStickers(Object object)

基础库 2.14.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.clearStickers.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.createOffscreenCanvas(object options)

基础库 2.29.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.createOffscreenCanvas.html

---

### LivePusherContext.exitPictureInPicture(Object object)

基础库 2.25.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.exitPictureInPicture.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.getMaxZoom(Object object)

基础库 2.31.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.getMaxZoom.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| maxZoom | string | 最大放缩级别 |

---

### LivePusherContext.onCustomRendererEvent(string event, function|function callback)

基础库 2.29.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.onCustomRendererEvent.html

**string event**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| frame | 采集到视频帧后触发 |  |
| update | 推流尺寸变更时触发 |  |

**function|function callback**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 推流宽度 |
| height | number | 推流高度 |

---

### LivePusherContext.pause(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.pause.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.pauseBGM(Object object)

基础库 2.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.pauseBGM.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.playBGM(Object object)

基础库 2.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.playBGM.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| url | string |  | 是 | 加入背景混音的资源地址 |  |
| startTimeMs | number | 0 | 否 | BGM开始播时间点，单位ms，若入参为负或超过文件长度，则默认从文件开头进行播放 | [2.31.0](../../../framework/compatibility.html) |
| endTimeMs | number | 0 | 否 | BGM结束播放时间点，单位ms，0代表播放至文件结尾，若入参为负或超过文件长度，则默认播放至文件结尾 | [2.31.0](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### LivePusherContext.resume(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.resume.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.resumeBGM(Object object)

基础库 2.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.resumeBGM.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.sendMessage(Object object)

基础库 2.10.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.sendMessage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| msg | string |  | 是 | SEI消息 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.setBGMVolume(Object object)

基础库 2.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.setBGMVolume.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| volume | string |  | 是 | 音量大小，范围是 0-1 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.setMICVolume(Object object)

基础库 2.10.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.setMICVolume.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| volume | number |  | 是 | 音量大小，范围是 0.0-1.0 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.setZoom(Object object)

基础库 2.31.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.setZoom.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| zoom | number |  | 是 | 缩放级别，范围[1, maxZoom]。zoom 可取小数，精确到小数后一位。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.snapshot(Object object)

基础库 1.9.90 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.snapshot.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | quality | string | raw | 否 | 图片的质量 | [2.10.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | raw | 原图 | | compressed | 压缩图 | | | | | | |
|  | sourceType | string | stream | 否 | 截取的源类型 | [2.25.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | stream | 截取视频源 | | view | 截取渲染后的画面 | | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| raw | 原图 |
| compressed | 压缩图 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| stream | 截取视频源 |
| view | 截取渲染后的画面 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempImagePath | string | 图片文件的临时路径 |
| width | string | 图片的宽度 |
| height | string | 图片的高度 |

---

### LivePusherContext.start(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.start.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.startPreview(Object object)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.startPreview.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.stop(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.stop.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.stopBGM(Object object)

基础库 2.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.stopBGM.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.stopPreview(Object object)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.stopPreview.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.switchCamera(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.switchCamera.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### LivePusherContext.toggleTorch(Object object)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.toggleTorch.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.stopRecord(Object object)

从基础库1.6.0开始，本接口停止维护，请使用wx.getRecorderManager代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/wx.stopRecord.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.startRecord(Object object)

从基础库1.6.0开始，本接口停止维护，请使用wx.getRecorderManager代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/wx.startRecord.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempFilePath | string | 录音文件的临时路径 (本地路径) |

---

### RecorderManager wx.getRecorderManager()

基础库 1.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/wx.getRecorderManager.html

---

### RecorderManager

全局唯一的录音管理器

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/RecorderManager.html

---

### RecorderManager.onError(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/RecorderManager.onError.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |

---

### RecorderManager.onFrameRecorded(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/RecorderManager.onFrameRecorded.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| frameBuffer | ArrayBuffer | 录音分片数据 |
| isLastFrame | boolean | 当前帧是否正常录音结束前的最后一帧 |

---

### RecorderManager.onInterruptionBegin(function listener)

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/RecorderManager.onInterruptionBegin.html

---

### RecorderManager.onInterruptionEnd(function listener)

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/RecorderManager.onInterruptionEnd.html

---

### RecorderManager.onPause(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/RecorderManager.onPause.html

---

### RecorderManager.onResume(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/RecorderManager.onResume.html

---

### RecorderManager.onStart(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/RecorderManager.onStart.html

---

### RecorderManager.onStop(function listener)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/RecorderManager.onStop.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempFilePath | string | 录音文件的临时路径 (本地路径) |
| duration | number | 录音总时长，单位：ms |
| fileSize | number | 录音文件大小，单位：Byte |

---

### RecorderManager.pause()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/RecorderManager.pause.html

---

### RecorderManager.resume()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/RecorderManager.resume.html

---

### RecorderManager.start(Object object)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/RecorderManager.start.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | duration | number | 60000 | 否 | 录音的时长，单位 ms，最大值 600000（10 分钟） |  |
|  | sampleRate | number | 8000 | 否 | 采样率（pc不支持） |  |
|  | | 合法值 | 说明 | | --- | --- | | 8000 | 8000 采样率 | | 11025 | 11025 采样率 | | 12000 | 12000 采样率 | | 16000 | 16000 采样率 | | 22050 | 22050 采样率 | | 24000 | 24000 采样率 | | 32000 | 32000 采样率 | | 44100 | 44100 采样率 | | 48000 | 48000 采样率 | | | | | | |
|  | numberOfChannels | number | 2 | 否 | 录音通道数 |  |
|  | | 合法值 | 说明 | | --- | --- | | 1 | 1 个通道 | | 2 | 2 个通道 | | | | | | |
|  | encodeBitRate | number | 48000 | 否 | 编码码率，有效值见下表格 |  |
|  | format | string | aac | 否 | 音频格式 |  |
|  | | 合法值 | 说明 | | --- | --- | | mp3 | mp3 格式 | | aac | aac 格式 | | wav | wav 格式 | | PCM | pcm 格式 | | | | | | |
|  | frameSize | number |  | 否 | 指定帧大小，单位 KB。传入 frameSize 后，每录制指定帧大小的内容后，会回调录制的文件内容，不指定则不会回调。暂仅支持 mp3、pcm 格式。 |  |
|  | audioSource | string | auto | 否 | 指定录音的音频输入源，可通过 [wx.getAvailableAudioSources()](../audio/wx.getAvailableAudioSources.html) 获取当前可用的音频源 | [2.1.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | auto | 自动设置，默认使用手机麦克风，插上耳麦后自动切换使用耳机麦克风，所有平台适用 | | buildInMic | 手机麦克风，仅限 iOS | | headsetMic | 有线耳机麦克风，仅限 iOS | | mic | 麦克风（没插耳麦时是手机麦克风，插耳麦时是耳机麦克风），仅限 Android | | camcorder | 同 mic，适用于录制音视频内容，仅限 Android | | voice\_communication | 同 mic，适用于实时沟通，仅限 Android | | voice\_recognition | 同 mic，适用于语音识别，仅限 Android | | | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 8000 | 8000 采样率 |
| 11025 | 11025 采样率 |
| 12000 | 12000 采样率 |
| 16000 | 16000 采样率 |
| 22050 | 22050 采样率 |
| 24000 | 24000 采样率 |
| 32000 | 32000 采样率 |
| 44100 | 44100 采样率 |
| 48000 | 48000 采样率 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 1 | 1 个通道 |
| 2 | 2 个通道 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| mp3 | mp3 格式 |
| aac | aac 格式 |
| wav | wav 格式 |
| PCM | pcm 格式 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| auto | 自动设置，默认使用手机麦克风，插上耳麦后自动切换使用耳机麦克风，所有平台适用 |
| buildInMic | 手机麦克风，仅限 iOS |
| headsetMic | 有线耳机麦克风，仅限 iOS |
| mic | 麦克风（没插耳麦时是手机麦克风，插耳麦时是耳机麦克风），仅限 Android |
| camcorder | 同 mic，适用于录制音视频内容，仅限 Android |
| voice\_communication | 同 mic，适用于实时沟通，仅限 Android |
| voice\_recognition | 同 mic，适用于语音识别，仅限 Android |

**采样率与编码码率限制**

| 采样率 | 编码码率 |
| --- | --- |
| 8000 | 16000 ~ 48000 |
| 11025 | 16000 ~ 48000 |
| 12000 | 24000 ~ 64000 |
| 16000 | 24000 ~ 96000 |
| 22050 | 32000 ~ 128000 |
| 24000 | 32000 ~ 128000 |
| 32000 | 48000 ~ 192000 |
| 44100 | 64000 ~ 320000 |
| 48000 | 64000 ~ 320000 |

---

### RecorderManager.stop()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/RecorderManager.stop.html

---

### CameraContext wx.createCameraContext()

基础库 1.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/camera/wx.createCameraContext.html

---

### CameraContext

相关文档:camera 组件介绍

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/camera/CameraContext.html

---

### CameraFrameListener CameraContext.onCameraFrame(function callback)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/camera/CameraContext.onCameraFrame.html

**function callback**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 图像数据矩形的宽度 |
| height | number | 图像数据矩形的高度 |
| data | ArrayBuffer | 图像像素点数据，一维数组，每四项表示一个像素点的 rgba |

---

### CameraContext.setZoom(Object object)

基础库 2.10.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/camera/CameraContext.setZoom.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| zoom | number |  | 是 | 缩放级别，范围[1, maxZoom]。zoom 可取小数，精确到小数后一位。maxZoom 可在 bindinitdone 返回值中获取。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| zoom | number | 实际设置的缩放级别。由于系统限制，某些机型可能无法设置成指定值，会改用最接近的可设值。 |

---

### CameraContext.startRecord(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/camera/CameraContext.startRecord.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| timeoutCallback | function |  | 否 | 超过录制时长上限时会结束录像并触发此回调，录像异常退出时也会触发此回调 |  |
| timeout | number | 30 | 否 | 录制时长上限，单位为秒，最长不能超过 5 分钟 | [2.22.0](../../../framework/compatibility.html) |
| selfieMirror | boolean | true | 否 | 是否开启镜像 | [2.22.0](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempThumbPath | string | 封面图片文件的临时路径 (本地路径) |
| tempVideoPath | string | 视频的文件的临时路径 (本地路径) |

---

### CameraContext.stopRecord(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/camera/CameraContext.stopRecord.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| compressed | boolean | false | 否 | 启动视频压缩，压缩效果同`chooseVideo` |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempThumbPath | string | 封面图片文件的临时路径 (本地路径) |
| tempVideoPath | string | 视频的文件的临时路径 (本地路径) |

---

### CameraContext.takePhoto(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/camera/CameraContext.takePhoto.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | quality | string | normal | 否 | 成像质量 |  |
|  | | 合法值 | 说明 | | --- | --- | | high | 高质量 | | normal | 普通质量 | | low | 低质量 | | original | 原图 | | | | | | |
|  | selfieMirror | boolean | true | 否 | 是否开启镜像 | [2.22.0](../../../framework/compatibility.html) |
|  | captureMetadata | boolean | false | 否 | 是否返回照片的拍摄信息 | [3.15.0](../../../framework/compatibility.html) |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| high | 高质量 |
| normal | 普通质量 |
| low | 低质量 |
| original | 原图 |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| tempImagePath | string | 照片文件的临时路径 (本地路径)，安卓是jpg图片格式，ios是png |  |
| metadata | Object | 照片的拍摄信息，仅当传入的 captureMetadata 属性值为 true 时返回该字段 | [3.15.0](../../../framework/compatibility.html) |

---

### CameraFrameListener

相关文档:camera 组件介绍

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/camera/CameraFrameListener.html

---

### CameraFrameListener.start(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/camera/CameraFrameListener.start.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| worker | [Worker](../../worker/Worker.html) |  | 否 | 可选参数。如果需要在 iOS ExperimentalWorker 内监听摄像头帧数据，则需要传入对应 Worker 对象。详情 [Worker.getCameraFrameData](../../worker/Worker.getCameraFrameData.html) | [2.25.1](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### CameraFrameListener.stop(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/camera/CameraFrameListener.stop.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### EditorContext.blur(Object object)

基础库 2.8.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.blur.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### EditorContext

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.html

---

### EditorContext.clear(Object object)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.clear.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### EditorContext.deleteText(Object object)

基础库 3.7.11 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.deleteText.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| index | number |  | 是 | 选区开始位置 |
| length | number |  | 否 | 选区长度 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### EditorContext.format(string name, string value)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.format.html

**支持设置的样式列表**

| name | value | verson |
| --- | --- | --- |
| bold |  | 2.7.0 |
| italic |  | 2.7.0 |
| underline |  | 2.7.0 |
| strike |  | 2.7.0 |
| ins |  | 2.7.0 |
| script | sub / super | 2.7.0 |
| header | H1 / H2 / h3 / H4 / h5 / H6 | 2.7.0 |
| align | left / center / right / justify | 2.7.0 |
| direction | rtl | 2.7.0 |
| indent | -1 / +1 | 2.7.0 |
| list | ordered / bullet / check | 2.7.0 |
| color | hex color | 2.7.0 |
| backgroundColor | hex color | 2.7.0 |
| margin/marginTop/marginBottom/marginLeft/marginRight | css style | 2.7.0 |
| padding/paddingTop/paddingBottom/paddingLeft/paddingRight | css style | 2.7.0 |
| font/fontSize/fontStyle/fontVariant/fontWeight/fontFamily | css style | 2.7.0 |
| lineHeight | css style | 2.7.0 |
| letterSpacing | css style | 2.7.0 |
| textDecoration | css style | 2.7.0 |
| textIndent | css style | 2.8.0 |
| wordWrap | css style | 2.10.2 |
| wordBreak | css style | 2.10.2 |
| whiteSpace | css style | 2.10.2 |

---

### EditorContext.getBounds(Object object)

基础库 3.7.11 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.getBounds.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| index | number |  | 是 | 选区开始位置 |
| length | number |  | 否 | 选区长度 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| bounds | Object | 选区相对于视口的大小和位置 |

---

### EditorContext.getContents(Object object)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.getContents.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| html | string | 带标签的HTML内容 |
| text | string | 纯文本内容 |
| delta | Object | 表示内容的delta对象 |

---

### EditorContext.getHistoryState(Object object)

基础库 3.9.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.getHistoryState.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### EditorContext.getSelection(Object object)

基础库 3.7.11 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.getSelection.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| range | Object | 选区位置，index 为开始位置，length 为选区长度 |
| bounds | Object | 选区相对于视口的大小和位置 |

---

### EditorContext.getSelectionText(Object object)

基础库 2.10.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.getSelectionText.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| text | string | 纯文本内容 |

---

### EditorContext.insertCustomBlock(Object object)

基础库 3.7.11 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.insertCustomBlock.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| nowrap | boolean | false | 否 | 插入自定义块后是否自动换行，默认换行 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| blockId | string | 自定义区块标识符，需结合 [editor-portal](../../../component/editor-portal.html) 组件一起使用。 |

---

### EditorContext.insertDivider(Object object)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.insertDivider.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### EditorContext.insertImage(Object object)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.insertImage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| src | string |  | 是 | 图片地址，仅支持 http(s)、base64、云图片(2.8.0)、临时文件(2.8.3)。 |
| nowrap | boolean | false | 否 | 插入图片后是否自动换行，默认换行 |
| alt | string |  | 否 | 图像无法显示时的替代文本 |
| width | string |  | 否 | 图片宽度（pixels/百分比) |
| height | string |  | 否 | 图片高度 (pixels/百分比) |
| extClass | string |  | 否 | 添加到图片 img 标签上的类名 |
| data | Object |  | 否 | data 被序列化为 name=value;name1=value2 的格式挂在属性 data-custom 上 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### EditorContext.insertText(Object object)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.insertText.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| text | string |  | 否 | 文本内容 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### EditorContext.redo(Object object)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.redo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### EditorContext.removeFormat(Object object)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.removeFormat.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### EditorContext.scrollIntoView()

基础库 2.8.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.scrollIntoView.html

---

### EditorContext.setContents(Object object)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.setContents.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| html | string |  | 否 | 带标签的HTML内容 |
| delta | Object |  | 否 | 表示内容的delta对象 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### EditorContext.setSelection(Object object)

基础库 3.7.11 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.setSelection.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| index | number |  | 是 | 选区开始位置 |
| length | number |  | 否 | 选区长度 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### EditorContext.undo(Object object)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.undo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### MediaContainer wx.createMediaContainer()

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video-processing/wx.createMediaContainer.html

---

### MediaContainer

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video-processing/MediaContainer.html

---

### MediaContainer.addTrack(MediaTrack track)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video-processing/MediaContainer.addTrack.html

---

### MediaContainer.destroy()

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video-processing/MediaContainer.destroy.html

---

### MediaContainer.export()

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video-processing/MediaContainer.export.html

---

### MediaContainer.extractDataSource(Object object)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video-processing/MediaContainer.extractDataSource.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| source | string |  | 是 | 视频源地址，只支持本地文件 |

---

### MediaContainer.removeTrack(MediaTrack track)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video-processing/MediaContainer.removeTrack.html

---

### MediaTrack

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video-processing/MediaTrack.html

**string kind**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| audio | 音频轨道 |  |
| video | 视频轨道 |  |

---

### wx.updateVoIPChatMuteConfig(Object object)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.updateVoIPChatMuteConfig.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | muteConfig | Object |  | 是 | 静音设置 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | muteMicrophone | Boolean | false | 否 | 是否静音麦克风 | |  | muteEarphone | Boolean | false | 否 | 是否静音耳机 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | muteMicrophone | Boolean | false | 否 | 是否静音麦克风 |
|  | muteEarphone | Boolean | false | 否 | 是否静音耳机 |

---

### wx.subscribeVoIPVideoMembers(Object object)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.subscribeVoIPVideoMembers.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| openIdList | Array.<String> |  | 是 | 订阅的成员列表 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.setEnable1v1Chat(Object object)

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.setEnable1v1Chat.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | enable | Boolean |  | 是 | 是否开启 |
|  | backgroundType | Number | 0 | 否 | 窗口背景色(音频通话背景以及小窗模式背景) |
|  | | 合法值 | 说明 | | --- | --- | | 0 | #262930 | | 1 | #FA5151 | | 2 | #FA9D3B | | 3 | #3D7257 | | 4 | #1485EE | | 5 | #6467F0 | | | | | |
|  | minWindowType | Number | 1 | 否 | 小窗样式 |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 0 | #262930 |
| 1 | #FA5151 |
| 2 | #FA9D3B |
| 3 | #3D7257 |
| 4 | #1485EE |
| 5 | #6467F0 |

---

### wx.onVoIPVideoMembersChanged(function listener)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.onVoIPVideoMembersChanged.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| openIdList | Array.<String> | 开启视频的成员名单 |
| errCode | Number | 错误码 |
| errMsg | String | 调用结果 |

---

### wx.onVoIPChatStateChanged(function listener)

基础库 2.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.onVoIPChatStateChanged.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| code | Number | 事件码 |
| data | object | 附加信息 |
| errCode | Number | 错误码 |
| errMsg | String | 调用结果 |

---

### wx.onVoIPChatSpeakersChanged(function listener)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.onVoIPChatSpeakersChanged.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| openIdList | Array.<String> | 还在实时语音通话中的成员 openId 名单 |
| errCode | Number | 错误码 |
| errMsg | String | 调用结果（错误原因） |

---

### wx.onVoIPChatMembersChanged(function listener)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.onVoIPChatMembersChanged.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| openIdList | Array.<String> | 还在实时语音通话中的成员 openId 名单 |
| errCode | Number | 错误码 |
| errMsg | String | 调用结果 |

---

### wx.onVoIPChatInterrupted(function listener)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.onVoIPChatInterrupted.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errCode | Number | 错误码 |
| errMsg | String | 调用结果（错误原因） |

---

### wx.offVoIPVideoMembersChanged(function listener)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.offVoIPVideoMembersChanged.html

---

### wx.offVoIPChatStateChanged(function listener)

基础库 2.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.offVoIPChatStateChanged.html

---

### wx.offVoIPChatSpeakersChanged(function listener)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.offVoIPChatSpeakersChanged.html

---

### wx.offVoIPChatMembersChanged(function listener)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.offVoIPChatMembersChanged.html

---

### wx.offVoIPChatInterrupted(function listener)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.offVoIPChatInterrupted.html

---

### wx.joinVoIPChat(Object object)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.joinVoIPChat.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | roomType | String | voice | 否 | 房间类型 |  |
|  | | 合法值 | 说明 | | --- | --- | | voice | 音频房间，用于语音通话 | | video | 视频房间，结合 [voip-room](../../../component/voip-room.html) 组件可显示成员画面 | | | | | | |
|  | signature | String |  | 是 | 签名，用于验证小游戏的身份 |  |
|  | nonceStr | String |  | 是 | 验证所需的随机字符串 |  |
|  | timeStamp | Number |  | 是 | 验证所需的时间戳 |  |
|  | groupId | String |  | 是 | 小游戏内此房间/群聊的 ID。同一时刻传入相同 groupId 的用户会进入到同个实时语音房间。 |  |
|  | muteConfig | Object |  | 否 | 静音设置 |  |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | muteMicrophone | Boolean | false | 否 | 是否静音麦克风 | |  | muteEarphone | Boolean | false | 否 | 是否静音耳机 | | | | | | |
|  | forceCellularNetwork | boolean | false | 否 | 开启后，joinVoIPChat 会同时走 Wi-Fi 和蜂窝网络2种网络模式，保证实时通话体验。 | [2.29.0](../../../framework/compatibility.html) |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| voice | 音频房间，用于语音通话 |
| video | 视频房间，结合 [voip-room](../../../component/voip-room.html) 组件可显示成员画面 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | muteMicrophone | Boolean | false | 否 | 是否静音麦克风 |
|  | muteEarphone | Boolean | false | 否 | 是否静音耳机 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| openIdList | Array.<String> | 在此通话中的成员 openId 名单 |
| errCode | Number | 错误码 |
| errMsg | String | 调用结果 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| -1 | 当前已在房间内 |  |
| -2 | 录音设备被占用，可能是当前正在使用微信内语音通话或系统通话 |  |
| -3 | 加入会话期间退出（可能是用户主动退出，或者退后台、来电等原因），因此加入失败 |  |
| -1000 | 系统错误 |  |

---

### wx.join1v1Chat(Object object)

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.join1v1Chat.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | caller | Object |  | 是 | 呼叫方信息 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | nickname | String |  | 是 | 昵称 | |  | headImage | String |  | 否 | 头像 | |  | openid | String |  | 是 | 小程序内 openid | | | | | |
|  | listener | Object |  | 是 | 接听方信息 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | nickname | String |  | 是 | 昵称 | |  | headImage | String |  | 否 | 头像 | |  | openid | String |  | 是 | 小程序内 openid | | | | | |
|  | backgroundType | Number | 0 | 否 | 窗口背景色(音频通话背景以及小窗模式背景) |
|  | | 合法值 | 说明 | | --- | --- | | 0 | #262930 | | 1 | #FA5151 | | 2 | #FA9D3B | | 3 | #3D7257 | | 4 | #1485EE | | 5 | #6467F0 | | | | | |
|  | roomType | String | video | 否 | 通话类型 |
|  | | 合法值 | 说明 | | --- | --- | | voice | 语音通话 | | video | 视频通话 | | | | | |
|  | minWindowType | Number | 1 | 否 | 小窗样式 |
|  | disableSwitchVoice | Boolean | false | 否 | 不允许切换到语音通话 |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | nickname | String |  | 是 | 昵称 |
|  | headImage | String |  | 否 | 头像 |
|  | openid | String |  | 是 | 小程序内 openid |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | nickname | String |  | 是 | 昵称 |
|  | headImage | String |  | 否 | 头像 |
|  | openid | String |  | 是 | 小程序内 openid |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 0 | #262930 |
| 1 | #FA5151 |
| 2 | #FA9D3B |
| 3 | #3D7257 |
| 4 | #1485EE |
| 5 | #6467F0 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| voice | 语音通话 |
| video | 视频通话 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| -20000 | not open 1v1 Chat | 未开通双人通话 |
| -20001 | device not support | 当前设备不支持 |
| -20002 | on call | 正在通话中 |
| -20003 | occupied by other miniprogram | 其它小程序正在通话中 |
| -30000 | system error | 内部系统错误 |
| -30001 | wechat has no camera authorization | 微信缺失相机权限 |
| -30002 | wechat has no record authorization | 微信缺失录音权限 |
| -30003 | miniprogram has no record authorization | 小程序缺失录音权限 |
| -30004 | miniprogram has no camera authorization | 小程序缺失相机权限 |
| -1 |  | 当前已在房间内 |
| -2 |  | 录音设备被占用，可能是当前正在使用微信内语音通话或系统通话 |
| -3 |  | 加入会话期间退出（可能是用户主动退出，或者退后台、来电等原因），因此加入失败 |
| -1000 |  | 系统错误 |

---

### wx.exitVoIPChat(Object object)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.exitVoIPChat.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### MediaRecorder wx.createMediaRecorder(Object canvas, Object options)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/media-recorder/wx.createMediaRecorder.html

**Object options**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 600 | 否 | 指定录制的时长（s)，到达自动停止。最大 7200，最小 5 |
| videoBitsPerSecond | number | 1000 | 否 | 视频比特率（kbps），最小值 600，最大值 3000 |
| gop | number | 12 | 否 | 视频关键帧间隔 |
| fps | number | 24 | 否 | 视频 fps |
| width | number | canvas.width | 否 | 画布录制宽度 |
| height | number | canvas.height | 否 | 画布录制高度 |

---

### MediaRecorder

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/media-recorder/MediaRecorder.html

---

### Promise MediaRecorder.destroy()

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/media-recorder/MediaRecorder.destroy.html

---

### MediaRecorder.off(string eventName, function callback)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/media-recorder/MediaRecorder.off.html

---

### MediaRecorder.on(string eventName, function callback)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/media-recorder/MediaRecorder.on.html

**string eventName**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| start | 录制开始事件。 |  |
| stop | 录制结束事件。返回 {tempFilePath, duration, fileSize} |  |
| pause | 录制暂停事件。 |  |
| resume | 录制继续事件。 |  |
| timeupdate | 录制时间更新事件。 |  |

---

### Promise MediaRecorder.pause()

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/media-recorder/MediaRecorder.pause.html

---

### Promise MediaRecorder.requestFrame(function callback)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/media-recorder/MediaRecorder.requestFrame.html

---

### Promise MediaRecorder.resume()

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/media-recorder/MediaRecorder.resume.html

---

### Promise MediaRecorder.start()

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/media-recorder/MediaRecorder.start.html

---

### Promise MediaRecorder.stop()

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/media-recorder/MediaRecorder.stop.html

---

### VideoDecoder wx.createVideoDecoder()

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video-decoder/wx.createVideoDecoder.html

---

### VideoDecoder

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video-decoder/VideoDecoder.html

---

### Object VideoDecoder.getFrameData()

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video-decoder/VideoDecoder.getFrameData.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 帧数据宽度 |
| height | number | 帧数据高度 |
| data | ArrayBuffer | 帧数据 |
| pkPts | number | 帧原始 pts |
| pkDts | number | 帧原始 dts |

---

### VideoDecoder.off(string eventName, function callback)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video-decoder/VideoDecoder.off.html

---

### VideoDecoder.on(string eventName, function callback)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video-decoder/VideoDecoder.on.html

**string eventName**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| start | 开始事件。返回 {width, height} |  |
| stop | 结束事件。 |  |
| seek | seek 完成事件。 |  |
| bufferchange | 缓冲区变化事件。 |  |
| ended | 解码结束事件。 |  |

---

### Promise VideoDecoder.remove()

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video-decoder/VideoDecoder.remove.html

---

### Promise VideoDecoder.seek(number position)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video-decoder/VideoDecoder.seek.html

---

### Promise VideoDecoder.start(Object object)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video-decoder/VideoDecoder.start.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| source | string |  | 是 | 需要解码的视频源文件。基础库 2.13.0 以下的版本只支持本地路径。 2.13.0 开始支持 http:// 和 https:// 协议的远程路径。 |  |
| mode | number | 1 | 否 | 解码模式。0：按 pts 解码；1：以最快速度解码 |  |
| abortAudio | boolean | false | 否 | 是否不需要音频轨道 | [2.15.0](../../../framework/compatibility.html) |
| abortVideo | boolean | false | 否 | 是否不需要视频轨道 | [2.15.0](../../../framework/compatibility.html) |

---

### Promise VideoDecoder.stop()

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/media/video-decoder/VideoDecoder.stop.html

---

<!-- pages: 311 -->
