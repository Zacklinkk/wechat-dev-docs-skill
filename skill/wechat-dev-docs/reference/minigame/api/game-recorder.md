# 微信小游戏 API 结构化参考 — game-recorder

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.operateGameRecorderVideo(Object object)

基础库 2.26.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/wx.operateGameRecorderVideo.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| title | string |  | 否 | 分享的对局回放打开后的标题内容 |
| desc | string |  | 否 | 分享的对局回放打开后的描述内容 |
| query | string |  | 否 | 分享的对局回放打开后跳转小游戏的 query |
| path | string |  | 否 | 分享的对局回放打开后跳转小游戏的 path （独立分包路径） |
| bgm | string |  | 否 | 对局回放背景音乐的地址 |
| timeRange | Array.<Array.<number>> |  | 否 | 对局回放的剪辑区间，是一个二维数组，单位 ms（毫秒）。[[1000, 3000], [4000, 5000]] 表示剪辑已录制对局回放的 1-3 秒和 4-5 秒最终合成为一个 3 秒的对局回放。对局回放剪辑后的总时长最多 60 秒，即 1 分钟 |
| volume | number | 1 | 否 | 对局回放的音量大小，最小0，最大1 |
| atempo | number | 1 | 否 | 对局回放的播放速率，只能设置以下几个值: 0.3, 0.5, 1, 1.5, 2, 2.5, 3.其中1表示元素播放，小于1表示减速播放，大于1表示加速播放 |
| audioMix | boolean | false | 否 | 如果原始视频文件中有音频，是否与新传入的bgm混音，默认为false，表示不混音，只保留一个音轨，值为true时表示原始音频与传入的bgm混音 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### GameRecorder wx.getGameRecorder()

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/wx.getGameRecorder.html

---

