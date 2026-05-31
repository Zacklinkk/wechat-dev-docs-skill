# 微信小游戏 API 结构化参考 — game-server-manager

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### GameServerManager wx.getGameServerManager()

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/wx.getGameServerManager.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1001 | has not logged in to server | 未登录到服务器就调用接口 |
| 2100 |  | 登录帧同步服务器超时 |
| 2101 |  | 重连帧同步服务器超时 |
| 2200 |  | 登录帧同步服务器错误或失败导致的disconnect |
| 2201 |  | 长期未收到帧导致的disconnect |
| 2202 |  | 长期未收到心跳导致的disconnect |
| 2203 |  | 断线过久，无法重连导致的disconnect |
| 2204 |  | UDPconnectionfail导致的disconnect |
| 2300 |  | UDPsocketerror |
| 2301 |  | UDPsystemerror |
| 2303 |  | UDPaddresserror |
| 2304 |  | UDPporterror |
| 2305 |  | UDPsenderror |
| 2401 |  | 登录帧同步服务器成功之前发送帧 |
| 2402 |  | frame长度超过MTU |
| 4001 | system error | 系统错误 |
| 4002 | record not exist | 访问记录不存在 |
| 4003 | invalid req | 非法请求 |
| 4005 | invalid room state | 房间状态异常 |
| 4006 | reach room member limit | 房间到达人数上限，无法加入 |
| 4009 | headimg and nickname is not authorized by the user | 该房间需要用户头像昵称，但用户未授权 |
| 4010 | fail to start game | 启动游戏失败 |
| 4011 | fail to broadcast | 广播消息失败 |
| 4013 | buffer overflow | 自定义 buffer 超过指定大小（matchInfo 和 extInfo） |
| 200000 |  | 无效的请求参数 |
| 200006 |  | matchid此时为未打开状态 |
| 500001 |  | 用户已经在匹配队列中 |
| 500003 |  | 用户未在匹配队列中 |
| 500005 |  | 无效的match\_id |
| 500009 |  | 路由到错误的服务器 |

---

### GameServerManager

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.html

---

### Promise GameServerManager.broadcastInRoom(object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.broadcastInRoom.html

**object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| msg | string |  | 是 | 广播内容 |
| toPosNumList | Array.<number> |  | 是 | 给座位号为哪些的玩家发送信息，不填代表给房间所有人发送 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### Promise GameServerManager.cancelMatch(object object)

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.cancelMatch.html

**object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| matchId | string |  | 是 | 需要取消匹配的matchId |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### Promise GameServerManager.changeSeat(object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.changeSeat.html

**object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| posNum | number |  | 是 | 座位号，从 0 开始 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### Promise GameServerManager.createRoom(object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.createRoom.html

**object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | maxMemberNum | number |  | 是 | 房间最大人数 |
|  | startPercent | number | 0 | 否 | 需要满足百分比的玩家都发送了开始指令才能启动游戏。有效范围 0~100，0 表示只要有一个人调用开始就启动，100 表示要求所有人都开始才能启动。 |
|  | needUserInfo | boolean | false | 否 | 是否需要用户头像和昵称 |
|  | | 合法值 | 说明 | | --- | --- | | true | 需要用户头像和昵称，则每个加入房间的人必须授权过用户信息，MemberInfo 中会有 headimage 和 nickname | | false | 不需要用户头像和昵称，MemberInfo 中不会有 headimage 和 nickname | | | | | |
|  | gameLastTime | number | 1200 | 否 | 游戏对局时长，到达指定时长时游戏会结束，最大值 3600。 |
|  | roomExtInfo | string |  | 否 | 游戏自定义的关于房间扩展信息，其他人可在 `RoomInfo` 中读取到最多 32 个字节 |
|  | memberExtInfo | string |  | 否 | 游戏自定义的关于个人的扩展信息，其他人可在 `MemberInfo` 中读取到，最多 32 个字节 |
|  | needGameSeed | boolean | false | 否 | 是否需要生成游戏随机种子，设置为 true，房间信息会携带 gameSeed 属性 |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**object object**

| 合法值 | 说明 |
| --- | --- |
| true | 需要用户头像和昵称，则每个加入房间的人必须授权过用户信息，MemberInfo 中会有 headimage 和 nickname |
| false | 不需要用户头像和昵称，MemberInfo 中不会有 headimage 和 nickname |

**object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | data | object |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | accessInfo | string | 房间唯一标识 | |  | clientId | number | 用户在房间内的唯一标识 | | | |
|  | errMsg | string | 错误信息 |
|  | errCode | number | 错误码 |

