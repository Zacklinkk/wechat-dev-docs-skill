# 微信小游戏 API 结构化参考 — ui

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.showToast(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ui/interaction/wx.showToast.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | title | string |  | 是 | 提示的内容 |  |
|  | icon | string | success | 否 | 图标 |  |
|  | | 合法值 | 说明 | 最低版本 | | --- | --- | --- | | success | 显示成功图标，此时 title 文本最多显示 7 个汉字长度 |  | | error | 显示失败图标，此时 title 文本最多显示 7 个汉字长度 | [2.14.1](../../../guide/runtime/client-lib/compatibility.html) | | loading | 显示加载图标，此时 title 文本最多显示 7 个汉字长度 |  | | none | 不显示图标，此时 title 文本最多可显示两行，[1.9.0](../../../guide/runtime/client-lib/compatibility.html)及以上版本支持 |  | | | | | | |
|  | image | string |  | 否 | 自定义图标的本地路径，image 的优先级高于 icon | [1.1.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | duration | number | 1500 | 否 | 提示的延迟时间 |  |
|  | mask | boolean | false | 否 | 是否显示透明蒙层，防止触摸穿透 |  |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| success | 显示成功图标，此时 title 文本最多显示 7 个汉字长度 |  |
| error | 显示失败图标，此时 title 文本最多显示 7 个汉字长度 | [2.14.1](../../../guide/runtime/client-lib/compatibility.html) |
| loading | 显示加载图标，此时 title 文本最多显示 7 个汉字长度 |  |
| none | 不显示图标，此时 title 文本最多可显示两行，[1.9.0](../../../guide/runtime/client-lib/compatibility.html)及以上版本支持 |  |

---

### wx.showModal(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ui/interaction/wx.showModal.html

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
| editable | boolean | false | 否 | 是否显示输入框 | [2.17.1](../../../guide/runtime/client-lib/compatibility.html) |
| placeholderText | string |  | 否 | 显示输入框时的提示文本 | [2.17.1](../../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| content | string | editable 为 true 时，用户输入的文本 |  |
| confirm | boolean | 为 true 时，表示用户点击了确定按钮 |  |
| cancel | boolean | 为 true 时，表示用户点击了取消（用于 Android 系统区分点击蒙层关闭还是点击取消按钮关闭） | [1.1.0](../../../guide/runtime/client-lib/compatibility.html) |

---

### wx.showLoading(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ui/interaction/wx.showLoading.html

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

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ui/interaction/wx.showActionSheet.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| alertText | string |  | 否 | 警示文案 | [2.14.0](../../../guide/runtime/client-lib/compatibility.html) |
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

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ui/interaction/wx.hideToast.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| noConflict | boolean | false | 否 | 目前 toast 和 loading 相关接口可以相互混用，此参数可用于取消混用特性 | [2.22.1](../../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### wx.hideLoading(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ui/interaction/wx.hideLoading.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| noConflict | boolean | false | 否 | 目前 toast 和 loading 相关接口可以相互混用，此参数可用于取消混用特性 | [2.22.1](../../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### wx.setMenuStyle(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ui/menu/wx.setMenuStyle.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | style | string |  | 是 | 样式风格 |
|  | | 合法值 | 说明 | | --- | --- | | light | 浅色 | | dark | 深色 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| light | 浅色 |
| dark | 深色 |

---

### wx.onOfficialComponentsInfoChange(function listener)

基础库 3.7.12 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ui/menu/wx.onOfficialComponentsInfoChange.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | OfficialComponentsInfo | Object | 全部组件的信息 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | notificationComponentInfo | Object | 通知组件信息 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | name | string | 组件的名称 | |  | isVisible | boolean | 组件是否显示 | |  | boundingClientRect | Object | 组件的布局位置信息 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | width | number | 宽度，单位：px | |  | height | number | 高度，单位：px | |  | top | number | 上边界坐标，单位：px | |  | right | number | 右边界坐标，单位：px | |  | bottom | number | 下边界坐标，单位：px | |  | left | number | 左边界坐标，单位：px | | | | | | | |  | rewardsComponentInfo | Object | 福利组件信息 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | name | string | 组件的名称 | |  | canReceiveGiftCount | number | 可领取的礼包数量 | |  | canReceiveFriendGiftCount | number | 可领取的好友礼包数量 | |  | receiveDetail | Object | 领取事件详情（只在onOfficialComponentsInfoChange回调中返回） | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | type | string | gift: 礼包, friendGift: 好友礼包 | |  | name | string | 礼包名称，只有 gift 类型才有 | |  | desc | string | 礼包描述，只有 gift 类型才有 | |  | icon | string | 礼包图标，只有 gift 类型才有 | | | | | | | |  | challengeRewardsComponentInfo | Object | 擂台赛组件领奖信息 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | name | string | 组件的名称 | |  | receiveDetail | Object | 领取事件详情（只在onOfficialComponentsInfoChange回调中返回） | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | userSourceList | Array.<Object> | 用户领取的奖励列表 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | source | Object | 奖励来源信息 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propList | Array.<Object> | 道具列表 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propName | string | 道具名称 | |  | propNum | number | 道具数量 | | | | |  | sourceName | string | 礼包名称 | |  | type | number | 奖励类型：1-普通奖励, 2-稀有奖励 | | | | |  | sourceNum | number | 获取的奖励数量 | |  | sourceType | number | 奖励类型：0-道具礼包, 1-微信蓝包, 2-h5商家券, 3-现金红包, 4-小程序券, 5-盲盒 | | | | |  | awardResult | number | 奖励领取结果：1-全部成功, 2-部分成功（礼物达到领取上限）, 3-领奖失败 | |  | receivedRareReward | boolean | 是否收到了稀有奖励 | | | | | | | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | notificationComponentInfo | Object | 通知组件信息 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | name | string | 组件的名称 | |  | isVisible | boolean | 组件是否显示 | |  | boundingClientRect | Object | 组件的布局位置信息 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | width | number | 宽度，单位：px | |  | height | number | 高度，单位：px | |  | top | number | 上边界坐标，单位：px | |  | right | number | 右边界坐标，单位：px | |  | bottom | number | 下边界坐标，单位：px | |  | left | number | 左边界坐标，单位：px | | | | | | |
|  | rewardsComponentInfo | Object | 福利组件信息 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | name | string | 组件的名称 | |  | canReceiveGiftCount | number | 可领取的礼包数量 | |  | canReceiveFriendGiftCount | number | 可领取的好友礼包数量 | |  | receiveDetail | Object | 领取事件详情（只在onOfficialComponentsInfoChange回调中返回） | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | type | string | gift: 礼包, friendGift: 好友礼包 | |  | name | string | 礼包名称，只有 gift 类型才有 | |  | desc | string | 礼包描述，只有 gift 类型才有 | |  | icon | string | 礼包图标，只有 gift 类型才有 | | | | | | |
|  | challengeRewardsComponentInfo | Object | 擂台赛组件领奖信息 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | name | string | 组件的名称 | |  | receiveDetail | Object | 领取事件详情（只在onOfficialComponentsInfoChange回调中返回） | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | userSourceList | Array.<Object> | 用户领取的奖励列表 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | source | Object | 奖励来源信息 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propList | Array.<Object> | 道具列表 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propName | string | 道具名称 | |  | propNum | number | 道具数量 | | | | |  | sourceName | string | 礼包名称 | |  | type | number | 奖励类型：1-普通奖励, 2-稀有奖励 | | | | |  | sourceNum | number | 获取的奖励数量 | |  | sourceType | number | 奖励类型：0-道具礼包, 1-微信蓝包, 2-h5商家券, 3-现金红包, 4-小程序券, 5-盲盒 | | | | |  | awardResult | number | 奖励领取结果：1-全部成功, 2-部分成功（礼物达到领取上限）, 3-领奖失败 | |  | receivedRareReward | boolean | 是否收到了稀有奖励 | | | | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | name | string | 组件的名称 |
|  | isVisible | boolean | 组件是否显示 |
|  | boundingClientRect | Object | 组件的布局位置信息 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | width | number | 宽度，单位：px | |  | height | number | 高度，单位：px | |  | top | number | 上边界坐标，单位：px | |  | right | number | 右边界坐标，单位：px | |  | bottom | number | 下边界坐标，单位：px | |  | left | number | 左边界坐标，单位：px | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | width | number | 宽度，单位：px |
|  | height | number | 高度，单位：px |
|  | top | number | 上边界坐标，单位：px |
|  | right | number | 右边界坐标，单位：px |
|  | bottom | number | 下边界坐标，单位：px |
|  | left | number | 左边界坐标，单位：px |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | name | string | 组件的名称 |
|  | canReceiveGiftCount | number | 可领取的礼包数量 |
|  | canReceiveFriendGiftCount | number | 可领取的好友礼包数量 |
|  | receiveDetail | Object | 领取事件详情（只在onOfficialComponentsInfoChange回调中返回） |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | type | string | gift: 礼包, friendGift: 好友礼包 | |  | name | string | 礼包名称，只有 gift 类型才有 | |  | desc | string | 礼包描述，只有 gift 类型才有 | |  | icon | string | 礼包图标，只有 gift 类型才有 | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | type | string | gift: 礼包, friendGift: 好友礼包 |
|  | name | string | 礼包名称，只有 gift 类型才有 |
|  | desc | string | 礼包描述，只有 gift 类型才有 |
|  | icon | string | 礼包图标，只有 gift 类型才有 |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | name | string | 组件的名称 |
|  | receiveDetail | Object | 领取事件详情（只在onOfficialComponentsInfoChange回调中返回） |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | userSourceList | Array.<Object> | 用户领取的奖励列表 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | source | Object | 奖励来源信息 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propList | Array.<Object> | 道具列表 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propName | string | 道具名称 | |  | propNum | number | 道具数量 | | | | |  | sourceName | string | 礼包名称 | |  | type | number | 奖励类型：1-普通奖励, 2-稀有奖励 | | | | |  | sourceNum | number | 获取的奖励数量 | |  | sourceType | number | 奖励类型：0-道具礼包, 1-微信蓝包, 2-h5商家券, 3-现金红包, 4-小程序券, 5-盲盒 | | | | |  | awardResult | number | 奖励领取结果：1-全部成功, 2-部分成功（礼物达到领取上限）, 3-领奖失败 | |  | receivedRareReward | boolean | 是否收到了稀有奖励 | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | userSourceList | Array.<Object> | 用户领取的奖励列表 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | source | Object | 奖励来源信息 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propList | Array.<Object> | 道具列表 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propName | string | 道具名称 | |  | propNum | number | 道具数量 | | | | |  | sourceName | string | 礼包名称 | |  | type | number | 奖励类型：1-普通奖励, 2-稀有奖励 | | | | |  | sourceNum | number | 获取的奖励数量 | |  | sourceType | number | 奖励类型：0-道具礼包, 1-微信蓝包, 2-h5商家券, 3-现金红包, 4-小程序券, 5-盲盒 | | | |
|  | awardResult | number | 奖励领取结果：1-全部成功, 2-部分成功（礼物达到领取上限）, 3-领奖失败 |
|  | receivedRareReward | boolean | 是否收到了稀有奖励 |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | source | Object | 奖励来源信息 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propList | Array.<Object> | 道具列表 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propName | string | 道具名称 | |  | propNum | number | 道具数量 | | | | |  | sourceName | string | 礼包名称 | |  | type | number | 奖励类型：1-普通奖励, 2-稀有奖励 | | | |
|  | sourceNum | number | 获取的奖励数量 |
|  | sourceType | number | 奖励类型：0-道具礼包, 1-微信蓝包, 2-h5商家券, 3-现金红包, 4-小程序券, 5-盲盒 |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | propList | Array.<Object> | 道具列表 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propName | string | 道具名称 | |  | propNum | number | 道具数量 | | | |
|  | sourceName | string | 礼包名称 |
|  | type | number | 奖励类型：1-普通奖励, 2-稀有奖励 |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | propName | string | 道具名称 |
|  | propNum | number | 道具数量 |

---

### wx.offOfficialComponentsInfoChange(function listener)

基础库 3.7.12 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ui/menu/wx.offOfficialComponentsInfoChange.html

---

### Object wx.getOfficialComponentsInfo()

基础库 3.7.12 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ui/menu/wx.getOfficialComponentsInfo.html

**Object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | notificationComponentInfo | Object | 通知组件信息 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | name | string | 组件的名称 | |  | isVisible | boolean | 组件是否显示 | |  | boundingClientRect | Object | 组件的布局位置信息 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | width | number | 宽度，单位：px | |  | height | number | 高度，单位：px | |  | top | number | 上边界坐标，单位：px | |  | right | number | 右边界坐标，单位：px | |  | bottom | number | 下边界坐标，单位：px | |  | left | number | 左边界坐标，单位：px | | | | | | |
|  | rewardsComponentInfo | Object | 福利组件信息 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | name | string | 组件的名称 | |  | canReceiveGiftCount | number | 可领取的礼包数量 | |  | canReceiveFriendGiftCount | number | 可领取的好友礼包数量 | |  | receiveDetail | Object | 领取事件详情（只在onOfficialComponentsInfoChange回调中返回） | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | type | string | gift: 礼包, friendGift: 好友礼包 | |  | name | string | 礼包名称，只有 gift 类型才有 | |  | desc | string | 礼包描述，只有 gift 类型才有 | |  | icon | string | 礼包图标，只有 gift 类型才有 | | | | | | |
|  | challengeRewardsComponentInfo | Object | 擂台赛组件领奖信息 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | name | string | 组件的名称 | |  | receiveDetail | Object | 领取事件详情（只在onOfficialComponentsInfoChange回调中返回） | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | userSourceList | Array.<Object> | 用户领取的奖励列表 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | source | Object | 奖励来源信息 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propList | Array.<Object> | 道具列表 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propName | string | 道具名称 | |  | propNum | number | 道具数量 | | | | |  | sourceName | string | 礼包名称 | |  | type | number | 奖励类型：1-普通奖励, 2-稀有奖励 | | | | |  | sourceNum | number | 获取的奖励数量 | |  | sourceType | number | 奖励类型：0-道具礼包, 1-微信蓝包, 2-h5商家券, 3-现金红包, 4-小程序券, 5-盲盒 | | | | |  | awardResult | number | 奖励领取结果：1-全部成功, 2-部分成功（礼物达到领取上限）, 3-领奖失败 | |  | receivedRareReward | boolean | 是否收到了稀有奖励 | | | | | | |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | name | string | 组件的名称 |
|  | isVisible | boolean | 组件是否显示 |
|  | boundingClientRect | Object | 组件的布局位置信息 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | width | number | 宽度，单位：px | |  | height | number | 高度，单位：px | |  | top | number | 上边界坐标，单位：px | |  | right | number | 右边界坐标，单位：px | |  | bottom | number | 下边界坐标，单位：px | |  | left | number | 左边界坐标，单位：px | | | |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | width | number | 宽度，单位：px |
|  | height | number | 高度，单位：px |
|  | top | number | 上边界坐标，单位：px |
|  | right | number | 右边界坐标，单位：px |
|  | bottom | number | 下边界坐标，单位：px |
|  | left | number | 左边界坐标，单位：px |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | name | string | 组件的名称 |
|  | canReceiveGiftCount | number | 可领取的礼包数量 |
|  | canReceiveFriendGiftCount | number | 可领取的好友礼包数量 |
|  | receiveDetail | Object | 领取事件详情（只在onOfficialComponentsInfoChange回调中返回） |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | type | string | gift: 礼包, friendGift: 好友礼包 | |  | name | string | 礼包名称，只有 gift 类型才有 | |  | desc | string | 礼包描述，只有 gift 类型才有 | |  | icon | string | 礼包图标，只有 gift 类型才有 | | | |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | type | string | gift: 礼包, friendGift: 好友礼包 |
|  | name | string | 礼包名称，只有 gift 类型才有 |
|  | desc | string | 礼包描述，只有 gift 类型才有 |
|  | icon | string | 礼包图标，只有 gift 类型才有 |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | name | string | 组件的名称 |
|  | receiveDetail | Object | 领取事件详情（只在onOfficialComponentsInfoChange回调中返回） |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | userSourceList | Array.<Object> | 用户领取的奖励列表 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | source | Object | 奖励来源信息 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propList | Array.<Object> | 道具列表 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propName | string | 道具名称 | |  | propNum | number | 道具数量 | | | | |  | sourceName | string | 礼包名称 | |  | type | number | 奖励类型：1-普通奖励, 2-稀有奖励 | | | | |  | sourceNum | number | 获取的奖励数量 | |  | sourceType | number | 奖励类型：0-道具礼包, 1-微信蓝包, 2-h5商家券, 3-现金红包, 4-小程序券, 5-盲盒 | | | | |  | awardResult | number | 奖励领取结果：1-全部成功, 2-部分成功（礼物达到领取上限）, 3-领奖失败 | |  | receivedRareReward | boolean | 是否收到了稀有奖励 | | | |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | userSourceList | Array.<Object> | 用户领取的奖励列表 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | source | Object | 奖励来源信息 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propList | Array.<Object> | 道具列表 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propName | string | 道具名称 | |  | propNum | number | 道具数量 | | | | |  | sourceName | string | 礼包名称 | |  | type | number | 奖励类型：1-普通奖励, 2-稀有奖励 | | | | |  | sourceNum | number | 获取的奖励数量 | |  | sourceType | number | 奖励类型：0-道具礼包, 1-微信蓝包, 2-h5商家券, 3-现金红包, 4-小程序券, 5-盲盒 | | | |
|  | awardResult | number | 奖励领取结果：1-全部成功, 2-部分成功（礼物达到领取上限）, 3-领奖失败 |
|  | receivedRareReward | boolean | 是否收到了稀有奖励 |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | source | Object | 奖励来源信息 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propList | Array.<Object> | 道具列表 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propName | string | 道具名称 | |  | propNum | number | 道具数量 | | | | |  | sourceName | string | 礼包名称 | |  | type | number | 奖励类型：1-普通奖励, 2-稀有奖励 | | | |
|  | sourceNum | number | 获取的奖励数量 |
|  | sourceType | number | 奖励类型：0-道具礼包, 1-微信蓝包, 2-h5商家券, 3-现金红包, 4-小程序券, 5-盲盒 |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | propList | Array.<Object> | 道具列表 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | propName | string | 道具名称 | |  | propNum | number | 道具数量 | | | |
|  | sourceName | string | 礼包名称 |
|  | type | number | 奖励类型：1-普通奖励, 2-稀有奖励 |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | propName | string | 道具名称 |
|  | propNum | number | 道具数量 |

---

### Object wx.getMenuButtonBoundingClientRect()

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ui/menu/wx.getMenuButtonBoundingClientRect.html

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

### wx.setStatusBarStyle(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ui/statusbar/wx.setStatusBarStyle.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | style | string |  | 是 | 样式风格 |
|  | | 合法值 | 说明 | | --- | --- | | white | 白色 | | black | 浅色 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| white | 白色 |
| black | 浅色 |

---

### wx.setWindowSize(Object object)

从基础库2.11.0开始，本接口停止维护

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ui/window/wx.setWindowSize.html

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

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ui/window/wx.onWindowStateChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| state | string | 改变的窗口状态，可能的值为： |

---

### wx.onWindowResize(function listener)

监听窗口尺寸变化事件

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ui/window/wx.onWindowResize.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| windowWidth | number | 变化后的窗口宽度，单位 px |
| windowHeight | number | 变化后的窗口高度，单位 px |

---

### wx.offWindowStateChange(function listener)

基础库 3.8.8 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ui/window/wx.offWindowStateChange.html

---

### wx.offWindowResize(function listener)

移除窗口尺寸变化事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/ui/window/wx.offWindowResize.html

---

<!-- pages: 17 -->