### GameRecorderShareButton wx.createGameRecorderShareButton(Object object)

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/wx.createGameRecorderShareButton.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | style | Object |  | 是 | 按钮的样式 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | left | number | 0 | 否 | 左上角横坐标，单位 逻辑像素 | |  | top | number | 0 | 否 | 左上角纵坐标，单位 逻辑像素 | |  | height | number | 40 | 否 | 按钮的高度，最小 40 逻辑像素 | |  | iconMarginRight | number | 8 | 否 | 图标和文本之间的距离，最小 8 逻辑像素 | |  | fontSize | number | 17 | 否 | 文本的字体大小。最小 17，最大 22。 | |  | color | string | #ffffff | 否 | 文本的颜色。 | |  | paddingLeft | number | 16 | 否 | 按钮的左内边距，最小 16 逻辑像素。 | |  | paddingRight | number | 16 | 否 | 按钮的右内边距，最小 16 逻辑像素。 | | | | | |
|  | icon | string |  | 否 | 图标的 url。支持 http/https 开头的网络资源和 wxfile:// 开头的本地资源。如果不设置则使用默认图标。 |
|  | image | string |  | 否 | 按钮的背景图片的 url。支持 http/https 开头的网络资源和 wxfile:// 开头的本地资源。如果不设置则使用默认图标。 |
|  | text | string |  | 否 | 按钮的文本。 |
|  | share | Object |  | 是 | 对局回放的分享参数。 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 | | --- | --- | --- | --- | --- | --- | --- | |  | query | string |  | 否 | 分享的对局回放打开后跳转小游戏的 query。 |  | |  | path | string |  | 否 | 分享的对局回放打开后跳转小游戏的 path （独立分包路径）。详见 [小游戏独立分包指南](../../guide/base-ability/independent-sub-packages.html) | [2.13.2](../../guide/runtime/client-lib/compatibility.html) | |  | bgm | string |  | 是 | 对局回放背景音乐的地址。必须是一个代码包文件路径或者 wxfile:// 文件路径，不支持 http/https 开头的 url。 |  | |  | timeRange | Array.<Array.<number>> |  | 是 | 对局回放的剪辑区间，是一个二维数组，单位 ms（毫秒）。[[1000, 3000], [4000, 5000]] 表示剪辑已录制对局回放的 1-3 秒和 4-5 秒最终合成为一个 3 秒的对局回放。对局回放剪辑后的总时长最多 60 秒，即 1 分钟。 |  | |  | volume | number | 1 | 否 | 对局回放的音量大小，最小 0，最大 1。 | [2.9.2](../../guide/runtime/client-lib/compatibility.html) | |  | atempo | number | 1 | 否 | 对局回放的播放速率，只能设置以下几个值：0.3，0.5，1，1.5，2，2.5，3。其中1表示原速播放，小于1表示减速播放，大于1表示加速播放。 | [2.9.2](../../guide/runtime/client-lib/compatibility.html) | |  | audioMix | boolean | false | 否 | 如果原始视频文件中有音频，是否与新传入的bgm混音，默认为false，表示不混音，只保留一个音轨，值为true时表示原始音频与传入的bgm混音。 | [2.10.0](../../guide/runtime/client-lib/compatibility.html) | | | | | |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | left | number | 0 | 否 | 左上角横坐标，单位 逻辑像素 |
|  | top | number | 0 | 否 | 左上角纵坐标，单位 逻辑像素 |
|  | height | number | 40 | 否 | 按钮的高度，最小 40 逻辑像素 |
|  | iconMarginRight | number | 8 | 否 | 图标和文本之间的距离，最小 8 逻辑像素 |
|  | fontSize | number | 17 | 否 | 文本的字体大小。最小 17，最大 22。 |
|  | color | string | #ffffff | 否 | 文本的颜色。 |
|  | paddingLeft | number | 16 | 否 | 按钮的左内边距，最小 16 逻辑像素。 |
|  | paddingRight | number | 16 | 否 | 按钮的右内边距，最小 16 逻辑像素。 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | query | string |  | 否 | 分享的对局回放打开后跳转小游戏的 query。 |  |
|  | path | string |  | 否 | 分享的对局回放打开后跳转小游戏的 path （独立分包路径）。详见 [小游戏独立分包指南](../../guide/base-ability/independent-sub-packages.html) | [2.13.2](../../guide/runtime/client-lib/compatibility.html) |
|  | bgm | string |  | 是 | 对局回放背景音乐的地址。必须是一个代码包文件路径或者 wxfile:// 文件路径，不支持 http/https 开头的 url。 |  |
|  | timeRange | Array.<Array.<number>> |  | 是 | 对局回放的剪辑区间，是一个二维数组，单位 ms（毫秒）。[[1000, 3000], [4000, 5000]] 表示剪辑已录制对局回放的 1-3 秒和 4-5 秒最终合成为一个 3 秒的对局回放。对局回放剪辑后的总时长最多 60 秒，即 1 分钟。 |  |
|  | volume | number | 1 | 否 | 对局回放的音量大小，最小 0，最大 1。 | [2.9.2](../../guide/runtime/client-lib/compatibility.html) |
|  | atempo | number | 1 | 否 | 对局回放的播放速率，只能设置以下几个值：0.3，0.5，1，1.5，2，2.5，3。其中1表示原速播放，小于1表示减速播放，大于1表示加速播放。 | [2.9.2](../../guide/runtime/client-lib/compatibility.html) |
|  | audioMix | boolean | false | 否 | 如果原始视频文件中有音频，是否与新传入的bgm混音，默认为false，表示不混音，只保留一个音轨，值为true时表示原始音频与传入的bgm混音。 | [2.10.0](../../guide/runtime/client-lib/compatibility.html) |

---