**object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | accessInfo | string | 房间唯一标识 |
|  | clientId | number | 用户在房间内的唯一标识 |

---

### Promise GameServerManager.endGame(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.endGame.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### Promise GameServerManager.endStateService(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.endStateService.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### GameServerManager.getFriendsStateData(Object object)

基础库 2.9.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.getFriendsStateData.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | list | Array.<Object> | 好友状态信息列表 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | userState | string | 该玩家的自定义状态信息，通过 `GameServerManager.setState` 接口设置 | |  | sysState | number | 系统状态，0 掉线 1 在线 | |  | openId | string | 好友 openId | |  | nickName | string | 好友昵称 | |  | avatarUrl | string | 好友头像 | |  | gender | number | 好友性别 0未设置 1男 2女 | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | userState | string | 该玩家的自定义状态信息，通过 `GameServerManager.setState` 接口设置 |
|  | sysState | number | 系统状态，0 掉线 1 在线 |
|  | openId | string | 好友 openId |
|  | nickName | string | 好友昵称 |
|  | avatarUrl | string | 好友头像 |
|  | gender | number | 好友性别 0未设置 1男 2女 |

---

### Promise GameServerManager.getJoinVoIPChatSignature(object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.getJoinVoIPChatSignature.html

**object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| subRoomId | string |  | 否 | 子房间 ID，用于区分同一房间下的不同语音子房间 |
| voipType | number |  | 否 | voip 房间类型，1 为整个游戏房间，2 为子房间 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | data | object |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | signature | string | 签名 | |  | nonceStr | string | 随机字符串 | |  | timeStamp | number | 时间戳 | |  | groupId | string | 语音房间的 groupId | | | |
|  | errMsg | string | 错误信息 |
|  | errCode | number | 错误码 |

**object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | signature | string | 签名 |
|  | nonceStr | string | 随机字符串 |
|  | timeStamp | number | 时间戳 |
|  | groupId | string | 语音房间的 groupId |

---

