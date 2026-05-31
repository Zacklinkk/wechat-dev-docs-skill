# 小程序服务端 API 结构化参考 — API/livebroadcast

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 创建直播间

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_createroom.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 直播间名字，最短3个汉字，最长17个汉字，1个汉字相当于2个字符 |
| coverImg | string | 是 | 背景图，填入mediaID（mediaID获取后，三天内有效）；图片mediaID的获取，请参考[新增临时素材](../../kf-mgnt/kf-message/api_uploadtempmedia)；直播间背景图，图片规则：建议像素1080\*1920，大小不超过2M |
| startTime | number | 是 | 直播计划开始时间（开播时间需要在当前时间的10分钟后 并且 开始时间不能在 6 个月后） |
| endTime | number | 是 | 直播计划结束时间（开播时间和结束时间间隔不得短于30分钟，不得超过24小时） |
| anchorName | string | 是 | 主播昵称，最短2个汉字，最长15个汉字，1个汉字相当于2个字符 |
| anchorWechat | string | 是 | 主播微信号，如果未实名认证，需要先前往[小程序直播](https://res.wx.qq.com/op_res/9rSix1dhHfK4rR049JL0PHJ7TpOvkuZ3mE0z7Ou_Etvjf-w1J_jVX0rZqeStLfwh)小程序进行实名验证 |
| subAnchorWechat | string | 否 | 主播副号微信号，如果未实名认证，需要先前往[小程序直播](https://res.wx.qq.com/op_res/9rSix1dhHfK4rR049JL0PHJ7TpOvkuZ3mE0z7Ou_Etvjf-w1J_jVX0rZqeStLfwh)小程序进行实名验证 |
| createrWechat | string | 否 | 创建者微信号，不传入则此直播间所有成员可见。传入则此房间仅创建者、管理员、超管、直播间主播可见 |
| shareImg | string | 是 | 分享图，填入mediaID（mediaID获取后，三天内有效）；图片mediaID的获取，请参考[新增临时素材](../../kf-mgnt/kf-message/api_uploadtempmedia)；直播间分享图，图片规则：建议像素800\*640，大小不超过1M； |
| feedsImg | string | 是 | 购物直播频道封面图，填入mediaID（mediaID获取后，三天内有效）；图片mediaID的获取，请参考[新增临时素材](../../kf-mgnt/kf-message/api_uploadtempmedia)；购物直播频道封面图，图片规则：建议像素800\*800，大小不超过100KB； |
| isFeedsPublic | number | 否 | 是否开启官方收录 【1: 开启，0：关闭】，默认开启收录 |
| type | number | 是 | 直播间类型 【1: 推流，0：手机直播】 |
| closeLike | number | 是 | 是否关闭点赞 【0：开启，1：关闭】（若关闭，观众端将隐藏点赞按钮，直播开始后不允许开启） |
| closeGoods | number | 是 | 是否关闭货架 【0：开启，1：关闭】（若关闭，观众端将隐藏商品货架，直播开始后不允许开启） |
| closeComment | number | 是 | 是否关闭评论 【0：开启，1：关闭】（若关闭，观众端将隐藏评论入口，直播开始后不允许开启） |
| closeReplay | number | 否 | 是否关闭回放 【0：开启，1：关闭】默认关闭回放（直播开始后允许开启） |
| closeShare | number | 否 | 是否关闭分享 【0：开启，1：关闭】默认开启分享（直播开始后不允许修改） |
| closeKf | number | 否 | 是否关闭客服 【0：开启，1：关闭】 默认关闭客服（直播开始后允许开启） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| roomId | number | 房间ID |
| qrcode\_url | string | [小程序直播](https://res.wx.qq.com/op_res/9rSix1dhHfK4rR049JL0PHJ7TpOvkuZ3mE0z7Ou_Etvjf-w1J_jVX0rZqeStLfwh)小程序码 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 1007 | get no data | 未获取到数据 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 200002 | 参数错误 |  |
| 300002 | 名称长度不符合规则 |  |
| 300028 | 房间名称违规 |  |
| 300031 | 直播间封面图不合规 |  |
| 300032 | 直播间分享图违规 |  |
| 300034 | 主播微信昵称长度不符合要求 |  |
| 300036 | 主播微信号未实名认证 |  |
| 300037 | 购物直播频道封面图不合规 |  |
| 300038 | 未在小程序管理后台配置客服 |  |
| 300039 | 主播副号微信号不合法 |  |
| 300040 | 名称含有非限定字符（含有特殊字符） |  |
| 300041 | 创建者微信号不合法 |  |

---

### 获取直播间列表和回放

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_getliveinfo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 起始拉取视频，0表示从第一个视频片段开始拉取 |
| limit | number | 是 | 每次拉取的数量，建议100以内 |
| action | string | 否 | 只能填"get\_replay"，表示获取回放。 |
| room\_id | number | 否 | 当action有值时该字段必填，直播间ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| room\_info | [objarray](#Res__room_info<Array>) | action="get\_replay"不返回。 |
| total | number | 拉取房间总数 |
| live\_replay | [objarray](#Res__live_replay<Array>) | action="get\_replay"才返回。 |

**Res.room_info(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| name | string | 直播间名称 |
| cover\_img | string | 直播间背景图链接 |
| start\_time | number | 直播间开始时间，列表按照start\_time降序排列 |
| end\_time | number | 直播计划结束时间 |
| anchor\_name | string | 主播名 |
| roomid | number | 直播间ID |
| goods | [objarray](#Res__room_info<Array>__goods<Array>) | 商品 |
| live\_status | number | 直播间状态。101：直播中，102：未开始，103已结束，104禁播，105：暂停，106：异常，107：已过期 |
| share\_img | string | 直播间分享图链接 |
| live\_type | number | 直播类型，1 推流 0 手机直播 |
| close\_like | number | 是否关闭点赞 【0：开启，1：关闭】（若关闭，观众端将隐藏点赞按钮，直播开始后不允许开启） |
| close\_goods | number | 是否关闭货架 【0：开启，1：关闭】（若关闭，观众端将隐藏商品货架，直播开始后不允许开启） |
| close\_comment | number | 是否关闭评论 【0：开启，1：关闭】（若关闭，观众端将隐藏评论入口，直播开始后不允许开启） |
| close\_kf | number | 是否关闭客服 【0：开启，1：关闭】 默认关闭客服（直播开始后允许开启） |
| close\_replay | number | 是否关闭回放 【0：开启，1：关闭】默认关闭回放（直播开始后允许开启） |
| is\_feeds\_public | number | 是否开启官方收录，1 开启，0 关闭 |
| creater\_openid | string | 创建者openid |
| feeds\_img | string | 官方收录封面 |

**Res.live_replay(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| create\_time | string | 回放视频创建时间 |
| expire\_time | string | 回放视频url过期时间 |
| media\_url | string | 回放视频链接 |

**Res.room_info(Array).goodsObject Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| name | string | 商品名称 |
| cover\_img | string | 商品封面图链接 |
| url | string | 商品小程序路径 |
| price | number | 商品价格（分） |
| price2 | number | 商品价格，使用方式看price\_type |
| price\_type | number | 价格类型，1：一口价（只需要传入price，price2不传） 2：价格区间（price字段为左边界，price2字段为右边界，price和price2必传） 3：显示折扣价（price字段为原价，price2字段为现价， price和price2必传） |
| goods\_id | number | 商品id |
| third\_party\_appid | string | 第三方商品appid ,当前小程序商品则为空 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 删除直播间

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_deleteroom.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 房间ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 200002 | 参数错误 |  |
| 300022 | 此房间号不存在 |  |
| 300023 | 房间状态 拦截（当前房间状态不允许此操作） |  |

---

### 导入商品

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_importgoods.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | numarray | 是 | 数组列表，可传入多个，里面填写 商品 ID |
| roomId | number | 是 | 房间ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 200002 |  | 入参错误 |
| 300022 |  | 此房间号不存在 |
| 300023 |  | 房间状态 拦截（当前房间状态不允许此操作） |
| 300024 |  | 商品不存在 |
| 300025 |  | 商品审核未通过 |
| 300027 |  | 导入商品失败 |
| 300033 |  | 添加商品超过直播间上限 |

---

### 编辑直播间

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_editroom.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 直播间id |
| name | string | 是 | 直播间名字，最短3个汉字，最长17个汉字，1个汉字相当于2个字符 |
| coverImg | string | 是 | 背景图，填入mediaID（mediaID获取后，三天内有效）；图片mediaID的获取，请参考[新增临时素材](../../kf-mgnt/kf-message/api_uploadtempmedia)；直播间背景图，图片规则：建议像素1080\*1920，大小不超过2M |
| startTime | number | 是 | 直播计划开始时间（开播时间需要在当前时间的10分钟后 并且 开始时间不能在 6 个月后） |
| endTime | number | 是 | 直播计划结束时间（开播时间和结束时间间隔不得短于30分钟，不得超过24小时） |
| anchorName | string | 是 | 主播昵称，最短2个汉字，最长15个汉字，1个汉字相当于2个字符 |
| anchorWechat | string | 是 | 主播微信号，如果未实名认证，需要先前往[小程序直播](https://res.wx.qq.com/op_res/9rSix1dhHfK4rR049JL0PHJ7TpOvkuZ3mE0z7Ou_Etvjf-w1J_jVX0rZqeStLfwh)小程序进行实名验证 |
| shareImg | string | 是 | 分享图，填入mediaID（mediaID获取后，三天内有效）；图片mediaID的获取，请参考[新增临时素材](../../kf-mgnt/kf-message/api_uploadtempmedia)；直播间分享图，图片规则：建议像素800\*640，大小不超过1M； |
| feedsImg | string | 是 | 购物直播频道封面图，填入mediaID（mediaID获取后，三天内有效）；图片mediaID的获取，请参考[新增临时素材](../../kf-mgnt/kf-message/api_uploadtempmedia)；购物直播频道封面图，图片规则：建议像素800\*800，大小不超过100KB； |
| isFeedsPublic | number | 否 | 是否开启官方收录 【1: 开启，0：关闭】，默认开启收录 |
| closeLike | number | 是 | 是否关闭点赞 【0：开启，1：关闭】（若关闭，观众端将隐藏点赞按钮，直播开始后不允许开启） |
| closeGoods | number | 是 | 是否关闭货架 【0：开启，1：关闭】（若关闭，观众端将隐藏商品货架，直播开始后不允许开启） |
| closeComment | number | 是 | 是否关闭评论 【0：开启，1：关闭】（若关闭，观众端将隐藏评论入口，直播开始后不允许开启） |
| closeReplay | number | 否 | 是否关闭回放 【0：开启，1：关闭】默认关闭回放（直播开始后允许开启） |
| closeShare | number | 否 | 是否关闭分享 【0：开启，1：关闭】默认开启分享（直播开始后不允许修改） |
| closeKf | number | 否 | 是否关闭客服 【0：开启，1：关闭】 默认关闭客服（直播开始后允许开启） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 200002 | 参数错误 |  |
| 300002 | 名称长度不符合规则 |  |
| 300022 | 此房间号不存在 |  |
| 300023 | 房间状态 拦截（当前房间状态不允许此操作） |  |
| 300030 | 主播微信号不合法 |  |
| 300031 | 直播间封面图不合规 |  |
| 300032 | 直播间分享图违规 |  |
| 300037 | 购物直播频道封面图不合规 |  |

---

### 获取直播间推流地址

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_getpushurl.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roomId | number | 是 | 房间ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| pushAddr | string | 推流地址 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 43001 | require GET method | 需要 GET 请求 |
| 300022 | 此房间号不存在 |  |
| 300023 | 房间状态 拦截（当前房间状态不允许此操作） |  |

---

### 获取直播间分享二维码

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_getsharedcode.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roomId | number | 是 | 房间ID |
| params | string | 否 | 自定义参数 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | 返回码 |
| cdnUrl | string | 分享二维码cdn url |
| pagePath | string | 分享路径 |
| posterUrl | string | 分享海报 url |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 1001 | 请求参数非法 |  |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 300022 | 此房间号不存在 |  |
| 300023 | 房间状态 拦截（当前房间状态不允许此操作） |  |

---

### 获取主播副号

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_getsubanchor.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roomId | number | 是 | 房间ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |
| username | string | 主播微信号 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

---

### 修改主播副号

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_modifysubanchor.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roomId | number | 是 | 房间ID |
| username | string | 是 | 微信号 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 500002 | 副号未实名 |  |
| 500004 | 不能设置重复的副号 |  |

---

### 删除主播副号

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_deletesubanchor.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roomId | number | 是 | 房间ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

---

### 添加主播副号

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_addsubanchor.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roomId | number | 是 | 房间ID |
| username | string | 是 | 用户微信号 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 500004 | 不能设置重复的副号 |  |
| 500005 | 副号不能和主号重复 |  |

---

### 删除直播间商品

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_deletedoods.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roomId | number | 是 | 房间ID |
| goodsId | number | 是 | 商品ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 300022 | 此房间号不存在 |  |
| 300047 | 已有商品正在推送，请稍后再试 |  |

---

### 推送商品

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_pushgoods.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roomId | number | 是 | 房间ID |
| goodsId | number | 是 | 商品ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 300023 | 房间状态 拦截（当前房间状态不允许此操作） |  |
| 300024 | 商品不存在 |  |
| 300047 | 已有商品正在推送，请稍后再试 |  |
| 300052 | 已下架的商品无法推送 |  |
| 300053 | 直播间未添加此商品 |  |

---

### 上下架商品

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_salegoods.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roomId | number | 是 | 房间ID |
| goodsId | number | 是 | 商品ID |
| onSale | number | 是 | 上下架 【0：下架，1：上架】 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 300022 | 此房间号不存在 |  |
| 300024 | 商品不存在 |  |
| 300048 | 拉取商品列表失败 |  |
| 300049 | 商品推送过程中不允许上下架 |  |

---

### 直播间商品排序

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_sortgoods.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roomId | number | 是 | 房间ID |
| goods | [objarray](#Body__goods<Array>) | 是 | 商品ID列表 |

**Body.goods(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| goodsId | number | 是 | 商品id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 300023 | 房间状态 拦截（当前房间状态不允许此操作） |  |
| 300048 | 拉取商品列表失败 |  |

---

### 修改直播间小助手

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_modifyassistant.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roomId | number | 是 | 房间ID |
| username | string | 是 | 用户微信号 |
| nickname | string | 是 | 用户微信昵称 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

---

### 查询直播间小助手

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_getassistantlist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roomId | number | 是 | 房间ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| list | [objarray](#Res__list<Array>) | 小助手列表 |
| count | number | 小助手个数 |
| maxCount | number | 小助手最大个数 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| timestamp | number | 修改时间 |
| headimg | string | 头像 |
| nickname | string | 昵称 |
| alias | string | 微信号 |
| openid | string | openid |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

---

### 删除直播间小助手

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_removeassistant.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roomId | number | 是 | 房间ID |
| username | string | 是 | 用户微信号 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 添加管理直播间小助手

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_addveassistant.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roomId | number | 是 | 房间ID |
| users | [objarray](#Body__users<Array>) | 是 | 用户数组 |

**Body.users(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| username | string | 是 | 用户微信号 |
| nickname | string | 是 | 用户昵称 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

---

### 禁言管理

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_updatecomment.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 房间ID |
| banComment | number | 是 | 1-禁言，0-取消禁言 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 300022 | 此房间号不存在 |  |
| 300023 | 房间状态 拦截（当前房间状态不允许此操作） |  |

---

### 官方收录管理

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_updatefeedpublic.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roomId | number | 是 | 房间ID |
| isFeedsPublic | number | 是 | 是否开启官方收录 【1: 开启，0：关闭】 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

---

### 客服功能管理

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_updatekf.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roomId | number | 是 | 房间ID |
| closeKf | number | 是 | 是否关闭客服 【0：开启，1：关闭】 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

---

### 回放功能管理

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_updatereplay.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roomId | number | 是 | 房间ID |
| closeReplay | number | 是 | 是否关闭回放 【0：开启，1：关闭】 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 300023 | 房间状态 拦截（当前房间状态不允许此操作） |  |

---

### 下载商品讲解视频

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_downloadgoodsvideo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roomId | number | 是 | 房间ID |
| goodsId | number | 是 | 商品ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| url | string | 讲解链接 |
| errcode | number | [错误码](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 41001 | access\_token missing | 缺少 access\_token 参数 |
| 300023 | 房间状态 拦截（当前房间状态不允许此操作） |  |
| 300024 | 商品不存在 |  |
| 300044 | 商品没有讲解视频 |  |
| 300045 | 讲解视频未生成 |  |
| 300048 | 拉取商品列表失败 |  |

---

### 直播挂件设置全局KEY

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_setdefault_goodskey.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| goodsKey | array | 是 | 商品KEY |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

---

### 直播挂件获取全局KEY

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_getdefault_goodskey.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |
| vendorGoodsKey | array | 全局KEY |

---

### 添加并提审商品

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/commodity-management/api_addgoods.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| goodsInfo | [object](#Body__goodsInfo) | 是 | 商品信息 |

**Body.goodsInfo Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| coverImgUrl | string | 是 | 填入mediaID（mediaID获取后，三天内有效）；图片mediaID的获取，请参考[新增临时素材](../../kf-mgnt/kf-message/api_uploadtempmedia)；图片规则：图片尺寸最大300像素\*300像素； |
| name | string | 是 | 商品名称，最长14个汉字，1个汉字相当于2个字符 |
| priceType | number | 是 | 价格类型，1：一口价（只需要传入price，price2不传） 2：价格区间（price字段为左边界，price2字段为右边界，price和price2必传） 3：显示折扣价（price字段为原价，price2字段为现价， price和price2必传） |
| price | number | 是 | 数字，最多保留两位小数，单位元 |
| price2 | number | 否 | 数字，最多保留两位小数，单位元 |
| url | string | 是 | 商品详情页的小程序路径，路径参数存在 url 的，该参数的值需要进行 encode 处理再填入 |
| thirdPartyAppid | string | 否 | 当商品为第三方小程序的商品则填写为对应第三方小程序的appid，自身小程序商品则填空 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| goodsId | number | 商品ID |
| auditId | number | 审核单ID |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 200002 | 参数错误 |  |
| 300002 | 名称长度不符合规则 |  |
| 300003 | 价格输入不合规（如现价比原价大、传入价格非数字等） |  |
| 300004 | 商品名称存在违规违法内容 |  |
| 300006 | 图片上传失败（如：mediaID过期） |  |
| 300007 | 线上小程序版本不存在该链接 |  |
| 300018 | 商品图片尺寸过大 |  |
| 300021 | 商品添加成功，审核失败 |  |

---

### 重新提交商品审核

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/commodity-management/api_resubmitaudit.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| goodsId | number | 是 | 商品ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| auditId | number | 审核单ID |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 300010 | 商品审核状态不对（如商品审核中） |  |
| 300011 | 操作非法（API不允许操作非API创建的商品） |  |

---

### 获取商品的信息与审核状态

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/commodity-management/api_getgoodsauditinfo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| goods\_ids | numarray | 是 | 商品ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| goods | [objarray](#Res__goods<Array>) | 商品列表 |
| total | number | 商品个数 |

**Res.goods(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| goods\_id | string | 商品ID |
| name | string | 商品名称，最长14个汉字，1个汉字相当于2个字符 |
| cover\_img\_url | string | 填入mediaID（mediaID获取后，三天内有效）；图片mediaID的获取，请参考[新增临时素材](../../kf-mgnt/kf-message/api_uploadtempmedia)；图片规则：图片尺寸最大300像素\*300像素； |
| url | string | 商品详情页的小程序路径，路径参数存在 url 的，该参数的值需要进行 encode 处理再填入 |
| priceType | number | 价格类型，1：一口价（只需要传入price，price2不传） 2：价格区间（price字段为左边界，price2字段为右边界，price和price2必传） 3：显示折扣价（price字段为原价，price2字段为现价， price和price2必传） |
| price | number | 数字，最多保留两位小数，单位元 |
| price2 | number | 数字，最多保留两位小数，单位元 |
| audit\_status | string | 审核状态（0：未审核，1：审核中，2:审核通过，3审核失败） |
| third\_party\_tag | number | 1、2：表示是为 API 添加商品，否则是直播控制台添加的商品 |
| thirdPartyAppid | string | 当商品为第三方小程序的商品则填写为对应第三方小程序的appid，自身小程序商品则填空 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 撤回商品审核

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/commodity-management/api_resetaudit.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| goodsId | number | 是 | 商品ID |
| auditId | number | 是 | 审核单ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 300009 | 商品审核撤回失败 |  |
| 300017 | 商品未提审 |  |

---

### 更新商品

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/commodity-management/api_updategoodsinfo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| goodsInfo | [object](#Body__goodsInfo) | 是 | 商品信息 |

**Body.goodsInfo Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| coverImgUrl | string | 是 | 填入mediaID（mediaID获取后，三天内有效）；图片mediaID的获取，请参考[新增临时素材](../../kf-mgnt/kf-message/api_uploadtempmedia)；图片规则：图片尺寸最大300像素\*300像素； |
| name | string | 是 | 商品名称，最长14个汉字，1个汉字相当于2个字符 |
| priceType | number | 是 | 价格类型，1：一口价（只需要传入price，price2不传） 2：价格区间（price字段为左边界，price2字段为右边界，price和price2必传） 3：显示折扣价（price字段为原价，price2字段为现价， price和price2必传） |
| price | number | 是 | 数字，最多保留两位小数，单位元 |
| price2 | number | 否 | 数字，最多保留两位小数，单位元 |
| url | string | 是 | 商品详情页的小程序路径，路径参数存在 url 的，该参数的值需要进行 encode 处理再填入 |
| thirdPartyAppid | string | 否 | 当商品为第三方小程序的商品则填写为对应第三方小程序的appid，自身小程序商品则填空 |
| goodsId | number | 是 | 商品ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 200002 | 参数错误 |  |
| 300002 | 名称长度不符合规则 |  |
| 300003 | 价格输入不合规（如现价比原价大、传入价格非数字等） |  |
| 300006 | 图片上传失败（如：mediaID过期） |  |
| 300007 | 线上小程序版本不存在该链接 |  |
| 300010 | 商品审核状态不对（如商品审核中） |  |
| 300011 | 操作非法（API不允许操作非API创建的商品） |  |

---

### 获取商品列表

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/commodity-management/api_getgoodsinfo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| offset | number | 是 | - | 分页条数起点 |
| limit | number | 否 | - | 分页大小，默认30，不超过100 |
| status | number | 是 | - | 商品状态，0：未审核。1：审核中，2：审核通过，3：审核驳回 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| goods | [objarray](#Res__goods<Array>) | 商品列表 |
| total | number | 商品个数 |

**Res.goods(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| goodsId | string | 商品ID |
| name | string | 商品名称，最长14个汉字，1个汉字相当于2个字符 |
| coverImgUrl | string | 填入mediaID（mediaID获取后，三天内有效）；图片mediaID的获取，请参考[新增临时素材](../../kf-mgnt/kf-message/api_uploadtempmedia)；图片规则：图片尺寸最大300像素\*300像素； |
| url | string | 商品详情页的小程序路径，路径参数存在 url 的，该参数的值需要进行 encode 处理再填入 |
| priceType | number | 价格类型，1：一口价（只需要传入price，price2不传） 2：价格区间（price字段为左边界，price2字段为右边界，price和price2必传） 3：显示折扣价（price字段为原价，price2字段为现价， price和price2必传） |
| price | number | 数字，最多保留两位小数，单位元 |
| price2 | number | 数字，最多保留两位小数，单位元 |
| third\_party\_tag | number | 1、2：表示是为 API 添加商品，否则是直播控制台添加的商品 |
| thirdPartyAppid | string | 当商品为第三方小程序的商品则填写为对应第三方小程序的appid，自身小程序商品则填空 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 200002 | 参数错误 |  |

---

### 删除商品

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/commodity-management/api_deletegoodsinfo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| goodsId | number | 是 | 商品ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

---

### 设置成员角色

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/role-management/api_getrolelistdw.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| username | string | 是 | 用户的微信号 |
| role | number | 是 | 设置用户的角色 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| codeurl | string | 如果主播未实名认证，需要先前往“[小程序直播](https://res.wx.qq.com/op_res/9rSix1dhHfK4rR049JL0PHJ7TpOvkuZ3mE0z7Ou_Etvjf-w1J_jVX0rZqeStLfwh)”小程序进行实名验证 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 200002 | 参数错误 |  |
| 400001 | 微信号不合规 |  |
| 400002 | 微信号需要实名认证，仅设置主播角色时可能出现 |  |
| 400003 | 添加角色达到上限（管理员10个，运营者500个，主播500个） |  |
| 400004 | 重复添加角色 |  |

---

### 移除成员角色

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/role-management/api_deleterole.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| username | string | 是 | 用户的微信号 |
| role | number | 是 | 删除用户的角色 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 2003 |  |  |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 200002 | 参数错误 |  |
| 400001 | 微信号不合规 |  |
| 400005 | 主播角色删除失败，该主播存在未开播的直播间 |  |

---

### 查询成员列表

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/role-management/api_getrolelist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| offset | number | 否 | - | 起始偏移量, 默认0 |
| limit | number | 否 | - | 查询个数，最大30，默认10 |
| keyword | string | 否 | - | 搜索的微信号或昵称，不传则返回全部 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| total | number | 总个数 |
| list | [objarray](#Res__list<Array>) | 角色列表 |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| headingimg | string | 微信用户头像url |
| nickname | string | 微信用户昵称 |
| openid | string | openid |
| roleList | numarray | 具有的身份，[0-超级管理员，1-管理员，2-主播，3-运营者] |
| updateTimestamp | string | 更新时间 |
| username | string | 微信号 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 发送直播开始事件

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/subscribe-management/api_pushmessage.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| room\_id | number | 是 | 直播开始事件的房间ID |
| user\_openid | array | 是 | 接收该群发开播事件的订阅用户OpenId列表 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| message\_id | string | 此次群发消息的标识ID，用于对应【长期订阅群发结果回调】的message\_id |
| errcode | number | 接口返回码，0表示成功，非0则失败。若errcode=0仅表明触发接口成功，最终群发结果请看【长期订阅群发结果回调】 |
| errmsg | string | 接口返回提示信息 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 9410005 | 当日另外一个房间已推送过 |  |
| 9410006 | 推送的直播间非直播中状态 |  |

---

### 获取长期订阅用户

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/subscribe-management/api_getfollowers.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| limit | number | 否 | 获取长期订阅用户的个数限制，默认200，最大2000 |
| page\_break | number | 否 | 翻页标记，获取第一页时不带，第二页开始需带上上一页返回结果中的page\_break |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| followers | array | 长期订阅用户列表 |
| openid | array | 长期订阅用户OpenId |
| subscribe\_time | timestamp | 长期订阅用户订阅时间 |
| room\_id | number | 用户订阅时所处房间 |
| room\_status | number | 用户订阅时房间状态 |
| page\_break | number | 翻页标记，获取下一页时带上该值 |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

<!-- pages: 38 -->
