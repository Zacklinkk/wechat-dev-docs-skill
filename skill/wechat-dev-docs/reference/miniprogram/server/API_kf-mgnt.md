# 小程序服务端 API 结构化参考 — API/kf-mgnt

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 添加客服账号

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-message/api_addkfaccount.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| kf\_account | string | 是 | test1@test | 完整客服账号，格式为：账号前缀@公众号微信号，账号前缀最多10个字符，必须是英文、数字字符或者下划线，后缀为公众号微信号，长度不超过30个字符 |
| nickname | string | 是 | 客服1 | 客服昵称，最长16个字 |
| business\_id | string | 否 | - | 客服子商户的business\_id，对于普通账号客服不需要填business\_id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok或者in a normal state | ok是指从不正常变成正常 in a normal state是指本来就正常 |
| 40003 | 非法的openid |  |
| 40005 | 不支持的媒体类型 |  |
| 40009 | 媒体文件长度不合法 |  |
| 65400 | please enable new custom service or wait for a while if you have enabled | API不可用，即没有开通/升级到新客服功能 |
| 65401 | 无效客服账号 |  |
| 65402 | 客服账号尚未绑定微信号，不能投入使用 |  |
| 65403 | illegal nickname | 客服昵称不合法 |
| 65404 | illegal custom service account | 客服账号不合法 |
| 65405 | custom service account number reach limit | 账号数目已达到上限，不能继续添加 |
| 65406 | custom service account exists | 已经存在的客服账号 |
| 65407 | 邀请对象已经是该小程序客服 |  |
| 65408 | 本小程序已经有一个邀请给该微信 |  |
| 65409 | 无效的微信号 |  |
| 65410 | 邀请对象绑定小程序客服数达到上限 |  |
| 65411 | 该账号已经有一个等待确认的邀请，不能重复邀请 |  |
| 65412 | 该账号已经绑定微信号，不能进行邀请 |  |
| 65413 | 不存在对应用户的会话信息 |  |
| 65414 | 客户正在被其他客服接待 |  |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | 仅认证 | 仅认证 | ✔ |

---