### Promise GameServerManager.getLastRoomInfo(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.getLastRoomInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | data | object |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | accessInfo | string | 最近参与房间的 accessInfo | |  | roomInfo | Object | 最近参与房间的详细信息 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 小游戏 appId | |  | roomIdStr | number | 房间 ID | |  | roomState | number | 房间状态 | |  | | 合法值 | 说明 | | --- | --- | | 1 | 组队中 | | 2 | 该房间的对局游戏已开始 | | 3 | 该房间的对局游戏已结束 | | 4 | 房间已销毁 | | 5 | 房间连接已建立，等待对战连接建立 | | | | |  | maxMemberNum | number | 房间最多可容纳人数 | |  | createTimestamp | number | 创建时间 | |  | updateTimestamp | number | 最近更新时间 | |  | gameTick | number | 游戏下发帧的时间间隔，单位 ms | |  | startPercent | number | 需要满足百分比的玩家都发送了开始指令才能启动游戏。有效范围 0~100，0 表示只要有一个人调用开始就启动，100 表示要求所有人都开始才能启动。 | |  | roomExtInfo | string | 游戏自定义的关于房间的扩展信息 | |  | gameLastTime | number | 游戏对局时长，单位 s | |  | udpReliabilityStrategy | number | UDP可靠性策略， 0：全冗余 N：固定冗余N帧 | |  | memberList | Array.<Object> | 成员列表 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | isReady | boolean | 玩家准备状态 | |  | role | number | 角色 | |  | | 合法值 | 说明 | | --- | --- | | 0 | 普通成员 | | 1 | 房主 | | | | |  | posNum | number | 座位号，从 0 开始 | |  | headimg | string | 头像 URL（房间 needUserInfo 为 true 时才会有） | |  | nickname | string | 用户昵称（房间 needUserInfo 为 true 时才会有） | |  | clientId | number | 用户在房间内的唯一标识 | |  | enableToStart | boolean | 是否已做好游戏开始准备（调用过 startGame） | |  | memberExtInfo | string | 游戏自定义的关于成员的扩展信息 | | | | |  | seed | string | 游戏随机种子 | | | | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | accessInfo | string | 最近参与房间的 accessInfo |
|  | roomInfo | Object | 最近参与房间的详细信息 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 小游戏 appId | |  | roomIdStr | number | 房间 ID | |  | roomState | number | 房间状态 | |  | | 合法值 | 说明 | | --- | --- | | 1 | 组队中 | | 2 | 该房间的对局游戏已开始 | | 3 | 该房间的对局游戏已结束 | | 4 | 房间已销毁 | | 5 | 房间连接已建立，等待对战连接建立 | | | | |  | maxMemberNum | number | 房间最多可容纳人数 | |  | createTimestamp | number | 创建时间 | |  | updateTimestamp | number | 最近更新时间 | |  | gameTick | number | 游戏下发帧的时间间隔，单位 ms | |  | startPercent | number | 需要满足百分比的玩家都发送了开始指令才能启动游戏。有效范围 0~100，0 表示只要有一个人调用开始就启动，100 表示要求所有人都开始才能启动。 | |  | roomExtInfo | string | 游戏自定义的关于房间的扩展信息 | |  | gameLastTime | number | 游戏对局时长，单位 s | |  | udpReliabilityStrategy | number | UDP可靠性策略， 0：全冗余 N：固定冗余N帧 | |  | memberList | Array.<Object> | 成员列表 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | isReady | boolean | 玩家准备状态 | |  | role | number | 角色 | |  | | 合法值 | 说明 | | --- | --- | | 0 | 普通成员 | | 1 | 房主 | | | | |  | posNum | number | 座位号，从 0 开始 | |  | headimg | string | 头像 URL（房间 needUserInfo 为 true 时才会有） | |  | nickname | string | 用户昵称（房间 needUserInfo 为 true 时才会有） | |  | clientId | number | 用户在房间内的唯一标识 | |  | enableToStart | boolean | 是否已做好游戏开始准备（调用过 startGame） | |  | memberExtInfo | string | 游戏自定义的关于成员的扩展信息 | | | | |  | seed | string | 游戏随机种子 | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | appId | string | 小游戏 appId |
|  | roomIdStr | number | 房间 ID |
|  | roomState | number | 房间状态 |
|  | | 合法值 | 说明 | | --- | --- | | 1 | 组队中 | | 2 | 该房间的对局游戏已开始 | | 3 | 该房间的对局游戏已结束 | | 4 | 房间已销毁 | | 5 | 房间连接已建立，等待对战连接建立 | | | |
|  | maxMemberNum | number | 房间最多可容纳人数 |
|  | createTimestamp | number | 创建时间 |
|  | updateTimestamp | number | 最近更新时间 |
|  | gameTick | number | 游戏下发帧的时间间隔，单位 ms |
|  | startPercent | number | 需要满足百分比的玩家都发送了开始指令才能启动游戏。有效范围 0~100，0 表示只要有一个人调用开始就启动，100 表示要求所有人都开始才能启动。 |
|  | roomExtInfo | string | 游戏自定义的关于房间的扩展信息 |
|  | gameLastTime | number | 游戏对局时长，单位 s |
|  | udpReliabilityStrategy | number | UDP可靠性策略， 0：全冗余 N：固定冗余N帧 |
|  | memberList | Array.<Object> | 成员列表 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | isReady | boolean | 玩家准备状态 | |  | role | number | 角色 | |  | | 合法值 | 说明 | | --- | --- | | 0 | 普通成员 | | 1 | 房主 | | | | |  | posNum | number | 座位号，从 0 开始 | |  | headimg | string | 头像 URL（房间 needUserInfo 为 true 时才会有） | |  | nickname | string | 用户昵称（房间 needUserInfo 为 true 时才会有） | |  | clientId | number | 用户在房间内的唯一标识 | |  | enableToStart | boolean | 是否已做好游戏开始准备（调用过 startGame） | |  | memberExtInfo | string | 游戏自定义的关于成员的扩展信息 | | | |
|  | seed | string | 游戏随机种子 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 1 | 组队中 |
| 2 | 该房间的对局游戏已开始 |
| 3 | 该房间的对局游戏已结束 |
| 4 | 房间已销毁 |
| 5 | 房间连接已建立，等待对战连接建立 |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | isReady | boolean | 玩家准备状态 |
|  | role | number | 角色 |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 普通成员 | | 1 | 房主 | | | |
|  | posNum | number | 座位号，从 0 开始 |
|  | headimg | string | 头像 URL（房间 needUserInfo 为 true 时才会有） |
|  | nickname | string | 用户昵称（房间 needUserInfo 为 true 时才会有） |
|  | clientId | number | 用户在房间内的唯一标识 |
|  | enableToStart | boolean | 是否已做好游戏开始准备（调用过 startGame） |
|  | memberExtInfo | string | 游戏自定义的关于成员的扩展信息 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 0 | 普通成员 |
| 1 | 房主 |

