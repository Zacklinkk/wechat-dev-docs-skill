# 微信小程序 API 结构化参考 — device

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.stopBluetoothDevicesDiscovery(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.stopBluetoothDevicesDiscovery.html

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

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.startBluetoothDevicesDiscovery.html

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

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.openBluetoothAdapter.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | mode | string | central | 否 | 蓝牙模式，可作为主/从设备，仅 iOS 需要。 | [2.10.0](../../../framework/compatibility.html) |
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

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.onBluetoothDeviceFound.html

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

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.onBluetoothAdapterStateChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| available | boolean | 蓝牙适配器是否可用 |
| discovering | boolean | 蓝牙适配器是否处于搜索状态 |

---

### wx.offBluetoothDeviceFound()

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.offBluetoothDeviceFound.html

---

### wx.offBluetoothAdapterStateChange()

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.offBluetoothAdapterStateChange.html

---

### wx.makeBluetoothPair(Object object)

基础库 2.12.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.makeBluetoothPair.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.isBluetoothDevicePaired.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string |  | 是 | 蓝牙设备 id |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.getConnectedBluetoothDevices(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.getConnectedBluetoothDevices.html

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

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.getBluetoothDevices.html

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

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.getBluetoothAdapterState.html

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

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.closeBluetoothAdapter.html

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

### wx.writeBLECharacteristicValue(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.writeBLECharacteristicValue.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.setBLEMTU.html

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

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.readBLECharacteristicValue.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.onBLEMTUChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| deviceId | string | 蓝牙设备 id |
| mtu | number | 最大传输单元 |

---

### wx.onBLEConnectionStateChange(function listener)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.onBLEConnectionStateChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| deviceId | string | 蓝牙设备 id |
| connected | boolean | 是否处于已连接状态 |

---

### wx.onBLECharacteristicValueChange(function listener)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.onBLECharacteristicValueChange.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.offBLEMTUChange.html

---

### wx.offBLEConnectionStateChange(function listener)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.offBLEConnectionStateChange.html

---

### wx.offBLECharacteristicValueChange()

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.offBLECharacteristicValueChange.html

---

### wx.notifyBLECharacteristicValueChange(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.notifyBLECharacteristicValueChange.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| deviceId | string |  | 是 | 蓝牙设备 id |  |
| serviceId | string |  | 是 | 蓝牙特征对应服务的 UUID |  |
| characteristicId | string |  | 是 | 蓝牙特征的 UUID |  |
| state | boolean |  | 是 | 是否启用 notify |  |
| type | string | indication | 否 | 设置特征订阅类型，有效值有 `notification` 和 `indication` | [2.4.0](../../../framework/compatibility.html) |
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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.getBLEMTU.html

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

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.getBLEDeviceServices.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.getBLEDeviceRSSI.html

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

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.getBLEDeviceCharacteristics.html

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

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.createBLEConnection.html

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

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.closeBLEConnection.html

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

### wx.onBLEPeripheralConnectionStateChanged(function listener)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/wx.onBLEPeripheralConnectionStateChanged.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| deviceId | String | 连接状态变化的设备 id |
| serverId | String | server 的 UUID |
| connected | Boolean | 连接目前状态 |

---

### wx.offBLEPeripheralConnectionStateChanged(function listener)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/wx.offBLEPeripheralConnectionStateChanged.html

---

### wx.createBLEPeripheralServer(Object object)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/wx.createBLEPeripheralServer.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.html

---

### BLEPeripheralServer.addService(Object object)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.addService.html

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

### BLEPeripheralServer.close(Object object)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.close.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### BLEPeripheralServer.offCharacteristicReadRequest(function listener)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.offCharacteristicReadRequest.html

---

### BLEPeripheralServer.offCharacteristicSubscribed(function listener)

基础库 2.13.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.offCharacteristicSubscribed.html

---

### BLEPeripheralServer.offCharacteristicUnsubscribed(function listener)

基础库 2.13.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.offCharacteristicUnsubscribed.html

---

### BLEPeripheralServer.offCharacteristicWriteRequest(function listener)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.offCharacteristicWriteRequest.html

---

### BLEPeripheralServer.onCharacteristicReadRequest(function listener)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.onCharacteristicReadRequest.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| serviceId | String | 蓝牙特征对应服务的 UUID |
| characteristicId | String | 蓝牙特征的 UUID |
| callbackId | Number | 唯一标识码，调用 [writeCharacteristicValue](BLEPeripheralServer.writeCharacteristicValue.html) 时使用 |

---

### BLEPeripheralServer.onCharacteristicSubscribed(function listener)

基础库 2.13.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.onCharacteristicSubscribed.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| serviceId | String | 蓝牙特征对应服务的 UUID |
| characteristicId | String | 蓝牙特征的 UUID |

---

### BLEPeripheralServer.onCharacteristicUnsubscribed(function listener)

基础库 2.13.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.onCharacteristicUnsubscribed.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| serviceId | String | 蓝牙特征对应服务的 UUID |
| characteristicId | String | 蓝牙特征的 UUID |

---

### BLEPeripheralServer.onCharacteristicWriteRequest(function listener)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.onCharacteristicWriteRequest.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.removeService.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.startAdvertising.html

**Object Object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | advertiseRequest | Object |  | 是 | 广播自定义参数 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | connectable | Boolean | true | 否 | 当前设备是否可连接 |  | |  | deviceName | String |  | 否 | 广播中 deviceName 字段，默认为空 |  | |  | serviceUuids | Array.<String> |  | 否 | 要广播的服务 UUID 列表。使用 16/32 位 UUID 时请参考注意事项。 |  | |  | manufacturerData | Array.<Object> |  | 否 | 广播的制造商信息。仅安卓支持，iOS 因系统限制无法定制。 |  | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | manufacturerId | String |  | 是 | 制造商ID，0x 开头的十六进制 | |  | manufacturerSpecificData | ArrayBuffer |  | 否 | 制造商信息 | | | | | | | |  | beacon | Object |  | 否 | 以 beacon 设备形式广播的参数。 | [2.20.1](../../../framework/compatibility.html) | |  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | uuid | String |  | 是 | Beacon 设备广播的 UUID | |  | major | Number |  | 是 | Beacon 设备的主 ID | |  | minor | Number |  | 是 | Beacon 设备的次 ID | |  | measuredPower | Number |  | 否 | 用于判断距离设备 1 米时 RSSI 大小的参考值 | | | | | | | | | | | |
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
|  | beacon | Object |  | 否 | 以 beacon 设备形式广播的参数。 | [2.20.1](../../../framework/compatibility.html) |
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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.stopAdvertising.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### BLEPeripheralServer.writeCharacteristicValue(Object Object)

基础库 2.10.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.writeCharacteristicValue.html

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

### wx.stopBeaconDiscovery(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/ibeacon/wx.stopBeaconDiscovery.html

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

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/ibeacon/wx.startBeaconDiscovery.html

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

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/ibeacon/wx.onBeaconUpdate.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| beacons | Array.<[BeaconInfo](BeaconInfo.html)> | 当前搜寻到的所有 Beacon 设备列表 |

---

### wx.onBeaconServiceChange(function listener)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/ibeacon/wx.onBeaconServiceChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| available | boolean | 服务目前是否可用 |
| discovering | boolean | 目前是否处于搜索状态 |

---

### wx.offBeaconUpdate()

基础库 2.8.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/ibeacon/wx.offBeaconUpdate.html

---

### wx.offBeaconServiceChange()

基础库 2.8.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/ibeacon/wx.offBeaconServiceChange.html

---

### wx.getBeacons(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/ibeacon/wx.getBeacons.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/ibeacon/BeaconInfo.html

**number proximity**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 0 | 信号太弱不足以计算距离，或非 iOS 设备 |  |
| 1 | 十分近 |  |
| 2 | 比较近 |  |
| 3 | 远 |  |

---

### wx.removeSecureElementPass(Object args)

基础库 3.8.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.removeSecureElementPass.html

**Object args**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| panid | String |  | 是 | 唯一id |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object args**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| result | String | 返回值 |
| errorMsg | String | 错误信息 |

---

### wx.rechargeTransitCard(Object args)

基础库 3.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.rechargeTransitCard.html

**Object args**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| issuerID | String |  | 是 | 交通卡卡种标识 |
| orderNo | String |  | 是 | 充值订单号 |
| operation | String |  | 是 | 操作类型："1"=普通充值，"2"=迁入充值 |
| sign | String |  | 是 | 请求签名 |
| timestamp | String |  | 否 | 签名时间戳（毫秒） |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object args**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | String | 错误信息 |
| errno | Number | 错误码，0 表示成功 |
| errorCode | Number | 失败时返回微信统一错误码 |

---

### wx.issueTransitCard(Object args)

基础库 3.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.issueTransitCard.html

**Object args**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| issuerID | String |  | 是 | 交通卡卡种标识 |
| orderNo | String |  | 是 | 开卡订单号 |
| operation | String |  | 是 | 操作类型："1"=普通开卡，"2"=卡片迁入 |
| sign | String |  | 是 | 请求签名 |
| timestamp | String |  | 否 | 签名时间戳（毫秒） |
| entrustId | String |  | 否 | 签约订单号，仅先乘后付业务需要 |
| paymentMode | String |  | 否 | 支付方式："1"=微信支付，"2"=支付宝支付，"3"=银联支付 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object args**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | String | 错误信息 |
| errno | Number | 错误码，0 表示成功 |
| cardNo | String | 开卡成功后的交通卡卡号 |
| errorCode | Number | 失败时返回微信统一错误码 |

---

### wx.getTransitCardList(Object args)

基础库 3.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.getTransitCardList.html

**Object args**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| issuerID | String |  | 否 | 交通卡卡种标识 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object args**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| result | boolean | 返回值 |
| errorMsg | String | 错误信息 |
| cards | Array.<String> | TransitCardInfo 的 JSON 字符串数组，需 JSON.parse 后使用 |

---

### wx.getTransitCardInfo(Object args)

基础库 3.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.getTransitCardInfo.html

**Object args**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| issuerID | String |  | 是 | 交通卡卡种标识 |
| fields | Array.<String> |  | 是 | 需要查询的字段列表，可选值："cardNo"、"balance"、"transactionRecords" |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object args**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| result | boolean | 返回值 |
| errorMsg | String | 错误信息 |
| cardInfo | String | TransitCardDetail 的 JSON 字符串，需 JSON.parse 后使用 |

---

### wx.getTransitCardCPLC(Object object)

基础库 3.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.getTransitCardCPLC.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| result | boolean | 返回值 |
| errorMsg | String | 错误信息 |
| cplc | String | 设备安全芯片的 CPLC 数据 |
| seid | String | 设备安全芯片的 SEID |
| walletVersionCode | String | 钱包版本号 |

---

### wx.getSecureElementPasses(Object args)

基础库 3.8.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.getSecureElementPasses.html

**Object args**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object args**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | result | String | 返回值 |
|  | errorMsg | String | 错误信息 |
|  | passes | Array.<Object> | SimplePKPass 的 JSON字符串，这里给出定义，需要进行 JSON.parse 后才可使用 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | primaryAccountIdentifier | string | 支付卡的主账户唯一标识符（由 Apple Pay 生成，用于设备端管理） | |  | primaryAccountNumberSuffix | string | 主实体卡号的后缀（如卡号末4位） | |  | deviceAccountIdentifier | string | 设备端生成的虚拟卡唯一标识符（用于本地关联安全元件中的卡片） | |  | deviceAccountNumberSuffix | string | 设备虚拟卡号的后缀（如虚拟卡号末4位） | |  | passActivationState | number | 卡片激活状态，具体值参考 PKSecureElementPassActivationState | |  | devicePassIdentifier | string | 设备端卡片的唯一 Pass ID（用于与 Wallet 应用交互） | |  | pairedTerminalIdentifier | string | 配对的终端设备标识符（如交通闸机设备 ID） | |  | isRemotePass | boolean | 是否为远程同步的卡片（如通过 iCloud 同步到设备的卡片） | | | |

**Object args**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | primaryAccountIdentifier | string | 支付卡的主账户唯一标识符（由 Apple Pay 生成，用于设备端管理） |
|  | primaryAccountNumberSuffix | string | 主实体卡号的后缀（如卡号末4位） |
|  | deviceAccountIdentifier | string | 设备端生成的虚拟卡唯一标识符（用于本地关联安全元件中的卡片） |
|  | deviceAccountNumberSuffix | string | 设备虚拟卡号的后缀（如虚拟卡号末4位） |
|  | passActivationState | number | 卡片激活状态，具体值参考 PKSecureElementPassActivationState |
|  | devicePassIdentifier | string | 设备端卡片的唯一 Pass ID（用于与 Wallet 应用交互） |
|  | pairedTerminalIdentifier | string | 配对的终端设备标识符（如交通闸机设备 ID） |
|  | isRemotePass | boolean | 是否为远程同步的卡片（如通过 iCloud 同步到设备的卡片） |

---

### NFCAdapter wx.getNFCAdapter()

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.getNFCAdapter.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### wx.deleteTransitCard(Object args)

基础库 3.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.deleteTransitCard.html

**Object args**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| issuerID | String |  | 是 | 交通卡卡种标识 |
| orderNo | String |  | 否 | 删卡订单号 |
| sign | String |  | 是 | 请求签名 |
| timestamp | String |  | 是 | 签名时间戳（毫秒） |
| refundAccountNumber | String |  | 否 | 退款账号（部分卡公司服务端接口需要） |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object args**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | String | 错误信息 |
| errno | Number | 错误码，0 表示成功 |
| errorCode | Number | 失败时返回微信统一错误码 |

---

### wx.checkTransitCardSupport(Object args)

基础库 3.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.checkTransitCardSupport.html

**Object args**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| issuerID | String |  | 是 | 交通卡卡种标识 |
| actionType | String |  | 否 | 要检查的操作类型，可选值："issue"（开卡）、"recharge"（充值）、"delete"（删卡），默认 "issue" |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object args**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| result | boolean | 返回值 |
| errorMsg | String | 错误信息 |
| supportNFC | boolean | 设备是否支持 NFC |
| supportSE | boolean | 设备是否支持安全芯片（eSE） |
| walletReady | boolean | 厂商钱包 APP 是否就绪（已安装且版本满足要求） |
| hasConflictCard | boolean | 是否存在冲突卡片（同一 issuerID 对应的卡已存在或存在互斥卡种） |

---

### wx.canAddSecureElementPass(Object args)

基础库 3.8.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.canAddSecureElementPass.html

**Object args**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| panid | String |  | 是 | 支付的panid（PrimaryAccountIdentifier） |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object args**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| result | String | 返回值 |
| errorMsg | String | 错误信息 |

---

### wx.addPaymentPassGetCertificateData(Object args, String cardholderName, String primaryAccountSuffix, String title, Array.<Object> showContents, String encryptScheme, String panid)

基础库 3.8.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.addPaymentPassGetCertificateData.html

**Object args**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| style | number |  | 是 | 0: Payment 1: Access |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object args**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| result | String | 返回值 |
| errorMsg | String | 错误信息 |
| certificates | Array.<String> | 证书链，由PassKit生成，二进制转Base64数据 |
| signNonce | String | nonce签名，二进制转Base64数据 |
| errnonceorMsg | String | nonce，二进制转Base64数据 |

**Array.<Object> showContents**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| key | String |  | 是 | 卡标题 |
| value | String |  | 是 | 卡描述文案 |

---

### wx.addPaymentPassFinish(Object args)

基础库 3.8.5 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.addPaymentPassFinish.html

**Object args**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| panid | String |  | 是 | addPaymentPassGetCertificateData传入的id |
| encryptedPassData | String |  | 是 | base64格式，详见PKAddPaymentPassRequest |
| ephemeralPublicKey | String |  | 是 | base64格式，详见PKAddPaymentPassRequest |
| activationData | String |  | 是 | base64格式，详见PKAddPaymentPassRequest |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object args**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| result | String | 返回值 |
| errorMsg | String | 错误信息 |

---

### IsoDep

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/IsoDep.html

---

### IsoDep.close(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/IsoDep.close.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### IsoDep.connect(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/IsoDep.connect.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### IsoDep.getHistoricalBytes(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/IsoDep.getHistoricalBytes.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| histBytes | ArrayBuffer | 返回历史二进制数据 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### IsoDep.getMaxTransceiveLength(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/IsoDep.getMaxTransceiveLength.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| length | number | 最大传输长度 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### IsoDep.isConnected(Object object)

该接口已废弃，连接状态开发者自行维护即可

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/IsoDep.isConnected.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### IsoDep.setTimeout(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/IsoDep.setTimeout.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number |  | 是 | 设置超时时间 (ms) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### IsoDep.transceive(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/IsoDep.transceive.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| data | ArrayBuffer |  | 是 | 需要传递的二进制数据 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | ArrayBuffer |  |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### MifareClassic

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/MifareClassic.html

---

### MifareClassic.close(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/MifareClassic.close.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### MifareClassic.connect(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/MifareClassic.connect.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### MifareClassic.getMaxTransceiveLength(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/MifareClassic.getMaxTransceiveLength.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| length | number | 最大传输长度 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### MifareClassic.isConnected(Object object)

该接口已废弃，连接状态开发者自行维护即可

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/MifareClassic.isConnected.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### MifareClassic.setTimeout(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/MifareClassic.setTimeout.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number |  | 是 | 设置超时时间 (ms) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### MifareClassic.transceive(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/MifareClassic.transceive.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| data | ArrayBuffer |  | 是 | 需要传递的二进制数据 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | ArrayBuffer |  |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### MifareUltralight

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/MifareUltralight.html

---

### MifareUltralight.close(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/MifareUltralight.close.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### MifareUltralight.connect(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/MifareUltralight.connect.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### MifareUltralight.getMaxTransceiveLength(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/MifareUltralight.getMaxTransceiveLength.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| length | number | 最大传输长度 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### MifareUltralight.isConnected(Object object)

该接口已废弃，连接状态开发者自行维护即可

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/MifareUltralight.isConnected.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### MifareUltralight.setTimeout(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/MifareUltralight.setTimeout.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number |  | 是 | 设置超时时间 (ms) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### MifareUltralight.transceive(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/MifareUltralight.transceive.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| data | ArrayBuffer |  | 是 | 需要传递的二进制数据 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | ArrayBuffer |  |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### Ndef

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/Ndef.html

---

### Ndef.close(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/Ndef.close.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### Ndef.connect(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/Ndef.connect.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### Ndef.isConnected(Object object)

该接口已废弃，连接状态开发者自行维护即可

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/Ndef.isConnected.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### Ndef.offNdefMessage(function callback)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/Ndef.offNdefMessage.html

---

### Ndef.onNdefMessage(function callback)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/Ndef.onNdefMessage.html

---

### Ndef.setTimeout(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/Ndef.setTimeout.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number |  | 是 | 设置超时时间 (ms) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### Ndef.writeNdefMessage(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/Ndef.writeNdefMessage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| uris | Array |  | 否 | uri 数组 |
| texts | Array |  | 否 | text 数组 |
| records | Array |  | 否 | 二进制对象数组, 需要指明 id, type 以及 payload (均为 ArrayBuffer 类型) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcA

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcA.html

---

### NfcA.close(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcA.close.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcA.connect(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcA.connect.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcA.getAtqa(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcA.getAtqa.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| atqa | ArrayBuffer | 返回 ATQA/SENS\_RES 数据 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcA.getMaxTransceiveLength(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcA.getMaxTransceiveLength.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| length | number | 最大传输长度 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcA.getSak(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcA.getSak.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| sak | number | 返回 SAK/SEL\_RES 数据 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcA.isConnected(Object object)

该接口已废弃，连接状态开发者自行维护即可

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcA.isConnected.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcA.setTimeout(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcA.setTimeout.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number |  | 是 | 设置超时时间 (ms) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcA.transceive(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcA.transceive.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| data | ArrayBuffer |  | 是 | 需要传递的二进制数据 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | ArrayBuffer |  |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NFCAdapter

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.html

**Object tech**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| ndef | string | 对应Ndef实例，实例支持对NDEF格式的NFC标签上的NDEF数据的读写 |
| nfcA | string | 对应NfcA实例，实例支持NFC-A (ISO 14443-3A)标准的读写 |
| nfcB | string | 对应NfcB实例，实例支持NFC-B (ISO 14443-3B)标准的读写 |
| isoDep | string | 对应IsoDep实例，实例支持ISO-DEP (ISO 14443-4)标准的读写 |
| nfcF | string | 对应NfcF实例，实例支持NFC-F (JIS 6319-4)标准的读写 |
| nfcV | string | 对应NfcV实例，实例支持NFC-V (ISO 15693)标准的读写 |
| mifareClassic | string | 对应MifareClassic实例，实例支持MIFARE Classic标签的读写 |
| mifareUltralight | string | 对应MifareUltralight实例，实例支持MIFARE Ultralight标签的读写 |

---

### IsoDep NFCAdapter.getIsoDep()

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.getIsoDep.html

---

### MifareClassic NFCAdapter.getMifareClassic()

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.getMifareClassic.html

---

### MifareUltralight NFCAdapter.getMifareUltralight()

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.getMifareUltralight.html

---

### Ndef NFCAdapter.getNdef()

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.getNdef.html

---

### NfcA NFCAdapter.getNfcA()

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.getNfcA.html

---

### NfcB NFCAdapter.getNfcB()

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.getNfcB.html

---

### NfcF NFCAdapter.getNfcF()

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.getNfcF.html

---

### NfcV NFCAdapter.getNfcV()

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.getNfcV.html

---

### NFCAdapter.offDiscovered(function listener)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.offDiscovered.html

---

### NFCAdapter.onDiscovered(function listener)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.onDiscovered.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| id | ArrayBuffer |  |
| techs | Array | tech 数组，用于匹配NFC卡片具体可以使用什么标准（NfcA等实例）处理 |
| messages | Array | 可选，NdefMessage 数组，消息格式为 {id: ArrayBuffer, type: ArrayBuffer, payload: ArrayBuffer} |

---

### NFCAdapter.startDiscovery(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.startDiscovery.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NFCAdapter.stopDiscovery(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.stopDiscovery.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcB

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcB.html

---

### NfcB.close(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcB.close.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcB.connect(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcB.connect.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcB.getMaxTransceiveLength(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcB.getMaxTransceiveLength.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| length | number | 最大传输长度 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcB.isConnected(Object object)

该接口已废弃，连接状态开发者自行维护即可

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcB.isConnected.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcB.setTimeout(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcB.setTimeout.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number |  | 是 | 设置超时时间 (ms) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcB.transceive(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcB.transceive.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| data | ArrayBuffer |  | 是 | 需要传递的二进制数据 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | ArrayBuffer |  |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcF

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcF.html

---

### NfcF.close(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcF.close.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcF.connect(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcF.connect.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcF.getMaxTransceiveLength(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcF.getMaxTransceiveLength.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| length | number | 最大传输长度 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcF.isConnected(Object object)

该接口已废弃，连接状态开发者自行维护即可

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcF.isConnected.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcF.setTimeout(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcF.setTimeout.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number |  | 是 | 设置超时时间 (ms) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcF.transceive(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcF.transceive.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| data | ArrayBuffer |  | 是 | 需要传递的二进制数据 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | ArrayBuffer |  |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcV

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcV.html

---

### NfcV.close(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcV.close.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcV.connect(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcV.connect.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcV.getMaxTransceiveLength(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcV.getMaxTransceiveLength.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| length | number | 最大传输长度 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcV.isConnected(Object object)

该接口已废弃，连接状态开发者自行维护即可

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcV.isConnected.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcV.setTimeout(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcV.setTimeout.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number |  | 是 | 设置超时时间 (ms) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### NfcV.transceive(Object object)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcV.transceive.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| data | ArrayBuffer |  | 是 | 需要传递的二进制数据 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | ArrayBuffer |  |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 13000 | 设备不支持NFC |  |
| 13001 | 系统NFC开关未打开 |  |
| 13010 | 未知错误 |  |
| 13019 | user is not authorized | 用户未授权 |
| 13011 | invalid parameter | 参数无效 |
| 13012 | parse NdefMessage failed | 将参数解析为NdefMessage失败 |
| 13021 | NFC discovery already started | 已经开始NFC扫描 |
| 13018 | NFC discovery has not started | 尝试在未开始NFC扫描时停止NFC扫描 |
| 13022 | Tech already connected | 标签已经连接 |
| 13023 | Tech has not connected | 尝试在未连接标签时断开连接 |
| 13013 | NFC tag has not been discovered | 未扫描到NFC标签 |
| 13014 | invalid tech | 无效的标签技术 |
| 13015 | unavailable tech | 从标签上获取对应技术失败 |
| 13024 | function not support | 当前标签技术不支持该功能 |
| 13017 | system internal error | 相关读写操作失败 |
| 13016 | connect fail | 连接失败 |

---

### wx.stopWifi(Object object)

基础库 1.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.stopWifi.html

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
| 12000 | not init | 未先调用 `startWifi` 接口 |
| 12001 | system not support | 当前系统不支持相关能力 |
| 12002 | password error Wi-Fi | 密码错误 |
| 12003 | connection timeout | 连接超时, 仅 Android 支持 |
| 12004 | duplicate request | 重复连接 Wi-Fi |
| 12005 | wifi not turned on | Android 特有，未打开 Wi-Fi 开关 |
| 12006 | gps not turned on | Android 特有，未打开 GPS 定位开关 |
| 12007 | user denied | 用户拒绝授权链接 Wi-Fi |
| 12008 | invalid SSID | 无效 SSID |
| 12009 | system config err | 系统运营商配置拒绝连接 Wi-Fi |
| 12010 | system internal error | 系统其他错误，需要在 errmsg 打印具体的错误原因 |
| 12011 | weapp in background | 应用在后台无法配置 Wi-Fi |
| 12013 | wifi config may be expired | 系统保存的 Wi-Fi 配置过期，建议忘记 Wi-Fi 后重试，仅 Android 支持 |
| 12014 | invalid WEP / WPA password | iOS 特有，无效的 WEP / WPA 密码 |

---

### wx.startWifi(Object object)

基础库 1.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.startWifi.html

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
| 12000 | not init | 未先调用 `startWifi` 接口 |
| 12001 | system not support | 当前系统不支持相关能力 |
| 12002 | password error Wi-Fi | 密码错误 |
| 12003 | connection timeout | 连接超时, 仅 Android 支持 |
| 12004 | duplicate request | 重复连接 Wi-Fi |
| 12005 | wifi not turned on | Android 特有，未打开 Wi-Fi 开关 |
| 12006 | gps not turned on | Android 特有，未打开 GPS 定位开关 |
| 12007 | user denied | 用户拒绝授权链接 Wi-Fi |
| 12008 | invalid SSID | 无效 SSID |
| 12009 | system config err | 系统运营商配置拒绝连接 Wi-Fi |
| 12010 | system internal error | 系统其他错误，需要在 errmsg 打印具体的错误原因 |
| 12011 | weapp in background | 应用在后台无法配置 Wi-Fi |
| 12013 | wifi config may be expired | 系统保存的 Wi-Fi 配置过期，建议忘记 Wi-Fi 后重试，仅 Android 支持 |
| 12014 | invalid WEP / WPA password | iOS 特有，无效的 WEP / WPA 密码 |

---

### wx.setWifiList(Object object)

基础库 1.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.setWifiList.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | wifiList | Array.<Object> |  | 是 | 提供预设的 Wi-Fi 信息列表 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | SSID | string |  | 否 | Wi-Fi 的 SSID | |  | BSSID | string |  | 否 | Wi-Fi 的 BSSID | |  | password | string |  | 否 | Wi-Fi 设备密码 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | SSID | string |  | 否 | Wi-Fi 的 SSID |
|  | BSSID | string |  | 否 | Wi-Fi 的 BSSID |
|  | password | string |  | 否 | Wi-Fi 设备密码 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| 12000 | not init | 未先调用 `startWifi` 接口 |
| 12001 | system not support | 当前系统不支持相关能力 |
| 12002 | password error Wi-Fi | 密码错误 |
| 12003 | connection timeout | 连接超时, 仅 Android 支持 |
| 12004 | duplicate request | 重复连接 Wi-Fi |
| 12005 | wifi not turned on | Android 特有，未打开 Wi-Fi 开关 |
| 12006 | gps not turned on | Android 特有，未打开 GPS 定位开关 |
| 12007 | user denied | 用户拒绝授权链接 Wi-Fi |
| 12008 | invalid SSID | 无效 SSID |
| 12009 | system config err | 系统运营商配置拒绝连接 Wi-Fi |
| 12010 | system internal error | 系统其他错误，需要在 errmsg 打印具体的错误原因 |
| 12011 | weapp in background | 应用在后台无法配置 Wi-Fi |
| 12013 | wifi config may be expired | 系统保存的 Wi-Fi 配置过期，建议忘记 Wi-Fi 后重试，仅 Android 支持 |
| 12014 | invalid WEP / WPA password | iOS 特有，无效的 WEP / WPA 密码 |

---

### wx.onWifiConnectedWithPartialInfo(function listener)

基础库 2.22.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.onWifiConnectedWithPartialInfo.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| wifi | [WifiInfo](WifiInfo.html) | 只包含 SSID 属性的 WifiInfo 对象 |

---

### wx.onWifiConnected(function listener)

基础库 1.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.onWifiConnected.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| wifi | [WifiInfo](WifiInfo.html) | Wi-Fi 信息 |

---

### wx.onGetWifiList(function listener)

基础库 1.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.onGetWifiList.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| wifiList | Array.<[WifiInfo](WifiInfo.html)> | Wi-Fi 列表数据 |

---

### wx.offWifiConnectedWithPartialInfo(function listener)

基础库 2.22.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.offWifiConnectedWithPartialInfo.html

---

### wx.offWifiConnected(function listener)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.offWifiConnected.html

---

### wx.offGetWifiList(function listener)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.offGetWifiList.html

---

### wx.getWifiList(Object object)

基础库 1.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.getWifiList.html

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
| 12000 | not init | 未先调用 `startWifi` 接口 |
| 12001 | system not support | 当前系统不支持相关能力 |
| 12002 | password error Wi-Fi | 密码错误 |
| 12003 | connection timeout | 连接超时, 仅 Android 支持 |
| 12004 | duplicate request | 重复连接 Wi-Fi |
| 12005 | wifi not turned on | Android 特有，未打开 Wi-Fi 开关 |
| 12006 | gps not turned on | Android 特有，未打开 GPS 定位开关 |
| 12007 | user denied | 用户拒绝授权链接 Wi-Fi |
| 12008 | invalid SSID | 无效 SSID |
| 12009 | system config err | 系统运营商配置拒绝连接 Wi-Fi |
| 12010 | system internal error | 系统其他错误，需要在 errmsg 打印具体的错误原因 |
| 12011 | weapp in background | 应用在后台无法配置 Wi-Fi |
| 12013 | wifi config may be expired | 系统保存的 Wi-Fi 配置过期，建议忘记 Wi-Fi 后重试，仅 Android 支持 |
| 12014 | invalid WEP / WPA password | iOS 特有，无效的 WEP / WPA 密码 |

---

### wx.getConnectedWifi(Object object)

基础库 1.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.getConnectedWifi.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| partialInfo | boolean | false | 否 | 是否需要返回部分 Wi-Fi 信息 | [2.22.0](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| wifi | [WifiInfo](WifiInfo.html) | Wi-Fi 信息 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| 12000 | not init | 未先调用 `startWifi` 接口 |
| 12001 | system not support | 当前系统不支持相关能力 |
| 12002 | password error Wi-Fi | 密码错误 |
| 12003 | connection timeout | 连接超时, 仅 Android 支持 |
| 12004 | duplicate request | 重复连接 Wi-Fi |
| 12005 | wifi not turned on | Android 特有，未打开 Wi-Fi 开关 |
| 12006 | gps not turned on | Android 特有，未打开 GPS 定位开关 |
| 12007 | user denied | 用户拒绝授权链接 Wi-Fi |
| 12008 | invalid SSID | 无效 SSID |
| 12009 | system config err | 系统运营商配置拒绝连接 Wi-Fi |
| 12010 | system internal error | 系统其他错误，需要在 errmsg 打印具体的错误原因 |
| 12011 | weapp in background | 应用在后台无法配置 Wi-Fi |
| 12013 | wifi config may be expired | 系统保存的 Wi-Fi 配置过期，建议忘记 Wi-Fi 后重试，仅 Android 支持 |
| 12014 | invalid WEP / WPA password | iOS 特有，无效的 WEP / WPA 密码 |

---

### wx.connectWifi(Object object)

基础库 1.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.connectWifi.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| SSID | string |  | 是 | Wi-Fi 设备 SSID |  |
| BSSID | string |  | 否 | Wi-Fi 设备 BSSID |  |
| password | string |  | 是 | Wi-Fi 设备密码 |  |
| maunal | boolean | false | 否 | 跳转到系统设置页进行连接 | [2.12.0](../../../framework/compatibility.html) |
| partialInfo | boolean | false | 否 | 是否需要返回部分 Wi-Fi 信息，仅安卓生效 | [2.22.0](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| 12000 | not init | 未先调用 `startWifi` 接口 |
| 12001 | system not support | 当前系统不支持相关能力 |
| 12002 | password error Wi-Fi | 密码错误 |
| 12003 | connection timeout | 连接超时, 仅 Android 支持 |
| 12004 | duplicate request | 重复连接 Wi-Fi |
| 12005 | wifi not turned on | Android 特有，未打开 Wi-Fi 开关 |
| 12006 | gps not turned on | Android 特有，未打开 GPS 定位开关 |
| 12007 | user denied | 用户拒绝授权链接 Wi-Fi |
| 12008 | invalid SSID | 无效 SSID |
| 12009 | system config err | 系统运营商配置拒绝连接 Wi-Fi |
| 12010 | system internal error | 系统其他错误，需要在 errmsg 打印具体的错误原因 |
| 12011 | weapp in background | 应用在后台无法配置 Wi-Fi |
| 12013 | wifi config may be expired | 系统保存的 Wi-Fi 配置过期，建议忘记 Wi-Fi 后重试，仅 Android 支持 |
| 12014 | invalid WEP / WPA password | iOS 特有，无效的 WEP / WPA 密码 |

---

### WifiInfo

相关文档:无线局域网 (Wi-Fi)

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/WifiInfo.html

---

### wx.addPhoneRepeatCalendar(Object object)

基础库 2.15.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/calendar/wx.addPhoneRepeatCalendar.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | title | string |  | 是 | 日历事件标题 |  |
|  | startTime | number |  | 是 | 开始时间的 unix 时间戳 (1970年1月1日开始所经过的秒数) |  |
|  | allDay | boolean |  | 否 | 是否全天事件，默认 false |  |
|  | description | string |  | 否 | 事件说明 |  |
|  | location | string |  | 否 | 事件位置 |  |
|  | endTime | string |  | 否 | 结束时间的 unix 时间戳，默认与开始时间相同 |  |
|  | alarm | boolean |  | 否 | 是否提醒，默认 true |  |
|  | alarmOffset | number |  | 否 | 提醒提前量，单位秒，默认 0 表示开始时提醒 |  |
|  | repeatInterval | string |  | 否 | 重复周期，默认 month 每月重复 |  |
|  | | 合法值 | 说明 | | --- | --- | | day | 每天重复 | | week | 每周重复 | | month | 每月重复。该模式日期不能大于 28 日 | | year | 每年重复 | | | | | | |
|  | repeatEndTime | number |  | 否 | 重复周期结束时间的 unix 时间戳，不填表示一直重复 |  |
|  | path | string |  | 否 | 跳转小程序路径，必须要和 signature 一起使用，填入后会自动生成跳转链接拼接在事件说明中 | [3.7.6](../../../framework/compatibility.html) |
|  | signature | string |  | 否 | 跳转小程序路径签名，必须要和 path 一起使用，用 session\_key 对 path 签名得到的结果，即 `hmac_sha256(session_key, path)`。详见 [用户数据的签名验证和加解密](../../../framework/open-ability/signature.html) | [3.7.6](../../../framework/compatibility.html) |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| day | 每天重复 |
| week | 每周重复 |
| month | 每月重复。该模式日期不能大于 28 日 |
| year | 每年重复 |

---

### wx.addPhoneCalendar(Object object)

基础库 2.15.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/calendar/wx.addPhoneCalendar.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| title | string |  | 是 | 日历事件标题 |  |
| startTime | number |  | 是 | 开始时间的 unix 时间戳 |  |
| allDay | boolean |  | 否 | 是否全天事件，默认 false |  |
| description | string |  | 否 | 事件说明 |  |
| location | string |  | 否 | 事件位置 |  |
| endTime | string |  | 否 | 结束时间的 unix 时间戳，默认与开始时间相同 |  |
| alarm | boolean |  | 否 | 是否提醒，默认 true |  |
| alarmOffset | number |  | 否 | 提醒提前量，单位秒，默认 0 表示开始时提醒 |  |
| path | string |  | 否 | 跳转小程序路径，必须要和 signature 一起使用，填入后会自动生成跳转链接拼接在事件说明中 | [3.7.6](../../../framework/compatibility.html) |
| signature | string |  | 否 | 跳转小程序路径签名，必须要和 path 一起使用，用 session\_key 对 path 签名得到的结果，即 `hmac_sha256(session_key, path)`。详见 [用户数据的签名验证和加解密](../../../framework/open-ability/signature.html) | [3.7.6](../../../framework/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

---

### wx.chooseContact(Object object)

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/contact/wx.chooseContact.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| phoneNumber | string | 手机号 |
| displayName | string | 联系人姓名 |
| phoneNumberList | string | 选定联系人的所有手机号（部分 Android 系统只能选联系人而不能选特定手机号） |

---

### wx.addPhoneContact(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/contact/wx.addPhoneContact.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| firstName | string |  | 是 | 名字 |
| photoFilePath | string |  | 否 | 头像本地文件路径 |
| nickName | string |  | 否 | 昵称 |
| lastName | string |  | 否 | 姓氏 |
| middleName | string |  | 否 | 中间名 |
| remark | string |  | 否 | 备注 |
| mobilePhoneNumber | string |  | 否 | 手机号 |
| weChatNumber | string |  | 否 | 微信号 |
| addressCountry | string |  | 否 | 联系地址国家 |
| addressState | string |  | 否 | 联系地址省份 |
| addressCity | string |  | 否 | 联系地址城市 |
| addressStreet | string |  | 否 | 联系地址街道 |
| addressPostalCode | string |  | 否 | 联系地址邮政编码 |
| organization | string |  | 否 | 公司 |
| title | string |  | 否 | 职位 |
| workFaxNumber | string |  | 否 | 工作传真 |
| workPhoneNumber | string |  | 否 | 工作电话 |
| hostNumber | string |  | 否 | 公司电话 |
| email | string |  | 否 | 电子邮件 |
| url | string |  | 否 | 网站 |
| workAddressCountry | string |  | 否 | 工作地址国家 |
| workAddressState | string |  | 否 | 工作地址省份 |
| workAddressCity | string |  | 否 | 工作地址城市 |
| workAddressStreet | string |  | 否 | 工作地址街道 |
| workAddressPostalCode | string |  | 否 | 工作地址邮政编码 |
| homeFaxNumber | string |  | 否 | 住宅传真 |
| homePhoneNumber | string |  | 否 | 住宅电话 |
| homeAddressCountry | string |  | 否 | 住宅地址国家 |
| homeAddressState | string |  | 否 | 住宅地址省份 |
| homeAddressCity | string |  | 否 | 住宅地址城市 |
| homeAddressStreet | string |  | 否 | 住宅地址街道 |
| homeAddressPostalCode | string |  | 否 | 住宅地址邮政编码 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.checkIsOpenAccessibility(Object object)

基础库 2.13.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/accessibility/wx.checkIsOpenAccessibility.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| open | Boolean | iOS 上开启辅助功能旁白，安卓开启 talkback 时返回 true |

---

### wx.onBatteryInfoChange(function listener)

基础库 3.5.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/battery/wx.onBatteryInfoChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| isLowPowerModeEnabled | boolean | 是否处于省电模式 |

---

### wx.offBatteryInfoChange(function listener)

基础库 3.5.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/battery/wx.offBatteryInfoChange.html

---

### Object wx.getBatteryInfoSync()

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/battery/wx.getBatteryInfoSync.html

**Object res**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| level | number | 设备电量，范围 1 - 100 |  |
| isCharging | boolean | 是否正在充电中 |  |
| isLowPowerModeEnabled | boolean | 是否处于省电模式 | [3.5.0](../../../framework/compatibility.html) |

---

### wx.getBatteryInfo(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/battery/wx.getBatteryInfo.html

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
| isLowPowerModeEnabled | boolean | 是否处于省电模式 | [3.5.0](../../../framework/compatibility.html) |

---

### wx.setClipboardData(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/clipboard/wx.setClipboardData.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/clipboard/wx.getClipboardData.html

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

### wx.stopHCE(Object object)

基础库 1.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc-hce/wx.stopHCE.html

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
| 13000 |  | 当前设备不支持NFC |
| 13001 |  | 当前设备支持NFC，但系统NFC开关未开启 |
| 13002 |  | 当前设备支持NFC，但不支持HCE |
| 13003 |  | AID列表参数格式错误 |
| 13004 |  | 未设置微信为默认NFC支付应用 |
| 13005 |  | 返回的指令不合法 |
| 13006 |  | 注册AID失败 |

---

### wx.startHCE(Object object)

基础库 1.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc-hce/wx.startHCE.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| aid\_list | Array.<string> |  | 是 | 需要注册到系统的 AID 列表 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| 13000 |  | 当前设备不支持NFC |
| 13001 |  | 当前设备支持NFC，但系统NFC开关未开启 |
| 13002 |  | 当前设备支持NFC，但不支持HCE |
| 13003 |  | AID列表参数格式错误 |
| 13004 |  | 未设置微信为默认NFC支付应用 |
| 13005 |  | 返回的指令不合法 |
| 13006 |  | 注册AID失败 |

---

### wx.sendHCEMessage(Object object)

基础库 1.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc-hce/wx.sendHCEMessage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| data | ArrayBuffer |  | 是 | 二进制数据 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| 13000 |  | 当前设备不支持NFC |
| 13001 |  | 当前设备支持NFC，但系统NFC开关未开启 |
| 13002 |  | 当前设备支持NFC，但不支持HCE |
| 13003 |  | AID列表参数格式错误 |
| 13004 |  | 未设置微信为默认NFC支付应用 |
| 13005 |  | 返回的指令不合法 |
| 13006 |  | 注册AID失败 |

---

### wx.onHCEMessage(function listener)

基础库 1.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc-hce/wx.onHCEMessage.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | messageType | number | 消息类型 |
|  | | 合法值 | 说明 | | --- | --- | | 1 | HCE APDU Command类型，小程序需对此指令进行处理，并调用 sendHCEMessage 接口返回处理指令 | | 2 | 设备离场事件类型 | | | |
|  | data | ArrayBuffer | `messageType=1` 时 ,客户端接收到 NFC 设备的指令 |
|  | reason | number | `messageType=2` 时，原因 |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| 1 | HCE APDU Command类型，小程序需对此指令进行处理，并调用 sendHCEMessage 接口返回处理指令 |
| 2 | 设备离场事件类型 |

---

### wx.offHCEMessage(function listener)

基础库 2.8.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc-hce/wx.offHCEMessage.html

---

### wx.getHCEState(Object object)

基础库 1.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc-hce/wx.getHCEState.html

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
| 13000 |  | 当前设备不支持NFC |
| 13001 |  | 当前设备支持NFC，但系统NFC开关未开启 |
| 13002 |  | 当前设备支持NFC，但不支持HCE |
| 13003 |  | AID列表参数格式错误 |
| 13004 |  | 未设置微信为默认NFC支付应用 |
| 13005 |  | 返回的指令不合法 |
| 13006 |  | 注册AID失败 |

---

### wx.onNetworkWeakChange(function listener)

基础库 2.21.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/network/wx.onNetworkWeakChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| weakNet | boolean | 当前是否处于弱网状态 |
| networkType | string | 当前网络类型 |

---

### wx.onNetworkStatusChange(function listener)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/network/wx.onNetworkStatusChange.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/network/wx.offNetworkWeakChange.html

---

### wx.offNetworkStatusChange(function listener)

基础库 2.9.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/network/wx.offNetworkStatusChange.html

---

### wx.getNetworkType(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/network/wx.getNetworkType.html

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
|  | hasSystemProxy | Boolean | 设备是否使用了网络代理 | [2.22.1](../../../framework/compatibility.html) |
|  | weakNet | Boolean | 是否处于弱网环境 | [3.5.3](../../../framework/compatibility.html) |

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/network/wx.getLocalIPAddress.html

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

### wx.getRandomValues(Object object)

基础库 2.15.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/crypto/wx.getRandomValues.html

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

### wx.setVisualEffectOnCapture(Object object)

基础库 2.20.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.setVisualEffectOnCapture.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.setScreenBrightness.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.setKeepScreenOn.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keepScreenOn | boolean |  | 是 | 是否保持屏幕常亮 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.onUserCaptureScreen(function listener)

基础库 1.4.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.onUserCaptureScreen.html

**function listener**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| query | string | 支持开发者自定义一键打开小程序时的 query | [3.3.0](../../../framework/compatibility.html) |
| promise | promise | 如果该参数存在，则其它的参数将会以 resolve 结果为准，如果一秒内不 resolve，分享会使用上面传入的默认参数 | [3.3.0](../../../framework/compatibility.html) |

---

### wx.onScreenRecordingStateChanged(function listener)

基础库 2.24.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.onScreenRecordingStateChanged.html

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

### wx.onGeneratePoster(function listener)

基础库 3.12.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.onGeneratePoster.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| src | string | 开发者生成自定义海报图片的路径，支持网络路径、本地路径 |
| promise | Object | 如果该参数存在，则其它的参数将会以 resolve 结果为准，如果3秒内不 resolve，会使用上面传入的默认参数 |

---

### wx.offUserCaptureScreen()

基础库 2.9.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.offUserCaptureScreen.html

---

### wx.offScreenRecordingStateChanged(function listener)

基础库 2.24.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.offScreenRecordingStateChanged.html

---

### wx.offGeneratePoster()

基础库 3.12.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.offGeneratePoster.html

---

### wx.getScreenRecordingState(Object object)

基础库 2.24.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.getScreenRecordingState.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.getScreenBrightness.html

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

### wx.onKeyUp(function listener)

基础库 3.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/keyboard/wx.onKeyUp.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| key | string | 按键名称，同 Web 规范 KeyEvent key 属性 |
| code | string | 按键 code，同 Web 规范 KeyEvent code 属性 |
| altKey | string | 当前是否同时按下了 altKey，同 Web 规范 KeyEvent altKey 属性 |
| shiftKey | string | 当前是否同时按下了 shiftKey，同 Web 规范 KeyEvent shiftKey 属性 |
| timeStamp | number | 事件触发时的时间戳 |

---

### wx.onKeyDown(function listener)

基础库 3.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/keyboard/wx.onKeyDown.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| key | string | 按键名称，同 Web 规范 KeyEvent key 属性 |
| code | string | 按键 code，同 Web 规范 KeyEvent code 属性 |
| altKey | string | 当前是否同时按下了 altKey，同 Web 规范 KeyEvent altKey 属性 |
| shiftKey | string | 当前是否同时按下了 shiftKey，同 Web 规范 KeyEvent shiftKey 属性 |
| timeStamp | number | 事件触发时的时间戳 |

---

### wx.onKeyboardHeightChange(function listener)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/keyboard/wx.onKeyboardHeightChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| height | number | 键盘高度 |

---

### wx.offKeyUp(function listener)

基础库 3.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/keyboard/wx.offKeyUp.html

---

### wx.offKeyDown(function listener)

基础库 3.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/keyboard/wx.offKeyDown.html

---

### wx.offKeyboardHeightChange(function listener)

基础库 2.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/keyboard/wx.offKeyboardHeightChange.html

---

### wx.hideKeyboard(Object object)

基础库 2.8.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/keyboard/wx.hideKeyboard.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.getSelectedTextRange(Object object)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/keyboard/wx.getSelectedTextRange.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| start | number | 输入框光标起始位置 |
| end | number | 输入框光标结束位置 |

---

### wx.makePhoneCall(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/phone/wx.makePhoneCall.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| phoneNumber | string |  | 是 | 需要拨打的电话号码 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.stopAccelerometer(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/accelerometer/wx.stopAccelerometer.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.startAccelerometer(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/accelerometer/wx.startAccelerometer.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | interval | string | normal | 否 | 监听加速度数据回调函数的执行频率 | [2.1.0](../../../framework/compatibility.html) |
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

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/accelerometer/wx.onAccelerometerChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| x | number | X 轴 |
| y | number | Y 轴 |
| z | number | Z 轴 |

---

### wx.offAccelerometerChange(function listener)

基础库 2.9.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/accelerometer/wx.offAccelerometerChange.html

---

### wx.stopCompass(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/compass/wx.stopCompass.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.startCompass(Object object)

基础库 1.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/compass/wx.startCompass.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.onCompassChange(function listener)

小程序插件：不支持

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/compass/wx.onCompassChange.html

**function listener**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| direction | number | 面对的方向度数 |  |
| accuracy | number/string | 精度 | [2.4.0](../../../framework/compatibility.html) |

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/compass/wx.offCompassChange.html

---

### wx.stopDeviceMotionListening(Object object)

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/motion/wx.stopDeviceMotionListening.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.startDeviceMotionListening(Object object)

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/motion/wx.startDeviceMotionListening.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/motion/wx.onDeviceMotionChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| alpha | number | 当 手机坐标 X/Y 和 地球 X/Y 重合时，绕着 Z 轴转动的夹角为 alpha，范围值为 [0, 2\*PI)。逆时针转动为正。 |
| beta | number | 当手机坐标 Y/Z 和地球 Y/Z 重合时，绕着 X 轴转动的夹角为 beta。范围值为 [-1\*PI, PI) 。顶部朝着地球表面转动为正。也有可能朝着用户为正。 |
| gamma | number | 当手机 X/Z 和地球 X/Z 重合时，绕着 Y 轴转动的夹角为 gamma。范围值为 [-1\*PI/2, PI/2)。右边朝着地球表面转动为正。 |

---

### wx.offDeviceMotionChange(function listener)

基础库 2.9.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/motion/wx.offDeviceMotionChange.html

---

### wx.stopGyroscope(Object object)

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/gyroscope/wx.stopGyroscope.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.startGyroscope(Object object)

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/gyroscope/wx.startGyroscope.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/gyroscope/wx.onGyroscopeChange.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| x | number | x 轴的角速度 |
| y | number | y 轴的角速度 |
| z | number | z 轴的角速度 |

---

### wx.offGyroscopeChange(function listener)

基础库 2.9.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/gyroscope/wx.offGyroscopeChange.html

---

### wx.onMemoryWarning(function listener)

基础库 2.0.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/memory/wx.onMemoryWarning.html

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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/memory/wx.offMemoryWarning.html

---

### wx.scanCode(Object object)

基础库 1.0.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/scan/wx.scanCode.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | onlyFromCamera | boolean | false | 否 | 是否只能从相机扫码，不允许从相册选择图片 | [1.2.0](../../../framework/compatibility.html) |
|  | scanType | Array.<string> | ['barCode', 'qrCode', 'wxCode'] | 否 | 扫码类型 | [1.7.0](../../../framework/compatibility.html) |
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

### wx.sendSms(Object object)

基础库 2.25.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/sms/wx.sendSms.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| phoneNumber | string |  | 否 | 预填到发送短信面板的手机号 |
| content | string |  | 否 | 预填到发送短信面板的内容 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.vibrateShort(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/vibrate/wx.vibrateShort.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| type | string |  | 是 | 震动强度类型，有效值为：heavy、medium、light | [2.13.0](../../../framework/compatibility.html) |
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

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/device/vibrate/wx.vibrateLong.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

<!-- pages: 220 -->
