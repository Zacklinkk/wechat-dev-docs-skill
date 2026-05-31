# 微信小程序 API 结构化参考 — wxml

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### SelectorQuery wx.createSelectorQuery()

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/wx.createSelectorQuery.html

---

### IntersectionObserver wx.createIntersectionObserver(Object component, Object options)

基础库 1.9.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/wx.createIntersectionObserver.html

**Object options**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| thresholds | Array.<number> | [0] | 否 | 一个数值数组，包含所有阈值。 |  |
| initialRatio | number | 0 | 否 | 初始的相交比例，如果调用时检测到的相交比例与这个值不相等且达到阈值，则会触发一次监听器的回调函数。 |  |
| observeAll | boolean | false | 否 | 是否同时观测多个目标节点（而非一个），如果设为 true ，observe 的 targetSelector 将选中多个节点（注意：同时选中过多节点将影响渲染性能） | [2.0.0](../../framework/compatibility.html) |
| nativeMode | boolean | false | 否 | 是否使用原生观察器模式。 | [3.5.7](../../framework/compatibility.html) |

---

### IntersectionObserver

相关文档:获取界面上的节点信息

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/IntersectionObserver.html

---

### IntersectionObserver.disconnect()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/IntersectionObserver.disconnect.html

---

### IntersectionObserver.observe(string targetSelector, function callback)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/IntersectionObserver.observe.html

**function callback**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | id | string | 节点 ID |
|  | dataset | Record.<string, any> | 节点自定义数据属性 |
|  | intersectionRatio | number | 相交比例 |
|  | intersectionRect | Object | 相交区域的边界 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | left | number | 左边界 | |  | right | number | 右边界 | |  | top | number | 上边界 | |  | bottom | number | 下边界 | |  | width | number | 宽度 | |  | height | number | 高度 | | | |
|  | boundingClientRect | Object | 目标边界 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | left | number | 左边界 | |  | right | number | 右边界 | |  | top | number | 上边界 | |  | bottom | number | 下边界 | |  | width | number | 宽度 | |  | height | number | 高度 | | | |
|  | relativeRect | Object | 参照区域的边界 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | left | number | 左边界 | |  | right | number | 右边界 | |  | top | number | 上边界 | |  | bottom | number | 下边界 | | | |
|  | time | number | 相交检测时的时间戳 |

**function callback**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | left | number | 左边界 |
|  | right | number | 右边界 |
|  | top | number | 上边界 |
|  | bottom | number | 下边界 |
|  | width | number | 宽度 |
|  | height | number | 高度 |

**function callback**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | left | number | 左边界 |
|  | right | number | 右边界 |
|  | top | number | 上边界 |
|  | bottom | number | 下边界 |
|  | width | number | 宽度 |
|  | height | number | 高度 |

**function callback**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | left | number | 左边界 |
|  | right | number | 右边界 |
|  | top | number | 上边界 |
|  | bottom | number | 下边界 |

---

### IntersectionObserver IntersectionObserver.relativeTo(string selector, Object margins)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/IntersectionObserver.relativeTo.html

**Object margins**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| left | number |  | 否 | 节点布局区域的左边界 |
| right | number |  | 否 | 节点布局区域的右边界 |
| top | number |  | 否 | 节点布局区域的上边界 |
| bottom | number |  | 否 | 节点布局区域的下边界 |

---

### IntersectionObserver IntersectionObserver.relativeToViewport(Object margins)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/IntersectionObserver.relativeToViewport.html

**Object margins**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| left | number |  | 否 | 节点布局区域的左边界 |
| right | number |  | 否 | 节点布局区域的右边界 |
| top | number |  | 否 | 节点布局区域的上边界 |
| bottom | number |  | 否 | 节点布局区域的下边界 |

---

### MediaQueryObserver

MediaQueryObserver 对象，用于监听页面 media query 状态的变化，如界面的长宽是不是在某个指定的范围内。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/MediaQueryObserver.html

---

### MediaQueryObserver.disconnect()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/MediaQueryObserver.disconnect.html

---

### MediaQueryObserver.observe(Object descriptor, function callback)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/MediaQueryObserver.observe.html