---

### Promise GameServerManager.getLostFrames(object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.getLostFrames.html

**object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| beginFrameId | number |  | 是 | 起始帧号。不填或非法值默认从第 1 帧开始补 |
| endFrameId | number |  | 是 | 结尾帧号。不填或非法值默认补到当前最新帧 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | data | object |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | frameList | Array.<Frame> | 丢失的帧数组 | | | |

**object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | frameList | Array.<Frame> | 丢失的帧数组 |

---

### Promise GameServerManager.getRoomInfo(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.getRoomInfo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | data | object |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | roomInfo | Object |  | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 小游戏 appId | |  | roomIdStr | number | 房间 ID | |  | roomState | number | 房间状态 | |  | | 合法值 | 说明 | | --- | --- | | 1 | 组队中 | | 2 | 该房间的对局游戏已开始 | | 3 | 该房间的对局游戏已结束 | | 4 | 房间已销毁 | | 5 | 房间连接已建立，等待对战连接建立 | | | | |  | maxMemberNum | number | 房间最多可容纳人数 | |  | createTimestamp | number | 创建时间 | |  | updateTimestamp | number | 最近更新时间 | |  | gameTick | number | 游戏下发帧的时间间隔，单位 ms | |  | startPercent | number | 需要满足百分比的玩家都发送了开始指令才能启动游戏。有效范围 0~100，0 表示只要有一个人调用开始就启动，100 表示要求所有人都开始才能启动。 | |  | roomExtInfo | string | 游戏自定义的关于房间的扩展信息 | |  | gameLastTime | number | 游戏对局时长，单位 s | |  | udpReliabilityStrategy | number | UDP可靠性策略， 0：全冗余 N：固定冗余N帧 | |  | memberList | Array.<Object> | 成员列表 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | isReady | boolean | 玩家准备状态 | |  | role | number | 角色 | |  | | 合法值 | 说明 | | --- | --- | | 0 | 普通成员 | | 1 | 房主 | | | | |  | posNum | number | 座位号，从 0 开始 | |  | headimg | string | 头像 URL（房间 needUserInfo 为 true 时才会有） | |  | nickname | string | 用户昵称（房间 needUserInfo 为 true 时才会有） | |  | clientId | number | 用户在房间内的唯一标识 | |  | enableToStart | boolean | 是否已做好游戏开始准备（调用过 startGame） | |  | memberExtInfo | string | 游戏自定义的关于成员的扩展信息 | | | | |  | seed | string | 游戏随机种子 | | | | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | roomInfo | Object |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 小游戏 appId | |  | roomIdStr | number | 房间 ID | |  | roomState | number | 房间状态 | |  | | 合法值 | 说明 | | --- | --- | | 1 | 组队中 | | 2 | 该房间的对局游戏已开始 | | 3 | 该房间的对局游戏已结束 | | 4 | 房间已销毁 | | 5 | 房间连接已建立，等待对战连接建立 | | | | |  | maxMemberNum | number | 房间最多可容纳人数 | |  | createTimestamp | number | 创建时间 | |  | updateTimestamp | number | 最近更新时间 | |  | gameTick | number | 游戏下发帧的时间间隔，单位 ms | |  | startPercent | number | 需要满足百分比的玩家都发送了开始指令才能启动游戏。有效范围 0~100，0 表示只要有一个人调用开始就启动，100 表示要求所有人都开始才能启动。 | |  | roomExtInfo | string | 游戏自定义的关于房间的扩展信息 | |  | gameLastTime | number | 游戏对局时长，单位 s | |  | udpReliabilityStrategy | number | UDP可靠性策略， 0：全冗余 N：固定冗余N帧 | |  | memberList | Array.<Object> | 成员列表 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | isReady | boolean | 玩家准备状态 | |  | role | number | 角色 | |  | | 合法值 | 说明 | | --- | --- | | 0 | 普通成员 | | 1 | 房主 | | | | |  | posNum | number | 座位号，从 0 开始 | |  | headimg | string | 头像 URL（房间 needUserInfo 为 true 时才会有） | |  | nickname | string | 用户昵称（房间 needUserInfo 为 true 时才会有） | |  | clientId | number | 用户在房间内的唯一标识 | |  | enableToStart | boolean | 是否已做好游戏开始准备（调用过 startGame） | |  | memberExtInfo | string | 游戏自定义的关于成员的扩展信息 | | | | |  | seed | string | 游戏随机种子 | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | appId | string | 小游戏 appId |
|  | roomIdStr | number | 房间 ID |
|  | roomState | number | 房间状态 |
|  | | 合法值 | 说明 | | --- | --- | | 1 | 组队中 | | 2 | 该房间的对局游戏已开始 | | 3 | 该房间的对局游戏已结束 | | 4 | 房间已销毁 | | 5 | 房间连接已建立，等待对战连接建立 | | | |
|  | maxMemberNum | number | 房间最多可容纳人数 |
|  | createTimestamp | number | 创建时间 |
|  | updateTimestamp | number | 最近更新时间 |
|  | gameTick | number | 游戏下发帧的时间间隔，单位 ms |
|  | startPercent | number | 需要满足百分比的玩家都发送了开始指令才能启动游戏。有效范围 0~100，0 表示只要有一个人调用开始就启动，100 表示要求所有人都开始才能启动。 |
|  | roomExtInfo | string | 游戏自定义的关于房间的扩展信息 |
|  | gameLastTime | number | 游戏对局时长，单位 s |
|  | udpReliabilityStrategy | number | UDP可靠性策略， 0：全冗余 N：固定冗余N帧 |
|  | memberList | Array.<Object> | 成员列表 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | isReady | boolean | 玩家准备状态 | |  | role | number | 角色 | |  | | 合法值 | 说明 | | --- | --- | | 0 | 普通成员 | | 1 | 房主 | | | | |  | posNum | number | 座位号，从 0 开始 | |  | headimg | string | 头像 URL（房间 needUserInfo 为 true 时才会有） | |  | nickname | string | 用户昵称（房间 needUserInfo 为 true 时才会有） | |  | clientId | number | 用户在房间内的唯一标识 | |  | enableToStart | boolean | 是否已做好游戏开始准备（调用过 startGame） | |  | memberExtInfo | string | 游戏自定义的关于成员的扩展信息 | | | |
|  | seed | string | 游戏随机种子 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 1 | 组队中 |
| 2 | 该房间的对局游戏已开始 |
| 3 | 该房间的对局游戏已结束 |
| 4 | 房间已销毁 |
| 5 | 房间连接已建立，等待对战连接建立 |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | isReady | boolean | 玩家准备状态 |
|  | role | number | 角色 |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 普通成员 | | 1 | 房主 | | | |
|  | posNum | number | 座位号，从 0 开始 |
|  | headimg | string | 头像 URL（房间 needUserInfo 为 true 时才会有） |
|  | nickname | string | 用户昵称（房间 needUserInfo 为 true 时才会有） |
|  | clientId | number | 用户在房间内的唯一标识 |
|  | enableToStart | boolean | 是否已做好游戏开始准备（调用过 startGame） |
|  | memberExtInfo | string | 游戏自定义的关于成员的扩展信息 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 0 | 普通成员 |
| 1 | 房主 |

