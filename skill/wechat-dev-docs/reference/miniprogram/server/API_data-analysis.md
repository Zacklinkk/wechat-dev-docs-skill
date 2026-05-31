# 小程序服务端 API 结构化参考 — API/data-analysis

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 获取用户访问小程序周留存

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/data-analysis/visit-retain/api_getweeklyretain.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin\_date | string | 是 | 开始日期，为周一日期。格式为 yyyymmdd |
| end\_date | string | 是 | 结束日期，为周日日期，限定查询一周数据。格式为 yyyymmdd |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ref\_date | string | 时间，如："20170306-20170312" |
| visit\_uv\_new | [objarray](#Res__visit_uv_new<Array>) | 新增用户留存 |
| visit\_uv | [objarray](#Res__visit_uv<Array>) | 活跃用户留存 |

**Res.visit_uv_new(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| key | number | 标识，0开始，表示当周，1表示1周后。依此类推，取值分别是：0,1,2,3,4 |
| value | number | key对应日期的新增用户数/活跃用户数（key=0时）或留存用户数（k>0时） |

**Res.visit_uv(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| key | number | 标识，0开始，表示当周，1表示1周后。依此类推，取值分别是：0,1,2,3,4 |
| value | number | key对应日期的新增用户数/活跃用户数（key=0时）或留存用户数（k>0时） |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取用户访问小程序月留存

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/data-analysis/visit-retain/api_getmonthlyretain.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin\_date | string | 是 | 开始日期，为自然月第一天。格式为 yyyymmdd |
| end\_date | string | 是 | 结束日期，为自然月最后一天，限定查询一个月数据。格式为 yyyymmdd |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ref\_date | string | 时间，如："201702" |
| visit\_uv\_new | [objarray](#Res__visit_uv_new<Array>) | 新增用户留存 |
| visit\_uv | [objarray](#Res__visit_uv<Array>) | 活跃用户留存 |

**Res.visit_uv_new(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| key | number | 标识，0开始，表示当月，1表示1月后。key取值分别是：0,1 |
| value | number | key对应日期的新增用户数/活跃用户数（key=0时）或留存用户数（k>0时） |

**Res.visit_uv(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| key | number | 标识，0开始，表示当月，1表示1月后。key取值分别是：0,1 |
| value | number | key对应日期的新增用户数/活跃用户数（key=0时）或留存用户数（k>0时） |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取用户访问小程序日留存

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/data-analysis/visit-retain/api_getdailyretain.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin\_date | string | 是 | 开始日期。格式为 yyyymmdd |
| end\_date | string | 是 | 结束日期，限定查询1天数据，允许设置的最大值为昨日。格式为 yyyymmdd |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ref\_date | string | 日期 |
| visit\_uv\_new | [objarray](#Res__visit_uv_new<Array>) | 新增用户留存 |
| visit\_uv | [objarray](#Res__visit_uv<Array>) | 活跃用户留存 |

**Res.visit_uv_new(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| key | number | 标识，0开始，表示当天，1表示1天后。依此类推，key取值分别是：0,1,2,3,4,5,6,7,14,30 |
| value | number | key对应日期的新增用户数/活跃用户数（key=0时）或留存用户数（k>0时） |

**Res.visit_uv(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| key | number | 标识，0开始，表示当天，1表示1天后。依此类推，key取值分别是：0,1,2,3,4,5,6,7,14,30 |
| value | number | key对应日期的新增用户数/活跃用户数（key=0时）或留存用户数（k>0时） |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取用户访问小程序数据月趋势

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/data-analysis/visit-trend/api_getmonthlyvisittrend.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin\_date | string | 是 | 开始日期，为自然月第一天。格式为 yyyymmdd |
| end\_date | string | 是 | 结束日期，为自然月最后一天，限定查询一个月的数据。格式为 yyyymmdd |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| list | [objarray](#Res__list<Array>) | 数据列表 |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ref\_date | string | 时间，格式为 yyyymm，如："201702" |
| session\_cnt | number | 打开次数（自然月内汇总） |
| visit\_pv | number | 访问次数（自然月内汇总） |
| visit\_uv | number | 访问人数（自然月内去重） |
| visit\_uv\_new | number | 新用户数（自然月内去重） |
| stay\_time\_uv | number | 人均停留时长 (浮点型，单位：秒) |
| stay\_time\_session | number | 次均停留时长 (浮点型，单位：秒) |
| visit\_depth | number | 平均访问深度 (浮点型) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取用户访问小程序数据日趋势

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/data-analysis/visit-trend/api_getdailyvisittrend.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin\_date | string | 是 | 开始日期。格式为 yyyymmdd |
| end\_date | string | 是 | 结束日期，限定查询1天数据，允许设置的最大值为昨日。格式为 yyyymmdd |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| list | [objarray](#Res__list<Array>) | 数据列表 |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ref\_date | string | 日期，格式为 yyyymmdd |
| session\_cnt | number | 打开次数 |
| visit\_pv | number | 访问次数 |
| visit\_uv | number | 访问人数 |
| visit\_uv\_new | number | 新用户数 |
| stay\_time\_uv | number | 人均停留时长 (浮点型，单位：秒) |
| stay\_time\_session | number | 次均停留时长 (浮点型，单位：秒) |
| visit\_depth | number | 平均访问深度 (浮点型) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 61504 | 系统繁忙，稍后再试试 | 系统繁忙，稍后再试试 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取用户访问小程序数据周趋势

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/data-analysis/visit-trend/api_getweeklyvisittrend.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin\_date | string | 是 | 开始日期，为周一日期。格式为 yyyymmdd |
| end\_date | string | 是 | 结束日期，为周日日期，限定查询一周数据。格式为 yyyymmdd |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| list | [objarray](#Res__list<Array>) | 数据列表 |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ref\_date | string | 时间，格式为 yyyymmdd-yyyymmdd，如："20170306-20170312" |
| session\_cnt | number | 打开次数（自然周内汇总） |
| visit\_pv | number | 访问次数（自然周内汇总） |
| visit\_uv | number | 访问人数（自然周内去重） |
| visit\_uv\_new | number | 新用户数（自然周内去重） |
| stay\_time\_uv | number | 人均停留时长 (浮点型，单位：秒) |
| stay\_time\_session | number | 次均停留时长 (浮点型，单位：秒) |
| visit\_depth | number | 平均访问深度 (浮点型) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取用户访问小程序数据概况

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/data-analysis/others/api_getdailysummary.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin\_date | string | 是 | 开始日期。格式为 yyyymmdd |
| end\_date | string | 是 | 结束日期，限定查询1天数据，允许设置的最大值为昨日。格式为 yyyymmdd |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| list | [objarray](#Res__list<Array>) | 数据列表 |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ref\_date | string | 日期，格式为 yyyymmdd |
| visit\_total | number | 累计用户数 |
| share\_pv | number | 转发次数 |
| share\_uv | number | 转发人数 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取访问页面数据

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/data-analysis/others/api_getvisitpage.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin\_date | string | 是 | 开始日期。格式为 yyyymmdd |
| end\_date | string | 是 | 结束日期，限定查询1天数据，允许设置的最大值为昨日。格式为 yyyymmdd |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ref\_date | string | 日期，格式为 yyyymmdd |
| list | [objarray](#Res__list<Array>) | 数据列表 |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| page\_path | string | 页面路径 |
| page\_visit\_pv | number | 访问次数 |
| page\_visit\_uv | number | 访问人数 |
| page\_staytime\_pv | number | 次均停留时长 |
| entrypage\_pv | number | 进入页次数 |
| exitpage\_pv | number | 退出页次数 |
| page\_share\_pv | number | 转发次数 |
| page\_share\_uv | number | 转发人数 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取小程序用户画像分布

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/data-analysis/others/api_getuserportrait.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin\_date | string | 是 | 开始日期。格式为 yyyymmdd |
| end\_date | string | 是 | 结束日期，开始日期与结束日期相差的天数限定为0/6/29，分别表示查询最近1/7/30天数据，允许设置的最大值为昨日。格式为 yyyymmdd |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ref\_date | string | 时间范围，如："20170611-20170617" |
| visit\_uv\_new | [object](#Res__visit_uv_new) | 新用户画像 |
| visit\_uv | [object](#Res__visit_uv) | 活跃用户画像 |

**Res.visit_uv_new Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| province | [objarray](#Res__visit_uv_new__province<Array>) | 省份，如北京、广东等 |
| city | [objarray](#Res__visit_uv_new__city<Array>) | 城市，如北京、广州等 |
| genders | [objarray](#Res__visit_uv_new__genders<Array>) | 性别，包括男、女、未知 |
| platforms | [objarray](#Res__visit_uv_new__platforms<Array>) | 平台类型，包括 Android、iOS 等 |
| devices | [objarray](#Res__visit_uv_new__devices<Array>) | 终端类型，包括 iPhone，android，其他 |
| ages | [objarray](#Res__visit_uv_new__ages<Array>) | 年龄，包括17岁以下、18-24岁等区间 |

**Res.visit_uv Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| province | [objarray](#Res__visit_uv__province<Array>) | 省份，如北京、广东等 |
| city | [objarray](#Res__visit_uv__city<Array>) | 城市，如北京、广州等 |
| genders | [objarray](#Res__visit_uv__genders<Array>) | 性别，包括男、女、未知 |
| platforms | [objarray](#Res__visit_uv__platforms<Array>) | 平台类型，包括 Android、iOS 等 |
| devices | [objarray](#Res__visit_uv__devices<Array>) | 终端类型，包括 iPhone，android，其他 |
| ages | [objarray](#Res__visit_uv__ages<Array>) | 年龄，包括17岁以下、18-24岁等区间 |

**Res.visit_uv_new.province(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | number | 属性值id |
| name | string | 属性值名称，与id对应。属性值为province、 city、 genders 、 platforms、devices 、 ages。 |
| value | number | 该场景访问uv |

**Res.visit_uv_new.city(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | number | 属性值id |
| name | string | 属性值名称，与id对应。属性值为province、 city、 genders 、 platforms、devices 、 ages。 |
| value | number | 该场景访问uv |

**Res.visit_uv_new.genders(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | number | 属性值id |
| name | string | 属性值名称，与id对应。属性值为province、 city、 genders 、 platforms、devices 、 ages。 |
| value | number | 该场景访问uv |

**Res.visit_uv_new.platforms(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | number | 属性值id |
| name | string | 属性值名称，与id对应。属性值为province、 city、 genders 、 platforms、devices 、 ages。 |
| value | number | 该场景访问uv |

**Res.visit_uv_new.devices(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | number | 属性值id |
| name | string | 属性值名称，与id对应。属性值为province、 city、 genders 、 platforms、devices 、 ages。 |
| value | number | 该场景访问uv |

**Res.visit_uv_new.ages(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | number | 属性值id |
| name | string | 属性值名称，与id对应。属性值为province、 city、 genders 、 platforms、devices 、 ages。 |
| value | number | 该场景访问uv |

**Res.visit_uv.province(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | number | 属性值id |
| name | string | 属性值名称，与id对应。属性值为province、 city、 genders 、 platforms、devices 、 ages。 |
| value | number | 该场景访问uv |

**Res.visit_uv.city(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | number | 属性值id |
| name | string | 属性值名称，与id对应。属性值为province、 city、 genders 、 platforms、devices 、 ages。 |
| value | number | 该场景访问uv |

**Res.visit_uv.genders(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | number | 属性值id |
| name | string | 属性值名称，与id对应。属性值为province、 city、 genders 、 platforms、devices 、 ages。 |
| value | number | 该场景访问uv |

**Res.visit_uv.platforms(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | number | 属性值id |
| name | string | 属性值名称，与id对应。属性值为province、 city、 genders 、 platforms、devices 、 ages。 |
| value | number | 该场景访问uv |

**Res.visit_uv.devices(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | number | 属性值id |
| name | string | 属性值名称，与id对应。属性值为province、 city、 genders 、 platforms、devices 、 ages。 |
| value | number | 该场景访问uv |

**Res.visit_uv.ages(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | number | 属性值id |
| name | string | 属性值名称，与id对应。属性值为province、 city、 genders 、 platforms、devices 、 ages。 |
| value | number | 该场景访问uv |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取小程序性能数据

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/data-analysis/others/api_getperformancedata.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| module | number | 是 | 查询数据的类型 |
| time | [object](#Body__time) | 是 | 开始和结束日期的时间戳，时间跨度不能超过30天 |
| params | [objarray](#Body__params<Array>) | 是 | 查询条件，比如机型，网络类型等等 |

**Body.time Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin\_timestamp | number | 是 | 开始日期时间戳 |
| end\_timestamp | number | 是 | 结束日期时间戳 |

**Body.params(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 查询条件 |
| value | string | 是 | 查询条件值 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| data | [object](#Res__data) | 返回的性能数据 |

**Res.data Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| body | [object](#Res__data__body) | 返回的性能数据 |

**Res.data.body Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| tables | [objarray](#Res__data__body__tables<Array>) | 返回的数据数组 |
| count | number | 数组大小 |

**Res.data.body.tables(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 性能数据指标id |
| lines | [objarray](#Res__data__body__tables<Array>__lines<Array>) | 按时间排列的性能数据 |
| zh | string | 性能数据指标中文名 |

**Res.data.body.tables(Array).linesObject Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| fields | [objarray](#Res__data__body__tables<Array>__lines<Array>__fields<Array>) | 单天的性能数据 |

**Res.data.body.tables(Array).lines.fieldsObject Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| refdate | string | 日期 |
| value | string | 性能数据值 |

**module 的合法值**

| 值 | 说明 |
| --- | --- |
| 10016 | 打开率, params字段可传入网络类型和机型 |
| 10017 | 启动各阶段耗时，params字段可传入网络类型和机型 |
| 10021 | 页面切换耗时，params数组字段可传入机型 |
| 10022 | 内存指标，params数组字段可传入机型 |
| 10023 | 内存异常，params数组字段可传入机型 |

**field 的合法值**

| 值 | 说明 |
| --- | --- |
| networktype | 网络类型作为查询条件，value=“-1,3g,4g,wifi”分别表示 全部网络类型，3G，4G，WIFI,不传networktype默认为全部网络类型 |
| device\_level | 机型作为查询条件，此时value=“-1,1,2,3”分别表示 全部机型，高档机，中档机，低档机,不传device\_level默认为全部机型 |
| device | 平台作为查询条件，此时value="-1,1,2"分别表示 全部平台，IOS平台，安卓平台,不传device默认为全部平台 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

### 获取用户小程序访问分布数据

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/data-analysis/others/api_getvisitdistribution.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin\_date | string | 是 | 开始日期。格式为 yyyymmdd |
| end\_date | string | 是 | 结束日期，限定查询 1 天数据，允许设置的最大值为昨日。格式为 yyyymmdd |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ref\_date | string | 日期，格式为 yyyymmdd |
| list | [objarray](#Res__list<Array>) | 数据列表 |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| index | string | 分布类型。枚举值为：access\_source\_session\_cnt（访问来源分布）、access\_staytime\_info（访问时长分布）、access\_depth\_info（访问深度的分布 ） |
| item\_list | [objarray](#Res__list<Array>__item_list<Array>) | 分布数据列表 |

**Res.list(Array).item_listObject Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| key | number | 场景 id，定义在各个 index 下不同，具体参见下方表格 |
| value | number | 该场景 id 访问 pv |

**4. 注意事项**

| 值 | 说明 |
| --- | --- |
| access\_source\_session\_cnt | 访问来源分布 |
| access\_staytime\_info | 访问时长分布 |
| access\_depth\_info | 访问深度的分布 |

**4. 注意事项**

| key | 访问来源 | 对应场景值 |
| --- | --- | --- |
| 1 | 小程序历史列表 | 1001 1002 1004 |
| 2 | 搜索 | 1005 1006 1027 1042 1053 1106 1108 1132 |
| 3 | 会话 | 1007 1008 1044 1093 1094 1096 |
| 4 | 扫一扫二维码 | 1011 1025 1047 1105 1124 1150 |
| 5 | 公众号主页 | 1020 |
| 6 | 聊天顶部 | 1022 |
| 7 | 系统桌面 | 1023 1113 1114 1117 |
| 8 | 小程序主页 | 1024 1135 |
| 9 | 附近的小程序 | 1026 1033 1068 |
| 11 | 模板消息 | 1014 1043 1107 1162 |
| 12 | 客服消息 | 1021 |
| 13 | 公众号菜单 | 1035 1102 1130 |
| 14 | APP分享 | 1036 |
| 15 | 支付完成页 | 1034 1060 1072 1097 1109 1137 1149 |
| 16 | 长按识别二维码 | 1012 1048 1050 1125 |
| 17 | 相册选取二维码 | 1013 1049 1126 |
| 18 | 公众号文章 | 1058 1091 |
| 19 | 钱包 | 1019 1057 1061 1066 1070 1071 |
| 20 | 卡包 | 1028 1128 1148 |
| 21 | 小程序内卡券 | 1029 1062 |
| 22 | 其他小程序 | 1037 |
| 23 | 其他小程序返回 | 1038 |
| 24 | 卡券适用门店列表 | 1052 |
| 25 | 搜索框快捷入口 | 1054 |
| 26 | 小程序客服消息 | 1073 1081 |
| 27 | 公众号下发 | 1074 1076 1082 1152 |
| 28 | 系统会话菜单 | 1080 1083 1088 |
| 29 | 任务栏-最近使用 | 1089 |
| 30 | 长按小程序菜单圆点 | 1085 1090 1147 |
| 31 | 连wifi成功页 | 1064 1078 |
| 32 | 城市服务 | 1092 |
| 33 | 微信广告 | 1045 1046 1067 1084 1095 |
| 34 | 其他移动应用 | 1065 1069 1111 1140 |
| 35 | 发现入口-我的小程序 | 1003 1103 |
| 36 | 任务栏-我的小程序 | 1104 |
| 37 | 微信圈子 | 1138 1163 |
| 38 | 手机充值 | 1098 |
| 39 | H5 | 1018 1055 |
| 40 | 插件 | 1040 1041 1099 |
| 41 | 大家在用 | 1118 1145 |
| 42 | 发现页 | 1112 1141 1142 1143 |
| 43 | 浮窗 | 1131 |
| 44 | 附近的人 | 1075 1134 |
| 45 | 看一看 | 1115 |
| 46 | 朋友圈 | 1009 1110 1154 1155 |
| 47 | 企业微信 | 1119 1120 1121 1122 1123 1156 |
| 48 | 视频 | 1136 1144 |
| 49 | 收藏 | 1010 |
| 50 | 微信红包 | 1100 |
| 51 | 微信游戏中心 | 1079 1127 |
| 52 | 摇一摇 | 1039 1077 |
| 53 | 公众号导购消息 | 1157 |
| 54 | 识物 | 1153 |
| 55 | 小程序订单 | 1151 |
| 56 | 小程序直播 | 1161 |
| 57 | 群工具 | 1158 1159 1160 |
| 10 | 其他 | 除上述外其余场景值 |

**4. 注意事项**

| key | 访问时长 |
| --- | --- |
| 1 | 0-2s |
| 2 | 3-5s |
| 3 | 6-10s |
| 4 | 11-20s |
| 5 | 20-30s |
| 6 | 30-50s |
| 7 | 50-100s |
| 8 | >100s |

**4. 注意事项**

| key | 访问时长 |
| --- | --- |
| 1 | 1 页 |
| 2 | 2 页 |
| 3 | 3 页 |
| 4 | 4 页 |
| 5 | 5 页 |
| 6 | 6-10 页 |
| 7 | >10 页 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

**7. 适用范围**

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

---

<!-- pages: 11 -->
