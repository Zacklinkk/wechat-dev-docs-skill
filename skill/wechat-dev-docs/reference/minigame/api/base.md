# 微信小游戏 API 结构化参考 — base

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.env

相关文档:文件系统

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/wx.env.html

---

### wx.openSystemBluetoothSetting(Object object)

基础库 2.25.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/system/wx.openSystemBluetoothSetting.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.openAppAuthorizeSetting(Object object)

基础库 2.25.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/system/wx.openAppAuthorizeSetting.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### Object wx.getWindowInfo()

基础库 2.25.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/system/wx.getWindowInfo.html

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

基础库 2.25.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/system/wx.getSystemSetting.html

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

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/system/wx.getSystemInfoSync.html

**Object res**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | brand | string | 设备品牌 | [1.5.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | model | string | 设备型号。新机型刚推出一段时间会显示unknown，微信会尽快进行适配。 |  |
|  | pixelRatio | number | 设备像素比 |  |
|  | screenWidth | number | 屏幕宽度，单位px | [1.1.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | screenHeight | number | 屏幕高度，单位px | [1.1.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | windowWidth | number | 可使用窗口宽度，单位px |  |
|  | windowHeight | number | 可使用窗口高度，单位px |  |
|  | statusBarHeight | number | 状态栏的高度，单位px | [1.9.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | language | string | 微信设置的语言 |  |
|  | version | string | 微信版本号 |  |
|  | system | string | 操作系统及版本 |  |
|  | platform | string | 客户端平台 |  |
|  | | 合法值 | 说明 | | --- | --- | | ios | iOS微信（包含 iPhone、iPad） | | android | Android微信 | | ohos | HarmonyOS 手机端微信 | | ohos\_pc | HarmonyOS PC微信 | | windows | Windows微信 | | mac | macOS微信 | | devtools | 微信开发者工具 | | | | |
|  | fontSizeSetting | number | 用户字体大小（单位px）。以微信客户端「我-设置-通用-字体大小」中的设置为准 | [1.5.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | SDKVersion | string | 客户端基础库版本 | [1.1.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | benchmarkLevel | number | 设备性能等级（仅 Android）。取值为：-2 或 0（该设备无法运行小游戏），-1（性能未知），>=1（设备性能值，该值越高，设备性能越好）  注意：性能等级当前仅反馈真机机型，暂不支持 IDE 模拟器机型 | [1.8.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | albumAuthorized | boolean | 允许微信使用相册的开关（仅 iOS 有效） | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | cameraAuthorized | boolean | 允许微信使用摄像头的开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | locationAuthorized | boolean | 允许微信使用定位的开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | microphoneAuthorized | boolean | 允许微信使用麦克风的开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | notificationAuthorized | boolean | 允许微信通知的开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | notificationAlertAuthorized | boolean | 允许微信通知带有提醒的开关（仅 iOS 有效） | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | notificationBadgeAuthorized | boolean | 允许微信通知带有标记的开关（仅 iOS 有效） | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | notificationSoundAuthorized | boolean | 允许微信通知带有声音的开关（仅 iOS 有效） | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | phoneCalendarAuthorized | boolean | 允许微信使用日历的开关 | [2.19.3](../../../guide/runtime/client-lib/compatibility.html) |
|  | bluetoothEnabled | boolean | 蓝牙的系统开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | locationEnabled | boolean | 地理位置的系统开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | wifiEnabled | boolean | Wi-Fi 的系统开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | safeArea | Object | 在竖屏正方向下的安全区域。部分机型没有安全区域概念，也不会返回 safeArea 字段，开发者需自行兼容。 | [2.7.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | left | number | 安全区域左上角横坐标 | |  | right | number | 安全区域右下角横坐标 | |  | top | number | 安全区域左上角纵坐标 | |  | bottom | number | 安全区域右下角纵坐标 | |  | width | number | 安全区域的宽度，单位逻辑像素 | |  | height | number | 安全区域的高度，单位逻辑像素 | | | | |
|  | locationReducedAccuracy | boolean | `true` 表示模糊定位，`false` 表示精确定位，仅 iOS 支持 |  |
|  | theme | string | 系统当前主题，取值为`light`或`dark`，全局配置`"darkmode":true`时才能获取，否则为 undefined （不支持小游戏） | [2.11.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | dark | 深色主题 | | light | 浅色主题 | | | | |
|  | host | Object | 当前小程序运行的宿主环境 | [2.12.3](../../../guide/runtime/client-lib/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 宿主 app 对应的 appId | | | | |
|  | enableDebug | boolean | 是否已打开调试。可通过右上角菜单或 [wx.setEnableDebug](../debug/wx.setEnableDebug.html) 打开调试。 | [2.15.0](../../../guide/runtime/client-lib/compatibility.html) |
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

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/system/wx.getSystemInfoAsync.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | brand | string | 设备品牌 | [1.5.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | model | string | 设备型号。新机型刚推出一段时间会显示unknown，微信会尽快进行适配。 |  |
|  | pixelRatio | number | 设备像素比 |  |
|  | screenWidth | number | 屏幕宽度，单位px | [1.1.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | screenHeight | number | 屏幕高度，单位px | [1.1.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | windowWidth | number | 可使用窗口宽度，单位px |  |
|  | windowHeight | number | 可使用窗口高度，单位px |  |
|  | statusBarHeight | number | 状态栏的高度，单位px | [1.9.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | language | string | 微信设置的语言 |  |
|  | version | string | 微信版本号 |  |
|  | system | string | 操作系统及版本 |  |
|  | platform | string | 客户端平台 |  |
|  | | 合法值 | 说明 | | --- | --- | | ios | iOS微信（包含 iPhone、iPad） | | android | Android微信 | | ohos | HarmonyOS 手机端微信 | | ohos\_pc | HarmonyOS PC微信 | | windows | Windows微信 | | mac | macOS微信 | | devtools | 微信开发者工具 | | | | |
|  | fontSizeSetting | number | 用户字体大小（单位px）。以微信客户端「我-设置-通用-字体大小」中的设置为准 | [1.5.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | SDKVersion | string | 客户端基础库版本 | [1.1.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | benchmarkLevel | number | 设备性能等级（仅 Android）。取值为：-2 或 0（该设备无法运行小游戏），-1（性能未知），>=1（设备性能值，该值越高，设备性能越好）  注意：性能等级当前仅反馈真机机型，暂不支持 IDE 模拟器机型 | [1.8.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | albumAuthorized | boolean | 允许微信使用相册的开关（仅 iOS 有效） | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | cameraAuthorized | boolean | 允许微信使用摄像头的开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | locationAuthorized | boolean | 允许微信使用定位的开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | microphoneAuthorized | boolean | 允许微信使用麦克风的开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | notificationAuthorized | boolean | 允许微信通知的开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | notificationAlertAuthorized | boolean | 允许微信通知带有提醒的开关（仅 iOS 有效） | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | notificationBadgeAuthorized | boolean | 允许微信通知带有标记的开关（仅 iOS 有效） | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | notificationSoundAuthorized | boolean | 允许微信通知带有声音的开关（仅 iOS 有效） | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | phoneCalendarAuthorized | boolean | 允许微信使用日历的开关 | [2.19.3](../../../guide/runtime/client-lib/compatibility.html) |
|  | bluetoothEnabled | boolean | 蓝牙的系统开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | locationEnabled | boolean | 地理位置的系统开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | wifiEnabled | boolean | Wi-Fi 的系统开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | safeArea | Object | 在竖屏正方向下的安全区域。部分机型没有安全区域概念，也不会返回 safeArea 字段，开发者需自行兼容。 | [2.7.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | left | number | 安全区域左上角横坐标 | |  | right | number | 安全区域右下角横坐标 | |  | top | number | 安全区域左上角纵坐标 | |  | bottom | number | 安全区域右下角纵坐标 | |  | width | number | 安全区域的宽度，单位逻辑像素 | |  | height | number | 安全区域的高度，单位逻辑像素 | | | | |
|  | locationReducedAccuracy | boolean | `true` 表示模糊定位，`false` 表示精确定位，仅 iOS 支持 |  |
|  | theme | string | 系统当前主题，取值为`light`或`dark`，全局配置`"darkmode":true`时才能获取，否则为 undefined （不支持小游戏） | [2.11.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | dark | 深色主题 | | light | 浅色主题 | | | | |
|  | host | Object | 当前小程序运行的宿主环境 | [2.12.3](../../../guide/runtime/client-lib/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 宿主 app 对应的 appId | | | | |
|  | enableDebug | boolean | 是否已打开调试。可通过右上角菜单或 [wx.setEnableDebug](../debug/wx.setEnableDebug.html) 打开调试。 | [2.15.0](../../../guide/runtime/client-lib/compatibility.html) |
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

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/system/wx.getSystemInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | brand | string | 设备品牌 | [1.5.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | model | string | 设备型号。新机型刚推出一段时间会显示unknown，微信会尽快进行适配。 |  |
|  | pixelRatio | number | 设备像素比 |  |
|  | screenWidth | number | 屏幕宽度，单位px | [1.1.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | screenHeight | number | 屏幕高度，单位px | [1.1.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | windowWidth | number | 可使用窗口宽度，单位px |  |
|  | windowHeight | number | 可使用窗口高度，单位px |  |
|  | statusBarHeight | number | 状态栏的高度，单位px | [1.9.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | language | string | 微信设置的语言 |  |
|  | version | string | 微信版本号 |  |
|  | system | string | 操作系统及版本 |  |
|  | platform | string | 客户端平台 |  |
|  | | 合法值 | 说明 | | --- | --- | | ios | iOS微信（包含 iPhone、iPad） | | android | Android微信 | | ohos | HarmonyOS 手机端微信 | | ohos\_pc | HarmonyOS PC微信 | | windows | Windows微信 | | mac | macOS微信 | | devtools | 微信开发者工具 | | | | |
|  | fontSizeSetting | number | 用户字体大小（单位px）。以微信客户端「我-设置-通用-字体大小」中的设置为准 | [1.5.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | SDKVersion | string | 客户端基础库版本 | [1.1.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | benchmarkLevel | number | 设备性能等级（仅 Android）。取值为：-2 或 0（该设备无法运行小游戏），-1（性能未知），>=1（设备性能值，该值越高，设备性能越好）  注意：性能等级当前仅反馈真机机型，暂不支持 IDE 模拟器机型 | [1.8.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | albumAuthorized | boolean | 允许微信使用相册的开关（仅 iOS 有效） | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | cameraAuthorized | boolean | 允许微信使用摄像头的开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | locationAuthorized | boolean | 允许微信使用定位的开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | microphoneAuthorized | boolean | 允许微信使用麦克风的开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | notificationAuthorized | boolean | 允许微信通知的开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | notificationAlertAuthorized | boolean | 允许微信通知带有提醒的开关（仅 iOS 有效） | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | notificationBadgeAuthorized | boolean | 允许微信通知带有标记的开关（仅 iOS 有效） | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | notificationSoundAuthorized | boolean | 允许微信通知带有声音的开关（仅 iOS 有效） | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | phoneCalendarAuthorized | boolean | 允许微信使用日历的开关 | [2.19.3](../../../guide/runtime/client-lib/compatibility.html) |
|  | bluetoothEnabled | boolean | 蓝牙的系统开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | locationEnabled | boolean | 地理位置的系统开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | wifiEnabled | boolean | Wi-Fi 的系统开关 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | safeArea | Object | 在竖屏正方向下的安全区域。部分机型没有安全区域概念，也不会返回 safeArea 字段，开发者需自行兼容。 | [2.7.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | left | number | 安全区域左上角横坐标 | |  | right | number | 安全区域右下角横坐标 | |  | top | number | 安全区域左上角纵坐标 | |  | bottom | number | 安全区域右下角纵坐标 | |  | width | number | 安全区域的宽度，单位逻辑像素 | |  | height | number | 安全区域的高度，单位逻辑像素 | | | | |
|  | locationReducedAccuracy | boolean | `true` 表示模糊定位，`false` 表示精确定位，仅 iOS 支持 |  |
|  | theme | string | 系统当前主题，取值为`light`或`dark`，全局配置`"darkmode":true`时才能获取，否则为 undefined （不支持小游戏） | [2.11.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | dark | 深色主题 | | light | 浅色主题 | | | | |
|  | host | Object | 当前小程序运行的宿主环境 | [2.12.3](../../../guide/runtime/client-lib/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 宿主 app 对应的 appId | | | | |
|  | enableDebug | boolean | 是否已打开调试。可通过右上角菜单或 [wx.setEnableDebug](../debug/wx.setEnableDebug.html) 打开调试。 | [2.15.0](../../../guide/runtime/client-lib/compatibility.html) |
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

### Object wx.getDeviceInfo()

基础库 2.25.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/system/wx.getDeviceInfo.html

**Object**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | abi | string | 应用（微信APP）二进制接口类型（仅 Android 支持） |  |
|  | deviceAbi | string | 设备二进制接口类型（仅 Android 支持） | [2.25.1](../../../guide/runtime/client-lib/compatibility.html) |
|  | benchmarkLevel | number | 设备性能等级（仅 Android 支持）。取值为：-2 或 0（该设备无法运行小游戏），-1（性能未知），>=1（设备性能值，该值越高，设备性能越好，目前最高不到50）  注意：从基础库3.4.5开始，本返回值停止维护，请使用[wx.getDeviceBenchmarkInfo](wx.getDeviceBenchmarkInfo.html)获取设备性能等级 |  |
|  | brand | string | 设备品牌 |  |
|  | model | string | 设备型号。新机型刚推出一段时间会显示unknown，微信会尽快进行适配。 |  |
|  | system | string | 操作系统及版本 |  |
|  | platform | string | 客户端平台 |  |
|  | | 合法值 | 说明 | | --- | --- | | ios | iOS微信（包含 iPhone、iPad） | | android | Android微信 | | ohos | HarmonyOS 手机端微信 | | ohos\_pc | HarmonyOS PC微信 | | windows | Windows微信 | | mac | macOS微信 | | devtools | 微信开发者工具 | | | | |
|  | cpuType | string | 设备 CPU 型号（仅 Android 支持）（Tips: GPU 型号可通过 WebGLRenderingContext.getExtension('WEBGL\_debug\_renderer\_info') 来获取） | [2.29.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | memorySize | string | 设备内存大小，单位为 MB | [2.30.0](../../../guide/runtime/client-lib/compatibility.html) |

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

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/system/wx.getDeviceBenchmarkInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| benchmarkLevel | number | 设备性能等级。-1（性能未知），>=1（设备性能值，该值越高，设备性能越好） 注意： 1. 设备的benchmarkLevel值不会随着时间的推移而变化，移动端设备目前最高不超过50 | [3.4.5](../../../guide/runtime/client-lib/compatibility.html) |
| modelLevel | number | 设备机型档位。0（档位未知），1（高档机），2（中档机），3（低档机）  注意：设备的机型档位会随着时间的推移而变化，因此在使用时请谨慎对待；若业务逻辑依赖于机型档位，但担心受到机型档位变化的影响，请参考[设备档位映射文档](https://developers.weixin.qq.com/minigame/dev/guide/performance/perf-benchmarkLevel.html)自行判断机型档位 | [3.4.5](../../../guide/runtime/client-lib/compatibility.html) |

---

### Object wx.getAppBaseInfo()

基础库 2.25.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/system/wx.getAppBaseInfo.html

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
|  | fontSizeSetting | number | 微信字体大小，单位px | [2.23.4](../../../guide/runtime/client-lib/compatibility.html) |

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

基础库 2.25.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/system/wx.getAppAuthorizeSetting.html

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

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/update/wx.updateWeChatApp.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### UpdateManager wx.getUpdateManager()

基础库 1.9.90 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/update/wx.getUpdateManager.html

---

### UpdateManager

UpdateManager 对象，用来管理更新，可通过wx.getUpdateManager接口获取实例。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/update/UpdateManager.html

---

### UpdateManager.applyUpdate()

强制小程序重启并使用新版本。在小程序新版本下载完成后（即收到onUpdateReady回调）调用。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/update/UpdateManager.applyUpdate.html

---

### UpdateManager.onCheckForUpdate(function listener)

监听向微信后台请求检查更新结果事件。微信在小程序每次启动（包括热启动）时自动检查更新，不需由开发者主动触发。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/update/UpdateManager.onCheckForUpdate.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| hasUpdate | boolean | 是否有新版本 |

---

### UpdateManager.onUpdateFailed(function listener)

监听小程序更新失败事件。小程序有新版本，客户端主动触发下载（无需开发者触发），下载失败（可能是网络原因等）后回调

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/update/UpdateManager.onUpdateFailed.html

---

### UpdateManager.onUpdateReady(function listener)

监听小程序有版本更新事件。客户端主动触发下载（无需开发者触发），下载成功后回调

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/update/UpdateManager.onUpdateReady.html

---

### wx.onShow(function listener)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/app/life-cycle/wx.onShow.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | scene | number | 场景值 |
|  | query | Record.<string, string> | 查询参数 |
|  | shareTicket | string | shareTicket |
|  | referrerInfo | object | 当场景为由从另一个小程序或公众号或App打开时，返回此字段 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 来源小程序或公众号或App的 appId | |  | extraData | object | 来源小程序传过来的数据，scene=1037或1038时支持 | | | |
|  | chatType | number | 从微信群聊/单聊打开小程序时，chatType 表示具体微信群聊/单聊类型 |
|  | | 合法值 | 说明 | | --- | --- | | 1 | 微信联系人单聊 | | 2 | 企业微信联系人单聊 | | 3 | 普通微信群聊 | | 4 | 企业微信互通群聊 | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | appId | string | 来源小程序或公众号或App的 appId |
|  | extraData | object | 来源小程序传过来的数据，scene=1037或1038时支持 |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| 1 | 微信联系人单聊 |
| 2 | 企业微信联系人单聊 |
| 3 | 普通微信群聊 |
| 4 | 企业微信互通群聊 |

---

### wx.onHide(function listener)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/app/life-cycle/wx.onHide.html

---

### wx.offShow(function listener)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/app/life-cycle/wx.offShow.html

---

### wx.offHide(function listener)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/app/life-cycle/wx.offHide.html

---

### Object wx.getLaunchOptionsSync()

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/app/life-cycle/wx.getLaunchOptionsSync.html

**Object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | scene | number | 启动小游戏的[场景值](https://developers.weixin.qq.com/minigame/dev/guide/base-ability/scene.html) |
|  | query | Record.<string, string> | 启动小游戏的 query 参数 |
|  | shareTicket | string | shareTicket，详见[获取更多转发信息](../../../../guide/open-ability/share/share.html#获取更多转发信息) |
|  | referrerInfo | object | 来源信息。从另一个小程序、公众号或 App 进入小程序时返回。否则返回 `{}`。(参见后文注意) |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 来源小程序、公众号或 App 的 appId | |  | extraData | object | 来源小程序传过来的数据，scene=1037或1038时支持 | | | |
|  | hostExtraData | string | 宿主传递的数据，第三方 app 中运行小游戏时返回，类型为json字符串，其中需要 host\_scene 字段，表示宿主app对应的场景值 |
|  | chatType | number | 从微信群聊/单聊打开小程序时，chatType 表示具体微信群聊/单聊类型 |
|  | | 合法值 | 说明 | | --- | --- | | 1 | 微信联系人单聊 | | 2 | 企业微信联系人单聊 | | 3 | 普通微信群聊 | | 4 | 企业微信互通群聊 | | | |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | appId | string | 来源小程序、公众号或 App 的 appId |
|  | extraData | object | 来源小程序传过来的数据，scene=1037或1038时支持 |

**Object**

| 合法值 | 说明 |
| --- | --- |
| 1 | 微信联系人单聊 |
| 2 | 企业微信联系人单聊 |
| 3 | 普通微信群聊 |
| 4 | 企业微信互通群聊 |

**返回有效 referrerInfo 的场景**

| 场景值 | 场景 | appId含义 |
| --- | --- | --- |
| 1020 | 公众号 profile 页相关小程序列表 | 来源公众号 |
| 1035 | 公众号自定义菜单 | 来源公众号 |
| 1036 | App 分享消息卡片 | 来源App |
| 1037 | 小程序打开小程序 | 来源小程序 |
| 1038 | 从另一个小程序返回 | 来源小程序 |
| 1043 | 公众号模板消息 | 来源公众号 |

---

### Object wx.getEnterOptionsSync()

基础库 2.13.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/app/life-cycle/wx.getEnterOptionsSync.html

**Object**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | scene | number | 启动小游戏的[场景值](https://developers.weixin.qq.com/minigame/dev/guide/base-ability/scene.html) |  |
|  | query | Record.<string, string> | 启动小游戏的 query 参数 |  |
|  | shareTicket | string | shareTicket，详见[获取更多转发信息](../../../../guide/open-ability/share/share.html#获取更多转发信息) |  |
|  | referrerInfo | object | 来源信息。从另一个小程序、公众号或 App 进入小程序时返回。否则返回 `{}`。(参见后文注意) |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 来源小程序、公众号或 App 的 appId | |  | extraData | object | 来源小程序传过来的数据，scene=1037或1038时支持 | | | | |
|  | chatType | number | 从微信群聊/单聊打开小程序时，chatType 表示具体微信群聊/单聊类型 |  |
|  | | 合法值 | 说明 | | --- | --- | | 1 | 微信联系人单聊 | | 2 | 企业微信联系人单聊 | | 3 | 普通微信群聊 | | 4 | 企业微信互通群聊 | | | | |
|  | apiCategory | string | API 类别 | [2.20.0](../../../../guide/runtime/client-lib/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | default | 默认类别 | | nativeFunctionalized | 原生功能化，视频号直播商品、商品橱窗等场景打开的小程序 | | browseOnly | 仅浏览，朋友圈快照页等场景打开的小程序 | | embedded | 内嵌，通过打开半屏小程序能力打开的小程序 | | | | |

**Object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | appId | string | 来源小程序、公众号或 App 的 appId |
|  | extraData | object | 来源小程序传过来的数据，scene=1037或1038时支持 |

**Object**

| 合法值 | 说明 |
| --- | --- |
| 1 | 微信联系人单聊 |
| 2 | 企业微信联系人单聊 |
| 3 | 普通微信群聊 |
| 4 | 企业微信互通群聊 |

**Object**

| 合法值 | 说明 |
| --- | --- |
| default | 默认类别 |
| nativeFunctionalized | 原生功能化，视频号直播商品、商品橱窗等场景打开的小程序 |
| browseOnly | 仅浏览，朋友圈快照页等场景打开的小程序 |
| embedded | 内嵌，通过打开半屏小程序能力打开的小程序 |

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

|  | default | nativeFunctionalized | browseOnly | embedded |
| --- | --- | --- | --- | --- |
| navigateToMiniProgram |  | `X` | `X` |  |
| openSetting |  |  | `X` |  |
| <button open-type="share"> |  | `X` | `X` | `X` |
| <button open-type="feedback"> |  |  | `X` |  |
| <button open-type="open-setting"> |  |  | `X` |  |
| openEmbeddedMiniProgram |  | `X` | `X` | `X` |

---

### wx.onUnhandledRejection(function listener)

基础库 2.10.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/app/app-event/wx.onUnhandledRejection.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| reason | string | 拒绝原因，一般是一个 Error 对象 |
| promise | string | 被拒绝的 promise 对象 |

---

### wx.onError(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/app/app-event/wx.onError.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| message | string | 错误信息，包含堆栈 |

---

### wx.onAudioInterruptionEnd(function listener)

基础库 1.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/app/app-event/wx.onAudioInterruptionEnd.html

---

### wx.onAudioInterruptionBegin(function listener)

基础库 1.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/app/app-event/wx.onAudioInterruptionBegin.html

---

### wx.offUnhandledRejection(function listener)

基础库 2.10.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/app/app-event/wx.offUnhandledRejection.html

---

### wx.offError(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/app/app-event/wx.offError.html

---

### wx.offAudioInterruptionEnd(function listener)

基础库 1.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/app/app-event/wx.offAudioInterruptionEnd.html

---

### wx.offAudioInterruptionBegin(function listener)

基础库 1.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/app/app-event/wx.offAudioInterruptionBegin.html

---

### wx.triggerGC()

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/performance/wx.triggerGC.html

---

### wx.reportPerformance(Number id, Number value, string|Array.<string> dimensions)

基础库 2.10.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/performance/wx.reportPerformance.html

---

### Performance wx.getPerformance()

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/performance/wx.getPerformance.html

---

### Performance

性能管理器

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/performance/Performance.html

---

### number Performance.now()

可以获取当前时间以微秒为单位的时间戳

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/performance/Performance.now.html

---

### PreDownloadSubpackageTask wx.preDownloadSubpackage(Object object)

基础库 2.27.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/subpackage/wx.preDownloadSubpackage.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | packageType | string | 'normal' | 否 | 分包的类型 |
|  | | 合法值 | 说明 | | --- | --- | | workers | worker 分包 | | normal | 普通分包, [3.4.9](../../../guide/runtime/client-lib/compatibility.html)及以上版本支持。下载普通分包，必须再传入 name 参数。 | | | | | |
|  | name | string |  | 是 | 分包的名字，可以填分包配置中的 name 或者 root 字段的值。仅在 packageType="normal" 时生效。在独立分包内，填 \_\_GAME\_\_ 表示加载主包，详见 [小游戏独立分包指南](../../../guide/base-ability/independent-sub-packages.html), [3.4.9](../../../guide/runtime/client-lib/compatibility.html)及以上版本支持 |
|  | success | function |  | 是 | 分包加载成功回调事件 |
|  | fail | function |  | 是 | 分包加载失败回调事件 |
|  | complete | function |  | 是 | 分包加载结束回调事件(加载成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| workers | worker 分包 |
| normal | 普通分包, [3.4.9](../../../guide/runtime/client-lib/compatibility.html)及以上版本支持。下载普通分包，必须再传入 name 参数。 |

---

### LoadSubpackageTask wx.loadSubpackage(Object object)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/subpackage/wx.loadSubpackage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| name | string |  | 是 | 分包的名字，可以填 name 或者 root。在独立分包内，填 \_\_GAME\_\_ 表示加载主包，详见 [小游戏独立分包指南](../../../guide/base-ability/independent-sub-packages.html) |
| success | function |  | 是 | 分包加载成功回调事件 |
| fail | function |  | 是 | 分包加载失败回调事件 |
| complete | function |  | 是 | 分包加载结束回调事件(加载成功、失败都会执行） |

---

### LoadSubpackageTask

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/subpackage/LoadSubpackageTask.html

---

### LoadSubpackageTask.onProgressUpdate(function listener)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/subpackage/LoadSubpackageTask.onProgressUpdate.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| progress | number | 分包下载进度百分比 |
| totalBytesWritten | number | 已经下载的数据长度，单位 Bytes |
| totalBytesExpectedToWrite | number | 预期需要下载的数据总长度，单位 Bytes |

---

### PreDownloadSubpackageTask

基础库 2.27.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/subpackage/PreDownloadSubpackageTask.html

---

### PreDownloadSubpackageTask.onProgressUpdate(function listener)

基础库 2.27.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/subpackage/PreDownloadSubpackageTask.onProgressUpdate.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| progress | number | 分包下载进度百分比 |
| totalBytesWritten | number | 已经下载的数据长度，单位 Bytes |
| totalBytesExpectedToWrite | number | 预期需要下载的数据总长度，单位 Bytes |

---

### wx.setEnableDebug(Object object)

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/wx.setEnableDebug.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| enableDebug | boolean |  | 是 | 是否打开调试 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### RealtimeLogManager wx.getRealtimeLogManager()

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/wx.getRealtimeLogManager.html

---

### LogManager wx.getLogManager(Object object)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/wx.getLogManager.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| level | number | 0 | 否 | 取值为0/1，取值为0表示会把 `App`、`Page` 的生命周期函数和 `wx` 命名空间下的函数调用写入日志，取值为1则不会。默认值是 0 | [2.3.2](../../../guide/runtime/client-lib/compatibility.html) |

---

### console

向调试面板中打印日志。console 是一个全局对象，可以直接访问。在微信客户端中，向 vConsole 中输出日志。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/console.html

---

### console.debug()

向调试面板中打印 debug 日志

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/console.debug.html

---

### console.error()

向调试面板中打印 error 日志

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/console.error.html

---

### console.group(string label)

在调试面板中创建一个新的分组。随后输出的内容都会被添加一个缩进，表示该内容属于当前分组。调用console.groupEnd之后分组结束。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/console.group.html

---

### console.groupEnd()

结束由console.group创建的分组

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/console.groupEnd.html

---

### console.info()

向调试面板中打印 info 日志

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/console.info.html

---

### console.log()

向调试面板中打印 log 日志

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/console.log.html

---

### console.warn()

向调试面板中打印 warn 日志

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/console.warn.html

---

### LogManager

日志管理器实例，可以通过wx.getLogManager获取。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/LogManager.html

---

### LogManager.debug()

写 debug 日志

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/LogManager.debug.html

---

### LogManager.info()

写 info 日志

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/LogManager.info.html

---

### LogManager.log()

写 log 日志

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/LogManager.log.html

---

### LogManager.warn()

写 warn 日志

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/LogManager.warn.html

---

### RealtimeLogManager

相关文档:实时日志

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/RealtimeLogManager.html

---

### RealtimeLogManager.addFilterMsg(string msg)

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/RealtimeLogManager.addFilterMsg.html

---

### RealtimeLogManager.error()

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/RealtimeLogManager.error.html

---

### RealtimeLogManager.info()

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/RealtimeLogManager.info.html

---

### RealtimeLogManager.setFilterMsg(string msg)

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/RealtimeLogManager.setFilterMsg.html

---

### RealtimeLogManager.warn()

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/debug/RealtimeLogManager.warn.html

---

### UserCryptoManager wx.getUserCryptoManager()

基础库 2.17.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/crypto/wx.getUserCryptoManager.html

---

### UserCryptoManager

基础库 2.17.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/crypto/UserCryptoManager.html

---

### UserCryptoManager.getLatestUserKey(Object object)

基础库 2.17.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/crypto/UserCryptoManager.getLatestUserKey.html

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

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/base/crypto/UserCryptoManager.getRandomValues.html

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

<!-- pages: 70 -->