### GameRecorder

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/GameRecorder.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 22002 | unknown error | 未知错误，没有被归纳到的错误 |
| 22012 | internal failed | 游戏画面录制 SDK 内部错误 |
| 22022 | frame not supported | 当前设备不支持录制游戏画面 |
| 22103 | duration invalid | duration 参数不合法 |
| 22113 | bitrate invalid | bitrate 参数不合法 |
| 22123 | fps invalid | fps 参数不合法 |
| 22133 | gop invalid | gop 参数不合法 |
| 22143 | start while already start recording | 在已经开始录制的情况下调用 start |
| 22153 | start while already paused | 在已经暂停录制的情况下调用 start，此时只能调用 resume 恢复录制 |
| 22203 | pause while not start recording | 在还没有开始录制的情况下调用 pause |
| 22213 | pause while already paused | 在已经暂停录制的情况下调用 pause |
| 22303 | resume while not start recording | 在还没有开始录制的情况下调用 resume |
| 22313 | resume while recording | 在录制中调用 resume，调用 resume 只能在暂停状态下 |
| 22403 | abort while not start recording | 在还没有开始录制的情况下调用 abort |
| 22503 | stop while not start recording | 在还没有开始录制的情况下调用 stop |
| 22603 | no recorded video | 在还没有一个录制好的对局回放的情况下发起分享 |
| 22613 | bgm not found | share.bgm 指定的额背景音乐不存在 |
| 22623 | time range invalid | share.timeRange 不合法 |
| 22633 | duration out of limit | share.timeRange 的所有片段的总和超出上限 |
| 22643 | time range too short.It should be longer than 2s | share.timeRange 太短 |

---

### Promise GameRecorder.abort()

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/GameRecorder.abort.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 22002 | unknown error | 未知错误，没有被归纳到的错误 |
| 22012 | internal failed | 游戏画面录制 SDK 内部错误 |
| 22022 | frame not supported | 当前设备不支持录制游戏画面 |
| 22103 | duration invalid | duration 参数不合法 |
| 22113 | bitrate invalid | bitrate 参数不合法 |
| 22123 | fps invalid | fps 参数不合法 |
| 22133 | gop invalid | gop 参数不合法 |
| 22143 | start while already start recording | 在已经开始录制的情况下调用 start |
| 22153 | start while already paused | 在已经暂停录制的情况下调用 start，此时只能调用 resume 恢复录制 |
| 22203 | pause while not start recording | 在还没有开始录制的情况下调用 pause |
| 22213 | pause while already paused | 在已经暂停录制的情况下调用 pause |
| 22303 | resume while not start recording | 在还没有开始录制的情况下调用 resume |
| 22313 | resume while recording | 在录制中调用 resume，调用 resume 只能在暂停状态下 |
| 22403 | abort while not start recording | 在还没有开始录制的情况下调用 abort |
| 22503 | stop while not start recording | 在还没有开始录制的情况下调用 stop |
| 22603 | no recorded video | 在还没有一个录制好的对局回放的情况下发起分享 |
| 22613 | bgm not found | share.bgm 指定的额背景音乐不存在 |
| 22623 | time range invalid | share.timeRange 不合法 |
| 22633 | duration out of limit | share.timeRange 的所有片段的总和超出上限 |
| 22643 | time range too short.It should be longer than 2s | share.timeRange 太短 |

---

### boolean GameRecorder.isAtempoSupported()

基础库 2.10.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/GameRecorder.isAtempoSupported.html

---

### boolean GameRecorder.isFrameSupported()

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/GameRecorder.isFrameSupported.html

---

### boolean GameRecorder.isSoundSupported()

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/GameRecorder.isSoundSupported.html

---

### boolean GameRecorder.isVolumeSupported()

基础库 2.10.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/GameRecorder.isVolumeSupported.html

---

### GameRecorder.off(string event, function callback)

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/GameRecorder.off.html

**string event**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| start | 录制开始事件。当调用 [GameRecorder.start()](GameRecorder.start.html) 且客户端真正开始了对游戏画面录制时触发该事件。 |  |
| stop | 录制结束事件。当调用 [GameRecorder.stop()](GameRecorder.stop.html) 且客户端真正停止了对游戏画面录制时触发该事件。 |  |
| pause | 录制暂停事件。当调用 [GameRecorder.pause()](GameRecorder.pause.html) 且客户端真正暂停了对游戏画面录制时触发该事件。 |  |
| resume | 录制恢复事件。当调用 [GameRecorder.resume()](GameRecorder.resume.html) 且客户端真正恢复了对游戏画面录制时触发该事件。 |  |
| abort | 录制取消事件。当调用 [GameRecorder.abort()](GameRecorder.abort.html) 且客户端真正取消了对游戏画面录制时触发该事件。 |  |
| timeUpdate | 录制时间更新事件。在录制过程中触发该事件。 |  |
| error | 错误事件。当录制和分享过程中发生错误时触发该事件。录制是指当调用 [GameRecorder](GameRecorder.html) 的接口进行录制；分享是指用户点击 [GameRecorderShareButton](GameRecorderShareButton.html) 发起编辑界面并进行分享的过程。 |  |

