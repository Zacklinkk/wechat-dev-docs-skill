# 微信小程序 API 结构化参考 — storage

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.setStorageSync(string key, any data)

小程序插件：支持，需要小程序基础库版本不低于1.9.6

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.setStorageSync.html

---

### wx.setStorage(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.setStorage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| key | string |  | 是 | 本地缓存中指定的 key |  |
| data | any |  | 是 | 需要存储的内容。只支持原生类型、Date、及能够通过`JSON.stringify`序列化的对象。 |  |
| encrypt | Boolean | false | 否 | 是否开启加密存储。只有异步的 setStorage 接口支持开启加密存储。开启后，将会对 data 使用 AES128 加密，接口回调耗时将会增加。若开启加密存储，setStorage 和 getStorage 需要同时声明 encrypt 的值为 true。此外，由于加密后的数据会比原始数据膨胀1.4倍，因此开启 encrypt 的情况下，单个 key 允许存储的最大数据长度为 0.7MB，所有数据存储上限为 7.1MB | [2.21.3](../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### wx.revokeBufferURL(string url)

基础库 2.14.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.revokeBufferURL.html

---

### wx.removeStorageSync(string key)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.removeStorageSync.html

---

### wx.removeStorage(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.removeStorage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| key | string |  | 是 | 本地缓存中指定的 key |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### any wx.getStorageSync(string key)

小程序插件：支持，需要小程序基础库版本不低于1.9.6

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.getStorageSync.html

---

### Object wx.getStorageInfoSync()

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.getStorageInfoSync.html

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| keys | Array.<string> | 当前 storage 中所有的 key |
| currentSize | number | 当前占用的空间大小, 单位 KB |
| limitSize | number | 限制的空间大小，单位 KB |

---

### wx.getStorageInfo(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.getStorageInfo.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.getStorage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| key | string |  | 是 | 本地缓存中指定的 key |  |
| encrypt | Boolean | false | 否 | 是否开启加密存储。只有异步的 getStorage 接口支持开启加密存储。开启后，将会对 data 使用 AES128 解密，接口回调耗时将会增加。若开启加密存储，setStorage 和 getStorage 需要同时声明 encrypt 的值为 true | [2.21.3](../../framework/compatibility.html) |
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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.createBufferURL.html

---

### wx.clearStorageSync()

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.clearStorageSync.html

---

### wx.clearStorage(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.clearStorage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.batchSetStorageSync(Array.<Object> kvList)

基础库 2.25.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.batchSetStorageSync.html

**Array.<Object> kvList**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| key | string |  | 是 | key 本地缓存中指定的 key |
| value | any |  | 是 | data 需要存储的内容。只支持原生类型、Date、及能够通过`JSON.stringify`序列化的对象。 |

---

### wx.batchSetStorage(Object object)

基础库 2.25.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.batchSetStorage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| kvList | Array |  | 是 | [{ key, value }] |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### Array.<any> wx.batchGetStorageSync(Array.<string> keyList)

基础库 2.25.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.batchGetStorageSync.html

---

### wx.batchGetStorage(Object object)

基础库 2.25.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.batchGetStorage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyList | Array.<string> |  | 是 | 本地缓存中指定的 keyList |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.setBackgroundFetchToken(object object)

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/background-fetch/wx.setBackgroundFetchToken.html

**object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| token | String |  | 是 | 自定义的登录态。上限 1024 字符。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.onBackgroundFetchData(function listener)

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/background-fetch/wx.onBackgroundFetchData.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| fetchType | string | 缓存数据类别，取值为 periodic 或 pre |
| fetchedData | string | 缓存数据 |
| timeStamp | number | 客户端拿到缓存数据的时间戳 |
| path | String | 小程序页面路径 |
| query | String | 传给页面的 query 参数 |
| scene | Number | 进入小程序的场景值 |

---

### wx.getBackgroundFetchToken(Object object)

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/background-fetch/wx.getBackgroundFetchToken.html

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

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/background-fetch/wx.getBackgroundFetchData.html

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

### CacheManager wx.createCacheManager(Object object)

基础库 2.24.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/wx.createCacheManager.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | origin | string |  | 否 | 全局 origin |
|  | mode | string | weakNetwork | 否 | 缓存模式 |
|  | | 合法值 | 说明 | | --- | --- | | weakNetwork | 弱网/离线使用缓存返回 | | always | 总是使用缓存返回 | | none | 不开启，后续可手动开启/停止使用缓存返回 | | | | | |
|  | maxAge | number |  | 否 | 全局缓存有效时间，单位为毫秒，默认为 7 天，最长不超过 30 天 |
|  | extra | object |  | 否 | 额外的缓存处理 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | apiList | Array.<string> |  | 否 | 需要缓存的 wx api 接口，不传则表示支持缓存的接口全都做缓存处理。返回的如果是缓存数据，开发者可通过 fromCache 标记区分 | |  | | 合法值 | 说明 | | --- | --- | | wx.login |  | | wx.checkSession |  | | wx.getSetting |  | | | | | | | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| weakNetwork | 弱网/离线使用缓存返回 |
| always | 总是使用缓存返回 |
| none | 不开启，后续可手动开启/停止使用缓存返回 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | apiList | Array.<string> |  | 否 | 需要缓存的 wx api 接口，不传则表示支持缓存的接口全都做缓存处理。返回的如果是缓存数据，开发者可通过 fromCache 标记区分 |
|  | | 合法值 | 说明 | | --- | --- | | wx.login |  | | wx.checkSession |  | | wx.getSetting |  | | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| wx.login |  |
| wx.checkSession |  |
| wx.getSetting |  |

---

### CacheManager

基础库 2.24.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/CacheManager.html

**string mode**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| weakNetwork | 默认值，弱网/离线使用缓存返回 |  |
| always | 总是使用缓存返回 |  |
| none | 不开启，后续可手动开启/停止使用缓存返回 |  |

**number state**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 0 | 不使用缓存返回 |  |
| 1 | 使用缓存返回 |  |
| 2 | 未知 |  |

---

### string CacheManager.addRule(string|RegExp|Record.<string, any> rule)

基础库 2.24.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/CacheManager.addRule.html

**对象写法**

| 属性名 | 类型 | 默认值 | 备注 |
| --- | --- | --- | --- |
| id | string |  | 规则 id，如果不填则会由基础库生成 |
| method | string |  | 请求方法，可选值 GET/POST/PATCH/PUT/DELETE，如果为空则表示前面提到的所有方法都能被匹配到 |
| url | any | 必填 | uri 匹配规则，可参考规则字符串写法和正则写法 |
| maxAge | number | 7 \* 24 \* 60 \* 60 \* 1000 | 缓存有效时间，单位为 ms，不填则默认取缓存管理器全局的缓存有效时间 |
| dataSchema | Array<DataRule> |  | 匹配请求参数 |

**对象写法**

| 属性名 | 类型 | 默认值 | 备注 |
| --- | --- | --- | --- |
| name | string |  | 需要匹配的参数名 |
| schema | DataSchema/Array<DataSchema> | 需要匹配的参数模式，支持数组，表示该参数值有多种模式 |  |

**对象写法**

| 属性名 | 类型 | 默认值 | 备注 |
| --- | --- | --- | --- |
| type | string |  | 需要匹配的 data 对象的参数类型，string、number、boolean、null、object、any（表示任意类型），同时支持数组模式（数组模式则在类型后面加 []，如 string[] 表示字符串数组） |
| value | string/regexp/function/Array<DataRule> |  | 需要匹配的 data 对象的参数值，当 type 为基本类型时，可以用 string/regexp 来匹配固定的值，也可以通过 function 来确定值是否匹配，如果传入的 type 是 object，那么表示需要嵌套匹配值是否正确，可以传入 Array |

---

### Array.<string> CacheManager.addRules(Array.<(string|RegExp|Record.<string, any>)> rules)

基础库 2.24.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/CacheManager.addRules.html

---

### CacheManager.clearCaches()

基础库 2.24.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/CacheManager.clearCaches.html

---

### CacheManager.clearRules()

基础库 2.24.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/CacheManager.clearRules.html

---

### CacheManager.deleteCache(string id)

基础库 2.24.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/CacheManager.deleteCache.html

---

### CacheManager.deleteCaches(Array.<string> ids)

基础库 2.24.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/CacheManager.deleteCaches.html

---

### CacheManager.deleteRule(string id)

基础库 2.24.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/CacheManager.deleteRule.html

---

### CacheManager.deleteRules(Array.<string> ids)

基础库 2.24.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/CacheManager.deleteRules.html

---

### Object CacheManager.match(Object evt)

基础库 2.24.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/CacheManager.match.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| ruleId | string | 命中的规则 id |
| cacheId | string | 缓存 id |
| data | any | 缓存内容，会带有 fromCache 标记，方便开发者区分内容是否来自缓存 |
| createTime | number | 缓存创建时间 |
| maxAge | number | 缓存有效时间 |

---

### CacheManager.off(string eventName, function handler)

基础库 2.24.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/CacheManager.off.html

---

### CacheManager.on(string eventName, function handler)

基础库 2.24.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/CacheManager.on.html

**string eventName**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| request | 发生 wx.request 请求，只在缓存管理器开启阶段会触发 |  |
| enterWeakNetwork | 进入弱网/离线状态 |  |
| exitWeakNetwork | 离开弱网/离线状态 |  |

---

### CacheManager.start()

基础库 2.24.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/CacheManager.start.html

---

### CacheManager.stop()

基础库 2.24.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/CacheManager.stop.html

---

<!-- pages: 35 -->