---

### GameServerManager.inviteFriend(object object)

基础库 2.9.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.inviteFriend.html

**object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| openId | string |  | 是 | 被邀请玩家的 openId |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### Promise GameServerManager.joinRoom(object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.joinRoom.html

**object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| accessInfo | string |  | 是 | 游戏房间访问凭证 |
| memberExtInfo | string |  | 否 | 游戏自定义的关于个人的扩展信息，其他人可在 `MemberInfo` 中读取到，最多 32 个字节 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | data | object |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | myPos | number | 加入房间后被分配的座位号 | |  | clientId | number | 用户在房间内的唯一标识 | | | |

**object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | myPos | number | 加入房间后被分配的座位号 |
|  | clientId | number | 用户在房间内的唯一标识 |

---

### Promise GameServerManager.kickoutMember(object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.kickoutMember.html

**object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| kickoutPos | number |  | 是 | 欲踢除的玩家的座位号 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### Promise GameServerManager.login()

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.login.html

---

### Promise GameServerManager.logout()

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.logout.html

---

### Promise GameServerManager.memberLeaveRoom(object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.memberLeaveRoom.html

**object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| accessInfo | string |  | 是 | 游戏房间访问凭证 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### GameServerManager.offBeKickedOut(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.offBeKickedOut.html

---

### GameServerManager.offBroadcast(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.offBroadcast.html

---

### GameServerManager.offDisconnect(function listener)

移除断开连接，收到此事件的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.offDisconnect.html

---

### GameServerManager.offGameEnd(function listener)

移除帧同步游戏结束的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.offGameEnd.html

---

