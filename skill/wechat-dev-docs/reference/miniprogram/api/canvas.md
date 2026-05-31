# 微信小程序 API 结构化参考 — canvas

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### OffscreenCanvas wx.createOffscreenCanvas(object object, number width, number height, Object this)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/wx.createOffscreenCanvas.html

**object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | type | string | webgl | 否 | 创建的离屏 canvas 类型 |
|  | | 合法值 | 说明 | | --- | --- | | webgl | webgl类型上下文 | | 2d | 2d类型上下文 | | | | | |
|  | width | number |  | 否 | 画布宽度 |
|  | height | number |  | 否 | 画布高度 |
|  | compInst | Component |  | 否 | 在自定义组件下，当前组件实例的 this |

**object object**

| 合法值 | 说明 |
| --- | --- |
| webgl | webgl类型上下文 |
| 2d | 2d类型上下文 |

---

### CanvasContext wx.createCanvasContext(string canvasId, Object this)

从基础库2.9.0开始，本接口停止维护，请使用Canvas代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/wx.createCanvasContext.html

---

### wx.canvasToTempFilePath(Object object, Object this)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/wx.canvasToTempFilePath.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | x | number | 0 | 否 | 指定的画布区域的左上角横坐标 | [1.2.0](../../framework/compatibility.html) |
|  | y | number | 0 | 否 | 指定的画布区域的左上角纵坐标 | [1.2.0](../../framework/compatibility.html) |
|  | width | number | canvas宽度-x | 否 | 指定的画布区域的宽度 | [1.2.0](../../framework/compatibility.html) |
|  | height | number | canvas高度-y | 否 | 指定的画布区域的高度 | [1.2.0](../../framework/compatibility.html) |
|  | destWidth | number | width\*屏幕像素密度 | 否 | 输出的图片的宽度 | [1.2.0](../../framework/compatibility.html) |
|  | destHeight | number | height\*屏幕像素密度 | 否 | 输出的图片的高度 | [1.2.0](../../framework/compatibility.html) |
|  | canvasId | string |  | 否 | 画布标识，传入 [canvas](../../component/canvas.html) 组件的 canvas-id |  |
|  | canvas | Object |  | 否 | 画布标识，传入 [canvas](../../component/canvas.html) 组件实例 （canvas type="2d" 时使用该属性）。 |  |
|  | fileType | string | png | 否 | 目标文件的类型 | [1.7.0](../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | jpg | jpg 图片 | | png | png 图片 | | | | | | |
|  | quality | number |  | 否 | 图片的质量，目前仅对 jpg 有效。取值范围为 (0, 1]，不在范围内时当作 1.0 处理。 | [1.7.0](../../framework/compatibility.html) |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| jpg | jpg 图片 |
| png | png 图片 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempFilePath | string | 生成文件的临时路径 (本地路径) |

---

### wx.canvasPutImageData(Object object, Object this)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/wx.canvasPutImageData.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| canvasId | string |  | 是 | 画布标识，传入 [canvas](../../component/canvas.html) 组件的 canvas-id 属性。 |
| data | Uint8ClampedArray |  | 是 | 图像像素点数据，一维数组，每四项表示一个像素点的 rgba |
| x | number |  | 是 | 源图像数据在目标画布中的位置偏移量（x 轴方向的偏移量） |
| y | number |  | 是 | 源图像数据在目标画布中的位置偏移量（y 轴方向的偏移量） |
| width | number |  | 是 | 源图像数据矩形区域的宽度 |
| height | number |  | 是 | 源图像数据矩形区域的高度 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.canvasGetImageData(Object object, Object this)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/wx.canvasGetImageData.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| canvasId | string |  | 是 | 画布标识，传入 [canvas](../../component/canvas.html) 组件的 `canvas-id` 属性。 |
| x | number |  | 是 | 将要被提取的图像数据矩形区域的左上角横坐标 |
| y | number |  | 是 | 将要被提取的图像数据矩形区域的左上角纵坐标 |
| width | number |  | 是 | 将要被提取的图像数据矩形区域的宽度 |
| height | number |  | 是 | 将要被提取的图像数据矩形区域的高度 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 图像数据矩形的宽度 |
| height | number | 图像数据矩形的高度 |
| data | Uint8ClampedArray | 图像像素点数据，一维数组，每四项表示一个像素点的 rgba |

---

### Canvas

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.html

---

### Canvas.cancelAnimationFrame(number requestID)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.cancelAnimationFrame.html

---

### Image Canvas.createImage()

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.createImage.html

---

### ImageData Canvas.createImageData()

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.createImageData.html

---

### Path2D Canvas.createPath2D(Path2D path)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.createPath2D.html

---

### RenderingContext Canvas.getContext(string contextType)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.getContext.html

**string contextType**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 2d | 2d 绘图上下文 |  |
| webgl | webgl 绘图上下文 |  |
| webgl2 | webgl2 绘图上下文 | [2.24.0](../../framework/compatibility.html) |

---

### number Canvas.requestAnimationFrame(function callback)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.requestAnimationFrame.html

---

### string Canvas.toDataURL(string type, number encoderOptions)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.toDataURL.html

---

### CanvasContext

相关文档:旧版画布迁移指南、canvas 组件介绍

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.html

**string lineJoin**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| bevel | 斜角 |  |
| round | 圆角 |  |
| miter | 尖角 |  |

---

### CanvasContext.arc(number x, number y, number r, number sAngle, number eAngle, boolean counterclockwise)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.arc.html

---

### CanvasContext.arcTo(number x1, number y1, number x2, number y2, number radius)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.arcTo.html

---

### CanvasContext.beginPath()

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.beginPath.html

---

### CanvasContext.bezierCurveTo(number cp1x, number cp1y, number cp2x, number cp2y, number x, number y)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.bezierCurveTo.html

---

### CanvasContext.clearRect(number x, number y, number width, number height)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.clearRect.html

---

### CanvasContext.clip()

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.clip.html

---

### CanvasContext.closePath()

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.closePath.html

---

### CanvasGradient CanvasContext.createCircularGradient(number x, number y, number r)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.createCircularGradient.html

---

### CanvasGradient CanvasContext.createLinearGradient(number x0, number y0, number x1, number y1)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.createLinearGradient.html

---

### CanvasContext.createPattern(string image, string repetition)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.createPattern.html

**string repetition**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| repeat | 水平竖直方向都重复 |  |
| repeat-x | 水平方向重复 |  |
| repeat-y | 竖直方向重复 |  |
| no-repeat | 不重复 |  |

---

### CanvasContext.draw(boolean reserve, function callback)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.draw.html

---

### CanvasContext.drawImage(string imageResource, number sx, number sy, number sWidth, number sHeight, number dx, number dy, number dWidth, number dHeight)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.drawImage.html

---

### CanvasContext.fill()

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.fill.html

---

### CanvasContext.fillRect(number x, number y, number width, number height)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.fillRect.html

---

### CanvasContext.fillText(string text, number x, number y, number maxWidth)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.fillText.html

---

### CanvasContext.lineTo(number x, number y)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.lineTo.html

---

### Object CanvasContext.measureText(string text)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.measureText.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 文本的宽度 |

---

### CanvasContext.moveTo(number x, number y)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.moveTo.html

---

### CanvasContext.quadraticCurveTo(number cpx, number cpy, number x, number y)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.quadraticCurveTo.html

---

### CanvasContext.rect(number x, number y, number width, number height)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.rect.html

---

### CanvasContext.restore()

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.restore.html

---

### CanvasContext.rotate(number rotate)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.rotate.html

---

### CanvasContext.save()

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.save.html

---

### CanvasContext.scale(number scaleWidth, number scaleHeight)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.scale.html

---

### CanvasContext.setFillStyle(string|CanvasGradient color)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.setFillStyle.html

---

### CanvasContext.setFontSize(number fontSize)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.setFontSize.html

---

### CanvasContext.setGlobalAlpha(number alpha)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.setGlobalAlpha.html

---

### CanvasContext.setLineCap(string lineCap)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.setLineCap.html

**string lineCap**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| butt | 向线条的每个末端添加平直的边缘。 |  |
| round | 向线条的每个末端添加圆形线帽。 |  |
| square | 向线条的每个末端添加正方形线帽。 |  |

---

### CanvasContext.setLineDash(Array.<number> pattern, number offset)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.setLineDash.html

---

### CanvasContext.setLineJoin(string lineJoin)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.setLineJoin.html

**string lineJoin**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| bevel | 斜角 |  |
| round | 圆角 |  |
| miter | 尖角 |  |

---

### CanvasContext.setLineWidth(number lineWidth)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.setLineWidth.html

---

### CanvasContext.setMiterLimit(number miterLimit)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.setMiterLimit.html

---

### CanvasContext.setShadow(number offsetX, number offsetY, number blur, string color)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.setShadow.html

---

### CanvasContext.setStrokeStyle(string|CanvasGradient color)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.setStrokeStyle.html

---

### CanvasContext.setTextAlign(string align)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.setTextAlign.html

**string align**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| left | 左对齐 |  |
| center | 居中对齐 |  |
| right | 右对齐 |  |

---

### CanvasContext.setTextBaseline(string textBaseline)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.setTextBaseline.html

**string textBaseline**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| top | 顶部对齐 |  |
| bottom | 底部对齐 |  |
| middle | 居中对齐 |  |
| normal |  |  |

---

### CanvasContext.setTransform(number scaleX, number skewX, number skewY, number scaleY, number translateX, number translateY)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.setTransform.html

---

### CanvasContext.stroke()

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.stroke.html

---

### CanvasContext.strokeRect(number x, number y, number width, number height)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.strokeRect.html

---

### CanvasContext.strokeText(string text, number x, number y, number maxWidth)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.strokeText.html

---

### CanvasContext.transform(number scaleX, number skewX, number skewY, number scaleY, number translateX, number translateY)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.transform.html

---

### CanvasContext.translate(number x, number y)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.translate.html

---

### CanvasGradient

相关文档:旧版画布迁移指南、canvas 组件介绍

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasGradient.html

---

### CanvasGradient.addColorStop(number stop, string color)

CanvasContext 是旧版的接口，新版Canvas 2D接口与 Web 一致

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasGradient.addColorStop.html

---

### Color

颜色。可以用以下几种方式来表示 canvas 中使用的颜色：

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Color.html

| Color Name | HEX |
| --- | --- |
| AliceBlue | #F0F8FF |
| AntiqueWhite | #FAEBD7 |
| Aqua | #00FFFF |
| Aquamarine | #7FFFD4 |
| Azure | #F0FFFF |
| Beige | #F5F5DC |
| Bisque | #FFE4C4 |
| Black | #000000 |
| BlanchedAlmond | #FFEBCD |
| Blue | #0000FF |
| BlueViolet | #8A2BE2 |
| Brown | #A52A2A |
| BurlyWood | #DEB887 |
| CadetBlue | #5F9EA0 |
| Chartreuse | #7FFF00 |
| Chocolate | #D2691E |
| Coral | #FF7F50 |
| CornflowerBlue | #6495ED |
| Cornsilk | #FFF8DC |
| Crimson | #DC143C |
| Cyan | #00FFFF |
| DarkBlue | #00008B |
| DarkCyan | #008B8B |
| DarkGoldenRod | #B8860B |
| DarkGray | #A9A9A9 |
| DarkGrey | #A9A9A9 |
| DarkGreen | #006400 |
| DarkKhaki | #BDB76B |
| DarkMagenta | #8B008B |
| DarkOliveGreen | #556B2F |
| DarkOrange | #FF8C00 |
| DarkOrchid | #9932CC |
| DarkRed | #8B0000 |
| DarkSalmon | #E9967A |
| DarkSeaGreen | #8FBC8F |
| DarkSlateBlue | #483D8B |
| DarkSlateGray | #2F4F4F |
| DarkSlateGrey | #2F4F4F |
| DarkTurquoise | #00CED1 |
| DarkViolet | #9400D3 |
| DeepPink | #FF1493 |
| DeepSkyBlue | #00BFFF |
| DimGray | #696969 |
| DimGrey | #696969 |
| DodgerBlue | #1E90FF |
| FireBrick | #B22222 |
| FloralWhite | #FFFAF0 |
| ForestGreen | #228B22 |
| Fuchsia | #FF00FF |
| Gainsboro | #DCDCDC |
| GhostWhite | #F8F8FF |
| Gold | #FFD700 |
| GoldenRod | #DAA520 |
| Gray | #808080 |
| Grey | #808080 |
| Green | #008000 |
| GreenYellow | #ADFF2F |
| HoneyDew | #F0FFF0 |
| HotPink | #FF69B4 |
| IndianRed | #CD5C5C |
| Indigo | #4B0082 |
| Ivory | #FFFFF0 |
| Khaki | #F0E68C |
| Lavender | #E6E6FA |
| LavenderBlush | #FFF0F5 |
| LawnGreen | #7CFC00 |
| LemonChiffon | #FFFACD |
| LightBlue | #ADD8E6 |
| LightCoral | #F08080 |
| LightCyan | #E0FFFF |
| LightGoldenRodYellow | #FAFAD2 |
| LightGray | #D3D3D3 |
| LightGrey | #D3D3D3 |
| LightGreen | #90EE90 |
| LightPink | #FFB6C1 |
| LightSalmon | #FFA07A |
| LightSeaGreen | #20B2AA |
| LightSkyBlue | #87CEFA |
| LightSlateGray | #778899 |
| LightSlateGrey | #778899 |
| LightSteelBlue | #B0C4DE |
| LightYellow | #FFFFE0 |
| Lime | #00FF00 |
| LimeGreen | #32CD32 |
| Linen | #FAF0E6 |
| Magenta | #FF00FF |
| Maroon | #800000 |
| MediumAquaMarine | #66CDAA |
| MediumBlue | #0000CD |
| MediumOrchid | #BA55D3 |
| MediumPurple | #9370DB |
| MediumSeaGreen | #3CB371 |
| MediumSlateBlue | #7B68EE |
| MediumSpringGreen | #00FA9A |
| MediumTurquoise | #48D1CC |
| MediumVioletRed | #C71585 |
| MidnightBlue | #191970 |
| MintCream | #F5FFFA |
| MistyRose | #FFE4E1 |
| Moccasin | #FFE4B5 |
| NavajoWhite | #FFDEAD |
| Navy | #000080 |
| OldLace | #FDF5E6 |
| Olive | #808000 |
| OliveDrab | #6B8E23 |
| Orange | #FFA500 |
| OrangeRed | #FF4500 |
| Orchid | #DA70D6 |
| PaleGoldenRod | #EEE8AA |
| PaleGreen | #98FB98 |
| PaleTurquoise | #AFEEEE |
| PaleVioletRed | #DB7093 |
| PapayaWhip | #FFEFD5 |
| PeachPuff | #FFDAB9 |
| Peru | #CD853F |
| Pink | #FFC0CB |
| Plum | #DDA0DD |
| PowderBlue | #B0E0E6 |
| Purple | #800080 |
| RebeccaPurple | #663399 |
| Red | #FF0000 |
| RosyBrown | #BC8F8F |
| RoyalBlue | #4169E1 |
| SaddleBrown | #8B4513 |
| Salmon | #FA8072 |
| SandyBrown | #F4A460 |
| SeaGreen | #2E8B57 |
| SeaShell | #FFF5EE |
| Sienna | #A0522D |
| Silver | #C0C0C0 |
| SkyBlue | #87CEEB |
| SlateBlue | #6A5ACD |
| SlateGray | #708090 |
| SlateGrey | #708090 |
| Snow | #FFFAFA |
| SpringGreen | #00FF7F |
| SteelBlue | #4682B4 |
| Tan | #D2B48C |
| Teal | #008080 |
| Thistle | #D8BFD8 |
| Tomato | #FF6347 |
| Turquoise | #40E0D0 |
| Violet | #EE82EE |
| Wheat | #F5DEB3 |
| White | #FFFFFF |
| WhiteSmoke | #F5F5F5 |
| Yellow | #FFFF00 |
| YellowGreen | #9ACD32 |

---

### Image

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Image.html

---

### ImageData

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/ImageData.html

---

### OffscreenCanvas

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/OffscreenCanvas.html

---

### Image OffscreenCanvas.createImage()

基础库 2.7.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/OffscreenCanvas.createImage.html

---

### RenderingContext OffscreenCanvas.getContext(string contextType)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/OffscreenCanvas.getContext.html

**string contextType**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| webgl | webgl类型上下文 |  |
| 2d | 2d类型上下文 | [2.16.1](../../framework/compatibility.html) |

---

### Path2D

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Path2D.html

---

### Path2D.addPath(Path2D path)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Path2D.addPath.html

---

### Path2D.arc(number x, number y, number radius, number startAngle, number endAngle, boolean counterclockwise)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Path2D.arc.html

---

### Path2D.arcTo(number x1, number y1, number x2, number y2, number radius)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Path2D.arcTo.html

---

### Path2D.bezierCurveTo(number cp1x, number cp1y, number cp2x, number cp2y, number x, number y)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Path2D.bezierCurveTo.html

---

### Path2D.closePath()

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Path2D.closePath.html

---

### Path2D.ellipse(number x, number y, number radiusX, number radiusY, number rotation, number startAngle, number endAngle, boolean counterclockwise)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Path2D.ellipse.html

---

### Path2D.lineTo(number x, number y)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Path2D.lineTo.html

---

### Path2D.moveTo(number x, number y)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Path2D.moveTo.html

---

### Path2D.quadraticCurveTo(number cpx, number cpy, number x, number y)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Path2D.quadraticCurveTo.html

---

### Path2D.rect(number x, number y, number width, number height)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Path2D.rect.html

---

### RenderingContext

相关文档:画布指南、canvas 组件介绍

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/canvas/RenderingContext.html

---

<!-- pages: 76 -->
