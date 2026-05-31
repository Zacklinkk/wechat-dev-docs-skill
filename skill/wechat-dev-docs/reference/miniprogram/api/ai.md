# 微信小程序 API 结构化参考 — ai

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.getInferenceEnvInfo(Object object)

基础库 2.30.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/wx.getInferenceEnvInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| ver | string | AI推理引擎版本 |

---

### InferenceSession wx.createInferenceSession(Object object)

基础库 2.30.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/wx.createInferenceSession.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | model | string |  | 是 | 模型文件路径，目前只执行后缀为.onnx格式(支持代码包路径，和本地文件系统路径） |
|  | precisionLevel | number | 4 | 否 | 推理精度，有效值为 0 - 4。一般来说，使用的precisionLevel等级越低，推理速度越快，但可能会损失精度。推荐开发者在开发时，在效果满足需求时优先使用更低精度以提高推理速度，节约能耗。 |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 使用fp16 存储浮点，fp16计算，Winograd 算法也采取fp16 计算，开启近似math计算 | | 1 | 使用fp16 存储浮点，fp16计算，禁用 Winograd 算法，开启近似math计算 | | 2 | 使用fp16 存储浮点，fp32计算，开启 Winograd，开启近似math计算 | | 3 | 使用fp32 存储浮点，fp32计算，开启 Winograd，开启近似math计算 | | 4 | 使用fp32 存储浮点，fp32计算，开启 Winograd，关闭近似math计算 | | | | | |
|  | allowQuantize | boolean | false | 否 | 是否生成量化模型推理 |
|  | allowNPU | boolean | false | 否 | 是否使用NPU推理，仅对IOS有效 |
|  | typicalShape | Object |  | 否 | 输入典型分辨率 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 0 | 使用fp16 存储浮点，fp16计算，Winograd 算法也采取fp16 计算，开启近似math计算 |
| 1 | 使用fp16 存储浮点，fp16计算，禁用 Winograd 算法，开启近似math计算 |
| 2 | 使用fp16 存储浮点，fp32计算，开启 Winograd，开启近似math计算 |
| 3 | 使用fp32 存储浮点，fp32计算，开启 Winograd，开启近似math计算 |
| 4 | 使用fp32 存储浮点，fp32计算，开启 Winograd，关闭近似math计算 |

---

### InferenceSession

基础库 2.30.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/InferenceSession.html

---

### InferenceSession.destroy()

基础库 2.30.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/InferenceSession.destroy.html

---

### InferenceSession.offError(function callback)

基础库 2.30.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/InferenceSession.offError.html

---

### InferenceSession.offLoad(function callback)

基础库 2.30.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/InferenceSession.offLoad.html

---

### InferenceSession.onError(function callback)

基础库 2.30.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/InferenceSession.onError.html

---

### InferenceSession.onLoad(function callback)

基础库 2.30.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/InferenceSession.onLoad.html

---

### Promise<Tensors> InferenceSession.run(Tensors tensors)

基础库 2.30.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/InferenceSession.run.html

---

### Tensor

基础库 2.30.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/Tensor.html

---

### Tensors

基础库 2.30.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/Tensors.html

---

### boolean wx.isVKSupport(string version)

基础库 2.22.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/wx.isVKSupport.html

**string version**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| v1 | 旧版本 |  |
| v2 | v2 版本，目前只有 iOS 基础库 2.22.0 以上支持 |  |

---

### VKSession wx.createVKSession(Object object)

基础库 2.20.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/wx.createVKSession.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | version | string |  | 否 | vision kit 版本。 | [2.22.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | v1 | v1适用于用户在平面场景下，例如桌面，地面，泛平面场景，放置虚拟物体，不提供真实世界距离。用户放置物体时，手机相机倾斜向下对着目标平面点击即可，具有广泛的机型支持 | | v2 | v2提供真实物理距离的 ar 定位功能，提供平面识别功能，用户在平面范围点击放置虚拟物体的功能，具有[有限的机型支持](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html#%E9%99%84%E5%BD%95)。iOS 设备在基础库 2.22.0 开始支持v2。安卓设备在基础库 2.25.1 开始支持v2，另外，安卓v2不支持竖直平面。\*\*使用v2算法需要初始化，移动手机进行左右平移初始化效果最佳。\*\* | | | | | | |
|  | track | Object |  | 是 | 跟踪能力配置，目前不同的跟踪能力之间是互斥的，默认使用平面跟踪能力。需要注意目前 track 中不同的跟踪配置存在互斥关系（比如 marker 跟踪配置和 OSD 跟踪配置不能同时存在），请按需配置。 |  |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | plane | Object |  | 是 | 平面跟踪配置 |  | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | mode | number |  | 是 | 平面跟踪配置模式 |  | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 检测横向平面 |  | | 2 | 检测纵向平面，只有 v2 版本支持 | [2.22.0](../../../framework/compatibility.html) | | 3 | 检测横向和纵向平面，只有 v2 版本支持 | [2.22.0](../../../framework/compatibility.html) | | | | | | | |  | force | boolean | false | 否 | 是否开启强制使用V2的模式，只有 v2 版本支持 | [3.6.5](../../../framework/compatibility.html) | | | | | | | |  | marker | boolean |  | 否 | marker 跟踪配置，基础库(3.0.0)开始允许同时支持v2的水平面检测能力 | [2.24.5](../../../framework/compatibility.html) | |  | OSD | boolean |  | 否 | OSD 跟踪配置 | [2.24.5](../../../framework/compatibility.html) | |  | depth | Object |  | 否 | 深度识别配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/depth.html)。 | [3.0.0](../../../framework/compatibility.html) | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | mode | number |  | 是 | 深度识别模式 | [3.0.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [3.0.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [3.0.0](../../../framework/compatibility.html) | | | | | | | | | | | | | |  | face | Object |  | 否 | 人脸检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/face.html)。安卓微信8.0.25开始支持，iOS微信8.0.24开始支持。 | [2.25.0](../../../framework/compatibility.html) | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | mode | number |  | 是 | 人脸检测模式 | [2.25.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.25.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.25.0](../../../framework/compatibility.html) | | | | | | | | | | | | | |  | OCR | Object |  | 否 | OCR检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/ocr.html)。 | [2.27.0](../../../framework/compatibility.html) | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | mode | number |  | 是 | OCR检测模式 | [2.27.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.27.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.27.0](../../../framework/compatibility.html) | | | | | | | | | | | | | |  | IDCard | Object |  | 否 | 身份证检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/idcard.html)。 | [3.3.0](../../../framework/compatibility.html) | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | mode | number |  | 是 | 身份证检测模式 | [3.3.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 2 | 静态图片检测 | [3.3.0](../../../framework/compatibility.html) | | | | | | | | | | | | | |  | body | Object |  | 否 | 人体检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/body.html)。 | [2.28.0](../../../framework/compatibility.html) | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | mode | number |  | 是 | 人体检测模式 | [2.28.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.28.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.28.0](../../../framework/compatibility.html) | | | | | | | | | | | | | |  | hand | Object |  | 否 | 手势检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/hand.html)。 | [2.28.0](../../../framework/compatibility.html) | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | mode | number |  | 是 | 手势检测模式 | [2.28.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.28.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.28.0](../../../framework/compatibility.html) | | | | | | | | | | | | | |  | shoe | Object |  | 否 | 鞋部检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/shoe.html)。 | [3.2.1](../../../framework/compatibility.html) | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | mode | number |  | 是 | 鞋部检测模式 | [3.2.1](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [3.2.1](../../../framework/compatibility.html) | | | | | | | | | | | | | |  | threeDof | boolean |  | 否 | 提供基础AR功能，输出相机旋转的3个自由度的位姿，利用手机陀螺仪传感器，实现快速稳定的AR定位能力，适用于简单AR场景。 | [2.28.0](../../../framework/compatibility.html) | | | | | | |
|  | gl | WebGLRenderingContext |  | 否 | 绑定的 WebGLRenderingContext 对象 | [2.23.0](../../../framework/compatibility.html) |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| v1 | v1适用于用户在平面场景下，例如桌面，地面，泛平面场景，放置虚拟物体，不提供真实世界距离。用户放置物体时，手机相机倾斜向下对着目标平面点击即可，具有广泛的机型支持 |
| v2 | v2提供真实物理距离的 ar 定位功能，提供平面识别功能，用户在平面范围点击放置虚拟物体的功能，具有[有限的机型支持](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html#%E9%99%84%E5%BD%95)。iOS 设备在基础库 2.22.0 开始支持v2。安卓设备在基础库 2.25.1 开始支持v2，另外，安卓v2不支持竖直平面。\*\*使用v2算法需要初始化，移动手机进行左右平移初始化效果最佳。\*\* |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | plane | Object |  | 是 | 平面跟踪配置 |  |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | mode | number |  | 是 | 平面跟踪配置模式 |  | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 检测横向平面 |  | | 2 | 检测纵向平面，只有 v2 版本支持 | [2.22.0](../../../framework/compatibility.html) | | 3 | 检测横向和纵向平面，只有 v2 版本支持 | [2.22.0](../../../framework/compatibility.html) | | | | | | | |  | force | boolean | false | 否 | 是否开启强制使用V2的模式，只有 v2 版本支持 | [3.6.5](../../../framework/compatibility.html) | | | | | | |
|  | marker | boolean |  | 否 | marker 跟踪配置，基础库(3.0.0)开始允许同时支持v2的水平面检测能力 | [2.24.5](../../../framework/compatibility.html) |
|  | OSD | boolean |  | 否 | OSD 跟踪配置 | [2.24.5](../../../framework/compatibility.html) |
|  | depth | Object |  | 否 | 深度识别配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/depth.html)。 | [3.0.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | mode | number |  | 是 | 深度识别模式 | [3.0.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [3.0.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [3.0.0](../../../framework/compatibility.html) | | | | | | | | | | | | |
|  | face | Object |  | 否 | 人脸检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/face.html)。安卓微信8.0.25开始支持，iOS微信8.0.24开始支持。 | [2.25.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | mode | number |  | 是 | 人脸检测模式 | [2.25.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.25.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.25.0](../../../framework/compatibility.html) | | | | | | | | | | | | |
|  | OCR | Object |  | 否 | OCR检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/ocr.html)。 | [2.27.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | mode | number |  | 是 | OCR检测模式 | [2.27.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.27.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.27.0](../../../framework/compatibility.html) | | | | | | | | | | | | |
|  | IDCard | Object |  | 否 | 身份证检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/idcard.html)。 | [3.3.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | mode | number |  | 是 | 身份证检测模式 | [3.3.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 2 | 静态图片检测 | [3.3.0](../../../framework/compatibility.html) | | | | | | | | | | | | |
|  | body | Object |  | 否 | 人体检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/body.html)。 | [2.28.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | mode | number |  | 是 | 人体检测模式 | [2.28.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.28.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.28.0](../../../framework/compatibility.html) | | | | | | | | | | | | |
|  | hand | Object |  | 否 | 手势检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/hand.html)。 | [2.28.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | mode | number |  | 是 | 手势检测模式 | [2.28.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.28.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.28.0](../../../framework/compatibility.html) | | | | | | | | | | | | |
|  | shoe | Object |  | 否 | 鞋部检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/shoe.html)。 | [3.2.1](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | mode | number |  | 是 | 鞋部检测模式 | [3.2.1](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [3.2.1](../../../framework/compatibility.html) | | | | | | | | | | | | |
|  | threeDof | boolean |  | 否 | 提供基础AR功能，输出相机旋转的3个自由度的位姿，利用手机陀螺仪传感器，实现快速稳定的AR定位能力，适用于简单AR场景。 | [2.28.0](../../../framework/compatibility.html) |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | mode | number |  | 是 | 平面跟踪配置模式 |  |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 检测横向平面 |  | | 2 | 检测纵向平面，只有 v2 版本支持 | [2.22.0](../../../framework/compatibility.html) | | 3 | 检测横向和纵向平面，只有 v2 版本支持 | [2.22.0](../../../framework/compatibility.html) | | | | | | |
|  | force | boolean | false | 否 | 是否开启强制使用V2的模式，只有 v2 版本支持 | [3.6.5](../../../framework/compatibility.html) |

**Object object**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| 1 | 检测横向平面 |  |
| 2 | 检测纵向平面，只有 v2 版本支持 | [2.22.0](../../../framework/compatibility.html) |
| 3 | 检测横向和纵向平面，只有 v2 版本支持 | [2.22.0](../../../framework/compatibility.html) |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | mode | number |  | 是 | 深度识别模式 | [3.0.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [3.0.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [3.0.0](../../../framework/compatibility.html) | | | | | | |

**Object object**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| 1 | 通过摄像头实时检测 | [3.0.0](../../../framework/compatibility.html) |
| 2 | 静态图片检测 | [3.0.0](../../../framework/compatibility.html) |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | mode | number |  | 是 | 人脸检测模式 | [2.25.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.25.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.25.0](../../../framework/compatibility.html) | | | | | | |

**Object object**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| 1 | 通过摄像头实时检测 | [2.25.0](../../../framework/compatibility.html) |
| 2 | 静态图片检测 | [2.25.0](../../../framework/compatibility.html) |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | mode | number |  | 是 | OCR检测模式 | [2.27.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.27.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.27.0](../../../framework/compatibility.html) | | | | | | |

**Object object**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| 1 | 通过摄像头实时检测 | [2.27.0](../../../framework/compatibility.html) |
| 2 | 静态图片检测 | [2.27.0](../../../framework/compatibility.html) |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | mode | number |  | 是 | 身份证检测模式 | [3.3.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 2 | 静态图片检测 | [3.3.0](../../../framework/compatibility.html) | | | | | | |

**Object object**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| 2 | 静态图片检测 | [3.3.0](../../../framework/compatibility.html) |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | mode | number |  | 是 | 人体检测模式 | [2.28.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.28.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.28.0](../../../framework/compatibility.html) | | | | | | |

**Object object**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| 1 | 通过摄像头实时检测 | [2.28.0](../../../framework/compatibility.html) |
| 2 | 静态图片检测 | [2.28.0](../../../framework/compatibility.html) |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | mode | number |  | 是 | 手势检测模式 | [2.28.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.28.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.28.0](../../../framework/compatibility.html) | | | | | | |

**Object object**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| 1 | 通过摄像头实时检测 | [2.28.0](../../../framework/compatibility.html) |
| 2 | 静态图片检测 | [2.28.0](../../../framework/compatibility.html) |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | mode | number |  | 是 | 鞋部检测模式 | [3.2.1](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [3.2.1](../../../framework/compatibility.html) | | | | | | |

**Object object**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| 1 | 通过摄像头实时检测 | [3.2.1](../../../framework/compatibility.html) |

---

### VKBodyAnchor

基础库 2.28.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKBodyAnchor.html

**number type**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 5 | 人体 |  |

**Object size**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 宽度 |
| height | number | 高度 |

**Object origin**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| x | number | 横坐标 |
| y | number | 纵坐标 |

**Array.<Object> points**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| x | number | 横坐标 |
| y | number | 纵坐标 |

---

### VKCamera

基础库 2.20.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKCamera.html

---

### Float32Array VKCamera.getProjectionMatrix(number near, number far)

基础库 2.20.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKCamera.getProjectionMatrix.html

---

### VKDepthAnchor

基础库 2.33.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKDepthAnchor.html

**number type**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 8 | DEPTH |  |

**Object size**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 宽度 |
| height | number | 高度 |

---

### VKFaceAnchor

基础库 2.25.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKFaceAnchor.html

**number type**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 3 | 人脸 |  |

**Object origin**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| x | number | 横坐标 |
| y | number | 纵坐标 |

**Object size**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 宽度 |
| height | number | 高度 |

**Array.<Object> points**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| x | number | 横坐标 |
| y | number | 纵坐标 |

---

### VKFrame

基础库 2.20.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKFrame.html

---

### ArrayBuffer VKFrame.getCameraBuffer(number width, number height)

基础库 2.24.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKFrame.getCameraBuffer.html

---

### ArrayBuffer VKFrame.getCameraJpgBuffer(number width, number height, number quality)

基础库 3.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKFrame.getCameraJpgBuffer.html

---

### Object VKFrame.getCameraTexture(WebGLRenderingContext gl)

基础库 2.20.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKFrame.getCameraTexture.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| yTexture | WebGLTexture | Y 分量纹理 |
| uvTexture | WebGLTexture | UV 分量纹理 |

---

### Object VKFrame.getDepthBuffer()

基础库 3.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKFrame.getDepthBuffer.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 深度纹理宽 |
| height | number | 深度纹理高 |
| DepthAddress | ArrayBuffer | 深度纹理buffer |

---

### Float32Array VKFrame.getDisplayTransform()

基础库 2.20.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKFrame.getDisplayTransform.html

---

### Object VKFrame.getLegSegmentBuffer()

基础库 3.2.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKFrame.getLegSegmentBuffer.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 腿部分割纹理宽 |
| height | number | 腿部分割纹理高 |
| DepthAddress | ArrayBuffer | 腿部分割纹理buffer，width \* height 大小的 裁剪值（0 为不是脚，越靠近 255 越接近腿部区域）（uint8） |

---

### VKHandAnchor

基础库 2.28.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKHandAnchor.html

**number type**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 7 | 手势 |  |

**Object size**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 宽度 |
| height | number | 高度 |

**Object origin**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| x | number | 横坐标 |
| y | number | 纵坐标 |

**Array.<Object> points**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| x | number | 横坐标 |
| y | number | 纵坐标 |

**number gesture**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 0 | 单手比心 |  |
| 1 | 布（数字5） |  |
| 2 | 剪刀（数字2） |  |
| 3 | 握拳 |  |
| 4 | 数字1 |  |
| 5 | 热爱 |  |
| 6 | 点赞 |  |
| 7 | 数字3 |  |
| 8 | 摇滚 |  |
| 9 | 数字6 |  |
| 10 | 数字8 |  |
| 11 | 双手抱拳（恭喜发财） |  |
| 12 | 数字4 |  |
| 13 | 比ok |  |
| 14 | 不喜欢（踩） |  |
| 15 | 双手比心 |  |
| 16 | 祈祷（双手合十） |  |
| 17 | 双手抱拳 |  |
| 18 | 无手势动作 |  |
| -1 | 无效手势 |  |

---

### VKMarkerAnchor

基础库 2.24.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKMarkerAnchor.html

**number type**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 1 | marker |  |

---

### VKOCRAnchor

基础库 2.27.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKOCRAnchor.html

**number type**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 6 | OCR |  |

---

### VKOSDAnchor

基础库 2.24.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKOSDAnchor.html

**number type**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 2 | OSD |  |

**Object size**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 宽度 |
| height | number | 高度 |

**Object origin**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| x | number | 横坐标 |
| y | number | 纵坐标 |

---

### VKPlaneAnchor

基础库 2.22.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKPlaneAnchor.html

**number type**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 0 | 平面 |  |

**Object size**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 宽度 |
| height | number | 高度 |

---

### VKSession

基础库 2.20.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.html

**number state**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 0 | 不可用 |  |
| 1 | 运行中 |  |
| 2 | 暂停中 |  |
| 3 | 初始化中 | [2.29.0](../../../framework/compatibility.html) |

**Object config**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | version | string | vision kit 版本。 | [2.22.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | v1 | v1适用于用户在平面场景下，例如桌面，地面，泛平面场景，放置虚拟物体，不提供真实世界距离。用户放置物体时，手机相机倾斜向下对着目标平面点击即可，具有广泛的机型支持 | | v2 | v2提供真实物理距离的 ar 定位功能，提供平面识别功能，用户在平面范围点击放置虚拟物体的功能，具有[有限的机型支持](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html#%E9%99%84%E5%BD%95)。iOS 设备在基础库 2.22.0 开始支持v2。安卓设备在基础库 2.25.1 开始支持v2，另外，安卓v2不支持竖直平面。\*\*使用v2算法需要初始化，移动手机进行左右平移初始化效果最佳。\*\* | | | | |
|  | track | Object | 跟踪能力配置，目前不同的跟踪能力之间是互斥的，默认使用平面跟踪能力。需要注意目前 track 中不同的跟踪配置存在互斥关系（比如 marker 跟踪配置和 OSD 跟踪配置不能同时存在），请按需配置。 |  |
|  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | plane | Object | 平面跟踪配置 |  | |  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | mode | number | 平面跟踪配置模式 |  | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 检测横向平面 |  | | 2 | 检测纵向平面，只有 v2 版本支持 | [2.22.0](../../../framework/compatibility.html) | | 3 | 检测横向和纵向平面，只有 v2 版本支持 | [2.22.0](../../../framework/compatibility.html) | | | | | |  | force | boolean | 是否开启强制使用V2的模式，只有 v2 版本支持 | [3.6.5](../../../framework/compatibility.html) | | | | | |  | marker | boolean | marker 跟踪配置，基础库(3.0.0)开始允许同时支持v2的水平面检测能力 | [2.24.5](../../../framework/compatibility.html) | |  | OSD | boolean | OSD 跟踪配置 | [2.24.5](../../../framework/compatibility.html) | |  | depth | Object | 深度识别配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/depth.html)。 | [3.0.0](../../../framework/compatibility.html) | |  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | mode | number | 深度识别模式 | [3.0.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [3.0.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [3.0.0](../../../framework/compatibility.html) | | | | | | | | | |  | face | Object | 人脸检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/face.html)。安卓微信8.0.25开始支持，iOS微信8.0.24开始支持。 | [2.25.0](../../../framework/compatibility.html) | |  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | mode | number | 人脸检测模式 | [2.25.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.25.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.25.0](../../../framework/compatibility.html) | | | | | | | | | |  | OCR | Object | OCR检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/ocr.html)。 | [2.27.0](../../../framework/compatibility.html) | |  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | mode | number | OCR检测模式 | [2.27.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.27.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.27.0](../../../framework/compatibility.html) | | | | | | | | | |  | IDCard | Object | 身份证检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/idcard.html)。 | [3.3.0](../../../framework/compatibility.html) | |  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | mode | number | 身份证检测模式 | [3.3.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 2 | 静态图片检测 | [3.3.0](../../../framework/compatibility.html) | | | | | | | | | |  | body | Object | 人体检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/body.html)。 | [2.28.0](../../../framework/compatibility.html) | |  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | mode | number | 人体检测模式 | [2.28.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.28.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.28.0](../../../framework/compatibility.html) | | | | | | | | | |  | hand | Object | 手势检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/hand.html)。 | [2.28.0](../../../framework/compatibility.html) | |  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | mode | number | 手势检测模式 | [2.28.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.28.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.28.0](../../../framework/compatibility.html) | | | | | | | | | |  | shoe | Object | 鞋部检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/shoe.html)。 | [3.2.1](../../../framework/compatibility.html) | |  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | mode | number | 鞋部检测模式 | [3.2.1](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [3.2.1](../../../framework/compatibility.html) | | | | | | | | | |  | threeDof | boolean | 提供基础AR功能，输出相机旋转的3个自由度的位姿，利用手机陀螺仪传感器，实现快速稳定的AR定位能力，适用于简单AR场景。 | [2.28.0](../../../framework/compatibility.html) | | | | |
|  | gl | WebGLRenderingContext | 绑定的 WebGLRenderingContext 对象 | [2.23.0](../../../framework/compatibility.html) |

**Object config**

| 合法值 | 说明 |
| --- | --- |
| v1 | v1适用于用户在平面场景下，例如桌面，地面，泛平面场景，放置虚拟物体，不提供真实世界距离。用户放置物体时，手机相机倾斜向下对着目标平面点击即可，具有广泛的机型支持 |
| v2 | v2提供真实物理距离的 ar 定位功能，提供平面识别功能，用户在平面范围点击放置虚拟物体的功能，具有[有限的机型支持](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html#%E9%99%84%E5%BD%95)。iOS 设备在基础库 2.22.0 开始支持v2。安卓设备在基础库 2.25.1 开始支持v2，另外，安卓v2不支持竖直平面。\*\*使用v2算法需要初始化，移动手机进行左右平移初始化效果最佳。\*\* |

**Object config**

|  | 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | plane | Object | 平面跟踪配置 |  |
|  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | mode | number | 平面跟踪配置模式 |  | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 检测横向平面 |  | | 2 | 检测纵向平面，只有 v2 版本支持 | [2.22.0](../../../framework/compatibility.html) | | 3 | 检测横向和纵向平面，只有 v2 版本支持 | [2.22.0](../../../framework/compatibility.html) | | | | | |  | force | boolean | 是否开启强制使用V2的模式，只有 v2 版本支持 | [3.6.5](../../../framework/compatibility.html) | | | | |
|  | marker | boolean | marker 跟踪配置，基础库(3.0.0)开始允许同时支持v2的水平面检测能力 | [2.24.5](../../../framework/compatibility.html) |
|  | OSD | boolean | OSD 跟踪配置 | [2.24.5](../../../framework/compatibility.html) |
|  | depth | Object | 深度识别配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/depth.html)。 | [3.0.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | mode | number | 深度识别模式 | [3.0.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [3.0.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [3.0.0](../../../framework/compatibility.html) | | | | | | | | |
|  | face | Object | 人脸检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/face.html)。安卓微信8.0.25开始支持，iOS微信8.0.24开始支持。 | [2.25.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | mode | number | 人脸检测模式 | [2.25.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.25.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.25.0](../../../framework/compatibility.html) | | | | | | | | |
|  | OCR | Object | OCR检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/ocr.html)。 | [2.27.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | mode | number | OCR检测模式 | [2.27.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.27.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.27.0](../../../framework/compatibility.html) | | | | | | | | |
|  | IDCard | Object | 身份证检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/idcard.html)。 | [3.3.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | mode | number | 身份证检测模式 | [3.3.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 2 | 静态图片检测 | [3.3.0](../../../framework/compatibility.html) | | | | | | | | |
|  | body | Object | 人体检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/body.html)。 | [2.28.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | mode | number | 人体检测模式 | [2.28.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.28.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.28.0](../../../framework/compatibility.html) | | | | | | | | |
|  | hand | Object | 手势检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/hand.html)。 | [2.28.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | mode | number | 手势检测模式 | [2.28.0](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.28.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.28.0](../../../framework/compatibility.html) | | | | | | | | |
|  | shoe | Object | 鞋部检测配置。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/shoe.html)。 | [3.2.1](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | |  | mode | number | 鞋部检测模式 | [3.2.1](../../../framework/compatibility.html) | |  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [3.2.1](../../../framework/compatibility.html) | | | | | | | | |
|  | threeDof | boolean | 提供基础AR功能，输出相机旋转的3个自由度的位姿，利用手机陀螺仪传感器，实现快速稳定的AR定位能力，适用于简单AR场景。 | [2.28.0](../../../framework/compatibility.html) |

**Object config**

|  | 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | mode | number | 平面跟踪配置模式 |  |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 检测横向平面 |  | | 2 | 检测纵向平面，只有 v2 版本支持 | [2.22.0](../../../framework/compatibility.html) | | 3 | 检测横向和纵向平面，只有 v2 版本支持 | [2.22.0](../../../framework/compatibility.html) | | | | |
|  | force | boolean | 是否开启强制使用V2的模式，只有 v2 版本支持 | [3.6.5](../../../framework/compatibility.html) |

**Object config**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| 1 | 检测横向平面 |  |
| 2 | 检测纵向平面，只有 v2 版本支持 | [2.22.0](../../../framework/compatibility.html) |
| 3 | 检测横向和纵向平面，只有 v2 版本支持 | [2.22.0](../../../framework/compatibility.html) |

**Object config**

|  | 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | mode | number | 深度识别模式 | [3.0.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [3.0.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [3.0.0](../../../framework/compatibility.html) | | | | |

**Object config**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| 1 | 通过摄像头实时检测 | [3.0.0](../../../framework/compatibility.html) |
| 2 | 静态图片检测 | [3.0.0](../../../framework/compatibility.html) |

**Object config**

|  | 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | mode | number | 人脸检测模式 | [2.25.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.25.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.25.0](../../../framework/compatibility.html) | | | | |

**Object config**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| 1 | 通过摄像头实时检测 | [2.25.0](../../../framework/compatibility.html) |
| 2 | 静态图片检测 | [2.25.0](../../../framework/compatibility.html) |

**Object config**

|  | 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | mode | number | OCR检测模式 | [2.27.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.27.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.27.0](../../../framework/compatibility.html) | | | | |

**Object config**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| 1 | 通过摄像头实时检测 | [2.27.0](../../../framework/compatibility.html) |
| 2 | 静态图片检测 | [2.27.0](../../../framework/compatibility.html) |

**Object config**

|  | 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | mode | number | 身份证检测模式 | [3.3.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 2 | 静态图片检测 | [3.3.0](../../../framework/compatibility.html) | | | | |

**Object config**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| 2 | 静态图片检测 | [3.3.0](../../../framework/compatibility.html) |

**Object config**

|  | 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | mode | number | 人体检测模式 | [2.28.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.28.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.28.0](../../../framework/compatibility.html) | | | | |

**Object config**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| 1 | 通过摄像头实时检测 | [2.28.0](../../../framework/compatibility.html) |
| 2 | 静态图片检测 | [2.28.0](../../../framework/compatibility.html) |

**Object config**

|  | 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | mode | number | 手势检测模式 | [2.28.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [2.28.0](../../../framework/compatibility.html) | | 2 | 静态图片检测 | [2.28.0](../../../framework/compatibility.html) | | | | |

**Object config**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| 1 | 通过摄像头实时检测 | [2.28.0](../../../framework/compatibility.html) |
| 2 | 静态图片检测 | [2.28.0](../../../framework/compatibility.html) |

**Object config**

|  | 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | mode | number | 鞋部检测模式 | [3.2.1](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | 1 | 通过摄像头实时检测 | [3.2.1](../../../framework/compatibility.html) | | | | |

**Object config**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| 1 | 通过摄像头实时检测 | [3.2.1](../../../framework/compatibility.html) |

**Object cameraSize**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 宽度 |
| height | number | 高度 |

---

### number VKSession.addMarker(string path)

基础库 2.24.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.addMarker.html

---

### number VKSession.addOSDMarker(string path)

基础库 2.24.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.addOSDMarker.html

---

### VKSession.cancelAnimationFrame(number requestID)

基础库 2.20.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.cancelAnimationFrame.html

---

### VKSession.destroy()

基础库 2.20.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.destroy.html

---

### VKSession.detectBody(Object object)

基础库 2.28.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.detectBody.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | frameBuffer | ArrayBuffer |  | 是 | 人脸图像像素点数据，每四项表示一个像素点的 RGBA |
|  | width | number |  | 是 | 图像宽度 |
|  | height | number |  | 是 | 图像高度 |
|  | scoreThreshold | number | 0.8 | 否 | 评分阈值。正常情况传入 0.8 即可。 |
|  | sourceType | number | 1 | 否 | 图像源类型。正常情况传入 1 即可。当输入的图片是来自一个连续视频的每一帧图像时，sourceType 传入 0 会得到更优的效果 |
|  | | 合法值 | 说明 | | --- | --- | | 1 | 表示输入的图片是随机的图片 | | 0 | 表示输入的图片是来自一个连续视频的每一帧图像 | | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 1 | 表示输入的图片是随机的图片 |
| 0 | 表示输入的图片是来自一个连续视频的每一帧图像 |

---

### VKSession.detectDepth(Object object)

基础库 2.33.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.detectDepth.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| frameBuffer | ArrayBuffer |  | 是 | 需要识别深度的图像像素点数据，每四项表示一个像素点的 RGBA |
| width | number |  | 是 | 图像宽度 |
| height | number |  | 是 | 图像高度 |

---

### VKSession.detectFace(Object object)

基础库 2.25.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.detectFace.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | frameBuffer | ArrayBuffer |  | 是 | 人脸图像像素点数据，每四项表示一个像素点的 RGBA |
|  | width | number |  | 是 | 图像宽度 |
|  | height | number |  | 是 | 图像高度 |
|  | scoreThreshold | number | 0.8 | 否 | 评分阈值。正常情况传入 0.8 即可。 |
|  | sourceType | number | 1 | 否 | 图像源类型。正常情况传入 1 即可。当输入的图片是来自一个连续视频的每一帧图像时，sourceType 传入 0 会得到更优的效果 |
|  | | 合法值 | 说明 | | --- | --- | | 1 | 表示输入的图片是随机的图片 | | 0 | 表示输入的图片是来自一个连续视频的每一帧图像 | | | | | |
|  | modelModel | number | 1 | 否 | 算法模型类型。正常情况传入 1 即可。0、1、2 分别表示小、中、大模型，模型越大识别准确率越高，但资源占用也越高。建议根据用户设备性能进行选择。 |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 小模型 | | 1 | 中模型 | | 2 | 大模型 | | | | | |
|  | pupilInfo | boolean | false | 否 | 是否返回瞳孔周围点信息，默认为 false。 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 1 | 表示输入的图片是随机的图片 |
| 0 | 表示输入的图片是来自一个连续视频的每一帧图像 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 0 | 小模型 |
| 1 | 中模型 |
| 2 | 大模型 |

---

### VKSession.detectHand(Object object)

基础库 2.28.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.detectHand.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | frameBuffer | ArrayBuffer |  | 是 | 人脸图像像素点数据，每四项表示一个像素点的 RGBA |
|  | width | number |  | 是 | 图像宽度 |
|  | height | number |  | 是 | 图像高度 |
|  | scoreThreshold | number | 0.8 | 否 | 评分阈值。正常情况传入 0.8 即可。 |
|  | algoMode | number |  | 否 | 算法检测模式 |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 检测模式，输出框和点 | | 1 | 手势模式，输出框和手势分类 | | 2 | 结合0和1模式，输出框、点、手势分类 | | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 0 | 检测模式，输出框和点 |
| 1 | 手势模式，输出框和手势分类 |
| 2 | 结合0和1模式，输出框、点、手势分类 |

---

### Array.<Object> VKSession.getAllMarker()

基础库 2.24.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.getAllMarker.html

**Array.<Object>**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| markerId | number | marker id |
| path | string | 图片路径 |

---

### Array.<Object> VKSession.getAllOSDMarker()

基础库 2.24.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.getAllOSDMarker.html

**Array.<Object>**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| markerId | number | marker id |
| path | string | 图片路径 |

---

### VKFrame VKSession.getVKFrame(number width, number height)

基础库 2.20.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.getVKFrame.html

---

### Array.<Object> VKSession.hitTest(number x, number y, Object reset)

基础库 2.20.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.hitTest.html

**Array.<Object>**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| transform | Float32Array | 包含位置、旋转、放缩信息的矩阵，以列为主序 |

---

### VKSession.off(string eventName, function fn)

基础库 2.20.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.off.html

---

### VKSession.on(string eventName, function fn)

基础库 2.20.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.on.html

**string eventName**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| resize | 相机尺寸变化事件，回调参数为相机尺寸 |  |
| addAnchors | 增加 anchor 事件，回调参数为 [VKPlaneAnchor](VKPlaneAnchor.html)/[VKMarkerAnchor](VKMarkerAnchor.html)/[VKOSDAnchor](VKOSDAnchor.html) 列表（只有v2版本支持） 或 [VKFaceAnchor](VKFaceAnchor.html)/[VKOCRAnchor](VKOCRAnchor.html)/[VKHandAnchor](VKHandAnchor.html)/[VKBodyAnchor](VKBodyAnchor.html)列表（v1、v2都支持） | [2.22.0](../../../framework/compatibility.html) |
| updateAnchors | 更新 anchor 事件，回调参数为 [VKPlaneAnchor](VKPlaneAnchor.html)/[VKMarkerAnchor](VKMarkerAnchor.html)/[VKOSDAnchor](VKOSDAnchor.html) 列表（只有v2版本支持） 或 [VKFaceAnchor](VKFaceAnchor.html)/[VKOCRAnchor](VKOCRAnchor.html)/[VKHandAnchor](VKHandAnchor.html)/[VKBodyAnchor](VKBodyAnchor.html)列表（v1、v2都支持） | [2.22.0](../../../framework/compatibility.html) |
| removeAnchors | 删除 anchor 事件，回调参数为 [VKPlaneAnchor](VKPlaneAnchor.html)/[VKMarkerAnchor](VKMarkerAnchor.html)/[VKOSDAnchor](VKOSDAnchor.html) 列表（只有v2版本支持） 或 [VKFaceAnchor](VKFaceAnchor.html)/[VKOCRAnchor](VKOCRAnchor.html)/[VKHandAnchor](VKHandAnchor.html)/[VKBodyAnchor](VKBodyAnchor.html) 列表（v1、v2都支持） | [2.22.0](../../../framework/compatibility.html) |

---

### VKSession.removeMarker(number markerId)

基础库 2.24.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.removeMarker.html

---

### VKSession.removeOSDMarker(number markerId)

基础库 2.24.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.removeOSDMarker.html

---

### number VKSession.requestAnimationFrame(function callback)

基础库 2.20.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.requestAnimationFrame.html

---

### VKSession.runOCR(Object object)

基础库 2.27.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.runOCR.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| frameBuffer | ArrayBuffer |  | 是 | 待识别图像的像素点数据，每四项表示一个像素点的 RGBA |
| width | number |  | 是 | 图像宽度 |
| height | number |  | 是 | 图像高度 |

---

### VKSession.setDepthOccRange(number threshold)

基础库 3.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.setDepthOccRange.html

---

### VKSession.start(function callback)

基础库 2.20.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.start.html

**function callback**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 0 | 成功 |  |
| 104 | 用户取消授权 |  |
| 112 | 接口未在隐私协议中声明 |  |
| 1025 | 小程序隐私接口被封禁，[解决方案参考链接](https://developers.weixin.qq.com/community/develop/doc/00062a6d514c88baacdf52e8a56009) |  |
| 1026 | 小游戏隐私接口被封禁，[解决方案参考链接](https://developers.weixin.qq.com/community/minigame/doc/0004c84925817819b7ffd8b2356008) |  |
| 2000001 | 参数错误 |  |
| 2003000 | 会话不可用 |  |
| 2000000 | 系统错误 |  |
| 2000002 | 设备不支持 |  |
| 2000003 | 系统不支持 |  |
| 2000004 | 设备不支持 |  |
| 2003001 | 未开启系统相机权限 |  |
| 2003002 | 未开启小程序相机权限 |  |

---

### VKSession.stop()

基础库 2.20.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.stop.html

---

### VKSession.update3DMode(Object object)

基础库 2.30.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.update3DMode.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| open3d | boolean |  | 是 | 是否开启三维识别 |

---

### VKSession.updateMaskMode(Object object)

基础库 3.2.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.updateMaskMode.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| useMask | boolean |  | 是 | 设置是否开启试鞋，返回腿部遮挡纹理 |

---

### VKSession.updateOSDThreshold(number threshold)

基础库 2.24.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.updateOSDThreshold.html

---

### wx.stopFaceDetect(Object object)

该接口已停止维护，推荐使用wx.createVKSession代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/face/wx.stopFaceDetect.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.initFaceDetect(Object object)

该接口已停止维护，推荐使用wx.createVKSession代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/face/wx.initFaceDetect.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.faceDetect(Object object)

该接口已停止维护，推荐使用wx.createVKSession代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ai/face/wx.faceDetect.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| frameBuffer | ArrayBuffer |  | 是 | 图像像素点数据，每四项表示一个像素点的 RGBA |
| width | number |  | 是 | 图像宽度 |
| height | number |  | 是 | 图像高度 |
| enablePoint | boolean | false | 否 | 是否返回当前图像的人脸（106 个点） |
| enableConf | boolean | false | 否 | 是否返回当前图像的人脸的置信度（可表示器官遮挡情况） |
| enableAngle | boolean | false | 否 | 是否返回当前图像的人脸角度信息 |
| enableMultiFace | boolean | false | 否 | 是否返回多张人脸的信息 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | detectRect | Object | 脸部方框数值，对象包含 height, width, originX, originY 四个属性 (origin 为方框左上角坐标) |
|  | x | number | 脸部中心点横坐标，检测不到人脸则为 -1 |
|  | y | number | 脸部中心点纵坐标，检测不到人脸则为 -1 |
|  | pointArray | Array.<Object> | 标记人脸轮廓的 106 个点位置数组，数组每个对象包含 x 和 y |
|  | confArray | Object | 人脸置信度，取值范围 [0, 1]，数值越大置信度越高（遮挡越少） |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | global | number | 整体可信度 | |  | leftEye | number | 左眼可信度 | |  | rightEye | number | 右眼可信度 | |  | mouth | number | 嘴巴可信度 | |  | nose | number | 鼻子可信度 | | | |
|  | angleArray | Object | 人脸角度信息，取值范围 [-1, 1]，数值越接近 0 表示越正对摄像头 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | pitch | number | 仰俯角（点头） | |  | yaw | number | 偏航角（摇头） | |  | roll | number | 翻滚角（左右倾） | | | |
|  | faceInfo | Array.<Object> | 多人模式（enableMultiFace）下的人脸信息，每个对象包含上述其它属性 |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | global | number | 整体可信度 |
|  | leftEye | number | 左眼可信度 |
|  | rightEye | number | 右眼可信度 |
|  | mouth | number | 嘴巴可信度 |
|  | nose | number | 鼻子可信度 |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | pitch | number | 仰俯角（点头） |
|  | yaw | number | 偏航角（摇头） |
|  | roll | number | 翻滚角（左右倾） |

---

<!-- pages: 58 -->