---

### GameRecorder.on(string event, function callback)

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/GameRecorder.on.html

**string event**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| start | 录制开始事件。当调用 [GameRecorder.start()](GameRecorder.start.html) 且客户端真正开始了对游戏画面录制时触发该事件。 |  |
| stop | 录制结束事件。当调用 [GameRecorder.stop()](GameRecorder.stop.html) 且客户端真正停止了对游戏画面录制时触发该事件。 |  |
| pause | 录制暂停事件。当调用 [GameRecorder.pause()](GameRecorder.pause.html) 且客户端真正暂停了对游戏画面录制时触发该事件。 |  |
| resume | 录制恢复事件。当调用 [GameRecorder.resume()](GameRecorder.resume.html) 且客户端真正恢复了对游戏画面录制时触发该事件。 |  |
| abort | 录制取消事件。当调用 [GameRecorder.abort()](GameRecorder.abort.html) 且客户端真正取消了对游戏画面录制时触发该事件。 |  |
| timeUpdate | 录制时间更新事件。在录制过程中触发该事件。 |  |
| error | 错误事件。当录制和分享过程中发生错误时触发该事件。录制是指当调用 [GameRecorder](GameRecorder.html) 的接口进行录制；分享是指用户点击 [GameRecorderShareButton](GameRecorderShareButton.html) 发起编辑界面并进行分享的过程。 |  |

**事件参数**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| currentTime | number | 当前视频录制到第几秒 |

**事件参数**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| code | number | 错误码 |
| message | string | 错误信息 |

**事件参数**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| duration | number | 视频的时长，单位 ms 毫秒 |

---

### Promise GameRecorder.pause()

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/GameRecorder.pause.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 22002 | unknown error | 未知错误，没有被归纳到的错误 |
| 22012 | internal failed | 游戏画面录制 SDK 内部错误 |
| 22022 | frame not supported | 当前设备不支持录制游戏画面 |
| 22103 | duration invalid | duration 参数不合法 |
| 22113 | bitrate invalid | bitrate 参数不合法 |
| 22123 | fps invalid | fps 参数不合法 |
| 22133 | gop invalid | gop 参数不合法 |
| 22143 | start while already start recording | 在已经开始录制的情况下调用 start |
| 22153 | start while already paused | 在已经暂停录制的情况下调用 start，此时只能调用 resume 恢复录制 |
| 22203 | pause while not start recording | 在还没有开始录制的情况下调用 pause |
| 22213 | pause while already paused | 在已经暂停录制的情况下调用 pause |
| 22303 | resume while not start recording | 在还没有开始录制的情况下调用 resume |
| 22313 | resume while recording | 在录制中调用 resume，调用 resume 只能在暂停状态下 |
| 22403 | abort while not start recording | 在还没有开始录制的情况下调用 abort |
| 22503 | stop while not start recording | 在还没有开始录制的情况下调用 stop |
| 22603 | no recorded video | 在还没有一个录制好的对局回放的情况下发起分享 |
| 22613 | bgm not found | share.bgm 指定的额背景音乐不存在 |
| 22623 | time range invalid | share.timeRange 不合法 |
| 22633 | duration out of limit | share.timeRange 的所有片段的总和超出上限 |
| 22643 | time range too short.It should be longer than 2s | share.timeRange 太短 |

---

