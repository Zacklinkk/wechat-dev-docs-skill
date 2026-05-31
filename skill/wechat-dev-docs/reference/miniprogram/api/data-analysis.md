# 微信小程序 API 结构化参考 — data-analysis

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.reportMonitor(string name, number value)

从基础库2.31.1开始，本接口停止维护，请使用wx.reportEvent代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/data-analysis/wx.reportMonitor.html

---

### wx.reportEvent(string eventId, object data)

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/data-analysis/wx.reportEvent.html

---

### wx.reportAnalytics(string eventName, Object data)

从基础库2.31.1开始，本接口停止维护，请使用wx.reportEvent代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/data-analysis/wx.reportAnalytics.html

---

### Object wx.getExptInfoSync(Array.<string> keys)

基础库 2.17.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/data-analysis/wx.getExptInfoSync.html

---

### wx.getCommonConfig(Object object)

基础库 2.33.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/data-analysis/wx.getCommonConfig.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keys | Array.<string> |  | 否 | 需要获取的数据指标的对象数组，每个string的格式约定：配置类型\_分表key |
| mode | number |  | 是 | 0：通用配置模式 1：实验模式, 参数与返回结果的使用等效于接口[wx.getExptInfoSync](https://developers.weixin.qq.com/miniprogram/dev/api/data-analysis/wx.getExptInfoSync.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | 错误码 |
| errmsg | string | 错误信息 |
| conf\_type | number | 配置类型, 1-表类型 2-kv类型 |
| conf | string | 根据conf\_type来确定conf内容,conf\_type为1时conf是一个json数组, 类似"[{xxx},{xxx}]", 每一项对应表类型每一行配置内容, 其中conf\_type为2时conf是一个json对象，类似"{xxxx}" |
| expire\_sec | number | 过期时间,单位秒. 0表示当次有效 |

---

<!-- pages: 5 -->
