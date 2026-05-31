# 小程序服务端 API 结构化参考 — API/transaction-guarantee

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 获取小程序交易体验分违规记录

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/basic/api_getpenaltylist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 获取从第offset条开始的limit条记录（序号从 0 开始），最大不超过总记录数 |
| limit | number | 是 | 获取从第offset条开始的limit条记录（序号从 0 开始），最大不超过 100 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| appealList | [objarray](#Res__appealList<Array>) | 记录列表 |
| currentScore | number | 当前小程序的交易体验分 |
| totalNum | number | 当前小程序的总扣分记录数 |

**Res.appealList(Array) Object Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| illegalOrderId | number | 扣分记录ID | - |
| complaintOrderId | number | 投诉单ID | - |
| illegalWording | string | 违规行为 | - |
| status | number | 扣分记录状态 | [枚举值](#Enum_Res__appealList<Array>__status) |
| minusScore | number | 扣除分数 | - |
| orderId | number | 订单号 | - |
| illegalTime | number | 扣分记录创建时间 | - |
| updateTime | number | 更新时间 | - |

**Res.appealList(Array).status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 2 | 扣分审批通过 |
| 4 | 申诉中 |
| 5 | 申述驳回 |
| 6 | 申诉成功 |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 20002 | 参数非法 |
| 200002 | 参数错误 |

---

### 获取交易保障标状态

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/basic/api_getguaranteestatus.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| isActived | boolean | 是否激活交易保障标 |
| msg | string | 保障标状态相关信息 |
| reasons | array | 未能开通保障标的原因 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 200002 | 参数错误 |

---

### 查询评价列表

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/comment/api_getccommentlist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| startTime | string | 是 | 查询时间段的开始时间 | - |
| endTime | string | 是 | 查询时间段的结束时间 | - |
| filterType | number | 否 | 过滤的数据类型 | [枚举值](#Enum_Body__filterType) |
| offset | number | 否 | 查询的偏移数（从offset开始计数拉取)，默认值为 0 代表首页拉取 | - |
| limit | number | 否 | 查询每页中的数量，默认值为 8 | - |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | string | [错误码](#apierrcode) |
| offset | number | 查询的偏移数（从offset开始计数拉取) |
| total | number | 评价总数 |
| commentList | [objarray](#Res__commentList<Array>) | 评价的列表 |

**Res.commentList(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| commentId | string | 评价id |
| amount | number | 金额,单位是分 |
| orderId | string | 订单id |
| createTime | string | 创建时间，单位是秒 |
| payTime | string | 支付时间，单位是秒 |
| wxPayId | string | 微信支付交易单号，一般以420开头，是微信支付接口文档中的transaction\_id |
| orderInfo | [object](#Res__commentList<Array>__orderInfo) | 商家订单信息 |
| userInfo | [object](#Res__commentList<Array>__userInfo) | 评价用户信息 |
| bizInfo | [object](#Res__commentList<Array>__bizInfo) | 商家小程序信息 |
| score | number | 评价分数（每100分对应1星） |
| content | [object](#Res__commentList<Array>__content) | 评价内容 |
| extInfo | [object](#Res__commentList<Array>__extInfo) | 评价额外信息 |
| productInfo | [object](#Res__commentList<Array>__productInfo) | 评价商品信息 |

**Res.commentList(Array).orderInfo Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| busiOrderId | string | 商户单号：商户系统内部订单号，只能是数字、大小写字母\_-\*且在同一个商户号下唯一；是微信支付接口文档中的 out\_trade\_no |

**Res.commentList(Array).userInfo Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| openid | string | 评价用户openid |
| headImg | string | 评价用户的头像 |
| nickName | string | 评价用户的昵称 |

**Res.commentList(Array).bizInfo Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| appid | string | 商家小程序的appid |
| headImg | string | 商家小程序的头像 |
| nickName | string | 商家小程序的昵称 |

**Res.commentList(Array).content Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| txt | string | 评价内容 |
| media | [objarray](#Res__commentList<Array>__content__media<Array>) | 评价的媒体文件，如图片、视频, 视频跟图片只能存在一种，不同时存在，如果是图片可以有多张图，如果是视频只会有一个视频 |

**Res.commentList(Array).content.mediaObject Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| img | string | 图片cdn |
| thumbImg | string | 缩略图cdn |
| video | string | 视频资源cdn（有img的时候没有video） |
| videoCover | string | 缩略图cdn（有img的时候没有videoCover） |
| videoDuration | number | 视频时长，单位秒（有img的时候没有videoDuration） |

**Res.commentList(Array).extInfo Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| isAlreadySendTmpl | boolean | 是否已发过「差评客服会话」 |

**Res.commentList(Array).productInfo Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| productList | [objarray](#Res__commentList<Array>__productInfo__productList<Array>) | 商品列表 |

**Res.commentList(Array).productInfo.productListObject Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| name | string | 商品名 |
| picUrl | string | 商品图片 |

**Body.filterType Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 全部差评，所有评价分数为1星、2星的评价 |
| 2 | 全部好评，所有评价分数为4星、5星的评价 |
| 3 | 差评待处理，所有未提交「和解挽回」的评价 |
| 4 | 开发者待回复，所有待开发者回复的评价 |
| 5 | 差评已改评 |
| 6 | 全部评价，所有好评、差评、中评（3星）部评价 |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -10403 | 无权限操作该评价/评论/回复 |
| -10008 | 服务异常 |
| -10007 | 无权限调用接口 |
| -10003 | 参数不匹配 |
| -10001 | 参数异常 |
| 10000 | 和解：不是差评/发送过模板消息；其它：参数异常 |

---

### 查询评论列表

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/comment/api_getcommentreplylist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| commentId | string | 是 | 评价的 id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| list | [object](#Res__list) | 评论（评论回复第一条内容） |

**Res.list Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| reply | [object](#Res__list__reply) | 评论 |
| commentReplyList | [objarray](#Res__list__commentReplyList<Array>) | 回复（评论回复第二条及之后的所有集合） |

**Res.list.reply Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| commentId | string | 评价id |
| replyId | string | 评论id |
| createTime | string | 创建时间，单位是秒 |
| updateTime | string | 更新时间，单位是秒 |
| replyContent | [object](#Res__list__reply__replyContent) | 回复 |
| replyObject | [object](#Res__list__reply__replyObject) | 评论的内容 |

**Res.list.reply.replyContent Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| content | string | 回复的内容 |

**Res.list.reply.replyObject Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| nickname | string | 用户的昵称 |
| imgUrl | string | 用户的头像 |

**Res.list.commentReplyList(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| commentId | string | 评价id |
| commentReplyId | string | 回复id |
| createTime | string | 评价创建时间，单位是秒 |
| updateTime | string | 更新时间，单位是秒 |
| commentReplyContent | [object](#Res__list__commentReplyList<Array>__commentReplyContent) | 回复 |
| commentReplyObject | [object](#Res__list__commentReplyList<Array>__commentReplyObject) | 评论的内容 |

**Res.list.commentReplyList(Array).commentReplyContent Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| content | string | 回复的内容 |

**Res.list.commentReplyList(Array).commentReplyObject Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| nickname | string | 用户的昵称 |
| imgUrl | string | 用户的头像 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -10403 | 无权限操作该评价/评论/回复 |
| -10008 | 服务异常 |
| -10007 | 无权限调用接口 |
| -10003 | 参数不匹配 |
| -10001 | 参数异常 |
| 10000 | 和解：不是差评/发送过模板消息；其它：参数异常 |

---

### 查询评价详情

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/comment/api_getcommentinfo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| commentId | string | 是 | 评价的 id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| info | [object](#Res__info) | 评价的信息 |
| processInfo | [object](#Res__processInfo) | 进度条的信息（只有差评才会有） |
| oldComment | [object](#Res__oldComment) | 旧评价的信息(只有改评的新评价才有) |

**Res.info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| content | [object](#Res__info__content) | 评价 |

**Res.processInfo Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| actionList | [objarray](#Res__processInfo__actionList<Array>) | 进度的具体状态,数组类型，从数组最后往前数有updateTime的就是当前状态 |
| commentId | string | 评价进度对应的评价id |

**Res.oldComment Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| commentId | string | 评价id |
| createTime | string | 创建时间，单位是秒 |
| score | number | 用户评价的打分，每100对应1分以及1颗星 |
| content | [object](#Res__oldComment__content) | 评论的内容 |

**Res.info.content Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| commentId | string | 评价id |
| amount | string | 金额,单位是分 |
| orderId | string | 订单id |
| createTime | string | 创建时间，单位是秒 |
| payTime | string | 支付时间，单位是秒 |
| orderInfo | [object](#Res__info__content__orderInfo) | 商家订单信息 |
| productInfo | [object](#Res__info__content__productInfo) | 评价商品信息 |
| wxPayId | string | 微信支付交易单号，一般以420开头，是微信支付接口文档中的transaction\_id |
| userInfo | [object](#Res__info__content__userInfo) | 评价用户信息 |
| bizInfo | [object](#Res__info__content__bizInfo) | 商家小程序信息 |
| score | string | 评价分数，每100分对应1星 |
| content | [object](#Res__info__content__content) | 评价内容 |

**Res.info.content.orderInfo Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| busiOrderId | string | 商户单号：商户系统内部订单号，只能是数字、大小写字母\_-\*且在同一个商户号下唯一；是微信支付接口文档中的 out\_trade\_no |

**Res.info.content.productInfo Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| productList | [objarray](#Res__info__content__productInfo__productList<Array>) | 商品列表 |

**Res.info.content.productInfo.productList(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| name | string | 商品名 |
| picUrl | string | 商品图片 |

**Res.info.content.userInfo Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| openid | string | 评价用户openid |
| headImg | string | 评价用户的头像 |
| nickName | string | 评价用户的昵称 |

**Res.info.content.bizInfo Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| appid | string | 商家小程序的appid |
| headImg | string | 商家小程序的头像 |
| nickName | string | 商家小程序的昵称 |

**Res.info.content.content Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| media | [objarray](#Res__info__content__content__media<Array>) | 评价的媒体文件，如图片、视频 |
| txt | string | 评价内容 |

**Res.info.content.content.media(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| img | string | 图片cdn |
| thumbImg | string | 缩略图cdn |
| video | string | 视频资源cdn（有img的时候没有video） |
| videoCover | string | 缩略图cdn（有img的时候没有videoCover） |
| videoDuration | number | 视频时长，单位秒（有img的时候没有videoDuration） |

**Res.processInfo.actionList(Array) Object Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| type | number | 进度的类型 | [枚举值](#Enum_Res__processInfo__actionList<Array>__type) |
| updateTime | number | 更新时间，processInfo.actionList里从后往前数第一个有更新时间的就是当前状态 | - |

**Res.oldComment.content Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| ext | string | 评价的文本内容 |
| media | [objarray](#Res__oldComment__content__media<Array>) | 评价的多媒体内容,跟上面提到的媒体结构一致 |

**Res.oldComment.content.media(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| img | string | 图片cdn |
| thumbImg | string | 缩略图cdn |
| video | string | 视频资源cdn（有img的时候没有video） |
| videoCover | string | 缩略图cdn（有img的时候没有videoCover） |
| videoDuration | number | 视频时长，单位秒（有img的时候没有videoDuration） |

**Res.processInfo.actionList(Array).type Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 发表差评 |
| 2 | 开发者处理 |
| 3 | 用户调研 |
| 4 | 用户改评 |

**7. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -10403 | 无权限操作该评价/评论/回复 |
| -10008 | 服务异常 |
| -10007 | 无权限调用接口 |
| -10003 | 参数不匹配 |
| -10001 | 参数异常 |
| 10000 | 和解：不是差评/发送过模板消息；其它：参数异常 |

---

### 创建评论

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/comment/api_addreply.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| commentId | string | 是 | 评价的 id |
| content | string | 是 | 评论的内容 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| success | boolean | 请求是否成功状态 |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -10403 | 无权限操作该评价/评论/回复 |
| -10008 | 服务异常 |
| -10007 | 无权限调用接口 |
| -10003 | 参数不匹配 |
| -10001 | 参数异常 |
| 10000 | 和解：不是差评/发送过模板消息；其它：参数异常 |

---

### 删除评论

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/comment/api_deletereply.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| commentId | string | 是 | 评价的 id |
| replyId | string | 是 | 评论的 id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| success | boolean | 请求是否成功状态 |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -10403 | 无权限操作该评价/评论/回复 |
| -10008 | 服务异常 |
| -10007 | 无权限调用接口 |
| -10003 | 参数不匹配 |
| -10001 | 参数异常 |
| 10000 | 和解：不是差评/发送过模板消息；其它：参数异常 |

---

### 创建回复

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/comment/api_addcommentreply.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| commentId | string | 是 | 评价的 id |
| replyId | string | 是 | 评论的 id |
| content | string | 是 | 回复评论的内容 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| success | boolean | 请求是否成功状态 |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -10403 | 无权限操作该评价/评论/回复 |
| -10008 | 服务异常 |
| -10007 | 无权限调用接口 |
| -10003 | 参数不匹配 |
| -10001 | 参数异常 |
| 10000 | 和解：不是差评/发送过模板消息；其它：参数异常 |

---

### 删除回复

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/comment/api_deletecommentreply.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| commentId | string | 是 | 评价的 id |
| replyId | string | 是 | 评论的 id |
| commentReplyId | string | 是 | 回复评论的 id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| success | boolean | 请求是否成功状态 |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -10403 | 无权限操作该评价/评论/回复 |
| -10008 | 服务异常 |
| -10007 | 无权限调用接口 |
| -10003 | 参数不匹配 |
| -10001 | 参数异常 |
| 10000 | 和解：不是差评/发送过模板消息；其它：参数异常 |

---

### 重置Api客服quota

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/comment/api_resetapikfquota.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| commentId | string | 是 | 评价的 id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| success | boolean | 请求是否成功状态 |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -10403 | 无权限操作该评价/评论/回复 |
| -10008 | 服务异常 |
| -10007 | 无权限调用接口 |
| -10003 | 参数不匹配 |
| -10001 | 参数异常 |
| 10000 | 和解：不是差评/发送过模板消息；其它：参数异常 |

---

### 确认和解

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/comment/api_confirmcompromise.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| commentId | string | 是 | 评价的 id |
| picList | array | 是 | 和解的图片mediaId集合,可参考[素材管理](https://developers.weixin.qq.com/doc/service/guide/product/asset) |
| content | string | 是 | 和解的文本内容 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| success | boolean | 请求是否成功状态 |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| -10403 | 无权限操作该评价/评论/回复 |
| -10008 | 服务异常 |
| -10007 | 无权限调用接口 |
| -10003 | 参数不匹配 |
| -10001 | 参数异常 |
| 10000 | 和解：不是差评/发送过模板消息；其它：参数异常 |

---

### 商家回应投诉

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/complaint/api_respondcomplaint.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | string | 是 | 回应的内容（图片数组mediaIdList跟内容content二选一） |
| complaintOrderId | number | 是 | 单号 |
| mediaIdList | array | 是 | 图片 id 列表，可参考[新增素材](../../kf-mgnt/kf-message/api_uploadtempmedia)（图片数组mediaIdList跟内容content二选一） |
| bussiHandle | number | 是 | 操作：1是同意和解，2是拒绝和解 |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number | 0 | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | 成功 |  |
| 1 | 单号不存在 |  |
| 309 | 状态不对（可能是已经转到下一个状态了） | 开发者自行校验投诉单状态 |
| 10001 | 参数异常，errmsg字段展示具体描述 |  |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 商家补充凭证

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/complaint/api_supplyproof.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | string | 是 | 回应的内容（图片数组mediaIdList跟内容content二选一） |
| complaintOrderId | number | 是 | 单号 |
| mediaIdList | array | 是 | 图片 id 列表，可参考这 [新增素材](../../kf-mgnt/kf-message/api_uploadtempmedia)（图片数组mediaIdList跟内容content二选一） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | 成功 |  |
| 1 | 单号不存在 |  |
| 309 | 状态不对（可能是已经转到下一个状态了） | 开发者自行校验投诉单状态 |
| 10001 | 参数异常，errmsg字段展示具体描述 |  |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 商家提交退款凭证

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/complaint/api_submitrefund.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | string | 是 | 回应的内容（图片数组mediaIdList跟内容content二选一） |
| complaintOrderId | number | 是 | 单号 |
| mediaIdList | array | 是 | 图片的id list 图片 id 列表，可参考[新增素材](../../kf-mgnt/kf-message/api_uploadtempmedia)（图片数组mediaIdList跟内容content二选一） |
| acceptReturn | number | 是 | 确认是否收货（退货状态下必填） |
| returnId | number | 是 | 退货单号，需要通过查询投诉单详情接口获取（退货状态下必填） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | 成功 |  |
| 1 | 单号不存在 |  |
| 309 | 状态不对（可能是已经转到下一个状态了） | 开发者自行校验投诉单状态 |
| 10001 | 参数异常，errmsg字段展示具体描述 |  |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 查询投诉单详情

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/complaint/api_getorderdetail.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| complaintOrderId | string | 是 | 订单id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| complaintOrder | [object](#Res__complaintOrder) | complaintOrder |
| item | [object](#Res__item) | 投诉进度 |
| returnBill | [object](#Res__returnBill) | returnBill |

**Res.complaintOrder Object Payload**

| 参数名 | 类型 | 示例 | 说明 | 枚举 |
| --- | --- | --- | --- | --- |
| complaintOrderId | string | - | 订单id | - |
| openid | string |  | 用户的openid | - |
| createTime | number |  | 投诉发起时间 | - |
| phoneNumber | number |  | 联系方式 | - |
| type | number |  | 投诉问题分类 | [枚举值](#Enum_Res__complaintOrder__type) |
| status | number | 101 | 投诉单状态 | [枚举值](#Enum_Res__complaintOrder__status) |
| customerMaterial | [object](#Res__complaintOrder__customerMaterial) |  | 投诉信息 | - |
| orderId | string |  | 微信支付订单号 | - |
| outTradeNo | string |  | 商家订单号 | - |
| productName | string |  | 商品名称 | - |
| payTime | number |  | 支付时间 | - |
| totalCost | string |  | 交易金额 | - |
| expireTime | number | - | 投诉单当前状态到期时间,0为不存在 | - |
| headImgUrl | string | - | 头像URL | - |
| nickName | string | - | 微信昵称 | - |
| appealState | number | - | 申诉状态 | [枚举值](#Enum_Res__complaintOrder__appealState) |

**Res.item Object Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| itemType | number | 投诉节点状态 | [枚举值](#Enum_Res__item__itemType) |
| time | number | 时间 | - |
| content | string | 内容文本 | - |
| mediaIdList | array | 图片cdn资源列表 | - |
| phoneNumber | number | 手机号 | - |
| blameResult | number | itemType 为（31， 32）时，判断是否经过退货的描述， 1对应文案为待用户退货中，0则对应文案为待上传处理凭证 | - |
| nickName | string | 操作者昵称 | - |
| appealItemType | number | 处于申诉阶段节点的申诉状态 | [枚举值](#Enum_Res__item__appealItemType) |

**Res.returnBill Object Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| returnId | string | 退货id | - |
| waybillId | string | 运单号 | - |
| deliveryName | string | 运力公司 | - |
| orderStatus | number | 运单状态 | [枚举值](#Enum_Res__returnBill__orderStatus) |

**Res.complaintOrder.customerMaterial Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| content | string | 投诉内容 |
| mediaIdList | array | 投诉内容图片cdn(出于安全性考虑，目前该图片url有过期时间，如需查看图片，需每次重新调用该接口获取，防止图片过期导致无法查看) |

**Res.complaintOrder.type Enum**

| 枚举值 | 描述 |
| --- | --- |
| 611 | 发货问题-未按约定时间发货 |
| 612 | 发货问题-商家拒绝发货 |
| 613 | 发货问题-少发/错发 |
| 614 | 发货问题-物流信息长时间不更新 |
| 621 | 客服问题-客服不回复 |
| 622 | 客服问题-客服辱骂/骚扰/恐吓 |
| 631 | 承诺未履行-赠品承诺未履行 |
| 632 | 承诺未履行-物流承诺未履行 |
| 633 | 承诺未履行-其他 |
| 641 | 商品问题-描述不符 |
| 642 | 商品问题-商品破损 |
| 643 | 商品问题-其他 |
| 650 | 收费异常问题-车辆没电或故障 |
| 651 | 收费异常问题-关锁成功仍计费 |
| 652 | 收费异常问题-扣费金额不对 |
| 653 | 收费异常问题-规范停车仍扣调度费 |
| 654 | 收费异常问题-其他 |
| 655 | 骑行卡问题-已购买骑行卡，仍扣费 |
| 656 | 骑行卡问题-骑行卡退款 |
| 657 | 押金/余额退还问题-押金退还 |
| 658 | 押金/余额退还问题-余额退还 |
| 659 | 客服问题-客服不回复 |
| 660 | 收费异常问题-充电宝未弹出，已扣费 |
| 661 | 收费异常问题-充电宝无法正常使用 |
| 662 | 收费异常问题-已归还，仍计费 |
| 663 | 收费异常问题-不认可计费时长 |
| 664 | 收费异常问题-其他 |
| 665 | 押金退还问题-押金退还异常 |
| 666 | 其他问题-客服不回复 |
| 667 | 其他问题-归还点少无法归还 |
| 668 | 其他问题-误操作购买，需消费 |
| 670 | 欺诈问题-虚假广告 |
| 671 | 欺诈问题-剧集数量与承诺不符 |
| 672 | 欺诈问题-付款金额与页面不符 |
| 673 | 欺诈问题-剧集内容与宣传不符 |
| 674 | 欺诈问题-营销活动问题 |
| 675 | 扣费问题-重复扣费 |
| 676 | 扣费问题-无理由扣费 |
| 677 | 扣费问题-扣费标准不一致 |
| 678 | 扣费问题-未成年误付款 |
| 679 | 其他问题 |
| 610001 | 可观看数量/时长与承诺不符 |
| 610002 | 剧集内容与宣传不符 |
| 610003 | 内容无法播放 |
| 610004 | 未成年人误付款 |
| 610005 | 其他 |

**Res.complaintOrder.status Enum**

| 枚举值 | 描述 |
| --- | --- |
| 101 | 平台客服处理中 |
| 102 | 用户取消申请 |
| 103 | 平台客服处理中 |
| 104 | 平台客服处理中 |
| 105 | 平台客服处理中 |
| 106 | 待商家补充凭证 |
| 107 | 平台客服处理中 |
| 108 | 待双方补充凭证 |
| 109 | 平台客服处理中 |
| 112 | 投诉已完结 |
| 115 | 投诉已完结 |
| 116 | 投诉已完结 |
| 201 | 待处理 |
| 202 | 商家超时未回应，待用户确认 |
| 203 | 已回应,待用户确认 |
| 204 | 已回应,待用户确认 |
| 205 | 投诉已完结 |
| 206 | 平台已判定为商责，待上传处理凭证 |
| 207 | 平台客服核实凭证中 |
| 208 | 超时未上传凭证 |
| 209 | 投诉已关闭 |
| 305 | 平台客服处理中 |
| 307 | 平台客服处理中 |
| 308 | 平台已判定为商责，待用户退货中 |
| 309 | 平台已判定为商责，待用户退货中 |
| 310 | 平台客服处理中 |
| 311 | 签收异常 |
| 312 | 平台判定商家责任，平台退款中 |

**Res.complaintOrder.appealState Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 未进入申诉阶段 |
| 401 | 待商家申诉 |
| 402 | 超过申诉时间 |
| 403 | 申诉中 |
| 117 | 申诉成功 |
| 118 | 申诉失败 |

**Res.item.itemType Enum**

| 枚举值 | 描述 |
| --- | --- |
| 1 | 用户发起投诉 |
| 2 | 用户补充留言 |
| 3 | 商家补充留言 |
| 7 | 用户补充凭证 |
| 8 | 商家补充凭证 |
| 11 | 用户申请平台客服协助 |
| 12 | 用户撤销投诉 |
| 13 | 平台客服处理中 |
| 14 | 待用户补充凭证 |
| 16 | 待商家补充凭证 |
| 18 | 平台要求双方补充凭证 |
| 26 | 平台核实处理凭证异常，投诉关闭，请商家自行联系用户解决问题，保障用户体验 |
| 30 | 平台已核实此投诉非商家责任，投诉已完结 |
| 31 | 平台已核实此投诉为商家责任，待上传处理凭证（blameResult为0）/平台已核实此投诉为商家责任，待用户退货中（blameResult为1） |
| 32 | 平台已核实此投诉为商家责任，待上传处理凭证（blameResult为0）/平台已核实此投诉为商家责任，待用户退货中（blameResult为1） |
| 33 | 平台已核实此投诉非商家责任，投诉已完结 |
| 36 | 平台已核实处理凭证，投诉完结 |
| 37 | 平台核实处理凭证异常，投诉关闭，请商家自行联系用户解决问题，保障用户体验 |
| 101 | 商家超时未回应投诉 |
| 104 | 用户认可处理结果，投诉已完结 |
| 107 | 商家超时未提交投诉处理凭证，平台客服处理中 |
| 108 | 用户超时未确认商家回应结果，投诉已完结 |
| 109 | 商家已回应投诉 |
| 110 | 商家提交投诉处理凭证 |
| 111 | 用户补充凭证超时 |
| 112 | 商家补充凭证超时 |
| 113 | 双方补充凭证超时 |
| 118 | 商责自动赔付 |

**Res.item.appealItemType Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 未进入申诉阶段 |
| 401 | 待商家申诉 |
| 402 | 超过申诉时间 |
| 403 | 申诉中 |
| 117 | 申诉成功 |
| 118 | 申诉失败 |

**Res.returnBill.orderStatus Enum**

| 枚举值 | 描述 |
| --- | --- |
| 0 | 已下单待揽件 |
| 1 | 已揽件 |
| 2 | 运输中 |
| 3 | 派件中 |
| 4 | 已签收 |
| 5 | 异常 |
| 6 | 代签收 |
| 7 | 揽收失败 |
| 8 | 签收失败 |
| 10 | 未下单 |
| 11 | 已取消 |
| 12 | 已删除 |
| 13 | 退件中 |
| 14 | 已退件 |
| 15 | 运力方取消 |
| 99 | 未确认状态 |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

---

### 商家申诉

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/complaint/api_busiappeal.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | string | 是 | 回应的内容（图片数组mediaIdList跟内容content二选一） |
| complaintOrderId | number | 是 | 单号 |
| mediaIdList | array | 是 | 图片 id 列表，可参考这 [新增素材](../../kf-mgnt/kf-message/api_uploadtempmedia)（图片数组mediaIdList跟内容content二选一） |

**返回体 Response Payload**

| 参数名 | 类型 | 示例 | 说明 |
| --- | --- | --- | --- |
| errcode | number |  | [错误码](#apierrcode) |
| errmsg | string | ok | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 成功 |
| 1 | 单号不存在 |
| 2 | 传入mediaIdList或content格式有误 |
| 1002 | 当前状态不支持该操作 |
| 10001 | 参数异常，errmsg字段展示具体描述 |

---

<!-- pages: 16 -->