### GameServerManager.offGameStart(function listener)

移除帧同步游戏开始的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.offGameStart.html

---

### GameServerManager.offInvite(function listener)

基础库 2.9.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.offInvite.html

---

### GameServerManager.offLockStepError(function listener)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.offLockStepError.html

---

### GameServerManager.offLogout(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.offLogout.html

---

### GameServerManager.offMatch(function listener)

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.offMatch.html

---

### GameServerManager.offRoomInfoChange(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.offRoomInfoChange.html

---

### GameServerManager.offStateUpdate(function listener)

基础库 2.9.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.offStateUpdate.html

---

### GameServerManager.offSyncFrame(function listener)

移除收到同个房间的帧同步消息的监听函数

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.offSyncFrame.html

---

### GameServerManager.onBeKickedOut(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.onBeKickedOut.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| res | Object |  |

---

### GameServerManager.onBroadcast(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.onBroadcast.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| msg | string | 广播消息 |

---

### GameServerManager.onDisconnect(function listener)

监听断开连接，收到此事件后，需要调用GameServerManager.reconnect进行重连

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.onDisconnect.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | res | Object |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | type | string |  | |  | | 合法值 | 说明 | | --- | --- | | room | 房间服务断开连接，只有在进入房间后有机会收到。房间服务断开连接后，将无法进行房间相关的操作，以及无法收到房间信息变化事件。 | | game | 游戏服务断开连接，只有在游戏开始后有机会收到。游戏服务断开连接后，将无法收发帧。 | | | | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | type | string |  |
|  | | 合法值 | 说明 | | --- | --- | | room | 房间服务断开连接，只有在进入房间后有机会收到。房间服务断开连接后，将无法进行房间相关的操作，以及无法收到房间信息变化事件。 | | game | 游戏服务断开连接，只有在游戏开始后有机会收到。游戏服务断开连接后，将无法收发帧。 | | | |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| room | 房间服务断开连接，只有在进入房间后有机会收到。房间服务断开连接后，将无法进行房间相关的操作，以及无法收到房间信息变化事件。 |
| game | 游戏服务断开连接，只有在游戏开始后有机会收到。游戏服务断开连接后，将无法收发帧。 |

---

### GameServerManager.onGameEnd(function listener)

监听帧同步游戏结束

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.onGameEnd.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| gameAccessInfo | string | 游戏唯一标识，用于后台接口拉取对局记录 |

---

### GameServerManager.onGameStart(function listener)

监听帧同步游戏开始

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.onGameStart.html

---

### GameServerManager.onInvite(function listener)

基础库 2.9.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.onInvite.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| res | Object |  |
| openId | string | 邀请者的 openId |
| data | string | 邀请者附带的额外信息 |

---

### GameServerManager.onLockStepError(function listener)

基础库 2.11.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.onLockStepError.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errCode | number | 错误码 |
| errMsg | string | 错误原因 |

---

### GameServerManager.onLogout(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.onLogout.html

---

### GameServerManager.onMatch(function listener)

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.onMatch.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | res | Object |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | matchId | string | 与 startMatch 一致的 matchId | |  | openId | string | 自己的 openId | |  | roomServiceAccessInfo | string | 房间服务的accessinfo，如果matchid中指定需要匹配完成时创建房间服务，则会携带下来，后续调用房间服务相关接口加入房间即可 | |  | raceId | string | 唯一的本次对局id | |  | groupInfoList | Array.<Object> | 匹配到的队伍信息 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | groupIndex | number | 队伍的序号 | |  | memberInfoList | Array.<Object> | 队伍中成员信息 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | memberIndex | number | 成员的序号 | |  | openId | string | 队伍中成员的openid | |  | nickName | string | 队伍中成员的昵称 | |  | avatarUrl | string | 队伍中成员的头像 | | | | | | | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | matchId | string | 与 startMatch 一致的 matchId |
|  | openId | string | 自己的 openId |
|  | roomServiceAccessInfo | string | 房间服务的accessinfo，如果matchid中指定需要匹配完成时创建房间服务，则会携带下来，后续调用房间服务相关接口加入房间即可 |
|  | raceId | string | 唯一的本次对局id |
|  | groupInfoList | Array.<Object> | 匹配到的队伍信息 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | groupIndex | number | 队伍的序号 | |  | memberInfoList | Array.<Object> | 队伍中成员信息 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | memberIndex | number | 成员的序号 | |  | openId | string | 队伍中成员的openid | |  | nickName | string | 队伍中成员的昵称 | |  | avatarUrl | string | 队伍中成员的头像 | | | | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | groupIndex | number | 队伍的序号 |
|  | memberInfoList | Array.<Object> | 队伍中成员信息 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | memberIndex | number | 成员的序号 | |  | openId | string | 队伍中成员的openid | |  | nickName | string | 队伍中成员的昵称 | |  | avatarUrl | string | 队伍中成员的头像 | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | memberIndex | number | 成员的序号 |
|  | openId | string | 队伍中成员的openid |
|  | nickName | string | 队伍中成员的昵称 |
|  | avatarUrl | string | 队伍中成员的头像 |

