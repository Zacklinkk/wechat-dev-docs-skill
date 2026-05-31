# 微信小程序 API 结构化参考 — base

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.env

相关文档:文件系统

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/wx.env.html

---

### boolean wx.canIUse(string schema)

基础库 1.1.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/wx.canIUse.html

---

### ArrayBuffer wx.base64ToArrayBuffer(string base64)

从基础库2.4.0开始，本接口停止维护

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/wx.base64ToArrayBuffer.html

---

### string wx.arrayBufferToBase64(ArrayBuffer arrayBuffer)

从基础库2.4.0开始，本接口停止维护

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/wx.arrayBufferToBase64.html

---

### wx.openSystemBluetoothSetting(Object object)

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.openSystemBluetoothSetting.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.openAppAuthorizeSetting(Object object)

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.openAppAuthorizeSetting.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### Object wx.getWindowInfo()

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getWindowInfo.html

**Object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | pixelRatio | number | 设备像素比 |
|  | screenWidth | number | 屏幕宽度，单位px |
|  | screenHeight | number | 屏幕高度，单位px |
|  | windowWidth | number | 可使用窗口宽度，单位px |
|  | windowHeight | number | 可使用窗口高度，单位px |
|  | statusBarHeight | number | 状态栏的高度，单位px |
|  | safeArea | Object | 在竖屏正方向下的安全区域。部分机型没有安全区域概念，也不会返回 safeArea 字段，开发者需自行兼容。 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | left | number | 安全区域左上角横坐标 | |  | right | number | 安全区域右下角横坐标 | |  | top | number | 安全区域左上角纵坐标 | |  | bottom | number | 安全区域右下角纵坐标 | |  | width | number | 安全区域的宽度，单位逻辑像素 | |  | height | number | 安全区域的高度，单位逻辑像素 | | | |
|  | screenTop | number | 窗口上边缘的y值 |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | left | number | 安全区域左上角横坐标 |
|  | right | number | 安全区域右下角横坐标 |
|  | top | number | 安全区域左上角纵坐标 |
|  | bottom | number | 安全区域右下角纵坐标 |
|  | width | number | 安全区域的宽度，单位逻辑像素 |
|  | height | number | 安全区域的高度，单位逻辑像素 |

---

### Object wx.getSystemSetting()

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getSystemSetting.html

**Object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | bluetoothEnabled | boolean | 蓝牙的系统开关 |
|  | locationEnabled | boolean | 地理位置的系统开关 |
|  | wifiEnabled | boolean | Wi-Fi 的系统开关 |
|  | deviceOrientation | string | 设备方向（注意：IOS客户端横屏游戏获取deviceOrientation可能不准，建议以屏幕宽高为准） |
|  | | 合法值 | 说明 | | --- | --- | | portrait | 竖屏 | | landscape | 横屏 | | | |

**Object**

| 合法值 | 说明 |
| --- | --- |
| portrait | 竖屏 |
| landscape | 横屏 |

---

### Object wx.getSystemInfoSync()

从基础库2.20.1开始，本接口停止维护，请使用wx.getSystemSetting、wx.getAppAuthorizeSetting、wx.getDeviceInfo、wx.getWindowInfo、wx.getAppBaseInfo代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getSystemInfoSync.html

