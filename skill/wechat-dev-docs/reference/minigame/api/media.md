# 微信小游戏 API 结构化参考 — media

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.setInnerAudioOption(Object object)

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/wx.setInnerAudioOption.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| mixWithOther | boolean | true | 否 | 是否与其他音频混播，设置为 true 之后，不会终止其他应用或微信内的音乐 |
| obeyMuteSwitch | boolean | true | 否 | （仅在 iOS 生效）是否遵循静音开关，设置为 false 之后，即使是在静音模式下，也能播放声音 |
| speakerOn | boolean | true | 否 | true 代表用扬声器播放，false 代表听筒播放，默认值为 true。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.getAvailableAudioSources(Object object)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/wx.getAvailableAudioSources.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | audioSources | Array.<string> | 支持的音频输入源列表，可在 [RecorderManager.start()](../recorder/RecorderManager.start.html) 接口中使用。返回值定义参考 https://developer.android.com/reference/kotlin/android/media/MediaRecorder.AudioSource |
|  | | 合法值 | 说明 | | --- | --- | | auto | 自动设置，默认使用手机麦克风，插上耳麦后自动切换使用耳机麦克风，所有平台适用 | | buildInMic | 手机麦克风，仅限 iOS | | headsetMic | 耳机麦克风，仅限 iOS | | mic | 麦克风（没插耳麦时是手机麦克风，插耳麦时是耳机麦克风），仅限 Android | | camcorder | 同 mic，适用于录制音视频内容，仅限 Android | | voice\_communication | 同 mic，适用于实时沟通，仅限 Android | | voice\_recognition | 同 mic，适用于语音识别，仅限 Android | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| auto | 自动设置，默认使用手机麦克风，插上耳麦后自动切换使用耳机麦克风，所有平台适用 |
| buildInMic | 手机麦克风，仅限 iOS |
| headsetMic | 耳机麦克风，仅限 iOS |
| mic | 麦克风（没插耳麦时是手机麦克风，插耳麦时是耳机麦克风），仅限 Android |
| camcorder | 同 mic，适用于录制音视频内容，仅限 Android |
| voice\_communication | 同 mic，适用于实时沟通，仅限 Android |
| voice\_recognition | 同 mic，适用于语音识别，仅限 Android |

---

### WebAudioContext wx.createWebAudioContext()

基础库 2.19.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/wx.createWebAudioContext.html

---

### MediaAudioPlayer wx.createMediaAudioPlayer()

基础库 2.13.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/wx.createMediaAudioPlayer.html

---

### InnerAudioContext wx.createInnerAudioContext(Object object)

基础库 1.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/wx.createInnerAudioContext.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| useWebAudioImplement | boolean | false | 否 | 是否使用 WebAudio 作为底层音频驱动，默认关闭。对于短音频、播放频繁的音频建议开启此选项，开启后将获得更优的性能表现。由于开启此选项后也会带来一定的内存增长，因此对于长音频建议关闭此选项。 | [2.19.0](../../../guide/runtime/client-lib/compatibility.html) |

---

### AudioBuffer

基础库 2.19.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/AudioBuffer.html

---

### AudioBuffer.copyFromChannel()

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/AudioBuffer.copyFromChannel.html

---

### AudioBuffer.copyToChannel(Float32Array source, number channelNumber, number startInChannel)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/AudioBuffer.copyToChannel.html

---

### Float32Array AudioBuffer.getChannelData(number channel)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/AudioBuffer.getChannelData.html

---

### AudioListener

空间音频监听器，代表在一个音频场景内唯一的位置和方向信息。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/AudioListener.html

---

### AudioParam

基础库 2.19.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/AudioParam.html

---

### BufferSourceNode

音频源节点，通过WebAudioContext.createBufferSource方法获得。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/BufferSourceNode.html

---

### BufferSourceNode.connect(AudioNode|AudioParam destination)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/BufferSourceNode.connect.html

---

### BufferSourceNode.disconnect()

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/BufferSourceNode.disconnect.html

---

### BufferSourceNode.start(number when, number offset, number duration)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/BufferSourceNode.start.html

---

### BufferSourceNode.stop(number when)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/BufferSourceNode.stop.html

---

### InnerAudioContext

InnerAudioContext 实例，可通过wx.createInnerAudioContext接口获取实例。注意，音频播放过程中，可能被系统中断，可通过wx.onAudioInterruptionBegin、wx.onAudioInterruptionEnd事件来处理这种情况。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.html

**支持格式**

| 格式 | iOS | Android |
| --- | --- | --- |
| flac | x | √ |
| m4a | √ | √ |
| ogg | x | √ |
| ape | x | √ |
| amr | x | √ |
| wma | x | √ |
| wav | √ | √ |
| mp3 | √ | √ |
| mp4 | x | √ |
| aac | √ | √ |
| aiff | √ | x |
| caf | √ | x |

---

### InnerAudioContext.destroy()

销毁当前实例

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.destroy.html

---

### InnerAudioContext.offCanplay(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.offCanplay.html

---

### InnerAudioContext.offEnded(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.offEnded.html

---

### InnerAudioContext.offError(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.offError.html

---

### InnerAudioContext.offPause(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.offPause.html

---

### InnerAudioContext.offPlay(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.offPlay.html

---

### InnerAudioContext.offSeeked(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.offSeeked.html

---

### InnerAudioContext.offSeeking(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.offSeeking.html

---

