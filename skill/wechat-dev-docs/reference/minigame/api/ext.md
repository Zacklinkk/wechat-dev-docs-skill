# 微信小游戏 API 结构化参考 — ext

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### Object wx.getExtConfigSync()

基础库 2.8.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ext/wx.getExtConfigSync.html

---

### wx.getExtConfig(Object object)

基础库 2.8.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ext/wx.getExtConfig.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| extConfig | Object | 第三方平台自定义的数据 |

---

<!-- pages: 2 -->
