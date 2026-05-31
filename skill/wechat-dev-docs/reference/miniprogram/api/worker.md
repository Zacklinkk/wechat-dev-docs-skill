# 微信小程序 API 结构化参考 — worker

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### Worker wx.createWorker(string scriptPath, object options)

基础库 1.9.90 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/worker/wx.createWorker.html

**object options**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| useExperimentalWorker | boolean | false | 否 | 是否使用实验worker。在iOS下，实验worker的JS运行效率比非实验worker提升数倍，如需在worker内进行重度计算的建议开启此选项。同时，实验worker存在极小概率会在系统资源紧张时被系统回收，因此建议配合 worker.onProcessKilled 事件使用，在worker被回收后可重新创建一个。 | [2.13.0](../../framework/compatibility.html) |

---

### Worker

相关文档:多线程 Worker

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/worker/Worker.html

**Object env**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| USER\_DATA\_PATH | string | 文件系统中的用户目录路径 (本地路径) |

---

### ArrayBuffer Worker.getCameraFrameData()

基础库 2.25.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/worker/Worker.getCameraFrameData.html

---

### Worker.onError(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/worker/Worker.onError.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| error | Object | 错误对象 |

---

### Worker.onMessage(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/worker/Worker.onMessage.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| message | Object | 主线程/Worker 线程向当前线程发送的消息 |

---

### Worker.onProcessKilled(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/worker/Worker.onProcessKilled.html

---

### Worker.postMessage(Object message)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/worker/Worker.postMessage.html

---

### Worker.terminate()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/worker/Worker.terminate.html

---

### Worker.testOnProcessKilled()

基础库 2.27.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/worker/Worker.testOnProcessKilled.html

---

<!-- pages: 9 -->
