# 微信小游戏 API 结构化参考 — device

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.updateKeyboard(Object object)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/keyboard/wx.updateKeyboard.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| value | string |  | 是 | 键盘输入框的当前值 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.showKeyboard(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/keyboard/wx.showKeyboard.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | defaultValue | string |  | 是 | 键盘输入框显示的默认值 |
|  | maxLength | number |  | 是 | 键盘中文本的最大长度 |
|  | multiple | boolean |  | 是 | 是否为多行输入 |
|  | confirmHold | boolean |  | 是 | 当点击完成时键盘是否保持显示 |
|  | confirmType | string |  | 是 | 键盘右下角 confirm 按钮的类型，只影响按钮的文本内容 |
|  | | 合法值 | 说明 | | --- | --- | | done | 完成 | | next | 下一个 | | search | 搜索 | | go | 前往 | | send | 发送 | | | | | |
|  | keyboardType | string |  | 是 | 键盘类型，默认为文本类型，客户端8.0.57以上支持数字键盘 |
|  | | 合法值 | 说明 | | --- | --- | | text | 文本 | | number | 数字 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| done | 完成 |
| next | 下一个 |
| search | 搜索 |
| go | 前往 |
| send | 发送 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| text | 文本 |
| number | 数字 |

---

### wx.onKeyUp(function listener)

基础库 2.10.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/keyboard/wx.onKeyUp.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| key | string | 同 Web 规范 KeyEvent key 属性 |
| code | string | 同 Web 规范 KeyEvent code 属性 |
| timeStamp | number | 事件触发时的时间戳 |

---

### wx.onKeyDown(function listener)

基础库 2.10.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/keyboard/wx.onKeyDown.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| key | string | 同 Web 规范 KeyEvent key 属性 |
| code | string | 同 Web 规范 KeyEvent code 属性 |
| timeStamp | number | 事件触发时的时间戳 |

---

### wx.onKeyboardInput(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/keyboard/wx.onKeyboardInput.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| value | string | 键盘输入的当前值 |

---

### wx.onKeyboardHeightChange(function listener)

基础库 2.21.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/keyboard/wx.onKeyboardHeightChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| height | number | 键盘高度 |

---

### wx.onKeyboardConfirm(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/keyboard/wx.onKeyboardConfirm.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| value | string | 键盘输入的当前值 |

---

### wx.onKeyboardComplete(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/keyboard/wx.onKeyboardComplete.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| value | string | 键盘输入的当前值 |

---

### wx.offKeyUp(function listener)

基础库 2.10.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/keyboard/wx.offKeyUp.html

---

### wx.offKeyDown(function listener)

基础库 2.10.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/keyboard/wx.offKeyDown.html

---

### wx.offKeyboardInput(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/keyboard/wx.offKeyboardInput.html

---

### wx.offKeyboardHeightChange(function listener)

基础库 2.21.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/keyboard/wx.offKeyboardHeightChange.html

---

### wx.offKeyboardConfirm(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/keyboard/wx.offKeyboardConfirm.html

---

### wx.offKeyboardComplete(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/keyboard/wx.offKeyboardComplete.html

---

### wx.hideKeyboard(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/keyboard/wx.hideKeyboard.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.onTouchStart(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/touch-event/wx.onTouchStart.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| touches | Array.<[Touch](Touch.html)> | 当前所有触摸点的列表 |
| changedTouches | Array.<[Touch](Touch.html)> | 触发此次事件的触摸点列表 |
| timeStamp | number | 事件触发时的时间戳 |

---

### wx.onTouchMove(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/touch-event/wx.onTouchMove.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| touches | Array.<[Touch](Touch.html)> | 当前所有触摸点的列表 |
| changedTouches | Array.<[Touch](Touch.html)> | 触发此次事件的触摸点列表 |
| timeStamp | number | 事件触发时的时间戳 |

---

### wx.onTouchEnd(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/touch-event/wx.onTouchEnd.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| touches | Array.<[Touch](Touch.html)> | 当前所有触摸点的列表 |
| changedTouches | Array.<[Touch](Touch.html)> | 触发此次事件的触摸点列表 |
| timeStamp | number | 事件触发时的时间戳 |

---

### wx.onTouchCancel(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/touch-event/wx.onTouchCancel.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| touches | Array.<[Touch](Touch.html)> | 当前所有触摸点的列表 |
| changedTouches | Array.<[Touch](Touch.html)> | 触发此次事件的触摸点列表 |
| timeStamp | number | 事件触发时的时间戳 |

---

### wx.offTouchStart(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/touch-event/wx.offTouchStart.html

---

### wx.offTouchMove(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/touch-event/wx.offTouchMove.html

---

### wx.offTouchEnd(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/touch-event/wx.offTouchEnd.html

---

### wx.offTouchCancel(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/touch-event/wx.offTouchCancel.html

---

### Touch

在触控设备上的触摸点。通常是指手指或者触控笔在触屏设备或者触摸板上的操作。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/touch-event/Touch.html

---

### wx.onMouseUp(function listener)

监听鼠标按键弹起事件

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/mouse-event/wx.onMouseUp.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| x | number | 事件触发时鼠标所在的位置横坐标 |
| y | number | 事件触发时鼠标所在的位置纵坐标 |
| button | number | 按键类型，0左键，1中键，2右键 |
| timeStamp | number | 事件触发时的时间戳 |

---

### wx.onMouseMove(function listener)

监听鼠标移动事件

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/mouse-event/wx.onMouseMove.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| x | number | 事件触发时鼠标所在的位置横坐标 |
| y | number | 事件触发时鼠标所在的位置纵坐标 |
| movementX | number | 鼠标横坐标偏移量 |
| movementY | number | 鼠标纵坐标偏移量 |
| timeStamp | number | 事件触发时的时间戳 |

---

### wx.onMouseDown(function listener)

监听鼠标按键按下事件

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/mouse-event/wx.onMouseDown.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| x | number | 事件触发时鼠标所在的位置横坐标 |
| y | number | 事件触发时鼠标所在的位置纵坐标 |
| button | number | 按键类型，0左键，1中键，2右键 |
| timeStamp | number | 事件触发时的时间戳 |

---

### wx.offMouseUp(function listener)

移除鼠标按键弹起事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/mouse-event/wx.offMouseUp.html

---

### wx.offMouseMove(function listener)

移除鼠标移动事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/mouse-event/wx.offMouseMove.html

---

### wx.offMouseDown(function listener)

移除鼠标按键按下事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/mouse-event/wx.offMouseDown.html

---

### wx.onWheel(function listener)

监听鼠标滚轮事件

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/wheel-event/wx.onWheel.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| deltaX | number | 滚轮 x 轴方向滚动量 |
| deltaY | number | 滚轮 y 轴方向滚动量 |
| deltaZ | number | 滚轮 z 轴方向滚动量 |
| x | number | 事件触发时鼠标所在的位置横坐标 |
| y | number | 事件触发时鼠标所在的位置纵坐标 |
| timeStamp | number | 事件触发时的时间戳 |

---

### wx.offWheel(function listener)

移除鼠标滚轮事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/wheel-event/wx.offWheel.html

---

### wx.stopBeaconDiscovery(Object object)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/ibeacon/wx.stopBeaconDiscovery.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| 11000 | unsupport | 系统或设备不支持 |
| 11001 | bluetooth service unavailable | 蓝牙服务不可用 |
| 11002 | location service unavailable | 位置服务不可用 |
| 11003 | already start | 已经开始搜索 |
| 11004 | not startBeaconDiscovery | 还未开始搜索 |
| 11005 | system error | 系统错误 |
| 11006 | invalid data | 参数不正确 |

---

### wx.startBeaconDiscovery(Object object)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/ibeacon/wx.startBeaconDiscovery.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| uuids | Array.<string> |  | 是 | Beacon 设备广播的 UUID 列表 |
| ignoreBluetoothAvailable | boolean | false | 否 | 是否校验蓝牙开关，仅在 iOS 下有效。iOS 11 起，控制面板里关掉蓝牙，还是能继续使用 Beacon 服务。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| 11000 | unsupport | 系统或设备不支持 |
| 11001 | bluetooth service unavailable | 蓝牙服务不可用 |
| 11002 | location service unavailable | 位置服务不可用 |
| 11003 | already start | 已经开始搜索 |
| 11004 | not startBeaconDiscovery | 还未开始搜索 |
| 11005 | system error | 系统错误 |
| 11006 | invalid data | 参数不正确 |

---

### wx.onBeaconUpdate(function listener)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/ibeacon/wx.onBeaconUpdate.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| beacons | Array.<[BeaconInfo](BeaconInfo.html)> | 当前搜寻到的所有 Beacon 设备列表 |

---

### wx.onBeaconServiceChange(function listener)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/ibeacon/wx.onBeaconServiceChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| available | boolean | 服务目前是否可用 |
| discovering | boolean | 目前是否处于搜索状态 |

---

### wx.offBeaconUpdate()

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/ibeacon/wx.offBeaconUpdate.html

---

### wx.offBeaconServiceChange()

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/ibeacon/wx.offBeaconServiceChange.html

---

### wx.getBeacons(Object object)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/ibeacon/wx.getBeacons.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| beacons | Array.<[BeaconInfo](BeaconInfo.html)> | Beacon 设备列表 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| 11000 | unsupport | 系统或设备不支持 |
| 11001 | bluetooth service unavailable | 蓝牙服务不可用 |
| 11002 | location service unavailable | 位置服务不可用 |
| 11003 | already start | 已经开始搜索 |
| 11004 | not startBeaconDiscovery | 还未开始搜索 |
| 11005 | system error | 系统错误 |
| 11006 | invalid data | 参数不正确 |

---

### BeaconInfo

相关文档:蓝牙信标 (Beacon)

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/ibeacon/BeaconInfo.html

**number proximity**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 0 | 信号太弱不足以计算距离，或非 iOS 设备 |  |
| 1 | 十分近 |  |
| 2 | 比较近 |  |
| 3 | 远 |  |

---

### wx.onBLEPeripheralConnectionStateChanged(function listener)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-peripheral/wx.onBLEPeripheralConnectionStateChanged.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| deviceId | String | 连接状态变化的设备 id |
| serverId | String | server 的 UUID |
| connected | Boolean | 连接目前状态 |

---

### wx.offBLEPeripheralConnectionStateChanged(function listener)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-peripheral/wx.offBLEPeripheralConnectionStateChanged.html

---

### wx.createBLEPeripheralServer(Object object)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-peripheral/wx.createBLEPeripheralServer.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| server | [BLEPeripheralServer](BLEPeripheralServer.html) | 外围设备的服务端。 |

---

### BLEPeripheralServer

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.html

---

### BLEPeripheralServer.addService(Object object)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.addService.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | service | Object |  | 是 | 描述service的Object |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | uuid | String |  | 是 | 蓝牙服务的 UUID | |  | characteristics | Array.<Object> |  | 是 | characteristics列表 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | uuid | String |  | 是 | characteristic 的 UUID | |  | properties | Object |  | 否 | 特征支持的操作 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | write | Boolean | false | 否 | 写 | |  | writeNoResponse | Boolean | false | 否 | 无回复写 | |  | read | Boolean | false | 否 | 读 | |  | notify | Boolean | false | 否 | 订阅 | |  | indicate | Boolean | false | 否 | 回包 | | | | | | |  | permission | Object |  | 否 | 特征权限 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | readable | Boolean | false | 否 | 可读 | |  | writeable | Boolean | false | 否 | 可写 | |  | readEncryptionRequired | Boolean | false | 否 | 加密读请求 | |  | writeEncryptionRequired | Boolean | false | 否 | 加密写请求 | | | | | | |  | value | ArrayBuffer |  | 否 | 特征对应的二进制值 | |  | descriptors | Array.<Object> |  | 否 | 描述符数据 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | uuid | String |  | 是 | Descriptor 的 UUID | |  | permission | Object |  | 否 | 描述符的权限 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | write | Boolean | false | 否 | 写 | |  | read | Boolean | false | 否 | 读 | | | | | | |  | value | ArrayBuffer |  | 否 | 描述符数据 | | | | | | | | | | | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | uuid | String |  | 是 | 蓝牙服务的 UUID |
|  | characteristics | Array.<Object> |  | 是 | characteristics列表 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | uuid | String |  | 是 | characteristic 的 UUID | |  | properties | Object |  | 否 | 特征支持的操作 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | write | Boolean | false | 否 | 写 | |  | writeNoResponse | Boolean | false | 否 | 无回复写 | |  | read | Boolean | false | 否 | 读 | |  | notify | Boolean | false | 否 | 订阅 | |  | indicate | Boolean | false | 否 | 回包 | | | | | | |  | permission | Object |  | 否 | 特征权限 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | readable | Boolean | false | 否 | 可读 | |  | writeable | Boolean | false | 否 | 可写 | |  | readEncryptionRequired | Boolean | false | 否 | 加密读请求 | |  | writeEncryptionRequired | Boolean | false | 否 | 加密写请求 | | | | | | |  | value | ArrayBuffer |  | 否 | 特征对应的二进制值 | |  | descriptors | Array.<Object> |  | 否 | 描述符数据 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | uuid | String |  | 是 | Descriptor 的 UUID | |  | permission | Object |  | 否 | 描述符的权限 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | write | Boolean | false | 否 | 写 | |  | read | Boolean | false | 否 | 读 | | | | | | |  | value | ArrayBuffer |  | 否 | 描述符数据 | | | | | | | | | | |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | uuid | String |  | 是 | characteristic 的 UUID |
|  | properties | Object |  | 否 | 特征支持的操作 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | write | Boolean | false | 否 | 写 | |  | writeNoResponse | Boolean | false | 否 | 无回复写 | |  | read | Boolean | false | 否 | 读 | |  | notify | Boolean | false | 否 | 订阅 | |  | indicate | Boolean | false | 否 | 回包 | | | | | |
|  | permission | Object |  | 否 | 特征权限 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | readable | Boolean | false | 否 | 可读 | |  | writeable | Boolean | false | 否 | 可写 | |  | readEncryptionRequired | Boolean | false | 否 | 加密读请求 | |  | writeEncryptionRequired | Boolean | false | 否 | 加密写请求 | | | | | |
|  | value | ArrayBuffer |  | 否 | 特征对应的二进制值 |
|  | descriptors | Array.<Object> |  | 否 | 描述符数据 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | uuid | String |  | 是 | Descriptor 的 UUID | |  | permission | Object |  | 否 | 描述符的权限 | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | write | Boolean | false | 否 | 写 | |  | read | Boolean | false | 否 | 读 | | | | | | |  | value | ArrayBuffer |  | 否 | 描述符数据 | | | | | |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | write | Boolean | false | 否 | 写 |
|  | writeNoResponse | Boolean | false | 否 | 无回复写 |
|  | read | Boolean | false | 否 | 读 |
|  | notify | Boolean | false | 否 | 订阅 |
|  | indicate | Boolean | false | 否 | 回包 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | readable | Boolean | false | 否 | 可读 |
|  | writeable | Boolean | false | 否 | 可写 |
|  | readEncryptionRequired | Boolean | false | 否 | 加密读请求 |
|  | writeEncryptionRequired | Boolean | false | 否 | 加密写请求 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | uuid | String |  | 是 | Descriptor 的 UUID |
|  | permission | Object |  | 否 | 描述符的权限 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | write | Boolean | false | 否 | 写 | |  | read | Boolean | false | 否 | 读 | | | | | |
|  | value | ArrayBuffer |  | 否 | 描述符数据 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | write | Boolean | false | 否 | 写 |
|  | read | Boolean | false | 否 | 读 |

---

### BLEPeripheralServer.offCharacteristicReadRequest(function listener)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.offCharacteristicReadRequest.html

---

### BLEPeripheralServer.offCharacteristicSubscribed(function listener)

基础库 2.13.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.offCharacteristicSubscribed.html

---

### BLEPeripheralServer.offCharacteristicUnsubscribed(function listener)

基础库 2.13.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.offCharacteristicUnsubscribed.html

---

### BLEPeripheralServer.offCharacteristicWriteRequest(function listener)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.offCharacteristicWriteRequest.html

---

### BLEPeripheralServer.onCharacteristicReadRequest(function listener)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.onCharacteristicReadRequest.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| serviceId | String | 蓝牙特征对应服务的 UUID |
| characteristicId | String | 蓝牙特征的 UUID |
| callbackId | Number | 唯一标识码，调用 [writeCharacteristicValue](BLEPeripheralServer.writeCharacteristicValue.html) 时使用 |

---

### BLEPeripheralServer.onCharacteristicSubscribed(function listener)

基础库 2.13.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.onCharacteristicSubscribed.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| serviceId | String | 蓝牙特征对应服务的 UUID |
| characteristicId | String | 蓝牙特征的 UUID |

---

### BLEPeripheralServer.onCharacteristicUnsubscribed(function listener)

基础库 2.13.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.onCharacteristicUnsubscribed.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| serviceId | String | 蓝牙特征对应服务的 UUID |
| characteristicId | String | 蓝牙特征的 UUID |

---

### BLEPeripheralServer.onCharacteristicWriteRequest(function listener)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.onCharacteristicWriteRequest.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| serviceId | String | 蓝牙特征对应服务的 UUID |
| characteristicId | String | 蓝牙特征的 UUID |
| callbackId | Number | 唯一标识码，调用 [writeCharacteristicValue](BLEPeripheralServer.writeCharacteristicValue.html) 时使用 |
| value | ArrayBuffer | 请求写入特征的二进制数据值 |

---

### BLEPeripheralServer.removeService(Object object)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.removeService.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| serviceId | String |  | 是 | service 的 UUID |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### BLEPeripheralServer.startAdvertising(Object Object)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.startAdvertising.html

**Object Object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | advertiseRequest | Object |  | 是 | 广播自定义参数 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | connectable | Boolean | true | 否 | 当前设备是否可连接 |  | |  | deviceName | String |  | 否 | 广播中 deviceName 字段，默认为空 |  | |  | serviceUuids | Array.<String> |  | 否 | 要广播的服务 UUID 列表。使用 16/32 位 UUID 时请参考注意事项。 |  | |  | manufacturerData | Array.<Object> |  | 否 | 广播的制造商信息。仅安卓支持，iOS 因系统限制无法定制。 |  | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | manufacturerId | String |  | 是 | 制造商ID，0x 开头的十六进制 | |  | manufacturerSpecificData | ArrayBuffer |  | 否 | 制造商信息 | | | | | | | |  | beacon | Object |  | 否 | 以 beacon 设备形式广播的参数。 | [2.20.1](../../../guide/runtime/client-lib/compatibility.html) | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | uuid | String |  | 是 | Beacon 设备广播的 UUID | |  | major | Number |  | 是 | Beacon 设备的主 ID | |  | minor | Number |  | 是 | Beacon 设备的次 ID | |  | measuredPower | Number |  | 否 | 用于判断距离设备 1 米时 RSSI 大小的参考值 | | | | | | | | | | | |
|  | powerLevel | String | medium | 否 | 广播功率 |
|  | | 合法值 | 说明 | | --- | --- | | low | 功率低 | | medium | 功率适中 | | high | 功率高 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object Object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | connectable | Boolean | true | 否 | 当前设备是否可连接 |  |
|  | deviceName | String |  | 否 | 广播中 deviceName 字段，默认为空 |  |
|  | serviceUuids | Array.<String> |  | 否 | 要广播的服务 UUID 列表。使用 16/32 位 UUID 时请参考注意事项。 |  |
|  | manufacturerData | Array.<Object> |  | 否 | 广播的制造商信息。仅安卓支持，iOS 因系统限制无法定制。 |  |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | manufacturerId | String |  | 是 | 制造商ID，0x 开头的十六进制 | |  | manufacturerSpecificData | ArrayBuffer |  | 否 | 制造商信息 | | | | | | |
|  | beacon | Object |  | 否 | 以 beacon 设备形式广播的参数。 | [2.20.1](../../../guide/runtime/client-lib/compatibility.html) |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | uuid | String |  | 是 | Beacon 设备广播的 UUID | |  | major | Number |  | 是 | Beacon 设备的主 ID | |  | minor | Number |  | 是 | Beacon 设备的次 ID | |  | measuredPower | Number |  | 否 | 用于判断距离设备 1 米时 RSSI 大小的参考值 | | | | | | |

**Object Object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | manufacturerId | String |  | 是 | 制造商ID，0x 开头的十六进制 |
|  | manufacturerSpecificData | ArrayBuffer |  | 否 | 制造商信息 |

**Object Object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | uuid | String |  | 是 | Beacon 设备广播的 UUID |
|  | major | Number |  | 是 | Beacon 设备的主 ID |
|  | minor | Number |  | 是 | Beacon 设备的次 ID |
|  | measuredPower | Number |  | 否 | 用于判断距离设备 1 米时 RSSI 大小的参考值 |

**Object Object**

| 合法值 | 说明 |
| --- | --- |
| low | 功率低 |
| medium | 功率适中 |
| high | 功率高 |

---

### BLEPeripheralServer.stopAdvertising(Object object)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.stopAdvertising.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### BLEPeripheralServer.writeCharacteristicValue(Object Object)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.writeCharacteristicValue.html

**Object Object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| serviceId | String |  | 是 | 蓝牙特征对应服务的 UUID |
| characteristicId | String |  | 是 | 蓝牙特征的 UUID |
| value | ArrayBuffer |  | 是 | characteristic 对应的二进制值 |
| needNotify | Boolean |  | 是 | 是否需要通知主机 value 已更新 |
| callbackId | Number |  | 否 | 可选，处理回包时使用 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.writeBLECharacteristicValue(Object object)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-ble/wx.writeBLECharacteristicValue.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | deviceId | string |  | 是 | 蓝牙设备 id |
|  | serviceId | string |  | 是 | 蓝牙特征对应服务的 UUID |
|  | characteristicId | string |  | 是 | 蓝牙特征的 UUID |
|  | value | ArrayBuffer |  | 是 | 蓝牙设备特征对应的二进制值 |
|  | writeType | string |  | 否 | 蓝牙特征值的写模式设置，有两种模式，iOS 优先 write，安卓优先 writeNoResponse 。（基础库 2.22.0 开始支持） |
|  | | 合法值 | 说明 | | --- | --- | | write | 强制回复写，不支持时报错 | | writeNoResponse | 强制无回复写，不支持时报错 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| write | 强制回复写，不支持时报错 |
| writeNoResponse | 强制无回复写，不支持时报错 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| -1 | already connect | 已连接 |
| 10000 | not init | 未初始化蓝牙适配器 |
| 10001 | not available | 当前蓝牙适配器不可用 |
| 10002 | no device | 没有找到指定设备 |
| 10003 | connection fail | 连接失败 |
| 10004 | no service | 没有找到指定服务 |
| 10005 | no characteristic | 没有找到指定特征 |
| 10006 | no connection | 当前连接已断开 |
| 10007 | property not support | 当前特征不支持此操作 |
| 10008 | system error | 其余所有系统上报的异常 |
| 10009 | system not support | Android 系统特有，系统版本低于 4.3 不支持 BLE |
| 10012 | operate time out | 连接超时 |
| 10013 | invalid\_data | 连接 deviceId 为空或者是格式不正确 |

---

### wx.setBLEMTU(Object object)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-ble/wx.setBLEMTU.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string |  | 是 | 蓝牙设备 id |
| mtu | number |  | 是 | 最大传输单元。设置范围为 (22,512) 区间内，单位 bytes |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| mtu | number | 最终协商的 MTU 值，与传入参数一致。安卓客户端 8.0.9 开始支持。 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| mtu | number | 最终协商的 MTU 值。如果协商失败则无此参数。安卓客户端 8.0.9 开始支持。 |

---

### wx.readBLECharacteristicValue(Object object)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-ble/wx.readBLECharacteristicValue.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string |  | 是 | 蓝牙设备 id |
| serviceId | string |  | 是 | 蓝牙特征对应服务的 UUID |
| characteristicId | string |  | 是 | 蓝牙特征的 UUID |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| -1 | already connect | 已连接 |
| 10000 | not init | 未初始化蓝牙适配器 |
| 10001 | not available | 当前蓝牙适配器不可用 |
| 10002 | no device | 没有找到指定设备 |
| 10003 | connection fail | 连接失败 |
| 10004 | no service | 没有找到指定服务 |
| 10005 | no characteristic | 没有找到指定特征 |
| 10006 | no connection | 当前连接已断开 |
| 10007 | property not support | 当前特征不支持此操作 |
| 10008 | system error | 其余所有系统上报的异常 |
| 10009 | system not support | Android 系统特有，系统版本低于 4.3 不支持 BLE |
| 10012 | operate time out | 连接超时 |
| 10013 | invalid\_data | 连接 deviceId 为空或者是格式不正确 |

---

### wx.onBLEMTUChange(function listener)

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-ble/wx.onBLEMTUChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| deviceId | string | 蓝牙设备 id |
| mtu | number | 最大传输单元 |

---

### wx.onBLEConnectionStateChange(function listener)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-ble/wx.onBLEConnectionStateChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| deviceId | string | 蓝牙设备 id |
| connected | boolean | 是否处于已连接状态 |

---

### wx.onBLECharacteristicValueChange(function listener)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-ble/wx.onBLECharacteristicValueChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| deviceId | string | 蓝牙设备 id |
| serviceId | string | 蓝牙特征对应服务的 UUID |
| characteristicId | string | 蓝牙特征的 UUID |
| value | ArrayBuffer | 特征最新的值 |

---

### wx.offBLEMTUChange(function listener)

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-ble/wx.offBLEMTUChange.html

---

### wx.offBLEConnectionStateChange(function listener)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-ble/wx.offBLEConnectionStateChange.html

---

### wx.offBLECharacteristicValueChange()

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-ble/wx.offBLECharacteristicValueChange.html

---

### wx.notifyBLECharacteristicValueChange(Object object)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-ble/wx.notifyBLECharacteristicValueChange.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| deviceId | string |  | 是 | 蓝牙设备 id |  |
| serviceId | string |  | 是 | 蓝牙特征对应服务的 UUID |  |
| characteristicId | string |  | 是 | 蓝牙特征的 UUID |  |
| state | boolean |  | 是 | 是否启用 notify |  |
| type | string | indication | 否 | 设置特征订阅类型，有效值有 `notification` 和 `indication` | [2.4.0](../../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| -1 | already connect | 已连接 |
| 10000 | not init | 未初始化蓝牙适配器 |
| 10001 | not available | 当前蓝牙适配器不可用 |
| 10002 | no device | 没有找到指定设备 |
| 10003 | connection fail | 连接失败 |
| 10004 | no service | 没有找到指定服务 |
| 10005 | no characteristic | 没有找到指定特征 |
| 10006 | no connection | 当前连接已断开 |
| 10007 | property not support | 当前特征不支持此操作 |
| 10008 | system error | 其余所有系统上报的异常 |
| 10009 | system not support | Android 系统特有，系统版本低于 4.3 不支持 BLE |
| 10012 | operate time out | 连接超时 |
| 10013 | invalid\_data | 连接 deviceId 为空或者是格式不正确 |

---

### wx.getBLEMTU(Object object)

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-ble/wx.getBLEMTU.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | deviceId | string |  | 是 | 蓝牙设备 id |
|  | writeType | string | write | 否 | 写模式 （iOS 特有参数） |
|  | | 合法值 | 说明 | | --- | --- | | write | 有回复写 | | writeNoResponse | 无回复写 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| write | 有回复写 |
| writeNoResponse | 无回复写 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| mtu | number | 最大传输单元 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| -1 | already connect | 已连接 |
| 10000 | not init | 未初始化蓝牙适配器 |
| 10001 | not available | 当前蓝牙适配器不可用 |
| 10002 | no device | 没有找到指定设备 |
| 10003 | connection fail | 连接失败 |
| 10004 | no service | 没有找到指定服务 |
| 10005 | no characteristic | 没有找到指定特征 |
| 10006 | no connection | 当前连接已断开 |
| 10007 | property not support | 当前特征不支持此操作 |
| 10008 | system error | 其余所有系统上报的异常 |
| 10009 | system not support | Android 系统特有，系统版本低于 4.3 不支持 BLE |
| 10012 | operate time out | 连接超时 |
| 10013 | invalid\_data | 连接 deviceId 为空或者是格式不正确 |

---

### wx.getBLEDeviceServices(Object object)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-ble/wx.getBLEDeviceServices.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string |  | 是 | 蓝牙设备 id。需要已经通过 [wx.createBLEConnection](wx.createBLEConnection.html) 建立连接 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | services | Array.<Object> | 设备服务列表 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | uuid | string | 蓝牙设备服务的 UUID | |  | isPrimary | boolean | 该服务是否为主服务 | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | uuid | string | 蓝牙设备服务的 UUID |
|  | isPrimary | boolean | 该服务是否为主服务 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| -1 | already connect | 已连接 |
| 10000 | not init | 未初始化蓝牙适配器 |
| 10001 | not available | 当前蓝牙适配器不可用 |
| 10002 | no device | 没有找到指定设备 |
| 10003 | connection fail | 连接失败 |
| 10004 | no service | 没有找到指定服务 |
| 10005 | no characteristic | 没有找到指定特征 |
| 10006 | no connection | 当前连接已断开 |
| 10007 | property not support | 当前特征不支持此操作 |
| 10008 | system error | 其余所有系统上报的异常 |
| 10009 | system not support | Android 系统特有，系统版本低于 4.3 不支持 BLE |
| 10012 | operate time out | 连接超时 |
| 10013 | invalid\_data | 连接 deviceId 为空或者是格式不正确 |

---

### wx.getBLEDeviceRSSI(Object object)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-ble/wx.getBLEDeviceRSSI.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string |  | 是 | 蓝牙设备 id |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| RSSI | Number | 信号强度，单位 dBm |

---

### wx.getBLEDeviceCharacteristics(Object object)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-ble/wx.getBLEDeviceCharacteristics.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string |  | 是 | 蓝牙设备 id。需要已经通过 [wx.createBLEConnection](wx.createBLEConnection.html) 建立连接 |
| serviceId | string |  | 是 | 蓝牙服务 UUID。需要先调用 [wx.getBLEDeviceServices](wx.getBLEDeviceServices.html) 获取 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | characteristics | Array.<Object> | 设备特征列表 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | uuid | string | 蓝牙设备特征的 UUID | |  | properties | Object | 该特征支持的操作类型 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | read | boolean | 该特征是否支持 read 操作 | |  | write | boolean | 该特征是否支持 write 操作 | |  | notify | boolean | 该特征是否支持 notify 操作 | |  | indicate | boolean | 该特征是否支持 indicate 操作 | |  | writeNoResponse | boolean | 该特征是否支持无回复写操作 | |  | writeDefault | boolean | 该特征是否支持有回复写操作 | | | | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | uuid | string | 蓝牙设备特征的 UUID |
|  | properties | Object | 该特征支持的操作类型 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | read | boolean | 该特征是否支持 read 操作 | |  | write | boolean | 该特征是否支持 write 操作 | |  | notify | boolean | 该特征是否支持 notify 操作 | |  | indicate | boolean | 该特征是否支持 indicate 操作 | |  | writeNoResponse | boolean | 该特征是否支持无回复写操作 | |  | writeDefault | boolean | 该特征是否支持有回复写操作 | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | read | boolean | 该特征是否支持 read 操作 |
|  | write | boolean | 该特征是否支持 write 操作 |
|  | notify | boolean | 该特征是否支持 notify 操作 |
|  | indicate | boolean | 该特征是否支持 indicate 操作 |
|  | writeNoResponse | boolean | 该特征是否支持无回复写操作 |
|  | writeDefault | boolean | 该特征是否支持有回复写操作 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| -1 | already connect | 已连接 |
| 10000 | not init | 未初始化蓝牙适配器 |
| 10001 | not available | 当前蓝牙适配器不可用 |
| 10002 | no device | 没有找到指定设备 |
| 10003 | connection fail | 连接失败 |
| 10004 | no service | 没有找到指定服务 |
| 10005 | no characteristic | 没有找到指定特征 |
| 10006 | no connection | 当前连接已断开 |
| 10007 | property not support | 当前特征不支持此操作 |
| 10008 | system error | 其余所有系统上报的异常 |
| 10009 | system not support | Android 系统特有，系统版本低于 4.3 不支持 BLE |
| 10012 | operate time out | 连接超时 |
| 10013 | invalid\_data | 连接 deviceId 为空或者是格式不正确 |

---

### wx.createBLEConnection(Object object)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-ble/wx.createBLEConnection.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string |  | 是 | 蓝牙设备 id |
| timeout | number |  | 否 | 超时时间，单位 ms，不填表示不会超时 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| -1 | already connect | 已连接 |
| 10000 | not init | 未初始化蓝牙适配器 |
| 10001 | not available | 当前蓝牙适配器不可用 |
| 10002 | no device | 没有找到指定设备 |
| 10003 | connection fail | 连接失败 |
| 10004 | no service | 没有找到指定服务 |
| 10005 | no characteristic | 没有找到指定特征 |
| 10006 | no connection | 当前连接已断开 |
| 10007 | property not support | 当前特征不支持此操作 |
| 10008 | system error | 其余所有系统上报的异常 |
| 10009 | system not support | Android 系统特有，系统版本低于 4.3 不支持 BLE |
| 10012 | operate time out | 连接超时 |
| 10013 | invalid\_data | 连接 deviceId 为空或者是格式不正确 |

---

### wx.closeBLEConnection(Object object)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth-ble/wx.closeBLEConnection.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string |  | 是 | 蓝牙设备 id |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| -1 | already connect | 已连接 |
| 10000 | not init | 未初始化蓝牙适配器 |
| 10001 | not available | 当前蓝牙适配器不可用 |
| 10002 | no device | 没有找到指定设备 |
| 10003 | connection fail | 连接失败 |
| 10004 | no service | 没有找到指定服务 |
| 10005 | no characteristic | 没有找到指定特征 |
| 10006 | no connection | 当前连接已断开 |
| 10007 | property not support | 当前特征不支持此操作 |
| 10008 | system error | 其余所有系统上报的异常 |
| 10009 | system not support | Android 系统特有，系统版本低于 4.3 不支持 BLE |
| 10012 | operate time out | 连接超时 |
| 10013 | invalid\_data | 连接 deviceId 为空或者是格式不正确 |

---

### wx.stopBluetoothDevicesDiscovery(Object object)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth/wx.stopBluetoothDevicesDiscovery.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| -1 | already connect | 已连接 |
| 10000 | not init | 未初始化蓝牙适配器 |
| 10001 | not available | 当前蓝牙适配器不可用 |
| 10002 | no device | 没有找到指定设备 |
| 10003 | connection fail | 连接失败 |
| 10004 | no service | 没有找到指定服务 |
| 10005 | no characteristic | 没有找到指定特征 |
| 10006 | no connection | 当前连接已断开 |
| 10007 | property not support | 当前特征不支持此操作 |
| 10008 | system error | 其余所有系统上报的异常 |
| 10009 | system not support | Android 系统特有，系统版本低于 4.3 不支持 BLE |
| 10012 | operate time out | 连接超时 |
| 10013 | invalid\_data | 连接 deviceId 为空或者是格式不正确 |

---

### wx.startBluetoothDevicesDiscovery(Object object)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth/wx.startBluetoothDevicesDiscovery.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | services | Array.<string> |  | 否 | 要搜索的蓝牙设备主服务的 UUID 列表（支持 16/32/128 位 UUID）。某些蓝牙设备会广播自己的主 service 的 UUID。如果设置此参数，则只搜索广播包有对应 UUID 的主服务的蓝牙设备。建议通过该参数过滤掉周边不需要处理的其他蓝牙设备。 |
|  | allowDuplicatesKey | boolean | false | 否 | 是否允许重复上报同一设备。如果允许重复上报，则 [wx.onBlueToothDeviceFound](errorwx.onBlueToothDeviceFound)) 方法会多次上报同一设备，但是 RSSI 值会有不同。 |
|  | interval | number | 0 | 否 | 上报设备的间隔，单位 ms。0 表示找到新设备立即上报，其他数值根据传入的间隔上报。 |
|  | powerLevel | string | medium | 否 | 扫描模式，越高扫描越快，也越耗电。仅安卓微信客户端 7.0.12 及以上支持。 |
|  | | 合法值 | 说明 | | --- | --- | | low | 低 | | medium | 中 | | high | 高 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| low | 低 |
| medium | 中 |
| high | 高 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| -1 | already connect | 已连接 |
| 10000 | not init | 未初始化蓝牙适配器 |
| 10001 | not available | 当前蓝牙适配器不可用 |
| 10002 | no device | 没有找到指定设备 |
| 10003 | connection fail | 连接失败 |
| 10004 | no service | 没有找到指定服务 |
| 10005 | no characteristic | 没有找到指定特征 |
| 10006 | no connection | 当前连接已断开 |
| 10007 | property not support | 当前特征不支持此操作 |
| 10008 | system error | 其余所有系统上报的异常 |
| 10009 | system not support | Android 系统特有，系统版本低于 4.3 不支持 BLE |
| 10012 | operate time out | 连接超时 |
| 10013 | invalid\_data | 连接 deviceId 为空或者是格式不正确 |

---

### wx.openBluetoothAdapter(Object object)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth/wx.openBluetoothAdapter.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | mode | string | central | 否 | 蓝牙模式，可作为主/从设备，仅 iOS 需要。 | [2.10.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | central | 主机模式 | | peripheral | 从机（外围设备）模式 | | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| central | 主机模式 |
| peripheral | 从机（外围设备）模式 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| -1 | already connect | 已连接 |
| 10000 | not init | 未初始化蓝牙适配器 |
| 10001 | not available | 当前蓝牙适配器不可用 |
| 10002 | no device | 没有找到指定设备 |
| 10003 | connection fail | 连接失败 |
| 10004 | no service | 没有找到指定服务 |
| 10005 | no characteristic | 没有找到指定特征 |
| 10006 | no connection | 当前连接已断开 |
| 10007 | property not support | 当前特征不支持此操作 |
| 10008 | system error | 其余所有系统上报的异常 |
| 10009 | system not support | Android 系统特有，系统版本低于 4.3 不支持 BLE |
| 10012 | operate time out | 连接超时 |
| 10013 | invalid\_data | 连接 deviceId 为空或者是格式不正确 |

**object.fail 回调函数返回的 state 参数（仅 iOS）**

| 状态码 | 说明 |
| --- | --- |
| 0 | 未知 |
| 1 | 重置中 |
| 2 | 不支持 |
| 3 | 未授权 |
| 4 | 未开启 |

---

### wx.onBluetoothDeviceFound(function listener)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth/wx.onBluetoothDeviceFound.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | devices | Array.<Object> | 新搜索到的设备列表 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | name | string | 蓝牙设备名称，某些设备可能没有 | |  | deviceId | string | 蓝牙设备 id | |  | RSSI | number | 当前蓝牙设备的信号强度，单位 dBm | |  | advertisData | ArrayBuffer | 当前蓝牙设备的广播数据段中的 ManufacturerData 数据段。 | |  | advertisServiceUUIDs | Array.<string> | 当前蓝牙设备的广播数据段中的 ServiceUUIDs 数据段 | |  | localName | string | 当前蓝牙设备的广播数据段中的 LocalName 数据段 | |  | serviceData | Object | 当前蓝牙设备的广播数据段中的 ServiceData 数据段 | |  | connectable | boolean | 当前蓝牙设备是否可连接（ Android 8.0 以下不支持返回该值 ） | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | name | string | 蓝牙设备名称，某些设备可能没有 |
|  | deviceId | string | 蓝牙设备 id |
|  | RSSI | number | 当前蓝牙设备的信号强度，单位 dBm |
|  | advertisData | ArrayBuffer | 当前蓝牙设备的广播数据段中的 ManufacturerData 数据段。 |
|  | advertisServiceUUIDs | Array.<string> | 当前蓝牙设备的广播数据段中的 ServiceUUIDs 数据段 |
|  | localName | string | 当前蓝牙设备的广播数据段中的 LocalName 数据段 |
|  | serviceData | Object | 当前蓝牙设备的广播数据段中的 ServiceData 数据段 |
|  | connectable | boolean | 当前蓝牙设备是否可连接（ Android 8.0 以下不支持返回该值 ） |

---

### wx.onBluetoothAdapterStateChange(function listener)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth/wx.onBluetoothAdapterStateChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| available | boolean | 蓝牙适配器是否可用 |
| discovering | boolean | 蓝牙适配器是否处于搜索状态 |

---

### wx.offBluetoothDeviceFound()

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth/wx.offBluetoothDeviceFound.html

---

### wx.offBluetoothAdapterStateChange()

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth/wx.offBluetoothAdapterStateChange.html

---

### wx.makeBluetoothPair(Object object)

基础库 2.12.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth/wx.makeBluetoothPair.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string |  | 是 | 蓝牙设备 id |
| pin | string |  | 是 | pin 码，Base64 格式。 |
| timeout | number | 20000 | 否 | 超时时间，单位 ms |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.isBluetoothDevicePaired(Object object)

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth/wx.isBluetoothDevicePaired.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string |  | 是 | 蓝牙设备 id |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.getConnectedBluetoothDevices(Object object)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth/wx.getConnectedBluetoothDevices.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| services | Array.<string> |  | 是 | 蓝牙设备主服务的 UUID 列表（支持 16/32/128 位 UUID） |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | devices | Array.<Object> | 搜索到的设备列表 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | name | string | 蓝牙设备名称，某些设备可能没有 | |  | deviceId | string | 用于区分设备的 id | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | name | string | 蓝牙设备名称，某些设备可能没有 |
|  | deviceId | string | 用于区分设备的 id |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| -1 | already connect | 已连接 |
| 10000 | not init | 未初始化蓝牙适配器 |
| 10001 | not available | 当前蓝牙适配器不可用 |
| 10002 | no device | 没有找到指定设备 |
| 10003 | connection fail | 连接失败 |
| 10004 | no service | 没有找到指定服务 |
| 10005 | no characteristic | 没有找到指定特征 |
| 10006 | no connection | 当前连接已断开 |
| 10007 | property not support | 当前特征不支持此操作 |
| 10008 | system error | 其余所有系统上报的异常 |
| 10009 | system not support | Android 系统特有，系统版本低于 4.3 不支持 BLE |
| 10012 | operate time out | 连接超时 |
| 10013 | invalid\_data | 连接 deviceId 为空或者是格式不正确 |

---

### wx.getBluetoothDevices(Object object)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth/wx.getBluetoothDevices.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | devices | Array.<Object> | UUID 对应的已连接设备列表 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | name | string | 蓝牙设备名称，某些设备可能没有 | |  | deviceId | string | 蓝牙设备 id | |  | RSSI | number | 当前蓝牙设备的信号强度，单位 dBm | |  | advertisData | ArrayBuffer | 当前蓝牙设备的广播数据段中的 ManufacturerData 数据段。 | |  | advertisServiceUUIDs | Array.<string> | 当前蓝牙设备的广播数据段中的 ServiceUUIDs 数据段 | |  | localName | string | 当前蓝牙设备的广播数据段中的 LocalName 数据段 | |  | serviceData | Object | 当前蓝牙设备的广播数据段中的 ServiceData 数据段 | |  | connectable | boolean | 当前蓝牙设备是否可连接（ Android 8.0 以下不支持返回该值 ） | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | name | string | 蓝牙设备名称，某些设备可能没有 |
|  | deviceId | string | 蓝牙设备 id |
|  | RSSI | number | 当前蓝牙设备的信号强度，单位 dBm |
|  | advertisData | ArrayBuffer | 当前蓝牙设备的广播数据段中的 ManufacturerData 数据段。 |
|  | advertisServiceUUIDs | Array.<string> | 当前蓝牙设备的广播数据段中的 ServiceUUIDs 数据段 |
|  | localName | string | 当前蓝牙设备的广播数据段中的 LocalName 数据段 |
|  | serviceData | Object | 当前蓝牙设备的广播数据段中的 ServiceData 数据段 |
|  | connectable | boolean | 当前蓝牙设备是否可连接（ Android 8.0 以下不支持返回该值 ） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| -1 | already connect | 已连接 |
| 10000 | not init | 未初始化蓝牙适配器 |
| 10001 | not available | 当前蓝牙适配器不可用 |
| 10002 | no device | 没有找到指定设备 |
| 10003 | connection fail | 连接失败 |
| 10004 | no service | 没有找到指定服务 |
| 10005 | no characteristic | 没有找到指定特征 |
| 10006 | no connection | 当前连接已断开 |
| 10007 | property not support | 当前特征不支持此操作 |
| 10008 | system error | 其余所有系统上报的异常 |
| 10009 | system not support | Android 系统特有，系统版本低于 4.3 不支持 BLE |
| 10012 | operate time out | 连接超时 |
| 10013 | invalid\_data | 连接 deviceId 为空或者是格式不正确 |

---

### wx.getBluetoothAdapterState(Object object)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth/wx.getBluetoothAdapterState.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| discovering | boolean | 是否正在搜索设备 |
| available | boolean | 蓝牙适配器是否可用 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| -1 | already connect | 已连接 |
| 10000 | not init | 未初始化蓝牙适配器 |
| 10001 | not available | 当前蓝牙适配器不可用 |
| 10002 | no device | 没有找到指定设备 |
| 10003 | connection fail | 连接失败 |
| 10004 | no service | 没有找到指定服务 |
| 10005 | no characteristic | 没有找到指定特征 |
| 10006 | no connection | 当前连接已断开 |
| 10007 | property not support | 当前特征不支持此操作 |
| 10008 | system error | 其余所有系统上报的异常 |
| 10009 | system not support | Android 系统特有，系统版本低于 4.3 不支持 BLE |
| 10012 | operate time out | 连接超时 |
| 10013 | invalid\_data | 连接 deviceId 为空或者是格式不正确 |

---

### wx.closeBluetoothAdapter(Object object)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/bluetooth/wx.closeBluetoothAdapter.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| -1 | already connect | 已连接 |
| 10000 | not init | 未初始化蓝牙适配器 |
| 10001 | not available | 当前蓝牙适配器不可用 |
| 10002 | no device | 没有找到指定设备 |
| 10003 | connection fail | 连接失败 |
| 10004 | no service | 没有找到指定服务 |
| 10005 | no characteristic | 没有找到指定特征 |
| 10006 | no connection | 当前连接已断开 |
| 10007 | property not support | 当前特征不支持此操作 |
| 10008 | system error | 其余所有系统上报的异常 |
| 10009 | system not support | Android 系统特有，系统版本低于 4.3 不支持 BLE |
| 10012 | operate time out | 连接超时 |
| 10013 | invalid\_data | 连接 deviceId 为空或者是格式不正确 |

---

### Object wx.getBatteryInfoSync()

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/battery/wx.getBatteryInfoSync.html

**Object res**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| level | number | 设备电量，范围 1 - 100 |  |
| isCharging | boolean | 是否正在充电中 |  |
| isLowPowerModeEnabled | boolean | 是否处于省电模式 | [3.5.0](../../../guide/runtime/client-lib/compatibility.html) |

---

### wx.getBatteryInfo(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/battery/wx.getBatteryInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| level | number | 设备电量，范围 1 - 100 |  |
| isCharging | boolean | 是否正在充电中 |  |
| isLowPowerModeEnabled | boolean | 是否处于省电模式 | [3.5.0](../../../guide/runtime/client-lib/compatibility.html) |

---

### wx.setClipboardData(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/clipboard/wx.setClipboardData.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| data | string |  | 是 | 剪贴板的内容 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.getClipboardData(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/clipboard/wx.getClipboardData.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | string | 剪贴板的内容 |

---

### wx.onGamepadDisconnected(function listener)

基础库 3.6.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/gamepad/wx.onGamepadDisconnected.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| gamepad | string | 本次断开的 Gamepad 实例。 |

---

### wx.onGamepadConnected(function listener)

基础库 3.6.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/gamepad/wx.onGamepadConnected.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| gamepad | string | 本次连接到的 Gamepad 实例。 |

---

### Array.<Object> wx.getGamepads()

基础库 3.6.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/gamepad/wx.getGamepads.html

**Array.<Object>**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 一个包含着控制器标识信息的 string |
| index | string | 一个自增的整形数字，对于当前连接到系统的每一个设备是唯一的 |
| connected | boolean | 控制器是否仍然连接着系统. |
| axes | Array.<object> | 一个表示控制器设备上存在的坐标轴的数组 (比如控制器摇杆)。 |
| buttons | Array.<object> | 设备上的按键的数组。 |

---

### wx.onNetworkWeakChange(function listener)

基础库 2.21.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/network/wx.onNetworkWeakChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| weakNet | boolean | 当前是否处于弱网状态 |
| networkType | string | 当前网络类型 |

---

### wx.onNetworkStatusChange(function listener)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/network/wx.onNetworkStatusChange.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | isConnected | boolean | 当前是否有网络连接 |
|  | networkType | string | 网络类型 |
|  | | 合法值 | 说明 | | --- | --- | | wifi | wifi 网络 | | 2g | 2g 网络 | | 3g | 3g 网络 | | 4g | 4g 网络 | | 5g | 5g 网络 | | unknown | Android 下不常见的网络类型 | | none | 无网络 | | | |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| wifi | wifi 网络 |
| 2g | 2g 网络 |
| 3g | 3g 网络 |
| 4g | 4g 网络 |
| 5g | 5g 网络 |
| unknown | Android 下不常见的网络类型 |
| none | 无网络 |

---

### wx.offNetworkWeakChange(function listener)

基础库 2.21.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/network/wx.offNetworkWeakChange.html

---

### wx.offNetworkStatusChange(function listener)

基础库 2.9.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/network/wx.offNetworkStatusChange.html

---

### wx.getNetworkType(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/network/wx.getNetworkType.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | networkType | string | 网络类型 |  |
|  | | 合法值 | 说明 | | --- | --- | | wifi | wifi 网络 | | 2g | 2g 网络 | | 3g | 3g 网络 | | 4g | 4g 网络 | | 5g | 5g 网络 | | unknown | Android 下不常见的网络类型 | | none | 无网络 | | | | |
|  | signalStrength | Number | 信号强弱，单位 dbm |  |
|  | hasSystemProxy | Boolean | 设备是否使用了网络代理 | [2.22.1](../../../guide/runtime/client-lib/compatibility.html) |
|  | weakNet | Boolean | 是否处于弱网环境 | [3.5.3](../../../guide/runtime/client-lib/compatibility.html) |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| wifi | wifi 网络 |
| 2g | 2g 网络 |
| 3g | 3g 网络 |
| 4g | 4g 网络 |
| 5g | 5g 网络 |
| unknown | Android 下不常见的网络类型 |
| none | 无网络 |

---

### wx.getLocalIPAddress(Object object)

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/network/wx.getLocalIPAddress.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |
| localip | string | 本机局域网IP地址 |
| netmask | string | 本机局域网子网掩码，基础库 2.24.0 开始支持 |

---

### wx.setVisualEffectOnCapture(Object object)

基础库 3.1.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/screen/wx.setVisualEffectOnCapture.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| visualEffect | string | none | 否 | 截屏/录屏时的表现，仅支持 none / hidden，传入 hidden 则表示在截屏/录屏时隐藏屏幕 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.setScreenBrightness(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/screen/wx.setScreenBrightness.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| value | number |  | 是 | 屏幕亮度值，范围 0 ~ 1，0 最暗，1 最亮。在安卓端支持传入特殊值 -1，表示屏幕亮度跟随系统变化 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.setKeepScreenOn(Object object)

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/screen/wx.setKeepScreenOn.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keepScreenOn | boolean |  | 是 | 是否保持屏幕常亮 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.onUserCaptureScreen(function listener)

基础库 2.8.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/screen/wx.onUserCaptureScreen.html

**function listener**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| query | string | 支持开发者自定义一键打开小程序时的 query | [3.3.0](../../../guide/runtime/client-lib/compatibility.html) |
| promise | promise | 如果该参数存在，则其它的参数将会以 resolve 结果为准，如果一秒内不 resolve，分享会使用上面传入的默认参数 | [3.3.0](../../../guide/runtime/client-lib/compatibility.html) |

---

### wx.onScreenRecordingStateChanged(function listener)

基础库 3.1.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/screen/wx.onScreenRecordingStateChanged.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | state | string | 录屏状态 |
|  | | 合法值 | 说明 | | --- | --- | | start | 开始录屏 | | stop | 结束录屏 | | | |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| start | 开始录屏 |
| stop | 结束录屏 |

---

### wx.offUserCaptureScreen()

基础库 2.9.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/screen/wx.offUserCaptureScreen.html

---

### wx.offScreenRecordingStateChanged(function listener)

基础库 3.1.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/screen/wx.offScreenRecordingStateChanged.html

---

### wx.getScreenRecordingState(Object object)

基础库 3.1.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/screen/wx.getScreenRecordingState.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | state | string | 录屏状态 |
|  | | 合法值 | 说明 | | --- | --- | | on | 开启 | | off | 关闭 | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| on | 开启 |
| off | 关闭 |

---

### wx.getScreenBrightness(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/screen/wx.getScreenBrightness.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| value | number | 屏幕亮度值，范围 0 ~ 1，0 最暗，1 最亮 |

---

### wx.stopAccelerometer(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/accelerometer/wx.stopAccelerometer.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.startAccelerometer(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/accelerometer/wx.startAccelerometer.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | interval | string | normal | 否 | 监听加速度数据回调函数的执行频率 | [2.1.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | game | 适用于更新游戏的回调频率，在 20ms/次 左右 | | ui | 适用于更新 UI 的回调频率，在 60ms/次 左右 | | normal | 普通的回调频率，在 200ms/次 左右 | | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| game | 适用于更新游戏的回调频率，在 20ms/次 左右 |
| ui | 适用于更新 UI 的回调频率，在 60ms/次 左右 |
| normal | 普通的回调频率，在 200ms/次 左右 |

---

### wx.onAccelerometerChange(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/accelerometer/wx.onAccelerometerChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| x | number | X 轴 |
| y | number | Y 轴 |
| z | number | Z 轴 |

---

### wx.offAccelerometerChange(function listener)

基础库 2.9.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/accelerometer/wx.offAccelerometerChange.html

---

### wx.stopCompass(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/compass/wx.stopCompass.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.startCompass(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/compass/wx.startCompass.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.onCompassChange(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/compass/wx.onCompassChange.html

**function listener**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| direction | number | 面对的方向度数 |  |
| accuracy | number/string | 精度 | [2.4.0](../../../guide/runtime/client-lib/compatibility.html) |

**accuracy 在 iOS/Android 的差异**

| 值 | 说明 |
| --- | --- |
| high | 高精度 |
| medium | 中等精度 |
| low | 低精度 |
| no-contact | 不可信，传感器失去连接 |
| unreliable | 不可信，原因未知 |
| unknow ${value} | 未知的精度枚举值，即该 Android 系统此时返回的表示精度的 value 不是一个标准的精度枚举值 |

---

### wx.offCompassChange(function listener)

基础库 2.9.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/compass/wx.offCompassChange.html

---

### wx.stopDeviceMotionListening(Object object)

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/motion/wx.stopDeviceMotionListening.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.startDeviceMotionListening(Object object)

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/motion/wx.startDeviceMotionListening.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | interval | string | normal | 否 | 监听设备方向的变化回调函数的执行频率 |
|  | | 合法值 | 说明 | | --- | --- | | game | 适用于更新游戏的回调频率，在 20ms/次 左右 | | ui | 适用于更新 UI 的回调频率，在 60ms/次 左右 | | normal | 普通的回调频率，在 200ms/次 左右 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| game | 适用于更新游戏的回调频率，在 20ms/次 左右 |
| ui | 适用于更新 UI 的回调频率，在 60ms/次 左右 |
| normal | 普通的回调频率，在 200ms/次 左右 |

---

### wx.onDeviceMotionChange(function listener)

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/motion/wx.onDeviceMotionChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| alpha | number | 当 手机坐标 X/Y 和 地球 X/Y 重合时，绕着 Z 轴转动的夹角为 alpha，范围值为 [0, 2\*PI)。逆时针转动为正。 |
| beta | number | 当手机坐标 Y/Z 和地球 Y/Z 重合时，绕着 X 轴转动的夹角为 beta。范围值为 [-1\*PI, PI) 。顶部朝着地球表面转动为正。也有可能朝着用户为正。 |
| gamma | number | 当手机 X/Z 和地球 X/Z 重合时，绕着 Y 轴转动的夹角为 gamma。范围值为 [-1\*PI/2, PI/2)。右边朝着地球表面转动为正。 |

---

### wx.offDeviceMotionChange(function listener)

基础库 2.9.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/motion/wx.offDeviceMotionChange.html

---

### wx.setDeviceOrientation(Object object)

基础库 2.26.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/orientation/wx.setDeviceOrientation.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | value | string |  | 是 | 表示切换为横屏还是竖屏 |
|  | | 合法值 | 说明 | | --- | --- | | landscape | 横屏 | | portrait | 竖屏 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| landscape | 横屏 |
| portrait | 竖屏 |

---

### wx.onDeviceOrientationChange(function listener)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/orientation/wx.onDeviceOrientationChange.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | value | string | 切换后的屏幕方向。 |
|  | | 合法值 | 说明 | | --- | --- | | landscape | 横屏正方向，以 HOME 键在屏幕右侧为正方向 | | landscapeReverse | 横屏反方向，以 HOME 键在屏幕左侧为反方向 | | | |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| landscape | 横屏正方向，以 HOME 键在屏幕右侧为正方向 |
| landscapeReverse | 横屏反方向，以 HOME 键在屏幕左侧为反方向 |

---

### wx.offDeviceOrientationChange(function listener)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/orientation/wx.offDeviceOrientationChange.html

---

### wx.stopGyroscope(Object object)

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/gyroscope/wx.stopGyroscope.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.startGyroscope(Object object)

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/gyroscope/wx.startGyroscope.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | interval | string | normal | 否 | 监听陀螺仪数据回调函数的执行频率 |
|  | | 合法值 | 说明 | | --- | --- | | game | 适用于更新游戏的回调频率，在 20ms/次 左右 | | ui | 适用于更新 UI 的回调频率，在 60ms/次 左右 | | normal | 普通的回调频率，在 200ms/次 左右 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| game | 适用于更新游戏的回调频率，在 20ms/次 左右 |
| ui | 适用于更新 UI 的回调频率，在 60ms/次 左右 |
| normal | 普通的回调频率，在 200ms/次 左右 |

---

### wx.onGyroscopeChange(function listener)

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/gyroscope/wx.onGyroscopeChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| x | number | x 轴的角速度 |
| y | number | y 轴的角速度 |
| z | number | z 轴的角速度 |

---

### wx.offGyroscopeChange(function listener)

基础库 2.9.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/gyroscope/wx.offGyroscopeChange.html

---

### wx.onMemoryWarning(function listener)

基础库 2.0.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/memory/wx.onMemoryWarning.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | level | number | 内存告警等级，只有 Android 才有，对应系统宏定义 |
|  | | 合法值 | 说明 | | --- | --- | | 5 | TRIM\_MEMORY\_RUNNING\_MODERATE | | 10 | TRIM\_MEMORY\_RUNNING\_LOW | | 15 | TRIM\_MEMORY\_RUNNING\_CRITICAL | | | |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| 5 | TRIM\_MEMORY\_RUNNING\_MODERATE |
| 10 | TRIM\_MEMORY\_RUNNING\_LOW |
| 15 | TRIM\_MEMORY\_RUNNING\_CRITICAL |

---

### wx.offMemoryWarning(function listener)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/memory/wx.offMemoryWarning.html

---

### wx.scanCode(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/scan/wx.scanCode.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | onlyFromCamera | boolean | false | 否 | 是否只能从相机扫码，不允许从相册选择图片 | [1.2.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | scanType | Array.<string> | ['barCode', 'qrCode', 'wxCode'] | 否 | 扫码类型 | [1.7.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | barCode | 一维码 | | qrCode | 二维码 | | wxCode | 小程序码 | | datamatrix | Data Matrix 码 | | pdf417 | PDF417 条码 | | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| barCode | 一维码 |
| qrCode | 二维码 |
| wxCode | 小程序码 |
| datamatrix | Data Matrix 码 |
| pdf417 | PDF417 条码 |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | result | string | 所扫码的内容 |
|  | scanType | string | 所扫码的类型 |
|  | | 合法值 | 说明 | | --- | --- | | QR\_CODE | 二维码 | | AZTEC | 一维码 | | CODABAR | 一维码 | | CODE\_39 | 一维码 | | CODE\_93 | 一维码 | | CODE\_128 | 一维码 | | DATA\_MATRIX | 二维码 | | EAN\_8 | 一维码 | | EAN\_13 | 一维码 | | ITF | 一维码 | | MAXICODE | 一维码 | | PDF\_417 | 二维码 | | RSS\_14 | 一维码 | | RSS\_EXPANDED | 一维码 | | UPC\_A | 一维码 | | UPC\_E | 一维码 | | UPC\_EAN\_EXTENSION | 一维码 | | WX\_CODE | 二维码 | | CODE\_25 | 一维码 | | | |
|  | charSet | string | 所扫码的字符集 |
|  | path | string | 当所扫的码为当前小程序二维码时，会返回此字段，内容为二维码携带的 path |
|  | rawData | string | 原始数据，base64编码 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| QR\_CODE | 二维码 |
| AZTEC | 一维码 |
| CODABAR | 一维码 |
| CODE\_39 | 一维码 |
| CODE\_93 | 一维码 |
| CODE\_128 | 一维码 |
| DATA\_MATRIX | 二维码 |
| EAN\_8 | 一维码 |
| EAN\_13 | 一维码 |
| ITF | 一维码 |
| MAXICODE | 一维码 |
| PDF\_417 | 二维码 |
| RSS\_14 | 一维码 |
| RSS\_EXPANDED | 一维码 |
| UPC\_A | 一维码 |
| UPC\_E | 一维码 |
| UPC\_EAN\_EXTENSION | 一维码 |
| WX\_CODE | 二维码 |
| CODE\_25 | 一维码 |

---

### wx.vibrateShort(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/vibrate/wx.vibrateShort.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| type | string |  | 是 | 震动强度类型，有效值为：heavy、medium、light | [2.13.0](../../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | errMsg | string | 错误信息 |
|  | | 合法值 | 说明 | | --- | --- | | style is not support | 当前设备不支持设置震动等级 | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| style is not support | 当前设备不支持设置震动等级 |

---

### wx.vibrateLong(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/device/vibrate/wx.vibrateLong.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

<!-- pages: 132 -->
