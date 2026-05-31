# 微信小游戏 API 结构化参考 — storage

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.setStorageSync(string key, any data)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/storage/wx.setStorageSync.html

---

### wx.setStorage(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/storage/wx.setStorage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| key | string |  | 是 | 本地缓存中指定的 key |  |
| data | any |  | 是 | 需要存储的内容。只支持原生类型、Date、及能够通过`JSON.stringify`序列化的对象。 |  |
| encrypt | Boolean | false | 否 | 是否开启加密存储。只有异步的 setStorage 接口支持开启加密存储。开启后，将会对 data 使用 AES128 加密，接口回调耗时将会增加。若开启加密存储，setStorage 和 getStorage 需要同时声明 encrypt 的值为 true。此外，由于加密后的数据会比原始数据膨胀1.4倍，因此开启 encrypt 的情况下，单个 key 允许存储的最大数据长度为 0.7MB，所有数据存储上限为 7.1MB | [2.21.3](../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### wx.revokeBufferURL(string url)

基础库 2.14.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/storage/wx.revokeBufferURL.html

---

### wx.removeStorageSync(string key)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/storage/wx.removeStorageSync.html

---

### wx.removeStorage(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/storage/wx.removeStorage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| key | string |  | 是 | 本地缓存中指定的 key |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### any wx.getStorageSync(string key)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/storage/wx.getStorageSync.html

---

### Object wx.getStorageInfoSync()

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/storage/wx.getStorageInfoSync.html

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| keys | Array.<string> | 当前 storage 中所有的 key |
| currentSize | number | 当前占用的空间大小, 单位 KB |
| limitSize | number | 限制的空间大小，单位 KB |

---

### wx.getStorageInfo(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/storage/wx.getStorageInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| keys | Array.<string> | 当前 storage 中所有的 key |
| currentSize | number | 当前占用的空间大小, 单位 KB |
| limitSize | number | 限制的空间大小，单位 KB |

---

### wx.getStorage(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/storage/wx.getStorage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| key | string |  | 是 | 本地缓存中指定的 key |  |
| encrypt | Boolean | false | 否 | 是否开启加密存储。只有异步的 getStorage 接口支持开启加密存储。开启后，将会对 data 使用 AES128 解密，接口回调耗时将会增加。若开启加密存储，setStorage 和 getStorage 需要同时声明 encrypt 的值为 true | [2.21.3](../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | any | key对应的内容 |

---

### string wx.createBufferURL(ArrayBuffer|TypedArray buffer)

基础库 2.14.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/storage/wx.createBufferURL.html

---

### wx.clearStorageSync()

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/storage/wx.clearStorageSync.html

---

### wx.clearStorage(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/storage/wx.clearStorage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.setBackgroundFetchToken(object object)

基础库 3.0.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/storage/background-fetch/wx.setBackgroundFetchToken.html

**object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| token | String |  | 是 | 自定义的登录态。上限 1024 字符。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.onBackgroundFetchData(function listener)

基础库 3.0.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/storage/background-fetch/wx.onBackgroundFetchData.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| fetchType | string | 缓存数据类别，取值为 periodic 或 pre |
| fetchedData | string | 缓存数据 |
| timeStamp | number | 客户端拿到缓存数据的时间戳 |
| path | String | 小游戏页面路径（一般不需要传，除非使用到小游戏独立分包） |
| query | String | 传给页面的 query 参数 |
| scene | Number | 进入小游戏的场景值 |

---

### wx.getBackgroundFetchToken(Object object)

基础库 3.0.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/storage/background-fetch/wx.getBackgroundFetchToken.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| token | String | 自定义的登录态 |
| errMsg | String | 接口调用结果 |

---

### wx.getBackgroundFetchData(object object)

基础库 3.0.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/storage/background-fetch/wx.getBackgroundFetchData.html

**object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| fetchType | String |  | 是 | 缓存数据类别，取值为 periodic 或 pre |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| fetchedData | String | 缓存数据 |
| timeStamp | Number | 客户端拿到缓存数据的时间戳 ms。(iOS 时间戳存在异常，8.0.27 修复) |
| path | String | 小程序页面路径 |
| query | String | 传给页面的 query 参数 |
| scene | Number | 进入小程序的场景值 |

---

<!-- pages: 16 -->
