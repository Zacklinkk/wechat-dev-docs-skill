# 微信小程序组件结构化参考 (components)

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### cover-image

目前原生组件均已支持同层渲染，建议使用image替代

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/cover-image.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | src | string |  | 否 | 图标路径，支持临时路径、网络地址（1.6.0起支持）、云文件ID（2.2.3起支持）。 | [1.4.0](../framework/compatibility.html) |
|  | referrer-policy | string | no-referrer | 否 | 格式固定为 `https://servicewechat.com/{appid}/{version}/page-frame.html`，其中 {appid} 为小程序的 appid，{version} 为小程序的版本号，版本号为 0 表示为开发版、体验版以及审核版本，版本号为 devtools 表示为开发者工具，其余为正式版本； | [2.13.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | origin | 发送完整的referrer | | no-referrer | 不发送 | | | | | | |
|  | bindload | eventhandle |  | 否 | 图片加载成功时触发 | [2.1.0](../framework/compatibility.html) |
|  | binderror | eventhandle |  | 否 | 图片加载失败时触发 | [2.1.0](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| origin | 发送完整的referrer |
| no-referrer | 不发送 |

**通用属性**

| 格式 | iOS | Android |
| --- | --- | --- |
| JPG | √ | √ |
| PNG | √ | √ |
| SVG | x | x |
| WEBP | √ | √ |
| GIF | √ | √ |
| BASE64 | x | x |

---

### cover-view

目前原生组件均已支持同层渲染，建议使用view替代

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/cover-view.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| scroll-top | number/string |  | 否 | 设置顶部滚动偏移量，仅在设置了 overflow-y: scroll 成为滚动元素后生效 | [2.1.0](../framework/compatibility.html) |

---

### match-media

基础库 2.11.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/match-media.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| min-width | number |  | 否 | 页面最小宽度（ px 为单位） | [2.11.1](../framework/compatibility.html) |
| max-width | number |  | 否 | 页面最大宽度（ px 为单位） | [2.11.1](../framework/compatibility.html) |
| width | number |  | 否 | 页面宽度（ px 为单位） | [2.11.1](../framework/compatibility.html) |
| min-height | number |  | 否 | 页面最小高度（ px 为单位） | [2.11.1](../framework/compatibility.html) |
| max-height | number |  | 否 | 页面最大高度（ px 为单位） | [2.11.1](../framework/compatibility.html) |
| height | number |  | 否 | 页面高度（ px 为单位） | [2.11.1](../framework/compatibility.html) |
| orientation | string |  | 否 | 屏幕方向（ `landscape` 或 `portrait` ） | [2.11.1](../framework/compatibility.html) |

---

### movable-area

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/movable-area.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| scale-area | Boolean | false | 否 | 当里面的movable-view设置为支持双指缩放时，设置此值可将缩放手势生效区域修改为整个movable-area | [1.9.90](../framework/compatibility.html) |

---

### movable-view

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/movable-view.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| direction | string | none | 否 | movable-view的移动方向，属性值有all、vertical、horizontal、none | [1.2.0](../framework/compatibility.html) |
| inertia | boolean | false | 否 | movable-view是否带有惯性 | [1.2.0](../framework/compatibility.html) |
| out-of-bounds | boolean | false | 否 | 超过可移动区域后，movable-view是否还可以移动 | [1.2.0](../framework/compatibility.html) |
| x | number/string |  | 否 | 定义x轴方向的偏移，如果x的值不在可移动范围内，会自动移动到可移动范围；改变x的值会触发动画；单位支持px（默认）、rpx； | [1.2.0](../framework/compatibility.html) |
| y | number/string |  | 否 | 定义y轴方向的偏移，如果y的值不在可移动范围内，会自动移动到可移动范围；改变y的值会触发动画；单位支持px（默认）、rpx； | [1.2.0](../framework/compatibility.html) |
| damping | number | 20 | 否 | 阻尼系数，用于控制x或y改变时的动画和过界回弹的动画，值越大移动越快 | [1.2.0](../framework/compatibility.html) |
| friction | number | 2 | 否 | 摩擦系数，用于控制惯性滑动的动画，值越大摩擦力越大，滑动越快停止；必须大于0，否则会被设置成默认值 | [1.2.0](../framework/compatibility.html) |
| disabled | boolean | false | 否 | 是否禁用 | [1.9.90](../framework/compatibility.html) |
| scale | boolean | false | 否 | 是否支持双指缩放，默认缩放手势生效区域是在movable-view内 | [1.9.90](../framework/compatibility.html) |
| scale-min | number | 0.1 | 否 | 定义缩放倍数最小值 | [1.9.90](../framework/compatibility.html) |
| scale-max | number | 10 | 否 | 定义缩放倍数最大值 | [1.9.90](../framework/compatibility.html) |
| scale-value | number | 1 | 否 | 定义缩放倍数，取值范围为 0.1 - 10 | [1.9.90](../framework/compatibility.html) |
| animation | boolean | true | 否 | 是否使用动画 | [2.1.0](../framework/compatibility.html) |
| bindchange | eventhandle |  | 否 | 拖动过程中触发的事件，event.detail = {x, y, source} | [1.9.90](../framework/compatibility.html) |
| bindscale | eventhandle |  | 否 | 缩放过程中触发的事件，event.detail = {x, y, scale}，x和y字段在[2.1.0](../framework/compatibility.html)之后支持 | [1.9.90](../framework/compatibility.html) |
| htouchmove | eventhandle |  | 否 | 初次手指触摸后移动为横向的移动时触发，如果catch此事件，则意味着touchmove事件也被catch | [1.9.90](../framework/compatibility.html) |
| vtouchmove | eventhandle |  | 否 | 初次手指触摸后移动为纵向的移动时触发，如果catch此事件，则意味着touchmove事件也被catch | [1.9.90](../framework/compatibility.html) |

**bindchange 返回的 source 表示产生移动的原因**

| 值 | 说明 |
| --- | --- |
| touch | 拖动 |
| touch-out-of-bounds | 超出移动范围 |
| out-of-bounds | 超出移动范围后的回弹 |
| friction | 惯性 |
| 空字符串 | setData |

---

### page-container

基础库 2.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/page-container.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| show | boolean | false | 否 | 是否显示容器组件 | [2.16.0](../framework/compatibility.html) |
| duration | number | 300 | 否 | 动画时长，单位毫秒 | [2.16.0](../framework/compatibility.html) |
| z-index | number | 100 | 否 | z-index 层级 | [2.16.0](../framework/compatibility.html) |
| overlay | boolean | true | 否 | 是否显示遮罩层 | [2.16.0](../framework/compatibility.html) |
| position | string | bottom | 否 | 弹出位置，可选值为 `top` `bottom` `right` `center` | [2.16.0](../framework/compatibility.html) |
| round | boolean | false | 否 | 是否显示圆角 | [2.16.0](../framework/compatibility.html) |
| close-on-slide-down | boolean | false | 否 | 是否在下滑一段距离后关闭 | [2.16.0](../framework/compatibility.html) |
| overlay-style | string |  | 否 | 自定义遮罩层样式 | [2.16.0](../framework/compatibility.html) |
| custom-style | string |  | 否 | 自定义弹出层样式 | [2.16.0](../framework/compatibility.html) |
| bind:beforeenter | eventhandle |  | 否 | 进入前触发 | [2.16.0](../framework/compatibility.html) |
| bind:enter | eventhandle |  | 否 | 进入中触发 | [2.16.0](../framework/compatibility.html) |
| bind:afterenter | eventhandle |  | 否 | 进入后触发 | [2.16.0](../framework/compatibility.html) |
| bind:beforeleave | eventhandle |  | 否 | 离开前触发 | [2.16.0](../framework/compatibility.html) |
| bind:leave | eventhandle |  | 否 | 离开中触发 | [2.16.0](../framework/compatibility.html) |
| bind:afterleave | eventhandle |  | 否 | 离开后触发 | [2.16.0](../framework/compatibility.html) |
| bind:clickoverlay | eventhandle |  | 否 | 点击遮罩层时触发 | [2.16.0](../framework/compatibility.html) |

---

### root-portal

基础库 2.25.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/root-portal.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| enable | boolean | true | 否 | 是否从页面中脱离出来 | [2.26.1](../framework/compatibility.html) |
| externalClass | string |  | 否 | 外部样式类 | [3.9.2](../framework/compatibility.html) |

---

### scroll-view

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/scroll-view.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | scroll-x | boolean | false | 否 | 允许横向滚动 | [1.0.0](../framework/compatibility.html) |
|  | scroll-y | boolean | false | 否 | 允许纵向滚动 | [1.0.0](../framework/compatibility.html) |
|  | upper-threshold | number/string | 50 | 否 | 距顶部/左边多远时，触发 scrolltoupper 事件 | [1.0.0](../framework/compatibility.html) |
|  | lower-threshold | number/string | 50 | 否 | 距底部/右边多远时，触发 scrolltolower 事件 | [1.0.0](../framework/compatibility.html) |
|  | scroll-top | number/string |  | 否 | 设置竖向滚动条位置 | [1.0.0](../framework/compatibility.html) |
|  | scroll-left | number/string |  | 否 | 设置横向滚动条位置 | [1.0.0](../framework/compatibility.html) |
|  | scroll-into-view | string |  | 否 | 值应为某子元素id（id不能以数字开头）。设置哪个方向可滚动，则在哪个方向滚动到该元素 | [1.0.0](../framework/compatibility.html) |
|  | scroll-into-view-offset | number | 0 | 否 | 跳转到 scroll-into-view 目标节点时的额外偏移。skyline 自 3.1.0 版本开始支持，webview 自 3.6.0 版本开始支持。 | [3.1.0](../framework/compatibility.html) |
|  | scroll-with-animation | boolean | false | 否 | 在设置滚动条位置时使用动画过渡 | [1.0.0](../framework/compatibility.html) |
|  | enable-back-to-top | boolean | false | 否 | iOS点击顶部状态栏、安卓双击标题栏时，滚动条返回顶部，只支持竖向。自 2.27.3 版本开始，若非显式设置为 false，则在显示尺寸大于屏幕 90% 时自动开启。鸿蒙 OS 暂不支持 | [1.0.0](../framework/compatibility.html) |
|  | enable-passive | boolean | false | 否 | 开启 passive 特性，能优化一定的滚动性能 | [2.25.3](../framework/compatibility.html) |
|  | refresher-enabled | boolean | false | 否 | 开启自定义下拉刷新 | [2.10.1](../framework/compatibility.html) |
|  | refresher-threshold | number | 45 | 否 | 设置自定义下拉刷新阈值 | [2.10.1](../framework/compatibility.html) |
|  | refresher-default-style | string | "black" | 否 | 设置自定义下拉刷新默认样式，支持设置 `black | white | none`， none 表示不使用默认样式 | [2.10.1](../framework/compatibility.html) |
|  | refresher-background | string |  | 否 | 设置自定义下拉刷新区域背景颜色，默认为透明 | [2.10.1](../framework/compatibility.html) |
|  | refresher-triggered | boolean | false | 否 | 设置当前下拉刷新状态，true 表示下拉刷新已经被触发，false 表示下拉刷新未被触发 | [2.10.1](../framework/compatibility.html) |
|  | bounces | boolean | true | 否 | iOS 下 scroll-view 边界弹性控制 (同时开启 enhanced 属性后生效) | [2.12.0](../framework/compatibility.html) |
|  | show-scrollbar | boolean | true | 否 | 滚动条显隐控制，仅对垂直滚动条有效 (同时开启 enhanced 属性后生效) | [2.12.0](../framework/compatibility.html) |
|  | fast-deceleration | boolean | false | 否 | 滑动减速速率控制, 仅在 iOS 下生效 (同时开启 enhanced 属性后生效) | [2.12.0](../framework/compatibility.html) |
|  | binddragstart | eventhandle |  | 否 | 滑动开始事件 (同时开启 enhanced 属性后生效) detail { scrollTop, scrollLeft } | [2.12.0](../framework/compatibility.html) |
|  | binddragging | eventhandle |  | 否 | 滑动事件 (同时开启 enhanced 属性后生效) detail { scrollTop, scrollLeft } | [2.12.0](../framework/compatibility.html) |
|  | binddragend | eventhandle |  | 否 | 滑动结束事件 (同时开启 enhanced 属性后生效) detail { scrollTop, scrollLeft, velocity } | [2.12.0](../framework/compatibility.html) |
|  | bindscrolltoupper | eventhandle |  | 否 | 滚动到顶部/左边时触发 | [1.0.0](../framework/compatibility.html) |
|  | bindscrolltolower | eventhandle |  | 否 | 滚动到底部/右边时触发 | [1.0.0](../framework/compatibility.html) |
|  | bindscroll | eventhandle |  | 否 | 滚动时触发，event.detail = { scrollLeft, scrollTop, scrollHeight, scrollWidth, deltaX, deltaY }。skyline 从 3.6.6开始，额外具有 boundaryVelocity 字段：如果该次滚动会触碰到边界，从该次滚动触发起到下一个滚动事件发生或者当次滚动事件结束为止 boundaryVelocity 将被置为触碰边界时的速度，否则置为 NAN。 | [1.0.0](../framework/compatibility.html) |
|  | bindrefresherpulling | eventhandle |  | 否 | 自定义下拉刷新控件被下拉 | [2.10.1](../framework/compatibility.html) |
|  | bindrefresherrefresh | eventhandle |  | 否 | 自定义下拉刷新被触发 | [2.10.1](../framework/compatibility.html) |
|  | bindrefresherrestore | eventhandle |  | 否 | 自定义下拉刷新被复位 | [2.10.1](../framework/compatibility.html) |
|  | bindrefresherabort | eventhandle |  | 否 | 自定义下拉刷新被中止 | [2.10.1](../framework/compatibility.html) |
|  | scroll-anchoring | boolean | false | 否 | 开启 scroll anchoring 特性，即控制滚动位置不随内容变化而抖动，可参考 CSS `overflow-anchor` 属性。webview 仅在 iOS 下生效。skyline 自 3.6.2 版本开始支持，默认为 true 。 | [2.8.2](../framework/compatibility.html) |

**Skyline 特有属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | type | string |  | 否 | 渲染模式 |  |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | list | 列表模式。只会渲染在屏节点，会根据直接子节点是否在屏来按需渲染，若只有一个直接子节点则性能会退化 | [2.25.2](../framework/compatibility.html) | | custom | 自定义模式。只会渲染在屏节点，子节点可以是 [sticky-section](sticky-section.html) [list-view](list-view.html) [grid-view](grid-view.html) 等组件 | [2.29.0](../framework/compatibility.html) | | nested | 嵌套模式。用于处理父子 scroll-view 间的嵌套滚动，子节点可以是 [nested-scroll-header](nested-scroll-header.html) [nested-scroll-body](nested-scroll-body.html) 组件或自定义 refresher | [3.2.0](../framework/compatibility.html) | | | | | | |
|  | associative-container | string |  | 否 | 关联的滚动容器 | [3.2.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | draggable-sheet | 关联 [draggable-sheet](draggable-sheet.html) 组件 | [3.2.0](../framework/compatibility.html) | | nested-scroll-view | 关联 `type=nested` 嵌套模式 | [3.2.0](../framework/compatibility.html) | | pop-gesture | 关联 [页面手势返回](../framework/runtime/skyline/pop-gesture.html) | [3.4.0](../framework/compatibility.html) | | | | | | |
|  | reverse | boolean | false | 否 | 是否反向滚动。一般初始滚动位置是在顶部，反向滚动则是在底部。 | [2.27.2](../framework/compatibility.html) |
|  | clip | boolean | true | 否 | 是否对溢出进行裁剪，默认开启 | [2.32.1](../framework/compatibility.html) |
|  | enable-back-to-top | boolean | false | 否 | 仅 iOS 支持，其余同 WebView 同名组件 | [2.32.1](../framework/compatibility.html) |
|  | cache-extent | number |  | 否 | 指定视口外渲染区域的距离，默认情况下视口外节点不渲染。指定 cache-extent 可优化滚动体验和加载速度，但会提高内存占用且影响首屏速度，可按需启用。 | [2.29.0](../framework/compatibility.html) |
|  | min-drag-distance | number | 18 | 否 | 指定 scroll-view 触发滚动的最小拖动距离。仅在 scroll-view 和其他组件存在手势冲突时使用，可通过调整该属性使得滚动更加灵敏。 | [2.33.0](../framework/compatibility.html) |
|  | scroll-into-view-within-extent | boolean | false | 否 | 只 scroll-into-view 到 cacheExtent 以内的目标节点，性能更佳 | [2.29.0](../framework/compatibility.html) |
|  | scroll-into-view-alignment | string | start | 否 | 指定 scroll-into-view 目标节点在视口内的位置 | [2.29.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | start | 目标节点显示在视口开始处 | | center | 目标节点显示在视口中间 | | end | 目标节点显示在视口结束处 | | nearest | 目标节点在就近的视口边缘显示，若节点已在视口内则不触发滚动 | | | | | | |
|  | bind:scrollstart | eventhandle |  | 否 | 滚动开始事件，仅支持非 worklet 的组件方法作为回调。event.detail = { isDrag } | [2.29.0](../framework/compatibility.html) |
|  | bind:scroll | eventhandle |  | 否 | 滚动事件，多返回 isDrag 字段，仅支持非 worklet 的组件方法作为回调。event.detail = { isDrag } |  |
|  | bind:scrollend | eventhandle |  | 否 | 滚动结束事件，仅支持非 worklet 的组件方法作为回调。event.detail = { isDrag } | [2.29.0](../framework/compatibility.html) |
|  | worklet:onscrollstart | worklet |  | 否 | 同 `bindscrollstart`，但仅支持 worklet 作为回调 | [2.29.2](../framework/compatibility.html) |
|  | worklet:onscrollupdate | worklet |  | 否 | `bindscroll` ，但仅支持 worklet 作为回调 | [2.29.2](../framework/compatibility.html) |
|  | worklet:onscrollend | worklet |  | 否 | 同 `bindscrollend`，但仅支持 worklet 作为回调 | [2.29.2](../framework/compatibility.html) |
|  | bind:refresherwillrefresh | eventhandle |  | 否 | 自定义下拉刷新即将触发刷新（拖动超过 refresher-threshold 时）的事件 | [2.29.0](../framework/compatibility.html) |
|  | worklet:adjust-deceleration-velocity | callback |  | 否 | 指定手指抬起时做惯性滚动的初速度。(velocity: number) => number | [2.29.2](../framework/compatibility.html) |
|  | padding | Array | [0, 0, 0, 0] | 否 | 长度为 4 的数组，按 top、right、bottom、left 顺序指定内边距 | [3.0.0](../framework/compatibility.html) |
|  | refresher-two-level-enabled | boolean | false | 否 | 开启下拉二级能力 | [3.0.0](../framework/compatibility.html) |
|  | refresher-two-level-triggered | boolean | false | 否 | 设置打开/关闭二级 | [3.0.0](../framework/compatibility.html) |
|  | refresher-two-level-threshold | number | 150 | 否 | 下拉二级阈值 | [3.0.0](../framework/compatibility.html) |
|  | refresher-two-level-close-threshold | number | 80 | 否 | 滑动返回时关闭二级的阈值 | [3.0.0](../framework/compatibility.html) |
|  | refresher-two-level-scroll-enabled | boolean | false | 否 | 处于二级状态时是否可滑动 | [3.0.0](../framework/compatibility.html) |
|  | refresher-ballistic-refresh-enabled | boolean | false | 否 | 惯性滚动是否触发下拉刷新 | [3.0.0](../framework/compatibility.html) |
|  | refresher-two-level-pinned | boolean | false | 否 | 即将打开二级时否定住 | [3.0.0](../framework/compatibility.html) |
|  | bind:refresherstatuschange | eventhandle |  | 否 | 下拉刷新状态回调 | [3.0.0](../framework/compatibility.html) |

**Skyline 特有属性**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| list | 列表模式。只会渲染在屏节点，会根据直接子节点是否在屏来按需渲染，若只有一个直接子节点则性能会退化 | [2.25.2](../framework/compatibility.html) |
| custom | 自定义模式。只会渲染在屏节点，子节点可以是 [sticky-section](sticky-section.html) [list-view](list-view.html) [grid-view](grid-view.html) 等组件 | [2.29.0](../framework/compatibility.html) |
| nested | 嵌套模式。用于处理父子 scroll-view 间的嵌套滚动，子节点可以是 [nested-scroll-header](nested-scroll-header.html) [nested-scroll-body](nested-scroll-body.html) 组件或自定义 refresher | [3.2.0](../framework/compatibility.html) |

**Skyline 特有属性**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| draggable-sheet | 关联 [draggable-sheet](draggable-sheet.html) 组件 | [3.2.0](../framework/compatibility.html) |
| nested-scroll-view | 关联 `type=nested` 嵌套模式 | [3.2.0](../framework/compatibility.html) |
| pop-gesture | 关联 [页面手势返回](../framework/runtime/skyline/pop-gesture.html) | [3.4.0](../framework/compatibility.html) |

**Skyline 特有属性**

| 合法值 | 说明 |
| --- | --- |
| start | 目标节点显示在视口开始处 |
| center | 目标节点显示在视口中间 |
| end | 目标节点显示在视口结束处 |
| nearest | 目标节点在就近的视口边缘显示，若节点已在视口内则不触发滚动 |

**WebView 特有属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | enable-flex | boolean | false | 否 | 启用 flexbox 布局。开启后，当前节点声明了 `display: flex` 就会成为 flex container，并作用于其孩子节点。 | [2.7.3](../framework/compatibility.html) |
|  | enhanced | boolean | false | 否 | 启用 scroll-view 增强特性，启用后可通过 [ScrollViewContext](../api/ui/scroll/ScrollViewContext.html) 操作 scroll-view。鸿蒙 OS 暂不支持 enhanced 及其相关的属性和方法。 | [2.12.0](../framework/compatibility.html) |
|  | paging-enabled | boolean | false | 否 | 分页滑动效果 (同时开启 enhanced 属性后生效) | [2.12.0](../framework/compatibility.html) |
|  | using-sticky | boolean | false | 否 | 使 scroll-view 下的 position sticky 特性生效，否则滚动一屏后 sticky 元素会被隐藏 | [3.2.1](../framework/compatibility.html) |

---

### swiper

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/swiper.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | indicator-dots | boolean | false | 否 | 是否显示面板指示点 | [1.0.0](../framework/compatibility.html) |
|  | indicator-color | color | rgba(0, 0, 0, .3) | 否 | 指示点颜色 | [1.1.0](../framework/compatibility.html) |
|  | indicator-active-color | color | #000000 | 否 | 当前选中的指示点颜色 | [1.1.0](../framework/compatibility.html) |
|  | autoplay | boolean | false | 否 | 是否自动切换 | [1.0.0](../framework/compatibility.html) |
|  | current | number | 0 | 否 | 当前所在滑块的 index | [1.0.0](../framework/compatibility.html) |
|  | interval | number | 5000 | 否 | 自动切换时间间隔 | [1.0.0](../framework/compatibility.html) |
|  | duration | number | 500 | 否 | 滑动动画时长 | [1.0.0](../framework/compatibility.html) |
|  | circular | boolean | false | 否 | 是否采用衔接滑动 | [1.0.0](../framework/compatibility.html) |
|  | vertical | boolean | false | 否 | 滑动方向是否为纵向 | [1.0.0](../framework/compatibility.html) |
|  | display-multiple-items | number | 1 | 否 | 同时显示的滑块数量 | [1.9.0](../framework/compatibility.html) |
|  | previous-margin | string | "0px" | 否 | 前边距，可用于露出前一项的一小部分，接受 px 和 rpx 值 | [1.9.0](../framework/compatibility.html) |
|  | next-margin | string | "0px" | 否 | 后边距，可用于露出后一项的一小部分，接受 px 和 rpx 值。skyline 于 3.5.1 版本支持 | [1.9.0](../framework/compatibility.html) |
|  | easing-function | string | "default" | 否 | 指定 swiper 切换缓动动画类型 | [2.6.5](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | default | 默认缓动函数 | | linear | 线性动画 | | easeInCubic | 缓入动画 | | easeOutCubic | 缓出动画 | | easeInOutCubic | 缓入缓出动画 | | | | | | |
|  | direction | string | "all" | 否 | 指定 swiper 滑动方向 | [3.8.10](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | all | 默认 | | positive | 如 vertical 为 true 时，允许用户下滑（swiper 内容向上滚动），为 false 时，允许用户右滑（swiper 内容向左滚动） | | negative | 如 vertical 为 true 时，允许用户上滑（swiper 内容向下滚动），为 false 时，允许用户左滑（swiper 内容向右滚动） | | | | | | |
|  | bindchange | eventhandle |  | 否 | current 改变时会触发 change 事件，event.detail = {current, source} | [1.0.0](../framework/compatibility.html) |
|  | bindtransition | eventhandle |  | 否 | swiper-item 的位置发生改变时会触发 transition 事件，event.detail = {dx: dx, dy: dy}。Skyline 仅支持非 worklet 的组件方法作为回调。 | [2.4.3](../framework/compatibility.html) |
|  | bindanimationfinish | eventhandle |  | 否 | 动画结束时会触发 animationfinish 事件，event.detail 同 bindchange。Skyline 仅支持非 worklet 的组件方法作为回调。 | [1.9.0](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| default | 默认缓动函数 |
| linear | 线性动画 |
| easeInCubic | 缓入动画 |
| easeOutCubic | 缓出动画 |
| easeInOutCubic | 缓入缓出动画 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| all | 默认 |
| positive | 如 vertical 为 true 时，允许用户下滑（swiper 内容向上滚动），为 false 时，允许用户右滑（swiper 内容向左滚动） |
| negative | 如 vertical 为 true 时，允许用户上滑（swiper 内容向下滚动），为 false 时，允许用户左滑（swiper 内容向右滚动） |

**Skyline 特有属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | layout-type | string | normal | 否 | 渲染模式 | [3.2.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | normal | 默认方式 | | stackLeft | 左向堆叠 | | stackRight | 右向堆叠 | | tinder | 滑动卡片 | | transformer | 过渡动画 | | | | | | |
|  | transformer-type | string | scaleAndFade | 否 | layout-type 为 transformer 时指定动画类型 | [3.2.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | scaleAndFade |  | | accordion |  | | threeD |  | | zoomIn |  | | zoomOut |  | | deepthPage |  | | | | | | |
|  | indicator-type | string | normal | 否 | 指示点动画类型 | [3.2.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | normal |  | | worm |  | | wormThin |  | | wormUnderground |  | | wormThinUnderground |  | | expand |  | | jump |  | | jumpWithOffset |  | | scroll |  | | scrollFixedCenter |  | | slide |  | | slideUnderground |  | | scale |  | | swap |  | | swapYRotation |  | | color |  | | | | | | |
|  | indicator-margin | number | 10 | 否 | 指示点四周边距 | [3.2.0](../framework/compatibility.html) |
|  | indicator-spacing | number | 4 | 否 | 指示点间距 | [3.2.0](../framework/compatibility.html) |
|  | indicator-radius | number | 4 | 否 | 指示点圆角大小 | [3.2.0](../framework/compatibility.html) |
|  | indicator-width | number | 8 | 否 | 指示点宽度 | [3.2.0](../framework/compatibility.html) |
|  | indicator-height | number | 8 | 否 | 指示点高度 | [3.2.0](../framework/compatibility.html) |
|  | indicator-alignment | Array.<number>/string | auto | 否 | 指示点的相对位置 | [3.2.0](../framework/compatibility.html) |
|  | indicator-offset | Array.<number> | [0, 0] | 否 | 指示点位置的偏移量 | [3.2.0](../framework/compatibility.html) |
|  | scroll-with-animation | boolean | true | 否 | 改变 current 时使用动画过渡 | [2.29.0](../framework/compatibility.html) |
|  | cache-extent | number | 0 | 否 | 缓存区域大小，值为 1 表示提前渲染上下各一屏区域（swiper 容器大小） | [2.29.0](../framework/compatibility.html) |
|  | worklet:onscrollstart | worklet |  | 否 | 滑动开始时触发，仅支持 worklet 作为回调。event.detail = {dx: dx, dy: dy} |  |
|  | worklet:onscrollupdate | worklet |  | 否 | 滑动位置更新时触发，仅支持 worklet 作为回调。event.detail = {dx: dx, dy: dy} |  |
|  | worklet:onscrollend | worklet |  | 否 | 滑动结束时触发，仅支持 worklet 作为回调。event.detail = {dx: dx, dy: dy} |  |

**Skyline 特有属性**

| 合法值 | 说明 |
| --- | --- |
| normal | 默认方式 |
| stackLeft | 左向堆叠 |
| stackRight | 右向堆叠 |
| tinder | 滑动卡片 |
| transformer | 过渡动画 |

**Skyline 特有属性**

| 合法值 | 说明 |
| --- | --- |
| scaleAndFade |  |
| accordion |  |
| threeD |  |
| zoomIn |  |
| zoomOut |  |
| deepthPage |  |

**Skyline 特有属性**

| 合法值 | 说明 |
| --- | --- |
| normal |  |
| worm |  |
| wormThin |  |
| wormUnderground |  |
| wormThinUnderground |  |
| expand |  |
| jump |  |
| jumpWithOffset |  |
| scroll |  |
| scrollFixedCenter |  |
| slide |  |
| slideUnderground |  |
| scale |  |
| swap |  |
| swapYRotation |  |
| color |  |

**WebView 特有属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | snap-to-edge | boolean | false | 否 | 当 swiper-item 的个数大于等于 2，关闭 circular 并且开启 previous-margin 或 next-margin 的时候，可以指定这个边距是否应用到第一个、最后一个元素 | [2.12.1](../framework/compatibility.html) |

---

### swiper-item

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/swiper-item.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| item-id | string |  | 否 | 该 swiper-item 的标识符 | [1.9.0](../framework/compatibility.html) |
| skip-hidden-item-layout | boolean | false | 否 | 是否跳过未显示的滑块布局，设为 true 可优化复杂情况下的滑动性能，但会丢失隐藏状态滑块的布局信息 | [1.9.0](../framework/compatibility.html) |

---

### view

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/view.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| hover-class | string | none | 否 | 指定按下去的样式类。当 `hover-class="none"` 时，没有点击态效果 | [1.0.0](../framework/compatibility.html) |
| hover-stop-propagation | boolean | false | 否 | 指定是否阻止本节点的祖先节点出现点击态 | [1.5.0](../framework/compatibility.html) |
| hover-start-time | number | 50 | 否 | 按住后多久出现点击态，单位毫秒 | [1.0.0](../framework/compatibility.html) |
| hover-stay-time | number | 400 | 否 | 手指松开后点击态保留时间，单位毫秒 | [1.0.0](../framework/compatibility.html) |

---

### icon

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/icon.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| type | string |  | 是 | icon的类型，有效值：success, success\_no\_circle, info, warn, waiting, cancel, download, search, clear | [1.0.0](../framework/compatibility.html) |
| size | number/string | 23 | 否 | icon的大小，单位默认为px，[2.4.0](../framework/compatibility.html)起支持传入单位(rpx/px)，[2.21.3](../framework/compatibility.html)起支持传入其余单位(rem 等)。 | [1.0.0](../framework/compatibility.html) |
| color | string |  | 否 | icon的颜色，同css的color | [1.0.0](../framework/compatibility.html) |

---

### progress

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/progress.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| percent | number |  | 否 | 百分比0~100 | [1.0.0](../framework/compatibility.html) |
| show-info | boolean | false | 否 | 在进度条右侧显示百分比 | [1.0.0](../framework/compatibility.html) |
| border-radius | number/string | 0 | 否 | 圆角大小 | [2.3.1](../framework/compatibility.html) |
| font-size | number/string | 16 | 否 | 右侧百分比字体大小 | [2.3.1](../framework/compatibility.html) |
| stroke-width | number/string | 6 | 否 | 进度条线的宽度 | [1.0.0](../framework/compatibility.html) |
| color | string | #09BB07 | 否 | 进度条颜色（请使用activeColor） | [1.0.0](../framework/compatibility.html) |
| activeColor | string | #09BB07 | 否 | 已选择的进度条的颜色 | [1.0.0](../framework/compatibility.html) |
| backgroundColor | string | #EBEBEB | 否 | 未选择的进度条的颜色 | [1.0.0](../framework/compatibility.html) |
| active | boolean | false | 否 | 进度条从左往右的动画 | [1.0.0](../framework/compatibility.html) |
| active-mode | string | backwards | 否 | backwards: 动画从头播；forwards：动画从上次结束点接着播 | [1.7.0](../framework/compatibility.html) |
| duration | number | 30 | 否 | 进度增加1%所需毫秒数 | [2.8.2](../framework/compatibility.html) |
| bindactiveend | eventhandle |  | 否 | 动画完成事件 | [2.4.1](../framework/compatibility.html) |

---

### rich-text

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/rich-text.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | nodes | array/string | [] | 否 | 节点列表/HTML String | [1.4.0](../framework/compatibility.html) |
|  | space | string |  | 否 | 显示连续空格 | [2.4.1](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | ensp | 中文字符空格一半大小 | | emsp | 中文字符空格大小 | | nbsp | 根据字体设置的空格大小 | | | | | | |
|  | user-select | boolean | false | 否 | 文本是否可选，该属性会使节点显示为 block | [2.24.0](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| ensp | 中文字符空格一半大小 |
| emsp | 中文字符空格大小 |
| nbsp | 根据字体设置的空格大小 |

**Skyline 特有属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | mode | string | default | 否 | 布局兼容模式 |
|  | | 合法值 | 说明 | | --- | --- | | default | 完全遵循 skyline 的默认行为，不对节点树进行任何更改。 | | compat | 尽可能将 tag 映射为 `<view><span></span></view>` 的形式。通常最接近 webview 的表现。 | | aggressive | 所有 tag 均被映射为形如 `<view><span></span></view>` 的形式。 | | inline-block | 实验性的 inline-block 布局策略，但无法实现折行。 | | web | 使用 webview 渲染富文本，基础库 3.6.0 开始支持。 | | web-static | 使用 webview 截图的方式渲染富文本，基础库 3.7.7 开始支持。 | | | | | |

**Skyline 特有属性**

| 合法值 | 说明 |
| --- | --- |
| default | 完全遵循 skyline 的默认行为，不对节点树进行任何更改。 |
| compat | 尽可能将 tag 映射为 `<view><span></span></view>` 的形式。通常最接近 webview 的表现。 |
| aggressive | 所有 tag 均被映射为形如 `<view><span></span></view>` 的形式。 |
| inline-block | 实验性的 inline-block 布局策略，但无法实现折行。 |
| web | 使用 webview 渲染富文本，基础库 3.6.0 开始支持。 |
| web-static | 使用 webview 截图的方式渲染富文本，基础库 3.7.7 开始支持。 |

**元素节点：type = node**

| 属性 | 说明 | 类型 | 必填 | 备注 |
| --- | --- | --- | --- | --- |
| name | 标签名 | string | 是 | 支持部分受信任的 HTML 节点 |
| attrs | 属性 | object | 否 | 支持部分受信任的属性，遵循 Pascal 命名法 |
| children | 子节点列表 | array | 否 | 结构和 nodes 一致 |

**文本节点：type = text**

| 属性 | 说明 | 类型 | 必填 | 备注 |
| --- | --- | --- | --- | --- |
| text | 文本 | string | 是 | 支持entities |

**受信任的HTML节点及属性**

| 节点 | 属性 |
| --- | --- |
| a |  |
| abbr |  |
| address |  |
| article |  |
| aside |  |
| b |  |
| bdi |  |
| bdo | dir |
| big |  |
| blockquote |  |
| br |  |
| caption |  |
| center |  |
| cite |  |
| code |  |
| col | span，width |
| colgroup | span，width |
| dd |  |
| del |  |
| div |  |
| dl |  |
| dt |  |
| em |  |
| fieldset |  |
| font |  |
| footer |  |
| h1 |  |
| h2 |  |
| h3 |  |
| h4 |  |
| h5 |  |
| h6 |  |
| header |  |
| hr |  |
| i |  |
| img | alt，src，height，width |
| ins |  |
| label |  |
| legend |  |
| li |  |
| mark |  |
| nav |  |
| ol | start，type |
| p |  |
| pre |  |
| q |  |
| rt |  |
| ruby |  |
| s |  |
| section |  |
| small |  |
| span |  |
| strong |  |
| sub |  |
| sup |  |
| table | width |
| tbody |  |
| td | colspan，height，rowspan，width |
| tfoot |  |
| th | colspan，height，rowspan，width |
| thead |  |
| tr | colspan，height，rowspan，width |
| tt |  |
| u |  |
| ul |  |

---

### selection

基础库 3.6.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/selection.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| disable-context-menu | boolean | false | 否 | 是否隐藏客户端原生文本选区按钮 | [3.6.4](../framework/compatibility.html) |
| bindselectionchange | eventhandle |  | 否 | 当选区发生变化时触发 selectionchange 事件 event.detail = { isCollapsed, selectedString, firstNodeId, firstOffset, lastNodeId, lastOffset, firstRangeRect } | [3.6.4](../framework/compatibility.html) |

---

### text

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/text.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | selectable | boolean | false | 否 | 文本是否可选 (已废弃) | [1.1.0](../framework/compatibility.html) |
|  | user-select | boolean | false | 否 | 文本是否可选，该属性会使文本节点显示为 inline-block | [2.12.1](../framework/compatibility.html) |

**Skyline 特有属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | overflow | string | visible | 是 | 文本溢出处理 |
|  | | 合法值 | 说明 | | --- | --- | | clip | 修剪文本 | | fade | 淡出 | | ellipsis | 显示省略号 | | visible | 文本不截断 | | | | | |
|  | max-lines | number |  | 是 | 限制文本最大行数 |

**Skyline 特有属性**

| 合法值 | 说明 |
| --- | --- |
| clip | 修剪文本 |
| fade | 淡出 |
| ellipsis | 显示省略号 |
| visible | 文本不截断 |

**WebView 特有属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | space | string |  | 否 | 显示连续空格 | [1.4.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | ensp | 中文字符空格一半大小 | | emsp | 中文字符空格大小 | | nbsp | 根据字体设置的空格大小 | | | | | | |
|  | decode | boolean | false | 否 | 是否解码 | [1.4.0](../framework/compatibility.html) |

**WebView 特有属性**

| 合法值 | 说明 |
| --- | --- |
| ensp | 中文字符空格一半大小 |
| emsp | 中文字符空格大小 |
| nbsp | 根据字体设置的空格大小 |

---

### button

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/button.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | size | string | default | 否 | 按钮的大小 | [1.0.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | default | 默认大小 | | mini | 小尺寸 | | | | | | |
|  | type | string | default | 否 | 按钮的样式类型 | [1.0.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | primary | 绿色 | | default | 白色 | | warn | 红色 | | | | | | |
|  | plain | boolean | false | 否 | 按钮是否镂空，背景色透明 | [1.0.0](../framework/compatibility.html) |
|  | disabled | boolean | false | 否 | 是否禁用 | [1.0.0](../framework/compatibility.html) |
|  | loading | boolean | false | 否 | 名称前是否带 loading 图标 | [1.0.0](../framework/compatibility.html) |
|  | form-type | string |  | 否 | 用于 [form](form.html) 组件，点击分别会触发 [form](form.html) 组件的 submit/reset 事件 | [1.0.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | submit | 提交表单 |  | | reset | 重置表单 |  | | submitToGroup | 转发文本到聊天 | [3.7.8](../framework/compatibility.html) | | | | | | |
|  | open-type | string |  | 否 | 微信开放能力 | [1.1.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | contact | 打开客服会话，如果用户在会话中点击消息卡片后返回小程序，可以从 bindcontact 回调中获得具体信息，[具体说明](../framework/open-ability/customer-message/customer-message.html)。鸿蒙 OS 暂不支持 | [1.1.0](../framework/compatibility.html) | | liveActivity | 通过前端获取[新的一次性订阅消息下发机制](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/subscribe-message-2.html)使用的 code | [2.26.2](../framework/compatibility.html) | | share | 触发用户转发，使用前建议先阅读[使用指引](../framework/open-ability/share.html#使用指引) | [1.2.0](../framework/compatibility.html) | | getPhoneNumber | 手机号快速验证，向用户申请，并在用户同意后，快速填写和验证手机，[具体说明](../framework/open-ability/getPhoneNumber.html) （\*小程序插件中不能使用\*） | [1.2.0](../framework/compatibility.html) | | getRealtimePhoneNumber | 手机号实时验证，向用户申请，并在用户同意后，快速填写和实时验证手机号。[具体说明](../framework/open-ability/getRealtimePhoneNumber.html) （\*小程序插件中不能使用\*） | [2.24.4](../framework/compatibility.html) | | getUserInfo | 获取用户信息，可以从bindgetuserinfo回调中获取到用户信息 （\*小程序插件中不能使用\*） | [1.3.0](../framework/compatibility.html) | | launchApp | 打开APP，可以通过app-parameter属性设定向APP传的参数[具体说明](../framework/open-ability/launchApp.html) | [1.9.5](../framework/compatibility.html) | | openSetting | 打开授权设置页 | [2.0.7](../framework/compatibility.html) | | feedback | 打开“意见反馈”页面，用户可提交反馈内容并上传[日志](../api/base/debug/wx.getLogManager.html)，开发者可以登录[小程序管理后台](https://mp.weixin.qq.com/)后进入左侧菜单“客服反馈”页面获取到反馈内容 | [2.1.0](../framework/compatibility.html) | | chooseAvatar | 获取用户头像，可以从bindchooseavatar回调中获取到头像信息 | [2.21.2](../framework/compatibility.html) | | agreePrivacyAuthorization | 用户同意隐私协议按钮。用户点击一次此按钮后，所有已声明过的隐私接口可以正常调用。可通过 bindagreeprivacyauthorization 监听用户同意隐私协议事件。隐私合规开发指南详情可见[《小程序隐私协议开发指南》](https://developers.weixin.qq.com/miniprogram/dev/framework/user-privacy/PrivacyAuthorize.html) | [2.32.3](../framework/compatibility.html) | | | | | | |
|  | hover-class | string | button-hover | 否 | 指定按钮按下去的样式类。当 `hover-class="none"` 时，没有点击态效果 | [1.0.0](../framework/compatibility.html) |
|  | hover-stop-propagation | boolean | false | 否 | 指定是否阻止本节点的祖先节点出现点击态 | [1.5.0](../framework/compatibility.html) |
|  | hover-start-time | number | 20 | 否 | 按住后多久出现点击态，单位毫秒 | [1.0.0](../framework/compatibility.html) |
|  | hover-stay-time | number | 70 | 否 | 手指松开后点击态保留时间，单位毫秒 | [1.0.0](../framework/compatibility.html) |
|  | lang | string | en | 否 | 指定返回用户信息的语言，zh\_CN 简体中文，zh\_TW 繁体中文，en 英文。 | [1.3.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | en | 英文 | | zh\_CN | 简体中文 | | zh\_TW | 繁体中文 | | | | | | |
|  | session-from | string |  | 否 | 会话来源，open-type="contact"时有效，长度不超过 1024 个字符 | [1.4.0](../framework/compatibility.html) |
|  | send-message-title | string | 当前标题 | 否 | 会话内消息卡片标题，open-type="contact"时有效 | [1.5.0](../framework/compatibility.html) |
|  | send-message-path | string | 当前分享路径 | 否 | 会话内消息卡片点击跳转小程序路径，open-type="contact"时有效 | [1.5.0](../framework/compatibility.html) |
|  | send-message-img | string | 截图 | 否 | 会话内消息卡片图片，open-type="contact"时有效 | [1.5.0](../framework/compatibility.html) |
|  | app-parameter | string |  | 否 | 打开 APP 时，向 APP 传递的参数，open-type=launchApp时有效 | [1.9.5](../framework/compatibility.html) |
|  | show-message-card | boolean | false | 否 | 是否显示会话内消息卡片，设置此参数为 true，用户进入客服会话会在右下角显示"可能要发送的小程序"提示，用户点击后可以快速发送小程序消息，open-type="contact"时有效 | [1.5.0](../framework/compatibility.html) |
|  | phone-number-no-quota-toast | boolean | true | 否 | 当手机号快速验证或手机号实时验证额度用尽时，是否对用户展示“申请获取你的手机号，但该功能使用次数已达当前小程序上限，暂时无法使用”的提示，默认展示，open-type="getPhoneNumber" 或 open-type="getRealtimePhoneNumber" 时有效 | [3.0.1](../framework/compatibility.html) |
|  | need-show-entrance | boolean | true | 否 | 转发的文本消息是否要带小程序入口 | [3.7.8](../framework/compatibility.html) |
|  | entrance-path | string | '' | 否 | 从消息小程序入口打开小程序的路径，默认为聊天工具启动路径 | [3.7.8](../framework/compatibility.html) |
|  | bindgetuserinfo | eventhandle |  | 否 | 用户点击该按钮时，会返回获取到的用户信息，回调的detail数据与[wx.getUserInfo](../api/open-api/user-info/wx.getUserInfo.html)返回的一致，open-type="getUserInfo"时有效 | [1.3.0](../framework/compatibility.html) |
|  | bindcontact | eventhandle |  | 否 | 客服消息回调，open-type="contact"时有效。 | [1.5.0](../framework/compatibility.html) |
|  | createliveactivity | eventhandle |  | 否 | [新的一次性订阅消息下发机制](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/subscribe-message-2.html)回调，open-type=liveActivity时有效 | [2.26.2](../framework/compatibility.html) |
|  | bindgetphonenumber | eventhandle |  | 否 | 手机号快速验证回调，open-type=getPhoneNumber时有效。Tips：在触发 bindgetphonenumber 回调后应立即隐藏手机号按钮组件，或置为 disabled 状态，避免用户重复授权手机号产生额外费用。 | [1.2.0](../framework/compatibility.html) |
|  | bindgetrealtimephonenumber | eventhandle |  | 否 | 手机号实时验证回调，open-type=getRealtimePhoneNumber 时有效。Tips：在触发 bindgetrealtimephonenumber 回调后应立即隐藏手机号按钮组件，或置为 disabled 状态，避免用户重复授权手机号产生额外费用。 | [2.24.4](../framework/compatibility.html) |
|  | binderror | eventhandle |  | 否 | 当使用开放能力时，发生错误的回调，open-type=launchApp时有效 | [1.9.5](../framework/compatibility.html) |
|  | bindopensetting | eventhandle |  | 否 | 在打开授权设置页后回调，open-type=openSetting时有效 | [2.0.7](../framework/compatibility.html) |
|  | bindlaunchapp | eventhandle |  | 否 | 打开 APP 成功的回调，open-type=launchApp时有效 | [2.4.4](../framework/compatibility.html) |
|  | bindchooseavatar | eventhandle |  | 否 | 获取用户头像回调，open-type=chooseAvatar时有效 | [2.21.2](../framework/compatibility.html) |
|  | bindagreeprivacyauthorization | eventhandle |  | 否 | 用户同意隐私协议事件回调，open-type=agreePrivacyAuthorization时有效 （Tips: 如果使用 onNeedPrivacyAuthorization 接口，需要在 bindagreeprivacyauthorization 触发后再调用 `resolve({ event: "agree", buttonId })`） | [2.32.3](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| default | 默认大小 |
| mini | 小尺寸 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| primary | 绿色 |
| default | 白色 |
| warn | 红色 |

**通用属性**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| submit | 提交表单 |  |
| reset | 重置表单 |  |
| submitToGroup | 转发文本到聊天 | [3.7.8](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| contact | 打开客服会话，如果用户在会话中点击消息卡片后返回小程序，可以从 bindcontact 回调中获得具体信息，[具体说明](../framework/open-ability/customer-message/customer-message.html)。鸿蒙 OS 暂不支持 | [1.1.0](../framework/compatibility.html) |
| liveActivity | 通过前端获取[新的一次性订阅消息下发机制](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/subscribe-message-2.html)使用的 code | [2.26.2](../framework/compatibility.html) |
| share | 触发用户转发，使用前建议先阅读[使用指引](../framework/open-ability/share.html#使用指引) | [1.2.0](../framework/compatibility.html) |
| getPhoneNumber | 手机号快速验证，向用户申请，并在用户同意后，快速填写和验证手机，[具体说明](../framework/open-ability/getPhoneNumber.html) （\*小程序插件中不能使用\*） | [1.2.0](../framework/compatibility.html) |
| getRealtimePhoneNumber | 手机号实时验证，向用户申请，并在用户同意后，快速填写和实时验证手机号。[具体说明](../framework/open-ability/getRealtimePhoneNumber.html) （\*小程序插件中不能使用\*） | [2.24.4](../framework/compatibility.html) |
| getUserInfo | 获取用户信息，可以从bindgetuserinfo回调中获取到用户信息 （\*小程序插件中不能使用\*） | [1.3.0](../framework/compatibility.html) |
| launchApp | 打开APP，可以通过app-parameter属性设定向APP传的参数[具体说明](../framework/open-ability/launchApp.html) | [1.9.5](../framework/compatibility.html) |
| openSetting | 打开授权设置页 | [2.0.7](../framework/compatibility.html) |
| feedback | 打开“意见反馈”页面，用户可提交反馈内容并上传[日志](../api/base/debug/wx.getLogManager.html)，开发者可以登录[小程序管理后台](https://mp.weixin.qq.com/)后进入左侧菜单“客服反馈”页面获取到反馈内容 | [2.1.0](../framework/compatibility.html) |
| chooseAvatar | 获取用户头像，可以从bindchooseavatar回调中获取到头像信息 | [2.21.2](../framework/compatibility.html) |
| agreePrivacyAuthorization | 用户同意隐私协议按钮。用户点击一次此按钮后，所有已声明过的隐私接口可以正常调用。可通过 bindagreeprivacyauthorization 监听用户同意隐私协议事件。隐私合规开发指南详情可见[《小程序隐私协议开发指南》](https://developers.weixin.qq.com/miniprogram/dev/framework/user-privacy/PrivacyAuthorize.html) | [2.32.3](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| en | 英文 |
| zh\_CN | 简体中文 |
| zh\_TW | 繁体中文 |

---

### checkbox

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/checkbox.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| value | string |  | 否 | [checkbox](checkbox.html)标识，选中时触发[checkbox-group](checkbox-group.html)的 change 事件，并携带 [checkbox](checkbox.html) 的 value | [1.0.0](../framework/compatibility.html) |
| disabled | boolean | false | 否 | 是否禁用 | [1.0.0](../framework/compatibility.html) |
| checked | boolean | false | 否 | 当前是否选中，可用来设置默认选中 | [1.0.0](../framework/compatibility.html) |
| color | string | #09BB07 | 否 | checkbox的颜色，同css的color | [1.0.0](../framework/compatibility.html) |

---

### checkbox-group

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/checkbox-group.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| bindchange | EventHandle |  | 否 | [checkbox-group](checkbox-group.html)中选中项发生改变时触发 change 事件，detail = {value:[选中的checkbox的value的数组]} | [1.0.0](../framework/compatibility.html) |

---

### editor

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/editor.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| read-only | boolean | false | 否 | 设置编辑器为只读 | [2.7.0](../framework/compatibility.html) |
| placeholder | string |  | 否 | 提示信息 | [2.7.0](../framework/compatibility.html) |
| show-img-size | boolean | false | 否 | 点击图片时显示图片大小控件 | [2.7.0](../framework/compatibility.html) |
| show-img-toolbar | boolean | false | 否 | 点击图片时显示工具栏控件 | [2.7.0](../framework/compatibility.html) |
| show-img-resize | boolean | false | 否 | 点击图片时显示修改尺寸控件 | [2.7.0](../framework/compatibility.html) |
| enable-formats | Array.<string> | 所有格式 | 否 | 编辑器允许的名单内的格式 | [3.2.2](../framework/compatibility.html) |
| enterkeyhint | string | enter | 否 | 定义虚拟键盘回车键的[操作标签](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Global_attributes/enterkeyhint) | [3.7.11](../framework/compatibility.html) |
| confirm-hold | boolean | true | 否 | 点击键盘回车键时是否保持键盘不收起 | [3.7.11](../framework/compatibility.html) |
| bindready | eventhandle |  | 否 | 编辑器初始化完成时触发 | [2.7.0](../framework/compatibility.html) |
| bindfocus | eventhandle |  | 否 | 编辑器聚焦时触发，event.detail = {html, text, delta} | [2.7.0](../framework/compatibility.html) |
| bindblur | eventhandle |  | 否 | 编辑器失去焦点时触发，detail = {html, text, delta} | [2.7.0](../framework/compatibility.html) |
| bindinput | eventhandle |  | 否 | 编辑器内容改变时触发，detail = {html, text, delta} | [2.7.0](../framework/compatibility.html) |
| bindstatuschange | eventhandle |  | 否 | 通过 Context 方法改变编辑器内样式时触发，返回选区已设置的样式 | [2.7.0](../framework/compatibility.html) |

**支持的标签**

| 类型 | 节点 |
| --- | --- |
| 行内元素 | `<span> <strong> <b> <ins> <em> <i> <u> <a> <del> <s> <sub> <sup> <img>` |
| 块级元素 | `<p> <h1> <h2> <h3> <h4> <h5> <h6> <hr> <ol> <ul> <li>` |

**支持的内联样式**

| 类型 | 样式 |
| --- | --- |
| 块级样式 | `text-align` `direction` `margin` `margin-top` `margin-left` `margin-right` `margin-bottom`   `padding` `padding-top` `padding-left` `padding-right` `padding-bottom` `line-height` `text-indent` |
| 行内样式 | `font` `font-size` `font-style` `font-variant` `font-weight` `font-family`   `letter-spacing` `text-decoration` `color` `background-color` |

**enable-formats 属性列表**

| name | version |
| --- | --- |
| bold | 3.2.2 |
| italic | 3.2.2 |
| underline | 3.2.2 |

---

### editor-portal

基础库 3.7.11 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/editor-portal.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| key | string |  | 是 | 自定义区块的 blockId |

---

### form

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/form.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| report-submit | boolean | false | 否 | 是否返回 formId 用于发送[模板消息](../framework/open-ability/template-message.html) | [1.0.0](../framework/compatibility.html) |
| report-submit-timeout | number | 0 | 否 | 等待一段时间（毫秒数）以确认 formId 是否生效。如果未指定这个参数，formId 有很小的概率是无效的（如遇到网络失败的情况）。指定这个参数将可以检测 formId 是否有效，以这个参数的时间作为这项检测的超时时间。如果失败，将返回 requestFormId:fail 开头的 formId | [2.6.2](../framework/compatibility.html) |
| bindsubmit | eventhandle |  | 否 | 携带 form 中的数据触发 submit 事件，event.detail = {value : {'name': 'value'} , formId: ''} | [1.0.0](../framework/compatibility.html) |
| bindreset | eventhandle |  | 否 | 表单重置时会触发 reset 事件 | [1.0.0](../framework/compatibility.html) |
| bindsubmitToGroup | eventhandle |  | 否 | 用户发送文本到聊天后触发，但不代表最终发送成功 | [3.7.8](../framework/compatibility.html) |

**wx://form-field**

| 属性名 | 类型 | 描述 | 最低版本 |
| --- | --- | --- | --- |
| name | String | 在表单中的字段名 | [1.6.7](../framework/compatibility.html) |
| value | 任意 | 在表单中的字段值 | [1.6.7](../framework/compatibility.html) |

---

### input

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/input.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | value | string |  | 是 | 输入框的初始内容 | [1.0.0](../framework/compatibility.html) |
|  | type | string | text | 否 | input 的类型 | [1.0.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | text | 文本输入键盘 |  | | number | 数字输入键盘 |  | | idcard | 身份证输入键盘 |  | | digit | 带小数点的数字键盘 |  | | safe-password | 密码安全输入键盘 [指引](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/safe-password.html)。仅 Webview 支持。 | [2.18.0](../framework/compatibility.html) | | nickname | 昵称输入键盘。 | [2.21.2](../framework/compatibility.html) | | | | | | |
|  | password | boolean | false | 否 | 是否是密码类型 | [1.0.0](../framework/compatibility.html) |
|  | placeholder | string |  | 是 | 输入框为空时占位符 | [1.0.0](../framework/compatibility.html) |
|  | placeholder-style | string |  | 是 | 指定 placeholder 的样式 | [1.0.0](../framework/compatibility.html) |
|  | disabled | boolean | false | 否 | 是否禁用 | [1.0.0](../framework/compatibility.html) |
|  | maxlength | number | 140 | 否 | 最大输入长度，设置为 -1 的时候不限制最大长度 | [1.0.0](../framework/compatibility.html) |
|  | cursor-spacing | number | 0 | 否 | 指定光标与键盘的距离，取 input 距离底部的距离和 cursor-spacing 指定的距离的最小值作为光标与键盘的距离 | [1.0.0](../framework/compatibility.html) |
|  | auto-focus | boolean | false | 否 | (即将废弃，请直接使用 focus )自动聚焦，拉起键盘 | [1.0.0](../framework/compatibility.html) |
|  | focus | boolean | false | 否 | 获取焦点 | [1.0.0](../framework/compatibility.html) |
|  | confirm-type | string | done | 否 | 设置键盘右下角按钮的文字，仅在type='text'时生效 | [1.1.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | send | 右下角按钮为“发送” | | search | 右下角按钮为“搜索” | | next | 右下角按钮为“下一个” | | go | 右下角按钮为“前往” | | done | 右下角按钮为“完成” | | | | | | |
|  | always-embed | boolean | false | 否 | 强制 input 处于同层状态，默认 focus 时 input 会切到非同层状态 (仅在 iOS 下生效) | [2.10.4](../framework/compatibility.html) |
|  | confirm-hold | boolean | false | 否 | 点击键盘右下角按钮时是否保持键盘不收起 | [1.1.0](../framework/compatibility.html) |
|  | cursor | number |  | 是 | 指定focus时的光标位置 | [1.5.0](../framework/compatibility.html) |
|  | cursor-color | string |  | 是 | 光标颜色。iOS 下的格式为十六进制颜色值 #000000，安卓下的只支持 default 和 green，Skyline 下无限制 | [3.1.0](../framework/compatibility.html) |
|  | selection-start | number | -1 | 否 | 光标起始位置，自动聚集时有效，需与selection-end搭配使用 | [1.9.0](../framework/compatibility.html) |
|  | selection-end | number | -1 | 否 | 光标结束位置，自动聚集时有效，需与selection-start搭配使用 | [1.9.0](../framework/compatibility.html) |
|  | adjust-position | boolean | true | 否 | 键盘弹起时，是否自动上推页面 | [1.9.90](../framework/compatibility.html) |
|  | hold-keyboard | boolean | false | 否 | focus时，点击页面的时候不收起键盘 | [2.8.2](../framework/compatibility.html) |
|  | safe-password-cert-path | string |  | 否 | 安全键盘加密公钥的路径，只支持包内路径。鸿蒙 OS 暂不支持 | [2.18.0](../framework/compatibility.html) |
|  | safe-password-length | number |  | 否 | 安全键盘输入密码长度。鸿蒙 OS 暂不支持 | [2.18.0](../framework/compatibility.html) |
|  | safe-password-time-stamp | number |  | 否 | 安全键盘加密时间戳。鸿蒙 OS 暂不支持 | [2.18.0](../framework/compatibility.html) |
|  | safe-password-nonce | string |  | 否 | 安全键盘加密盐值。鸿蒙 OS 暂不支持 | [2.18.0](../framework/compatibility.html) |
|  | safe-password-salt | string |  | 否 | 安全键盘计算hash盐值，若指定custom-hash 则无效。鸿蒙 OS 暂不支持 | [2.18.0](../framework/compatibility.html) |
|  | safe-password-custom-hash | string |  | 否 | 安全键盘计算hash的算法表达式，如 `md5(sha1('foo' + sha256(sm3(password + 'bar'))))`。鸿蒙 OS 暂不支持 | [2.18.0](../framework/compatibility.html) |
|  | bindinput | eventhandle |  | 是 | 键盘输入时或内容改变时触发。event.detail = { value: string, cursor?: number, keyCode?: number }，cursor 为光标位置，keyCode 为键值。2.1.0 起支持，处理函数可以直接 return 一个字符串，将替换输入框的内容。 | [1.0.0](../framework/compatibility.html) |
|  | bindchange | eventhandle |  | 是 | 键盘非聚焦状态内容改变时触发。event.detail = { value: string } | [1.0.0](../framework/compatibility.html) |
|  | bindfocus | eventhandle |  | 是 | 输入框聚焦时触发，event.detail = { value: string, height: number }，height 为键盘高度，在基础库 1.9.90 起支持 | [1.0.0](../framework/compatibility.html) |
|  | bindblur | eventhandle |  | 是 | 输入框失去焦点时触发，event.detail = { value: string, encryptedValue?: string, encryptError?: string } | [1.0.0](../framework/compatibility.html) |
|  | bindconfirm | eventhandle |  | 是 | 点击完成按钮时触发，event.detail = { value: string, encryptedValue?: string, encryptError?: string } | [1.0.0](../framework/compatibility.html) |
|  | bindkeyboardheightchange | eventhandle |  | 是 | 键盘高度发生变化的时候触发此事件，event.detail = {height: number, duration: number} | [2.7.0](../framework/compatibility.html) |
|  | bindnicknamereview | eventhandle |  | 是 | 用户昵称审核完毕后触发，仅在 type 为 "nickname" 时有效，event.detail = { pass: boolean, timeout: boolean } | [2.29.1](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| text | 文本输入键盘 |  |
| number | 数字输入键盘 |  |
| idcard | 身份证输入键盘 |  |
| digit | 带小数点的数字键盘 |  |
| safe-password | 密码安全输入键盘 [指引](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/safe-password.html)。仅 Webview 支持。 | [2.18.0](../framework/compatibility.html) |
| nickname | 昵称输入键盘。 | [2.21.2](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| send | 右下角按钮为“发送” |
| search | 右下角按钮为“搜索” |
| next | 右下角按钮为“下一个” |
| go | 右下角按钮为“前往” |
| done | 右下角按钮为“完成” |

**Skyline 特有属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | bind:selectionchange | eventhandle |  | 否 | 选区改变事件, {selectionStart, selectionEnd} | [3.2.0](../framework/compatibility.html) |
|  | bind:keyboardcompositionstart | eventhandle |  | 否 | 输入法开始新的输入时触发 （仅当输入法支持时触发） | [3.2.0](../framework/compatibility.html) |
|  | bind:keyboardcompositionupdate | eventhandle |  | 否 | 输入法输入字符时触发（仅当输入法支持时触发） | [3.2.0](../framework/compatibility.html) |
|  | bind:keyboardcompositionend | eventhandle |  | 否 | 输入法输入结束时触发（仅当输入法支持时触发） | [3.2.0](../framework/compatibility.html) |
|  | worklet:onkeyboardheightchange | worklet |  | 否 | 键盘高度变化时触发。event.detail = {height: height, pageBottomPadding: pageBottomPadding}； height: 键盘高度，pageBottomPadding: 页面上推高度 | [3.2.4](../framework/compatibility.html) |

**WebView 特有属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | placeholder-class | string | input-placeholder | 否 | 指定 placeholder 的样式类 | [1.0.0](../framework/compatibility.html) |

---

### keyboard-accessory

基础库 2.15.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/keyboard-accessory.html

---

### label

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/label.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| for | string |  | 否 | 绑定控件的 id | [1.0.0](../framework/compatibility.html) |

---

### picker

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/picker.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | header-text | string |  | 否 | 选择器的标题，仅安卓可用 | [2.11.0](../framework/compatibility.html) |
|  | mode | string | selector | 否 | 选择器类型 | [1.0.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | selector | 普通选择器 | | multiSelector | 多列选择器 | | time | 时间选择器 | | date | 日期选择器 | | region | 省市区选择器 | | | | | | |
|  | disabled | boolean | false | 否 | 是否禁用 | [1.0.0](../framework/compatibility.html) |
|  | bindcancel | eventhandle |  | 否 | 取消选择时触发 | [1.9.90](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| selector | 普通选择器 |
| multiSelector | 多列选择器 |
| time | 时间选择器 |
| date | 日期选择器 |
| region | 省市区选择器 |

**普通选择器：mode = selector**

| 属性名 | 类型 | 默认值 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
| range | array/object array | [] | mode 为 selector 或 multiSelector 时，range 有效 |  |
| range-key | string |  | 当 range 是一个 Object Array 时，通过 range-key 来指定 Object 中 key 的值作为选择器显示内容 |  |
| value | number | 0 | 表示选择了 range 中的第几个（下标从 0 开始） |  |
| bindchange | eventhandle |  | value 改变时触发 change 事件，event.detail = {value} |  |

**多列选择器：mode = multiSelector**

| 属性名 | 类型 | 默认值 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
| range | array/object array | [] | mode 为 selector 或 multiSelector 时，range 有效 |  |
| range-key | string |  | 当 range 是一个 Object Array 时，通过 range-key 来指定 Object 中 key 的值作为选择器显示内容 |  |
| value | array | [] | 表示选择了 range 中的第几个（下标从 0 开始） |  |
| bindchange | eventhandle |  | value 改变时触发 change 事件，event.detail = {value} |  |
| bindcolumnchange | eventhandle |  | 列改变时触发 |  |

**时间选择器：mode = time**

| 属性名 | 类型 | 默认值 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
| value | string |  | 表示选中的时间，格式为"hh:mm" |  |
| start | string |  | 表示有效时间范围的开始，字符串格式为"hh:mm" |  |
| end | string |  | 表示有效时间范围的结束，字符串格式为"hh:mm" |  |
| bindchange | eventhandle |  | value 改变时触发 change 事件，event.detail = {value} |  |

**日期选择器：mode = date**

| 属性名 | 类型 | 默认值 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
| value | string | 当天 | 表示选中的日期，格式为"YYYY-MM-DD" |  |
| start | string |  | 表示有效日期范围的开始，字符串格式为"YYYY-MM-DD" |  |
| end | string |  | 表示有效日期范围的结束，字符串格式为"YYYY-MM-DD" |  |
| fields | string | day | 有效值 year,month,day，表示选择器的粒度 |  |
| bindchange | eventhandle |  | value 改变时触发 change 事件，event.detail = {value} |  |

**日期选择器：mode = date**

| 值 | 说明 |
| --- | --- |
| year | 选择器粒度为年 |
| month | 选择器粒度为月份 |
| day | 选择器粒度为天 |

**省市区选择器：mode = region 1.4.0**

| 属性名 | 类型 | 默认值 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
| value | array | [] | 表示选中的省市区，默认选中每一列的第一个值 |  |
| custom-item | string |  | 可为每一列的顶部添加一个自定义的项 | [1.5.0](../framework/compatibility.html) |
| level | string | region | 选择器层级 | [2.21.1](../framework/compatibility.html) |
| bindchange | eventhandle |  | value 改变时触发 change 事件，event.detail = {value, code, postcode}，其中字段 code 是统计用区划代码，postcode 是邮政编码 |  |

**省市区选择器：mode = region 1.4.0**

| 值 | 说明 |
| --- | --- |
| province | 省级选择器 |
| city | 市级选择器 |
| region | 区级选择器 |
| sub-district | 街道选择器 |

---

### picker-view

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/picker-view.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | value | Array.<number> |  | 否 | 数组中的数字依次表示 picker-view 内的 picker-view-column 选择的第几项（下标从 0 开始），数字大于 picker-view-column 可选项长度时，选择最后一项。 | [1.0.0](../framework/compatibility.html) |
|  | mask-class | string |  | 否 | 设置蒙层的类名 | [1.5.0](../framework/compatibility.html) |
|  | indicator-style | string |  | 否 | 设置选择器中间选中框的样式 | [1.0.0](../framework/compatibility.html) |
|  | bindchange | eventhandle |  | 否 | 滚动选择时触发change事件，event.detail = {value}；value为数组，表示 picker-view 内的 picker-view-column 当前选择的是第几项（下标从 0 开始） | [1.0.0](../framework/compatibility.html) |
|  | bindpickstart | eventhandle |  | 否 | 当滚动选择开始时候触发事件 | [2.3.1](../framework/compatibility.html) |
|  | bindpickend | eventhandle |  | 否 | 当滚动选择结束时候触发事件 | [2.3.1](../framework/compatibility.html) |

**WebView 特有属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | indicator-class | string |  | 否 | 设置选择器中间选中框的类名 | [1.1.0](../framework/compatibility.html) |
|  | mask-style | string |  | 否 | 设置蒙层的样式 | [1.5.0](../framework/compatibility.html) |
|  | immediate-change | boolean | false | 否 | 是否在手指松开时立即触发 change 事件。若不开启则会在滚动动画结束后触发 change 事件。 | [2.21.1](../framework/compatibility.html) |

---

### picker-view-column

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/picker-view-column.html

---

### radio

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/radio.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| value | string |  | 否 | [radio](radio.html) 标识。当该[radio](radio.html) 选中时，[radio-group](radio-group.html) 的 change 事件会携带[radio](radio.html)的value | [1.0.0](../framework/compatibility.html) |
| checked | boolean | false | 否 | 当前是否选中 | [1.0.0](../framework/compatibility.html) |
| disabled | boolean | false | 否 | 是否禁用 | [1.0.0](../framework/compatibility.html) |
| color | string | #09BB07 | 否 | radio的颜色，同css的color | [1.0.0](../framework/compatibility.html) |

---

### radio-group

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/radio-group.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| bindchange | EventHandle |  | 否 | [radio-group](radio-group.html)中选中项发生改变时触发 change 事件，detail = {value:[选中的radio的value的数组]} | [1.0.0](../framework/compatibility.html) |

---

### slider

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/slider.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| min | number | 0 | 否 | 最小值 | [1.0.0](../framework/compatibility.html) |
| max | number | 100 | 否 | 最大值 | [1.0.0](../framework/compatibility.html) |
| step | number | 1 | 否 | 步长，取值必须大于 0，并且可被(max - min)整除 | [1.0.0](../framework/compatibility.html) |
| disabled | boolean | false | 否 | 是否禁用 | [1.0.0](../framework/compatibility.html) |
| value | number | 0 | 否 | 当前取值 | [1.0.0](../framework/compatibility.html) |
| color | color | #e9e9e9 | 否 | 背景条的颜色（请使用 backgroundColor） | [1.0.0](../framework/compatibility.html) |
| selected-color | color | #1aad19 | 否 | 已选择的颜色（请使用 activeColor） | [1.0.0](../framework/compatibility.html) |
| activeColor | color | #1aad19 | 否 | 已选择的颜色 | [1.0.0](../framework/compatibility.html) |
| backgroundColor | color | #e9e9e9 | 否 | 背景条的颜色 | [1.0.0](../framework/compatibility.html) |
| block-size | number | 28 | 否 | 滑块的大小，取值范围为 12 - 28 | [1.9.0](../framework/compatibility.html) |
| block-color | color | #ffffff | 否 | 滑块的颜色 | [1.9.0](../framework/compatibility.html) |
| show-value | boolean | false | 否 | 是否显示当前 value | [1.0.0](../framework/compatibility.html) |
| bindchange | eventhandle |  | 否 | 完成一次拖动后触发的事件，event.detail = {value} | [1.0.0](../framework/compatibility.html) |
| bindchanging | eventhandle |  | 否 | 拖动过程中触发的事件，event.detail = {value} | [1.7.0](../framework/compatibility.html) |

---

### switch

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/switch.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| checked | boolean | false | 否 | 是否选中 | [1.0.0](../framework/compatibility.html) |
| disabled | boolean | false | 否 | 是否禁用 | [1.0.0](../framework/compatibility.html) |
| type | string | switch | 否 | 样式，有效值：switch, checkbox | [1.0.0](../framework/compatibility.html) |
| color | string | #04BE02 | 否 | switch 的颜色，同 css 的 color | [1.0.0](../framework/compatibility.html) |
| bindchange | eventhandle |  | 否 | 点击导致 checked 改变时会触发 change 事件，event.detail={ value} | [1.0.0](../framework/compatibility.html) |

---

### textarea

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/textarea.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | value | string |  | 否 | 输入框的内容 | [1.0.0](../framework/compatibility.html) |
|  | placeholder | string |  | 否 | 输入框为空时占位符 | [1.0.0](../framework/compatibility.html) |
|  | placeholder-style | string |  | 否 | 指定 placeholder 的样式，目前仅支持color,font-size,font-weight,line-height | [1.0.0](../framework/compatibility.html) |
|  | disabled | boolean | false | 否 | 是否禁用 | [1.0.0](../framework/compatibility.html) |
|  | maxlength | number | 140 | 否 | 最大输入长度，设置为 -1 的时候不限制最大长度 | [1.0.0](../framework/compatibility.html) |
|  | auto-focus | boolean | false | 否 | 自动聚焦，拉起键盘。 | [1.0.0](../framework/compatibility.html) |
|  | focus | boolean | false | 否 | 获取焦点 | [1.0.0](../framework/compatibility.html) |
|  | auto-height | boolean | false | 否 | 是否自动增高，设置auto-height时，style.height不生效 | [1.0.0](../framework/compatibility.html) |
|  | cursor-spacing | number | 0 | 否 | 指定光标与键盘的距离。取`textarea`距离底部的距离和`cursor-spacing`指定的距离的最小值作为光标与键盘的距离 | [1.0.0](../framework/compatibility.html) |
|  | cursor | number | -1 | 否 | 指定focus时的光标位置 | [1.5.0](../framework/compatibility.html) |
|  | selection-start | number | -1 | 否 | 光标起始位置，自动聚集时有效，需与`selection-end`搭配使用 | [1.9.0](../framework/compatibility.html) |
|  | selection-end | number | -1 | 否 | 光标结束位置，自动聚集时有效，需与`selection-start`搭配使用 | [1.9.0](../framework/compatibility.html) |
|  | adjust-position | boolean | true | 否 | 键盘弹起时，是否自动上推页面 | [1.9.90](../framework/compatibility.html) |
|  | hold-keyboard | boolean | false | 否 | focus时，点击页面的时候不收起键盘 | [2.8.2](../framework/compatibility.html) |
|  | disable-default-padding | boolean | false | 否 | 是否去掉 iOS 下的默认内边距 | [2.10.0](../framework/compatibility.html) |
|  | confirm-type | string | return | 否 | 设置键盘右下角按钮的文字 | [2.13.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | send | 右下角按钮为“发送” | | search | 右下角按钮为“搜索” | | next | 右下角按钮为“下一个” | | go | 右下角按钮为“前往” | | done | 右下角按钮为“完成” | | return | 右下角按钮为“换行” | | | | | | |
|  | confirm-hold | boolean | false | 否 | 点击键盘右下角按钮时是否保持键盘不收起 | [2.16.0](../framework/compatibility.html) |
|  | adjust-keyboard-to | boolean | cursor | 否 | 键盘对齐位置。 | [2.16.1](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | cursor | 对齐光标位置 | | bottom | 对齐输入框底部 | | | | | | |
|  | bindfocus | eventhandle |  | 否 | 输入框聚焦时触发，event.detail = { value, height }，height 为键盘高度，在基础库 1.9.90 起支持 | [1.0.0](../framework/compatibility.html) |
|  | bindblur | eventhandle |  | 否 | 输入框失去焦点时触发，event.detail = {value, cursor} | [1.0.0](../framework/compatibility.html) |
|  | bindlinechange | eventhandle |  | 否 | 输入框行数变化时调用，event.detail = {height: 0, heightRpx: 0, lineCount: 0} | [1.0.0](../framework/compatibility.html) |
|  | bindinput | eventhandle |  | 否 | 当键盘输入时，触发 input 事件，event.detail = {value, cursor, keyCode}，keyCode 为键值，目前工具还不支持返回keyCode参数。\*\*bindinput 处理函数的返回值并不会反映到 textarea 上\*\* | [1.0.0](../framework/compatibility.html) |
|  | bindconfirm | eventhandle |  | 否 | 点击完成时， 触发 confirm 事件，event.detail = {value: value} | [1.0.0](../framework/compatibility.html) |
|  | bindkeyboardheightchange | eventhandle |  | 否 | 键盘高度发生变化的时候触发此事件，event.detail = {height: height, duration: duration} | [2.7.0](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| send | 右下角按钮为“发送” |
| search | 右下角按钮为“搜索” |
| next | 右下角按钮为“下一个” |
| go | 右下角按钮为“前往” |
| done | 右下角按钮为“完成” |
| return | 右下角按钮为“换行” |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| cursor | 对齐光标位置 |
| bottom | 对齐输入框底部 |

**Skyline 特有属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | placeholder-style | string |  | 否 | 需传入对象，格式为 `{ fontSize: number, fontWeight: string, color: string }` |  |
|  | bind:selectionchange | eventhandle |  | 否 | 选区改变事件, {selectionStart, selectionEnd} | [3.2.0](../framework/compatibility.html) |
|  | bind:keyboardcompositionstart | eventhandle |  | 否 | 输入法开始新的输入时触发 （仅当输入法支持时触发） | [3.2.0](../framework/compatibility.html) |
|  | bind:keyboardcompositionupdate | eventhandle |  | 否 | 输入法输入字符时触发（仅当输入法支持时触发） | [3.2.0](../framework/compatibility.html) |
|  | bind:keyboardcompositionend | eventhandle |  | 否 | 输入法输入结束时触发（仅当输入法支持时触发） | [3.2.0](../framework/compatibility.html) |

**WebView 特有属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | placeholder-class | string | textarea-placeholder | 否 | 指定 placeholder 的样式类，目前仅支持color,font-size和font-weight | [1.0.0](../framework/compatibility.html) |
|  | fixed | boolean | false | 否 | 如果 textarea 是在一个 `position:fixed` 的区域，需要显示指定属性 fixed 为 true | [1.0.0](../framework/compatibility.html) |
|  | show-confirm-bar | boolean | true | 否 | 是否显示键盘上方带有”完成“按钮那一栏 | [1.6.0](../framework/compatibility.html) |

---

### double-tap-gesture-handler

相关文档:手势系统

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/double-tap-gesture-handler.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | tag | string |  | 否 | 声明手势协商时的组件标识 |
|  | worklet:ongesture | eventhandler |  | 否 | 手势识别成功的回调 |
|  | | eventhandler 回调参数 | 说明 | | --- | --- | | state | 手势状态 | | absoluteX | 相对于全局的 X 坐标 | | absoluteY | 相对于全局的 Y 坐标 | | | | | |
|  | worklet:should-response-on-move | callback |  | 否 | 手指移动过程中手势是否响应 |
|  | worklet:should-accept-gesture | callback |  | 否 | 手势是否应该被识别 |
|  | simultaneous-handlers | Array.<string> |  | 否 | 声明可同时触发的手势节点 |
|  | native-view | string |  | 否 | 代理的原生节点类型 |

**通用属性**

| eventhandler 回调参数 | 说明 |
| --- | --- |
| state | 手势状态 |
| absoluteX | 相对于全局的 X 坐标 |
| absoluteY | 相对于全局的 Y 坐标 |

---

### force-press-gesture-handler

相关文档:手势系统

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/force-press-gesture-handler.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | tag | string |  | 否 | 声明手势协商时的组件标识 |
|  | worklet:ongesture | eventhandler |  | 否 | 手势识别成功的回调 |
|  | | eventhandler 回调参数 | 说明 | | --- | --- | | state | 手势状态 | | absoluteX | 相对于全局的 X 坐标 | | absoluteY | 相对于全局的 Y 坐标 | | pressure | 压力大小 | | | | | |
|  | worklet:should-accept-gesture | callback |  | 否 | 手势是否应该被识别 |
|  | simultaneous-handlers | Array.<string> |  | 否 | 声明可同时触发的手势节点 |
|  | native-view | string |  | 否 | 代理的原生节点类型 |

**通用属性**

| eventhandler 回调参数 | 说明 |
| --- | --- |
| state | 手势状态 |
| absoluteX | 相对于全局的 X 坐标 |
| absoluteY | 相对于全局的 Y 坐标 |
| pressure | 压力大小 |

---

### horizontal-drag-gesture-handler

相关文档:手势系统

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/horizontal-drag-gesture-handler.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | tag | string |  | 否 | 声明手势协商时的组件标识 |
|  | worklet:ongesture | eventhandler |  | 否 | 手势识别成功的回调 |
|  | | eventhandler 回调参数 | 说明 | | --- | --- | | state | 手势状态 | | absoluteX | 相对于全局的 X 坐标 | | absoluteY | 相对于全局的 Y 坐标 | | deltaX | 相对上一次，X 轴方向移动的坐标 | | deltaY | 相对上一次，Y 轴方向移动的坐标 | | velocityX | 手指离开屏幕时的横向速度（pixel per second) | | velocityY | 手指离开屏幕时的纵向速度（pixel per second) | | | | | |
|  | worklet:should-response-on-move | callback |  | 否 | 手指移动过程中手势是否响应 |
|  | worklet:should-accept-gesture | callback |  | 否 | 手势是否应该被识别 |
|  | simultaneous-handlers | Array.<string> |  | 否 | 声明可同时触发的手势节点 |
|  | native-view | string |  | 否 | 代理的原生节点类型 |

**通用属性**

| eventhandler 回调参数 | 说明 |
| --- | --- |
| state | 手势状态 |
| absoluteX | 相对于全局的 X 坐标 |
| absoluteY | 相对于全局的 Y 坐标 |
| deltaX | 相对上一次，X 轴方向移动的坐标 |
| deltaY | 相对上一次，Y 轴方向移动的坐标 |
| velocityX | 手指离开屏幕时的横向速度（pixel per second) |
| velocityY | 手指离开屏幕时的纵向速度（pixel per second) |

---

### long-press-gesture-handler

相关文档:手势系统

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/long-press-gesture-handler.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | tag | string |  | 否 | 声明手势协商时的组件标识 |
|  | worklet:ongesture | eventhandler |  | 否 | 手势识别成功的回调 |
|  | | eventhandler 回调参数 | 说明 | | --- | --- | | state | 手势状态 | | absoluteX | 相对于全局的 X 坐标 | | absoluteY | 相对于全局的 Y 坐标 | | translationX | 相对于初始触摸点的 X 轴偏移量 | | translationY | 相对于初始触摸点的 Y 轴偏移量 | | velocityX | 手指离开屏幕时的横向速度（pixel per second) | | velocityY | 手指离开屏幕时的纵向速度（pixel per second) | | | | | |
|  | worklet:should-response-on-move | callback |  | 否 | 手指移动过程中手势是否响应 |
|  | worklet:should-accept-gesture | callback |  | 否 | 手势是否应该被识别 |
|  | simultaneous-handlers | Array.<string> |  | 否 | 声明可同时触发的手势节点 |
|  | native-view | string |  | 否 | 代理的原生节点类型 |

**通用属性**

| eventhandler 回调参数 | 说明 |
| --- | --- |
| state | 手势状态 |
| absoluteX | 相对于全局的 X 坐标 |
| absoluteY | 相对于全局的 Y 坐标 |
| translationX | 相对于初始触摸点的 X 轴偏移量 |
| translationY | 相对于初始触摸点的 Y 轴偏移量 |
| velocityX | 手指离开屏幕时的横向速度（pixel per second) |
| velocityY | 手指离开屏幕时的纵向速度（pixel per second) |

---

### pan-gesture-handler

相关文档:手势系统

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/pan-gesture-handler.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | tag | string |  | 否 | 声明手势协商时的组件标识 |
|  | worklet:ongesture | eventhandler |  | 否 | 手势识别成功的回调 |
|  | | eventhandler 回调参数 | 说明 | | --- | --- | | state | 手势状态 | | absoluteX | 相对于全局的 X 坐标 | | absoluteY | 相对于全局的 Y 坐标 | | deltaX | 相对上一次，X 轴方向移动的坐标 | | deltaY | 相对上一次，Y 轴方向移动的坐标 | | velocityX | 手指离开屏幕时的横向速度（pixel per second) | | velocityY | 手指离开屏幕时的纵向速度（pixel per second) | | | | | |
|  | worklet:should-response-on-move | callback |  | 否 | 手指移动过程中手势是否响应 |
|  | worklet:should-accept-gesture | callback |  | 否 | 手势是否应该被识别 |
|  | simultaneous-handlers | Array.<string> |  | 否 | 声明可同时触发的手势节点 |
|  | native-view | string |  | 否 | 代理的原生节点类型 |

**通用属性**

| eventhandler 回调参数 | 说明 |
| --- | --- |
| state | 手势状态 |
| absoluteX | 相对于全局的 X 坐标 |
| absoluteY | 相对于全局的 Y 坐标 |
| deltaX | 相对上一次，X 轴方向移动的坐标 |
| deltaY | 相对上一次，Y 轴方向移动的坐标 |
| velocityX | 手指离开屏幕时的横向速度（pixel per second) |
| velocityY | 手指离开屏幕时的纵向速度（pixel per second) |

---

### scale-gesture-handler

相关文档:手势系统

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/scale-gesture-handler.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | tag | string |  | 否 | 声明手势协商时的组件标识 |
|  | worklet:ongesture | eventhandler |  | 否 | 手势识别成功的回调 |
|  | | eventhandler 回调参数 | 说明 | | --- | --- | | state | 手势状态 | | focalX | 中心点相对于全局的X坐标 | | focalY | 中心点相对于全局的Y坐标 | | focalDeltaX | 相对上一次，中心点在X轴方向移动的坐标 | | focalDeltaY | 相对上一次，中心点在Y轴方向移动的坐标 | | scale | 放大或缩小的比例 | | horizontalScale | scale的横向分量 | | verticalScale | scale的纵向分量 | | rotation | 旋转角（单位：弧度） | | velocityX | 手指离开屏幕时的横向速度（pixel per second) | | velocityY | 手指离开屏幕时的纵向速度（pixel per second) | | pointerCount | 跟踪的手指数 | | | | | |
|  | worklet:should-response-on-move | callback |  | 否 | 手指移动过程中手势是否响应 |
|  | worklet:should-accept-gesture | callback |  | 否 | 手势是否应该被识别 |
|  | simultaneous-handlers | Array.<string> |  | 否 | 声明可同时触发的手势节点 |
|  | native-view | string |  | 否 | 代理的原生节点类型 |

**通用属性**

| eventhandler 回调参数 | 说明 |
| --- | --- |
| state | 手势状态 |
| focalX | 中心点相对于全局的X坐标 |
| focalY | 中心点相对于全局的Y坐标 |
| focalDeltaX | 相对上一次，中心点在X轴方向移动的坐标 |
| focalDeltaY | 相对上一次，中心点在Y轴方向移动的坐标 |
| scale | 放大或缩小的比例 |
| horizontalScale | scale的横向分量 |
| verticalScale | scale的纵向分量 |
| rotation | 旋转角（单位：弧度） |
| velocityX | 手指离开屏幕时的横向速度（pixel per second) |
| velocityY | 手指离开屏幕时的纵向速度（pixel per second) |
| pointerCount | 跟踪的手指数 |

---

### tap-gesture-handler

相关文档:手势系统

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/tap-gesture-handler.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | tag | string |  | 否 | 声明手势协商时的组件标识 |
|  | worklet:ongesture | eventhandler |  | 否 | 手势识别成功的回调 |
|  | | eventhandler 回调参数 | 说明 | | --- | --- | | state | 手势状态 | | absoluteX | 相对于全局的 X 坐标 | | absoluteY | 相对于全局的 Y 坐标 | | | | | |
|  | worklet:should-response-on-move | callback |  | 否 | 手指移动过程中手势是否响应 |
|  | worklet:should-accept-gesture | callback |  | 否 | 手势是否应该被识别 |
|  | simultaneous-handlers | Array.<string> |  | 否 | 声明可同时触发的手势节点 |
|  | native-view | string |  | 否 | 代理的原生节点类型 |

**通用属性**

| eventhandler 回调参数 | 说明 |
| --- | --- |
| state | 手势状态 |
| absoluteX | 相对于全局的 X 坐标 |
| absoluteY | 相对于全局的 Y 坐标 |

---

### vertical-drag-gesture-handler

相关文档:手势系统

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/vertical-drag-gesture-handler.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | tag | string |  | 否 | 声明手势协商时的组件标识 |
|  | worklet:ongesture | eventhandler |  | 否 | 手势识别成功的回调 |
|  | | eventhandler 回调参数 | 说明 | | --- | --- | | state | 手势状态 | | absoluteX | 相对于全局的 X 坐标 | | absoluteY | 相对于全局的 Y 坐标 | | deltaX | 相对上一次，X 轴方向移动的坐标 | | deltaY | 相对上一次，Y 轴方向移动的坐标 | | velocityX | 手指离开屏幕时的横向速度（pixel per second) | | velocityY | 手指离开屏幕时的纵向速度（pixel per second) | | | | | |
|  | worklet:should-response-on-move | callback |  | 否 | 手指移动过程中手势是否响应 |
|  | worklet:should-accept-gesture | callback |  | 否 | 手势是否应该被识别 |
|  | simultaneous-handlers | Array.<string> |  | 否 | 声明可同时触发的手势节点 |
|  | native-view | string |  | 否 | 代理的原生节点类型 |

**通用属性**

| eventhandler 回调参数 | 说明 |
| --- | --- |
| state | 手势状态 |
| absoluteX | 相对于全局的 X 坐标 |
| absoluteY | 相对于全局的 Y 坐标 |
| deltaX | 相对上一次，X 轴方向移动的坐标 |
| deltaY | 相对上一次，Y 轴方向移动的坐标 |
| velocityX | 手指离开屏幕时的横向速度（pixel per second) |
| velocityY | 手指离开屏幕时的纵向速度（pixel per second) |

---

### draggable-sheet

基础库 3.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/draggable-sheet.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| initial-child-size | number | 0.5 | 否 | 初始时占父容器的比例 | [3.2.0](../framework/compatibility.html) |
| min-child-size | number | 0.25 | 否 | 最小时占父容器的比例 | [3.2.0](../framework/compatibility.html) |
| max-child-size | number | 1.0 | 否 | 最大时占父容器的比例 | [3.2.0](../framework/compatibility.html) |
| snap | boolean | false | 否 | 拖拽后是否自动对齐关键点 | [3.2.0](../framework/compatibility.html) |
| snap-sizes | Array.<number> | [] | 否 | 拖拽后对齐的关键点，无需包含最小和最大值 | [3.2.0](../framework/compatibility.html) |
| worklet:onsizeupdate | worklet |  | 否 | 尺寸发生变化时触发，仅支持 worklet 作为回调。event = {pixels, size} | [3.2.0](../framework/compatibility.html) |

---

### grid-builder

基础库 3.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/grid-builder.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | padding | Array | [0, 0, 0, 0] | 否 | 长度为 4 的数组，按 top、right、bottom、left 顺序指定内边距 |
|  | list | Array |  | 是 | 需要用于渲染的列表 |
|  | child-count | Array |  | 否 | 完整列表的长度，如果不传则取 list 的长度作为其值 |
|  | type | string | aligned | 是 | 布局方式 |
|  | | 合法值 | 说明 | | --- | --- | | aligned | 每行高度由同一行中最大高度子节点决定 | | masonry | 瀑布流，根据子元素高度自动布局 | | | | | |
|  | cross-axis-count | number | 2 | 否 | 交叉轴元素数量 |
|  | max-cross-axis-extent | number | 0 | 否 | 交叉轴元素最大范围 |
|  | main-axis-gap | number | 0 | 否 | 主轴方向间隔 |
|  | cross-axis-gap | number | 0 | 否 | 交叉轴方向间隔 |
|  | binditembuild | eventhandle |  | 否 | 列表项创建时触发，event.detail = {index}，index 即被创建的列表项序号 |
|  | binditemdispose | eventhandle |  | 否 | 列表项回收时触发，event.detail = {index}，index 即被回收的列表项序号 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| aligned | 每行高度由同一行中最大高度子节点决定 |
| masonry | 瀑布流，根据子元素高度自动布局 |

---

### grid-view

基础库 2.29.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/grid-view.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | type | string | aligned | 是 | 布局方式 |  |
|  | | 合法值 | 说明 | | --- | --- | | aligned | 每行高度由同一行中最大高度子节点决定 | | masonry | 瀑布流，根据子元素高度自动布局 | | | | | | |
|  | cross-axis-count | number | 2 | 否 | 交叉轴元素数量 |  |
|  | max-cross-axis-extent | number | 0 | 否 | 交叉轴元素最大范围 |  |
|  | main-axis-gap | number | 0 | 否 | 主轴方向间隔 |  |
|  | cross-axis-gap | number | 0 | 否 | 交叉轴方向间隔 |  |
|  | padding | Array | [0, 0, 0, 0] | 否 | 长度为 4 的数组，按 top、right、bottom、left 顺序指定内边距 | [3.0.0](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| aligned | 每行高度由同一行中最大高度子节点决定 |
| masonry | 瀑布流，根据子元素高度自动布局 |

---

### list-builder

基础库 3.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/list-builder.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | padding | Array | [0, 0, 0, 0] | 否 | 长度为 4 的数组，按 top、right、bottom、left 顺序指定内边距 |  |
|  | type | string | static | 是 | 类型，默认为定高模式 |  |
|  | | 合法值 | 说明 | | --- | --- | | static | 定高模式，所有列表项等高，需要传入 child-height | | dynamic | 不定高模式 | | | | | | |
|  | list | Array |  | 是 | 需要用于渲染的列表 |  |
|  | child-count | Array |  | 否 | 完整列表的长度，如果不传则取 list 的长度作为其值 |  |
|  | child-height | Array |  | 否 | 列表项的高度，当 type 为 static 时必须传入 |  |
|  | binditembuild | eventhandle |  | 否 | 列表项创建时触发，event.detail = {index}，index 即被创建的列表项序号 |  |
|  | binditemdispose | eventhandle |  | 否 | 列表项回收时触发，event.detail = {index}，index 即被回收的列表项序号 |  |
|  | initial-child-count | number | 0 | 否 | 首次渲染时渲染的列表项数量，用于减少首次渲染时的白屏时长。不传则首屏也根据布局结果按需渲染 | [3.7.12](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| static | 定高模式，所有列表项等高，需要传入 child-height |
| dynamic | 不定高模式 |

---

### list-view

基础库 2.29.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/list-view.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| padding | Array | [0, 0, 0, 0] | 否 | 长度为 4 的数组，按 top、right、bottom、left 顺序指定内边距 | [3.0.0](../framework/compatibility.html) |

---

### nested-scroll-body

基础库 3.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/nested-scroll-body.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| offset-top | number | 0 | 否 | 滚动目标距离顶部的距离(px)。在外层 scroll-view 滚动时此组件会在主轴方向会逐渐撑开，直到此组件顶部与视窗顶部距离为该属性值时才开始里层 scroll-view 的滚动。默认为 0，即表示此组件撑开到顶部与视窗顶部齐平时才开始里层 scroll-view 的滚动。 | [3.6.2](../framework/compatibility.html) |

---

### nested-scroll-header

基础库 3.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/nested-scroll-header.html

---

### open-container

基础库 3.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/open-container.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | closed-color | string | white | 是 | 初始容器背景色 |
|  | closed-elevation | number | 0 | 是 | 初始容器影深大小 |
|  | closed-border-radius | number | 0 | 是 | 初始容器圆角大小 |
|  | middle-color | string | '' | 是 | `fadeThrough` 模式下的过渡背景色 |
|  | open-color | string | white | 是 | 打开状态下容器背景色 |
|  | open-elevation | number | 0 | 是 | 打开状态下容器影深大小 |
|  | open-border-radius | number | 0 | 是 | 打开状态下容器圆角大小 |
|  | transition-duration | number | 300 | 是 | 动画时长 |
|  | transition-type | string | fade | 是 | 动画类型 |
|  | | 合法值 | 说明 | | --- | --- | | fade | 将传入元素淡入传出元素之上 | | fadeThrough | 首先淡出传出元素，并在传出元素完全淡出后开始淡入传入元素 | | | | | |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| fade | 将传入元素淡入传出元素之上 |
| fadeThrough | 首先淡出传出元素，并在传出元素完全淡出后开始淡入传入元素 |

---

### open-data-item

基础库 3.7.8 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/open-data-item.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | type | string |  | 是 | 开放数据类型 |
|  | | 合法值 | 说明 | | --- | --- | | userNickName | 用户昵称 | | userAvatar | 用户头像 | | | | | |
|  | index | number |  | 是 | 序号 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| userNickName | 用户昵称 |
| userAvatar | 用户头像 |

---

### open-data-list

基础库 3.7.8 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/open-data-list.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | type | string |  | 是 | 开放数据类型 |
|  | | 合法值 | 说明 | | --- | --- | | groupMembers | 群成员信息 | | | | | |
|  | members | Array.<string> |  | 否 | 群成员group\_openid列表 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| groupMembers | 群成员信息 |

---

### share-element

基础库 2.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/share-element.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | key | string |  | 是 | 映射标记，页面内唯一 | [2.29.2](../framework/compatibility.html) |
|  | transform | boolean | false | 否 | 是否进行动画 | [2.16.0](../framework/compatibility.html) |
|  | duration | number | 300 | 否 | 动画时长，单位毫秒 | [2.16.0](../framework/compatibility.html) |
|  | easing-function | string | ease-out | 否 | `css`缓动函数 | [2.16.0](../framework/compatibility.html) |

**Skyline 特有属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | transition-on-gesture | boolean | false | 否 | 手势返回时是否进行动画 | [2.29.2](../framework/compatibility.html) |
|  | shuttle-on-push | string | to | 否 | 指定 push 阶段的飞跃物 | [2.30.2](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | from | push 阶段采用源页面节点作为飞跃物 | | to | push 阶段采用目标页面节点作为飞跃物 | | from | pop 阶段采用源页面节点作为飞跃物 | | to | pop 阶段采用目标页面节点作为飞跃物 | | | | | | |
|  | shuttle-on-pop | string | to | 否 | 指定 pop 阶段的飞跃物 | [2.30.2](../framework/compatibility.html) |
|  | worklet:onframe | callback |  | 否 | 动画帧回调 | [2.30.2](../framework/compatibility.html) |
|  | rect-tween-type | string | materialRectArc | 否 | 动画插值曲线 | [2.30.2](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | materialRectArc | 矩形对角动画 | | materialRectCenterArc | 径向动画 | | linear |  | | elasticIn |  | | elasticOut |  | | elasticInOut |  | | bounceIn |  | | bounceOut |  | | bounceInOut |  | | cubic-bezier(x1, y1, x2, y2 | ) | | | | | | |

**Skyline 特有属性**

| 合法值 | 说明 |
| --- | --- |
| from | push 阶段采用源页面节点作为飞跃物 |
| to | push 阶段采用目标页面节点作为飞跃物 |
| from | pop 阶段采用源页面节点作为飞跃物 |
| to | pop 阶段采用目标页面节点作为飞跃物 |

**Skyline 特有属性**

| 合法值 | 说明 |
| --- | --- |
| materialRectArc | 矩形对角动画 |
| materialRectCenterArc | 径向动画 |
| linear |  |
| elasticIn |  |
| elasticOut |  |
| elasticInOut |  |
| bounceIn |  |
| bounceOut |  |
| bounceInOut |  |
| cubic-bezier(x1, y1, x2, y2 | ) |

---

### snapshot

基础库 3.0.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/snapshot.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | mode | string | view | 是 | 渲染模式 |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | view | 以真实节点渲染。 | [3.1.0](../framework/compatibility.html) | | picture | 对子节点生成的内容截图渲染。 | [3.1.0](../framework/compatibility.html) | | | | | |

**通用属性**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| view | 以真实节点渲染。 | [3.1.0](../framework/compatibility.html) |
| picture | 对子节点生成的内容截图渲染。 | [3.1.0](../framework/compatibility.html) |

---

### span

渲染框架支持情况：Skyline （使用最新Nightly工具调试）

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/span.html

---

### sticky-header

基础库 2.29.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/sticky-header.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| offset-top | number | 0 | 否 | 吸顶时与视窗顶部的距离(px) | [3.0.0](../framework/compatibility.html) |
| allow-overlapping | bool | false | 否 | 是否允许与前一个 sticky-header 重叠 | [3.7.11](../framework/compatibility.html) |
| padding | Array | [0, 0, 0, 0] | 否 | 长度为 4 的数组，按 top、right、bottom、left 顺序指定内边距(px) | [3.0.0](../framework/compatibility.html) |
| bind:stickontopchange | eventhandle |  | 否 | 吸顶状态变化事件，仅支持非 worklet 的组件方法作为回调。event.detail = { isStickOnTop }，当 sticky-header 吸顶时为 true，否则为 false。 | [3.6.2](../framework/compatibility.html) |

---

### sticky-section

基础库 2.29.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/sticky-section.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| push-pinned-header | boolean | true | 否 | 吸顶元素重叠时是否继续上推 |  |
| padding | Array | [0, 0, 0, 0] | 否 | 长度为 4 的数组，按 top、right、bottom、left 顺序指定内边距 | [3.0.0](../framework/compatibility.html) |

---

### functional-page-navigator

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/functional-page-navigator.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | version | string | release | 否 | 跳转到的小程序版本，\*\*线上版本必须设置为 release\*\* | [2.1.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | develop | 开发版 | | trial | 体验版 | | release | 正式版 | | | | | | |
|  | name | string |  | 否 | 要跳转到的功能页 | [2.1.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | loginAndGetUserInfo | [用户信息功能页](../framework/plugin/functional-pages/user-info.html) | [2.1.0](../framework/compatibility.html) | | requestPayment | [支付功能页](../framework/plugin/functional-pages/request-payment.html) | [2.1.0](../framework/compatibility.html) | | chooseAddress | [收货地址功能页](../framework/plugin/functional-pages/choose-address.html) | [2.4.0](../framework/compatibility.html) | | chooseInvoice | [获取发票功能页](../framework/plugin/functional-pages/choose-invoice.html) | [2.14.1](../framework/compatibility.html) | | chooseInvoiceTitle | [获取发票抬头功能页](../framework/plugin/functional-pages/choose-invoice-title.html) | [2.14.1](../framework/compatibility.html) | | | | | | |
|  | args | object |  | 否 | 功能页参数，参数格式与具体功能页相关 | [2.1.0](../framework/compatibility.html) |
|  | bindsuccess | eventhandler |  | 否 | 功能页返回，且操作成功时触发， detail 格式与具体功能页相关 | [2.1.0](../framework/compatibility.html) |
|  | bindfail | eventhandler |  | 否 | 功能页返回，且操作失败时触发， detail 格式与具体功能页相关 | [2.1.0](../framework/compatibility.html) |
|  | bindcancel | eventhandler |  | 否 | 因用户操作从功能页返回时触发 | [2.4.1](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| develop | 开发版 |
| trial | 体验版 |
| release | 正式版 |

**通用属性**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| loginAndGetUserInfo | [用户信息功能页](../framework/plugin/functional-pages/user-info.html) | [2.1.0](../framework/compatibility.html) |
| requestPayment | [支付功能页](../framework/plugin/functional-pages/request-payment.html) | [2.1.0](../framework/compatibility.html) |
| chooseAddress | [收货地址功能页](../framework/plugin/functional-pages/choose-address.html) | [2.4.0](../framework/compatibility.html) |
| chooseInvoice | [获取发票功能页](../framework/plugin/functional-pages/choose-invoice.html) | [2.14.1](../framework/compatibility.html) |
| chooseInvoiceTitle | [获取发票抬头功能页](../framework/plugin/functional-pages/choose-invoice-title.html) | [2.14.1](../framework/compatibility.html) |

---

### navigator

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/navigator.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | target | string | self | 否 | 在哪个目标上发生跳转，默认当前小程序 | [2.0.7](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | self | 当前小程序 | | miniProgram | 其它小程序 | | | | | | |
|  | url | string |  | 否 | 当前小程序内的跳转链接 | [1.0.0](../framework/compatibility.html) |
|  | open-type | string | navigate | 否 | 跳转方式 | [1.0.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | navigate | 对应 [wx.navigateTo](../api/route/wx.navigateTo.html) 或 [wx.navigateToMiniProgram](../api/navigate/wx.navigateToMiniProgram.html) 的功能 |  | | redirect | 对应 [wx.redirectTo](../api/route/wx.redirectTo.html) 的功能 |  | | switchTab | 对应 [wx.switchTab](../api/route/wx.switchTab.html) 的功能 |  | | reLaunch | 对应 [wx.reLaunch](../api/route/wx.reLaunch.html) 的功能 | [1.1.0](../framework/compatibility.html) | | navigateBack | 对应 [wx.navigateBack](../api/route/wx.navigateBack.html) 或 [wx.navigateBackMiniProgram](../api/navigate/wx.navigateBackMiniProgram.html) （基础库 2.24.4 版本支持）的功能 | [1.1.0](../framework/compatibility.html) | | exit | 退出小程序，`target="miniProgram"`时生效 | [2.1.0](../framework/compatibility.html) | | | | | | |
|  | delta | number | 1 | 否 | 当 open-type 为 'navigateBack' 时有效，表示回退的层数 | [1.0.0](../framework/compatibility.html) |
|  | app-id | string |  | 否 | 当`target="miniProgram"`且`open-type="navigate"`时有效，要打开的小程序 appId | [2.0.7](../framework/compatibility.html) |
|  | path | string |  | 否 | 当`target="miniProgram"`且`open-type="navigate"`时有效，打开的页面路径，如果为空则打开首页 | [2.0.7](../framework/compatibility.html) |
|  | extra-data | object |  | 否 | 当`target="miniProgram"`且`open-type="navigate/navigateBack"`时有效，需要传递给目标小程序的数据，目标小程序可在 `App.onLaunch()`，`App.onShow()` 中获取到这份数据。[详情](../framework/app-service/app.html) | [2.0.7](../framework/compatibility.html) |
|  | version | string | release | 否 | 当`target="miniProgram"`且`open-type="navigate"`时有效，要打开的小程序版本 | [2.0.7](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | develop | 开发版 | | trial | 体验版 | | release | 正式版，仅在当前小程序为开发版或体验版时此参数有效；如果当前小程序是正式版，则打开的小程序必定是正式版。 | | | | | | |
|  | short-link | string |  | 否 | 当`target="miniProgram"`时有效，当传递该参数后，可以不传 app-id 和 path。链接可以通过【小程序菜单】->【复制链接】获取。 | [2.18.1](../framework/compatibility.html) |
|  | hover-class | string | navigator-hover | 否 | 指定点击时的样式类，当`hover-class="none"`时，没有点击态效果 | [1.0.0](../framework/compatibility.html) |
|  | hover-stop-propagation | boolean | false | 否 | 指定是否阻止本节点的祖先节点出现点击态 | [1.5.0](../framework/compatibility.html) |
|  | hover-start-time | number | 50 | 否 | 按住后多久出现点击态，单位毫秒 | [1.0.0](../framework/compatibility.html) |
|  | hover-stay-time | number | 600 | 否 | 手指松开后点击态保留时间，单位毫秒 | [1.0.0](../framework/compatibility.html) |
|  | bindsuccess | string |  | 否 | 当`target="miniProgram"`且`open-type="navigate/navigateBack"`时有效时有效，跳转小程序成功 | [2.0.7](../framework/compatibility.html) |
|  | bindfail | string |  | 否 | 当`target="miniProgram"`且`open-type="navigate/navigateBack"`时有效时有效，跳转小程序失败 | [2.0.7](../framework/compatibility.html) |
|  | bindcomplete | string |  | 否 | 当`target="miniProgram"`且`open-type="navigate/navigateBack"`时有效时有效，跳转小程序完成 | [2.0.7](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| self | 当前小程序 |
| miniProgram | 其它小程序 |

**通用属性**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| navigate | 对应 [wx.navigateTo](../api/route/wx.navigateTo.html) 或 [wx.navigateToMiniProgram](../api/navigate/wx.navigateToMiniProgram.html) 的功能 |  |
| redirect | 对应 [wx.redirectTo](../api/route/wx.redirectTo.html) 的功能 |  |
| switchTab | 对应 [wx.switchTab](../api/route/wx.switchTab.html) 的功能 |  |
| reLaunch | 对应 [wx.reLaunch](../api/route/wx.reLaunch.html) 的功能 | [1.1.0](../framework/compatibility.html) |
| navigateBack | 对应 [wx.navigateBack](../api/route/wx.navigateBack.html) 或 [wx.navigateBackMiniProgram](../api/navigate/wx.navigateBackMiniProgram.html) （基础库 2.24.4 版本支持）的功能 | [1.1.0](../framework/compatibility.html) |
| exit | 退出小程序，`target="miniProgram"`时生效 | [2.1.0](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| develop | 开发版 |
| trial | 体验版 |
| release | 正式版，仅在当前小程序为开发版或体验版时此参数有效；如果当前小程序是正式版，则打开的小程序必定是正式版。 |

---

### audio

从基础库1.6.0开始，本接口停止维护，请使用wx.createInnerAudioContext代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/audio.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| id | string |  | 否 | audio 组件的唯一标识符 | [1.0.0](../framework/compatibility.html) |
| src | string |  | 否 | 要播放音频的资源地址 | [1.0.0](../framework/compatibility.html) |
| loop | boolean | false | 否 | 是否循环播放 | [1.0.0](../framework/compatibility.html) |
| controls | boolean | false | 否 | 是否显示默认控件 | [1.0.0](../framework/compatibility.html) |
| poster | string |  | 否 | 默认控件上的音频封面的图片资源地址，如果 controls 属性值为 false 则设置 poster 无效 | [1.0.0](../framework/compatibility.html) |
| name | string | 未知音频 | 否 | 默认控件上的音频名字，如果 controls 属性值为 false 则设置 name 无效 | [1.0.0](../framework/compatibility.html) |
| author | string | 未知作者 | 否 | 默认控件上的作者名字，如果 controls 属性值为 false 则设置 author 无效 | [1.0.0](../framework/compatibility.html) |
| binderror | eventhandle |  | 否 | 当发生错误时触发 error 事件，detail = {errMsg:MediaError.code} | [1.0.0](../framework/compatibility.html) |
| bindplay | eventhandle |  | 否 | 当开始/继续播放时触发play事件 | [1.0.0](../framework/compatibility.html) |
| bindpause | eventhandle |  | 否 | 当暂停播放时触发 pause 事件 | [1.0.0](../framework/compatibility.html) |
| bindtimeupdate | eventhandle |  | 否 | 当播放进度改变时触发 timeupdate 事件，detail = {currentTime, duration} | [1.0.0](../framework/compatibility.html) |
| bindended | eventhandle |  | 否 | 当播放到末尾时触发 ended 事件 | [1.0.0](../framework/compatibility.html) |

**MediaError.code**

| 返回错误码 | 描述 |
| --- | --- |
| 1 | 获取资源被用户禁止 |
| 2 | 网络错误 |
| 3 | 解码错误 |
| 4 | 不合适资源 |

---

### camera

基础库 1.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/camera.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | mode | string | normal | 否 | 应用模式，只在初始化时有效，不能动态变更 | [2.1.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | normal | 相机模式 | | scanCode | 扫码模式 | | | | | | |
|  | resolution | string | medium | 否 | 分辨率，不支持动态修改 | [2.10.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | low | 低 | | medium | 中 | | high | 高 | | | | | | |
|  | device-position | string | back | 否 | 摄像头朝向 | [1.0.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | front | 前置 | | back | 后置 | | | | | | |
|  | flash | string | auto | 否 | 闪光灯，值为auto, on, off | [1.0.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | auto | 自动 |  | | on | 打开 |  | | off | 关闭 |  | | torch | 常亮 | [2.8.0](../framework/compatibility.html) | | | | | | |
|  | frame-size | string | medium | 否 | 指定期望的相机帧数据尺寸 | [2.7.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | small | 小尺寸帧数据 | | medium | 中尺寸帧数据 | | large | 大尺寸帧数据 | | | | | | |
|  | bindstop | eventhandle |  | 否 | 摄像头在非正常终止时触发，如退出后台等情况 | [1.0.0](../framework/compatibility.html) |
|  | binderror | eventhandle |  | 否 | 用户不允许使用摄像头时触发 | [1.0.0](../framework/compatibility.html) |
|  | bindinitdone | eventhandle |  | 否 | 相机初始化完成时触发，`e.detail = {maxZoom}` | [2.7.0](../framework/compatibility.html) |
|  | bindscancode | eventhandle |  | 否 | 在扫码识别成功时触发，仅在 mode="scanCode" 时生效 | [2.1.0](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| normal | 相机模式 |
| scanCode | 扫码模式 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| low | 低 |
| medium | 中 |
| high | 高 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| front | 前置 |
| back | 后置 |

**通用属性**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| auto | 自动 |  |
| on | 打开 |  |
| off | 关闭 |  |
| torch | 常亮 | [2.8.0](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| small | 小尺寸帧数据 |
| medium | 中尺寸帧数据 |
| large | 大尺寸帧数据 |

---

### channel-live

基础库 2.29.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/channel-live.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| feed-id | string |  | 是 | 视频 feedId |
| finder-user-name | string |  | 是 | 视频号 id，以“sph”开头的id，可在视频号助手获取。视频号必须与当前小程序相同主体。 |

---

### channel-video

基础库 2.25.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/channel-video.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | feed-id | string |  | 是 | 仅视频号视频与小程序同主体时生效。若内嵌非同主体视频，请使用 feed-token。 |  |
|  | finder-user-name | string |  | 是 | 视频号 id，以“sph”开头的id，可在视频号助手获取。视频号必须与当前小程序相同主体。 |  |
|  | feed-token | string |  | 是 | 仅内嵌小程序非同主体视频号视频时使用，获取方式参考[本指引](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/channels-activity#feed-token)。 | [2.31.1](../framework/compatibility.html) |
|  | autoplay | string |  | 是 | 是否自动播放。仅视频号视频与小程序同主体时支持设置为 true。 | [2.31.1](../framework/compatibility.html) |
|  | loop | boolean | false | 否 | 是否循环播放 |  |
|  | muted | boolean | false | 否 | 是否静音播放 |  |
|  | object-fit | boolean | contain | 否 | 当视频大小与 video 容器大小不一致时，视频的表现形式 |  |
|  | | 合法值 | 说明 | | --- | --- | | contain | 包含 | | fill | 填充 | | cover | 覆盖 | | | | | | |
|  | binderror | eventhandle |  | 否 | 视频播放出错时触发 |  |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| contain | 包含 |
| fill | 填充 |
| cover | 覆盖 |

---

### image

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/image.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | src | string |  | 否 | 图片资源地址 | [1.0.0](../framework/compatibility.html) |
|  | mode | string | scaleToFill | 否 | 图片裁剪、缩放的模式 | [1.0.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | scaleToFill | 缩放模式，不保持纵横比缩放图片，使图片的宽高完全拉伸至填满 image 元素 |  | | aspectFit | 缩放模式，保持纵横比缩放图片，使图片的长边能完全显示出来。也就是说，可以完整地将图片显示出来。 |  | | aspectFill | 缩放模式，保持纵横比缩放图片，只保证图片的短边能完全显示出来。也就是说，图片通常只在水平或垂直方向是完整的，另一个方向将会发生截取。 |  | | widthFix | 缩放模式，宽度不变，高度自动变化，保持原图宽高比不变 |  | | heightFix | 缩放模式，高度不变，宽度自动变化，保持原图宽高比不变 | [2.10.3](../framework/compatibility.html) | | top | 裁剪模式，不缩放图片，只显示图片的顶部区域。仅 Webview 支持。 |  | | bottom | 裁剪模式，不缩放图片，只显示图片的底部区域。仅 Webview 支持。 |  | | center | 裁剪模式，不缩放图片，只显示图片的中间区域。仅 Webview 支持。 |  | | left | 裁剪模式，不缩放图片，只显示图片的左边区域。仅 Webview 支持。 |  | | right | 裁剪模式，不缩放图片，只显示图片的右边区域。仅 Webview 支持。 |  | | top left | 裁剪模式，不缩放图片，只显示图片的左上边区域。仅 Webview 支持。 |  | | top right | 裁剪模式，不缩放图片，只显示图片的右上边区域。仅 Webview 支持。 |  | | bottom left | 裁剪模式，不缩放图片，只显示图片的左下边区域。仅 Webview 支持。 |  | | bottom right | 裁剪模式，不缩放图片，只显示图片的右下边区域。仅 Webview 支持。 |  | | | | | | |
|  | show-menu-by-longpress | boolean | false | 否 | 长按图片显示发送给朋友、收藏、保存图片、搜一搜、打开名片/前往群聊/打开小程序（若图片中包含对应二维码或小程序码）的菜单。 | [2.7.0](../framework/compatibility.html) |
|  | binderror | eventhandle |  | 否 | 当错误发生时触发，event.detail = {errMsg} | [1.0.0](../framework/compatibility.html) |
|  | bindload | eventhandle |  | 否 | 当图片载入完毕时触发，event.detail = {height, width} | [1.0.0](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| scaleToFill | 缩放模式，不保持纵横比缩放图片，使图片的宽高完全拉伸至填满 image 元素 |  |
| aspectFit | 缩放模式，保持纵横比缩放图片，使图片的长边能完全显示出来。也就是说，可以完整地将图片显示出来。 |  |
| aspectFill | 缩放模式，保持纵横比缩放图片，只保证图片的短边能完全显示出来。也就是说，图片通常只在水平或垂直方向是完整的，另一个方向将会发生截取。 |  |
| widthFix | 缩放模式，宽度不变，高度自动变化，保持原图宽高比不变 |  |
| heightFix | 缩放模式，高度不变，宽度自动变化，保持原图宽高比不变 | [2.10.3](../framework/compatibility.html) |
| top | 裁剪模式，不缩放图片，只显示图片的顶部区域。仅 Webview 支持。 |  |
| bottom | 裁剪模式，不缩放图片，只显示图片的底部区域。仅 Webview 支持。 |  |
| center | 裁剪模式，不缩放图片，只显示图片的中间区域。仅 Webview 支持。 |  |
| left | 裁剪模式，不缩放图片，只显示图片的左边区域。仅 Webview 支持。 |  |
| right | 裁剪模式，不缩放图片，只显示图片的右边区域。仅 Webview 支持。 |  |
| top left | 裁剪模式，不缩放图片，只显示图片的左上边区域。仅 Webview 支持。 |  |
| top right | 裁剪模式，不缩放图片，只显示图片的右上边区域。仅 Webview 支持。 |  |
| bottom left | 裁剪模式，不缩放图片，只显示图片的左下边区域。仅 Webview 支持。 |  |
| bottom right | 裁剪模式，不缩放图片，只显示图片的右下边区域。仅 Webview 支持。 |  |

**Skyline 特有属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | fade-in | boolean | false | 否 | 是否渐显 |  |
|  | preload | boolean | false | 否 | 是否预加载图片，即设置图片 src 时就触发图片下载和解码 | [3.15.0](../framework/compatibility.html) |

**WebView 特有属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | webp | boolean | false | 否 | 默认不解析 webP 格式，只支持网络资源 | [2.9.0](../framework/compatibility.html) |
|  | lazy-load | boolean | false | 否 | 图片懒加载，在即将进入一定范围（上下三屏）时才开始加载。Skyline 默认懒加载。 | [1.5.0](../framework/compatibility.html) |
|  | forceHttps | boolean | false | 否 | 自动将 http 链接替换为 https 链接 | [3.9.1](../framework/compatibility.html) |

**支持长按识别的码**

| 类型 | 说明 | 最低版本 |
| --- | --- | --- |
| 小程序码 |  |  |
| 微信个人码 |  | [2.18.0](../framework/compatibility.html) |
| 企业微信个人码 |  | [2.18.0](../framework/compatibility.html) |
| 普通群码 | 指仅包含微信用户的群 | [2.18.0](../framework/compatibility.html) |
| 互通群码 | 指既有微信用户也有企业微信用户的群 | [2.18.0](../framework/compatibility.html) |
| 公众号二维码 |  | [2.18.0](../framework/compatibility.html) |

---

### live-player

基础库 1.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/live-player.html

**申请开通**

| 一级类目/主体类型 | 二级类目 | 小程序内容场景 |
| --- | --- | --- |
| 社交 | 直播 | 涉及非表演类在线直播（如电商类、教育类等）等。选择该类目后首次提交代码审核，需经当地互联网主管机关审核确认，预计审核时长 7 天左右 |
| 社交 | 直播表演 | 适用于提供表演类在线直播（如游戏直播、娱乐秀场类、线上演唱会、剧目直播、演艺直播等）。选择该类目后首次提交代码审核，需经当地互联网主管机关审核确认，预计审核时长 7 天左右 |
| 教育 | 在线视频课程 | 网课、在线培训、讲座等教育类直播 |
| 医疗 | 互联网医院，公立医疗机构，三级私立医疗机构，其他私立医疗机构 | 问诊、大型健康讲座等直播 |
| 金融 | 银行、信托、公募基金、私募基金、证券/期货、证券、期货投资咨询、保险、企业征信、新三板信息服务平台、股票信息服务平台、股票信息服务平台（港股/美股）、消费金融、融资担保、汽车金融/融资租赁 | 金融产品视频客服理赔、金融产品推广直播等 |
| 汽车 | 汽车预售 | 汽车预售、推广直播 |
| 政府主体账号 | / | 政府相关工作推广直播、领导讲话直播等 |
| IT科技 | 多方通信；音视频设备 | 为多方提供电话会议/视频会议等服务；智能家居场景下控制摄像头 |
| 房地产服务 | 房地产营销 | 房地产营销直播服务、在线音视频带看等 |
| 商业服务 | 公证 | 在线业务办理等 |
| 公共服务 | 交通运输 | 仅适用于港澳特区政府主体提供当地的交通管理相关政务服务（如道路运输、车辆管理等） |

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | src | string |  | 否 | 音视频地址。目前仅支持 `flv`, `rtmp` 格式 | [1.7.0](../framework/compatibility.html) |
|  | mode | string | live | 否 | 模式 | [1.7.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | live | 直播 | | RTC | 实时通话，该模式时延更低 | | | | | | |
|  | autoplay | boolean | false | 否 | 自动播放 | [1.7.0](../framework/compatibility.html) |
|  | muted | boolean | false | 否 | 是否静音 | [1.7.0](../framework/compatibility.html) |
|  | orientation | string | vertical | 否 | 画面方向 | [1.7.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | vertical | 竖直 | | horizontal | 水平 | | | | | | |
|  | object-fit | string | contain | 否 | 填充模式，可选值有 `contain`，`fillCrop` | [1.7.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | contain | 图像长边填满屏幕，短边区域会被填充⿊⾊ | | fillCrop | 图像铺满屏幕，超出显示区域的部分将被截掉 | | | | | | |
|  | background-mute | boolean | false | 否 | 进入后台时是否静音（已废弃，默认退后台静音） | [1.7.0](../framework/compatibility.html) |
|  | min-cache | number | 1 | 否 | 最小缓冲区，单位s（RTC 模式推荐 0.2s） | [1.7.0](../framework/compatibility.html) |
|  | max-cache | number | 3 | 否 | 最大缓冲区，单位s（RTC 模式推荐 0.8s）。缓冲区用来抵抗网络波动，缓冲数据越多，网络抗性越好，但时延越大。 | [1.7.0](../framework/compatibility.html) |
|  | sound-mode | string | speaker | 否 | 声音输出方式 | [1.9.90](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | speaker | 扬声器 | | ear | 听筒 | | | | | | |
|  | auto-pause-if-navigate | boolean | true | 否 | 当跳转到本小程序的其他页面时，是否自动暂停本页面的实时音视频播放 | [2.5.0](../framework/compatibility.html) |
|  | auto-pause-if-open-native | boolean | true | 否 | 当跳转到其它微信原生页面时，是否自动暂停本页面的实时音视频播放 | [2.5.0](../framework/compatibility.html) |
|  | picture-in-picture-mode | string/Array |  | 否 | 设置小窗模式： push, pop，空字符串或通过数组形式设置多种模式（如： ["push", "pop"]） | [2.10.3](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | [] | 取消小窗 | | push | 路由 push 时触发小窗 | | pop | 路由 pop 时触发小窗 | | | | | | |
|  | picture-in-picture-init-position | string |  | 否 | 小窗模式下小窗的初始显示位置，格式为 (alignment, y)，其中 alignment 表示小窗吸附屏幕左侧还是右侧，可选值为 left、right，y 代表小窗最顶部所在的屏幕高度百分比 | [3.3.0](../framework/compatibility.html) |
|  | enable-system-pip | boolean | true | 否 | 是否支持 iOS 系统画中画，默认支持 | [3.14.1](../framework/compatibility.html) |
|  | enable-auto-rotation | boolean | false | 否 | 是否开启手机横屏时自动全屏，当系统设置开启自动旋转时生效 | [2.11.0](../framework/compatibility.html) |
|  | referrer-policy | string | no-referrer | 否 | 格式固定为 `https://servicewechat.com/{appid}/{version}/page-frame.html`，其中 {appid} 为小程序的 appid，{version} 为小程序的版本号，版本号为 0 表示为开发版、体验版以及审核版本，版本号为 devtools 表示为开发者工具，其余为正式版本； | [2.13.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | origin | 发送完整的referrer | | no-referrer | 不发送 | | | | | | |
|  | enable-casting | boolean | false | 否 | 是否支持投屏。开启后，可以通过 [LivePlayerContext](../api/media/live/LivePlayerContext.html) 上相关方法进行操作。 | [2.32.0](../framework/compatibility.html) |
|  | mute-on-audio-conflict | boolean | false | 否 | 音频冲突时是否静音 | [3.16.2](../framework/compatibility.html) |
|  | bindstatechange | eventhandle |  | 否 | 播放状态变化事件，detail = {code} | [1.7.0](../framework/compatibility.html) |
|  | bindfullscreenchange | eventhandle |  | 否 | 全屏变化事件，detail = {direction, fullScreen} | [1.7.0](../framework/compatibility.html) |
|  | bindnetstatus | eventhandle |  | 否 | 网络状态通知，detail = {info} | [1.9.0](../framework/compatibility.html) |
|  | bindaudiovolumenotify | eventhandler |  | 否 | 播放音量大小通知，detail = {} | [2.10.0](../framework/compatibility.html) |
|  | bindenterpictureinpicture | eventhandler |  | 否 | 播放器进入小窗 | [2.11.0](../framework/compatibility.html) |
|  | bindleavepictureinpicture | eventhandler |  | 否 | 播放器退出小窗 | [2.11.0](../framework/compatibility.html) |
|  | bindcastinguserselect | eventhandler |  | 否 | 用户选择投屏设备时触发 detail = { state: "success"/"fail" } | [2.32.0](../framework/compatibility.html) |
|  | bindcastingstatechange | eventhandler |  | 否 | 投屏成功/失败时触发 detail = { type, state: "success"/"fail" } | [2.32.0](../framework/compatibility.html) |
|  | bindcastinginterrupt | eventhandler |  | 否 | 投屏被中断时触发 | [2.32.0](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| live | 直播 |
| RTC | 实时通话，该模式时延更低 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| vertical | 竖直 |
| horizontal | 水平 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| contain | 图像长边填满屏幕，短边区域会被填充⿊⾊ |
| fillCrop | 图像铺满屏幕，超出显示区域的部分将被截掉 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| speaker | 扬声器 |
| ear | 听筒 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| [] | 取消小窗 |
| push | 路由 push 时触发小窗 |
| pop | 路由 pop 时触发小窗 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| origin | 发送完整的referrer |
| no-referrer | 不发送 |

**状态码**

| 代码 | 说明 |
| --- | --- |
| 2001 | 拉流：已经连接服务器 |
| 2002 | 拉流：已经连接服务器，开始拉流 |
| 2003 | 拉流：视频首帧渲染事件 |
| 2004 | 拉流：视频播放开始 |
| 2007 | 拉流：视频播放Loading |
| 2008 | 拉流：视频解码器启动 |
| 2009 | 拉流：视频分辨率改变 |
| 2026 | 拉流：音频播放首帧事件 |
| 2030 | 音频设备发生改变，即当前的输入输出设备发生改变，比如耳机被拔出 |
| 2032 | 拉流：Audio Session 被其他 App 中断（iOS 平台特有） |
| 2033 | 拉流：渲染view窗口变化后首帧渲染事件（比如分辨率发生变化）flv，rtmp标准协议特有，如果期望监听视频首帧渲染事件，建议用2003 |
| 2034 | 拉流：接收首帧视频 |
| 2035 | 拉流：解码首帧视频 |
| 2036 | 拉流：视频时间戳发生回退 |
| 2101 | 拉流：当前视频帧解码失败 |
| 2102 | 拉流：当前音频帧解码失败 |
| 2103 | 拉流：网络连不上，自动重连事件，重连最多尝试3次，自动重连连续失败超过三次会放弃，返回-2301 |
| 2104 | 拉流：网络来包不稳：可能是下行带宽不足，或由于主播端出流不均匀 |
| 2105 | 拉流：当前视频播放出现卡顿 |
| 2106 | 拉流：硬解启动失败，采用软解 |
| 2107 | 拉流：当前视频帧不连续，可能丢帧 |
| 2108 | 拉流：当前流硬解第一个I帧失败，SDK自动切软解 |
| 3001 | 拉流：RTMP-DNS解析失败 |
| 3002 | 拉流：RTMP服务器连接失败 |
| 3003 | 拉流：RTMP服务器握手失败 |
| 3005 | 拉流：RTMP 读/写失败，之后会发起网络重试 |
| -2301 | 拉流：网络断连，且经多次重连无效，请自行重启拉流 |
| -2302 | 拉流：获取拉流地址失败 |
| 0 | 无错误 |
| 6000 | 拉流：被挂起，小程序或微信被退后台时挂起拉流 |

**网络状态数据**

| 键名 | 说明 |
| --- | --- |
| videoBitrate | 当前视频编/码器输出的比特率，单位 kbps |
| audioBitrate | 当前音频编/码器输出的比特率，单位 kbps |
| videoFPS | 当前视频帧率 |
| videoGOP | 当前视频 GOP,也就是每两个关键帧(I帧)间隔时长，单位 s |
| netSpeed | 当前的发送/接收速度 |
| netJitter | 网络抖动情况，为 0 时表示没有任何抖动，值越大表明网络抖动越大，网络越不稳定 |
| netQualityLevel | 网络质量：0：未定义 1：最好 2：好 3：一般 4：差 5：很差 6：不可用 |
| videoWidth | 视频画面的宽度 |
| videoHeight | 视频画面的高度 |
| videoCache | 缓冲的视频总时长，单位毫秒 |
| audioCache | 缓冲的音频总时长，单位毫秒 |
| vDecCacheSize | 解码器中缓存的视频帧数 (Android 端硬解码时存在） |
| vSumCacheSize | 缓冲的总视频帧数，该数值越大，播放延迟越高 |
| avPlayInterval | 音画同步错位时间（播放），单位 ms，此数值越小，音画同步越好 |
| avRecvInterval | 音画同步错位时间（网络），单位 ms，此数值越小，音画同步越好 |
| audioCacheThreshold | 音频缓冲时长阈值，缓冲超过该阈值后，播放器会开始调控延时 |

---

### live-pusher

基础库 1.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html

**申请开通**

| 一级类目/主体类型 | 二级类目 | 小程序内容场景 |
| --- | --- | --- |
| 社交 | 直播 | 涉及非表演类在线直播（如电商类、教育类等）等。选择该类目后首次提交代码审核，需经当地互联网主管机关审核确认，预计审核时长 7 天左右 |
| 社交 | 直播表演 | 适用于提供表演类在线直播（如游戏直播、娱乐秀场类、线上演唱会、剧目直播、演艺直播等）。选择该类目后首次提交代码审核，需经当地互联网主管机关审核确认，预计审核时长 7 天左右 |
| 教育 | 在线视频课程 | 网课、在线培训、讲座等教育类直播 |
| 医疗 | 互联网医院，公立医疗机构，三级私立医疗机构，其他私立医疗机构 | 问诊、大型健康讲座等直播 |
| 金融 | 银行、信托、公募基金、私募基金、证券/期货、证券、期货投资咨询、保险、企业征信、新三板信息服务平台、股票信息服务平台、股票信息服务平台（港股/美股）、消费金融、融资担保、汽车金融/融资租赁 | 金融产品视频客服理赔、金融产品推广直播等 |
| 汽车 | 汽车预售 | 汽车预售、推广直播 |
| 政府主体账号 | / | 政府相关工作推广直播、领导讲话直播等 |
| IT科技 | 多方通信；音视频设备 | 为多方提供电话会议/视频会议等服务；智能家居场景下控制摄像头 |
| 房地产服务 | 房地产营销 | 房地产营销直播服务、在线音视频带看等 |
| 商业服务 | 公证 | 在线业务办理等 |
| 公共服务 | 交通运输 | 仅适用于港澳特区政府主体提供当地的交通管理相关政务服务（如道路运输、车辆管理等） |

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | url | string |  | 否 | 推流地址。目前仅支持 `rtmp` 格式 | [1.7.0](../framework/compatibility.html) |
|  | mode | string | RTC | 否 | 模式 | [1.7.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | QVGA | Quarter VGA | [3.5.0](../framework/compatibility.html) | | HVGA | Half-size VGA | [3.5.0](../framework/compatibility.html) | | SD | 标清 | [1.7.0](../framework/compatibility.html) | | HD | 高清 | [1.7.0](../framework/compatibility.html) | | FHD | 超清 | [1.7.0](../framework/compatibility.html) | | RTC | 实时通话 | [1.7.0](../framework/compatibility.html) | | | | | | |
|  | autopush | boolean | false | 否 | 自动推流 | [1.7.0](../framework/compatibility.html) |
|  | enableVideoCustomRender | boolean | false | 否 | 自定义渲染，允许开发者自行处理所采集的视频帧，详见[LivePusherContext](../api/media/live/LivePusherContext.html) | [2.29.0](../framework/compatibility.html) |
|  | muted | boolean | false | 否 | 是否静音。即将废弃，可用 `enable-mic` 替代 | [1.7.0](../framework/compatibility.html) |
|  | enable-camera | boolean | true | 否 | 开启摄像头 | [1.7.0](../framework/compatibility.html) |
|  | auto-focus | boolean | true | 否 | 自动聚集 | [1.7.0](../framework/compatibility.html) |
|  | orientation | string | vertical | 否 | 画面方向 | [1.7.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | vertical | 竖直 | | horizontal | 水平 | | | | | | |
|  | beauty | number | 0 | 否 | 美颜，取值范围 0-9 ，0 表示关闭。鸿蒙 OS 暂不支持 | [1.7.0](../framework/compatibility.html) |
|  | whiteness | number | 0 | 否 | 美白，取值范围 0-9 ，0 表示关闭 | [1.7.0](../framework/compatibility.html) |
|  | aspect | string | 9:16 | 否 | 宽高比，可选值有 `3:4`, `9:16` | [1.7.0](../framework/compatibility.html) |
|  | min-bitrate | number | 200 | 否 | 最小码率 | [1.7.0](../framework/compatibility.html) |
|  | max-bitrate | number | 1000 | 否 | 最大码率 | [1.7.0](../framework/compatibility.html) |
|  | audio-quality | string | high | 否 | 高音质(48KHz)或低音质(16KHz)，值为`high`, `low` | [1.7.0](../framework/compatibility.html) |
|  | waiting-image | string |  | 否 | 进入后台时推流的等待画面 | [1.7.0](../framework/compatibility.html) |
|  | waiting-image-hash | string |  | 否 | 等待画面资源的MD5值 | [1.7.0](../framework/compatibility.html) |
|  | zoom | boolean | false | 否 | 调整焦距 | [2.1.0](../framework/compatibility.html) |
|  | device-position | string | front | 否 | 前置或后置，值为`front`, `back` | [2.3.0](../framework/compatibility.html) |
|  | background-mute | boolean | false | 否 | 进入后台时是否静音（已废弃，默认退后台静音） | [1.7.0](../framework/compatibility.html) |
|  | mirror | boolean | false | 否 | 设置推流画面是否镜像，产生的效果在 live-player 反应到 | [2.7.0](../framework/compatibility.html) |
|  | remote-mirror | boolean | false | 否 | 同 mirror 属性，后续 mirror 将废弃 | [2.10.0](../framework/compatibility.html) |
|  | local-mirror | string | auto | 否 | 控制本地预览画面是否镜像 | [2.10.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | auto | 前置摄像头镜像，后置摄像头不镜像 | | enable | 前后置摄像头均镜像 | | disable | 前后置摄像头均不镜像 | | | | | | |
|  | audio-reverb-type | number | 0 | 否 | 音频混响类型 | [2.10.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 关闭 | | 1 | KTV | | 2 | 小房间 | | 3 | 大会堂 | | 4 | 低沉 | | 5 | 洪亮 | | 6 | 金属声 | | 7 | 磁性 | | | | | | |
|  | enable-mic | boolean | true | 否 | 开启或关闭麦克风 | [2.10.0](../framework/compatibility.html) |
|  | enable-agc | boolean | false | 否 | 是否开启音频自动增益 | [2.10.0](../framework/compatibility.html) |
|  | enable-ans | boolean | false | 否 | 是否开启音频噪声抑制 | [2.10.0](../framework/compatibility.html) |
|  | audio-volume-type | string | auto | 否 | 音量类型 | [2.10.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | auto | 自动 | | media | 媒体音量 | | voicecall | 通话音量 | | | | | | |
|  | video-width | number | 360 | 否 | 上推的视频流的分辨率宽度 | [2.10.0](../framework/compatibility.html) |
|  | video-height | number | 640 | 否 | 上推的视频流的分辨率高度 | [2.10.0](../framework/compatibility.html) |
|  | beauty-style | string | smooth | 否 | 设置美颜类型。鸿蒙 OS 暂不支持 | [2.12.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | smooth | 光滑美颜 | | nature | 自然美颜 | | | | | | |
|  | filter | string | standard | 否 | 设置色彩滤镜 | [2.12.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | standard | 标准 | | pink | 粉嫩 | | nostalgia | 怀旧 | | blues | 蓝调 | | romantic | 浪漫 | | cool | 清凉 | | fresher | 清新 | | solor | 日系 | | aestheticism | 唯美 | | whitening | 美白 | | cerisered | 樱红 | | | | | | |
|  | picture-in-picture-mode | string/Array |  | 否 | 设置小窗模式： push, pop，空字符串或通过数组形式设置多种模式（如： ["push", "pop"]） | [2.25.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | [] | 取消小窗 | | push | 路由 push 时触发小窗 | | pop | 路由 pop 时触发小窗 | | | | | | |
|  | voice-changer-type | number | 0 | 否 | 0：关闭变声；1：熊孩子；2：萝莉；3：大叔；4：重金属；6：外国人；7：困兽；8：死肥仔；9：强电流；10：重机械；11：空灵 | [2.31.0](../framework/compatibility.html) |
|  | custom-effect | boolean | false | 否 | 是否启动自定义特效，设定后不能更改 | [2.29.1](../framework/compatibility.html) |
|  | skin-whiteness | number | 0 | 否 | 自定义特效美白效果，取值 0~1。需要开启 `custom-effect` | [2.29.1](../framework/compatibility.html) |
|  | skin-smoothness | number | 0 | 否 | 自定义特效磨皮效果，取值 0~1。需要开启 `custom-effect` | [2.29.1](../framework/compatibility.html) |
|  | face-thinness | number | 0 | 否 | 自定义特效瘦脸效果，取值 0~1。需要开启 `custom-effect` | [2.29.1](../framework/compatibility.html) |
|  | eye-bigness | number | 0 | 否 | 自定义特效大眼效果，取值 0~1。需要开启 `custom-effect` | [2.29.1](../framework/compatibility.html) |
|  | fps | number | 15 | 否 | 帧率，有效值为 1~30 | [2.31.0](../framework/compatibility.html) |
|  | mute-on-audio-conflict | boolean | false | 否 | 音频冲突时是否静音 | [3.16.2](../framework/compatibility.html) |
|  | bindstatechange | eventhandle |  | 否 | 状态变化事件，detail = {code} | [1.7.0](../framework/compatibility.html) |
|  | bindnetstatus | eventhandle |  | 否 | 网络状态通知，detail = {info} | [1.9.0](../framework/compatibility.html) |
|  | binderror | eventhandle |  | 否 | 渲染错误事件，detail = {errMsg, errCode} | [1.7.4](../framework/compatibility.html) |
|  | bindbgmstart | eventhandle |  | 否 | 背景音开始播放时触发 | [2.4.0](../framework/compatibility.html) |
|  | bindbgmprogress | eventhandle |  | 否 | 背景音进度变化时触发，detail = {progress, duration} | [2.4.0](../framework/compatibility.html) |
|  | bindbgmcomplete | eventhandle |  | 否 | 背景音播放完成时触发 | [2.4.0](../framework/compatibility.html) |
|  | bindaudiovolumenotify | eventhandle |  | 否 | 返回麦克风采集的音量大小 | [2.12.0](../framework/compatibility.html) |
|  | bindenterpictureinpicture | eventhandler |  | 否 | 进入小窗 | [2.25.0](../framework/compatibility.html) |
|  | bindleavepictureinpicture | eventhandler |  | 否 | 退出小窗 | [2.25.0](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| QVGA | Quarter VGA | [3.5.0](../framework/compatibility.html) |
| HVGA | Half-size VGA | [3.5.0](../framework/compatibility.html) |
| SD | 标清 | [1.7.0](../framework/compatibility.html) |
| HD | 高清 | [1.7.0](../framework/compatibility.html) |
| FHD | 超清 | [1.7.0](../framework/compatibility.html) |
| RTC | 实时通话 | [1.7.0](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| vertical | 竖直 |
| horizontal | 水平 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| auto | 前置摄像头镜像，后置摄像头不镜像 |
| enable | 前后置摄像头均镜像 |
| disable | 前后置摄像头均不镜像 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| 0 | 关闭 |
| 1 | KTV |
| 2 | 小房间 |
| 3 | 大会堂 |
| 4 | 低沉 |
| 5 | 洪亮 |
| 6 | 金属声 |
| 7 | 磁性 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| auto | 自动 |
| media | 媒体音量 |
| voicecall | 通话音量 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| smooth | 光滑美颜 |
| nature | 自然美颜 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| standard | 标准 |
| pink | 粉嫩 |
| nostalgia | 怀旧 |
| blues | 蓝调 |
| romantic | 浪漫 |
| cool | 清凉 |
| fresher | 清新 |
| solor | 日系 |
| aestheticism | 唯美 |
| whitening | 美白 |
| cerisered | 樱红 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| [] | 取消小窗 |
| push | 路由 push 时触发小窗 |
| pop | 路由 pop 时触发小窗 |

**错误码（errCode）**

| 代码 | 说明 |
| --- | --- |
| 10001 | 用户禁止使用摄像头 |
| 10002 | 用户禁止使用录音 |
| 10003 | 背景音资源（BGM）加载失败 |
| 10004 | 等待画面资源（waiting-image）加载失败 |

**状态码（code）**

| 代码 | 说明 |
| --- | --- |
| 1001 | 推流：已经连接推流服务器 |
| 1002 | 推流：已经与服务器握手完毕，开始推流 |
| 1003 | 推流：打开摄像头成功 |
| 1004 | 推流：录屏启动成功 |
| 1005 | 推流：推流动态调整分辨率 |
| 1006 | 推流：推流动态调整码率 |
| 1007 | 推流：首帧画面采集完成 |
| 1008 | 推流：编码器启动 |
| 1009 | 推流：发送视频首帧 |
| 1018 | 推流：进房成功（ROOM协议特有） |
| 1019 | 推流：退房成功（ROOM协议特有） |
| 1020 | 推流：远端主播列表变化（ROOM协议特有） |
| 1021 | 推流：网络变更时重进房，WiFi 切换到4G 会触发断线重连（ROOM协议特有） |
| 1022 | 推流：进入房间失败（ROOM协议特有） |
| 1031 | 推流：远端主播进房通知（ROOM协议特有） |
| 1032 | 推流：远端主播退房通知（ROOM协议特有） |
| 1033 | 推流：远端主播视频状态位变化（ROOM协议特有） |
| 1034 | 推流：远端主播音频状态位变化（ROOM协议特有） |
| 1101 | 推流：网络状况不佳：上行带宽太小，上传数据受阻 |
| 1102 | 推流：网络断连, 已启动自动重连 |
| 1103 | 推流：硬编码启动失败，内部会尝试切换软编码器（Android特有） |
| 1104 | 推流：编码器类型发生变化 |
| 1109 | 推流：软编码启动失败, 内部会尝试切换硬编码器（Android特有） |
| 2027 | 推流：麦克风启动成功 |
| 3001 | 推流：RTMP DNS解析失败 |
| 3002 | 推流：RTMP服务器连接失败 |
| 3003 | 推流：RTMP服务器握手失败 |
| 3004 | 推流：RTMP服务器主动断开，请检查推流地址的合法性或防盗链有效期 |
| 3005 | 推流：RTMP 读/写失败 |
| -1301 | 推流：打开摄像头失败 |
| -1302 | 推流：打开麦克风失败 |
| -1303 | 推流：视频编码失败 |
| -1304 | 推流：音频编码失败 |
| -1305 | 推流：不支持的视频分辨率 |
| -1306 | 推流：不支持的音频采样率 |
| -1307 | 推流：网络断连，且经多次重连抢救无效，请自行重启推流 |
| -1308 | 推流：开始录屏失败，可能是被用户拒绝 |
| -1309 | 推流：录屏失败，不支持的Android系统版本，需要5.0以上的系统 |
| -1310 | 推流：录屏被其他应用打断了 |
| -1311 | 推流：Android Mic打开成功，但是录不到音频数据 |
| -1312 | 推流：录屏动态切横竖屏失败 |
| -1318 | 推流：麦克风设置参数失败，当前设备不支持设置的参数 |
| 10001 | 用户禁止使用摄像头 |
| 10002 | 用户禁止使用录音 |
| 10003 | 背景音资源（BGM）加载失败 |
| 10004 | 等待画面资源（waiting-image）加载失败 |
| 4998 | Mic状态切换的时候，enable-mic触发（iOS特有） |
| 4999 | mute状态切换的时候，muted 触发（iOS特有） |
| 5000 | 推流：被挂起，小程序或微信被退后台时挂起推流 |
| 5001 | 系统电话打断或者微信音视频电话打断 |
| 0 | 无错误 |

**网络状态数据（info）**

| 键名 | 说明 |
| --- | --- |
| videoBitrate | 当前视频编/码器输出的比特率，单位 kbps |
| audioBitrate | 当前音频编/码器输出的比特率，单位 kbps |
| videoFPS | 当前视频帧率 |
| videoGOP | 当前视频 GOP,也就是每两个关键帧(I帧)间隔时长，单位 s |
| netSpeed | 当前的发送/接收速度 |
| netJitter | 网络抖动情况，抖动越大，网络越不稳定 |
| netQualityLevel | 网络质量：0：未定义 1：最好 2：好 3：一般 4：差 5：很差 6：不可用 |
| videoWidth | 视频画面的宽度 |
| videoHeight | 视频画面的高度 |
| videoCache | 主播端堆积的视频帧数 |
| audioCache | 主播端堆积的音频帧数 |

---

### video

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/video.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | src | string |  | 是 | 要播放视频的资源地址，支持网络路径、本地临时路径、云文件ID（[2.3.0](../framework/compatibility.html)） | [1.0.0](../framework/compatibility.html) |
|  | duration | number |  | 否 | 指定视频时长 | [1.1.0](../framework/compatibility.html) |
|  | controls | boolean | true | 否 | 是否显示默认播放控件（播放/暂停按钮、播放进度、时间） | [1.0.0](../framework/compatibility.html) |
|  | danmu-list | Array.<object> |  | 否 | 弹幕列表 | [1.0.0](../framework/compatibility.html) |
|  | danmu-btn | boolean | false | 否 | 是否显示弹幕按钮，只在初始化时有效，不能动态变更 | [1.0.0](../framework/compatibility.html) |
|  | enable-danmu | boolean | false | 否 | 是否展示弹幕，只在初始化时有效，不能动态变更 | [1.0.0](../framework/compatibility.html) |
|  | autoplay | boolean | false | 否 | 是否自动播放 | [1.0.0](../framework/compatibility.html) |
|  | loop | boolean | false | 否 | 是否循环播放 | [1.4.0](../framework/compatibility.html) |
|  | muted | boolean | false | 否 | 是否静音播放 | [1.4.0](../framework/compatibility.html) |
|  | initial-time | number | 0 | 否 | 指定视频初始播放位置 | [1.6.0](../framework/compatibility.html) |
|  | page-gesture | boolean | false | 否 | 在非全屏模式下，是否开启亮度与音量调节手势（废弃，见 vslide-gesture） | [1.6.0](../framework/compatibility.html) |
|  | direction | number |  | 否 | 设置全屏时视频的方向，不指定则根据宽高比自动判断 | [1.7.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 正常竖向 | | 90 | 屏幕逆时针90度 | | -90 | 屏幕顺时针90度 | | | | | | |
|  | show-progress | boolean | true | 否 | 若不设置，宽度大于240时才会显示 | [1.9.0](../framework/compatibility.html) |
|  | show-fullscreen-btn | boolean | true | 否 | 是否显示全屏按钮 | [1.9.0](../framework/compatibility.html) |
|  | show-play-btn | boolean | true | 否 | 是否显示视频底部控制栏的播放按钮 | [1.9.0](../framework/compatibility.html) |
|  | show-center-play-btn | boolean | true | 否 | 是否显示视频中间的播放按钮 | [1.9.0](../framework/compatibility.html) |
|  | enable-progress-gesture | boolean | true | 否 | 是否开启控制进度的手势 | [1.9.0](../framework/compatibility.html) |
|  | object-fit | string | contain | 否 | 当视频大小与 video 容器大小不一致时，视频的表现形式 | [1.0.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | contain | 包含 | | fill | 填充 | | cover | 覆盖 | | | | | | |
|  | poster | string |  | 否 | 视频封面的图片网络资源地址或云文件ID（[2.3.0](../framework/compatibility.html)）。若 controls 属性值为 false 则设置 poster 无效 | [1.0.0](../framework/compatibility.html) |
|  | show-mute-btn | boolean | false | 否 | 是否显示静音按钮 | [2.4.0](../framework/compatibility.html) |
|  | title | string |  | 否 | 视频的标题，全屏时在顶部展示 | [2.4.0](../framework/compatibility.html) |
|  | play-btn-position | string | bottom | 否 | 播放按钮的位置 | [2.4.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | bottom | controls bar上 | | center | 视频中间 | | | | | | |
|  | enable-play-gesture | boolean | false | 否 | 是否开启播放手势，即双击切换播放/暂停 | [2.4.0](../framework/compatibility.html) |
|  | auto-pause-if-navigate | boolean | true | 否 | 当跳转到本小程序的其他页面时，是否自动暂停本页面的视频播放 | [2.5.0](../framework/compatibility.html) |
|  | auto-pause-if-open-native | boolean | true | 否 | 当跳转到其它微信原生页面时，是否自动暂停本页面的视频 | [2.5.0](../framework/compatibility.html) |
|  | vslide-gesture | boolean | false | 否 | 在非全屏模式下，是否开启亮度与音量调节手势（同 page-gesture） | [2.6.2](../framework/compatibility.html) |
|  | vslide-gesture-in-fullscreen | boolean | true | 否 | 在全屏模式下，是否开启亮度与音量调节手势 | [2.6.2](../framework/compatibility.html) |
|  | show-bottom-progress | boolean | true | 否 | 是否展示底部进度条 | [2.8.0](../framework/compatibility.html) |
|  | ad-unit-id | string |  | 是 | 视频前贴广告单元ID，更多详情可参考开放能力[视频前贴广告](../framework/open-ability/ad/video-patch-ad.html) | [2.8.1](../framework/compatibility.html) |
|  | poster-for-crawler | string |  | 是 | 用于给搜索等场景作为视频封面展示，建议使用无播放 icon 的视频封面图，只支持网络地址 |  |
|  | show-casting-button | boolean | false | 否 | 显示投屏按钮。安卓在同层渲染下生效，支持 DLNA 协议；iOS 支持 AirPlay 和 DLNA 协议；鸿蒙 OS 暂不支持。可以通过[VideoContext](../api/media/video/VideoContext.html)的相关方法进行操作。 | [2.10.2](../framework/compatibility.html) |
|  | picture-in-picture-mode | string/Array |  | 否 | 设置小窗模式： push, pop，空字符串或通过数组形式设置多种模式（如： ["push", "pop"]）。鸿蒙 OS 暂不支持 | [2.11.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | [] | 取消小窗 | | push | 路由 push 时触发小窗 | | pop | 路由 pop 时触发小窗 | | | | | | |
|  | picture-in-picture-show-progress | boolean | false | 否 | 是否在小窗模式下显示播放进度 | [2.11.0](../framework/compatibility.html) |
|  | picture-in-picture-init-position | string |  | 否 | 小窗模式下小窗的初始显示位置，格式为 (alignment, y)，其中 alignment 表示小窗吸附屏幕左侧还是右侧，可选值为 left、right，y 代表小窗最顶部所在的屏幕高度百分比 | [3.3.0](../framework/compatibility.html) |
|  | enable-system-pip | boolean | true | 否 | 是否支持 iOS 系统画中画，默认支持 | [3.15.1](../framework/compatibility.html) |
|  | enable-auto-rotation | boolean | false | 否 | 是否开启手机横屏时自动全屏，当系统设置开启自动旋转时生效 | [2.11.0](../framework/compatibility.html) |
|  | show-screen-lock-button | boolean | false | 否 | 是否显示锁屏按钮，仅在全屏时显示，锁屏后控制栏的操作 | [2.11.0](../framework/compatibility.html) |
|  | show-snapshot-button | boolean | false | 否 | 是否显示截屏按钮，仅在全屏时显示 | [2.13.0](../framework/compatibility.html) |
|  | show-background-playback-button | boolean | true | 否 | 是否展示后台小窗播放按钮。鸿蒙 OS 暂不支持。基础库 3.6.0 开始默认值为 true。 | [2.14.3](../framework/compatibility.html) |
|  | background-poster | string |  | 否 | 进入后台小窗播放后的通知栏图标（Android 独有） | [2.14.3](../framework/compatibility.html) |
|  | referrer-policy | string | no-referrer | 否 | 格式固定为 `https://servicewechat.com/{appid}/{version}/page-frame.html`，其中 {appid} 为小程序的 appid，{version} 为小程序的版本号，版本号为 0 表示为开发版、体验版以及审核版本，版本号为 devtools 表示为开发者工具，其余为正式版本； | [2.13.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | origin | 发送完整的referrer | | no-referrer | 不发送 | | | | | | |
|  | is-drm | boolean |  | 否 | 是否为 DRM 视频源 | [2.19.3](../framework/compatibility.html) |
|  | is-live | boolean |  | 否 | 是否为直播源 | [2.28.1](../framework/compatibility.html) |
|  | provision-url | string |  | 否 | DRM 设备身份认证 url，仅 is-drm 为 true 时生效 (Android) | [2.19.3](../framework/compatibility.html) |
|  | certificate-url | string |  | 否 | DRM 设备身份认证 url，仅 is-drm 为 true 时生效 (iOS) | [2.19.3](../framework/compatibility.html) |
|  | license-url | string |  | 否 | DRM 获取加密信息 url，仅 is-drm 为 true 时生效 | [2.19.3](../framework/compatibility.html) |
|  | preferred-peak-bit-rate | number |  | 否 | 指定码率上界，单位为比特每秒 | [2.26.0](../framework/compatibility.html) |
|  | bindplay | eventhandle |  | 否 | 当开始/继续播放时触发play事件 | [1.0.0](../framework/compatibility.html) |
|  | bindpause | eventhandle |  | 否 | 当暂停播放时触发 pause 事件 | [1.0.0](../framework/compatibility.html) |
|  | bindended | eventhandle |  | 否 | 当播放到末尾时触发 ended 事件 | [1.0.0](../framework/compatibility.html) |
|  | bindtimeupdate | eventhandle |  | 否 | 播放进度变化时触发，event.detail = {currentTime, duration} 。触发频率 250ms 一次 | [1.0.0](../framework/compatibility.html) |
|  | bindfullscreenchange | eventhandle |  | 否 | 视频进入和退出全屏时触发，event.detail = {fullScreen, direction}，direction 有效值为 vertical 或 horizontal | [1.4.0](../framework/compatibility.html) |
|  | bindwaiting | eventhandle |  | 否 | 视频出现缓冲时触发 | [1.7.0](../framework/compatibility.html) |
|  | binderror | eventhandle |  | 否 | 视频播放出错时触发 | [1.7.0](../framework/compatibility.html) |
|  | bindprogress | eventhandle |  | 否 | 加载进度变化时触发，只支持一段加载。event.detail = {buffered}，百分比 | [2.4.0](../framework/compatibility.html) |
|  | bindloadedmetadata | eventhandle |  | 否 | 视频元数据加载完成时触发。event.detail = {width, height, duration} | [2.7.0](../framework/compatibility.html) |
|  | bindcontrolstoggle | eventhandle |  | 否 | 切换 controls 显示隐藏时触发。event.detail = {show} | [2.9.5](../framework/compatibility.html) |
|  | bindenterpictureinpicture | eventhandler |  | 否 | 播放器进入小窗 | [2.11.0](../framework/compatibility.html) |
|  | bindleavepictureinpicture | eventhandler |  | 否 | 播放器退出小窗 | [2.11.0](../framework/compatibility.html) |
|  | bindseekcomplete | eventhandler |  | 否 | seek 完成时触发 (position iOS 单位 s, Android 单位 ms) | [2.12.0](../framework/compatibility.html) |
|  | bindcastinguserselect | eventhandler |  | 否 | 用户选择投屏设备时触发 detail = { state: "success"/"fail" }。鸿蒙 OS 暂不支持 | [2.32.0](../framework/compatibility.html) |
|  | bindcastingstatechange | eventhandler |  | 否 | 投屏成功/失败时触发 detail = { type, state: "success"/"fail" }。鸿蒙 OS 暂不支持 | [2.32.0](../framework/compatibility.html) |
|  | bindcastinginterrupt | eventhandler |  | 否 | 投屏被中断时触发。鸿蒙 OS 暂不支持 | [2.32.0](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| 0 | 正常竖向 |
| 90 | 屏幕逆时针90度 |
| -90 | 屏幕顺时针90度 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| contain | 包含 |
| fill | 填充 |
| cover | 覆盖 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| bottom | controls bar上 |
| center | 视频中间 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| [] | 取消小窗 |
| push | 路由 push 时触发小窗 |
| pop | 路由 pop 时触发小窗 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| origin | 发送完整的referrer |
| no-referrer | 不发送 |

**支持的格式**

| 格式 | iOS | Android |
| --- | --- | --- |
| mp4 | √ | √ |
| mov | √ | x |
| m4v | √ | x |
| 3gp | √ | √ |
| avi | √ | x |
| m3u8 | √ | √ |
| webm | x | √ |

**支持的编码格式**

| 格式 | iOS | Android |
| --- | --- | --- |
| H.264 | √ | √ |
| HEVC | √ | √ |
| MPEG-4 | √ | √ |
| VP9 | x | √ |

---

### voip-room

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/voip-room.html

**申请开通**

| 一级类目/主体类型 | 二级类目 | 小程序内容场景 |
| --- | --- | --- |
| 教育 | 在线视频课程 | 网课、在线培训、讲座等教育类直播 |
| 医疗 | 互联网医院，公立医院 | 问诊、大型健康讲座等直播 |
| 医疗 | 私立医疗机构 | / |
| 金融 | 银行、信托、基金、证券/期货、证券、期货投资咨询、保险、征信业务、新三板信息服务平台、股票信息服务平台（港股/美股）、消费金融 | 金融产品视频客服理赔、金融产品推广直播等 |
| 汽车 | 汽车预售服务 | 汽车预售、推广直播 |
| 政府主体账号 | / | 政府相关工作推广直播、领导讲话直播等 |
| IT 科技 | 多方通信 | 在线会议 |
| 快递业与邮政 | 寄件/收件 | 视频客服 |

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | openid | string |  | 是 | 进入房间用户的 openid | [2.11.0](../framework/compatibility.html) |
|  | mode | string | camera | 是 | 对话窗口类型 | [2.11.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | camera | 自身传入 camera | | video | 其他用户传入 video | | | | | | |
|  | device-position | string | front | 是 | 摄像头方向，仅在 mode 为 camera 时有效 | [2.11.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | front | 前置 | | back | 后置 | | | | | | |
|  | object-fit | string | fill | 是 | 画面与容器比例不一致时，画面的表现形式 | [2.29.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | fill | 填充 | | contain | 包含 | | cover | 覆盖，安卓暂未支持，iOS 生效 | | | | | | |
|  | binderror | eventhandle |  | 否 | 创建对话窗口失败时触发 | [2.11.0](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| camera | 自身传入 camera |
| video | 其他用户传入 video |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| front | 前置 |
| back | 后置 |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| fill | 填充 |
| contain | 包含 |
| cover | 覆盖，安卓暂未支持，iOS 生效 |

---

### map

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/map.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| longitude | number |  | 是 | 中心经度 | [1.0.0](../framework/compatibility.html) |
| latitude | number |  | 是 | 中心纬度 | [1.0.0](../framework/compatibility.html) |
| scale | number | 16 | 否 | 缩放级别，取值范围为3-20 | [1.0.0](../framework/compatibility.html) |
| min-scale | number | 3 | 否 | 最小缩放级别 | [2.13.0](../framework/compatibility.html) |
| max-scale | number | 20 | 否 | 最大缩放级别 | [2.13.0](../framework/compatibility.html) |
| markers | Array.<marker> |  | 否 | 标记点 | [1.0.0](../framework/compatibility.html) |
| covers | Array.<cover> |  | 否 | **即将移除，请使用 markers** | [1.0.0](../framework/compatibility.html) |
| polyline | Array.<polyline> |  | 否 | 路线 | [1.0.0](../framework/compatibility.html) |
| circles | Array.<circle> |  | 否 | 圆 | [1.0.0](../framework/compatibility.html) |
| controls | Array.<control> |  | 否 | 控件（即将废弃，建议使用 [cover-view](cover-view.html) 代替） | [1.0.0](../framework/compatibility.html) |
| include-points | Array.<point> |  | 否 | 缩放视野以包含所有给定的坐标点 | [1.0.0](../framework/compatibility.html) |
| show-location | boolean | false | 否 | 显示带有方向的当前定位点，[3.10.0](../framework/compatibility.html)起需要用户位置授权。[3.13.2](../framework/compatibility.html)起如果开发者没有手动申请，则会自动申请 | [1.0.0](../framework/compatibility.html) |
| polygons | Array.<polygon> |  | 否 | 多边形 | [2.3.0](../framework/compatibility.html) |
| subkey | string |  | 否 | 地图能力【个性化地图】使用的key，不支持动态修改 | [2.3.0](../framework/compatibility.html) |
| layer-style | number | 1 | 否 | 地图能力【个性化地图】配置的 style |  |
| rotate | number | 0 | 否 | 旋转角度，范围 0 ~ 360, 地图正北和设备 y 轴角度的夹角 | [2.5.0](../framework/compatibility.html) |
| skew | number | 0 | 否 | 倾斜角度，范围 0 ~ 40 , 关于 z 轴的倾角 | [2.5.0](../framework/compatibility.html) |
| enable-3D | boolean | false | 否 | 展示3D楼块 | [2.3.0](../framework/compatibility.html) |
| show-compass | boolean | false | 否 | 显示指南针 | [2.3.0](../framework/compatibility.html) |
| show-scale | boolean | false | 否 | 显示比例尺，工具暂不支持 | [2.8.0](../framework/compatibility.html) |
| enable-overlooking | boolean | false | 否 | 开启俯视 | [2.3.0](../framework/compatibility.html) |
| enable-auto-max-overlooking | boolean | false | 否 | 开启最大俯视角，俯视角度从 45 度拓展到 75 度 | [2.26.0](../framework/compatibility.html) |
| enable-zoom | boolean | true | 否 | 是否支持缩放 | [2.3.0](../framework/compatibility.html) |
| enable-scroll | boolean | true | 否 | 是否支持拖动 | [2.3.0](../framework/compatibility.html) |
| enable-rotate | boolean | false | 否 | 是否支持旋转 | [2.3.0](../framework/compatibility.html) |
| enable-satellite | boolean | false | 否 | 是否开启卫星图 | [2.7.0](../framework/compatibility.html) |
| enable-traffic | boolean | false | 否 | 是否开启实时路况 | [2.7.0](../framework/compatibility.html) |
| enable-poi | boolean | true | 否 | 是否展示 POI 点 | [2.14.0](../framework/compatibility.html) |
| enable-building | boolean |  | 否 | 是否展示建筑物 | [2.14.0](../framework/compatibility.html) |
| setting | object |  | 否 | 配置项 | [2.8.2](../framework/compatibility.html) |
| bindtap | eventhandle |  | 否 | 点击地图时触发，[2.9.0](../framework/compatibility.html)起返回经纬度信息 | [1.0.0](../framework/compatibility.html) |
| bindmarkertap | eventhandle |  | 否 | 点击标记点时触发，`e.detail = {markerId}` | [1.0.0](../framework/compatibility.html) |
| bindlabeltap | eventhandle |  | 否 | 点击label时触发，`e.detail = {markerId}` | [2.9.0](../framework/compatibility.html) |
| bindcontroltap | eventhandle |  | 否 | 点击控件时触发，`e.detail = {controlId}` | [1.0.0](../framework/compatibility.html) |
| bindcallouttap | eventhandle |  | 否 | 点击标记点对应的气泡时触发`e.detail = {markerId}` | [1.2.0](../framework/compatibility.html) |
| bindupdated | eventhandle |  | 否 | 在地图渲染更新完成时触发 | [1.6.0](../framework/compatibility.html) |
| bindregionchange | eventhandle |  | 否 | 视野发生变化时触发， | [2.3.0](../framework/compatibility.html) |
| bindpoitap | eventhandle |  | 否 | 点击地图poi点时触发，`e.detail = {name, longitude, latitude}` | [2.3.0](../framework/compatibility.html) |
| bindpolylinetap | eventhandle |  | 否 | 点击地图路线时触发，`e.detail = {longitude, latitude}` | [3.1.0](../framework/compatibility.html) |
| bindabilitysuccess | eventhandle |  | 否 | 地图能力生效时触发，`e.detail = {ability, errCode, errMsg}` |  |
| bindabilityfail | eventhandle |  | 否 | 地图能力失败时触发，`e.detail = {ability, errCode, errMsg}` |  |
| bindauthsuccess | eventhandle |  | 否 | 地图鉴权结果成功时触发，`e.detail = {errCode, errMsg}` |  |
| bindinterpolatepoint | eventhandle |  | 否 | MapContext.moveAlong 插值动画时触发。`e.detail = {markerId, longitude, latitude, animationStatus: "interpolating" | "complete"}`, | [3.1.0](../framework/compatibility.html) |
| binderror | eventhandle |  | 否 | 组件错误时触发，例如创建或鉴权失败，`e.detail = {longitude, latitude}` |  |

**marker**

| 属性 | 说明 | 类型 | 必填 | 备注 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| id | 标记点 id | number | 是 | marker 点击事件回调会返回此 id。 |  |
| clusterId | 聚合簇的 id | Number | 否 | 自定义点聚合簇效果时使用 |  |
| joinCluster | 是否参与点聚合 | Boolean | 否 | 默认不参与点聚合 |  |
| latitude | 纬度 | number | 是 | 浮点数，范围 -90 ~ 90 |  |
| longitude | 经度 | number | 是 | 浮点数，范围 -180 ~ 180 |  |
| title | 标注点名 | string | 否 | 点击时显示，callout 存在时将被忽略 |  |
| zIndex | 显示层级 | number | 否 |  | [2.3.0](../framework/compatibility.html) |
| iconPath | 显示的图标 | string | 是 | 项目目录下的图片路径，支持网络路径、本地路径、代码包路径（[2.3.0](../framework/compatibility.html)） |  |
| rotate | 旋转角度 | number | 否 | 顺时针旋转的角度，范围 0 ~ 360，默认为 0 |  |
| alpha | 标注的透明度 | number | 否 | 默认 1，无透明，范围 0 ~ 1 |  |
| width | 标注图标宽度 | number/string | 否 | 默认为图片实际宽度 |  |
| height | 标注图标高度 | number/string | 否 | 默认为图片实际高度 |  |
| callout | 标记点上方的气泡窗口 | Object | 否 | 支持的属性见下表，可识别换行符。 | [1.2.0](../framework/compatibility.html) |
| customCallout | 自定义气泡窗口 | Object | 否 | 支持的属性见下表 |  |
| label | 为标记点旁边增加标签 | Object | 否 | 支持的属性见下表，可识别换行符。 | [1.2.0](../framework/compatibility.html) |
| anchor | 经纬度在标注图标的锚点，默认底边中点 | Object | 否 | {x, y}，x 表示横向(0-1)，y 表示竖向(0-1)。{x: .5, y: 1} 表示底边中点 | [1.2.0](../framework/compatibility.html) |
| aria-label | 无障碍访问，（属性）元素的额外描述 | string | 否 |  | [2.5.0](../framework/compatibility.html) |
| collisionRelation | 碰撞关系 | string | 否 | 详见下表碰撞关系 | [3.4.3](../framework/compatibility.html) |
| collision | 碰撞类型 | string | 否 | 详见下表碰撞关系 | [3.4.3](../framework/compatibility.html) |

**marker 上的气泡 callout**

| 属性 | 说明 | 类型 | 最低版本 |
| --- | --- | --- | --- |
| content | 文本 | string | [1.2.0](../framework/compatibility.html) |
| color | 文本颜色 | string | [1.2.0](../framework/compatibility.html) |
| fontSize | 文字大小 | number | [1.2.0](../framework/compatibility.html) |
| borderRadius | 边框圆角 | number | [1.2.0](../framework/compatibility.html) |
| borderWidth | 边框宽度 | number | [2.3.0](../framework/compatibility.html) |
| borderColor | 边框颜色 | string | [2.3.0](../framework/compatibility.html) |
| bgColor | 背景色 | string | [1.2.0](../framework/compatibility.html) |
| padding | 文本边缘留白 | number | [1.2.0](../framework/compatibility.html) |
| display | 'BYCLICK':点击显示; 'ALWAYS':常显 | string | [1.2.0](../framework/compatibility.html) |
| textAlign | 文本对齐方式。有效值: left, right, center | string | [1.6.0](../framework/compatibility.html) |
| anchorX | 横向偏移量，向右为正数 | number | [2.11.0](../framework/compatibility.html) |
| anchorY | 纵向偏移量，向下为正数 | number | [2.11.0](../framework/compatibility.html) |
| collision | 碰撞类型 | string | [3.4.3](../framework/compatibility.html) |

**marker 上的自定义气泡 customCallout**

| 属性 | 说明 | 类型 | 最低版本 |
| --- | --- | --- | --- |
| display | 'BYCLICK':点击显示; 'ALWAYS':常显 | string | [2.12.0](../framework/compatibility.html) |
| anchorX | 横向偏移量，向右为正数 | number | [2.12.0](../framework/compatibility.html) |
| anchorY | 纵向偏移量，向下为正数 | number | [2.12.0](../framework/compatibility.html) |

**marker 上的气泡 label**

| 属性 | 说明 | 类型 | 最低版本 |
| --- | --- | --- | --- |
| content | 文本 | string | [1.2.0](../framework/compatibility.html) |
| color | 文本颜色 | string | [1.2.0](../framework/compatibility.html) |
| fontSize | 文字大小 | number | [1.2.0](../framework/compatibility.html) |
| x | label的坐标（废弃） | number | [1.2.0](../framework/compatibility.html) |
| y | label的坐标（废弃） | number | [1.2.0](../framework/compatibility.html) |
| anchorX | label的坐标，原点是 marker 对应的经纬度 | number | [2.1.0](../framework/compatibility.html) |
| anchorY | label的坐标，原点是 marker 对应的经纬度 | number | [2.1.0](../framework/compatibility.html) |
| borderWidth | 边框宽度 | number | [1.6.0](../framework/compatibility.html) |
| borderColor | 边框颜色 | string | [1.6.0](../framework/compatibility.html) |
| borderRadius | 边框圆角 | number | [1.6.0](../framework/compatibility.html) |
| bgColor | 背景色 | string | [1.6.0](../framework/compatibility.html) |
| padding | 文本边缘留白 | number | [1.6.0](../framework/compatibility.html) |
| textAlign | 文本对齐方式。有效值: left, right, center | string | [1.6.0](../framework/compatibility.html) |
| collision | 碰撞类型 | string | [3.4.3](../framework/compatibility.html) |

**polyline**

| 属性 | 说明 | 类型 | 必填 | 备注 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| points | 经纬度数组 | array | 是 | [{latitude: 0, longitude: 0}] |  |
| color | 线的颜色 | string | 否 | 十六进制 |  |
| colorList | 彩虹线 | array | 否 | 存在时忽略 color 值 | [2.13.0](../framework/compatibility.html) |
| width | 线的宽度 | number | 否 |  |  |
| dottedLine | 是否虚线 | boolean | 否 | 默认 false |  |
| arrowLine | 带箭头的线 | boolean | 否 | 默认 false，开发者工具暂不支持该属性 | [1.2.0](../framework/compatibility.html) |
| arrowIconPath | 更换箭头图标 | string | 否 | 在 arrowLine 为 true 时生效 | [1.6.0](../framework/compatibility.html) |
| borderColor | 线的边框颜色 | string | 否 |  | [1.2.0](../framework/compatibility.html) |
| borderWidth | 线的厚度 | number | 否 |  | [1.2.0](../framework/compatibility.html) |
| level | 压盖关系 | string | 否 | 默认为 abovelabels | [2.14.0](../framework/compatibility.html) |
| textStyle | 文字样式 | TextStyle | 否 | 折线上文本样式 | [2.22.0](../framework/compatibility.html) |
| segmentTexts | 分段文本 | `Array<SegmentText>` | 否 | 折线上文本内容和位置 | [2.22.0](../framework/compatibility.html) |

**polyline**

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| name | 名称 | string | '' |
| startIndex | 起点 | number |  |
| endIndex | 终点 | number |  |

**polyline**

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| textColor | 文本颜色 | string | #000000 |
| strokeColor | 描边颜色 | string | #ffffff |
| fontSize | 文本大小 | number | 14 |

**polyline**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| abovelabels | 显示在所有 POI 之上 | [2.14.0](../framework/compatibility.html) |
| abovebuildings | 显示在楼块之上 POI 之下 | [2.14.0](../framework/compatibility.html) |
| aboveroads | 显示在道路之上楼块之下 | [2.14.0](../framework/compatibility.html) |

**polygon**

| 属性 | 说明 | 类型 | 必填 | 备注 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| dashArray | 边线虚线 | `Array<number>` | 否 | 默认值 [0, 0] 为实线，[10, 10]表示十个像素的实线和十个像素的空白（如此反复）组成的虚线 | [2.22.0](../framework/compatibility.html) |
| points | 经纬度数组 | array | 是 | [{latitude: 0, longitude: 0}] | [2.3.0](../framework/compatibility.html) |
| strokeWidth | 描边的宽度 | number | 否 |  | [2.3.0](../framework/compatibility.html) |
| strokeColor | 描边的颜色 | string | 否 | 十六进制 | [2.3.0](../framework/compatibility.html) |
| fillColor | 填充颜色 | string | 否 | 十六进制 |  |
| zIndex | 设置多边形 Z 轴数值 | number | 否 |  | [2.3.0](../framework/compatibility.html) |
| level | 压盖关系 | string | 否 | 默认为 abovelabels | [2.14.0](../framework/compatibility.html) |

**circle**

| 属性 | 说明 | 类型 | 必填 | 备注 |
| --- | --- | --- | --- | --- |
| latitude | 纬度 | number | 是 | 浮点数，范围 -90 ~ 90 |
| longitude | 经度 | number | 是 | 浮点数，范围 -180 ~ 180 |
| color | 描边的颜色 | string | 否 | 十六进制 |
| fillColor | 填充颜色 | string | 否 | 十六进制 |
| radius | 半径 | number | 是 |  |
| strokeWidth | 描边的宽度 | number | 否 |  |
| level | 压盖关系 | string | 否 | 默认为 abovelabels |

**control**

| 属性 | 说明 | 类型 | 必填 | 备注 |
| --- | --- | --- | --- | --- |
| id | 控件id | number | 否 | 在控件点击事件回调会返回此id |
| position | 控件在地图的位置 | object | 是 | 控件相对地图位置 |
| iconPath | 显示的图标 | string | 是 | 项目目录下的图片路径，支持本地路径、代码包路径 |
| clickable | 是否可点击 | boolean | 否 | 默认不可点击 |

**position**

| 属性 | 说明 | 类型 | 必填 | 备注 |
| --- | --- | --- | --- | --- |
| left | 距离地图的左边界多远 | number | 否 | 默认为0 |
| top | 距离地图的上边界多远 | number | 否 | 默认为0 |
| width | 控件宽度 | number | 否 | 默认为图片宽度 |
| height | 控件高度 | number | 否 | 默认为图片高度 |

**bindregionchange 返回值**

| 属性 | 说明 | 类型 | 备注 |
| --- | --- | --- | --- |
| type | 视野变化开始、结束时触发 | string | 视野变化开始为begin，结束为end |
| causedBy | 导致视野变化的原因 | string | 拖动地图导致(drag)、缩放导致(scale)、调用接口导致(update) |

**比例尺**

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scale | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| 比例 | 1000km | 500km | 200km | 100km | 50km | 25km | 20km | 10km | 5km |
| scale | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| 比例 | 2km | 1km | 500m | 200m | 100m | 50m | 20m | 10m | 5m |

**bindabilitysuccess、bindabilityfail 和 binderror 的返回值**

| errCode | 说明 ｜ |
| --- | --- |
| 无 | 地图创建失败 ｜ |
| 0 | 成功 ｜ |
| [-100, -500] ｜ 服务器鉴权错误 |  |
| 1000 ｜ 网络链路错误 |  |
| 1001 ｜ 内部错误 |  |
| 1400001 ｜ 欠费 |  |

---

### canvas

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| type | string |  | 否 | 指定 canvas 类型，支持 2d (2.9.0) 和 webgl (2.7.0) | [2.7.0](../framework/compatibility.html) |
| canvas-id | string |  | 否 | canvas 组件的唯一标识符，若指定了 type 则无需再指定该属性 | [1.0.0](../framework/compatibility.html) |
| disable-scroll | boolean | false | 否 | 当在 canvas 中移动时且有绑定手势事件时，禁止屏幕滚动以及下拉刷新 | [1.0.0](../framework/compatibility.html) |
| bindtouchstart | eventhandle |  | 否 | 手指触摸动作开始 | [1.0.0](../framework/compatibility.html) |
| bindtouchmove | eventhandle |  | 否 | 手指触摸后移动 | [1.0.0](../framework/compatibility.html) |
| bindtouchend | eventhandle |  | 否 | 手指触摸动作结束 | [1.0.0](../framework/compatibility.html) |
| bindtouchcancel | eventhandle |  | 否 | 手指触摸动作被打断，如来电提醒，弹窗 | [1.0.0](../framework/compatibility.html) |
| bindlongtap | eventhandle |  | 否 | 手指长按 500ms 之后触发，触发了长按事件后进行移动不会触发屏幕的滚动 | [1.0.0](../framework/compatibility.html) |
| binderror | eventhandle |  | 否 | 当发生错误时触发 error 事件，detail = {errMsg} | [1.0.0](../framework/compatibility.html) |

---

### ad

基础库 1.9.94 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/ad.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | unit-id | string |  | 是 | 广告单元id，可在[小程序管理后台](https://mp.weixin.qq.com)的流量主模块新建 | [1.9.94](../framework/compatibility.html) |
|  | ad-intervals | number |  | 否 | 广告自动刷新的间隔时间，单位为秒，参数值必须大于等于30（该参数不传入时 Banner 广告不会自动刷新） | [2.3.1](../framework/compatibility.html) |
|  | ad-type | string | banner | 否 | 广告类型，默认为展示banner，可通过设置该属性为`video`展示视频广告, `grid`为格子广告 | [2.8.0](../framework/compatibility.html) |
|  | ad-theme | string | white | 否 |  | [2.8.0](../framework/compatibility.html) |
|  | bindload | eventhandle |  | 否 | 广告加载成功的回调 | [2.2.1](../framework/compatibility.html) |
|  | binderror | eventhandle |  | 否 | 广告加载失败的回调，event.detail = {errCode: 1002} | [2.2.1](../framework/compatibility.html) |
|  | bindclose | eventhandle |  | 否 | 广告关闭的回调 | [2.6.5](../framework/compatibility.html) |

**通用属性**

| 代码 | 异常情况 | 理由 | 解决方案 |
| --- | --- | --- | --- |
| 1000 | 后端错误调用失败 | 该项错误不是开发者的异常情况 | 一般情况下忽略一段时间即可恢复。 |
| 1001 | 参数错误 | 使用方法错误 | 可以前往developers.weixin.qq.com确认具体教程（小程序和小游戏分别有各自的教程，可以在顶部选项中，“设计”一栏的右侧进行切换。 |
| 1002 | 广告单元无效 | 可能是拼写错误、或者误用了其他APP的广告ID | 请重新前往mp.weixin.qq.com确认广告位ID。 |
| 1003 | 内部错误 | 该项错误不是开发者的异常情况 | 一般情况下忽略一段时间即可恢复。 |
| 1004 | 无适合的广告 | 广告不是每一次都会出现，这次没有出现可能是由于该用户不适合浏览广告 | 属于正常情况，且开发者需要针对这种情况做形态上的兼容。 |
| 1005 | 广告组件审核中 | 你的广告正在被审核，无法展现广告 | 请前往mp.weixin.qq.com确认审核状态，且开发者需要针对这种情况做形态上的兼容。 |
| 1006 | 广告组件被驳回 | 你的广告审核失败，无法展现广告 | 请前往mp.weixin.qq.com确认审核状态，且开发者需要针对这种情况做形态上的兼容。 |
| 1007 | 广告组件被封禁 | 你的广告能力已经被封禁，封禁期间无法展现广告 | 请前往mp.weixin.qq.com确认小程序广告封禁状态。 |
| 1008 | 广告单元已关闭 | 该广告位的广告能力已经被关闭 | 请前往mp.weixin.qq.com重新打开对应广告位的展现。 |

---

### ad-custom

基础库 2.10.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/ad-custom.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| unit-id | string |  | 是 | 广告单元id，可在[小程序管理后台](https://mp.weixin.qq.com)的流量主模块新建 | [2.10.4](../framework/compatibility.html) |
| ad-intervals | number |  | 否 | 广告自动刷新的间隔时间，单位为秒，参数值必须大于等于30（该参数不传入时 模板 广告不会自动刷新） | [2.10.4](../framework/compatibility.html) |
| bindload | eventhandle |  | 否 | 广告加载成功的回调 | [2.10.4](../framework/compatibility.html) |
| binderror | eventhandle |  | 否 | 广告加载失败的回调，event.detail = {errCode: 1002} | [2.10.4](../framework/compatibility.html) |

**属性说明**

| 代码 | 异常情况 | 理由 | 解决方案 |
| --- | --- | --- | --- |
| 1000 | 后端错误调用失败 | 该项错误不是开发者的异常情况 | 一般情况下忽略一段时间即可恢复。 |
| 1001 | 参数错误 | 使用方法错误 | 可以前往developers.weixin.qq.com确认具体教程（小程序和小游戏分别有各自的教程，可以在顶部选项中，“设计”一栏的右侧进行切换。 |
| 1002 | 广告单元无效 | 可能是拼写错误、或者误用了其他APP的广告ID | 请重新前往mp.weixin.qq.com确认广告位ID。 |
| 1003 | 内部错误 | 该项错误不是开发者的异常情况 | 一般情况下忽略一段时间即可恢复。 |
| 1004 | 无适合的广告 | 广告不是每一次都会出现，这次没有出现可能是由于该用户不适合浏览广告 | 属于正常情况，且开发者需要针对这种情况做形态上的兼容。 |
| 1005 | 广告组件审核中 | 你的广告正在被审核，无法展现广告 | 请前往mp.weixin.qq.com确认审核状态，且开发者需要针对这种情况做形态上的兼容。 |
| 1006 | 广告组件被驳回 | 你的广告审核失败，无法展现广告 | 请前往mp.weixin.qq.com确认审核状态，且开发者需要针对这种情况做形态上的兼容。 |
| 1007 | 广告组件被驳回 | 你的广告能力已经被封禁，封禁期间无法展现广告 | 请前往mp.weixin.qq.com确认小程序广告封禁状态。 |
| 1008 | 广告单元已关闭 | 该广告位的广告能力已经被关闭 | 请前往mp.weixin.qq.com重新打开对应广告位的展现。 |

---

### official-account

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/official-account.html

**Tips**

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| bindload | EventHandle | 组件加载成功时触发 |
| binderror | EventHandle | 组件加载失败时触发 |

**detail 对象**

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| status | Number | 状态码 |
| errMsg | String | 错误信息 |

**detail 对象**

| 值 | 说明 |
| --- | --- |
| -2 | 网络错误 |
| -1 | 数据解析错误 |
| 0 | 加载成功 |
| 1 | 小程序关注公众号功能被封禁 |
| 2 | 关联公众号被封禁 |
| 3 | 关联关系解除或未选中关联公众号 |
| 4 | 未开启关注公众号功能 |
| 5 | 场景值错误 |
| 6 | 重复创建 |

---

### official-account-publish

基础库 3.9.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/official-account-publish.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| topic | string |  | 否 | 话题名称，最多20字，默认使用小程序名称 | [3.9.3](../framework/compatibility.html) |
| limit | number | 4 | 否 | 小程序页面内最多展示的贴图数量，超出后剩余的贴图需要点击「查看更多」前往查看 | [3.10.3](../framework/compatibility.html) |
| path | string |  | 否 | 发表贴图后，点击来源小程序跳转的页面 | [3.11.1](../framework/compatibility.html) |
| background-color | color | #f7f7f7 | 否 | 贴图组件的背景颜色 | [3.9.3](../framework/compatibility.html) |
| color-unity | boolean | false | 否 | 是否需要色彩统一，话题名称颜色和贴图卡片背景颜色是否对齐 | [3.9.3](../framework/compatibility.html) |
| placeholder | string | 来写下第一条吧 | 否 | 无内容时的占位文案 | [3.10.2](../framework/compatibility.html) |
| recommend-link | string |  | 否 | 贴图链接卡片字段，暂时只支持小程序短链 | [3.16.0](../framework/compatibility.html) |
| show-related | boolean | true | 否 | 是否展示相关内容 | [3.16.0](../framework/compatibility.html) |
| binderror | eventhandle |  | 否 | 列表拉取失败时触发 | [3.9.3](../framework/compatibility.html) |
| bindempty | eventhandle |  | 否 | 列表拉取为空时触发 | [3.9.3](../framework/compatibility.html) |
| bindpublishsuccess | eventhandle |  | 否 | 发表成功时触发，在e.detail中可获取发表的贴图链接postUrl（只有在真正发表完成后链接才可访问） | [3.11.3](../framework/compatibility.html) |
| bindpublishfail | eventhandle |  | 否 | 发表失败时触发 | [3.11.3](../framework/compatibility.html) |

---

### open-data

用户信息相关功能已进行调整，详见小程序用户信息相关接口调整公告

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/open-data.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | type | string |  | 否 | 开放数据类型 | [1.4.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | groupName | 拉取群名称 | [1.4.0](../framework/compatibility.html) | | userNickName | 用户昵称。不再返回，展示“微信用户” | [1.9.90](../framework/compatibility.html) | | userAvatarUrl | 用户头像。不再返回，展示 [灰色头像](https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0) | [1.9.90](../framework/compatibility.html) | | userGender | 用户性别。不再返回，将展示为空（“”） | [1.9.90](../framework/compatibility.html) | | userCity | 用户所在城市。不再返回，将展示为空（“”） | [1.9.90](../framework/compatibility.html) | | userProvince | 用户所在省份。不再返回，将展示为空（“”） | [1.9.90](../framework/compatibility.html) | | userCountry | 用户所在国家。不再返回，将展示为空（“”） | [1.9.90](../framework/compatibility.html) | | userLanguage | 用户的语言。不再返回，将展示为空（“”） | [1.9.90](../framework/compatibility.html) | | | | | | |
|  | open-gid | string |  | 否 | 当 type="groupName" 时生效, 群id | [1.4.0](../framework/compatibility.html) |
|  | lang | string | en | 否 | 当 type="user\*" 时生效，以哪种语言展示 userInfo | [1.4.0](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | en | 英文 | | zh\_CN | 简体中文 | | zh\_TW | 繁体中文 | | | | | | |
|  | default-text | string |  | 否 | 数据为空时的默认文案 | [2.8.1](../framework/compatibility.html) |
|  | default-avatar | string |  | 否 | 用户头像为空时的默认图片，支持相对路径和网络图片路径 | [2.8.1](../framework/compatibility.html) |
|  | binderror | eventhandle |  | 否 | 群名称或用户信息为空时触发 | [2.8.1](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| groupName | 拉取群名称 | [1.4.0](../framework/compatibility.html) |
| userNickName | 用户昵称。不再返回，展示“微信用户” | [1.9.90](../framework/compatibility.html) |
| userAvatarUrl | 用户头像。不再返回，展示 [灰色头像](https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0) | [1.9.90](../framework/compatibility.html) |
| userGender | 用户性别。不再返回，将展示为空（“”） | [1.9.90](../framework/compatibility.html) |
| userCity | 用户所在城市。不再返回，将展示为空（“”） | [1.9.90](../framework/compatibility.html) |
| userProvince | 用户所在省份。不再返回，将展示为空（“”） | [1.9.90](../framework/compatibility.html) |
| userCountry | 用户所在国家。不再返回，将展示为空（“”） | [1.9.90](../framework/compatibility.html) |
| userLanguage | 用户的语言。不再返回，将展示为空（“”） | [1.9.90](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| en | 英文 |
| zh\_CN | 简体中文 |
| zh\_TW | 繁体中文 |

**Skyline 特有属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | type | string |  | 否 | 开放数据类型 | [3.7.11](../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | groupName | 拉取群名称 | [3.7.11](../framework/compatibility.html) | | | | | | |
|  | default-text | string |  | 否 | 数据为空时的默认文案 | [3.7.11](../framework/compatibility.html) |

**Skyline 特有属性**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| groupName | 拉取群名称 | [3.7.11](../framework/compatibility.html) |

---

### store-coupon

基础库 3.8.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/store-coupon.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| appid | string |  | 是 | 小店appid。获取方式：[小店后台](https://store.weixin.qq.com/shop/setting/home) - 店铺管理 - 基础信息 - 账号信息 - 微信小店ID。 |  |
| coupon-id | string |  | 是 | 优惠券id。获取小店优惠券id，可以通过[小店后台](https://store.weixin.qq.com/shop/marketing/coupon) - 营销中心 - 优惠券。 |  |
| custom-style | object |  | 否 | 自定义样式。支持自定义的样式请查看custom-style。 |  |
| promoter-share-link | string |  | 否 | 推客参数。对于「机构推广券」类型优惠券，通过该参数，支持推客染色，可以通过[接口](https://developers.weixin.qq.com/doc/store/leagueheadsupplier/API/promotion/content/coupon/getcouponpromotersharelink.html)获取。 | [3.8.11](../framework/compatibility.html) |
| bindentersuccess | eventhandle |  | 否 | 跳转小店成功的回调。 |  |
| bindentererror | eventhandle |  | 否 | 跳转小店失败的回调，event.detail={code,message}。 |  |

**自定义样式(custom-style)**

| 键名 | 说明 | 允许自定义的属性 |
| --- | --- | --- |
| card | 卡片样式 | background-color、width |
| discount-fee | 折扣金额样式（左上角） | color |
| coupon-type | 优惠券类型样式（左下角） | color |
| condition-text | 优惠使用条件样式（右上角） | color |
| valid-time | 优惠有效时间样式（右上角） | color |
| coupon-button | 优惠领取按钮样式 | border-radius、color、background-color |
| coupon-text-disabled | 优惠已领取状态样式 | color |
| coupon-footer-line | 卡片底部分割线样式 | background-color |
| coupon-shop-icon | 卡片底部logo icon样式 | fill、fill-opacity |
| coupon-shop-nickname | 卡片底部店铺昵称样式 | color |

**detail 对象**

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| code | Number | 状态码 |
| message | String | 错误信息 |

**detail 对象**

| 值 | 说明 |
| --- | --- |
| -1 | 系统失败，请重试 |
| 0 | 成功 |
| 109114、268542430 | 优惠券券不存在 |
| 109119 | 该类型优惠券不支持在小程序发放 |

---

### store-gift

基础库 3.8.10 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/store-gift.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| present-order-id | string |  | 是 | 礼物订单id，调用“创建并发送礼物”或通过“查询礼物订单列表”open api拿到，[open api文档链接](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/cooperation_shop/activity_present_cooperation_shop.html)。 | [3.8.10](../framework/compatibility.html) |
| open-id | string |  | 是 | 用户openid。 | [3.8.10](../framework/compatibility.html) |
| show-gift-card | boolean | true | 否 | 控制是否展示礼物卡片，默认展示礼物卡片。 | [3.8.10](../framework/compatibility.html) |
| bindsuccess | eventhandle |  | 否 | 打开礼物成功的回调，event.detail={code,message}。【新特性支持】微信iOS / Android版本>=8.0.61、鸿蒙版本>=8.0.15，支持在成功打开礼物并回到小程序时，触发成功回调。 | [3.8.10](../framework/compatibility.html) |
| binderror | eventhandle |  | 否 | 打开礼物失败的回调，event.detail={code,message}。 | [3.8.10](../framework/compatibility.html) |

**detail 对象**

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| code | Number | 状态码 |
| message | String | 错误信息 |

**detail 对象**

| 值 | 含义 | 备注 |
| --- | --- | --- |
| -1001 | 打开礼物失败[参数错误] | 代表调用组件的传参有误 |
| -1003 | 打开礼物失败 | 调用客户端jsapi失败，是因为客户端是测试包不支持jsapi所致 |
| -1004 | 正在loading无法打开礼物 | 正在获取礼物订单信息中，可提醒用户稍后再试 |
| -1005 | 当前客户端版本不支持礼物领取 |  |

---

### store-home

基础库 3.5.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/store-home.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| appid | string |  | 是 | 小店appid。获取方式：[小店后台](https://store.weixin.qq.com/shop/setting/home) - 店铺管理 - 基础信息 - 账号信息 - 微信小店ID。 |

---

### store-product

基础库 3.5.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/store-product.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | appid | string |  | 是 | 小店appid。获取方式：[小店后台](https://store.weixin.qq.com/shop/setting/home) - 店铺管理 - 基础信息 - 账号信息 - 微信小店ID。 | [3.5.5](../framework/compatibility.html) |
|  | product-id | string |  | 是 | 商品id。获取小店商品id，可以通过API获取([参考链接](https://developers.weixin.qq.com/doc/store/API/product/get.html))或通过[小店后台](https://store.weixin.qq.com/shop/goods/list) - 商品管理 - 商品列表 - 规格/编码获取。 | [3.5.5](../framework/compatibility.html) |
|  | product-promotion-link | string |  | 否 | 带货商品跟佣信息。若需要商品售卖时使用小店优选联盟带货跟佣功能，可以通过API获取带货商品跟佣信息([参考链接](https://developers.weixin.qq.com/doc/channels/API/windowproduct/get.html))。 | [3.5.5](../framework/compatibility.html) |
|  | media-id | string |  | 否 | 媒体文件id。可以通过API获取([参考链接](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/cooperation_shop/upload.html#%E4%B8%80%E3%80%81%E4%B8%8A%E4%BC%A0%E8%B5%84%E6%96%99))。 | [3.7.1](../framework/compatibility.html) |
|  | custom-style | object |  | 否 | 自定义样式。支持自定义的样式请查看custom-style。 | [3.7.1](../framework/compatibility.html) |
|  | custom-content | boolean | false | 否 | 开启自定义插槽。开启后可自行控制卡片内容。 | [3.7.2](../framework/compatibility.html) |
|  | open-page | string | product-detail | 否 | 设置点击打开的页面(同时开启 custom-content 属性后生效)。 | [3.7.4](../framework/compatibility.html) |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | product-detail | 商品详情页 | [3.7.4](../framework/compatibility.html) | | gift-product-detail | 送礼商品详情页 | [3.7.7](../framework/compatibility.html) | | buy | 下单页，只能支持「热招品牌且关联小店」商家 | [3.7.4](../framework/compatibility.html) | | gift | 送礼下单页，只能支持「热招品牌且关联小店」商家 | [3.15.1](../framework/compatibility.html) | | | | | | |
|  | logo-position | string | bottom-left | 否 | 设置小店标识的位置，不允许隐藏(同时开启 custom-content 属性后生效)。 | [3.7.2](../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | bottom-left | 左下方 | | bottom-right | 右下方 | | | | | | |
|  | bindentersuccess | eventhandle |  | 否 | 跳转小店成功的回调。 | [3.7.1](../framework/compatibility.html) |
|  | bindentererror | eventhandle |  | 否 | 跳转小店失败的回调，event.detail={code,message}。 | [3.7.1](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| product-detail | 商品详情页 | [3.7.4](../framework/compatibility.html) |
| gift-product-detail | 送礼商品详情页 | [3.7.7](../framework/compatibility.html) |
| buy | 下单页，只能支持「热招品牌且关联小店」商家 | [3.7.4](../framework/compatibility.html) |
| gift | 送礼下单页，只能支持「热招品牌且关联小店」商家 | [3.15.1](../framework/compatibility.html) |

**通用属性**

| 合法值 | 说明 |
| --- | --- |
| bottom-left | 左下方 |
| bottom-right | 右下方 |

**自定义样式(custom-style)**

| 键名 | 说明 | 允许自定义的属性 |
| --- | --- | --- |
| card | 卡片样式 | background-color |
| title | 标题样式 | color |
| price | 价格样式 | color |
| buy-button | 购买按钮样式 | width、border-radius、color、background-color |
| buy-button-disabled | 购买按钮禁用态样式 | width、border-radius、color、background-color |

**detail 对象**

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| code | Number | 状态码 |
| message | String | 错误信息 |

**detail 对象**

| 值 | 说明 |
| --- | --- |
| -1 | 系统失败，请重试 |
| 0 | 成功 |
| 10001 | 无效的media-id |
| 10002 | 无效的media-id |
| 10003 | 文件正在上传中，请等待 |
| 10004 | 上传的文件存在风险，请重新上传 |
| 20001 | 该商品因违规已下架 |
| 60001 | 正在加载中 |
| 60002 | 正在渲染中 |
| 60004 | 加载异常 |
| 60005 | 加载失败 |

---

### web-view

基础库 1.6.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/web-view.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| src | string |  | 否 | webview 指向网页的链接。可打开关联的公众号的文章，其它网页需登录[小程序管理后台](https://mp.weixin.qq.com/)配置业务域名。 | [1.6.4](../framework/compatibility.html) |
| bindmessage | eventhandler |  | 否 | 网页向小程序 postMessage 时，会在以下特定时机触发并收到消息：小程序后退、组件销毁、分享、复制链接（[2.31.1](../framework/compatibility.html)）。e.detail = { data }，data是多次 postMessage 的参数组成的数组。 | [1.6.4](../framework/compatibility.html) |
| bindload | eventhandler |  | 否 | 网页加载成功时候触发此事件。e.detail = { src } | [1.6.4](../framework/compatibility.html) |
| binderror | eventhandler |  | 否 | 网页加载失败的时候触发此事件。e.detail = { url, fullUrl }，其中 fullUrl 为加载失败时的完整 url | [1.6.4](../framework/compatibility.html) |

**相关接口 1**

| 接口名 | 说明 | 最低版本 |
| --- | --- | --- |
| wx.miniProgram.navigateTo | 参数与小程序接口一致 | [1.6.4](../framework/compatibility.html) |
| wx.miniProgram.navigateBack | 参数与小程序接口一致 | [1.6.4](../framework/compatibility.html) |
| wx.miniProgram.switchTab | 参数与小程序接口一致 | [1.6.5](../framework/compatibility.html) |
| wx.miniProgram.reLaunch | 参数与小程序接口一致 | [1.6.5](../framework/compatibility.html) |
| wx.miniProgram.redirectTo | 参数与小程序接口一致 | [1.6.5](../framework/compatibility.html) |
| wx.miniProgram.postMessage | 向小程序发送消息，会在以下特定时机触发组件的message事件：小程序后退、组件销毁、分享、复制链接（[2.31.1](../framework/compatibility.html)） | [1.7.1](../framework/compatibility.html) |
| wx.miniProgram.getEnv | 获取当前环境 | [1.7.1](../framework/compatibility.html) |

**相关接口 2**

| 接口模块 | 接口说明 | 具体接口 | 鸿蒙 OS 支持情况 |
| --- | --- | --- | --- |
| 判断客户端是否支持js |  | checkJSApi | ✓ |
| 图像接口 | 拍照或上传 | chooseImage | ✓ |
|  | 预览图片 | previewImage | ✓ |
|  | 上传图片 | uploadImage | ✓ |
|  | 下载图片 | downloadImage | ✓ |
|  | 获取本地图片 | getLocalImgData | ✓ |
| 音频接口 | 开始录音 | startRecord |  |
|  | 停止录音 | stopRecord |  |
|  | 监听录音自动停止 | onVoiceRecordEnd |  |
|  | 播放语音 | playVoice |  |
|  | 暂停播放 | pauseVoice |  |
|  | 停止播放 | stopVoice |  |
|  | 监听语音播放完毕 | onVoicePlayEnd |  |
|  | 上传接口 | uploadVoice |  |
|  | 下载接口 | downloadVoice |  |
| 智能接口 | 识别音频 | translateVoice |  |
| 设备信息 | 获取网络状态 | getNetworkType | ✓ |
| 地理位置 | 使用内置地图打开地点 | openLocation | ✓ |
|  | 获取地理位置 | getLocation | ✓ |
| 摇一摇周边 | 开启ibeacon | startSearchBeacons |  |
|  | 关闭ibeacon | stopSearchBeacons |  |
|  | 监听ibeacon | onSearchBeacons |  |
| 微信扫一扫 | 调起微信扫一扫 | scanQRCode | ✓ |
| 微信卡券 | 拉取使用卡券列表 | chooseCard |  |
|  | 批量添加卡券接口 | addCard |  |
|  | 查看微信卡包的卡券 | openCard |  |
| 长按识别 | 小程序圆形码 | 无 | ✓ |

---

### native-component

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/native-component.html

---

### aria-component

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/aria-component.html

**无障碍访问**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| aria-activedescendant | aria-atomic | aria-autocomplete | aria-busy | aria-checked |
| aria-colcount | aria-colindex | aria-colspan | aria-controls | aria-current |
| aria-describedby | aria-details | aria-disabled | aria-dropeffect | aria-errormessage |
| aria-expanded | aria-flowto | aria-grabbed | aria-haspopup | aria-hidden |
| aria-invalid | aria-keyshortcuts | aria-label | aria-labelledby | aria-level |
| aria-live | aria-modal | aria-multiline | aria-multiselectable | aria-orientation |
| aria-owns | aria-placeholder | aria-posinset | aria-pressed | aria-readonly |
| aria-relevant | aria-required | aria-role | aria-roledescription | aria-rowcount |
| aria-rowindex | aria-rowspan | aria-selected | aria-setsize | aria-sort |
| aria-valuemax | aria-valuemin | aria-valuenow | aria-valuetext |  |

---

### navigation-bar

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/navigation-bar.html

**属性说明**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| title | string |  | 否 | 导航条标题 | [2.9.0](../framework/compatibility.html) |
| loading | boolean | false | 否 | 是否在导航条显示 loading 加载提示 | [2.9.0](../framework/compatibility.html) |
| front-color | string |  | 否 | 导航条前景颜色值，包括按钮、标题、状态栏的颜色，仅支持 `#ffffff` 和 `#000000` | [2.9.0](../framework/compatibility.html) |
| background-color | string |  | 否 | 导航条背景颜色值，有效值为十六进制颜色 | [2.9.0](../framework/compatibility.html) |
| color-animation-duration | number | 0 | 否 | 改变导航栏颜色时的动画时长，默认为 `0` （即没有动画效果） | [2.9.0](../framework/compatibility.html) |
| color-animation-timing-func | string | "linear" | 否 | 改变导航栏颜色时的动画方式，支持 `linear` 、 `easeIn` 、 `easeOut` 和 `easeInOut` | [2.9.0](../framework/compatibility.html) |

---

### page-meta

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/page-meta.html

**通用属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | background-text-style | string |  | 否 | 下拉背景字体、loading 图的样式，仅支持 `dark` 和 `light` | [2.9.0](../framework/compatibility.html) |
|  | background-color | string |  | 否 | 窗口的背景色，必须为十六进制颜色值 | [2.9.0](../framework/compatibility.html) |
|  | background-color-top | string |  | 否 | 顶部窗口的背景色，必须为十六进制颜色值，仅 iOS 支持 | [2.9.0](../framework/compatibility.html) |
|  | background-color-bottom | string |  | 否 | 底部窗口的背景色，必须为十六进制颜色值，仅 iOS 支持 | [2.9.0](../framework/compatibility.html) |
|  | root-background-color | string |  | 否 | 页面内容的背景色，用于页面中的空白部分和页面大小变化 resize 动画期间的临时空闲区域 | [2.12.1](../framework/compatibility.html) |
|  | page-style | string | "" | 否 | 页面根节点样式，页面根节点是所有页面节点的祖先节点，相当于 HTML 中的 body 节点 | [2.9.0](../framework/compatibility.html) |
|  | page-font-size | string | "" | 否 | 页面 page 的字体大小，可以设置为 `system` ，表示使用当前用户设置的微信字体大小 | [2.11.0](../framework/compatibility.html) |
|  | root-font-size | string | "" | 否 | 页面的根字体大小，页面中的所有 rem 单位，将使用这个字体大小作为参考值，即 `1rem` 等于这个字体大小；自小程序版本 2.11.0 起，也可以设置为 `system` | [2.9.0](../framework/compatibility.html) |
|  | page-orientation | string | "" | 否 | 页面的方向，可为 `auto` `portrait` 或 `landscape` | [2.12.0](../framework/compatibility.html) |
|  | bindresize | eventhandle |  | 否 | 页面尺寸变化时会触发 `resize` 事件， `event.detail = { size: { windowWidth, windowHeight } }` | [2.9.0](../framework/compatibility.html) |

**WebView 特有属性**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | scroll-top | string | "" | 否 | 滚动位置，可以使用 px 或者 rpx 为单位，在被设置时，页面会滚动到对应位置 | [2.9.0](../framework/compatibility.html) |
|  | scroll-duration | number | 300 | 否 | 滚动动画时长 | [2.9.0](../framework/compatibility.html) |
|  | bindscroll | eventhandle |  | 否 | 页面滚动时会触发 `scroll` 事件， `event.detail = { scrollTop }` | [2.9.0](../framework/compatibility.html) |
|  | bindscrolldone | eventhandle |  | 否 | 如果通过改变 `scroll-top` 属性来使页面滚动，页面滚动结束后会触发 `scrolldone` 事件 | [2.9.0](../framework/compatibility.html) |

---

### 组件

组件Component用于实现xr-frame中所有的逻辑，以生命周期拉驱动。它们在wxml中对应于每个标签上的属性，比如<xr-element transform="position: 1 1 1;" />，就是在xr-element标签上挂在了一个transform组件。组件的聚合构成了后面章节的元素，也就是wxml中对应的标签。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/core/component.html

---

### 组件数据解析

在组件一章我们知道需要有一个解析器将xml中组件对应属性的字符串转换为组件需要的数据类型，对此，框架提供了一套机制来处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/core/data-values.html

**非资源数据**

| 类型 | 例子 | 转换 | 说明 |
| --- | --- | --- | --- |
| string | henshin: KuugaAgitoRyuki FaziBladeHibikiKabutoDenOkiva DecadeWOOOFourzeWizardGaim DriveGhostExaidbuildGrandZio | 'KuugaAgitoRyuki FaziBladeHibikiKabutoDenOkiva DecadeWOOOFourzeWizardGaim DriveGhostExaidbuildGrandZio' | 字符串，不作任何处理 |
| number | truth:42 | 42 | 数字，会转成float，支持其他进制如`0xff`、`0b11` |
| boolean | yiyandingzhen:false | false | 布尔，当写'false'时为`false`，否则均为`true`(包括不写值) |
| array | producer:wowaka neru kurogaki | ['wowaka','neru','kurogaki'] | 字符串数组，用空格分割 |
| number-array | idolOffice:7 6 5 | [7,6,5] | 数字数组，用空格分割 |
| color | rem:0.57 0.75 1 1 | [0.57,0.75,1,1] | 颜色，rgba，也可以使用`#fff`这种方式 |
| map | cat:10,dog:8,fox:6 | [['cat',10],['dog',8],['fox',6]] | 映射形式是`key:value`，用`,`分割 |
| dict | camp:瞬光:混乱善良,roam:中立善良,xinyi:绝对中立 | {瞬光:'混乱善良',roam:'中立善良',xinyi:'绝对中立'} | 字典，和`map`类型写起来一样，转换结果不同 |
| transform | target:homo | `nodeId`为homo的Transform组件引用 | 变换，可以用于索引标记过`nodeId`的变换组件 |

---

### 元素

元素Element本身没有逻辑，其主要负责两部分——组件的聚合和属性代理。所以在阅读以下内容之前，请保证先阅读了组件的相关内容。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/core/element.html

---

### 事件

事件管理器从属于元素，提供给组件的设计者一个向使用者派发事件的手段。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/core/event.html

---

### 场景

场景Scene是一种特殊的元素，对于所有的xr-frame小程序组件，其最外层必须有一个xr-scene标签作为根元素，并且组件内只能有一个，以此作为整个组件的基础。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/core/scene.html

**事件**

| 事件 | 参数 | 立即 | wxml | 时机 |
| --- | --- | --- | --- | --- |
| ready | 无 | 是 | 是 | 场景第一次解析完毕 |
| tick | 数字，`delta`(ms) | 是 | 是 | 一帧驱动开始 |
| pause | 无 | 是 | 是 | 场景暂停，一般是是压后台 |
| resume | 无 | 是 | 是 | 场景恢复，一般是从后台唤醒 |

---

### 节点

元素虽然有很多派生，但本质上可以分为两类——3D节点和非3D节点（简称节点）。节点Node对应的标签是xr-node，它是场景中用于渲染的元素的基础，本质上是在基础元素的基础上默认添加了Transform变换组件。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/core/node.html

---

### Shadow元素

有时候我们需要用代码动态创建元素之后添加到场景中，这个需求和wxml写标签这种静态的模板编译方式是冲突的，为了保证DOM树不混乱，我们提供了类似于HTML中的ShadowRoot的XRShadow元素，对应于xml中的xr-shadow标签，来解决这个问题。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/core/shadow.html

---

### Slot

在某些场合，我们希望使用和小程序UI组件一致的slot能力来做一些灵活的封装，解决复用。xr-frame同样支持slot，但在具体的用法上用一些限制，下面就让我们通过一个例子教大家使用。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/core/slot.html

---

### 资源加载器

xr-frame允许开发者定制资源加载器，来添加自己所需的资源类型。所有的资源加载器都需要派生自AssetLoader类，然后使用上一章的方法在xml中或者手动使用。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/assets/loader.html

---

### 资源加载元素

在资源系统一章中我们简略提到了几个xml中和资源相关的标签xr-assets、xr-asset-load等，这一章就来详细介绍一下它们。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/assets/elements.html

**事件**

| 事件 | 参数 | 立即 | wxml | 时机 |
| --- | --- | --- | --- | --- |
| progress | 对象，进度`progress`，和当前资源描述`asset` | 是 | 是 | 场景第一次解析完毕 |
| loaded | 对象，成功的资源`assets`，和出的错误`errors` | 是 | 是 | 场景销毁之前 |

---

### 几何数据

渲染的基础之一是几何数据Geometry资源，它描述了一个模型的顶点信息、索引信息以及顶点的存取结构。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/render/geometry.html

---

### 效果

几何数据提供了渲染的原材料，材质决定了渲染的方式，但在讨论材质之前，我们要讨论一下其基于的效果Effect。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/render/effect.html

---

### 材质

材质Material基于效果 Effect，提供了修改渲染状态、Uniforms的接口，真正决定了物体最后的渲染方式，体现为物体表面的外观。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/render/material.html

**材质支持渲染状态列表**

| 状态名称 | 说明 | 类型 |
| --- | --- | --- |
| renderQueue | 渲染顺序 | number |
| cullOn | 是否开启剔除 | bool |
| depthTestOn | 是否开启深度测试 | bool |
| depthTestWrite | 是否开启深度写入 | bool |
| alphaMode | 透明模式 | 'OPAQUE' 'BLEND' 'MASK' |
| alphaCutOff | 是否开启透明剔除 | bool |
| depthTestComp | 深度测试方法 | number, [ECompareFunc](./../../../api/xr-frame/enums/ECompareFunc.html)对应的值 |
| stencilTestOn | 是否开启模板测试 | boolean |
| stencilComp | 模板测试相关 | number, [ECompareFunc](./../../../api/xr-frame/enums/ECompareFunc.html)对应的值 |
| stencilRef | 模板测试相关 | number |
| stencilReadMask | 模板测试相关 | number |
| stencilWriteMask | 模板测试相关 | number |
| stencilPass | 模板测试相关 | number, [EStencilOp](./../../../api/xr-frame/enums/EStencilOp.html)对应的值 |
| stencilFail | 模板测试相关 | number, [EStencilOp](./../../../api/xr-frame/enums/EStencilOp.html)对应的值 |
| stencilZFail | 模板测试相关 | number, [EStencilOp](./../../../api/xr-frame/enums/EStencilOp.html)对应的值 |
| colorWrite | 颜色通道写入掩码，基础库`v2.31.1开始支持` | number, 一个4bits的mask，由高到低为`ABGR`四个通道，比如`0b1001`表示只开启`R`和`A`通道写入 |

---

### 网格

网格Mesh是一种组件，严格来讲应该称为网格渲染器，但出于精简就这么命名了。其作用是组织起几何数据和材质实现渲染的载体。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/render/mesh.html

---

### 纹理

纹理Texture是GPU中的图像，供着色器采样使用。在框架中其一般被作为材质的一部uniforms使用。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/render/texture.html

---

### 相机

相机Camera是渲染系统最核心的组件之一，和几乎所有的渲染引擎一样，它真正驱动着整个渲染管线的运作。相机组件一般被代理到相机元素XRCamera中使用，其派生自XRNode，对应在xml中的标签为xr-camera。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/render/camera.html

---

### 渲染纹理

相机一章中提到了渲染目标renderTarget可以指定为渲染纹理，纹理也提到了渲染纹理可以作为纹理使用。可见，渲染纹理RenderTexture就是连接多个相机渲染之间的桥梁。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/render/render-texture.html

---

### 图集

图集Atlas是一种资源，可以优化渲染流程和资源，在业界中用于精灵动画和UI比较多。它将一些散碎的小图拼接为一张大图，加之偏移数据uvMatrix或者uvST，能有效减少渲染时的纹理数量和切换次数。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/render/atlas.html

---

### 环境

环境Env是一种特殊的组件，其一般被代理到元素XREnv上使用。环境用于描述当前场景的环境贴图和光照信息，其一般和相机与材质协作，实现丰富真实的渲染效果。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/render/env.html

**uniforms和宏**

| 类型 | 宏 | 说明 |
| --- | --- | --- |
| 开启环境漫反射 | `WX_USE_IBL_DIFFUSE` | bool |
| 开启环境高光反射 | `WX_USE_IBL_SPECULAR` | bool |
| 高光反射mipmaps数量 | `WX_USE_SPECULAR_MIPMAPS` | int |
| 高光反射使用RGBD | `WX_USE_SPECULAR_RGBD` | bool |

**uniforms和宏**

| 类型 | uniforms | 说明 |
| --- | --- | --- |
| 漫反射系数 | `u_diffuseSH` | vec3[9] |
| 漫反射曝光值 | `u_diffuseExp` | texture2d |
| 高光反射纹理 | `u_specularEnvMap` | texture2d |
| 高光反射曝光值 | `u_specularExp` | v |
| 环境和天空盒旋转 | `u_envRotation` | float |

---

### 灯光

灯光组件Light用于给场景提供照明，也是阴影的核心。相机组件一般被代理到灯光元素XRLight中使用，其派生自XRNode，对应在xml中的标签为xr-light。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/render/light.html

**主光源**

| 类型 | uniforms | 宏 | 说明 |
| --- | --- | --- | --- |
| 环境光 | 颜色和亮度`u_ambientLightColorIns` | 是否开启`WX_USE_AMBIENT_LIGHT` | [r, g, b, ins] |
| 平行光 | 颜色和亮度`u_mainLightColorIns`和方向`u_mainLightDir` | 是否开启`WX_USE_MAIN_DIR_LIGHT` | [r, g, b, ins]/vec3 |

**追加光源**

| 类型 | 宏 | 说明 |
| --- | --- | --- |
| 开启追加光源 | `WX_USE_ADD_LIGHTS` | bool |
| 灯光数量 | `WX_ADD_LIGHTS_COUNT` | int |

**追加光源**

| 类型 | uniforms | 说明 |
| --- | --- | --- |
| 灯光信息 | `u_addLightsInfo` | [type, range, innerConeAngle, outerConeAngle][4] |
| 灯光位置 | `u_addLightsPos` | vec3[4] |
| 灯光方向 | `u_addLightsDir` | vec3[4] |
| 灯光颜色亮度 | `u_addLightsColorIns` | [r, g, b, ins][4] |

**宏和uniforms**

| 类型 | 宏 | 说明 |
| --- | --- | --- |
| 开启接受阴影 | `WX_RECEIVE_SHADOW` | bool |

**宏和uniforms**

| 方法 | 说明 |
| --- | --- |
| `float shadowCalculation(vec3 posWorld)` | 传入世界坐标，返回阴影强度 |

---

### 后处理

后处理一般指一次渲染的最后环节，它接受一个相机的渲染结果，用图像处理算法对结果增强来达到一些效果，比如模糊、辉光、渐晕等等。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/render/post-process.html

---

### GLTF介绍

GLTF是一种被广泛使用的文件格式，用来储存3D模型和3D场景。在xr-frame里你可以非常轻松地引入任意GLTF模型，并将其渲染出来。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/gltf/introduction.html

---

### xr-frame里的GLTF

GLTF模型需要先通过Loader加载进小程序中，才可以渲染。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/gltf/specification.html

**Loader选项**

| 选项名 | 用途 | 备注 |
| --- | --- | --- |
| preserveRaw | 加载完后，在`GLTFModel`资源中保留原始json，保存在`jsonRaw`字段中。 | 可通过`scene.assets.getAsset("gltf", "xxx")`来获取`GLTFModel`资源。 |
| ignoreError | 可用于渲染超出限制的模型。 | 使用方法参考[渲染超出限制的模型](#%E6%B8%B2%E6%9F%93%E8%B6%85%E5%87%BA%E9%99%90%E5%88%B6%E7%9A%84%E6%A8%A1%E5%9E%8B)。 |

**GLTF组件**

| 属性名 | 组件.属性 | 备注 |
| --- | --- | --- |
| model | GLTF.model | 使用的GLTFModel资源，对应`xr-asset-load`标签中的asset-id属性 |
| cast-shadow | GLTF.castShadow | GLTF模型是否投射阴影 |
| receive-shadow | GLTF.receiveShadow | GLTF模型是否接受阴影 |

**GLTF组件**

| 事件名 | 描述 | 事件回调参数 | 备注 |
| --- | --- | --- | --- |
| gltf-loaded | GLTF组件将GLTFModel渲染完毕后触发。 | { target: Element } | - |

**使用TS脚本来修改GLTF**

| 接口名 | 描述 | 备注 |
| --- | --- | --- |
| getInternalNodeByName | 根据GLTFNode节点的`name`字段来获取xr-frame对应的`Element` |  |
| get meshes | 获取生成的所有`Mesh组件` |  |
| [getPrimitivesByNodeName](./../../../api/xr-frame/classes/GLTF.html#getPrimitivesByNodeName) | 根据GLTFNode节点的`name`字段来获取其下的所有`Mesh组件` | 2.28.1版本加入；详见API文档 |
| [getPrimitivesByMeshName](./../../../api/xr-frame/classes/GLTF.html#getPrimitivesByMeshName) | 根据GLTFMesh节点的`name`字段来获取所有相关的`Mesh组件` | 2.28.1版本加入；详见API文档 |

---

### GLTF画廊

*以下图片均为xr-frame渲染截屏，模型来源为gltf官方示例与sketchfab资源（CC-Licensed）。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/gltf/gallery.html

---

### AR追踪器

AR追踪器ARTracker是AR系统的一部分。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/ar/tracker.html

**事件**

| 事件 | 参数 | 立即 | wxml | 时机 |
| --- | --- | --- | --- | --- |
| ar-tracker-state | ARTracker实例，识别状态 | 是 | 是 | 要求基础库v2.29.1及以上，追踪器识别状态切换时，详见上一节 |
| ar-tracker-switch | boolean，识别状态 | 是 | 是 | 追踪器识别状态切换时，识别到了为`true`，否则为`false` |

---

### 帧动画

帧动画是一种内置的动画实现，提供给开发者类似于css动画的能力，去控制一个元素下所有组件的数据。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/animation/keyframe.html

---

### 轮廓

如果想要与场景中的物体进行互动，比如说点击、拖拽物体，那么这个物体得先拥有一个轮廓才行。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/physics/shape.html

**轮廓种类**

| 名称 | 标签属性名 | 组件数据 | 备注 |
| --- | --- | --- | --- |
| 球状轮廓 | sphere-shape | center, radius, autoFit |  |
| 胶囊体轮廓 | capsule-shape | center, radius, height, autoFit |  |
| 长方体轮廓 | cube-shape | center, size, autoFit |  |
| 网格模型轮廓 | mesh-shape | - | 自动适配元素下的Mesh和GLTF模型 |

**轮廓交互**

| 事件名 | 描述 | 事件回调参数 | 备注 |
| --- | --- | --- | --- |
| touch-shape | 点击轮廓时触发 | [IShapeTouchEvent](./../../../api/xr-frame/interfaces/IShapeTouchEvent.html) | 如果有多个物体叠在一起，会点中最上层的。 |
| drag-shape | 点击轮廓后，手指不松开的情况下进行拖拽时触发 | [IShapeDragEvent](./../../../api/xr-frame/interfaces/IShapeDragEvent.html) | 只有在先触发touch-shape之后才会触发这个事件，target和touch-shape保持一致。 |
| untouch-shape | 点击轮廓后，手指松开时触发 | [IShapeTouchEvent](./../../../api/xr-frame/interfaces/IShapeTouchEvent.html) | 只有在先触发touch-shape之后才会触发这个事件。 |

---

### 刚体和全局物理

⚠️刚体物理功能目前尚在Beta阶段，并且需要2.32.1及之后的基础库才能使用。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/physics/rigidbody.html

**全局物理配置**

| 属性名 | 描述 | 值类型 | 备注 |
| --- | --- | --- | --- |
| disabled | 是否禁用物理 | boolean | `disable=true`的话，效果和不存在`<xr-physics>`标签时一致。 |
| gravity | 全局重力 | Vector3 | 默认重力(0, -9.8, 0) |

**刚体配置**

| 属性值 | 描述 | 值类型 | 备注 |
| --- | --- | --- | --- |
| disabled | 是否禁用刚体 | boolean | `disable=true`的话，效果和不存在rigidbody属性时一致。 |
| mass | 刚体质量 | number | mass > 0 |
| useGravity | 是否受重力影响 | boolean |  |
| constraintsMask | 限制刚体在某个轴上的移动 | number | 具体指参考 @TODO |

**刚体组件**

| 方法名 | 描述 | 备注 |
| --- | --- | --- |
| addForce / addTorque | 是否禁用刚体 | 对刚体施加力，产生加速度。 |
| sleep / wakeUp | 强制刚体睡眠/唤醒 | 正常情况下睡眠状态是由物理引擎自动管理的，如果发现刚体异常静止，可以尝试手动wakeUp。 |

---

### 轮廓间交互

⚠️轮廓间交互功能目前尚在Beta阶段，并且需要2.32.1及之后的基础库才能使用。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/physics/interact.html

**组件属性**

| 属性值 | 描述 | 值类型 | 备注 |
| --- | --- | --- | --- |
| disabled | 是否禁用交互 | boolean | `disable=true`的话，效果和不存在shape-interact属性时一致 |
| collide | 是否发生碰撞 | boolean | `collide=true`的话，发生碰撞，否则发生重叠，**默认`false`** |
| bounciness | 弹性系数 | number | 0≤bounciness≤1，仅当`collide=true`时生效 |
| staticFriction | 静摩擦系数 | number | 0≤staticFriction≤1，仅当`collide=true`时生效 |
| dynamicFriction | 动摩擦系数 | number | 0≤staticFriction≤1，仅当`collide=true`时生效 |

**交互事件**

| 事件名 | 描述 | 事件回调参数 |
| --- | --- | --- |
| collide-begin | 发生碰撞 | ICollideEvent |
| collide-persist | 碰撞持续 | ICollideEvent |
| collide-exit | 碰撞结束 | ICollideEvent |
| overlap-begin | 发生重叠 | IOverlapEvent |
| overlap-persist | 重叠持续 | IOverlapEvent |
| overlap-exit | 重叠结束 | IOverlapEvent |

---

### 粒子发射器

粒子系统目前内置了不同形态的发射器类型，通过对相关参数的调整，满足开发者所需要的粒子效果。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/particles/emiter.html

**BoxShapeEmitter 箱形发射器**

| 参数名称 | 类型 | 备注 | 默认值 |
| --- | --- | --- | --- |
| direction | Vector3 | 粒子初始发射方向左区间 | (0, 1.0, 0) |
| direction2 | Vector3 | 粒子初始发射方向右区间 | (0, 1.0, 0) |
| minEmitBox | Vector3 | 粒子初始位置左区间 | (-0.5, -0.5, -0.5) |
| maxEmitBox | Vector3 | 粒子初始位置右区间 | (0.5, 0.5, 0.5) |

**CircleShapeEmitter 圆形发射器**

| 参数名称 | 类型 | 备注 | 默认值 |
| --- | --- | --- | --- |
| radius | number | 粒子随机生成圆形区域的半径 | 1 |
| radiusRange | number | 粒子在圆形区域内的覆盖范围 [0-1] | 0 |
| direction | Vector3 | 粒子初始发射方向左区间 | (0, 1.0, 0) |
| direction2 | Vector3 | 粒子初始发射方向右区间 | (0, 1.0, 0) |
| arc | number | 规定粒子生成的扇形区域角度大小 [0-360] | 360 |

**ConeShapeEmitter 锥形发射器**

| 参数名称 | 类型 | 备注 | 默认值 |
| --- | --- | --- | --- |
| radius | number | 粒子随机生成锥型区域的半径 | 3 |
| radiusRange | number | 粒子在锥型区域内的覆盖范围 [0-1] | 0 |
| heightRange | number | 粒子在高度方向上的覆盖范围 [0-1] | 1 |
| arc | number | 规定粒子生成的扇形区域角度大小 [0-360] | 360 |
| randomizeDirection | number | 粒子发射方向的扰动程度 [0-1] | 0 |

**PointShapeEmitter 点状发射器**

| 参数名称 | 类型 | 备注 | 默认值 |
| --- | --- | --- | --- |
| direction | Vector3 | 粒子初始发射方向左区间 | (0, 1.0, 0) |
| direction2 | Vector3 | 粒子初始发射方向右区间 | (0, 1.0, 0) |

**SphereShapeEmitter 球形发射器**

| 参数名称 | 类型 | 备注 | 默认值 |
| --- | --- | --- | --- |
| radius | number | 粒子随机生成球型区域的半径 | 3 |
| radiusRange | number | 粒子在球型区域内的覆盖范围 [0-1] | 0 |
| arc | number | 规定粒子生成的扇形区域角度大小 [0-360] | 360 |
| randomizeDirection | number | 粒子发射方向的扰动程度 [0-1] | 0 |

**粒子实例相关属性**

| 名称 | 类型 | 备注 |
| --- | --- | --- |
| angle | number | 粒子的偏移角度 |
| color | Vector4 | 粒子颜色 |
| direction | Vector3 | 粒子的运动方向 |
| particleSystem | Particle | 粒子所归属的粒子系统 |
| position | Vector3 | 粒子所处位置 |
| size | number | 粒子大小 |

---

### 其他属性和动画

RenderMode不进行设置的前提下, 无论相机如何的转动，所有粒子永远正对着屏幕。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/particles/attribute.html

**RenderMode字段相关变量介绍**

| 名称 | 备注 |
| --- | --- |
| off | 是否启用Billboard渲染 |
| default | 默认Billboard渲染模式，粒子始终正对屏幕 |
| y | Y轴渲染模式，粒子Y轴将锁定, 其它轴的显示正对屏幕 |
| stretched | 拉伸渲染模式，将附带一些旋转，使粒子朝向其运动方向 |
| mesh | 粒子将以指定网格渲染，与粒子系统中的mesh字段搭配 |

**支持色彩取样构建**

| 名称 | 类型 | 备注 | 默认值 |
| --- | --- | --- | --- |
| useRampGradients | boolean | 是否启用色彩梯度取样 | false |

**addRampGradient**

| 名称 | 类型 | 备注 |
| --- | --- | --- |
| gradient | number | 在指定位置设置对应色彩, 该值与（1-粒子alpha值）对应，取值范围[0~1] |
| color | Vector3 | 色彩RGB值 |

**addColorRemapGradient**

| 名称 | 类型 | 备注 |
| --- | --- | --- |
| time | number | 指定粒子生命周期的阶段 |
| min | number | alpha值左区间 |
| max | number | alpha值右区间 |

**addSizeGradient**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| gradient | number | 指定所处粒子生命周期的阶段 |
| sizeScale | number | 指定粒子大小的左区间 |
| sizeScale2 | number | 指定粒子大小的右区间[可选] |

**addColorGradient**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| gradient | number | 指定所处粒子生命周期的阶段 |
| color | Vector4 | 指定粒子颜色的左区间 |
| color2 | Vector4 | 指定粒子颜色的右区间[可选] |

**addAlphaGradient**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| gradient | number | 指定所处粒子生命周期的阶段 |
| alpha | number | 指定粒子颜色透明度的左区间 |
| alpha2 | number | 指定粒子颜色透明度的右区间[可选] |

**addSpeedScaleGradient**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| gradient | number | 指定所处粒子生命周期的阶段 |
| speedScale | number | 指定粒子速度的左区间 |
| speedScale2 | number | 指定粒子速度的右区间[可选] |

**相关属性**

| 参数 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| ATTACH | number | 指定发射器为附加类型 | 0 |
| END | number | 指定发射器为粒子结束时生成 | 1 |

---

### 内置环境数据

框架内置了一些环境数据资源。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/builtin/env.html

| 资源id | 描述 | 预览 |
| --- | --- | --- |
| xr-frame-team-workspace-day | xr-frame团队工作地，白天 |  |
| xr-frame-team-workspace-night | xr-frame团队工作地，夜晚 |  |
| xr-frame-team-workspace-day2 | xr-frame团队工作地2，白天 |  |
| gz-haixinsha | 广州海心沙，下午 |  |

---

### 内置几何数据

我们提供了几个内置的几何数据，均拥有UV、法线和切线：

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/builtin/geometry.html

| 资源id | 描述 | 尺寸 |
| --- | --- | --- |
| cube | 立方体 | 原点在中心，大小为1x1x1 |
| sphere | 球体 | 原点在中心，半径为1 |
| plane | 平面 | 原点在中心，一个xz平面，大小为1x1 |
| cylinder | 圆柱 | 原点在中心，半径为1，高度为2 |

---

### 内置纹理资源

框架内置了一些纹理资源。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/builtin/texture.html

**普通纹理**

| 资源id | 描述 |
| --- | --- |
| white | 白色 |
| transparent | 白色透明 |
| black | 黑色 |
| red | 红色 |
| green | 绿色 |
| blue | 蓝色 |
| yellow | 黄色 |
| babyblue | 淡蓝色 |
| babygreen | 淡绿色 |
| babyred | 淡红色 |
| brdf-lut |  |
| uv-debug |  |

**立方体纹理**

| 资源id | 描述 |
| --- | --- |
| white | 白色 |
| transparent | 白色透明 |
| black | 黑色 |
| red | 红色 |
| green | 绿色 |
| blue | 蓝色 |
| yellow | 黄色 |
| babyblue | 淡蓝色 |
| babygreen | 淡绿色 |
| babyred | 淡红色 |

---

### 内置效果和定义

框架内置了一些效果资源。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/builtin/effect.html

**基础**

| 类型 | 宏 | 说明 |
| --- | --- | --- |
| 是否为蒙皮网格 | `WX_SKINNED` | bool |
| 骨骼数量 | `WX_BONE_NUM` | int |
| 是否使用骨骼数据纹理 | `WX_USE_BONE_MATRIX_TEXTURE` | bool |

**基础**

| 类型 | uniforms | 说明 |
| --- | --- | --- |
| 视图矩阵 | `u_view` | mat4 |
| 投影矩阵 | `u_projection` | mat4 |
| 世界矩阵 | `u_world` | mat4 |
| 视图投影矩阵 | `u_vp` | mat4 |
| 视图逆矩阵 | `u_viewInverse` | mat4 |
| 游戏时间戳 | `u_gameTime` | float |
| 骨骼偏移矩阵 | `u_boneOffsetMatrix` | mat4[宏决定] |
| 骨骼矩阵太大时，转换为的贴图 | `u_boneMatrixTexture` | texture2d |

**后处理相关**

| 类型 | 宏 | 说明 |
| --- | --- | --- |
| 是否开启了后处理 | `WX_PP_ACTIVE` | bool |

---

### Simple 无光照渲染

Simple材质基于最基本的无光照情况进行实现。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/builtin/effect-simple.html

**simple 参数定义**

| 名称 | 类型 | 备注 | 默认值 |
| --- | --- | --- | --- |
| u\_baseColorMap | texture | 颜色贴图，颜色空间为 `SRGB` | 默认未使用 |
| u\_baseColorFactor | vec4 | 颜色因子，颜色空间为 `SRGB` | 1, 1, 1, 1 |

**simple 宏定义**

| 宏 | 说明 | 类型 |
| --- | --- | --- |
| WX\_USE\_BASECOLORMAP | 是否使用基础色贴图，使用u\_baseColorMap后会自动设为true | bool |

---

### Standard 标准物理光照渲染

Standard材质基于标准的PBR进行实现。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/builtin/effect-standard.html

**基础色 (baseColor)**

| uniforms | 类型 | 备注 | 默认值 |
| --- | --- | --- | --- |
| u\_baseColorMap | texture | 颜色贴图，颜色空间为 `SRGB` | 默认未使用 |
| u\_baseColorFactor | vec4 | 颜色因子，颜色空间为 `SRGB` | 1, 1, 1, 1 |

**金属度粗糙度 (metallic rougness)**

| uniforms | 类型 | 备注 | 默认值 |
| --- | --- | --- | --- |
| u\_metallicRoughnessMap | texture | 金属粗糙度贴图，g 部分为粗糙度，b 部分为金属度 | 默认未使用 |
| u\_metallicMap | texture | 金属度贴图，未使用金属粗糙度贴图时才生效 | 默认未使用 |
| u\_roughnessMap | texture | 粗糙度度贴图，未使用金属粗糙度贴图时才生效 | 默认未使用 |
| u\_metallicRoughnessValues | vec2 | 金属粗糙度因子，第一位为金属度，第二位为粗糙度 | 0, 1 |
| u\_ior | float | 折射率，默认值可以认为类似塑料折射率 | 1.5 |

**法线 (Normal)**

| uniforms | 类型 | 备注 | 默认值 |
| --- | --- | --- | --- |
| u\_normalMap | texture | 法线贴图 | 默认未使用 |
| u\_normalScale | float | 法线贴图缩放，需使用法线贴图才生效 | 1 |

**自发光 (Emissive)**

| uniforms | 类型 | 备注 | 默认值 |
| --- | --- | --- | --- |
| u\_emissiveMap | texture | 自发光贴图，颜色空间为 `SRGB` | 默认未使用 |
| u\_emissiveFactor | vec3 | 自发光贴图因子，颜色空间为 `LINEAR` | 0, 0, 0 |

**环境光遮蔽 (Ambient occlusion)**

| uniforms | 类型 | 备注 | 默认值 |
| --- | --- | --- | --- |
| u\_occlusionMap | texture | 环境光遮蔽贴图 | 默认未使用 |
| u\_occlusionStrength | float | 环境光遮蔽贴图强度，需使用遮蔽贴图才生效 | 1 |

**透明剔除 (alphaCutoff)**

| uniforms | 类型 | 备注 | 默认值 |
| --- | --- | --- | --- |
| u\_alphaCutoff | float | 透明剔除阈值，当 baseColor 的 alpha 小于 u\_alphaCutoff 时，不进行绘制，`alphaMode` 为 `MASK` 的情况下才生效 | 0.5 |

**清漆效果 (clearcoat)**

| uniforms | 类型 | 备注 | 默认值 |
| --- | --- | --- | --- |
| u\_clearcoatFactor | float | 清漆强度 | 0 |
| u\_clearcoatRoughnessFactor | float | 清漆粗糙度 | 0 |

**高光反射与光泽度 (specularGlossiness)**

| uniforms | 类型 | 备注 | 默认值 |
| --- | --- | --- | --- |
| u\_specularFactor | vec3 | 高光反射因子 | 1, 1, 1 |
| u\_glossinessFactor | float | 光泽度 | 1.0 |
| u\_specularGlossinessMap | texture | 高光光泽贴图，其中rgb部分是高光反射，a部分为光泽度 | 默认未使用 |

**standard 宏定义**

| 宏 | 说明 | 类型 |
| --- | --- | --- |
| WX\_MANUAL\_LINEAR\_BASECOLORFACTOR | 基础色因子是否使用 `Linear空间` | bool |
| WX\_USE\_BASECOLORMAP | 是否使用基础色贴图，使用u\_baseColorMap后会自动设为true | bool |
| WX\_USE\_METALROUGHNESSMAP | 是否使用金属粗糙度贴图，使用u\_metallicRoughnessMap后会自动设为true | bool |
| WX\_USE\_EMISSIVEMAP | 是否使用自发光贴图，使用u\_emissiveMap后会自动设为true | bool |
| WX\_USE\_OCCLUSIONMAP | 是否使用遮挡贴图，使用u\_occlusionMap后会自动设为true | bool |
| WX\_USE\_COLOR\_0 | 是否使用第一位顶点色 | bool |
| WX\_USE\_ALPHA\_CUTOFF | 是否使用透明剔除 | bool |
| WX\_USE\_CLEARCOAT | 是否使用清漆效果 | bool |
| WX\_USE\_SPECULARGLOSSINESS | 是否使用高光反射与光泽度渲染流程 | bool |
| WX\_USE\_SPECULARGLOSSINESSMAP | 是否使用高光反射与光泽度渲染贴图，使用u\_specularGlossinessMap后会自动设为true | bool |

---

### 内置图集

框架内置了一些图集资源。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/builtin/atlas.html

---

### 内置后处理资源

此处列出了框架内置支持的后处理资源类型、参数和对应效果。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/builtin/post-process.html

**blur**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| radius | number | 5 | 模糊半径 |

**fastblur**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| radius | number | 5 | 模糊半径 |

**bloom**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| threshold | number | 0.5 | 阈值 |
| softThreshold | number | 0 | 软阈值 |
| radius | number | 20 | 半径 |
| intensity | number | 2 | 亮度 |

**vignette**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| center | number[] | [0.5,0.5] | 半径 |
| color | number[] | [0,0,0,1] | 颜色 |
| intensity | number | 1 | 亮度 |
| smoothness | number | 1 | 边缘柔化 |
| roundness | number | 1 | 圆度 |
| rounded | number | 0/1 | 强制为圆形 |

---

### 调试

除了vConsole，XR-FRAME目前还可以通过小程序工具的真机调试2.0功能来进行调试。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/tools/debug.html

---

### xr-frame-tookit

我们提供了命令行工具xr-frame-cli来对框架需要的一些资源进行优化，或是生成环境数据。CLI已被废弃，现迁移到可视化工具XR-FRAME-TOOLS。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/tools/toolkit.html

---

<!-- pages: 124 -->