### InnerAudioContext.offStop(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.offStop.html

---

### InnerAudioContext.offTimeUpdate(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.offTimeUpdate.html

---

### InnerAudioContext.offWaiting(function listener)

基础库 1.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.offWaiting.html

---

### InnerAudioContext.onCanplay(function listener)

监听音频进入可以播放状态的事件。但不保证后面可以流畅播放

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.onCanplay.html

---

### InnerAudioContext.onEnded(function listener)

监听音频自然播放至结束的事件

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.onEnded.html

---

### InnerAudioContext.onError(function listener)

监听音频播放错误事件

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.onError.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | errMsg | string |  |
|  | errCode | number |  |
|  | | 合法值 | 说明 | | --- | --- | | 10001 | 系统错误 | | 10002 | 网络错误 | | 10003 | 文件错误 | | 10004 | 格式错误 | | -1 | 未知错误 | | | |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| 10001 | 系统错误 |
| 10002 | 网络错误 |
| 10003 | 文件错误 |
| 10004 | 格式错误 |
| -1 | 未知错误 |

---

### InnerAudioContext.onPause(function listener)

监听音频暂停事件

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.onPause.html

---

### InnerAudioContext.onPlay(function listener)

监听音频播放事件

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.onPlay.html

---

### InnerAudioContext.onSeeked(function listener)

监听音频完成跳转操作的事件

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.onSeeked.html

---

### InnerAudioContext.onSeeking(function listener)

监听音频进行跳转操作的事件

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.onSeeking.html

---

### InnerAudioContext.onStop(function listener)

监听音频停止事件

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.onStop.html

---

### InnerAudioContext.onTimeUpdate(function listener)

监听音频播放进度更新事件

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.onTimeUpdate.html

---

### InnerAudioContext.onWaiting(function listener)

监听音频加载中事件。当音频因为数据不足，需要停下来加载时会触发

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.onWaiting.html

---

### InnerAudioContext.pause()

暂停。暂停后的音频再播放会从暂停处开始播放

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.pause.html

---

### InnerAudioContext.play()

播放

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.play.html

---

### InnerAudioContext.seek(number position)

跳转到指定位置

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.seek.html

---

### InnerAudioContext.stop()

停止。停止后的音频再播放会从头开始播放。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/InnerAudioContext.stop.html

---

### MediaAudioPlayer

MediaAudioPlayer 实例，可通过wx.createMediaAudioPlayer接口获取实例。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/MediaAudioPlayer.html

---

### Promise MediaAudioPlayer.addAudioSource(VideoDecoder source)

添加音频源

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/MediaAudioPlayer.addAudioSource.html

---

### Promise MediaAudioPlayer.destroy()

销毁播放器

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/MediaAudioPlayer.destroy.html

---

### Promise MediaAudioPlayer.removeAudioSource(VideoDecoder source)

移除音频源

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/MediaAudioPlayer.removeAudioSource.html

---

### Promise MediaAudioPlayer.start()

启动播放器

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/MediaAudioPlayer.start.html

---

### Promise MediaAudioPlayer.stop()

停止播放器

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/MediaAudioPlayer.stop.html

---

### WebAudioContext

基础库 2.19.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.html

---

### Promise WebAudioContext.close()

关闭WebAudioContext

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.close.html

---

### AnalyserNode WebAudioContext.createAnalyser()

基础库 2.22.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.createAnalyser.html

---

### BiquadFilterNode WebAudioContext.createBiquadFilter()

创建一个BiquadFilterNode

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.createBiquadFilter.html

---

### AudioBuffer WebAudioContext.createBuffer(number numOfChannels, number length, number sampleRate)

创建一个AudioBuffer，代表着一段驻留在内存中的短音频

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.createBuffer.html

---

### BufferSourceNode WebAudioContext.createBufferSource()

创建一个BufferSourceNode实例，通过AudioBuffer对象来播放音频数据。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.createBufferSource.html

---

### ChannelMergerNode WebAudioContext.createChannelMerger(number numberOfInputs)

创建一个ChannelMergerNode

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.createChannelMerger.html

---

### ChannelSplitterNode WebAudioContext.createChannelSplitter(number numberOfOutputs)

创建一个ChannelSplitterNode

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.createChannelSplitter.html

---

### ConstantSourceNode WebAudioContext.createConstantSource()

创建一个ConstantSourceNode

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.createConstantSource.html

---

### DelayNode WebAudioContext.createDelay(number maxDelayTime)

创建一个DelayNode

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.createDelay.html

---

### DynamicsCompressorNode WebAudioContext.createDynamicsCompressor()

创建一个DynamicsCompressorNode

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.createDynamicsCompressor.html

---

### GainNode WebAudioContext.createGain()

创建一个GainNode

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.createGain.html

---

### IIRFilterNode WebAudioContext.createIIRFilter(Array.<number> feedforward, Array.<number> feedback)

创建一个IIRFilterNode

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.createIIRFilter.html

---

### OscillatorNode WebAudioContext.createOscillator()

创建一个OscillatorNode

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.createOscillator.html

---

### PannerNode WebAudioContext.createPanner()

创建一个PannerNode

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.createPanner.html

---

### PeriodicWaveNode WebAudioContext.createPeriodicWave(Float32Array real, Float32Array imag, object constraints)

创建一个PeriodicWaveNode

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.createPeriodicWave.html

