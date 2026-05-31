# 小程序服务端 API 结构化参考 — API/face

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### 获取用户人脸核身会话唯一标识

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/face/api_getverifyid.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| out\_seq\_no | string | 是 | 业务方系统内部流水号，要求5-32个字符内，只能包含数字、大小写字母和\_-字符，且在同一个appid下唯一。 |
| cert\_info | [object](#Body__cert_info) | 是 | 用户身份信息 |
| openid | string | 是 | 用户身份标识 |

**Body.cert_info Object Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cert\_type | string | 是 | 证件类型，身份证填 IDENTITY\_CARD |
| cert\_name | string | 是 | 证件姓名 |
| cert\_no | string | 是 | 证件号码 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | [错误码](#apierrcode) |
| errmsg | string | [错误信息](#apierrcode) |
| verify\_id | string | 微信侧生成的人脸核身会话唯一标识，用于后续接口调用。长度不超过 256 字符 |
| expires\_in | number | verify\_id 有效期，过期后无法发起核身，默认值3600，单位：秒 |

**6. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 40003 | openid 无效 |  |
| 84010 | 缺少 out\_seq\_no 参数 |  |
| 84011 | out\_seq\_no 格式无效 |  |
| 84012 | 缺少 cert\_info 参数 |  |
| 84013 | 证件类型无效 |  |
| 84014 | 证件姓名无效 | cert\_name 不能为空，且必须是 UTF-8 编码 |
| 84015 | 证件号码无效 |  |
| 84016 | 缺少 openid 参数 |  |
| 84019 | out\_seq\_no 已存在 | 更换新的 out\_seq\_no |

---

### 查询用户人脸核身真实验证结果

接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考接口调用指南。

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/server/API/face/api_queryverifyinfo.html

**查询参数 Query String Parameters**

| 参数名 | 类型 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- | --- |
| access\_token | string | 是 | ACCESS\_TOKEN | 接口调用凭证，可使用 [access\_token](../mp-access-token/api_getaccesstoken) |

**请求体 Request Payload**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| verify\_id | string | 是 | getVerifyId 接口返回的人脸核身会话唯一标识 |
| out\_seq\_no | string | 是 | 业务方系统外部流水号，必须和 getVerifyId 接口传入的一致 |
| cert\_hash | string | 是 | 根据 getVerifyId 中传入的证件信息生成的信息摘要，计算方式见注意事项。 |
| openid | string | 是 | 用户身份标识，必须和 getVerifyId 接口传入的一致 |

**返回体 Response Payload**

| 参数名 | 类型 | 说明 | 枚举 |
| --- | --- | --- | --- |
| errcode | number | [错误码](#apierrcode) | - |
| errmsg | string | [错误信息](#apierrcode) | - |
| verify\_ret | number | 人脸核身验证结果 | [枚举值](#Enum_Res__verify_ret) |

**Res.verify_ret Enum**

| 枚举值 | 描述 |
| --- | --- |
| 90001 | 设备不支持人脸检测 |
| 90002 | 用户取消 |
| 90003 | 用户取消 |
| 90004 | 用户取消 |
| 90005 | 用户取消 |
| 90006 | 用户取消 |
| 90007 | 网络错误 |
| 90008 | 相机权限未授权 |
| 90009 | 麦克风权限未授权 |
| 90010 | 相机和麦克风权限都未授权 |
| 90011 | 人脸数据采集无效 |
| 90012 | 网络错误上传失败 |
| 90013 | 人脸数据采集无效 |
| 90014 | 人脸数据采集无效 |
| 90017 | 识别过程超时 |
| 90018 | 系统错误 |
| 90104 | 获取人脸配置失败 |
| 90105 | 获取确认数据失败 |
| 90106 | 相机失败 |
| 90107 | 用户检测超时 |
| 90109 | 设备不支持人脸检测 |
| 90110 | 获取协议信息失败 |
| 90199 | 用户系统错误 |
| 10000 | 识别成功 |
| 10001 | 参数错误 |
| 10002 | 人脸特征检测失败 |
| 10003 | 身份证号不匹配 |
| 10004 | 比对人脸信息不匹配 |
| 10005 | 正在检测中 |
| 10006 | appid 没有权限 |
| 10007 | 后台获取图片失败 |
| 10008 | 系统失败 |
| 10010 | 照片质量较低 |
| 10012 | 比对验证失败 |
| 10013 | 系统错误 |
| 10014 | 系统失败 |
| 10015 | 系统失败 |
| 10016 | 存储用户图片失败 |
| 10017 | 非法 Id |
| 10018 | 用户信息不存在 |
| 10020 | 认证超时 |
| 10021 | 重复的请求，返回上一次的结果 |
| 10026 | 用户身份数据不在权威源比对库中 |
| 10029 | 请求超时 |
| 10040 | 请求数据编码不对，必须是 UTF8 编码 |
| 10041 | 非法用户 |
| 10042 | 请求过于频繁，稍后再重试 |
| 10045 | 系统失败 |
| 10052 | 请求超时 |
| 10300 | 未完成核身 |

**7. 错误码**

| 错误码 | 错误描述 | 解决方案 |
| --- | --- | --- |
| 84010 | 缺少 out\_seq\_no 参数 |  |
| 84016 | 缺少 openid 参数 |  |
| 84017 | openid 不匹配 | 必须和 getVerifyId 接口传入的一致 |
| 84018 | cert\_hash 无效或不匹配 | 必须与getVerifyId 接口传入的 cert\_info 一致 |
| 84019 | out\_seq\_no 已存在 | 更换新的 out\_seq\_no |
| 84020 | out\_seq\_no不匹配 | 必须和 getVerifyId 接口传入的一致 |
| 84021 | 缺少 verify\_id 参数 |  |
| 84022 | verify\_id 已过期 | verify\_id 有效期为 1 小时 |

---

<!-- pages: 2 -->
