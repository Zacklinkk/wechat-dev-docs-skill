# 微信小游戏 API 结构化参考 — render

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### Path2D wx.createPath2D()

基础库 2.24.6 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/canvas/wx.createPath2D.html

---

### Canvas wx.createCanvas()

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/canvas/wx.createCanvas.html

---

### Canvas

画布对象

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/canvas/Canvas.html

---

### RenderingContext Canvas.getContext(string contextType, Object contextAttributes)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/canvas/Canvas.getContext.html

**string contextType**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 2d | 2d 绘图上下文 |  |
| webgl | webgl 绘图上下文 |  |
| webgl2 | webgl2 绘图上下文 | [2.24.0](../../../guide/runtime/client-lib/compatibility.html) |

**Object contextAttributes**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| antialias | boolean | false | 否 | 表示是否抗锯齿 |  |
| preserveDrawingBuffer | boolean | false | 否 | 表示是否绘图完成后是否保留绘图缓冲区 |  |
| antialiasSamples | number | 2 | 否 | 抗锯齿样本数。最小值为 2，最大不超过系统限制数量，仅 iOS 支持 |  |
| alpha | boolean | false | 否 | 是否开启透明通道，仅当 contextType 为 webgl 时有效。（开启后，配合wx.createVideo({underGameView: true}) 即可在video组件之上渲染主屏画布） | [2.11.0](../../../guide/runtime/client-lib/compatibility.html) |

---

### string Canvas.toDataURL()

把画布上的绘制内容以一个 data URI 的格式返回

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/canvas/Canvas.toDataURL.html

---

### Canvas.toTempFilePath(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/canvas/Canvas.toTempFilePath.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | x | number | 0 | 否 | 截取 canvas 的左上角横坐标 |
|  | y | number | 0 | 否 | 截取 canvas 的左上角纵坐标 |
|  | width | number | canvas 的宽度 | 否 | 截取 canvas 的宽度 |
|  | height | number | canvas 的高度 | 否 | 截取 canvas 的高度 |
|  | destWidth | number | canvas 的宽度 | 否 | 目标文件的宽度，会将截取的部分拉伸或压缩至该数值 |
|  | destHeight | number | canvas 的高度 | 否 | 目标文件的高度，会将截取的部分拉伸或压缩至该数值 |
|  | fileType | string | png | 否 | 目标文件的类型 |
|  | | 合法值 | 说明 | | --- | --- | | jpg | jpg 文件 | | png | png 文件 | | | | | |
|  | quality | number | 1.0 | 否 | jpg图片的质量，仅当 fileType 为 jpg 时有效。取值范围为 0.0（最低）- 1.0（最高），不含 0。不在范围内时当作 1.0 |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| jpg | jpg 文件 |
| png | png 文件 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempFilePath | string | canvas 生成的临时文件路径 (本地路径) |

---

### string Canvas.toTempFilePathSync(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/canvas/Canvas.toTempFilePathSync.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | x | number | 0 | 否 | 截取 canvas 的左上角横坐标 |
|  | y | number | 0 | 否 | 截取 canvas 的左上角纵坐标 |
|  | width | number | canvas 的宽度 | 否 | 截取 canvas 的宽度 |
|  | height | number | canvas 的高度 | 否 | 截取 canvas 的高度 |
|  | destWidth | number | canvas 的宽度 | 否 | 目标文件的宽度，会将截取的部分拉伸或压缩至该数值 |
|  | destHeight | number | canvas 的高度 | 否 | 目标文件的高度，会将截取的部分拉伸或压缩至该数值 |
|  | fileType | string | png | 否 | 目标文件的类型 |
|  | | 合法值 | 说明 | | --- | --- | | jpg | jpg 文件 | | png | png 文件 | | | | | |
|  | quality | number | 1.0 | 否 | jpg图片的质量，仅当 fileType 为 jpg 时有效。取值范围为 0.0（最低）- 1.0（最高），不含 0。不在范围内时当作 1.0 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| jpg | jpg 文件 |
| png | png 文件 |

---

### Path2D

基础库 2.24.6 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/canvas/Path2D.html

---

### RenderingContext

画布对象的绘图上下文。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/canvas/RenderingContext.html

---

### WebGLRenderingContext.wxBindCanvasTexture(number texture, Canvas canvas)

从基础库3.13.0开始，本接口停止维护

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/canvas/WebGLRenderingContext.wxBindCanvasTexture.html

---

### wx.setPreferredFramesPerSecond(number fps)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/frame/wx.setPreferredFramesPerSecond.html

---

### cancelAnimationFrame(number requestID)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/frame/cancelAnimationFrame.html

---

### number requestAnimationFrame(function callback)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/frame/requestAnimationFrame.html

---

### string wx.loadFont(string path)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/font/wx.loadFont.html

---

### number wx.getTextLineHeight(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/font/wx.getTextLineHeight.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | fontStyle | string | normal | 否 | 字体样式 |
|  | | 合法值 | 说明 | | --- | --- | | normal | 正常 | | italic | 斜体 | | | | | |
|  | fontWeight | string | normal | 否 | 字重 |
|  | | 合法值 | 说明 | | --- | --- | | normal | 正常 | | bold | 粗体 | | | | | |
|  | fontSize | number | 16 | 否 | 字号 |
|  | fontFamily | string |  | 是 | 字体名称 |
|  | text | string |  | 是 | 文本的内容 |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| normal | 正常 |
| italic | 斜体 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| normal | 正常 |
| bold | 粗体 |

---

### ImageData wx.createImageData(number width, number height, Uint8ClampedArray data)

基础库 3.4.10 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/image/wx.createImageData.html

---

### Image wx.createImage()

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/image/wx.createImage.html

---

### Image

图片对象

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/image/Image.html

---

### ImageData

基础库 3.4.10 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/image/ImageData.html

---

### boolean wx.setCursor(string path, number x, number y)

基础库 2.10.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/cursor/wx.setCursor.html

---

### wx.requestPointerLock()

基础库 3.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/cursor/wx.requestPointerLock.html

---

### boolean wx.isPointerLocked()

基础库 3.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/cursor/wx.isPointerLocked.html

---

### wx.exitPointerLock()

基础库 3.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/render/cursor/wx.exitPointerLock.html

---

<!-- pages: 23 -->
