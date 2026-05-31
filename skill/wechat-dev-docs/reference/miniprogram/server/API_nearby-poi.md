# 小程序服务端 API 结构化参考 — API/nearby-poi

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 添加地点

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/nearby-poi/api_addnearbypoi.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| kf\_info | string | 是 | 客服信息 选填，可自定义服务头像与昵称，具体填写字段见下方示例kf\_info pic\_list是字符串，内容是一个json |
| pic\_list | string | 是 | 门店图片，最多9张，最少1张，上传门店图片如门店外景、环境设施、商品服务等，图片将展示在微信客户端的门店页。图片链接通过文档https://mp.weixin.qq.com/wiki?t=resource/res\_main&id=mp1444738729中的《上传图文消息内的图片获取URL》接口获取。必填，文件格式为bmp、png、jpeg、jpg或gif，大小不超过5M pic\_list是字符串，内容是一个json |
| service\_infos | string | 是 | 必服务标签列表 必填，需要填写 1、 服务标签ID 2、 服务类型tpye 3、 服务名称name 详细字段格式见下方《服务标签id编号、类型与服务名称表》 4、 APPID 5、 对应服务落地页的path路径：path路径页面要与对应的服务标签一致，例如选取外卖服务，path路径应该是小程序的外卖对应的那个页面，path路径获取咨询开发或者到小程序管理后台-工具-生成小程序码页面获取 6、新增服务描述desc：描述服务内容，例如满减、折扣等优惠信息或新品、爆品等商品信息，仅标准服务都可添加，10个字符以内。 service\_infos是字符串，内容是一个json |
| store\_name | string | 是 | 门店名字 必填，门店名称需按照所选地理位置自动拉取腾讯地图门店名称，不可修改，如需修改请重现选择地图地点或重新创建地点。 |
| contract\_phone | string | 是 | 门店电话 |
| hour | string | 是 | 营业时间，格式11:11-12:12 |
| company\_name | string | 是 | 主体名字 |
| credential | string | 是 | 资质号, 15位营业执照注册号或9位组织机构代码 |
| address | string | 是 | 地址 |
| qualification\_list | string | 是 | 证明材料 必填 如果company\_name和该小程序主体不一致，需要填qualification\_list，详细规则见附近的小程序使用指南-如何证明门店的经营主体跟公众号或小程序帐号主体相关http://kf.qq.com/faq/170401MbUnim17040122m2qY.html |
| is\_comm\_nearby | string | 是 | 必填,写死为"1" |
| poi\_id | string | 是 | 如果创建新的门店，poi\_id字段为空 如果更新门店，poi\_id参数则填对应门店的poi\_id 选填 |
| map\_poi\_id | string | 是 | 对应《在腾讯地图中搜索门店》中的sosomap\_poi\_uid字段 腾讯地图那边有些数据不一致，如果不填map\_poi\_id的话，小概率会提交失败！ 注： poi\_id与map\_poi\_id关系： map\_poi\_id是腾讯地图对于poi的唯一标识 poi\_id是门店进驻附近后的门店唯一标识 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | - |
| errmsg | string | - |
| data | [object](#Res__data) | 附近小程序的数据 |

**Res.data Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| audit\_id | number | 审核单 ID |
| poi\_id | number | 附近地点 ID |
| related\_credential | string | 经营资质证件号 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |

---

### 删除地点

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/nearby-poi/api_deletenearbypoi.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| poi\_id | string | 是 | 附近地点 ID |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| -1 | system error | 系统繁忙，此时请开发者稍候再试 |

---

### 查看地点

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/nearby-poi/api_getnearbypoilist.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| page | number | 是 | 起始页id（从1开始计数） |
| page\_rows | number | 是 | 每页展示个数（最多1000个） |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| data | [object](#Res__data) | 附近小程序的数据 |

**Res.data Object Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| max\_apply\_num | number | 最大可添加地点个数 |
| left\_apply\_num | number | 剩余可添加地点个数 |
| data | string | 地址列表的 JSON 格式字符串 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 20002 | POST参数非法 |  |
| 40001 | invalid credential  access\_token isinvalid or not latest | 获取 access\_token 时 AppSecret 错误，或者 access\_token 无效。请开发者认真比对 AppSecret 的正确性，或查看是否正在为恰当的公众号调用接口 |
| 44002 | empty post data | POST 的数据包为空 |
| 92000 | 该经营资质已添加，请勿重复添加 | 该经营资质已添加，请勿重复添加 |
| 92002 | 附近地点添加数量达到上线，无法继续添加 | 附近地点添加数量达到上线，无法继续添加 |
| 92003 | 地点已被其它小程序占用 | 地点已被其它小程序占用 |
| 92004 | 附近功能被封禁 |  |
| 92005 | 地点正在审核中 | 地点正在审核中 |
| 92006 | 地点正在展示小程序 |  |
| 92007 | 地点审核失败 |  |
| 92008 | 小程序未展示在该地点 | 小程序未展示在该地点 |
| 93009 | 小程序未上架或不可见 | 小程序未上架或不可见 |
| 93010 | 地点不存在 | 地点不存在 |
| 93011 | 个人类型小程序不可用 | 个人类型小程序不可用 |
| 93012 | 非普通类型小程序（门店小程序、小店小程序等）不可用 | 非普通类型小程序（门店小程序、小店小程序等）不可用 |
| 93013 | 从腾讯地图获取地址详细信息失败 | 从腾讯地图获取地址详细信息失败 |
| 93014 | 同一资质证件号重复添加 |  |

---

### 设置展示状态

调试诊断

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/nearby-poi/api_setshowstatus.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access\_token | string | 是 | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken)、[authorizer\_access\_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| poi\_id | string | 是 | 附近地点 ID |
| status | number | 是 | 是否展示,0表示不展示，1表示展示 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 0 | ok | ok |

---

<!-- pages: 4 -->