**Object descriptor**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| minWidth | number |  | 否 | 页面最小宽度（ px 为单位） |
| maxWidth | number |  | 否 | 页面最大宽度（ px 为单位） |
| width | number |  | 否 | 页面宽度（ px 为单位） |
| minHeight | number |  | 否 | 页面最小高度（ px 为单位） |
| maxHeight | number |  | 否 | 页面最大高度（ px 为单位） |
| height | number |  | 否 | 页面高度（ px 为单位） |
| orientation | string |  | 否 | 屏幕方向（ `landscape` 或 `portrait` ） |

**function callback**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| matches | boolean | 页面的当前状态是否满足所指定的 media query |

---

### NodesRef

相关文档:获取界面上的节点信息

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/NodesRef.html

---

### SelectorQuery NodesRef.boundingClientRect(function callback)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/NodesRef.boundingClientRect.html

**function callback**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 节点的 ID |
| dataset | Object | 节点的 dataset |
| left | number | 节点的左边界坐标 |
| right | number | 节点的右边界坐标 |
| top | number | 节点的上边界坐标 |
| bottom | number | 节点的下边界坐标 |
| width | number | 节点的宽度 |
| height | number | 节点的高度 |

---

### SelectorQuery NodesRef.context(function callback)

基础库 2.4.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/NodesRef.context.html

**function callback**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| context | Object | 节点对应的 Context 对象 |

---

### SelectorQuery NodesRef.fields(Object fields, function callback)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/NodesRef.fields.html

**Object fields**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| id | boolean | false | 否 | 是否返回节点 id |  |
| dataset | boolean | false | 否 | 是否返回节点 dataset |  |
| mark | boolean | false | 否 | 是否返回节点 mark |  |
| rect | boolean | false | 否 | 是否返回节点布局位置（`left` `right` `top` `bottom`） |  |
| size | boolean | false | 否 | 是否返回节点尺寸（`width` `height`） |  |
| scrollOffset | boolean | false | 否 | 否 是否返回节点的 `scrollLeft` `scrollTop`，节点必须是 `scroll-view` 或者 `viewport` |  |
| properties | Array.<string> | [] | 否 | 指定属性名列表，返回节点对应属性名的当前属性值（只能获得组件文档中标注的常规属性值，id class style 和事件绑定的属性值不可获取） |  |
| computedStyle | Array.<string> | [] | 否 | 指定样式名列表，返回节点对应样式名的当前值 | [2.1.0](../../framework/compatibility.html) |
| context | boolean | false | 否 | 是否返回节点对应的 Context 对象 | [2.4.2](../../framework/compatibility.html) |
| node | boolean | false | 否 | 是否返回节点对应的 Node 实例 | [2.7.0](../../framework/compatibility.html) |
| ref | boolean | false | 否 | 是否返回节点对应的 Ref 对象，仅 `Skyline` 下支持 | [3.3.0](../../framework/compatibility.html) |

---

### SelectorQuery NodesRef.node(function callback)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/NodesRef.node.html

**function callback**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| node | Object | 节点对应的 Node 实例 |

---

### SelectorQuery NodesRef.ref(function callback)

基础库 3.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/NodesRef.ref.html

**function callback**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| ref | Object | 节点对应的 Ref 对象 |

---

### SelectorQuery NodesRef.scrollOffset(function callback)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/NodesRef.scrollOffset.html

**function callback**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 节点的 ID |
| dataset | Object | 节点的 dataset |
| scrollLeft | number | 节点的水平滚动位置 |
| scrollTop | number | 节点的竖直滚动位置 |
| scrollWidth | number | 节点的滚动宽度 |
| scrollHeight | number | 节点的滚动高度 |

---

### SelectionContext

基础库 3.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectionContext.html

---

### SelectionContext.removeSelection()

基础库 3.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectionContext.removeSelection.html

---

### SelectionContext.selectRange(number start, number end)

基础库 3.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectionContext.selectRange.html

---

### SelectorQuery

相关文档:获取界面上的节点信息

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.html

---

### NodesRef SelectorQuery.exec(function callback)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.exec.html

---

### SelectorQuery SelectorQuery.in(Component component)

基础库 1.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.in.html

---

### NodesRef SelectorQuery.select(string selector)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.select.html

---

### NodesRef SelectorQuery.selectAll(string selector)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.selectAll.html

---

### NodesRef SelectorQuery.selectViewport()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.selectViewport.html

---

<!-- pages: 26 -->