---

### GameServerManager.onRoomInfoChange(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.onRoomInfoChange.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | res | Object |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | appId | string | 小游戏 appId | |  | roomIdStr | number | 房间 ID | |  | roomState | number | 房间状态 | |  | | 合法值 | 说明 | | --- | --- | | 1 | 组队中 | | 2 | 该房间的对局游戏已开始 | | 3 | 该房间的对局游戏已结束 | | 4 | 房间已销毁 | | 5 | 房间连接已建立，等待对战连接建立 | | | | |  | maxMemberNum | number | 房间最多可容纳人数 | |  | createTimestamp | number | 创建时间 | |  | updateTimestamp | number | 最近更新时间 | |  | gameTick | number | 游戏下发帧的时间间隔，单位 ms | |  | startPercent | number | 需要满足百分比的玩家都发送了开始指令才能启动游戏。有效范围 0~100，0 表示只要有一个人调用开始就启动，100 表示要求所有人都开始才能启动。 | |  | roomExtInfo | string | 游戏自定义的关于房间的扩展信息 | |  | gameLastTime | number | 游戏对局时长，单位 s | |  | udpReliabilityStrategy | number | UDP可靠性策略， 0：全冗余 N：固定冗余N帧 | |  | memberList | Array.<Object> | 成员列表 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | isReady | boolean | 玩家准备状态 | |  | role | number | 角色 | |  | | 合法值 | 说明 | | --- | --- | | 0 | 普通成员 | | 1 | 房主 | | | | |  | posNum | number | 座位号，从 0 开始 | |  | headimg | string | 头像 URL（房间 needUserInfo 为 true 时才会有） | |  | nickname | string | 用户昵称（房间 needUserInfo 为 true 时才会有） | |  | clientId | number | 用户在房间内的唯一标识 | |  | enableToStart | boolean | 是否已做好游戏开始准备（调用过 startGame） | |  | memberExtInfo | string | 游戏自定义的关于成员的扩展信息 | | | | |  | seed | string | 游戏随机种子 | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | appId | string | 小游戏 appId |
|  | roomIdStr | number | 房间 ID |
|  | roomState | number | 房间状态 |
|  | | 合法值 | 说明 | | --- | --- | | 1 | 组队中 | | 2 | 该房间的对局游戏已开始 | | 3 | 该房间的对局游戏已结束 | | 4 | 房间已销毁 | | 5 | 房间连接已建立，等待对战连接建立 | | | |
|  | maxMemberNum | number | 房间最多可容纳人数 |
|  | createTimestamp | number | 创建时间 |
|  | updateTimestamp | number | 最近更新时间 |
|  | gameTick | number | 游戏下发帧的时间间隔，单位 ms |
|  | startPercent | number | 需要满足百分比的玩家都发送了开始指令才能启动游戏。有效范围 0~100，0 表示只要有一个人调用开始就启动，100 表示要求所有人都开始才能启动。 |
|  | roomExtInfo | string | 游戏自定义的关于房间的扩展信息 |
|  | gameLastTime | number | 游戏对局时长，单位 s |
|  | udpReliabilityStrategy | number | UDP可靠性策略， 0：全冗余 N：固定冗余N帧 |
|  | memberList | Array.<Object> | 成员列表 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | isReady | boolean | 玩家准备状态 | |  | role | number | 角色 | |  | | 合法值 | 说明 | | --- | --- | | 0 | 普通成员 | | 1 | 房主 | | | | |  | posNum | number | 座位号，从 0 开始 | |  | headimg | string | 头像 URL（房间 needUserInfo 为 true 时才会有） | |  | nickname | string | 用户昵称（房间 needUserInfo 为 true 时才会有） | |  | clientId | number | 用户在房间内的唯一标识 | |  | enableToStart | boolean | 是否已做好游戏开始准备（调用过 startGame） | |  | memberExtInfo | string | 游戏自定义的关于成员的扩展信息 | | | |
|  | seed | string | 游戏随机种子 |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| 1 | 组队中 |
| 2 | 该房间的对局游戏已开始 |
| 3 | 该房间的对局游戏已结束 |
| 4 | 房间已销毁 |
| 5 | 房间连接已建立，等待对战连接建立 |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | isReady | boolean | 玩家准备状态 |
|  | role | number | 角色 |
|  | | 合法值 | 说明 | | --- | --- | | 0 | 普通成员 | | 1 | 房主 | | | |
|  | posNum | number | 座位号，从 0 开始 |
|  | headimg | string | 头像 URL（房间 needUserInfo 为 true 时才会有） |
|  | nickname | string | 用户昵称（房间 needUserInfo 为 true 时才会有） |
|  | clientId | number | 用户在房间内的唯一标识 |
|  | enableToStart | boolean | 是否已做好游戏开始准备（调用过 startGame） |
|  | memberExtInfo | string | 游戏自定义的关于成员的扩展信息 |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| 0 | 普通成员 |
| 1 | 房主 |