**object constraints**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| disableNormalization | boolean |  | 否 | 如果指定为true则禁用标准化，默认为false |

---

### ScriptProcessorNode WebAudioContext.createScriptProcessor(number bufferSize, number numberOfInputChannels, number numberOfOutputChannels)

创建一个ScriptProcessorNode

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.createScriptProcessor.html

---

### WaveShaperNode WebAudioContext.createWaveShaper()

创建一个WaveShaperNode

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.createWaveShaper.html

---

### AudioBuffer WebAudioContext.decodeAudioData(ArrayBuffer audioData, function successCallback, function errorCallback)

异步解码一段资源为AudioBuffer。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.decodeAudioData.html

---

### Promise WebAudioContext.resume()

同步恢复已经被暂停的WebAudioContext上下文

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.resume.html

---

### Promise WebAudioContext.suspend()

同步暂停WebAudioContext上下文

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContext.suspend.html

---

### WebAudioContextNode

一类音频处理模块，不同的Node具备不同的功能，如GainNode(音量调整)等。一个WebAudioContextNode可以通过上下文来创建。 目前已经支持以下Node： IIRFilterNode WaveShaperNode ConstantSourceNode ChannelMergerNode OscillatorNode GainNode BiquadFilterNode PeriodicWaveNode BufferSourceNode ChannelSplitterNode ChannelMergerNode DelayNode DynamicsCompressorNode ScriptProcessorNode PannerNode AnalyserNode

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/audio/WebAudioContextNode.html

---

### wx.saveImageToPhotosAlbum(Object object)

基础库 1.2.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/image/wx.saveImageToPhotosAlbum.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| filePath | string |  | 是 | 图片文件路径，可以是临时文件路径或永久文件路径 (本地路径) ，不支持网络路径 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### wx.previewMedia(Object object)