### Promise GameRecorder.resume()

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/GameRecorder.resume.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 22002 | unknown error | 未知错误，没有被归纳到的错误 |
| 22012 | internal failed | 游戏画面录制 SDK 内部错误 |
| 22022 | frame not supported | 当前设备不支持录制游戏画面 |
| 22103 | duration invalid | duration 参数不合法 |
| 22113 | bitrate invalid | bitrate 参数不合法 |
| 22123 | fps invalid | fps 参数不合法 |
| 22133 | gop invalid | gop 参数不合法 |
| 22143 | start while already start recording | 在已经开始录制的情况下调用 start |
| 22153 | start while already paused | 在已经暂停录制的情况下调用 start，此时只能调用 resume 恢复录制 |
| 22203 | pause while not start recording | 在还没有开始录制的情况下调用 pause |
| 22213 | pause while already paused | 在已经暂停录制的情况下调用 pause |
| 22303 | resume while not start recording | 在还没有开始录制的情况下调用 resume |
| 22313 | resume while recording | 在录制中调用 resume，调用 resume 只能在暂停状态下 |
| 22403 | abort while not start recording | 在还没有开始录制的情况下调用 abort |
| 22503 | stop while not start recording | 在还没有开始录制的情况下调用 stop |
| 22603 | no recorded video | 在还没有一个录制好的对局回放的情况下发起分享 |
| 22613 | bgm not found | share.bgm 指定的额背景音乐不存在 |
| 22623 | time range invalid | share.timeRange 不合法 |
| 22633 | duration out of limit | share.timeRange 的所有片段的总和超出上限 |
| 22643 | time range too short.It should be longer than 2s | share.timeRange 太短 |

---

### GameRecorder.start(Object object)

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/GameRecorder.start.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| fps | number | 24 | 否 | 视频 fps |  |
| duration | number | 7200 | 否 | 视频的时长限制，单位为秒（s）。最大值 7200，最小值 5，到达指定时长后不会再录入。但还需要手动调用 [GameRecorder.stop()](GameRecorder.stop.html) 来结束录制。 |  |
| bitrate | number | 1000 | 否 | 视频比特率（kbps），默认值1000，最大值 3000，最小值 600 |  |
| gop | number | 12 | 否 | 视频关键帧间隔 |  |
| hookBgm | boolean | true | 否 | 是否录制游戏音效（仅iOS支持） | [2.10.0](../../guide/runtime/client-lib/compatibility.html) |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 22002 | unknown error | 未知错误，没有被归纳到的错误 |
| 22012 | internal failed | 游戏画面录制 SDK 内部错误 |
| 22022 | frame not supported | 当前设备不支持录制游戏画面 |
| 22103 | duration invalid | duration 参数不合法 |
| 22113 | bitrate invalid | bitrate 参数不合法 |
| 22123 | fps invalid | fps 参数不合法 |
| 22133 | gop invalid | gop 参数不合法 |
| 22143 | start while already start recording | 在已经开始录制的情况下调用 start |
| 22153 | start while already paused | 在已经暂停录制的情况下调用 start，此时只能调用 resume 恢复录制 |
| 22203 | pause while not start recording | 在还没有开始录制的情况下调用 pause |
| 22213 | pause while already paused | 在已经暂停录制的情况下调用 pause |
| 22303 | resume while not start recording | 在还没有开始录制的情况下调用 resume |
| 22313 | resume while recording | 在录制中调用 resume，调用 resume 只能在暂停状态下 |
| 22403 | abort while not start recording | 在还没有开始录制的情况下调用 abort |
| 22503 | stop while not start recording | 在还没有开始录制的情况下调用 stop |
| 22603 | no recorded video | 在还没有一个录制好的对局回放的情况下发起分享 |
| 22613 | bgm not found | share.bgm 指定的额背景音乐不存在 |
| 22623 | time range invalid | share.timeRange 不合法 |
| 22633 | duration out of limit | share.timeRange 的所有片段的总和超出上限 |
| 22643 | time range too short.It should be longer than 2s | share.timeRange 太短 |

---