---

### GameServerManager.onStateUpdate(function listener)

基础库 2.9.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.onStateUpdate.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | res | Object |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | userState | string | 该玩家的自定义状态信息 | |  | sysState | number | 系统状态，0 掉线 1 在线 | |  | openId | string | 好友 openId | | | |

**function listener**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | userState | string | 该玩家的自定义状态信息 |
|  | sysState | number | 系统状态，0 掉线 1 在线 |
|  | openId | string | 好友 openId |

---

### GameServerManager.onSyncFrame(function listener)

监听收到同个房间的帧同步消息

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.onSyncFrame.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| frameId | number | 帧号，从 1 开始递增 |
| actionList | Array.<string>/Array.<ArrayBuffer> | 帧数据列表，如果为空则说明该帧是空帧，每一项的类型与配置项 `lockStepOption.dataType` 一致 |

---

### Promise GameServerManager.ownerLeaveRoom(object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.ownerLeaveRoom.html

**object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| accessInfo | string |  | 是 | 游戏房间访问凭证 |
| assignOwnerToPosNum | boolean |  | 否 | 指定座位号的玩家接任房主角色，优先级高于 assignToMinPosNum |
| assignToMinPosNum | boolean |  | 否 | 自动指定最小座位号玩家作为新房主 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### Promise<ReconnectSuccessRes> GameServerManager.reconnect(object object)

重连游戏服务。如果此时连接并未断开或游戏未开始，会直接成功；如果游戏已开始并且连接已断开，会进行重连，并返回此时服务器的最大帧号。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.reconnect.html

**object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| accessInfo | string |  | 是 | 需要重连的对局房间唯一标识 |

---

### Promise GameServerManager.restart(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.restart.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### boolean GameServerManager.setInviteData(string data)

基础库 2.9.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.setInviteData.html

---

### Promise GameServerManager.setState(object object)

基础库 2.9.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.setState.html

**object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| userState | string |  | 是 | 该玩家的自定义状态信息，长度限制为 256 个字符 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### GameServerManager.startGame(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.startGame.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### Promise GameServerManager.startMatch(object object)

基础库 2.14.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.startMatch.html

**object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| matchId | string |  | 是 | 通过后台接口申请的matchId |
| fillType | number | 0 | 否 | 补充类型，0:自动补充队友 1:不补充队友 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### Promise GameServerManager.startStateService(object object)

基础库 2.9.4 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.startStateService.html

**object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| userState | string |  | 是 | 该玩家的自定义状态信息，长度限制为 256 个字符 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### Promise GameServerManager.updateReadyStatus(object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.updateReadyStatus.html

**object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| accessInfo | string |  | 是 | 游戏房间访问凭证 |
| isReady | boolean |  | 是 | 是否准备完成 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### Promise GameServerManager.uploadFrame(object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/GameServerManager.uploadFrame.html

**object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| actionList | Array.<string>/Array.<ArrayBuffer> |  | 是 | 指令数组，每一项的类型必须与配置项 `lockStepOption.dataType` 一致 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### ReconnectSuccessRes

GameServerManager.reconnect 接口 resolve 后的返回值

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-server-manager/ReconnectSuccessRes.html

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | data | Object |  |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | maxFrameId | Array.<Frame> | 此时服务器的最大帧号。 | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | maxFrameId | Array.<Frame> | 此时服务器的最大帧号。 |

---

<!-- pages: 54 -->
