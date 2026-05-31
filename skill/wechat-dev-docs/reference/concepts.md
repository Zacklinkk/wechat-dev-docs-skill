# 小程序核心概念导览 / Core Concepts Orientation

> 这是"去哪查"的索引:每条 = 官方页面 + 一句**原创**定位说明(非原文转载)。
> 需要完整说明时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

## 项目结构与配置

- [小程序代码构成](https://developers.weixin.qq.com/miniprogram/dev/framework/quickstart/code.html) — 解释 .wxml/.wxss/.js/.json 四类文件各司其职的分工关系。
- [目录结构](https://developers.weixin.qq.com/miniprogram/dev/framework/structure.html) — 列出项目根目录下 app.* 全局文件与各页面子目录的标准布局。
- [全局配置 app.json](https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/app.html) — app.json 所有字段的权威字段表，路由/窗口/tabBar 等均在此查阅。
- [页面配置 page.json](https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/page.html) — 单页 .json 可覆盖全局样式的各项字段说明。
- [框架接口总览](https://developers.weixin.qq.com/miniprogram/dev/framework/MINA.html) — 对小程序逻辑层框架（MINA）的高层介绍，是理解整体架构的起点。

## 运行时:渲染层与逻辑层

- [运行环境](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/env.html) — 说明 iOS/Android/开发者工具三端实际使用的 JS 引擎与渲染内核差异。
- [运行机制](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/operating-mechanism.html) — 讲清冷启动与热启动的触发条件及前台/后台状态切换规则。
- [更新机制](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/update-mechanism.html) — 描述微信何时静默拉包、何时提示用户更新的策略及 UpdateManager API 用法。
- [JavaScript 支持](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/js-support.html) — 列出逻辑层支持的 ES 特性白名单与不可用的浏览器 API 清单。
- [渲染层与逻辑层架构](https://developers.weixin.qq.com/miniprogram/dev/framework/quickstart/framework.html) — 从 quickstart 视角说明双线程通信模型和 setData 数据流向。

## 程序与页面生命周期

- [注册小程序 App()](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/app.html) — App() 构造选项与 onLaunch/onShow/onHide 等全局钩子的用法说明。
- [注册页面 Page()](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/page.html) — Page() 构造选项，包含 data 初始化、事件处理函数与 setData 调用方式。
- [页面生命周期](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/page-life-cycle.html) — 带时序图说明 onLoad→onShow→onReady→onHide→onUnload 各钩子的触发时机。
- [页面路由](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route.html) — 解释路由栈模型、navigateTo/redirectTo/navigateBack 对栈的影响。
- [模块化](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/module.html) — 介绍 require/exports/module.exports 在逻辑层的使用规范。

## 自定义组件

- [Component 构造器](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/component.html) — Component() 选项结构：properties/data/methods/observers 各字段的作用。
- [组件模板和样式](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/wxml-wxss.html) — 说明组件 slot 插槽、样式隔离模式（isolated/shared）及 externalClasses 用法。
- [组件间通信与事件](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/events.html) — 覆盖 triggerEvent 自定义事件、父子属性绑定与 selectComponent 直接调用三种通信方式。
- [组件生命周期](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/lifetimes.html) — 列出 created/attached/ready/detached 及页面 show/hide 钩子的触发顺序。
- [behaviors](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/behaviors.html) — 类似 mixin 的代码复用机制，将公共 properties/data/方法抽离到独立 behavior 对象。
- [数据监听器 observers](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/observer.html) — 声明式监听 data/properties 变更并自动执行副作用，替代手动 watch 逻辑。
- [组件所在页面的生命周期](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/lifetimes.html) — 同上页面也涵盖组件随宿主页面进入/离开前台时的 pageLifetimes 回调。

## 视图层(WXML / WXSS / WXS / 事件)

- [WXML 模板语法](https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxml/) — 数据绑定 `{{}}` 、列表渲染 wx:for、条件渲染 wx:if 的完整语法入口。
- [WXSS 样式](https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxss.html) — 介绍 rpx 响应式单位、样式导入与全局/局部样式覆盖规则。
- [WXS 脚本](https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxs/) — 在渲染层执行轻量 JS 逻辑（过滤器/计算属性），避免跨线程通信的场景。
- [事件系统](https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxml/event.html) — 冒泡/非冒泡事件分类、bind vs catch 绑定、事件对象 detail 字段说明。
- [获取节点信息 SelectorQuery](https://developers.weixin.qq.com/miniprogram/dev/framework/view/selector.html) — 用 wx.createSelectorQuery() 在逻辑层异步查询 DOM 尺寸与位置。

## 进阶与性能(分包 / Skyline / glass-easel)

- [分包加载总览](https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages.html) — 介绍将代码拆分为主包 + 多分包以突破 2MB 单包限制的整体策略。
- [使用分包](https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages/basic.html) — app.json 中 subpackages 字段的配置方法与分包页面路径规则。
- [独立分包](https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages/independent.html) — 无需下载主包即可独立启动的分包配置，适合活动页等轻量入口。
- [分包预下载](https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages/preload.html) — 在用户进入指定页面时提前拉取其他分包，降低跳转延迟。
- [自定义 tabBar](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/custom-tabbar.html) — 用自定义组件完全接管底部标签栏的外观与交互逻辑。
- [Skyline 渲染引擎介绍](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html) — 新一代同层渲染引擎概述：与 WebView 渲染模式的关键差异及适用场景。
- [glass-easel 介绍](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/glass-easel/introduction.html) — 小程序底层组件框架 glass-easel 的架构说明，Skyline 模式下组件系统的基础。

## 服务端与云开发

- [服务端 API 总览](https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/backend-api.html) — 服务端接口的入口;具体接口见 reference/miniprogram/server/。
- [云开发入门](https://developers.weixin.qq.com/miniprogram/dev/wxcloudservice/wxcloud/basis/getting-started.html) — 云函数/数据库/存储起步;云开发以指南为主,细节用 fetch_doc 现抓。
