# 微信小游戏 API 结构化参考 — data-analysis

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.reportUserBehaviorBranchAnalytics(Object object)

基础库 2.12.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/data-analysis/wx.reportUserBehaviorBranchAnalytics.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| branchId | string |  | 是 | 分支ID，在「小程序管理后台」获取 |
| branchDim | string |  | 否 | 自定义维度，基础库 v2.14.0 开始支持可选 |
| eventType | number |  | 是 | 事件类型，1：曝光； 2：点击 |

---

### wx.reportScene(Object object)

基础库 2.26.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/data-analysis/wx.reportScene.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sceneId | Number |  | 是 | 场景ID，在「小程序管理后台」获取 |
| costTime | Number | 0 | 否 | 此场景的耗时，单位 ms |
| dimension | Object |  | 否 | 自定义维度数据，key在「小程序管理后台」获取。只支持能够通过JSON.stringify序列化的对象，且序列化后长度不超过1024个字符 |
| metric | Object |  | 否 | 自定义指标数据，key在「小程序管理后台」获取。只支持能够通过JSON.stringify序列化的对象，且序列化后长度不超过1024个字符 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| data | Object | 开发者上报的原始数据 | [2.28.1](../../guide/runtime/client-lib/compatibility.html) |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| data | Object | 开发者上报的原始数据 | [2.28.1](../../guide/runtime/client-lib/compatibility.html) |
| errMsg | String | 错误信息 | [2.28.1](../../guide/runtime/client-lib/compatibility.html) |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
|  | ${paramName} should be ${expectType} instead of ${paramType} | 参数的类型需为指定的数据类型 |
|  | parameter.${paramName} should greater than or equal to zero | 参数的值需要大于等于0 |
|  | parameter.${paramName}.${key} needs to be a string type and a non-empty string | value仅支持传入非空字符串 |
|  | parameter.${paramName}.${key} needs to be a numeric value of type string | value仅支持传入纯数值组成的字符串（如：'25'） |
|  | failed to serialize parameter.${paramName} by JSON.stringify | 参数对象序列化失败 |
|  | parameter.${paramName} cannot exceed 1024 characters | 参数序列化后，字符串长度不可超过1024个字符 |
|  | report sceneId:${sceneId} repeatedly | 单次启动流程里，场景ID不可重复上报 |

---

### wx.reportMonitor(string name, number value)

从基础库2.31.1开始，本接口停止维护，请使用wx.reportEvent代替

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/data-analysis/wx.reportMonitor.html

---

### wx.reportEvent(string eventId, object data)

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/data-analysis/wx.reportEvent.html

---

### MiniReportManager wx.getMiniReportManager(Object param)

基础库 3.8.12 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/data-analysis/wx.getMiniReportManager.html

**Object param**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| eventList | Array.<string> | [] | 否 | 需要上报的事件ID列表 |
| debug | boolean | false | 否 | 是否开启调试模式，调试模式下每次上报成功都会在控制台输出上报内容。调试模式仅在开发版和体验版小游戏中生效。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### GameLogManager wx.getGameLogManager(Object param)

基础库 3.7.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/data-analysis/wx.getGameLogManager.html

**Object param**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| commonInfo | Object |  | 否 | 自定义全局日志信息。该信息会包含在每条日志的基础信息中。数据类型为 object，且能够通过 JSON.stringify 序列化。 |
| debug | boolean | false | 否 | 是否开启调试模式，调试模式下每次上报成功都会在控制台输出上报内容。调试模式仅在开发版和体验版小游戏中生效。 |
| success | function |  | 否 | 初始化成功后的回调。 |
| fail | function |  | 否 | 初始化失败后的回调。 |
| complete | function |  | 否 | 初始化完成后的回调（成功、失败都会执行）。 |

---

### wx.getGameExptInfo(Object options)

基础库 3.8.8 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/data-analysis/wx.getGameExptInfo.html

**Object options**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyList | Array.<string> |  | 是 | 实验参数数组，不填则获取所有实验参数 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object options**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | list | Array.<Object> | 结果对象，各项为实验的相关信息 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | expt\_id | number | 实验ID，标识实验 | |  | param\_name | string | 参数名称 | |  | param\_value | string | 参数值 | | | |

**Object options**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | expt\_id | number | 实验ID，标识实验 |
|  | param\_name | string | 参数名称 |
|  | param\_value | string | 参数值 |

---

### Object wx.getExptInfoSync(Array.<string> keys)

基础库 2.17.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/data-analysis/wx.getExptInfoSync.html

---

### GameLogManager

GameLogManager 类用于管理小游戏日志。可以通过wx.getGameLogManager获取。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/data-analysis/GameLogManager.html

---

### Object GameLogManager.getCommonInfo()

基础库 3.7.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/data-analysis/GameLogManager.getCommonInfo.html

---

### GameLogManager.log(Object param)

基础库 3.7.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/data-analysis/GameLogManager.log.html

**Object param**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| level | string |  | 是 | 日志等级，用于标识日志的级别和重要性。只能是'info'、'warn'、'error'、'debug'中的一种。 |
| key | string | 'default' | 是 | 日志标签，用于日志分类（如 登录、战斗……）。key 只能是 string 类型，且能够通过 JSON.stringify 序列化。若不传入 key 参数，上报使用默认 key 'default'。 |
| value | Object/Array.<any>/number/string/boolean |  | 是 | 日志内容。value 可以是 string/number/boolean/array/object 类型，且能够通过 JSON.stringify 序列化。 |
| success | function |  | 否 | 上报成功后的回调。 |
| fail | function |  | 否 | 上报失败后的回调。 |
| complete | function |  | 否 | 上报完成后的回调，成功、失败都会执行。 |

---

### Object GameLogManager.tag(string key)

基础库 3.7.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/data-analysis/GameLogManager.tag.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| info | function | 上报 info 级别的日志，仅支持传入日志内容。key 固定为 tag 传入的参数。 |
| warn | function | 上报 warn 级别的日志，仅支持传入日志内容。key 固定为 tag 传入的参数。 |
| error | function | 上报 error 级别的日志，仅支持传入日志内容。key 固定为 tag 传入的参数。 |
| debug | function | 上报 debug 级别的日志，仅支持传入日志内容。key 固定为 tag 传入的参数。 |

---

### GameLogManager.updateCommonInfo(Object newCommonInfo)

基础库 3.7.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/data-analysis/GameLogManager.updateCommonInfo.html

---

### MiniReportManager

MiniReportManager 类用于管理小游戏日志。可以通过wx.getMiniReportManager获取。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/data-analysis/MiniReportManager.html

---

### MiniReportManager.report(Object param)

基础库 3.8.12 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/data-analysis/MiniReportManager.report.html

**Object param**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| eventID | string |  | 是 | 关卡事件 ID，在 [小游戏管理后台](https://mp.weixin.qq.com/)->统计-> 收入诊断调优->分析调优->事件上报中配置 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

<!-- pages: 15 -->