基础库 2.12.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/image/wx.previewMedia.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | sources | Array.<Object> |  | 是 | 需要预览的资源列表 |  |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | url | String |  | 是 | 图片或视频的地址 | |  | type | String | image | 否 | 资源的类型，默认为图片 | |  | | 合法值 | 说明 | | --- | --- | | image | 图片 | | video | 视频 | | | | | | |  | poster | string |  | 否 | 视频的封面图片 | | | | | | |
|  | current | number | 0 | 否 | 当前显示的资源序号 |  |
|  | showmenu | boolean | true | 否 | 是否显示长按菜单。 | [2.13.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | referrerPolicy | string | no-referrer | 否 | `origin`: 发送完整的referrer; `no-referrer`: 不发送。格式固定为 `https://servicewechat.com/{appid}/{version}/page-frame.html`，其中 {appid} 为小程序的 appid，{version} 为小程序的版本号，版本号为 0 表示为开发版、体验版以及审核版本，版本号为 devtools 表示为开发者工具，其余为正式版本； | [2.13.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | url | String |  | 是 | 图片或视频的地址 |
|  | type | String | image | 否 | 资源的类型，默认为图片 |
|  | | 合法值 | 说明 | | --- | --- | | image | 图片 | | video | 视频 | | | | | |
|  | poster | string |  | 否 | 视频的封面图片 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| image | 图片 |
| video | 视频 |

**支持长按识别的码**

| 类型 | 说明 | 最低版本 |
| --- | --- | --- |
| 小程序码 |  |  |
| 微信个人码 | 不支持小游戏 | [2.18.0](../../../guide/runtime/client-lib/compatibility.html) |
| 企业微信个人码 | 不支持小游戏 | [2.18.0](../../../guide/runtime/client-lib/compatibility.html) |
| 普通群码 | 指仅包含微信用户的群，不支持小游戏 | [2.18.0](../../../guide/runtime/client-lib/compatibility.html) |
| 互通群码 | 指既有微信用户也有企业微信用户的群，不支持小游戏 | [2.18.0](../../../guide/runtime/client-lib/compatibility.html) |
| 公众号二维码 | 不支持小游戏 | [2.18.0](../../../guide/runtime/client-lib/compatibility.html) |

---

### wx.previewImage(Object object)

以Promise 风格调用：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/image/wx.previewImage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| urls | Array.<string> |  | 是 | 需要预览的图片链接列表。[2.2.3](../../../guide/runtime/client-lib/compatibility.html) 起支持云文件ID。 |  |
| showmenu | boolean | true | 否 | 是否显示长按菜单。 | [2.13.0](../../../guide/runtime/client-lib/compatibility.html) |
| current | string | urls 的第一张 | 否 | 当前显示图片的链接 |  |
| referrerPolicy | string | no-referrer | 否 | `origin`: 发送完整的referrer; `no-referrer`: 不发送。格式固定为 `https://servicewechat.com/{appid}/{version}/page-frame.html`，其中 {appid} 为小程序的 appid，{version} 为小程序的版本号，版本号为 0 表示为开发版、体验版以及审核版本，版本号为 devtools 表示为开发者工具，其余为正式版本； | [2.13.0](../../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**支持长按识别的码**

| 类型 | 说明 | 最低版本 |
| --- | --- | --- |
| 小程序码 |  |  |
| 微信个人码 |  | [2.18.0](../../../guide/runtime/client-lib/compatibility.html) |
| 企业微信个人码 |  | [2.18.0](../../../guide/runtime/client-lib/compatibility.html) |
| 普通群码 | 指仅包含微信用户的群 | [2.18.0](../../../guide/runtime/client-lib/compatibility.html) |
| 互通群码 | 指既有微信用户也有企业微信用户的群 | [2.18.0](../../../guide/runtime/client-lib/compatibility.html) |
| 公众号二维码 |  | [2.18.0](../../../guide/runtime/client-lib/compatibility.html) |

---

### wx.compressImage(Object object)

基础库 3.0.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/image/wx.compressImage.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| src | string |  | 是 | 图片路径，图片的路径，支持本地路径、代码包路径 |  |
| quality | number | 80 | 否 | 压缩质量，范围0～100，数值越小，质量越低，压缩率越高（仅对jpg有效）。 |  |
| compressedWidth | number |  | 否 | 压缩后图片的宽度，单位为px，若不填写则默认以compressedHeight为准等比缩放。 | [2.26.0](../../../guide/runtime/client-lib/compatibility.html) |
| compressedHeight | number |  | 否 | 压缩后图片的高度，单位为px，若不填写则默认以compressedWidth为准等比缩放 | [2.26.0](../../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempFilePath | string | 压缩后图片的临时文件路径 (本地路径) |

---

### wx.chooseMessageFile(Object object)

基础库 2.23.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/image/wx.chooseMessageFile.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | count | number |  | 是 | 最多可以选择的文件个数，可以 0～100 |  |
|  | type | string | 'all' | 否 | 所选的文件的类型 |  |
|  | | 合法值 | 说明 | | --- | --- | | all | 从所有文件选择 | | video | 只能选择视频文件 | | image | 只能选择图片文件 | | file | 可以选择除了图片和视频之外的其它的文件 | | | | | | |
|  | extension | Array.<string> |  | 否 | 根据文件拓展名过滤，仅 type==file 时有效。每一项都不能是空字符串。默认不过滤。 | [2.6.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| all | 从所有文件选择 |
| video | 只能选择视频文件 |
| image | 只能选择图片文件 |
| file | 可以选择除了图片和视频之外的其它的文件 |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | tempFiles | Array.<Object> | 返回选择的文件的本地临时文件对象数组 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | path | string | 本地临时文件路径 (本地路径) | |  | size | number | 本地临时文件大小，单位 B | |  | name | string | 选择的文件名称 | |  | type | string | 选择的文件类型 | |  | | 合法值 | 说明 | | --- | --- | | video | 选择了视频文件 | | image | 选择了图片文件 | | file | 选择了除图片和视频的文件 | | | | |  | time | number | 选择的文件的会话发送时间，Unix时间戳，工具暂不支持此属性 | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | path | string | 本地临时文件路径 (本地路径) |
|  | size | number | 本地临时文件大小，单位 B |
|  | name | string | 选择的文件名称 |
|  | type | string | 选择的文件类型 |
|  | | 合法值 | 说明 | | --- | --- | | video | 选择了视频文件 | | image | 选择了图片文件 | | file | 选择了除图片和视频的文件 | | | |
|  | time | number | 选择的文件的会话发送时间，Unix时间戳，工具暂不支持此属性 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| video | 选择了视频文件 |
| image | 选择了图片文件 |
| file | 选择了除图片和视频的文件 |

---

### wx.chooseImage(Object object)

从基础库2.21.0开始，本接口停止维护，请使用wx.chooseMedia代替

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/image/wx.chooseImage.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | count | number | 9 | 否 | 最多可以选择的图片张数 |
|  | sizeType | Array.<string> | ['original', 'compressed'] | 否 | 所选的图片的尺寸 |
|  | | 合法值 | 说明 | | --- | --- | | original | 原图 | | compressed | 压缩图 | | | | | |
|  | sourceType | Array.<string> | ['album', 'camera'] | 否 | 选择图片的来源 |
|  | | 合法值 | 说明 | | --- | --- | | album | 从相册选图 | | camera | 使用相机 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| original | 原图 |
| compressed | 压缩图 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| album | 从相册选图 |
| camera | 使用相机 |

**Object object**

|  | 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- |
|  | tempFilePaths | Array.<string> | 图片的本地临时文件路径列表 (本地路径) |  |
|  | tempFiles | Array.<Object> | 图片的本地临时文件列表 | [1.2.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | path | string | 本地临时文件路径 (本地路径) | |  | size | number | 本地临时文件大小，单位 B | | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | path | string | 本地临时文件路径 (本地路径) |
|  | size | number | 本地临时文件大小，单位 B |

---

### RecorderManager wx.getRecorderManager()

基础库 1.6.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/recorder/wx.getRecorderManager.html

---

### RecorderManager

全局唯一的录音管理器

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/recorder/RecorderManager.html

---

### RecorderManager.onError(function listener)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/recorder/RecorderManager.onError.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |

---

### RecorderManager.onFrameRecorded(function listener)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/recorder/RecorderManager.onFrameRecorded.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| frameBuffer | ArrayBuffer | 录音分片数据 |
| isLastFrame | boolean | 当前帧是否正常录音结束前的最后一帧 |

---

### RecorderManager.onInterruptionBegin(function listener)

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/recorder/RecorderManager.onInterruptionBegin.html

---

### RecorderManager.onInterruptionEnd(function listener)

基础库 2.3.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/recorder/RecorderManager.onInterruptionEnd.html

---

### RecorderManager.onPause(function listener)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/recorder/RecorderManager.onPause.html

---

### RecorderManager.onResume(function listener)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/recorder/RecorderManager.onResume.html

---

### RecorderManager.onStart(function listener)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/recorder/RecorderManager.onStart.html

---

### RecorderManager.onStop(function listener)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/recorder/RecorderManager.onStop.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempFilePath | string | 录音文件的临时路径 (本地路径) |
| duration | number | 录音总时长，单位：ms |
| fileSize | number | 录音文件大小，单位：Byte |

---

### RecorderManager.pause()

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/recorder/RecorderManager.pause.html

---

### RecorderManager.resume()

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/recorder/RecorderManager.resume.html

---

### RecorderManager.start(Object object)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/recorder/RecorderManager.start.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | duration | number | 60000 | 否 | 录音的时长，单位 ms，最大值 600000（10 分钟） |  |
|  | sampleRate | number | 8000 | 否 | 采样率（pc不支持） |  |
|  | | 合法值 | 说明 | | --- | --- | | 8000 | 8000 采样率 | | 11025 | 11025 采样率 | | 12000 | 12000 采样率 | | 16000 | 16000 采样率 | | 22050 | 22050 采样率 | | 24000 | 24000 采样率 | | 32000 | 32000 采样率 | | 44100 | 44100 采样率 | | 48000 | 48000 采样率 | | | | | | |
|  | numberOfChannels | number | 2 | 否 | 录音通道数 |  |
|  | | 合法值 | 说明 | | --- | --- | | 1 | 1 个通道 | | 2 | 2 个通道 | | | | | | |
|  | encodeBitRate | number | 48000 | 否 | 编码码率，有效值见下表格 |  |
|  | format | string | aac | 否 | 音频格式 |  |
|  | | 合法值 | 说明 | | --- | --- | | mp3 | mp3 格式 | | aac | aac 格式 | | wav | wav 格式 | | PCM | pcm 格式 | | | | | | |
|  | frameSize | number |  | 否 | 指定帧大小，单位 KB。传入 frameSize 后，每录制指定帧大小的内容后，会回调录制的文件内容，不指定则不会回调。暂仅支持 mp3、pcm 格式。 |  |
|  | audioSource | string | auto | 否 | 指定录音的音频输入源，可通过 [wx.getAvailableAudioSources()](../audio/wx.getAvailableAudioSources.html) 获取当前可用的音频源 | [2.1.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | | 合法值 | 说明 | | --- | --- | | auto | 自动设置，默认使用手机麦克风，插上耳麦后自动切换使用耳机麦克风，所有平台适用 | | buildInMic | 手机麦克风，仅限 iOS | | headsetMic | 有线耳机麦克风，仅限 iOS | | mic | 麦克风（没插耳麦时是手机麦克风，插耳麦时是耳机麦克风），仅限 Android | | camcorder | 同 mic，适用于录制音视频内容，仅限 Android | | voice\_communication | 同 mic，适用于实时沟通，仅限 Android | | voice\_recognition | 同 mic，适用于语音识别，仅限 Android | | | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 8000 | 8000 采样率 |
| 11025 | 11025 采样率 |
| 12000 | 12000 采样率 |
| 16000 | 16000 采样率 |
| 22050 | 22050 采样率 |
| 24000 | 24000 采样率 |
| 32000 | 32000 采样率 |
| 44100 | 44100 采样率 |
| 48000 | 48000 采样率 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| 1 | 1 个通道 |
| 2 | 2 个通道 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| mp3 | mp3 格式 |
| aac | aac 格式 |
| wav | wav 格式 |
| PCM | pcm 格式 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| auto | 自动设置，默认使用手机麦克风，插上耳麦后自动切换使用耳机麦克风，所有平台适用 |
| buildInMic | 手机麦克风，仅限 iOS |
| headsetMic | 有线耳机麦克风，仅限 iOS |
| mic | 麦克风（没插耳麦时是手机麦克风，插耳麦时是耳机麦克风），仅限 Android |
| camcorder | 同 mic，适用于录制音视频内容，仅限 Android |
| voice\_communication | 同 mic，适用于实时沟通，仅限 Android |
| voice\_recognition | 同 mic，适用于语音识别，仅限 Android |

**采样率与编码码率限制**

| 采样率 | 编码码率 |
| --- | --- |
| 8000 | 16000 ~ 48000 |
| 11025 | 16000 ~ 48000 |
| 12000 | 24000 ~ 64000 |
| 16000 | 24000 ~ 96000 |
| 22050 | 32000 ~ 128000 |
| 24000 | 32000 ~ 128000 |
| 32000 | 48000 ~ 192000 |
| 44100 | 64000 ~ 320000 |
| 48000 | 64000 ~ 320000 |

---

### RecorderManager.stop()

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/recorder/RecorderManager.stop.html

---

### Video wx.createVideo(Object object)

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/wx.createVideo.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | x | number | 0 | 否 | 视频的左上角横坐标 |  |
|  | y | number | 0 | 否 | 视频的左上角纵坐标 |  |
|  | width | number | 300 | 否 | 视频的宽度 |  |
|  | height | number | 150 | 否 | 视频的高度 |  |
|  | src | string |  | 是 | 视频的资源地址 |  |
|  | poster | string |  | 否 | 视频的封面 |  |
|  | initialTime | number | 0 | 否 | 视频的初始播放位置，单位为 s 秒 |  |
|  | playbackRate | number | 1.0 | 否 | 视频的播放速率，有效值有 0.5、0.8、1.0、1.25、1.5 |  |
|  | live | boolean | false | 否 | 视频是否为直播 |  |
|  | objectFit | string | 'contain' | 否 | 视频的缩放模式 |  |
|  | | 合法值 | 说明 | | --- | --- | | fill | 填充，视频拉伸填满整个容器，不保证保持原有长宽比例 | | contain | 包含，保持原有长宽比例。保证视频尺寸一定可以在容器里面放得下。因此，可能会有部分空白 | | cover | 覆盖，保持原有长宽比例。保证视频尺寸一定大于容器尺寸，宽度和高度至少有一个和容器一致。因此，视频有部分会看不见 | | | | | | |
|  | controls | boolean | true | 否 | 视频是否显示控件 |  |
|  | showProgress | boolean | true | 否 | 是否显示视频底部进度条 | [2.12.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | showProgressInControlMode | boolean | true | 否 | 是否显示控制栏的进度条 | [2.12.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | backgroundColor | string | '#000000' | 否 | 视频背景颜色 | [2.12.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | autoplay | boolean | false | 否 | 视频是否自动播放 |  |
|  | loop | boolean | false | 否 | 视频是否是否循环播放 |  |
|  | muted | boolean | false | 否 | 视频是否禁音播放 |  |
|  | obeyMuteSwitch | boolean | false | 否 | 视频是否遵循系统静音开关设置（仅iOS） | [2.4.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | enableProgressGesture | boolean | true | 否 | 是否启用手势控制播放进度 |  |
|  | enablePlayGesture | boolean | false | 否 | 是否开启双击播放的手势 |  |
|  | showCenterPlayBtn | boolean | true | 否 | 是否显示视频中央的播放按钮 |  |
|  | underGameView | boolean | false | 否 | 视频是否显示在游戏画布之下（配合 Canvas.getContext('webgl', {alpha: true}) 使主屏canvas实现透明效果） | [2.11.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | autoPauseIfNavigate | boolean | true | 否 | 视频跳转后自动暂停播放 |  |
|  | autoPauseIfOpenNative | boolean | true | 否 | 视频跳转原生页后自动暂停播放 |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| fill | 填充，视频拉伸填满整个容器，不保证保持原有长宽比例 |
| contain | 包含，保持原有长宽比例。保证视频尺寸一定可以在容器里面放得下。因此，可能会有部分空白 |
| cover | 覆盖，保持原有长宽比例。保证视频尺寸一定大于容器尺寸，宽度和高度至少有一个和容器一致。因此，视频有部分会看不见 |

---

### wx.chooseMedia(Object object)

基础库 2.23.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/wx.chooseMedia.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | count | number | 9 | 否 | 最多可以选择的文件个数，基础库2.25.0前，最多可支持9个文件，2.25.0及以后最多可支持20个文件 |
|  | mediaType | Array.<string> | ['image', 'video'] | 否 | 文件类型 |
|  | | 合法值 | 说明 | | --- | --- | | image | 只能拍摄图片或从相册选择图片 | | video | 只能拍摄视频或从相册选择视频 | | mix | 可同时选择图片和视频 | | | | | |
|  | sourceType | Array.<string> | ['album', 'camera'] | 否 | 图片和视频选择的来源 |
|  | | 合法值 | 说明 | | --- | --- | | album | 从相册选择 | | camera | 使用相机拍摄 | | | | | |
|  | maxDuration | number | 10 | 否 | 拍摄视频最长拍摄时间，单位秒。时间范围为 3s 至 60s 之间。不限制相册。 |
|  | sizeType | Array.<string> | ['original', 'compressed'] | 否 | 是否压缩所选文件，基础库2.25.0前仅对 mediaType 为 image 时有效，2.25.0及以后对全量 mediaType 有效 |
|  | camera | string | 'back' | 否 | 仅在 sourceType 为 camera 时生效，使用前置或后置摄像头 |
|  | | 合法值 | 说明 | | --- | --- | | back | 使用后置摄像头 | | front | 使用前置摄像头 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| image | 只能拍摄图片或从相册选择图片 |
| video | 只能拍摄视频或从相册选择视频 |
| mix | 可同时选择图片和视频 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| album | 从相册选择 |
| camera | 使用相机拍摄 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| back | 使用后置摄像头 |
| front | 使用前置摄像头 |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | tempFiles | Array.<Object> | 本地临时文件列表 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | tempFilePath | string | 本地临时文件路径 (本地路径) | |  | size | number | 本地临时文件大小，单位 B | |  | duration | number | 视频的时间长度 | |  | height | number | 视频的高度 | |  | width | number | 视频的宽度 | |  | thumbTempFilePath | string | 视频缩略图临时文件路径 | |  | fileType | string | 文件类型 | |  | | 合法值 | 说明 | | --- | --- | | image | 图片 | | video | 视频 | | | | | | |
|  | type | string | 文件类型，有效值有 image 、video、mix |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | tempFilePath | string | 本地临时文件路径 (本地路径) |
|  | size | number | 本地临时文件大小，单位 B |
|  | duration | number | 视频的时间长度 |
|  | height | number | 视频的高度 |
|  | width | number | 视频的宽度 |
|  | thumbTempFilePath | string | 视频缩略图临时文件路径 |
|  | fileType | string | 文件类型 |
|  | | 合法值 | 说明 | | --- | --- | | image | 图片 | | video | 视频 | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| image | 图片 |
| video | 视频 |

---

### Video

视频对象

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.html

---

### Video.destroy()

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.destroy.html

---

### Promise Video.exitFullScreen()

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.exitFullScreen.html

---

### Video.offEnded(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.offEnded.html

---

### Video.offError(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.offError.html

---

### Video.offPause(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.offPause.html

---

### Video.offPlay(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.offPlay.html

---

### Video.offProgress(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.offProgress.html

---

### Video.offTimeUpdate(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.offTimeUpdate.html

---

### Video.offWaiting(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.offWaiting.html

---

### Video.onEnded(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.onEnded.html

---

### Video.onError(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.onError.html

**function listener**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | errMsg | string | 错误信息 |
|  | | 合法值 | 说明 | | --- | --- | | MEDIA\_ERR\_NETWORK | 当下载时发生错误 | | MEDIA\_ERR\_DECODE | 当解码时发生错误 | | MEDIA\_ERR\_SRC\_NOT\_SUPPORTED | video 的 src 属性是不支持的资源类型 | | | |

**function listener**

| 合法值 | 说明 |
| --- | --- |
| MEDIA\_ERR\_NETWORK | 当下载时发生错误 |
| MEDIA\_ERR\_DECODE | 当解码时发生错误 |
| MEDIA\_ERR\_SRC\_NOT\_SUPPORTED | video 的 src 属性是不支持的资源类型 |

---

### Video.onPause(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.onPause.html

---

### Video.onPlay(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.onPlay.html

---

### Video.onProgress(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.onProgress.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| buffered | number | 当前的缓冲进度，缓冲进度区间为 (0~100]，100表示缓冲完成 |
| duration | number | 视频的总时长，单位为秒 |

---

### Video.onTimeUpdate(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.onTimeUpdate.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| position | number | 当前的播放位置，单位为秒 |
| duration | number | 视频的总时长，单位为秒 |

---

### Video.onWaiting(function listener)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.onWaiting.html

---

### Promise Video.pause()

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.pause.html

---

### Promise Video.play()

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.play.html

---

### Promise Video.requestFullScreen(number direction)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.requestFullScreen.html

**number direction**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 0 | 正常竖向 |  |
| 90 | 屏幕逆时针90度 |  |
| -90 | 屏幕顺时针90度 |  |

---

### Promise Video.seek(number time)

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.seek.html

---

### Promise Video.stop()

微信 鸿蒙 OS 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video/Video.stop.html

---

### Camera wx.createCamera(Object object)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/camera/wx.createCamera.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 0 | 否 | 相机的左上角横坐标 |
| y | number | 0 | 否 | 相机的左上角纵坐标 |
| width | number | 300 | 否 | 相机的宽度 |
| height | number | 150 | 否 | 相机的高度 |
| devicePosition | string | back | 否 | 摄像头朝向，值为 front, back |
| flash | string | auto | 否 | 闪光灯，值为 auto, on, off |
| size | string | small | 否 | 帧数据图像尺寸，值为 small, medium, large |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### Camera

相机对象

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/camera/Camera.html

---

### Camera.closeFrameChange()

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/camera/Camera.closeFrameChange.html

---

### Camera.destroy()

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/camera/Camera.destroy.html

---

### Camera.listenFrameChange(Worker worker)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/camera/Camera.listenFrameChange.html

---

### Camera.onAuthCancel(function callback)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/camera/Camera.onAuthCancel.html

---

### Camera.onCameraFrame(function callback)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/camera/Camera.onCameraFrame.html

**function callback**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 图像数据矩形的宽度 |
| height | number | 图像数据矩形的高度 |
| data | ArrayBuffer | 图像像素点数据，一维数组，每四项表示一个像素点的 rgba |

---

### Camera.onStop(function callback)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/camera/Camera.onStop.html

---

### Promise Camera.setZoom(Object args)

基础库 3.9.2 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/camera/Camera.setZoom.html

**Object args**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| zoom | number |  | 是 | 缩放级别，范围 [1, maxZoom]。zoom 可取小数，精确到小数后一位。maxZoom 可在 bindinitdone 返回值中获取。 |

---

### Promise Camera.startRecord()

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/camera/Camera.startRecord.html

---

### Promise Camera.stopRecord(boolean compressed)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/camera/Camera.stopRecord.html

---

### Promise Camera.takePhoto(string quality)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/camera/Camera.takePhoto.html

---

### VideoDecoder wx.createVideoDecoder()

基础库 2.11.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video-decoder/wx.createVideoDecoder.html

---

### VideoDecoder

基础库 2.11.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video-decoder/VideoDecoder.html

---

### Object VideoDecoder.getFrameData()

基础库 2.11.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video-decoder/VideoDecoder.getFrameData.html

**Object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 帧数据宽度 |
| height | number | 帧数据高度 |
| data | ArrayBuffer | 帧数据 |
| pkPts | number | 帧原始 pts |
| pkDts | number | 帧原始 dts |

---

### VideoDecoder.off(string eventName, function callback)

基础库 2.11.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video-decoder/VideoDecoder.off.html

---

### VideoDecoder.on(string eventName, function callback)

基础库 2.11.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video-decoder/VideoDecoder.on.html

**string eventName**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| start | 开始事件。返回 {width, height} |  |
| stop | 结束事件。 |  |
| seek | seek 完成事件。 |  |
| bufferchange | 缓冲区变化事件。 |  |
| ended | 解码结束事件。 |  |

---

### Promise VideoDecoder.remove()

基础库 2.11.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video-decoder/VideoDecoder.remove.html

---

### Promise VideoDecoder.seek(number position)

基础库 2.11.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video-decoder/VideoDecoder.seek.html

---

### Promise VideoDecoder.start(Object object)

基础库 2.11.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video-decoder/VideoDecoder.start.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| source | string |  | 是 | 需要解码的视频源文件。基础库 2.13.0 以下的版本只支持本地路径。 2.13.0 开始支持 http:// 和 https:// 协议的远程路径。 |  |
| mode | number | 1 | 否 | 解码模式。0：按 pts 解码；1：以最快速度解码 |  |
| abortAudio | boolean | false | 否 | 是否不需要音频轨道 | [2.15.0](../../../guide/runtime/client-lib/compatibility.html) |
| abortVideo | boolean | false | 否 | 是否不需要视频轨道 | [2.15.0](../../../guide/runtime/client-lib/compatibility.html) |

---

### Promise VideoDecoder.stop()

基础库 2.11.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/video-decoder/VideoDecoder.stop.html

---

### wx.updateVoIPChatMuteConfig(Object object)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/voip/wx.updateVoIPChatMuteConfig.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | muteConfig | Object |  | 是 | 静音设置 |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | muteMicrophone | Boolean | false | 否 | 是否静音麦克风 | |  | muteEarphone | Boolean | false | 否 | 是否静音耳机 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | muteMicrophone | Boolean | false | 否 | 是否静音麦克风 |
|  | muteEarphone | Boolean | false | 否 | 是否静音耳机 |

---

### wx.onVoIPChatStateChanged(function listener)

基础库 2.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/voip/wx.onVoIPChatStateChanged.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| code | Number | 事件码 |
| data | object | 附加信息 |
| errCode | Number | 错误码 |
| errMsg | String | 调用结果 |

---

### wx.onVoIPChatSpeakersChanged(function listener)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/voip/wx.onVoIPChatSpeakersChanged.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| openIdList | Array.<String> | 还在实时语音通话中的成员 openId 名单 |
| errCode | Number | 错误码 |
| errMsg | String | 调用结果（错误原因） |

---

### wx.onVoIPChatMembersChanged(function listener)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/voip/wx.onVoIPChatMembersChanged.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| openIdList | Array.<String> | 还在实时语音通话中的成员 openId 名单 |
| errCode | Number | 错误码 |
| errMsg | String | 调用结果 |

---

### wx.onVoIPChatInterrupted(function listener)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/voip/wx.onVoIPChatInterrupted.html

**function listener**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errCode | Number | 错误码 |
| errMsg | String | 调用结果（错误原因） |

---

### wx.offVoIPChatStateChanged(function listener)

基础库 2.16.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/voip/wx.offVoIPChatStateChanged.html

---

### wx.offVoIPChatSpeakersChanged(function listener)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/voip/wx.offVoIPChatSpeakersChanged.html

---

### wx.offVoIPChatMembersChanged(function listener)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/voip/wx.offVoIPChatMembersChanged.html

---

### wx.offVoIPChatInterrupted(function listener)

基础库 2.9.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/voip/wx.offVoIPChatInterrupted.html

---

### wx.joinVoIPChat(Object object)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/voip/wx.joinVoIPChat.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | roomType | String | voice | 否 | 房间类型 |  |
|  | | 合法值 | 说明 | | --- | --- | | voice | 音频房间，用于语音通话 | | video | 视频房间，结合 [voip-room](errorvoip-room)) 组件可显示成员画面 | | | | | | |
|  | signature | String |  | 是 | 签名，用于验证小游戏的身份 |  |
|  | nonceStr | String |  | 是 | 验证所需的随机字符串 |  |
|  | timeStamp | Number |  | 是 | 验证所需的时间戳 |  |
|  | groupId | String |  | 是 | 小游戏内此房间/群聊的 ID。同一时刻传入相同 groupId 的用户会进入到同个实时语音房间。 |  |
|  | muteConfig | Object |  | 否 | 静音设置 |  |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | muteMicrophone | Boolean | false | 否 | 是否静音麦克风 | |  | muteEarphone | Boolean | false | 否 | 是否静音耳机 | | | | | | |
|  | forceCellularNetwork | boolean | false | 否 | 开启后，joinVoIPChat 会同时走 Wi-Fi 和蜂窝网络2种网络模式，保证实时通话体验。 | [2.29.0](../../../guide/runtime/client-lib/compatibility.html) |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| voice | 音频房间，用于语音通话 |
| video | 视频房间，结合 [voip-room](errorvoip-room)) 组件可显示成员画面 |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | muteMicrophone | Boolean | false | 否 | 是否静音麦克风 |
|  | muteEarphone | Boolean | false | 否 | 是否静音耳机 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| openIdList | Array.<String> | 在此通话中的成员 openId 名单 |
| errCode | Number | 错误码 |
| errMsg | String | 调用结果 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| -1 | 当前已在房间内 |  |
| -2 | 录音设备被占用，可能是当前正在使用微信内语音通话或系统通话 |  |
| -3 | 加入会话期间退出（可能是用户主动退出，或者退后台、来电等原因），因此加入失败 |  |
| -1000 | 系统错误 |  |

---

### wx.exitVoIPChat(Object object)

基础库 2.7.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/media/voip/wx.exitVoIPChat.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

<!-- pages: 146 -->