**Object res**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | brand | string | 设备品牌 | [1.5.0](../../../framework/compatibility.html) |
|  | model | string | 设备型号。新机型刚推出一段时间会显示unknown，微信会尽快进行适配。 |  |
|  | pixelRatio | number | 设备像素比 |  |
|  | screenWidth | number | 屏幕宽度，单位px | [1.1.0](../../../framework/compatibility.html) |
|  | screenHeight | number | 屏幕高度，单位px | [1.1.0](../../../framework/compatibility.html) |
|  | windowWidth | number | 可使用窗口宽度，单位px |  |
|  | windowHeight | number | 可使用窗口高度，单位px |  |
|  | statusBarHeight | number | 状态栏的高度，单位px | [1.9.0](../../../framework/compatibility.html) |
|  | language | string | 微信设置的语言 |  |
|  | version | string | 微信版本号 |  |
|  | system | string | 操作系统及版本 |  |
|  | platform | string | 客户端平台 |  |
|  | | 合法值 | 说明 | | --- | --- | | ios | iOS微信（包含 iPhone、iPad） | | android | Android微信 | | ohos | HarmonyOS 手机端微信 | | ohos\_pc | HarmonyOS PC微信 | | windows | Windows微信 | | mac | macOS微信 | | devtools | 微信开发者工具 | | | | |
|  | fontSizeSetting | number | 用户字体大小（单位px）。以微信客户端「我-设置-通用-字体大小」中的设置为准 | [1.5.0](../../../framework/compatibility.html) |
|  | SDKVersion | string | 客户端基础库版本 | [1.1.0](../../../framework/compatibility.html) |
|  | benchmarkLevel | number | 设备性能等级（仅 Android）。取值为：-2 或 0（该设备无法运行小游戏），-1（性能未知），>=1（设备性能值，该值越高，设备性能越好）  注意：性能等级当前仅反馈真机机型，暂不支持 IDE 模拟器机型 | [1.8.0](../../../framework/compatibility.html) |
|  | albumAuthorized | boolean | 允许微信使用相册的开关（仅 iOS 有效） | [2.6.0](../../../framework/compatibility.html) |
|  | cameraAuthorized | boolean | 允许微信使用摄像头的开关 | [2.6.0](../../../framework/compatibility.html) |
|  | locationAuthorized | boolean | 允许微信使用定位的开关 | [2.6.0](../../../framework/compatibility.html) |
|  | microphoneAuthorized | boolean | 允许微信使用麦克风的开关 | [2.6.0](../../../framework/compatibility.html) |
|  | notificationAuthorized | boolean | 允许微信通知的开关 | [2.6.0](../../../framework/compatibility.html) |
|  | notificationAlertAuthorized | boolean | 允许微信通知带有提醒的开关（仅 iOS 有效） | [2.6.0](../../../framework/compatibility.html) |
|  | notificationBadgeAuthorized | boolean | 允许微信通知带有标记的开关（仅 iOS 有效） | [2.6.0](../../../framework/compatibility.html) |
|  | notificationSoundAuthorized | boolean | 允许微信通知带有声音的开关（仅 iOS 有效） | [2.6.0](../../../framework/compatibility.html) |
|  | phoneCalendarAuthorized | boolean | 允许微信使用日历的开关 | [2.19.3](../../../framework/compatibility.html) |
|  | bluetoothEnabled | boolean | 蓝牙的系统开关 | [2.6.0](../../../framework/compatibility.html) |
|  | locationEnabled | boolean | 地理位置的系统开关 | [2.6.0](../../../framework/compatibility.html) |
|  | wifiEnabled | boolean | Wi-Fi 的系统开关 | [2.6.0](../../../framework/compatibility.html) |
|  | safeArea | Object | 在竖屏正方向下的安全区域。部分机型没有安全区域概念，也不会返回 safeArea 字段，开发者需自行兼容。 | [2.7.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | left | number | 安全区域左上角横坐标 | |  | right | number | 安全区域右下角横坐标 | |  | top | number | 安全区域左上角纵坐标 | |  | bottom | number | 安全区域右下角纵坐标 | |  | width | number | 安全区域的宽度，单位逻辑像素 | |  | height | number | 安全区域的高度，单位逻辑像素 | | | | |
|  | locationReducedAccuracy | boolean | `true` 表示模糊定位，`false` 表示精确定位，仅 iOS 支持 |  |
|  | theme | string | 系统当前主题，取值为`light`或`dark`，全局配置`"darkmode":true`时才能获取，否则为 undefined （不支持小游戏） | [2.11.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | dark | 深色主题 | | light | 浅色主题 | | | | |
|  | host | Object | 当前小程序运行的宿主环境 | [2.12.3](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 宿主 app 对应的 appId | | | | |
|  | enableDebug | boolean | 是否已打开调试。可通过右上角菜单或 [wx.setEnableDebug](../debug/wx.setEnableDebug.html) 打开调试。 | [2.15.0](../../../framework/compatibility.html) |
|  | deviceOrientation | string | 设备方向（注意：IOS客户端横屏游戏获取deviceOrientation可能不准，建议以屏幕宽高为准） |  |
|  | | 合法值 | 说明 | | --- | --- | | portrait | 竖屏 | | landscape | 横屏 | | | | |

**Object res**

| 合法值 | 说明 |
| --- | --- |
| ios | iOS微信（包含 iPhone、iPad） |
| android | Android微信 |
| ohos | HarmonyOS 手机端微信 |
| ohos\_pc | HarmonyOS PC微信 |
| windows | Windows微信 |
| mac | macOS微信 |
| devtools | 微信开发者工具 |

**Object res**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | left | number | 安全区域左上角横坐标 |
|  | right | number | 安全区域右下角横坐标 |
|  | top | number | 安全区域左上角纵坐标 |
|  | bottom | number | 安全区域右下角纵坐标 |
|  | width | number | 安全区域的宽度，单位逻辑像素 |
|  | height | number | 安全区域的高度，单位逻辑像素 |

**Object res**

| 合法值 | 说明 |
| --- | --- |
| dark | 深色主题 |
| light | 浅色主题 |

**Object res**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | appId | string | 宿主 app 对应的 appId |

**Object res**

| 合法值 | 说明 |
| --- | --- |
| portrait | 竖屏 |
| landscape | 横屏 |

---

### wx.getSystemInfoAsync(Object object)

从基础库2.20.1开始，本接口停止维护，请使用wx.getSystemSetting、wx.getAppAuthorizeSetting、wx.getDeviceInfo、wx.getWindowInfo、wx.getAppBaseInfo代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getSystemInfoAsync.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | brand | string | 设备品牌 | [1.5.0](../../../framework/compatibility.html) |
|  | model | string | 设备型号。新机型刚推出一段时间会显示unknown，微信会尽快进行适配。 |  |
|  | pixelRatio | number | 设备像素比 |  |
|  | screenWidth | number | 屏幕宽度，单位px | [1.1.0](../../../framework/compatibility.html) |
|  | screenHeight | number | 屏幕高度，单位px | [1.1.0](../../../framework/compatibility.html) |
|  | windowWidth | number | 可使用窗口宽度，单位px |  |
|  | windowHeight | number | 可使用窗口高度，单位px |  |
|  | statusBarHeight | number | 状态栏的高度，单位px | [1.9.0](../../../framework/compatibility.html) |
|  | language | string | 微信设置的语言 |  |
|  | version | string | 微信版本号 |  |
|  | system | string | 操作系统及版本 |  |
|  | platform | string | 客户端平台 |  |
|  | | 合法值 | 说明 | | --- | --- | | ios | iOS微信（包含 iPhone、iPad） | | android | Android微信 | | ohos | HarmonyOS 手机端微信 | | ohos\_pc | HarmonyOS PC微信 | | windows | Windows微信 | | mac | macOS微信 | | devtools | 微信开发者工具 | | | | |
|  | fontSizeSetting | number | 用户字体大小（单位px）。以微信客户端「我-设置-通用-字体大小」中的设置为准 | [1.5.0](../../../framework/compatibility.html) |
|  | SDKVersion | string | 客户端基础库版本 | [1.1.0](../../../framework/compatibility.html) |
|  | benchmarkLevel | number | 设备性能等级（仅 Android）。取值为：-2 或 0（该设备无法运行小游戏），-1（性能未知），>=1（设备性能值，该值越高，设备性能越好）  注意：性能等级当前仅反馈真机机型，暂不支持 IDE 模拟器机型 | [1.8.0](../../../framework/compatibility.html) |
|  | albumAuthorized | boolean | 允许微信使用相册的开关（仅 iOS 有效） | [2.6.0](../../../framework/compatibility.html) |
|  | cameraAuthorized | boolean | 允许微信使用摄像头的开关 | [2.6.0](../../../framework/compatibility.html) |
|  | locationAuthorized | boolean | 允许微信使用定位的开关 | [2.6.0](../../../framework/compatibility.html) |
|  | microphoneAuthorized | boolean | 允许微信使用麦克风的开关 | [2.6.0](../../../framework/compatibility.html) |
|  | notificationAuthorized | boolean | 允许微信通知的开关 | [2.6.0](../../../framework/compatibility.html) |
|  | notificationAlertAuthorized | boolean | 允许微信通知带有提醒的开关（仅 iOS 有效） | [2.6.0](../../../framework/compatibility.html) |
|  | notificationBadgeAuthorized | boolean | 允许微信通知带有标记的开关（仅 iOS 有效） | [2.6.0](../../../framework/compatibility.html) |
|  | notificationSoundAuthorized | boolean | 允许微信通知带有声音的开关（仅 iOS 有效） | [2.6.0](../../../framework/compatibility.html) |
|  | phoneCalendarAuthorized | boolean | 允许微信使用日历的开关 | [2.19.3](../../../framework/compatibility.html) |
|  | bluetoothEnabled | boolean | 蓝牙的系统开关 | [2.6.0](../../../framework/compatibility.html) |
|  | locationEnabled | boolean | 地理位置的系统开关 | [2.6.0](../../../framework/compatibility.html) |
|  | wifiEnabled | boolean | Wi-Fi 的系统开关 | [2.6.0](../../../framework/compatibility.html) |
|  | safeArea | Object | 在竖屏正方向下的安全区域。部分机型没有安全区域概念，也不会返回 safeArea 字段，开发者需自行兼容。 | [2.7.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | left | number | 安全区域左上角横坐标 | |  | right | number | 安全区域右下角横坐标 | |  | top | number | 安全区域左上角纵坐标 | |  | bottom | number | 安全区域右下角纵坐标 | |  | width | number | 安全区域的宽度，单位逻辑像素 | |  | height | number | 安全区域的高度，单位逻辑像素 | | | | |
|  | locationReducedAccuracy | boolean | `true` 表示模糊定位，`false` 表示精确定位，仅 iOS 支持 |  |
|  | theme | string | 系统当前主题，取值为`light`或`dark`，全局配置`"darkmode":true`时才能获取，否则为 undefined （不支持小游戏） | [2.11.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | dark | 深色主题 | | light | 浅色主题 | | | | |
|  | host | Object | 当前小程序运行的宿主环境 | [2.12.3](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 宿主 app 对应的 appId | | | | |
|  | enableDebug | boolean | 是否已打开调试。可通过右上角菜单或 [wx.setEnableDebug](../debug/wx.setEnableDebug.html) 打开调试。 | [2.15.0](../../../framework/compatibility.html) |
|  | deviceOrientation | string | 设备方向（注意：IOS客户端横屏游戏获取deviceOrientation可能不准，建议以屏幕宽高为准） |  |
|  | | 合法值 | 说明 | | --- | --- | | portrait | 竖屏 | | landscape | 横屏 | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| ios | iOS微信（包含 iPhone、iPad） |
| android | Android微信 |
| ohos | HarmonyOS 手机端微信 |
| ohos\_pc | HarmonyOS PC微信 |
| windows | Windows微信 |
| mac | macOS微信 |
| devtools | 微信开发者工具 |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | left | number | 安全区域左上角横坐标 |
|  | right | number | 安全区域右下角横坐标 |
|  | top | number | 安全区域左上角纵坐标 |
|  | bottom | number | 安全区域右下角纵坐标 |
|  | width | number | 安全区域的宽度，单位逻辑像素 |
|  | height | number | 安全区域的高度，单位逻辑像素 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| dark | 深色主题 |
| light | 浅色主题 |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | appId | string | 宿主 app 对应的 appId |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| portrait | 竖屏 |
| landscape | 横屏 |

---

### wx.getSystemInfo(Object object)

从基础库2.20.1开始，本接口停止维护，请使用wx.getSystemSetting、wx.getAppAuthorizeSetting、wx.getDeviceInfo、wx.getWindowInfo、wx.getAppBaseInfo代替

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getSystemInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | brand | string | 设备品牌 | [1.5.0](../../../framework/compatibility.html) |
|  | model | string | 设备型号。新机型刚推出一段时间会显示unknown，微信会尽快进行适配。 |  |
|  | pixelRatio | number | 设备像素比 |  |
|  | screenWidth | number | 屏幕宽度，单位px | [1.1.0](../../../framework/compatibility.html) |
|  | screenHeight | number | 屏幕高度，单位px | [1.1.0](../../../framework/compatibility.html) |
|  | windowWidth | number | 可使用窗口宽度，单位px |  |
|  | windowHeight | number | 可使用窗口高度，单位px |  |
|  | statusBarHeight | number | 状态栏的高度，单位px | [1.9.0](../../../framework/compatibility.html) |
|  | language | string | 微信设置的语言 |  |
|  | version | string | 微信版本号 |  |
|  | system | string | 操作系统及版本 |  |
|  | platform | string | 客户端平台 |  |
|  | | 合法值 | 说明 | | --- | --- | | ios | iOS微信（包含 iPhone、iPad） | | android | Android微信 | | ohos | HarmonyOS 手机端微信 | | ohos\_pc | HarmonyOS PC微信 | | windows | Windows微信 | | mac | macOS微信 | | devtools | 微信开发者工具 | | | | |
|  | fontSizeSetting | number | 用户字体大小（单位px）。以微信客户端「我-设置-通用-字体大小」中的设置为准 | [1.5.0](../../../framework/compatibility.html) |
|  | SDKVersion | string | 客户端基础库版本 | [1.1.0](../../../framework/compatibility.html) |
|  | benchmarkLevel | number | 设备性能等级（仅 Android）。取值为：-2 或 0（该设备无法运行小游戏），-1（性能未知），>=1（设备性能值，该值越高，设备性能越好）  注意：性能等级当前仅反馈真机机型，暂不支持 IDE 模拟器机型 | [1.8.0](../../../framework/compatibility.html) |
|  | albumAuthorized | boolean | 允许微信使用相册的开关（仅 iOS 有效） | [2.6.0](../../../framework/compatibility.html) |
|  | cameraAuthorized | boolean | 允许微信使用摄像头的开关 | [2.6.0](../../../framework/compatibility.html) |
|  | locationAuthorized | boolean | 允许微信使用定位的开关 | [2.6.0](../../../framework/compatibility.html) |
|  | microphoneAuthorized | boolean | 允许微信使用麦克风的开关 | [2.6.0](../../../framework/compatibility.html) |
|  | notificationAuthorized | boolean | 允许微信通知的开关 | [2.6.0](../../../framework/compatibility.html) |
|  | notificationAlertAuthorized | boolean | 允许微信通知带有提醒的开关（仅 iOS 有效） | [2.6.0](../../../framework/compatibility.html) |
|  | notificationBadgeAuthorized | boolean | 允许微信通知带有标记的开关（仅 iOS 有效） | [2.6.0](../../../framework/compatibility.html) |
|  | notificationSoundAuthorized | boolean | 允许微信通知带有声音的开关（仅 iOS 有效） | [2.6.0](../../../framework/compatibility.html) |
|  | phoneCalendarAuthorized | boolean | 允许微信使用日历的开关 | [2.19.3](../../../framework/compatibility.html) |
|  | bluetoothEnabled | boolean | 蓝牙的系统开关 | [2.6.0](../../../framework/compatibility.html) |
|  | locationEnabled | boolean | 地理位置的系统开关 | [2.6.0](../../../framework/compatibility.html) |
|  | wifiEnabled | boolean | Wi-Fi 的系统开关 | [2.6.0](../../../framework/compatibility.html) |
|  | safeArea | Object | 在竖屏正方向下的安全区域。部分机型没有安全区域概念，也不会返回 safeArea 字段，开发者需自行兼容。 | [2.7.0](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | left | number | 安全区域左上角横坐标 | |  | right | number | 安全区域右下角横坐标 | |  | top | number | 安全区域左上角纵坐标 | |  | bottom | number | 安全区域右下角纵坐标 | |  | width | number | 安全区域的宽度，单位逻辑像素 | |  | height | number | 安全区域的高度，单位逻辑像素 | | | | |
|  | locationReducedAccuracy | boolean | `true` 表示模糊定位，`false` 表示精确定位，仅 iOS 支持 |  |
|  | theme | string | 系统当前主题，取值为`light`或`dark`，全局配置`"darkmode":true`时才能获取，否则为 undefined （不支持小游戏） | [2.11.0](../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | dark | 深色主题 | | light | 浅色主题 | | | | |
|  | host | Object | 当前小程序运行的宿主环境 | [2.12.3](../../../framework/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 宿主 app 对应的 appId | | | | |
|  | enableDebug | boolean | 是否已打开调试。可通过右上角菜单或 [wx.setEnableDebug](../debug/wx.setEnableDebug.html) 打开调试。 | [2.15.0](../../../framework/compatibility.html) |
|  | deviceOrientation | string | 设备方向（注意：IOS客户端横屏游戏获取deviceOrientation可能不准，建议以屏幕宽高为准） |  |
|  | | 合法值 | 说明 | | --- | --- | | portrait | 竖屏 | | landscape | 横屏 | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| ios | iOS微信（包含 iPhone、iPad） |
| android | Android微信 |
| ohos | HarmonyOS 手机端微信 |
| ohos\_pc | HarmonyOS PC微信 |
| windows | Windows微信 |
| mac | macOS微信 |
| devtools | 微信开发者工具 |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | left | number | 安全区域左上角横坐标 |
|  | right | number | 安全区域右下角横坐标 |
|  | top | number | 安全区域左上角纵坐标 |
|  | bottom | number | 安全区域右下角纵坐标 |
|  | width | number | 安全区域的宽度，单位逻辑像素 |
|  | height | number | 安全区域的高度，单位逻辑像素 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| dark | 深色主题 |
| light | 浅色主题 |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | appId | string | 宿主 app 对应的 appId |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| portrait | 竖屏 |
| landscape | 横屏 |

---

### Object wx.getSkylineInfoSync()

基础库 2.26.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getSkylineInfoSync.html

**Object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | isSupported | boolean | 当前运行环境是否支持 [Skyline 渲染引擎](../../../framework/runtime/skyline/introduction.html) |
|  | version | string | 当前运行环境 [Skyline 渲染引擎](../../../framework/runtime/skyline/introduction.html) 的版本号，形如 `0.9.7` |
|  | reason | string | 当前运行环境不支持 [Skyline 渲染引擎](../../../framework/runtime/skyline/introduction.html) 的原因，仅在 `isSupported` 为 `false` 时出现 |
|  | | 合法值 | 说明 | | --- | --- | | client not supported | 当前微信客户端不支持 [Skyline 渲染引擎](../../../framework/runtime/skyline/introduction.html)，可以尝试通过升级微信客户端解决 | | baselib not supported | 当前基础库不支持 [Skyline 渲染引擎](../../../framework/runtime/skyline/introduction.html)，基础库会自动更新到当前客户端所能支持的最新的版本，基础库不支持时也可以尝试通过升级微信客户端解决 | | a-b test not enabled | 命中了 \_We 分析\_ 平台上的 AB 实验关闭的情况。详细可以查看 [Skyline 起步 > 配置 We 分析 AB 实验](../../../framework/custom-component/glass-easel/migration.html#%E9%85%8D%E7%BD%AE-We-%E5%88%86%E6%9E%90-AB-%E5%AE%9E%E9%AA%8C) 一节 | | SwitchRender option set to webview | 本地调试的快捷切换入口被设置为了强制使用 Webview. 详情可以查看 [Skyline 起步 > 快捷切换入口](../../../framework/custom-component/glass-easel/migration.html#快捷切换入口) 一节 | | | |

**Object**

| 合法值 | 说明 |
| --- | --- |
| client not supported | 当前微信客户端不支持 [Skyline 渲染引擎](../../../framework/runtime/skyline/introduction.html)，可以尝试通过升级微信客户端解决 |
| baselib not supported | 当前基础库不支持 [Skyline 渲染引擎](../../../framework/runtime/skyline/introduction.html)，基础库会自动更新到当前客户端所能支持的最新的版本，基础库不支持时也可以尝试通过升级微信客户端解决 |
| a-b test not enabled | 命中了 \_We 分析\_ 平台上的 AB 实验关闭的情况。详细可以查看 [Skyline 起步 > 配置 We 分析 AB 实验](../../../framework/custom-component/glass-easel/migration.html#%E9%85%8D%E7%BD%AE-We-%E5%88%86%E6%9E%90-AB-%E5%AE%9E%E9%AA%8C) 一节 |
| SwitchRender option set to webview | 本地调试的快捷切换入口被设置为了强制使用 Webview. 详情可以查看 [Skyline 起步 > 快捷切换入口](../../../framework/custom-component/glass-easel/migration.html#快捷切换入口) 一节 |

---

### wx.getSkylineInfo(Object object)

基础库 2.26.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getSkylineInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | isSupported | boolean | 当前运行环境是否支持 [Skyline 渲染引擎](../../../framework/runtime/skyline/introduction.html) |
|  | version | string | 当前运行环境 [Skyline 渲染引擎](../../../framework/runtime/skyline/introduction.html) 的版本号，形如 `0.9.7` |
|  | reason | string | 当前运行环境不支持 [Skyline 渲染引擎](../../../framework/runtime/skyline/introduction.html) 的原因，仅在 `isSupported` 为 `false` 时出现 |
|  | | 合法值 | 说明 | | --- | --- | | client not supported | 当前微信客户端不支持 [Skyline 渲染引擎](../../../framework/runtime/skyline/introduction.html)，可以尝试通过升级微信客户端解决 | | baselib not supported | 当前基础库不支持 [Skyline 渲染引擎](../../../framework/runtime/skyline/introduction.html)，基础库会自动更新到当前客户端所能支持的最新的版本，基础库不支持时也可以尝试通过升级微信客户端解决 | | a-b test not enabled | 命中了 \_We 分析\_ 平台上的 AB 实验关闭的情况。详细可以查看 [Skyline 起步 > 配置 We 分析 AB 实验](../../../framework/custom-component/glass-easel/migration.html#%E9%85%8D%E7%BD%AE-We-%E5%88%86%E6%9E%90-AB-%E5%AE%9E%E9%AA%8C) 一节 | | SwitchRender option set to webview | 本地调试的快捷切换入口被设置为了强制使用 Webview. 详情可以查看 [Skyline 起步 > 快捷切换入口](../../../framework/custom-component/glass-easel/migration.html#快捷切换入口) 一节 | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| client not supported | 当前微信客户端不支持 [Skyline 渲染引擎](../../../framework/runtime/skyline/introduction.html)，可以尝试通过升级微信客户端解决 |
| baselib not supported | 当前基础库不支持 [Skyline 渲染引擎](../../../framework/runtime/skyline/introduction.html)，基础库会自动更新到当前客户端所能支持的最新的版本，基础库不支持时也可以尝试通过升级微信客户端解决 |
| a-b test not enabled | 命中了 \_We 分析\_ 平台上的 AB 实验关闭的情况。详细可以查看 [Skyline 起步 > 配置 We 分析 AB 实验](../../../framework/custom-component/glass-easel/migration.html#%E9%85%8D%E7%BD%AE-We-%E5%88%86%E6%9E%90-AB-%E5%AE%9E%E9%AA%8C) 一节 |
| SwitchRender option set to webview | 本地调试的快捷切换入口被设置为了强制使用 Webview. 详情可以查看 [Skyline 起步 > 快捷切换入口](../../../framework/custom-component/glass-easel/migration.html#快捷切换入口) 一节 |

---

### Promise wx.getRendererUserAgent(Object object)

基础库 2.26.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getRendererUserAgent.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### Object wx.getDeviceInfo()

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getDeviceInfo.html

**Object**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | abi | string | 应用（微信APP）二进制接口类型（仅 Android 支持） |  |
|  | deviceAbi | string | 设备二进制接口类型（仅 Android 支持） | [2.25.1](../../../framework/compatibility.html) |
|  | benchmarkLevel | number | 设备性能等级（仅 Android 支持）。取值为：-2 或 0（该设备无法运行小游戏），-1（性能未知），>=1（设备性能值，该值越高，设备性能越好，目前最高不到50）  注意：从基础库3.4.5开始，本返回值停止维护，请使用[wx.getDeviceBenchmarkInfo](wx.getDeviceBenchmarkInfo.html)获取设备性能等级 |  |
|  | brand | string | 设备品牌 |  |
|  | model | string | 设备型号。新机型刚推出一段时间会显示unknown，微信会尽快进行适配。 |  |
|  | system | string | 操作系统及版本 |  |
|  | platform | string | 客户端平台 |  |
|  | | 合法值 | 说明 | | --- | --- | | ios | iOS微信（包含 iPhone、iPad） | | android | Android微信 | | ohos | HarmonyOS 手机端微信 | | ohos\_pc | HarmonyOS PC微信 | | windows | Windows微信 | | mac | macOS微信 | | devtools | 微信开发者工具 | | | | |
|  | cpuType | string | 设备 CPU 型号（仅 Android 支持）（Tips: GPU 型号可通过 WebGLRenderingContext.getExtension('WEBGL\_debug\_renderer\_info') 来获取） | [2.29.0](../../../framework/compatibility.html) |
|  | memorySize | string | 设备内存大小，单位为 MB | [2.30.0](../../../framework/compatibility.html) |

**Object**

| 合法值 | 说明 |
| --- | --- |
| ios | iOS微信（包含 iPhone、iPad） |
| android | Android微信 |
| ohos | HarmonyOS 手机端微信 |
| ohos\_pc | HarmonyOS PC微信 |
| windows | Windows微信 |
| mac | macOS微信 |
| devtools | 微信开发者工具 |

---

### wx.getDeviceBenchmarkInfo(Object object)

基础库 3.4.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getDeviceBenchmarkInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| benchmarkLevel | number | 设备性能等级。-1（性能未知），>=1（设备性能值，该值越高，设备性能越好） 注意： 1. 设备的benchmarkLevel值不会随着时间的推移而变化，移动端设备目前最高不超过50 | [3.4.5](../../../framework/compatibility.html) |
| modelLevel | number | 设备机型档位。0（档位未知），1（高档机），2（中档机），3（低档机）  注意：设备的机型档位会随着时间的推移而变化，因此在使用时请谨慎对待；若业务逻辑依赖于机型档位，但担心受到机型档位变化的影响，请参考[设备档位映射文档](https://developers.weixin.qq.com/minigame/dev/guide/performance/perf-benchmarkLevel.html)自行判断机型档位 | [3.4.5](../../../framework/compatibility.html) |

---

### Object wx.getAppBaseInfo()

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getAppBaseInfo.html

**Object**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | SDKVersion | string | 客户端基础库版本 |  |
|  | enableDebug | boolean | 是否已打开调试。可通过右上角菜单或 [wx.setEnableDebug](../debug/wx.setEnableDebug.html) 打开调试。 |  |
|  | host | Object | 当前小程序运行的宿主环境 |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 宿主 app（第三方App） 对应的 appId （当小程序运行在第三方App环境时才返回） | | | | |
|  | language | string | 微信设置的语言 |  |
|  | version | string | 微信版本号 |  |
|  | PCKernelVersion | string | PC 内核版本号，仅在 PC 端存在该值 |  |
|  | theme | string | 系统当前主题，取值为`light`或`dark`，全局配置`"darkmode":true`时才能获取，否则为 undefined （不支持小游戏） |  |
|  | | 合法值 | 说明 | | --- | --- | | dark | 深色主题 | | light | 浅色主题 | | | | |
|  | fontSizeScaleFactor | number | 微信字体大小缩放比例 |  |
|  | fontSizeSetting | number | 微信字体大小，单位px | [2.23.4](../../../framework/compatibility.html) |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | appId | string | 宿主 app（第三方App） 对应的 appId （当小程序运行在第三方App环境时才返回） |

**Object**

| 合法值 | 说明 |
| --- | --- |
| dark | 深色主题 |
| light | 浅色主题 |

---

### Object wx.getAppAuthorizeSetting()

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getAppAuthorizeSetting.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| albumAuthorized | 'authorized'/'denied'/'not determined' | 允许微信使用相册的开关（仅 iOS 有效） |
| bluetoothAuthorized | 'authorized'/'denied'/'not determined' | 允许微信使用蓝牙的开关（安卓基础库 3.5.0 以上有效） |
| cameraAuthorized | 'authorized'/'denied'/'not determined' | 允许微信使用摄像头的开关 |
| locationAuthorized | 'authorized'/'denied'/'not determined' | 允许微信使用定位的开关 |
| locationReducedAccuracy | boolean | 定位准确度。true 表示模糊定位，false 表示精确定位（仅 iOS 有效） |
| microphoneAuthorized | 'authorized'/'denied'/'not determined' | 允许微信使用麦克风的开关 |
| notificationAuthorized | 'authorized'/'denied'/'not determined' | 允许微信通知的开关 |
| notificationAlertAuthorized | 'authorized'/'denied'/'not determined' | 允许微信通知带有提醒的开关（仅 iOS 有效） |
| notificationBadgeAuthorized | 'authorized'/'denied'/'not determined' | 允许微信通知带有标记的开关（仅 iOS 有效） |
| notificationSoundAuthorized | 'authorized'/'denied'/'not determined' | 允许微信通知带有声音的开关（仅 iOS 有效） |
| phoneCalendarAuthorized | 'authorized'/'denied'/'not determined' | 允许微信读写日历的开关 |

---

### wx.updateWeChatApp(Object object)

基础库 2.12.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/update/wx.updateWeChatApp.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### UpdateManager wx.getUpdateManager()

基础库 1.9.90 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/update/wx.getUpdateManager.html

---

### UpdateManager

UpdateManager 对象，用来管理更新，可通过wx.getUpdateManager接口获取实例。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/update/UpdateManager.html

---

### UpdateManager.applyUpdate()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/update/UpdateManager.applyUpdate.html

---

### UpdateManager.onCheckForUpdate(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/update/UpdateManager.onCheckForUpdate.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| hasUpdate | boolean | 是否有新版本 |

---

### UpdateManager.onUpdateFailed(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/update/UpdateManager.onUpdateFailed.html

---

### UpdateManager.onUpdateReady(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/update/UpdateManager.onUpdateReady.html

---

### wx.onApiCategoryChange(function listener)

基础库 2.33.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/life-cycle/wx.onApiCategoryChange.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | apiCategory | number | API 类别 |
|  | | 合法值 | 说明 | | --- | --- | | default | 默认类别 | | nativeFunctionalized | 原生功能化，视频号直播商品、商品橱窗等场景打开的小程序 | | browseOnly | 仅浏览，朋友圈快照页等场景打开的小程序 | | embedded | 内嵌，通过打开半屏小程序能力打开的小程序 | | chatTool | 聊天工具打开小程序 | | | |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| default | 默认类别 |
| nativeFunctionalized | 原生功能化，视频号直播商品、商品橱窗等场景打开的小程序 |
| browseOnly | 仅浏览，朋友圈快照页等场景打开的小程序 |
| embedded | 内嵌，通过打开半屏小程序能力打开的小程序 |
| chatTool | 聊天工具打开小程序 |

**不同 apiCategory 场景下的 API 限制**

|  | default | nativeFunctionalized | browseOnly | embedded | chatTool |
| --- | --- | --- | --- | --- | --- |
| openSetting |  |  | `X` |  |  |
| <button open-type="share"> |  | `X` | `X` | `X` | `X` |
| <button open-type="feedback"> |  |  | `X` |  |  |
| <button open-type="open-setting"> |  |  | `X` |  |  |
| navigateToMiniProgram |  | `X` | `X` |  | `X` |
| openEmbeddedMiniProgram |  | `X` | `X` | `X` | `X` |
| openOfficialAccountArticle |  |  |  |  | `X` |
| openChannelsUserProfile |  |  |  |  | `X` |
| ad |  |  |  |  | `X` |
| ad-custom |  |  |  |  | `X` |
| 小程序菜单分享 |  |  |  |  | `X` |

---

### wx.offApiCategoryChange(function listener)

基础库 2.33.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/life-cycle/wx.offApiCategoryChange.html

---

### Object wx.getLaunchOptionsSync()

基础库 2.1.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/life-cycle/wx.getLaunchOptionsSync.html

**Object**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | path | string | 启动小程序的路径 (代码包路径) |  |
|  | scene | number | 启动小程序的[场景值](../../../../framework/app-service/scene.html) |  |
|  | query | Record.<string, string> | 启动小程序的 query 参数 |  |
|  | shareTicket | string | shareTicket，详见[获取更多转发信息](../../../../framework/open-ability/share.html#获取更多转发信息) |  |
|  | referrerInfo | Object | 来源信息。从另一个小程序、公众号或 App 进入小程序时返回。否则返回 `{}`。(参见后文注意) |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 来源小程序、公众号或 App 的 appId | |  | extraData | Object | 来源小程序传过来的数据，scene=1037或1038时支持 | | | | |
|  | forwardMaterials | Array.<Object> | 打开的文件信息数组，只有从聊天素材场景打开（scene为1173）才会携带该参数 |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | type | string | 文件的mimetype类型 | |  | name | string | 文件名 | |  | path | string | 文件路径（如果是webview则是url） | |  | size | number | 文件大小 | | | | |
|  | chatType | number | 从微信群聊/单聊打开小程序时，chatType 表示具体微信群聊/单聊类型 |  |
|  | | 合法值 | 说明 | | --- | --- | | 1 | 微信联系人单聊 | | 2 | 企业微信联系人单聊 | | 3 | 普通微信群聊 | | 4 | 企业微信互通群聊 | | | | |
|  | hostExtraData | Object | 宿主传递的数据，第三方 app 中运行小程序时返回 |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | host\_scene | string | 宿主app对应的场景值 | | | | |
|  | apiCategory | string | API 类别 | [2.20.0](../../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | default | 默认类别 | | nativeFunctionalized | 原生功能化，视频号直播商品、商品橱窗等场景打开的小程序 | | browseOnly | 仅浏览，朋友圈快照页等场景打开的小程序 | | embedded | 内嵌，通过打开半屏小程序能力打开的小程序 | | chatTool | 聊天工具，通过打开聊天工具能力打开的小程序 | | | | |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | appId | string | 来源小程序、公众号或 App 的 appId |
|  | extraData | Object | 来源小程序传过来的数据，scene=1037或1038时支持 |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | type | string | 文件的mimetype类型 |
|  | name | string | 文件名 |
|  | path | string | 文件路径（如果是webview则是url） |
|  | size | number | 文件大小 |

**Object**

| 合法值 | 说明 |
| --- | --- |
| 1 | 微信联系人单聊 |
| 2 | 企业微信联系人单聊 |
| 3 | 普通微信群聊 |
| 4 | 企业微信互通群聊 |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | host\_scene | string | 宿主app对应的场景值 |

**Object**

| 合法值 | 说明 |
| --- | --- |
| default | 默认类别 |
| nativeFunctionalized | 原生功能化，视频号直播商品、商品橱窗等场景打开的小程序 |
| browseOnly | 仅浏览，朋友圈快照页等场景打开的小程序 |
| embedded | 内嵌，通过打开半屏小程序能力打开的小程序 |
| chatTool | 聊天工具，通过打开聊天工具能力打开的小程序 |

**返回有效 referrerInfo 的场景**

| 场景值 | 场景 | appId含义 |
| --- | --- | --- |
| 1020 | 公众号 profile 页相关小程序列表 | 来源公众号 |
| 1035 | 公众号自定义菜单 | 来源公众号 |
| 1036 | App 分享消息卡片 | 来源App |
| 1037 | 小程序打开小程序 | 来源小程序 |
| 1038 | 从另一个小程序返回 | 来源小程序 |
| 1043 | 公众号模板消息 | 来源公众号 |
| 1069 | 移动应用 | 来源App |

**不同 apiCategory 场景下的 API 限制**

|  | default | nativeFunctionalized | browseOnly | embedded |
| --- | --- | --- | --- | --- |
| navigateToMiniProgram |  | `X` | `X` |  |
| openSetting |  |  | `X` |  |
| <button open-type="share"> |  | `X` | `X` | `X` |
| <button open-type="feedback"> |  |  | `X` |  |
| <button open-type="open-setting"> |  |  | `X` |  |
| openEmbeddedMiniProgram |  | `X` | `X` | `X` |

---

### Object wx.getEnterOptionsSync()

基础库 2.9.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/life-cycle/wx.getEnterOptionsSync.html

**Object**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | path | string | 启动小程序的路径 (代码包路径) |  |
|  | scene | number | 启动小程序的[场景值](../../../../framework/app-service/scene.html) |  |
|  | query | Record.<string, string> | 启动小程序的 query 参数 |  |
|  | shareTicket | string | shareTicket，详见[获取更多转发信息](../../../../framework/open-ability/share.html#获取更多转发信息) |  |
|  | referrerInfo | Object | 来源信息。从另一个小程序、公众号或 App 进入小程序时返回。否则返回 `{}`。(参见后文注意) |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 来源小程序、公众号或 App 的 appId | |  | extraData | Object | 来源小程序传过来的数据，scene=1037或1038时支持 | | | | |
|  | forwardMaterials | Array.<Object> | 打开的文件信息数组，只有从聊天素材场景打开（scene为1173）才会携带该参数 |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | type | string | 文件的mimetype类型 | |  | name | string | 文件名 | |  | path | string | 文件路径（如果是webview则是url） | |  | size | number | 文件大小 | | | | |
|  | chatType | number | 从微信群聊/单聊打开小程序时，chatType 表示具体微信群聊/单聊类型 |  |
|  | | 合法值 | 说明 | | --- | --- | | 1 | 微信联系人单聊 | | 2 | 企业微信联系人单聊 | | 3 | 普通微信群聊 | | 4 | 企业微信互通群聊 | | | | |
|  | hostExtraData | Object | 宿主传递的数据，第三方 app 中运行小程序时返回 |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | host\_scene | string | 宿主app对应的场景值 | | | | |
|  | apiCategory | string | API 类别 | [2.20.0](../../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | default | 默认类别 | | nativeFunctionalized | 原生功能化，视频号直播商品、商品橱窗等场景打开的小程序 | | browseOnly | 仅浏览，朋友圈快照页等场景打开的小程序 | | embedded | 内嵌，通过打开半屏小程序能力打开的小程序 | | chatTool | 聊天工具，通过打开聊天工具能力打开的小程序 | | | | |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | appId | string | 来源小程序、公众号或 App 的 appId |
|  | extraData | Object | 来源小程序传过来的数据，scene=1037或1038时支持 |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | type | string | 文件的mimetype类型 |
|  | name | string | 文件名 |
|  | path | string | 文件路径（如果是webview则是url） |
|  | size | number | 文件大小 |

**Object**

| 合法值 | 说明 |
| --- | --- |
| 1 | 微信联系人单聊 |
| 2 | 企业微信联系人单聊 |
| 3 | 普通微信群聊 |
| 4 | 企业微信互通群聊 |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | host\_scene | string | 宿主app对应的场景值 |

**Object**

| 合法值 | 说明 |
| --- | --- |
| default | 默认类别 |
| nativeFunctionalized | 原生功能化，视频号直播商品、商品橱窗等场景打开的小程序 |
| browseOnly | 仅浏览，朋友圈快照页等场景打开的小程序 |
| embedded | 内嵌，通过打开半屏小程序能力打开的小程序 |
| chatTool | 聊天工具，通过打开聊天工具能力打开的小程序 |

**返回有效 referrerInfo 的场景**

| 场景值 | 场景 | appId含义 |
| --- | --- | --- |
| 1020 | 公众号 profile 页相关小程序列表 | 来源公众号 |
| 1035 | 公众号自定义菜单 | 来源公众号 |
| 1036 | App 分享消息卡片 | 来源App |
| 1037 | 小程序打开小程序 | 来源小程序 |
| 1038 | 从另一个小程序返回 | 来源小程序 |
| 1043 | 公众号模板消息 | 来源公众号 |

**不同 apiCategory 场景下的 API 限制**

|  | default | nativeFunctionalized | browseOnly | embedded | chatTool |
| --- | --- | --- | --- | --- | --- |
| openSetting |  |  | `X` |  |  |
| <button open-type="share"> |  | `X` | `X` | `X` | `X` |
| <button open-type="feedback"> |  |  | `X` |  |  |
| <button open-type="open-setting"> |  |  | `X` |  |  |
| navigateToMiniProgram |  | `X` | `X` |  | `X` |
| openEmbeddedMiniProgram |  | `X` | `X` | `X` | `X` |
| openOfficialAccountArticle |  |  |  |  | `X` |
| openChannelsUserProfile |  |  |  |  | `X` |
| ad |  |  |  |  | `X` |
| ad-custom |  |  |  |  | `X` |
| 小程序菜单分享 |  |  |  |  | `X` |

---

### string wx.getApiCategory()

基础库 2.33.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/life-cycle/wx.getApiCategory.html

**不同 apiCategory 场景下的 API 限制**

|  | default | nativeFunctionalized | browseOnly | embedded | chatTool |
| --- | --- | --- | --- | --- | --- |
| openSetting |  |  | `X` |  |  |
| <button open-type="share"> |  | `X` | `X` | `X` | `X` |
| <button open-type="feedback"> |  |  | `X` |  |  |
| <button open-type="open-setting"> |  |  | `X` |  |  |
| navigateToMiniProgram |  | `X` | `X` |  | `X` |
| openEmbeddedMiniProgram |  | `X` | `X` | `X` | `X` |
| openOfficialAccountArticle |  |  |  |  | `X` |
| openChannelsUserProfile |  |  |  |  | `X` |
| ad |  |  |  |  | `X` |
| ad-custom |  |  |  |  | `X` |
| 小程序菜单分享 |  |  |  |  | `X` |

---

### wx.postMessageToReferrerPage(Object object)

基础库 3.7.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.postMessageToReferrerPage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| extraData | Object |  | 否 | 需要返回的数据 |

---

### wx.postMessageToReferrerMiniProgram(Object object)

基础库 3.2.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.postMessageToReferrerMiniProgram.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| extraData | Object |  | 否 | 需要返回的数据 |

---

### wx.onUnhandledRejection(function listener)

基础库 2.10.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onUnhandledRejection.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| reason | string | 拒绝原因，一般是一个 Error 对象 |
| promise | Promise.<any> | 被拒绝的 Promise 对象 |

---

### wx.onThemeChange(function listener)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onThemeChange.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | theme | string | 系统当前的主题，取值为`light`或`dark` |
|  | | 合法值 | 说明 | | --- | --- | | dark | 深色主题 | | light | 浅色主题 | | | |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| dark | 深色主题 |
| light | 浅色主题 |

---

### wx.onPageNotFound(function listener)

基础库 2.1.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onPageNotFound.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| path | string | 不存在页面的路径 (代码包路径) |
| query | Record.<string, string> | 打开不存在页面的 query 参数 |
| isEntryPage | boolean | 是否本次启动的首个页面（例如从分享等入口进来，首个页面是开发者配置的分享页面） |

---

### wx.onLazyLoadError(function listener)

基础库 2.24.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onLazyLoadError.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| type | string | 'subpackage' 失败类型 |
| subpackage | Array | 异步组件所属的分包 |
| errMsg | string | 详细信息 |

---

### wx.onError(function listener)

基础库 2.1.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onError.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| message | string | 错误信息，包含堆栈 |

---

### wx.onAudioInterruptionEnd(function listener)

基础库 2.6.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onAudioInterruptionEnd.html

---

### wx.onAudioInterruptionBegin(function listener)

基础库 2.6.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onAudioInterruptionBegin.html

---

### wx.onAppShow(function listener)

基础库 2.1.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onAppShow.html

**function listener**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | path | string | 启动小程序的路径 (代码包路径) |  |
|  | scene | number | 启动小程序的[场景值](../../../../framework/app-service/scene.html) |  |
|  | query | Record.<string, string> | 启动小程序的 query 参数 |  |
|  | shareTicket | string | shareTicket，详见[获取更多转发信息](../../../../framework/open-ability/share.html#获取更多转发信息) |  |
|  | referrerInfo | Object | 来源信息。从另一个小程序、公众号或 App 进入小程序时返回。否则返回 `{}`。(参见后文注意) |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 来源小程序、公众号或 App 的 appId | |  | extraData | Object | 来源小程序传过来的数据，scene=1037或1038时支持 | | | | |
|  | forwardMaterials | Array.<Object> | 打开的文件信息数组，只有从聊天素材场景打开（scene为1173）才会携带该参数 |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | type | string | 文件的mimetype类型 | |  | name | string | 文件名 | |  | path | string | 文件路径（如果是webview则是url） | |  | size | number | 文件大小 | | | | |
|  | chatType | number | 从微信群聊/单聊打开小程序时，chatType 表示具体微信群聊/单聊类型 |  |
|  | | 合法值 | 说明 | | --- | --- | | 1 | 微信联系人单聊 | | 2 | 企业微信联系人单聊 | | 3 | 普通微信群聊 | | 4 | 企业微信互通群聊 | | | | |
|  | hostExtraData | Object | 宿主传递的数据，第三方 app 中运行小程序时返回 |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | host\_scene | string | 宿主app对应的场景值 | | | | |
|  | apiCategory | string | API 类别 | [2.20.0](../../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | default | 默认类别 | | nativeFunctionalized | 原生功能化，视频号直播商品、商品橱窗等场景打开的小程序 | | browseOnly | 仅浏览，朋友圈快照页等场景打开的小程序 | | embedded | 内嵌，通过打开半屏小程序能力打开的小程序 | | chatTool | 聊天工具，通过打开聊天工具能力打开的小程序 | | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | appId | string | 来源小程序、公众号或 App 的 appId |
|  | extraData | Object | 来源小程序传过来的数据，scene=1037或1038时支持 |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | type | string | 文件的mimetype类型 |
|  | name | string | 文件名 |
|  | path | string | 文件路径（如果是webview则是url） |
|  | size | number | 文件大小 |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| 1 | 微信联系人单聊 |
| 2 | 企业微信联系人单聊 |
| 3 | 普通微信群聊 |
| 4 | 企业微信互通群聊 |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | host\_scene | string | 宿主app对应的场景值 |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| default | 默认类别 |
| nativeFunctionalized | 原生功能化，视频号直播商品、商品橱窗等场景打开的小程序 |
| browseOnly | 仅浏览，朋友圈快照页等场景打开的小程序 |
| embedded | 内嵌，通过打开半屏小程序能力打开的小程序 |
| chatTool | 聊天工具，通过打开聊天工具能力打开的小程序 |

**返回有效 referrerInfo 的场景**

| 场景值 | 场景 | appId含义 |
| --- | --- | --- |
| 1020 | 公众号 profile 页相关小程序列表 | 来源公众号 |
| 1035 | 公众号自定义菜单 | 来源公众号 |
| 1036 | App 分享消息卡片 | 来源App |
| 1037 | 小程序打开小程序 | 来源小程序 |
| 1038 | 从另一个小程序返回 | 来源小程序 |
| 1043 | 公众号模板消息 | 来源公众号 |

**不同 apiCategory 场景下的 API 限制**

|  | default | nativeFunctionalized | browseOnly | embedded | chatTool |
| --- | --- | --- | --- | --- | --- |
| openSetting |  |  | `X` |  |  |
| <button open-type="share"> |  | `X` | `X` | `X` | `X` |
| <button open-type="feedback"> |  |  | `X` |  |  |
| <button open-type="open-setting"> |  |  | `X` |  |  |
| navigateToMiniProgram |  | `X` | `X` |  | `X` |
| openEmbeddedMiniProgram |  | `X` | `X` | `X` | `X` |
| openOfficialAccountArticle |  |  |  |  | `X` |
| openChannelsUserProfile |  |  |  |  | `X` |
| ad |  |  |  |  | `X` |
| ad-custom |  |  |  |  | `X` |
| 小程序菜单分享 |  |  |  |  | `X` |

---

### wx.onAppHide(function listener)

基础库 2.1.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onAppHide.html

**function listener**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | reason | number | 原因 | [3.5.7](../../../../framework/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 用户退出小程序 | | 1 | 进入其他小程序 | | 2 | 打开原生功能页 | | 3 | 其他 | | | | |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| 0 | 用户退出小程序 |
| 1 | 进入其他小程序 |
| 2 | 打开原生功能页 |
| 3 | 其他 |

---

### wx.offUnhandledRejection(function listener)

基础库 2.10.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.offUnhandledRejection.html

---

### wx.offThemeChange(function listener)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.offThemeChange.html

---

### wx.offPageNotFound(function listener)

基础库 2.1.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.offPageNotFound.html

---

### wx.offLazyLoadError(function listener)

基础库 2.24.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.offLazyLoadError.html

---

### wx.offError(function listener)

基础库 2.1.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.offError.html

---

### wx.offAudioInterruptionEnd(function listener)

基础库 2.6.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.offAudioInterruptionEnd.html

---

### wx.offAudioInterruptionBegin(function listener)

基础库 2.6.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.offAudioInterruptionBegin.html

---

### wx.offAppShow(function listener)

基础库 2.1.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.offAppShow.html

---

### wx.offAppHide(function listener)

基础库 2.1.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.offAppHide.html

---

### wx.onBeforePageUnload(function listener)

基础库 3.5.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onBeforePageUnload.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| path | string | 页面路径 |
| routeEventId | string | 路由事件 id |
| page | Object | 页面实例 |

---

### wx.onBeforePageLoad(function listener)

基础库 3.5.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onBeforePageLoad.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | path | string | 页面路径 |
|  | query | Object | 路由参数 |
|  | componentFramework | string | 组件框架 |
|  | | 合法值 | 说明 | | --- | --- | | exparser | 旧版小程序组件框架 | | glass-easel | 新版小程序组件框架 | | | |
|  | openType | string | 路由打开类型 |
|  | routeEventId | string | 路由事件 id |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| exparser | 旧版小程序组件框架 |
| glass-easel | 新版小程序组件框架 |

---

### wx.onBeforeAppRoute(function listener)

基础库 3.5.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onBeforeAppRoute.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | path | string | 页面路径 |
|  | query | Object | 路由参数 |
|  | renderer | string | 渲染引擎 |
|  | | 合法值 | 说明 | | --- | --- | | webview | Webview 渲染引擎 | | skyline | Skyline 渲染引擎 | | xr-frame | xr-frame 解决方案 | | | |
|  | openType | string | 路由打开类型 |
|  | webviewId | number | 当前页面 id |
|  | routeEventId | string | 路由事件 id |
|  | pipMode | string |  |
|  | | 合法值 | 说明 | | --- | --- | | min | 视频页面缩小为小窗 | | max | 视频小窗还原为页面 | | | |
|  | notFound | boolean | 是否未找到页面 |
|  | page | Object | 当前打开页面的相关配置 |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| webview | Webview 渲染引擎 |
| skyline | Skyline 渲染引擎 |
| xr-frame | xr-frame 解决方案 |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| min | 视频页面缩小为小窗 |
| max | 视频小窗还原为页面 |

---

### wx.onAppRouteDone(function listener)

基础库 3.5.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onAppRouteDone.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| path | string | 页面路径 |
| query | Object | 路由参数 |
| openType | string | 路由打开类型 |
| webviewId | number | 当前页面 id |
| timeStamp | number | 路由下发的时间戳 |
| routeEventId | string | 路由事件 id |

---

### wx.onAppRoute(function listener)

基础库 3.5.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onAppRoute.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | path | string | 页面路径 |
|  | query | Object | 路由参数 |
|  | renderer | string | 渲染引擎 |
|  | | 合法值 | 说明 | | --- | --- | | webview | Webview 渲染引擎 | | skyline | Skyline 渲染引擎 | | xr-frame | xr-frame 解决方案 | | | |
|  | openType | string | 路由打开类型 |
|  | webviewId | number | 当前页面 id |
|  | timeStamp | number | 路由下发的时间戳 |
|  | routeEventId | string | 路由事件 id |
|  | pipMode | string |  |
|  | | 合法值 | 说明 | | --- | --- | | min | 视频页面缩小为小窗 | | max | 视频小窗还原为页面 | | | |
|  | notFound | boolean | 是否未找到页面 |
|  | page | Object | 当前打开页面的相关配置 |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| webview | Webview 渲染引擎 |
| skyline | Skyline 渲染引擎 |
| xr-frame | xr-frame 解决方案 |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| min | 视频页面缩小为小窗 |
| max | 视频小窗还原为页面 |

---

### wx.onAfterPageUnload(function listener)

基础库 3.5.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onAfterPageUnload.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| path | string | 页面路径 |
| routeEventId | string | 路由事件 id |

---

### wx.onAfterPageLoad(function listener)

基础库 3.5.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onAfterPageLoad.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | path | string | 页面路径 |
|  | query | Object | 路由参数 |
|  | componentFramework | string | 组件框架 |
|  | | 合法值 | 说明 | | --- | --- | | exparser | 旧版小程序组件框架 | | glass-easel | 新版小程序组件框架 | | | |
|  | openType | string | 路由打开类型 |
|  | routeEventId | string | 路由事件 id |
|  | page | Object | 页面实例 |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| exparser | 旧版小程序组件框架 |
| glass-easel | 新版小程序组件框架 |

---

### wx.offBeforePageUnload(function listener)

基础库 3.5.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.offBeforePageUnload.html

---

### wx.offBeforePageLoad(function listener)

基础库 3.5.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.offBeforePageLoad.html

---

### wx.offBeforeAppRoute(function listener)

基础库 3.5.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.offBeforeAppRoute.html

---

### wx.offAppRouteDone(function listener)

基础库 3.5.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.offAppRouteDone.html

---

### wx.offAppRoute(function listener)

基础库 3.5.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.offAppRoute.html

---

### wx.offAfterPageUnload(function listener)

基础库 3.5.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.offAfterPageUnload.html

---

### wx.offAfterPageLoad(function listener)

基础库 3.5.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.offAfterPageLoad.html

---

### wx.setEnableDebug(Object object)

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/wx.setEnableDebug.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| enableDebug | boolean |  | 是 | 是否打开调试 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### RealtimeLogManager wx.getRealtimeLogManager()

基础库 2.7.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/wx.getRealtimeLogManager.html

---

### LogManager wx.getLogManager(Object object)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/wx.getLogManager.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| level | number | 0 | 否 | 取值为0/1，取值为0表示会把 `App`、`Page` 的生命周期函数和 `wx` 命名空间下的函数调用写入日志，取值为1则不会。默认值是 0 | [2.3.2](../../../framework/compatibility.html) |

---

### console

向调试面板中打印日志。console 是一个全局对象，可以直接访问。在微信客户端中，向 vConsole 中输出日志。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/console.html

---

### console.debug()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/console.debug.html

---

### console.error()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/console.error.html

---

### console.group(string label)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/console.group.html

---

### console.groupEnd()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/console.groupEnd.html

---

### console.info()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/console.info.html

---

### console.log()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/console.log.html

---

### console.warn()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/console.warn.html

---

### LogManager

日志管理器实例，可以通过wx.getLogManager获取。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/LogManager.html

---

### LogManager.debug()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/LogManager.debug.html

---

### LogManager.info()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/LogManager.info.html

---

### LogManager.log()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/LogManager.log.html

---

### LogManager.warn()

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/LogManager.warn.html

---

### RealtimeLogManager

相关文档:实时日志

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeLogManager.html

---

### RealtimeLogManager.addFilterMsg(string msg)

基础库 2.8.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeLogManager.addFilterMsg.html

---

### RealtimeLogManager.error()

基础库 2.7.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeLogManager.error.html

---

### Object RealtimeLogManager.getCurrentState()

基础库 2.19.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeLogManager.getCurrentState.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| size | number | 当前缓存中已使用空间，以字节为单位 |
| maxSize | number | 当前缓存最大可用空间，以字节为单位 |
| logCount | number | 当前缓存中的日志条数 |
| maxLogCount | number | 当前缓存中最大可存日志条数 |

---

### RealtimeLogManager.in(Page pageInstance)

基础库 2.9.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeLogManager.in.html

---

### RealtimeLogManager.info()

基础库 2.7.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeLogManager.info.html

---

### RealtimeLogManager.setFilterMsg(string msg)

基础库 2.7.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeLogManager.setFilterMsg.html

---

### RealtimeTagLogManager RealtimeLogManager.tag(string tagName)

基础库 2.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeLogManager.tag.html

---

### RealtimeLogManager.warn()

基础库 2.7.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeLogManager.warn.html

---

### RealtimeTagLogManager

基础库 2.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeTagLogManager.html

---

### RealtimeTagLogManager.addFilterMsg(string msg)

基础库 2.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeTagLogManager.addFilterMsg.html

---

### RealtimeTagLogManager.error(string key, Object|Array.<any>|number|string value)

基础库 2.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeTagLogManager.error.html

---

### RealtimeTagLogManager.info(string key, Object|Array.<any>|number|string value)

基础库 2.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeTagLogManager.info.html

---

### RealtimeTagLogManager.setFilterMsg(string msg)

基础库 2.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeTagLogManager.setFilterMsg.html

---

### RealtimeTagLogManager.warn(string key, Object|Array.<any>|number|string value)

基础库 2.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeTagLogManager.warn.html

---

### wx.requestIdleCallback(function callback, Object object)

基础库 3.10.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/wx.requestIdleCallback.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number |  | 否 |  |

---

### wx.reportPerformance(Number id, Number value, String|Array dimensions)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/wx.reportPerformance.html

---

### wx.preloadWebview(Object object)

基础库 2.15.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/wx.preloadWebview.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.preloadSkylineView(Object object)

基础库 2.24.7 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/wx.preloadSkylineView.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.preloadAssets(Object object)

基础库 2.22.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/wx.preloadAssets.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | data | Array.<Object> |  | 是 |  |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | type | string |  | 是 |  | |  | | 合法值 | 说明 | | --- | --- | | 'font' | 字体 | | 'image' | 图片 | | | | | | |  | src | string |  | 是 |  | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | type | string |  | 是 |  |
|  | | 合法值 | 说明 | | --- | --- | | 'font' | 字体 | | 'image' | 图片 | | | | | |
|  | src | string |  | 是 |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 'font' | 字体 |
| 'image' | 图片 |

---

### Performance wx.getPerformance()

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/wx.getPerformance.html

**Performance**

| 指标类型（entryType） | 指标名称 | 最低版本 ｜ |
| --- | --- | --- |
| 路由（navigation） | route: 路由性能 |  |
| 路由（navigation） | appLaunch: 小程序启动耗时 |  |
| 渲染（render） | firstRender: 页面首次渲染耗时 |  |
| 渲染（render） | firstPaint: 页面首次绘制 | <2.21.2> |
| 渲染（render） | firstContentfulPaint: 页面首次内容绘制 | <2.21.2> |
| 渲染（render） | largestContentfulPaint: 页面最大内容绘制 | <2.23.1> |
| 脚本（script） | evaluateScript: 注入脚本耗时 |  |
| 包加载（loadPackage） | downloadPackage: 代码包下载耗时 | <2.24.0> |
| 资源（resource） | resourceTiming: 视图层资源加载耗时 | <2.24.0> |

---

### wx.cancelIdleCallback(number idleCallbackId)

基础库 3.10.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/wx.cancelIdleCallback.html

---

### EntryList

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/EntryList.html

---

### Array.<PerformanceEntry> EntryList.getEntries()

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/EntryList.getEntries.html

---

### Array.<PerformanceEntry> EntryList.getEntriesByName(string name, string entryType)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/EntryList.getEntriesByName.html

---

### Array.<PerformanceEntry> EntryList.getEntriesByType(string entryType)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/EntryList.getEntriesByType.html

---

### Performance

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/Performance.html

---

### PerformanceObserver Performance.createObserver(function callback)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/Performance.createObserver.html

---

### Array.<PerformanceEntry> Performance.getEntries()

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/Performance.getEntries.html

---

### Array.<PerformanceEntry> Performance.getEntriesByName(string name, string entryType)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/Performance.getEntriesByName.html

---

### Array.<PerformanceEntry> Performance.getEntriesByType(string entryType)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/Performance.getEntriesByType.html

---

### Performance.setBufferSize(number size)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/Performance.setBufferSize.html

---

### PerformanceEntry

相关文档:性能优化

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/PerformanceEntry.html

**string entryType**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| navigation | 路由 |  |
| render | 渲染 |  |
| script | 脚本 |  |

**string name**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| appLaunch | 小程序启动耗时。(entryType: navigation) |  |
| route | 路由处理耗时。(entryType: navigation) |  |
| firstRender | 页面首次渲染耗时。(entryType: render) |  |
| firstPaint | 页面首次绘制(FP)时间点，无 duration。（iOS 不支持）(entryType: render) | [2.21.2](../../../framework/compatibility.html) |
| firstContentfulPaint | 页面首次内容绘制(FCP)时间点，无 duration。（iOS 14.5 以下版本不支持）(entryType: render) | [2.21.2](../../../framework/compatibility.html) |
| largestContentfulPaint | 页面最大内容绘制(LCP)时间点，无 duration。（iOS 不支持）(entryType: render) | [2.23.1](../../../framework/compatibility.html) |
| evaluateScript | 逻辑层 JS 代码注入耗时。(entryType: script) |  |
| downloadPackage | 代码包下载耗时。(entryType: loadPackage) | [2.24.0](../../../framework/compatibility.html) |
| resourceTiming | 视图层资源加载耗时。(entryType: resource) | [2.24.0](../../../framework/compatibility.html) |

**string initiatorType**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| audio | 音频 |  |
| cover-image | cover-image 组件的图片 |  |
| image | 组件的图片 |  |
| open-data | 组件的图片 |  |

---

### PerformanceObserver

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/PerformanceObserver.html

---

### PerformanceObserver.disconnect()

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/PerformanceObserver.disconnect.html

---

### PerformanceObserver.observe(Object options)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/PerformanceObserver.observe.html

**Object options**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | type | string |  | 否 | 指标类型。不能和 entryTypes 同时使用 |
|  | | 合法值 | 说明 | | --- | --- | | navigation | 路由 | | render | 渲染 | | script | 脚本 | | loadPackage | 代码包下载 | | | | | |
|  | entryTypes | Array.<string> |  | 否 | 指标类型列表。不能和 type 同时使用。 |

**Object options**

| 合法值 | 说明 |
| --- | --- |
| navigation | 路由 |
| render | 渲染 |
| script | 脚本 |
| loadPackage | 代码包下载 |

---

### PreDownloadSubpackageTask wx.preDownloadSubpackage(Object object)

基础库 2.27.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/subpackage/wx.preDownloadSubpackage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| packageType | string |  | 是 | 分包的类型。目前仅支持填 "workers"，表示 workers 分包。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### PreDownloadSubpackageTask

基础库 2.27.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/subpackage/PreDownloadSubpackageTask.html

---

### PreDownloadSubpackageTask.onProgressUpdate(function listener)

基础库 2.27.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/subpackage/PreDownloadSubpackageTask.onProgressUpdate.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| progress | number | 分包下载进度百分比 |
| totalBytesWritten | number | 已经下载的数据长度，单位 Bytes |
| totalBytesExpectedToWrite | number | 预期需要下载的数据总长度，单位 Bytes |

---

### UserCryptoManager wx.getUserCryptoManager()

基础库 2.17.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/crypto/wx.getUserCryptoManager.html

---

### UserCryptoManager

基础库 2.17.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/crypto/UserCryptoManager.html

---

### UserCryptoManager.getLatestUserKey(Object object)

基础库 2.17.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/crypto/UserCryptoManager.getLatestUserKey.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| encryptKey | string | 用户加密密钥 |
| iv | string | 密钥初始向量 |
| version | number | 密钥版本 |
| expireTime | number | 密钥过期时间 |

---

### UserCryptoManager.getRandomValues(Object object)

基础库 2.17.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/base/crypto/UserCryptoManager.getRandomValues.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| length | number |  | 是 | 整数，生成随机数的字节数，最大 1048576 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| randomValues | ArrayBuffer | 随机数内容，长度为传入的字节数 |

---

<!-- pages: 123 -->
