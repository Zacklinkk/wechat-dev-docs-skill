# 微信小程序 API 结构化参考 — ui

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.showToast(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.showToast.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | title | string |  | 是 | 提示的内容 |  |
|  | icon | string | success | 否 | 图标 |  |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | success | 显示成功图标，此时 title 文本最多显示 7 个汉字长度 |  | | error | 显示失败图标，此时 title 文本最多显示 7 个汉字长度 | [2.14.1](../../../framework/compatibility.html) | | loading | 显示加载图标，此时 title 文本最多显示 7 个汉字长度 |  | | none | 不显示图标，此时 title 文本最多可显示两行，[1.9.0](../../../framework/compatibility.html)及以上版本支持 |  | | | | | | |
|  | image | string |  | 否 | 自定义图标的本地路径，image 的优先级高于 icon | [1.1.0](../../../framework/compatibility.html) |
|  | duration | number | 1500 | 否 | 提示的延迟时间 |  |
|  | mask | boolean | false | 否 | 是否显示透明蒙层，防止触摸穿透 |  |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| success | 显示成功图标，此时 title 文本最多显示 7 个汉字长度 |  |
| error | 显示失败图标，此时 title 文本最多显示 7 个汉字长度 | [2.14.1](../../../framework/compatibility.html) |
| loading | 显示加载图标，此时 title 文本最多显示 7 个汉字长度 |  |
| none | 不显示图标，此时 title 文本最多可显示两行，[1.9.0](../../../framework/compatibility.html)及以上版本支持 |  |

---

### wx.showModal(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.showModal.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| title | string |  | 否 | 提示的标题 |  |
| content | string |  | 否 | 提示的内容 |  |
| showCancel | boolean | true | 否 | 是否显示取消按钮 |  |
| cancelText | string | 取消 | 否 | 取消按钮的文字，最多 4 个字符 |  |
| cancelColor | string | #000000 | 否 | 取消按钮的文字颜色，必须是 16 进制格式的颜色字符串 |  |
| confirmText | string | 确定 | 否 | 确认按钮的文字，最多 4 个字符 |  |
| confirmColor | string | #576B95 | 否 | 确认按钮的文字颜色，必须是 16 进制格式的颜色字符串 |  |
| editable | boolean | false | 否 | 是否显示输入框 | [2.17.1](../../../framework/compatibility.html) |
| placeholderText | string |  | 否 | 显示输入框时的提示文本 | [2.17.1](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| content | string | editable 为 true 时，用户输入的文本 |  |
| confirm | boolean | 为 true 时，表示用户点击了确定按钮 |  |
| cancel | boolean | 为 true 时，表示用户点击了取消（用于 Android 系统区分点击蒙层关闭还是点击取消按钮关闭） | [1.1.0](../../../framework/compatibility.html) |

---

### wx.showLoading(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.showLoading.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| title | string |  | 是 | 提示的内容 |
| mask | boolean | false | 否 | 是否显示透明蒙层，防止触摸穿透 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.showActionSheet(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.showActionSheet.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| alertText | string |  | 否 | 警示文案 | [2.14.0](../../../framework/compatibility.html) |
| itemList | Array.<string> |  | 是 | 按钮的文字数组，数组长度最大为 6 |  |
| itemColor | string | #000000 | 否 | 按钮的文字颜色 |  |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tapIndex | number | 用户点击的按钮序号，从上到下的顺序，从0开始 |

---

### wx.hideToast(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.hideToast.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| noConflict | boolean | false | 否 | 目前 toast 和 loading 相关接口可以相互混用，此参数可用于取消混用特性 | [2.22.1](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### wx.hideLoading(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.hideLoading.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| noConflict | boolean | false | 否 | 目前 toast 和 loading 相关接口可以相互混用，此参数可用于取消混用特性 | [2.22.1](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### wx.enableAlertBeforeUnload(Object object)

基础库 2.12.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.enableAlertBeforeUnload.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| message | string |  | 是 | 询问对话框内容 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.disableAlertBeforeUnload(Object object)

基础库 2.12.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.disableAlertBeforeUnload.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.showNavigationBarLoading(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/navigation-bar/wx.showNavigationBarLoading.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.setNavigationBarTitle(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/navigation-bar/wx.setNavigationBarTitle.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| title | string |  | 是 | 页面标题 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.setNavigationBarColor(Object object)

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/navigation-bar/wx.setNavigationBarColor.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | frontColor | string |  | 是 | 前景颜色值，包括按钮、标题、状态栏的颜色，仅支持 #ffffff 和 #000000 |
|  | backgroundColor | string |  | 是 | 背景颜色值，有效值为十六进制颜色 |
|  | animation | Object |  | 否 | 动画效果 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | duration | number | 0 | 否 | 动画变化时间，单位 ms | |  | timingFunc | string | 'linear' | 否 | 动画变化方式 | |  | | 合法值 | 说明 | | --- | --- | | 'linear' | 动画从头到尾的速度是相同的 | | 'easeIn' | 动画以低速开始 | | 'easeOut' | 动画以低速结束 | | 'easeInOut' | 动画以低速开始和结束 | | | | | | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | duration | number | 0 | 否 | 动画变化时间，单位 ms |
|  | timingFunc | string | 'linear' | 否 | 动画变化方式 |
|  | | 合法值 | 说明 | | --- | --- | | 'linear' | 动画从头到尾的速度是相同的 | | 'easeIn' | 动画以低速开始 | | 'easeOut' | 动画以低速结束 | | 'easeInOut' | 动画以低速开始和结束 | | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 'linear' | 动画从头到尾的速度是相同的 |
| 'easeIn' | 动画以低速开始 |
| 'easeOut' | 动画以低速结束 |
| 'easeInOut' | 动画以低速开始和结束 |

---

### wx.hideNavigationBarLoading(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/navigation-bar/wx.hideNavigationBarLoading.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.hideHomeButton(Object object)

基础库 2.8.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/navigation-bar/wx.hideHomeButton.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.setBackgroundTextStyle(Object object)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/background/wx.setBackgroundTextStyle.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | textStyle | string |  | 是 | 下拉背景字体、loading 图的样式。 |
|  | | 合法值 | 说明 | | --- | --- | | dark | dark 样式 | | light | light 样式 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| dark | dark 样式 |
| light | light 样式 |

---

### wx.setBackgroundColor(Object object)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/background/wx.setBackgroundColor.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundColor | string |  | 否 | 窗口的背景色，必须为十六进制颜色值 |
| backgroundColorTop | string |  | 否 | 顶部窗口的背景色，必须为十六进制颜色值，仅 iOS 支持 |
| backgroundColorBottom | string |  | 否 | 底部窗口的背景色，必须为十六进制颜色值，仅 iOS 支持 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.showTabBarRedDot(Object object)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/tab-bar/wx.showTabBarRedDot.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| index | number |  | 是 | tabBar 的哪一项，从左边算起 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.showTabBar(Object object)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/tab-bar/wx.showTabBar.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| animation | boolean | false | 否 | 是否需要动画效果 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.setTabBarStyle(Object object)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/tab-bar/wx.setTabBarStyle.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| color | string |  | 否 | tab 上的文字默认颜色，HexColor |
| selectedColor | string |  | 否 | tab 上的文字选中时的颜色，HexColor |
| backgroundColor | string |  | 否 | tab 的背景色，HexColor |
| borderStyle | string |  | 否 | tabBar上边框的颜色， 仅支持 black/white |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.setTabBarItem(Object object)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/tab-bar/wx.setTabBarItem.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| index | number |  | 是 | tabBar 的哪一项，从左边算起 |
| text | string |  | 否 | tab 上的按钮文字 |
| iconPath | string |  | 否 | 图片路径，icon 大小限制为 40kb，建议尺寸为 81px \* 81px，当 postion 为 top 时，此参数无效 |
| selectedIconPath | string |  | 否 | 选中时的图片路径，icon 大小限制为 40kb，建议尺寸为 81px \* 81px ，当 postion 为 top 时，此参数无效 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.setTabBarBadge(Object object)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/tab-bar/wx.setTabBarBadge.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| index | number |  | 是 | tabBar 的哪一项，从左边算起 |
| text | string |  | 是 | 显示的文本，超过 4 个字符则显示成 ... |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.removeTabBarBadge(Object object)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/tab-bar/wx.removeTabBarBadge.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| index | number |  | 是 | tabBar 的哪一项，从左边算起 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.hideTabBarRedDot(Object object)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/tab-bar/wx.hideTabBarRedDot.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| index | number |  | 是 | tabBar 的哪一项，从左边算起 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.hideTabBar(Object object)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/tab-bar/wx.hideTabBar.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| animation | boolean | false | 否 | 是否需要动画效果 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.loadFontFace(Object object)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/font/wx.loadFontFace.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | global | boolean | false | 否 | 是否全局生效 | [2.10.0](../../../framework/compatibility.html) |
|  | family | string |  | 是 | 定义的字体名称 |  |
|  | source | string |  | 是 | 字体资源的地址，可以为 https 链接或者 Data URL。 |  |
|  | desc | Object |  | 否 | 可选的字体描述符 |  |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | style | string | 'normal' | 否 | 字体样式，可选值为 normal / italic / oblique | |  | weight | string | 'normal' | 否 | 字体粗细，可选值为 normal / bold / 100 / 200../ 900 | |  | variant | string | 'normal' | 否 | 设置小型大写字母的字体显示文本，可选值为 normal / small-caps / inherit | | | | | | |
|  | scopes | Array |  | 否 | 字体作用范围，可选值为 webview / native / skyline，默认全选，设置 native 可在 Canvas 2D 下使用 |  |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | style | string | 'normal' | 否 | 字体样式，可选值为 normal / italic / oblique |
|  | weight | string | 'normal' | 否 | 字体粗细，可选值为 normal / bold / 100 / 200../ 900 |
|  | variant | string | 'normal' | 否 | 设置小型大写字母的字体显示文本，可选值为 normal / small-caps / inherit |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| status | string | 加载字体结果 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| status | string | 加载字体结果 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| status | string | 加载字体结果 |

---

### wx.loadBuiltInFontFace(Object object)

基础库 3.7.9 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/font/wx.loadBuiltInFontFace.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | global | boolean | false | 否 | <是否全局生效 |
|  | family | string |  | 是 | 定义的字体名称 |
|  | source | string |  | 是 | 要加载的内置字体名字 |
|  | | 合法值 | 说明 | | --- | --- | | WeChatSansSS | WeChatSansSS 字体 | | WeChatSansStd | WeChatSansStd 字体 | | | | | |
|  | scopes | Array |  | 否 | 字体作用范围，可选值为 webview / native / skyline，默认全选，设置 native 可在 Canvas 2D 下使用 |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| WeChatSansSS | WeChatSansSS 字体 |
| WeChatSansStd | WeChatSansStd 字体 |

---

### wx.stopPullDownRefresh(Object object)

基础库 1.5.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/pull-down-refresh/wx.stopPullDownRefresh.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.startPullDownRefresh(Object object)

基础库 1.5.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/pull-down-refresh/wx.startPullDownRefresh.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.pageScrollTo(Object object)

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/scroll/wx.pageScrollTo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| scrollTop | number |  | 否 | 滚动到页面的目标位置，单位 px |  |
| duration | number | 300 | 否 | 滚动动画的时长，单位 ms |  |
| selector | string |  | 否 | 选择器 | [2.7.3](../../../framework/compatibility.html) |
| offsetTop | number |  | 否 | 偏移距离，需要和 selector 参数搭配使用，可以滚动到 selector 加偏移距离的位置，单位 px | [2.23.1](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### ScrollViewContext

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/scroll/ScrollViewContext.html

---

### ScrollViewContext.closeRefresh()

基础库 3.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/scroll/ScrollViewContext.closeRefresh.html

---

### ScrollViewContext.closeTwoLevel(Object object)

基础库 3.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/scroll/ScrollViewContext.closeTwoLevel.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 500 | 否 | 动画时长 |
| easingFunction | string | ease | 否 | [动画曲线]((skyline/easingFunction)) |

---

### ScrollViewContext.scrollIntoView(string selector, object ScrollIntoViewOptions)

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/scroll/ScrollViewContext.scrollIntoView.html

**object ScrollIntoViewOptions**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 0 | 否 | 跳转到目标节点时的额外偏移 |
| withinExtent | boolean | false | 否 | 只跳转到 cacheExtent 以内的目标节点，性能更佳 |
| alignment | string | "start" | 否 | 指定目标节点在视口内的位置 |
| animated | boolean | true | 否 | 是否启用滚动动画 |

---

### ScrollViewContext.scrollTo(Object object)

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/scroll/ScrollViewContext.scrollTo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| top | number |  | 否 | 顶部距离 |
| left | number |  | 否 | 左边界距离 |
| velocity | number |  | 否 | 初始速度 (webview 仅在 iOS 下生效；skyline 在 3.14.3 后支持) |
| duration | number |  | 否 | 滚动动画时长 (webview 仅在 iOS 下生效；skyline 在 3.14.3 后支持) |
| animated | boolean |  | 否 | 是否启用滚动动画 |

---

### ScrollViewContext.triggerRefresh(Object object)

基础库 3.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/scroll/ScrollViewContext.triggerRefresh.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 300 | 否 | 动画时长 |
| easingFunction | string | ease | 否 | [动画曲线]((skyline/easingFunction)) |

---

### ScrollViewContext.triggerTwoLevel(Object object)

基础库 3.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/scroll/ScrollViewContext.triggerTwoLevel.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 500 | 否 | 动画时长 |
| easingFunction | string | ease | 否 | [动画曲线]((skyline/easingFunction)) |

---

### Animation wx.createAnimation(Object object)

小程序插件：支持，需要小程序基础库版本不低于1.9.6

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/wx.createAnimation.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | duration | number | 400 | 否 | 动画持续时间，单位 ms |
|  | timingFunction | string | 'linear' | 否 | 动画的效果 |
|  | | 合法值 | 说明 | | --- | --- | | 'linear' | 动画从头到尾的速度是相同的 | | 'ease' | 动画以低速开始，然后加快，在结束前变慢 | | 'ease-in' | 动画以低速开始 | | 'ease-in-out' | 动画以低速开始和结束 | | 'ease-out' | 动画以低速结束 | | 'step-start' | 动画第一帧就跳至结束状态直到结束 | | 'step-end' | 动画一直保持开始状态，最后一帧跳到结束状态 | | | | | |
|  | delay | number | 0 | 否 | 动画延迟时间，单位 ms |
|  | transformOrigin | string | '50% 50% 0' | 否 |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 'linear' | 动画从头到尾的速度是相同的 |
| 'ease' | 动画以低速开始，然后加快，在结束前变慢 |
| 'ease-in' | 动画以低速开始 |
| 'ease-in-out' | 动画以低速开始和结束 |
| 'ease-out' | 动画以低速结束 |
| 'step-start' | 动画第一帧就跳至结束状态直到结束 |
| 'step-end' | 动画一直保持开始状态，最后一帧跳到结束状态 |

---

### Animation

相关文档:动画

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.html

---

### Animation Animation.backgroundColor(string value)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.backgroundColor.html

---

### Animation Animation.bottom(number|string value)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.bottom.html

---

### Object Animation.export()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.export.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| actions | Array.<Object> |  |

---

### Animation Animation.height(number|string value)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.height.html

---

### Animation Animation.left(number|string value)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.left.html

---

### Animation Animation.matrix()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.matrix.html

---

### Animation Animation.matrix3d()

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.matrix3d.html

---

### Animation Animation.opacity(number value)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.opacity.html

---

### Animation Animation.right(number|string value)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.right.html

---

### Animation Animation.rotate(number angle)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.rotate.html

---

### Animation Animation.rotate3d(number x, number y, number z, number angle)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.rotate3d.html

---

### Animation Animation.rotateX(number angle)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.rotateX.html

---

### Animation Animation.rotateY(number angle)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.rotateY.html

---

### Animation Animation.rotateZ(number angle)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.rotateZ.html

---

### Animation Animation.scale(number sx, number sy)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.scale.html

---

### Animation Animation.scale3d(number sx, number sy, number sz)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.scale3d.html

---

### Animation Animation.scaleX(number scale)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.scaleX.html

---

### Animation Animation.scaleY(number scale)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.scaleY.html

---

### Animation Animation.scaleZ(number scale)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.scaleZ.html

---

### Animation Animation.skew(number ax, number ay)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.skew.html

---

### Animation Animation.skewX(number angle)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.skewX.html

---

### Animation Animation.skewY(number angle)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.skewY.html

---

### Animation Animation.step(Object object)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.step.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | duration | number | 400 | 否 | 动画持续时间，单位 ms |
|  | timingFunction | string | 'linear' | 否 | 动画的效果 |
|  | | 合法值 | 说明 | | --- | --- | | 'linear' | 动画从头到尾的速度是相同的 | | 'ease' | 动画以低速开始，然后加快，在结束前变慢 | | 'ease-in' | 动画以低速开始 | | 'ease-in-out' | 动画以低速开始和结束 | | 'ease-out' | 动画以低速结束 | | 'step-start' | 动画第一帧就跳至结束状态直到结束 | | 'step-end' | 动画一直保持开始状态，最后一帧跳到结束状态 | | | | | |
|  | delay | number | 0 | 否 | 动画延迟时间，单位 ms |
|  | transformOrigin | string | '50% 50% 0' | 否 |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 'linear' | 动画从头到尾的速度是相同的 |
| 'ease' | 动画以低速开始，然后加快，在结束前变慢 |
| 'ease-in' | 动画以低速开始 |
| 'ease-in-out' | 动画以低速开始和结束 |
| 'ease-out' | 动画以低速结束 |
| 'step-start' | 动画第一帧就跳至结束状态直到结束 |
| 'step-end' | 动画一直保持开始状态，最后一帧跳到结束状态 |

---

### Animation Animation.top(number|string value)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.top.html

---

### Animation Animation.translate(number tx, number ty)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.translate.html

---

### Animation Animation.translate3d(number tx, number ty, number tz)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.translate3d.html

---

### Animation Animation.translateX(number translation)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.translateX.html

---

### Animation Animation.translateY(number translation)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.translateY.html

---

### Animation Animation.translateZ(number translation)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.translateZ.html

---

### Animation Animation.width(number|string value)

小程序插件：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.width.html

---

### wx.setTopBarText(Object object)

从基础库1.9.9开始，本接口停止维护

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/sticky/wx.setTopBarText.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| text | string |  | 是 | 置顶栏文字 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.nextTick(function callback)

基础库 2.2.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/custom-component/wx.nextTick.html

---

### wx.onUserTriggerTranslation(function listener)

基础库 3.7.9 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/menu/wx.onUserTriggerTranslation.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| locale | string | 翻译到的目标语言 |
| type | string | 触发来源， `button` 表示点击了菜单中的翻译按钮， `capsule` 表示点击了胶囊中的翻译提示 |

---

### wx.onUserOffTranslation(function listener)

基础库 3.14.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/menu/wx.onUserOffTranslation.html

---

### wx.onMenuButtonBoundingClientRectWeightChange(function listener)

基础库 3.4.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/menu/wx.onMenuButtonBoundingClientRectWeightChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 宽度，单位：px |
| height | number | 高度，单位：px |
| top | number | 上边界坐标，单位：px |
| right | number | 右边界坐标，单位：px |
| bottom | number | 下边界坐标，单位：px |
| left | number | 左边界坐标，单位：px |

---

### wx.offUserTriggerTranslation(function listener)

基础库 3.7.9 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/menu/wx.offUserTriggerTranslation.html

---

### wx.offUserOffTranslation(function listener)

基础库 3.14.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/menu/wx.offUserOffTranslation.html

---

### wx.offMenuButtonBoundingClientRectWeightChange(function listener)

基础库 3.4.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/menu/wx.offMenuButtonBoundingClientRectWeightChange.html

---

### Object wx.getMenuButtonBoundingClientRect()

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/menu/wx.getMenuButtonBoundingClientRect.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 宽度，单位：px |
| height | number | 高度，单位：px |
| top | number | 上边界坐标，单位：px |
| right | number | 右边界坐标，单位：px |
| bottom | number | 下边界坐标，单位：px |
| left | number | 左边界坐标，单位：px |

---

### wx.setWindowSize(Object object)

从基础库2.11.0开始，本接口停止维护

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.setWindowSize.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| width | number |  | 是 | 窗口宽度，以像素为单位 |
| height | number |  | 是 | 窗口高度，以像素为单位 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.onWindowStateChange(function listener)

基础库 3.8.8 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.onWindowStateChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| state | string | 改变的窗口状态，可能的值为： |

---

### wx.onWindowResize(function listener)

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.onWindowResize.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | size | Object |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | windowWidth | number | 变化后的窗口宽度，单位 px | |  | windowHeight | number | 变化后的窗口高度，单位 px | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | windowWidth | number | 变化后的窗口宽度，单位 px |
|  | windowHeight | number | 变化后的窗口高度，单位 px |

---

### wx.onParallelStateChange(function listener)

基础库 3.12.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.onParallelStateChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| isOnParallel | boolean | 当前是否分栏 |
| rightPage | Page | 分栏右侧页面对象（非分栏状态时返回当前页面） |
| leftPage | Page | 分栏左侧页面对象（非分栏状态时返回当前页面） |

---

### wx.offWindowStateChange(function listener)

基础库 3.8.8 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.offWindowStateChange.html

---

### wx.offWindowResize(function listener)

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.offWindowResize.html

---

### wx.offParallelStateChange(function listener)

基础库 3.12.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.offParallelStateChange.html

---

### boolean wx.checkIsPictureInPictureActive()

基础库 2.29.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.checkIsPictureInPictureActive.html

---

### wx.worklet

基础库 2.29.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/wx.worklet.html

---

### worklet.cancelAnimation(SharedValue SharedValue)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/base/worklet.cancelAnimation.html

---

### DerivedValue worklet.derived(WorkletFunction updaterWorklet)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/base/worklet.derived.html

---

### worklet.scrollViewContext

基础库 3.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/base/worklet.scrollViewContext.html

---

### worklet.scrollViewContext.scrollTo(Object object)

基础库 3.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/base/worklet.scrollViewContext.scrollTo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| top | number |  | 否 | 顶部距离 |
| left | number |  | 否 | 左边界距离 |
| duration | number |  | 否 | 滚动动画时长 |
| animated | boolean |  | 否 | 是否启用滚动动画 |
| easingFunction | string |  | 否 | 动画曲线 |

---

### SharedValue worklet.shared(any initialValue)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/base/worklet.shared.html

---

### AnimationObject worklet.decay(Object options, function callback)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/animation/worklet.decay.html

**Object options**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| velocity | number | 0 | 否 | 初速度 |
| deceleration | number | 0.998 | 否 | 衰减速率 |
| clamp | Array.<number> | [] | 否 | 边界值，长度为 2 的数组 |

---

### worklet.Easing

相关文档:worklet 动画

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/animation/worklet.Easing.html

---

### AnimationObject worklet.spring(number|string toValue, Object options, function callback)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/animation/worklet.spring.html

**Object options**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| damping | number | 10 | 否 | 阻尼系数 |
| mass | number | 1 | 否 | 重量系数，值越大移动越慢 |
| stiffness | number | 100 | 否 | 弹性系数 |
| overshootClamping | boolean | false | 否 | 动画是否可以在指定值上反弹 |
| restDisplacementThreshold | number | 0.01 | 否 | 弹簧静止时的位移 |
| restSpeedThreshold | number | 2 | 否 | 弹簧静止的速度 |
| velocity | number | 0 | 否 | 速度 |

---

### AnimationObject worklet.timing(number toValue, Object options, function callback)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/animation/worklet.timing.html

**Object options**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 300 | 否 | 动画时长 |
| easing | function | Easing.inOut(Easing.quad) | 否 | 动画曲线，参考 [Easing](worklet.Easing.html) 模块。 |

---

### AnimationObject worklet.delay(number delayMS, AnimationObject delayedAnimation)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/combine-animation/worklet.delay.html

---

### AnimationObject worklet.repeat(AnimationObject animation, number numberOfReps, boolean reverse, function callback)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/combine-animation/worklet.repeat.html

---

### AnimationObject worklet.sequence(AnimationObject animationN)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/combine-animation/worklet.sequence.html

---

### function worklet.runOnJS(function fn)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/tool-function/worklet.runOnJS.html

---

### function worklet.runOnUI(function fn)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/tool-function/worklet.runOnUI.html

---

<!-- pages: 99 -->
