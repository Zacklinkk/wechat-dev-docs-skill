# 微信小程序 API 结构化参考 — skyline

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### DraggableSheetContext.scrollTo(Object object)

基础库 3.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/skyline/DraggableSheetContext.scrollTo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| size | number |  | 否 | 相对目标位置 |
| pixels | number |  | 否 | 绝对目标位置 |
| animated | boolean | true | 否 | 是否启用滚动动画 |
| duration | number | 300 | 否 | 滚动动画时长（ms) |
| easingFunction | string | ease | 否 | 缓动函数 |

---

### DraggableSheetContext

基础库 3.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/skyline/DraggableSheetContext.html

---

### OpenContainer

相关文档:open-container

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/skyline/OpenContainer.html

---

### Snapshot

相关文档:snapshot

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/skyline/Snapshot.html

---

### Snapshot.takeSnapshot(Object object)

基础库 3.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/skyline/Snapshot.takeSnapshot.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| type | String |  | 是 | 截图导出类型，'file' 保存到临时文件目录或 'arraybuffer' 返回图片二进制数据，默认值为 'file' |
| format | String |  | 是 | 截图文件格式，'rgba' 或 'png'，默认值为 'png' |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempFilePath | String | 截图保存的临时文件路径，当 type 为 file 该字段生效 |
| data | ArrayBuffer | 截图对应的二进制数据，当 type 为 arraybuffer 该字段生效 |

---

<!-- pages: 5 -->