### Promise GameRecorder.stop()

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/GameRecorder.stop.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 22002 | unknown error | 未知错误，没有被归纳到的错误 |
| 22012 | internal failed | 游戏画面录制 SDK 内部错误 |
| 22022 | frame not supported | 当前设备不支持录制游戏画面 |
| 22103 | duration invalid | duration 参数不合法 |
| 22113 | bitrate invalid | bitrate 参数不合法 |
| 22123 | fps invalid | fps 参数不合法 |
| 22133 | gop invalid | gop 参数不合法 |
| 22143 | start while already start recording | 在已经开始录制的情况下调用 start |
| 22153 | start while already paused | 在已经暂停录制的情况下调用 start，此时只能调用 resume 恢复录制 |
| 22203 | pause while not start recording | 在还没有开始录制的情况下调用 pause |
| 22213 | pause while already paused | 在已经暂停录制的情况下调用 pause |
| 22303 | resume while not start recording | 在还没有开始录制的情况下调用 resume |
| 22313 | resume while recording | 在录制中调用 resume，调用 resume 只能在暂停状态下 |
| 22403 | abort while not start recording | 在还没有开始录制的情况下调用 abort |
| 22503 | stop while not start recording | 在还没有开始录制的情况下调用 stop |
| 22603 | no recorded video | 在还没有一个录制好的对局回放的情况下发起分享 |
| 22613 | bgm not found | share.bgm 指定的额背景音乐不存在 |
| 22623 | time range invalid | share.timeRange 不合法 |
| 22633 | duration out of limit | share.timeRange 的所有片段的总和超出上限 |
| 22643 | time range too short.It should be longer than 2s | share.timeRange 太短 |

---

### GameRecorderShareButton

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/GameRecorderShareButton.html

**Object style**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| left | number | 左上角横坐标，单位 逻辑像素 |
| top | number | 左上角纵坐标，单位 逻辑像素 |
| height | number | 按钮的高度，最小 40 逻辑像素 |
| iconMarginRight | number | 图标和文本之间的距离，最小 8 逻辑像素 |
| fontSize | number | 文本的字体大小。最小 17，最大 22。 |
| color | string | 文本的颜色。 |
| paddingLeft | number | 按钮的左内边距，最小 16 逻辑像素。 |
| paddingRight | number | 按钮的右内边距，最小 16 逻辑像素。 |
| backgroundColor | string | 按钮背景颜色，十六进制颜色值，'transparent'为透明背景。 |
| borderRadius | number | 按钮圆角大小，单位为逻辑像素。 |

**Object share**

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| query | string | 分享的对局回放打开后跳转小游戏的 query。 |  |
| path | string | 分享的对局回放打开后跳转小游戏的 path （独立分包路径）。详见 [小游戏独立分包指南](../../guide/base-ability/independent-sub-packages.html) | [2.13.2](../../guide/runtime/client-lib/compatibility.html) |
| bgm | string | 对局回放背景音乐的地址。必须是一个代码包文件路径或者 wxfile:// 文件路径，不支持 http/https 开头的 url。 |  |
| timeRange | Array.<Array.<number>> | 对局回放的剪辑区间，是一个二维数组，单位 ms（毫秒）。[[1000, 3000], [4000, 5000]] 表示剪辑已录制对局回放的 1-3 秒和 4-5 秒最终合成为一个 3 秒的对局回放。对局回放剪辑后的总时长最多 60 秒，即 1 分钟。 |  |
| volume | number | 对局回放的音量大小，最小 0，最大 1。 | [2.9.2](../../guide/runtime/client-lib/compatibility.html) |
| atempo | number | 对局回放的播放速率，只能设置以下几个值：0.3，0.5，1，1.5，2，2.5，3。其中1表示原速播放，小于1表示减速播放，大于1表示加速播放。 | [2.9.2](../../guide/runtime/client-lib/compatibility.html) |
| audioMix | boolean | 如果原始视频文件中有音频，是否与新传入的bgm混音，默认为false，表示不混音，只保留一个音轨，值为true时表示原始音频与传入的bgm混音。 | [2.10.0](../../guide/runtime/client-lib/compatibility.html) |

---

### GameRecorderShareButton.hide()

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/GameRecorderShareButton.hide.html

---

### GameRecorderShareButton.offTap(function listener)

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/GameRecorderShareButton.offTap.html

---

### GameRecorderShareButton.onTap(function listener)

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/GameRecorderShareButton.onTap.html

---

### GameRecorderShareButton.show()

基础库 2.8.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/game-recorder/GameRecorderShareButton.show.html

---

<!-- pages: 20 -->