### 获取所有客服账号

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-message/api_getkflist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| business\_id | string | 否 | 客服子商户的business\_id，对于普通账号（小程序、公众号、服务号）客服不需要填business\_id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| kf\_list | [objarray](#Res__kf_list<Array>) | 客服列表 |

**Res.kf_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| kf\_account | string | 完整客服账号，格式为：账号前缀@公众号微信号 |
| kf\_nick | string | 客服昵称 |
| kf\_id | string | 客服编号 |
| kf\_headimgurl | string | 客服头像 |
| kf\_wx | string | 如果客服账号已绑定了客服人员微信号， 则此处显示微信号 |
| invite\_wx | string | 如果客服账号尚未绑定微信号，但是已经发起了一个绑定邀请， 则此处显示绑定邀请的微信号 |
| invite\_expire\_time | string | 如果客服账号尚未绑定微信号，但是已经发起过一个绑定邀请， 邀请的过期时间，为unix 时间戳 |
| invite\_status | string | 邀请的状态，有等待确认“waiting”，被拒绝“rejected”， 过期“expired” |
| kf\_openid | string | 客服openid |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 成功 |
| 40003 | 非法的openid |
| 40005 | 不支持的媒体类型 |
| 40009 | 媒体文件长度不合法 |
| 65400 | API不可用，即没有开通/升级到新版客服功能 |
| 65401 | 无效客服账号 |
| 65402 | 客服账号尚未绑定微信号，不能投入使用 |
| 65403 | 客服昵称不合法 |
| 65404 | 客服账号不合法 |
| 65405 | 账号数目已达到上限，不能继续添加 |
| 65406 | 已经存在的客服账号 |
| 65407 | 邀请对象已经是该小程序客服 |
| 65408 | 本小程序已经有一个邀请给该微信 |
| 65409 | 无效的微信号 |
| 65410 | 邀请对象绑定小程序客服数达到上限 |
| 65411 | 该账号已经有一个等待确认的邀请，不能重复邀请 |
| 65412 | 该账号已经绑定微信号，不能进行邀请 |
| 65413 | 不存在对应用户的会话信息 |
| 65414 | 客户正在被其他客服接待 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | 仅认证 | 仅认证 | ✔ |

---

### 获取在线客服列表

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-message/api_getonlinekflist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| business\_id | string | 否 | 客服子商户的business\_id，对于普通小程序客服不需要填business\_id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| kf\_online\_list | [objarray](#Res__kf_online_list<Array>) | 在线客服列表 |

**Res.kf_online_list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| kf\_account | string | 完整客服账号，格式为：账号前缀@公众号微信号 |
| status | number | 客服在线状态，目前为：0-不在线，1-web 在线 |
| kf\_id | number | 客服编号 |
| accepted\_case | number | 客服当前正在接待的会话数 |
| kf\_openid | string | 客服openid |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 成功 |
| 40003 | 非法的openid |
| 40005 | 不支持的媒体类型 |
| 40009 | 媒体文件长度不合法 |
| 65400 | API不可用，即没有开通/升级到新版客服功能 |
| 65401 | 无效客服账号 |
| 65402 | 客服账号尚未绑定微信号，不能投入使用 |
| 65403 | 客服昵称不合法 |
| 65404 | 客服账号不合法 |
| 65405 | 账号数目已达到上限，不能继续添加 |
| 65406 | 已经存在的客服账号 |
| 65407 | 邀请对象已经是该小程序客服 |
| 65408 | 本小程序已经有一个邀请给该微信 |
| 65409 | 无效的微信号 |
| 65410 | 邀请对象绑定小程序客服数达到上限 |
| 65411 | 该账号已经有一个等待确认的邀请，不能重复邀请 |
| 65412 | 该账号已经绑定微信号，不能进行邀请 |
| 65413 | 不存在对应用户的会话信息 |
| 65414 | 客户正在被其他客服接待 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | 仅认证 | 仅认证 | ✔ |

---

### 删除客服账号

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-message/api_delkfaccount.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| kf\_account | string | 是 | 完整客服帐号，格式为：帐号前缀@公众号微信号 |
| business\_id | string | 否 | 客服子商户的business\_id，对于普通账号客服不需要填business\_id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok或者in a normal state | ok是指从不正常变成正常 in a normal state是指本来就正常 |
| 40003 | 非法的openid |  |
| 40005 | 不支持的媒体类型 |  |
| 40009 | 媒体文件长度不合法 |  |
| 65400 | please enable new custom service or wait for a while if you have enabled | API不可用，即没有开通/升级到新版客服功能 |
| 65401 | invalid custom service account | 无效客服账号 |
| 65402 | 客服账号尚未绑定微信号，不能投入使用 |  |
| 65403 | 客服昵称不合法 |  |
| 65404 | 客服账号不合法 |  |
| 65405 | 账号数目已达到上限，不能继续添加 |  |
| 65406 | 已经存在的客服账号 |  |
| 65407 | 邀请对象已经是该小程序客服 |  |
| 65408 | 本小程序已经有一个邀请给该微信 |  |
| 65409 | 无效的微信号 |  |
| 65410 | 邀请对象绑定小程序客服数达到上限 |  |
| 65411 | 该账号已经有一个等待确认的邀请，不能重复邀请 |  |
| 65412 | 该账号已经绑定微信号，不能进行邀请 |  |
| 65413 | 不存在对应用户的会话信息 |  |
| 65414 | 客户正在被其他客服接待 |  |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | 仅认证 | 仅认证 | ✔ |

---

### 发送客服消息

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-message/api_sendcustommessage.html

| 场景 | 下发额度 | 额度有效期 |
| --- | --- | --- |
| 用户发送消息 | 5条 | 48小时 |
| 点击自定义菜单 | 3条 | 1分钟 |
| 关注公众号 | 3条 | 1分钟 |
| 扫描二维码 | 3条 | 1分钟 |

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| touser | string | 是 | 用户的 OpenID |
| msgtype | string | 是 | 消息类型。text表示文本消息；image表示图片消息；link表示图文链接；miniprogrampage表示小程序卡片。 |
| text | [object](#Body__text) | 否 | 文本消息，msgtype="text" 时必填 |
| image | [object](#Body__image) | 否 | 图片消息，msgtype="image" 时必填 |
| voice | [object](#Body__voice) | 否 | 语音消息，msgtype="voice" 时必填 |
| video | [object](#Body__video) | 否 | 视频消息，msgtype="video" 时必填 |
| music | [object](#Body__music) | 否 | 音乐消息，msgtype="music" 时必填 |
| news | [object](#Body__news) | 否 | 图文消息（点击跳转到外链），msgtype="news" 时必填 |
| mpnews | [object](#Body__mpnews) | 否 | 图文消息（点击跳转到图文消息页面），msgtype="mpnews" 时必填，图文消息条数限制在1条以内，注意，如果图文数超过1，则将会返回错误码45008。（草稿灰度完成后，此类型不再支持） |
| mpnewsarticle | [object](#Body__mpnewsarticle) | 否 | 图文消息（点击跳转到图文消息页面），msgtype="mpnewsarticle" 时必填，使用通过 “发布” 系列接口得到的 article\_id |
| msgmenu | [object](#Body__msgmenu) | 否 | 菜单消息，msgtype="msgmenu" 时必填 |
| wxcard | [object](#Body__wxcard) | 否 | 卡券信息，msgtype="wxcard"时必填 |
| miniprogrampage | [object](#Body__miniprogrampage) | 否 | 小程序消息，msgtype="miniprogrampage"时必填 |
| customservice | [object](#Body__customservice) | 否 | 以某个客服账号来发消息 |
| aimsgcontext | [object](#Body__aimsgcontext) | 否 | ai 消息上下文 |
| businessid | string | 否 | 子商户ID，普通账号无需传 |

**Body.text Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | string | 是 | 文本内容，支持插入跳小程序的文字链， 例如「文本内容[点击跳小程序](http://www.qq.com)」  说明： 1.data-miniprogram-appid 项，填写小程序appid，则表示该链接跳小程序； 2.data-miniprogram-path项，填写小程序路径，路径与app.json中保持一致，可带参数； 3.对于不支持data-miniprogram-appid 项的客户端版本，如果有herf项，则仍然保持跳href中的网页链接； 4.data-miniprogram-appid对应的小程序必须与公众号有绑定关系。 |

**Body.image Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| media\_id | string | 是 | 媒体ID，通过素材上传接口获得。 |

**Body.voice Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| media\_id | string | 是 | 媒体ID，通过素材上传接口获得。 |

**Body.video Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| media\_id | string | 是 | 媒体ID，通过素材上传接口获得。 |
| thumb\_media\_id | string | 是 | 缩略图媒体ID，通过素材上传接口获得。 |
| title | string | 否 | 视频标题 |
| description | string | 否 | 视频描述 |

**Body.music Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 是 | 音乐标题 |
| description | string | 是 | 音乐描述 |
| musicurl | string | 是 | 音乐链接 |
| hqmusicurl | string | 否 | 高质量音乐链接 |
| thumb\_media\_id | string | 是 | 缩略图媒体ID |

**Body.news Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| articles | [objarray](#Body__news__articles<Array>) | 是 | 图文消息条数限制在1条以内 |

**Body.mpnews Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| media\_id | string | 是 | 素材ID，通过素材上传接口获得。 |

**Body.mpnewsarticle Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| article\_id | string | 是 | 发布文章ID |

**Body.msgmenu Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| head\_content | string | 否 | 菜单描述 |
| list | [objarray](#Body__msgmenu__list<Array>) | 是 | 菜单内容 |
| tail\_content | string | 否 | 菜单结尾 |

**Body.wxcard Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| card\_id | string | 是 | 卡券ID |

**Body.miniprogrampage Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 是 | 小程序卡片标题 |
| appid | string | 是 | 小程序APPID |
| pagepath | string | 是 | 小程序的页面路径，跟app.json对齐，支持参数，比如pages/index/index?foo=bar |
| thumb\_media\_id | string | 是 | 小程序消息卡片的封面， image 类型的 media\_id，通过素材上传图片文件获得，建议大小为 520\*416 |

**Body.customservice Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| kf\_account | string | 是 | 客服账号 |

**Body.aimsgcontext Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| is\_ai\_msg | number | 否 | 消息下方增加灰色 wording “内容由第三方AI生成” 0 不增加 1 增加 |

**Body.news.articles(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 是 | 消息标题 |
| description | string | 是 | 消息描述 |
| picurl | string | 是 | 封面图片url |
| url | string | 是 | 跳转url |

**Body.msgmenu.list(Array) Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 菜单值 |
| content | string | 是 | 菜单项 |

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
| 40013 | invalid appid | 不合法的 AppID ，请开发者检查 AppID 的正确性，避免异常字符，注意大小写 |
| 70000 | 为保护未成年人权益，该条消息发送失败 |  |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | 仅认证 | 仅认证 | ✔ |

---

### 客服输入状态

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-message/api_typing.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| touser | string | 是 | 用户的 OpenID |
| command | string | 是 | 命令。Typing表示对用户下发"正在输入"状态 ；CancelTyping表示取消对用户的"正在输入"状态 |
| businessid | string | 否 | 子商户 ID，普通账号无需填写 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40200 | invalid account type | 账号类型不符合要求 |
| 45072 | invalid command | command字段取值不对 |
| 45080 | need sending message to user  orrecving message from user in the last 30 seconds before typing | 下发输入状态，需要之前30秒内跟用户有过消息交互 |
| 45081 | you are already typing | 已经在输入状态，不可重复下发 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | 仅认证 | 仅认证 | ✔ |

---

### 设置客服管理员

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-message/api_setkfadmin.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| kf\_openid | string | 是 | - | 账号openid |
| business\_id | string | 否 | - | 客服子商户的business\_id，对于普通账号客服不需要填business\_id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 成功 |
| 40003 | 非法的openid |
| 40005 | 不支持的媒体类型 |
| 40009 | 媒体文件长度不合法 |
| 65400 | API不可用，即没有开通/升级到新版客服功能 |
| 65401 | 无效客服账号 |
| 65402 | 客服账号尚未绑定微信号，不能投入使用 |
| 65403 | 客服昵称不合法 |
| 65404 | 客服账号不合法 |
| 65405 | 账号数目已达到上限，不能继续添加 |
| 65406 | 已经存在的客服账号 |
| 65407 | 邀请对象已经是该小程序客服 |
| 65408 | 本小程序已经有一个邀请给该微信 |
| 65409 | 无效的微信号 |
| 65410 | 邀请对象绑定小程序客服数达到上限 |
| 65411 | 该账号已经有一个等待确认的邀请，不能重复邀请 |
| 65412 | 该账号已经绑定微信号，不能进行邀请 |
| 65413 | 不存在对应用户的会话信息 |
| 65414 | 客户正在被其他客服接待 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | 仅认证 | 仅认证 | ✔ |

---

### 取消客服管理员

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-message/api_cancelkfadmin.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| kf\_openid | string | 是 | - | 账号openid |
| business\_id | string | 否 | - | 客服子商户的business\_id，对于普通账号客服不需要填business\_id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 0 | 成功 |
| 40003 | 非法的openid |
| 40005 | 不支持的媒体类型 |
| 40009 | 媒体文件长度不合法 |
| 65400 | API不可用，即没有开通/升级到新版客服功能 |
| 65401 | 无效客服账号 |
| 65402 | 客服账号尚未绑定微信号，不能投入使用 |
| 65403 | 客服昵称不合法 |
| 65404 | 客服账号不合法 |
| 65405 | 账号数目已达到上限，不能继续添加 |
| 65406 | 已经存在的客服账号 |
| 65407 | 邀请对象已经是该小程序客服 |
| 65408 | 本小程序已经有一个邀请给该微信 |
| 65409 | 无效的微信号 |
| 65410 | 邀请对象绑定小程序客服数达到上限 |
| 65411 | 该账号已经有一个等待确认的邀请，不能重复邀请 |
| 65412 | 该账号已经绑定微信号，不能进行邀请 |
| 65413 | 不存在对应用户的会话信息 |
| 65414 | 客户正在被其他客服接待 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | 仅认证 | 仅认证 | ✔ |

---

### 新增临时素材

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-message/api_uploadtempmedia.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| type | string | 是 | 媒体文件类型，分别有图片（image）、语音（voice）、视频（video）和缩略图（thumb） |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| media | formdata | 是 | form-data 中媒体文件标识，有filename、filelength、content-type等信息 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| type | string | 媒体文件类型 |
| media\_id | string | 媒体文件标识 |
| created\_at | number | 上传时间戳 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40004 | invalid media type | 不合法的媒体文件类型 |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ |

---

### 获取临时素材

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-message/api_getmedia.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |
| media\_id | string | 是 | MEDIA\_ID | 媒体文件ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| video\_url | string | 视频消息素材下载地址 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 40007 | invalid media\_id | 无效的媒体ID |

**7. 适用范围**

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ |

---

### 客服子商户创建商户

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-management/api_registerbusiness.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| account\_name | string | 是 | 创建商户时用到，一个account\_name只能创建一次，account\_name为6-30字符，必须为英文、数字、或者下划线，区分大小写。 |
| nickname | string | 是 | 商户昵称，会在客户端会话里展示，4-30字符(中文视为2字符)，由中文、英文、数字组成 |
| icon\_media\_id | string | 是 | 头像，图片类型，需要用临时素材接口得到，使用[新增临时素材](../kf-message/api_uploadtempmedia)，为空则不更新头像 |
| transfer\_to\_commkf | boolean | 否 | 是否将消息转发到通用客服，false为不转发，true为转发，如果transfer\_to\_commkf=true时，可以使用客服管理相关api，请求参数新增business\_id |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |
| business\_id | string | 商户ID |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 40004 | icon\_media\_id类型不对，应该为图片类型 |
| 40007 | icon\_media\_id不是合法的media\_id |
| 45070 | account\_name对应账号已经被创建(一个account\_name对应一个business\_id) |
| 45077 | 子商户数量已达到上限 |
| 45078 | 昵称不合法，请检查是否满足nickname规则 |
| 45079 | 昵称含有违规词汇 |
| 45091 | account\_name不合法，请检查是否满足account\_name规则 |

---

### 客服子商户更新商户信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-management/api_updatebusiness.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| business\_id | string | 是 | 创建商户时得到的商户id |
| nickname | string | 否 | 商户昵称，会在客户端会话里展示，4-30字符(中文视为2字符)，由中文、英文、数字组成 |
| icon\_media\_id | string | 否 | 头像，图片类型，需要用临时素材接口得到，使用[新增临时素材](../kf-message/api_uploadtempmedia)，为空则不更新头像 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 40004 | icon\_media\_id类型不对，应该为图片类型 |
| 40007 | icon\_media\_id不是合法的media\_id |
| 45071 | business\_id对应的商户不存在 |
| 45077 | 子商户数量已达到上限 |
| 45078 | 昵称不合法，请检查是否满足nickname规则 |
| 45079 | 昵称含有违规词汇 |

---

### 客服子商户拉取单个商户信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-management/api_getbusiness.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| business\_id | string | 否 | 创建商户时得到的商户id,与account\_name选填一个 |
| account\_name | string | 否 | 创建商户时用到的account\_name,与business\_id选填一个 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |
| business\_info | [object](#Res__business_info) | 商户信息 |

**Res.business_info Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| business\_id | string | 商户ID |
| account\_name | string | 商户账号名称 |
| nickname | string | 商户昵称，会在客户端会话里展示 |
| icon\_media\_id | string | 商户头像 |

**6. 错误码**

| 错误码 | 错误描述 |
| --- | --- |
| 45071 | business\_id对应的商户不存在 |

---

### 客服子商户拉取多个商户信息

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-management/api_listbusiness.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 用于分页拉取，从0开始 |
| count | number | 是 | 一次拉取的商户个数，最多为200 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误描述](#apierrcode) |
| list | [objarray](#Res__list<Array>) | 商户信息列表 |

**Res.list(Array) Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| business\_id | string | 商户ID |
| account\_name | string | 商户账号名称 |
| nickname | string | 商户昵称，会在客户端会话里展示 |
| icon\_media\_id | string | 商户头像 |

---

<!-- pages: 14 -->
