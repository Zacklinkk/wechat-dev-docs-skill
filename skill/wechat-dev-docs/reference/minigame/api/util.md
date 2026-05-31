# 微信小游戏 API 结构化参考 — util

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### ArrayBuffer wx.encode(Object object)

将字符串按照指定的编码格式编码成 ArrayBuffer

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/util/wx.encode.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | data | string |  | 是 | 要编码的字符串 |
|  | format | string | utf8 | 否 | 编码的格式。注意：iOS高性能模式和iOS高性能+模式下，仅支持utf-8格式 |
|  | | 合法值 | 说明 | | --- | --- | | utf8 |  | | utf-8 |  | | ucs2 | 以小端序读取 | | ucs-2 | 以小端序读取 | | utf16le | 以小端序读取 | | utf-16le | 以小端序读取 | | latin1 |  | | gbk |  | | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| utf8 |  |
| utf-8 |  |
| ucs2 | 以小端序读取 |
| ucs-2 | 以小端序读取 |
| utf16le | 以小端序读取 |
| utf-16le | 以小端序读取 |
| latin1 |  |
| gbk |  |

---

### string wx.decode(Object object)

将 ArrayBuffer 按照指定的编码格式解码成字符串

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/util/wx.decode.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | data | ArrayBuffer |  | 是 | 要解码的 ArrayBuffer |
|  | format | string | utf8 | 否 | 编码的格式 |
|  | | 合法值 | 说明 | | --- | --- | | utf8 |  | | utf-8 |  | | ucs2 | 以小端序读取 | | ucs-2 | 以小端序读取 | | utf16le | 以小端序读取 | | utf-16le | 以小端序读取 | | latin1 |  | | gbk |  | | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| utf8 |  |
| utf-8 |  |
| ucs2 | 以小端序读取 |
| ucs-2 | 以小端序读取 |
| utf16le | 以小端序读取 |
| utf-16le | 以小端序读取 |
| latin1 |  |
| gbk |  |

---

<!-- pages: 2 -->
