# 微信小程序 API 结构化参考 — xr-frame

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html

ƬRaycastDesc:Object

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html

**RaycastDesc**

| Name | Type |
| --- | --- |
| `distance?` | `number` |
| `hit?` | [`RaycastHit`](./classes/RaycastHit.html) |
| `layerMask?` | `number` |
| `origin` | [`Vector3`](./classes/Vector3.html) |
| `unitDir` | [`Vector3`](./classes/Vector3.html) |

**TEventCallback**

| Name |
| --- |
| `TParams` |

**TEventCallback**

| Name | Type |
| --- | --- |
| `params` | `TParams` |
| `sender` | `Element` |

**ARTrackSchema**

| Name | Type |
| --- | --- |
| `autoSync` | { `type`: `string` = 'number-array' } |
| `autoSync.type` | `string` |
| `image` | { `type`: `string` = 'image' } |
| `image.type` | `string` |
| `mode` | { `type`: `string` = 'string' } |
| `mode.type` | `string` |
| `src` | { `type`: `string` = 'string' } |
| `src.type` | `string` |

**AnimatorSchema**

| Name | Type |
| --- | --- |
| `autoPlay` | { `type`: `string` = 'dict' } |
| `autoPlay.type` | `string` |
| `clipMap` | { `type`: `string` = 'dict' } |
| `clipMap.type` | `string` |
| `keyframe` | { `type`: `string` = 'keyframe' } |
| `keyframe.type` | `string` |

**RigidbodySchema**

| Name | Type |
| --- | --- |
| `constraintsMask` | { `type`: `string` = 'number' } |
| `constraintsMask.type` | `string` |
| `disabled` | { `type`: `string` = 'boolean' } |
| `disabled.type` | `string` |
| `kinematic` | { `type`: `string` = 'boolean' } |
| `kinematic.type` | `string` |
| `mass` | { `type`: `string` = 'number' } |
| `mass.type` | `string` |
| `useGravity` | { `type`: `string` = 'boolean' } |
| `useGravity.type` | `string` |

**ShapeInteractSchema**

| Name | Type |
| --- | --- |
| `bounciness` | { `type`: `string` = 'number' } |
| `bounciness.type` | `string` |
| `collide` | { `type`: `string` = 'boolean' } |
| `collide.type` | `string` |
| `disabled` | { `type`: `string` = 'boolean' } |
| `disabled.type` | `string` |
| `dynamicFriction` | { `type`: `string` = 'number' } |
| `dynamicFriction.type` | `string` |
| `staticFriction` | { `type`: `string` = 'number' } |
| `staticFriction.type` | `string` |

**noneParamsEaseFuncs**

| Name | Type |
| --- | --- |
| `ease-in` | (`x`: `number`) => `number` |
| `ease-in-back` | (`x`: `any`) => `number` |
| `ease-in-bounce` | (`x`: `any`) => `number` |
| `ease-in-circ` | (`x`: `any`) => `number` |
| `ease-in-cubic` | (`x`: `any`) => `number` |
| `ease-in-elastic` | (`x`: `any`) => `number` |
| `ease-in-expo` | (`x`: `any`) => `number` |
| `ease-in-out` | (`x`: `number`) => `number` |
| `ease-in-out-back` | (`x`: `any`) => `number` |
| `ease-in-out-bounce` | (`x`: `any`) => `number` |
| `ease-in-out-circ` | (`x`: `any`) => `number` |
| `ease-in-out-cubic` | (`x`: `any`) => `number` |
| `ease-in-out-elastic` | (`x`: `any`) => `number` |
| `ease-in-out-expo` | (`x`: `any`) => `number` |
| `ease-in-out-quad` | (`x`: `any`) => `number` |
| `ease-in-out-quart` | (`x`: `any`) => `number` |
| `ease-in-out-quint` | (`x`: `any`) => `number` |
| `ease-in-out-sine` | (`x`: `any`) => `number` |
| `ease-in-quad` | (`x`: `any`) => `number` |
| `ease-in-quart` | (`x`: `any`) => `number` |
| `ease-in-quint` | (`x`: `any`) => `number` |
| `ease-in-sine` | (`x`: `any`) => `number` |
| `ease-out` | (`x`: `number`) => `number` |
| `ease-out-back` | (`x`: `any`) => `number` |
| `ease-out-bounce` | `TEaseFunction` |
| `ease-out-circ` | (`x`: `any`) => `number` |
| `ease-out-cubic` | (`x`: `any`) => `number` |
| `ease-out-elastic` | (`x`: `any`) => `number` |
| `ease-out-expo` | (`x`: `any`) => `number` |
| `ease-out-quad` | (`x`: `any`) => `number` |
| `ease-out-quart` | (`x`: `any`) => `number` |
| `ease-out-quint` | (`x`: `any`) => `number` |
| `ease-out-sine` | (`x`: `any`) => `number` |
| `linear` | (`x`: `any`) => `any` |

**useParamsEaseFuncs**

| Name | Type |
| --- | --- |
| `cubic-bezier` | (`times`: `number`[], `params`: `number`[]) => (`x`: `number`) => `number` |
| `steps` | (`times`: `number`[], `params`: `number`[]) => (`x`: `number`) => `number` |

**genLspMeta**

| Name | Type |
| --- | --- |
| `scene` | [`Scene`](./classes/Scene.html) |

**isTextureWrapper**

| Name | Type |
| --- | --- |
| `value` | `any` |

**registerAssetLoader**

| Name | Type | Description |
| --- | --- | --- |
| `type` | `string` | 类型，也是写在[AssetLoad](./classes/AssetLoad.html)上的那个`type`。 |
| `clz` | (`scene`: [`Scene`](./classes/Scene.html), `type`: `string`) => [`AssetLoader`](./classes/AssetLoader.html)<`any`, `any`> | 继承自[AssetLoader](./classes/AssetLoader.html)的自定义资源加载器类。 |

**registerComponent**

| Name | Type |
| --- | --- |
| `type` | `string` |
| `clz` | () => [`Component`](./classes/Component.html)<`any`> |

**registerDataValue**

| Name |
| --- |
| `TDataValue` |

**registerDataValue**

| Name | Type |
| --- | --- |
| `type` | `string` |
| `handler` | [`IDataValueHandler`](./interfaces/IDataValueHandler.html)<`TDataValue`> |

**registerEffect**

| Name | Type |
| --- | --- |
| `id` | `string` |
| `factory` | (`scene`: [`Scene`](./classes/Scene.html)) => [`Effect`](./classes/Effect.html) |

**registerElement**

| Name | Type |
| --- | --- |
| `type` | `string` |
| `clz` | typeof [`Element`](./classes/Element.html) |

**registerGeometry**

| Name | Type |
| --- | --- |
| `id` | `string` |
| `factory` | (`scene`: [`Scene`](./classes/Scene.html)) => [`Geometry`](./classes/Geometry.html) |

**registerMaterial**

| Name | Type |
| --- | --- |
| `id` | `string` |
| `factory` | (`scene`: [`Scene`](./classes/Scene.html)) => [`Material`](./classes/Material.html) |

**registerTexture**

| Name | Type |
| --- | --- |
| `id` | `string` |
| `factory` | (`scene`: [`Scene`](./classes/Scene.html)) => `default` |

**registerUniformDesc**

| Name | Type |
| --- | --- |
| `id` | `string` |
| `factory` | (`scene`: [`Scene`](./classes/Scene.html)) => `default` |

**registerVertexDataDesc**

| Name | Type |
| --- | --- |
| `id` | `string` |
| `factory` | (`scene`: [`Scene`](./classes/Scene.html)) => `default` |

**registerVertexLayout**

| Name | Type |
| --- | --- |
| `id` | `string` |
| `factory` | (`scene`: [`Scene`](./classes/Scene.html)) => `default` |

---

### 导览提示

这里只是通过代码注释生成、供查阅的API文档，建议在日常使用以下两篇文档：

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/guide.html

---

### Enumeration: EARTrackerState

xr-frame/Exports/ EARTrackerState

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EARTrackerState.html

---

### Enumeration: EAnimationBlendType

xr-frame/Exports/ EAnimationBlendType

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EAnimationBlendType.html

---

### Enumeration: EBlendEquation

xr-frame/Exports/ EBlendEquation

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EBlendEquation.html

---

### Enumeration: EBlendFactor

xr-frame/Exports/ EBlendFactor

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EBlendFactor.html

---

### Enumeration: EColorMask

xr-frame/Exports/ EColorMask

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EColorMask.html

---

### Enumeration: ECompareFunc

xr-frame/Exports/ ECompareFunc

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/ECompareFunc.html

---

### Enumeration: ECullMode

xr-frame/Exports/ ECullMode

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/ECullMode.html

---

### Enumeration: EDataModelType

xr-frame/Exports/ EDataModelType

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EDataModelType.html

---

### Enumeration: EEventType

xr-frame/Exports/ EEventType

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EEventType.html

---

### Enumeration: EFaceWinding

xr-frame/Exports/ EFaceWinding

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EFaceWinding.html

---

### Enumeration: EFilterMode

xr-frame/Exports/ EFilterMode

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EFilterMode.html

---

### Enumeration: EIndexType

xr-frame/Exports/ EIndexType

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EIndexType.html

---

### Enumeration: ELoadAction

xr-frame/Exports/ ELoadAction

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/ELoadAction.html

---

### Enumeration: EMeshRenderType

xr-frame/Exports/ EMeshRenderType

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EMeshRenderType.html

---

### Enumeration: EPixelType

xr-frame/Exports/ EPixelType

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EPixelType.html

---

### Enumeration: EPrimitiveType

xr-frame/Exports/ EPrimitiveType

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EPrimitiveType.html

---

### Enumeration: EShareRecordState

xr-frame/Exports/ EShareRecordState

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EShareRecordState.html

---

### Enumeration: EShadowFitMode

xr-frame/Exports/ EShadowFitMode

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EShadowFitMode.html

---

### Enumeration: EShadowMode

xr-frame/Exports/ EShadowMode

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EShadowMode.html

---

### Enumeration: EShapeType

xr-frame/Exports/ EShapeType

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EShapeType.html

---

### Enumeration: EStencilOp

xr-frame/Exports/ EStencilOp

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EStencilOp.html

---

### Enumeration: ETextureFormat

xr-frame/Exports/ ETextureFormat

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/ETextureFormat.html

---

### Enumeration: ETextureType

xr-frame/Exports/ ETextureType

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/ETextureType.html

---

### Enumeration: EUniformType

xr-frame/Exports/ EUniformType

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EUniformType.html

---

### Enumeration: EUseDefaultAddedAction

xr-frame/Exports/ EUseDefaultAddedAction

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EUseDefaultAddedAction.html

---

### Enumeration: EUseDefaultRemovedAction

xr-frame/Exports/ EUseDefaultRemovedAction

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EUseDefaultRemovedAction.html

---

### Enumeration: EUseDefaultRetainedAction

xr-frame/Exports/ EUseDefaultRetainedAction

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EUseDefaultRetainedAction.html

---

### Enumeration: EVertexBatchOperator

xr-frame/Exports/ EVertexBatchOperator

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EVertexBatchOperator.html

---

### Enumeration: EVertexFormat

xr-frame/Exports/ EVertexFormat

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EVertexFormat.html

---

### Enumeration: EVertexLayoutUsage

xr-frame/Exports/ EVertexLayoutUsage

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EVertexLayoutUsage.html

---

### Enumeration: EVertexStep

xr-frame/Exports/ EVertexStep

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EVertexStep.html

---

### Enumeration: EVideoState

xr-frame/Exports/ EVideoState

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EVideoState.html

---

### Enumeration: EWrapMode

xr-frame/Exports/ EWrapMode

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EWrapMode.html

---

### Enumeration: ECapsuleShapeDirection

xr-frame/Exports/ ECapsuleShapeDirection

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/ECapsuleShapeDirection.html

---

### Class: Component<IData>

xr-frame/Exports/ Component

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Component.html

**Type parameters**

| Name | Description |
| --- | --- |
| `IData` | 组件数据的类型，应当和`schema`中一致，用于TS类型推断。 |

**constructor**

| Name |
| --- |
| `IData` |

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | `IData` |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | `IData` |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | `IData` |

**onTick**

| Name | Type | Description |
| --- | --- | --- |
| `deltaTime` | `number` | 单位为毫秒(ms)。 |
| `data` | `IData` | - |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | `IData` |
| `preData` | `IData` |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends `string` | `number` | `symbol` |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<`IData`> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends `string` | `number` | `symbol` |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | `IData`[`T`] |

---

### Class: ARSystem

xr-frame/Exports/ ARSystem

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/ARSystem.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IARSystemData`](./../interfaces/IARSystemData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IARSystemData`](./../interfaces/IARSystemData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IARSystemData`](./../interfaces/IARSystemData.html) |

**onTick**

| Name | Type |
| --- | --- |
| `deltaTime` | `number` |
| `data` | [`IARSystemData`](./../interfaces/IARSystemData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IARSystemData`](./../interfaces/IARSystemData.html) |
| `preData` | [`IARSystemData`](./../interfaces/IARSystemData.html) |

**forceSetViewMatrix**

| Name | Type |
| --- | --- |
| `camera` | [`Camera`](./Camera.html) |
| `mat` | [`Matrix4`](./Matrix4.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IARSystemData`](./../interfaces/IARSystemData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**placeHere**

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `nodeIdOrElement` | `string` | [`Element`](./Element.html) | `undefined` | 节点的`nodeId`或是`element`引用。 |
| `switchVisible` | `boolean` | `true` | 是否要自动切换显示或隐藏。 |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IARSystemData`](./../interfaces/IARSystemData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IARSystemData`](./../interfaces/IARSystemData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IARSystemData`](./../interfaces/IARSystemData.html)[`T`] |

---

### Class: ARTracker

xr-frame/Exports/ ARTracker

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/ARTracker.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IARTrackerData`](./../interfaces/IARTrackerData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IARTrackerData`](./../interfaces/IARTrackerData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IARTrackerData`](./../interfaces/IARTrackerData.html) |

**onTick**

| Name | Type | Description |
| --- | --- | --- |
| `deltaTime` | `number` | 单位为毫秒(ms)。 |
| `data` | [`IARTrackerData`](./../interfaces/IARTrackerData.html) | - |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IARTrackerData`](./../interfaces/IARTrackerData.html) |
| `preData` | [`IARTrackerData`](./../interfaces/IARTrackerData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IARTrackerData`](./../interfaces/IARTrackerData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**getPosition**

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `point` | `number` | `undefined` | 特征点索引，需要在`0~105`，否则返回`undefined`。 |
| `output?` | [`Vector3`](./Vector3.html) | `undefined` | - |
| `relativeToTracker` | `boolean` | `true` | 仅在`ar-system`的`pose3d`属性为`false`时生效。是否相对于`ARTracker`本身，默认为`true`，否则返回世界空间坐标。 |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IARTrackerData`](./../interfaces/IARTrackerData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IARTrackerData`](./../interfaces/IARTrackerData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IARTrackerData`](./../interfaces/IARTrackerData.html)[`T`] |

---

### Class: Animation<IData, IOptions>

xr-frame/Exports/ Animation

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Animation.html

**Type parameters**

| Name | Type | Description |
| --- | --- | --- |
| `IData` | `any` | 动画初始化接受的数据。 |
| `IOptions` | `any` | 动画播放时接受的额外追加选项。 |

**constructor**

| Name | Type |
| --- | --- |
| `IData` | `any` |
| `IOptions` | `any` |

**constructor**

| Name | Type | Description |
| --- | --- | --- |
| `_scene` | [`Scene`](./Scene.html) | 场景实例。 |
| `data` | `IData` | 初始化动画数据。 |

**onInit**

| Name | Type | Description |
| --- | --- | --- |
| `data` | `IData` | 初始化动画数据。 |

**onPause**

| Name | Type | Description |
| --- | --- | --- |
| `el` | [`Element`](./Element.html) | 本次播放作用于的`element`。 |

**onPlay**

| Name | Type | Description |
| --- | --- | --- |
| `el` | [`Element`](./Element.html) | 本次播放作用于的`element`，一个动画可能作用于多个`element`，可以在这里区分。 |
| `clipName` | `string` | 本次播放的片段名字。 |
| `options` | `IOptions` | 本次播放时的附加选项。 |

**onPlay**

| Name | Type |
| --- | --- |
| `delay?` | `number` |
| `direction?` | [`TDirection`](./../modules.html#TDirection) |
| `duration` | `number` |
| `loop?` | `number` |

**onResume**

| Name | Type | Description |
| --- | --- | --- |
| `el` | [`Element`](./Element.html) | 本次播放作用于的`element`。 |

**onStop**

| Name | Type | Description |
| --- | --- | --- |
| `el` | [`Element`](./Element.html) | 本次播放作用于的`element`。 |

**onUpdate**

| Name | Type | Description |
| --- | --- | --- |
| `el` | [`Element`](./Element.html) | 本次播放作用于的`element`。 |
| `progress` | `number` | 播放进度，范围为线性的`0~1`。 |
| `reverse` | `boolean` | 本次播放是否反向。 |

---

### Class: AnimationSystem

xr-frame/Exports/ AnimationSystem

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/AnimationSystem.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IAnimationSystemData`](./../interfaces/IAnimationSystemData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IAnimationSystemData`](./../interfaces/IAnimationSystemData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IAnimationSystemData`](./../interfaces/IAnimationSystemData.html) |

**onTick**

| Name | Type |
| --- | --- |
| `deltaTime` | `number` |
| `data` | [`IAnimationSystemData`](./../interfaces/IAnimationSystemData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IAnimationSystemData`](./../interfaces/IAnimationSystemData.html) |
| `preData` | [`IAnimationSystemData`](./../interfaces/IAnimationSystemData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IAnimationSystemData`](./../interfaces/IAnimationSystemData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IAnimationSystemData`](./../interfaces/IAnimationSystemData.html)[`T`] |

---

### Class: Animator

xr-frame/Exports/ Animator

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Animator.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IAnimatorData`](./../interfaces/IAnimatorData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IAnimatorData`](./../interfaces/IAnimatorData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IAnimatorData`](./../interfaces/IAnimatorData.html) |

**onTick**

| Name | Type | Description |
| --- | --- | --- |
| `deltaTime` | `number` | 单位为毫秒(ms)。 |
| `data` | [`IAnimatorData`](./../interfaces/IAnimatorData.html) | - |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IAnimatorData`](./../interfaces/IAnimatorData.html) |
| `preData` | [`IAnimatorData`](./../interfaces/IAnimatorData.html) |

**addAnimation**

| Name | Type |
| --- | --- |
| `T` | extends [`Animation`](./Animation.html)<`any`, `any`, `T`> |

**addAnimation**

| Name | Type | Description |
| --- | --- | --- |
| `anim` | `T` | - |
| `clipMap?` | `Object` | 可选的动画片段名字映射。 |

**createAnimation**

| Name | Type |
| --- | --- |
| `T` | extends [`Animation`](./Animation.html)<`any`, `any`, `T`> |

**createAnimation**

| Name | Type |
| --- | --- |
| `clz` | (`scene`: [`Scene`](./Scene.html), `data`: `T`[`"__DATA_TYPE"`]) => `T` |
| `data` | `T`[`"__DATA_TYPE"`] |
| `clipMap?` | `Object` |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IAnimatorData`](./../interfaces/IAnimatorData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**pause**

| Name | Type | Description |
| --- | --- | --- |
| `name?` | `string` | 需要暂停的片段，如果不填则暂停所有正在播放的片段。 |

**pauseToFrame**

| Name | Type | Description |
| --- | --- | --- |
| `name` | `string` | 片段名称。 |
| `progress` | `number` | 停到的某个进度，0~1。 |

**play**

| Name | Type | Description |
| --- | --- | --- |
| `name` | `string` | 动画片段名称。 |
| `options?` | [`IAnimationPlayOptions`](./../interfaces/IAnimationPlayOptions.html) & { `[key: string]`: `any`; } | 播放选项。 |

**removeAnimation**

| Name | Type |
| --- | --- |
| `anim` | [`Animation`](./Animation.html)<`any`, `any`> |

**resume**

| Name | Type | Description |
| --- | --- | --- |
| `name?` | `string` | 需要唤醒的片段，如果不填则唤醒所有暂停的片段。 |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IAnimatorData`](./../interfaces/IAnimatorData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IAnimatorData`](./../interfaces/IAnimatorData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IAnimatorData`](./../interfaces/IAnimatorData.html)[`T`] |

**stop**

| Name | Type | Description |
| --- | --- | --- |
| `name?` | `string` | 需要停止的片段，如果不填则停止所有正在播放的片段。 |

---

### Class: AssetLoad

xr-frame/Exports/ AssetLoad

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/AssetLoad.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | `IAssetLoadData`<`any`> |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | `IAssetLoadData`<`any`> |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | `IAssetLoadData`<`any`> |

**onTick**

| Name | Type | Description |
| --- | --- | --- |
| `deltaTime` | `number` | 单位为毫秒(ms)。 |
| `data` | `IAssetLoadData`<`any`> | - |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | `IAssetLoadData`<`any`> |
| `preData` | `IAssetLoadData`<`any`> |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof `IAssetLoadData`<`any`> |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<`IAssetLoadData`<`any`>> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof `IAssetLoadData`<`any`> |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | `IAssetLoadData`<`any`>[`T`] |

---

### Class: AssetLoader<T, ILoadOptions>

xr-frame/Exports/ AssetLoader

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/AssetLoader.html

**Type parameters**

| Name | Description |
| --- | --- |
| `T` | 加载资源的类型。 |
| `ILoadOptions` | 可接受额外配置的类型。 |

**constructor**

| Name |
| --- |
| `T` |
| `ILoadOptions` |

**constructor**

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](./Scene.html) |
| `type` | `string` |

**cancel**

| Name | Type |
| --- | --- |
| `params` | `IAssetLoadData`<`ILoadOptions`> |

**load**

| Name | Type | Description |
| --- | --- | --- |
| `data` | `IAssetLoadData`<`ILoadOptions`> | - |
| `callbacks` | `Object` | 开发者需要在加载进度更新时执行`onLoading`，在加载完成时执行`onLoaded`，在加载出错是执行`onError` |
| `callbacks.onError` | (`error`: `Error`) => `void` | - |
| `callbacks.onLoaded` | (`result`: `T`, `localPath?`: `string`) => `void` | - |
| `callbacks.onLoading` | (`progress`: `number`) => `void` | - |

**release**

| Name | Type |
| --- | --- |
| `params` | `IAssetLoadData`<`ILoadOptions`> |
| `value` | `T` |

---

### Class: AssetMaterial

xr-frame/Exports/ AssetMaterial

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/AssetMaterial.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IAssetMaterialData`](./../interfaces/IAssetMaterialData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IAssetMaterialData`](./../interfaces/IAssetMaterialData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IAssetMaterialData`](./../interfaces/IAssetMaterialData.html) |

**onTick**

| Name | Type | Description |
| --- | --- | --- |
| `deltaTime` | `number` | 单位为毫秒(ms)。 |
| `data` | [`IAssetMaterialData`](./../interfaces/IAssetMaterialData.html) | - |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IAssetMaterialData`](./../interfaces/IAssetMaterialData.html) |
| `preData` | [`IAssetMaterialData`](./../interfaces/IAssetMaterialData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IAssetMaterialData`](./../interfaces/IAssetMaterialData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IAssetMaterialData`](./../interfaces/IAssetMaterialData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IAssetMaterialData`](./../interfaces/IAssetMaterialData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IAssetMaterialData`](./../interfaces/IAssetMaterialData.html)[`T`] |

---

### Class: AssetPostProcess

xr-frame/Exports/ AssetPostProcess

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/AssetPostProcess.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IAssetPostProcessData`](./../interfaces/IAssetPostProcessData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IAssetPostProcessData`](./../interfaces/IAssetPostProcessData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IAssetPostProcessData`](./../interfaces/IAssetPostProcessData.html) |

**onTick**

| Name | Type | Description |
| --- | --- | --- |
| `deltaTime` | `number` | 单位为毫秒(ms)。 |
| `data` | [`IAssetPostProcessData`](./../interfaces/IAssetPostProcessData.html) | - |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IAssetPostProcessData`](./../interfaces/IAssetPostProcessData.html) |
| `preData` | [`IAssetPostProcessData`](./../interfaces/IAssetPostProcessData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IAssetPostProcessData`](./../interfaces/IAssetPostProcessData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IAssetPostProcessData`](./../interfaces/IAssetPostProcessData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IAssetPostProcessData`](./../interfaces/IAssetPostProcessData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IAssetPostProcessData`](./../interfaces/IAssetPostProcessData.html)[`T`] |

---

### Class: AssetRenderTexture

xr-frame/Exports/ AssetRenderTexture

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/AssetRenderTexture.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IAssetRenderTextureData`](./../interfaces/IAssetRenderTextureData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IAssetRenderTextureData`](./../interfaces/IAssetRenderTextureData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IAssetRenderTextureData`](./../interfaces/IAssetRenderTextureData.html) |

**onTick**

| Name | Type | Description |
| --- | --- | --- |
| `deltaTime` | `number` | 单位为毫秒(ms)。 |
| `data` | [`IAssetRenderTextureData`](./../interfaces/IAssetRenderTextureData.html) | - |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IAssetRenderTextureData`](./../interfaces/IAssetRenderTextureData.html) |
| `preData` | [`IAssetRenderTextureData`](./../interfaces/IAssetRenderTextureData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IAssetRenderTextureData`](./../interfaces/IAssetRenderTextureData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IAssetRenderTextureData`](./../interfaces/IAssetRenderTextureData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IAssetRenderTextureData`](./../interfaces/IAssetRenderTextureData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IAssetRenderTextureData`](./../interfaces/IAssetRenderTextureData.html)[`T`] |

---

### Class: Assets

xr-frame/Exports/ Assets

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Assets.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IAssetsData`](./../interfaces/IAssetsData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IAssetsData`](./../interfaces/IAssetsData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IAssetsData`](./../interfaces/IAssetsData.html) |

**onTick**

| Name | Type | Description |
| --- | --- | --- |
| `deltaTime` | `number` | 单位为毫秒(ms)。 |
| `data` | [`IAssetsData`](./../interfaces/IAssetsData.html) | - |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IAssetsData`](./../interfaces/IAssetsData.html) |
| `preData` | [`IAssetsData`](./../interfaces/IAssetsData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IAssetsData`](./../interfaces/IAssetsData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IAssetsData`](./../interfaces/IAssetsData.html)[`T`] |

---

### Class: AssetsSystem

xr-frame/Exports/ AssetsSystem

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/AssetsSystem.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IAssetsSystemData`](./../interfaces/IAssetsSystemData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IAssetsSystemData`](./../interfaces/IAssetsSystemData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IAssetsSystemData`](./../interfaces/IAssetsSystemData.html) |

**onTick**

| Name | Type | Description |
| --- | --- | --- |
| `deltaTime` | `number` | 单位为毫秒(ms)。 |
| `data` | [`IAssetsSystemData`](./../interfaces/IAssetsSystemData.html) | - |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IAssetsSystemData`](./../interfaces/IAssetsSystemData.html) |
| `preData` | [`IAssetsSystemData`](./../interfaces/IAssetsSystemData.html) |

**addAsset**

| Name |
| --- |
| `T` |

**addAsset**

| Name | Type |
| --- | --- |
| `type` | `string` |
| `id` | `string` |
| `asset` | `T` |

**cancelAsset**

| Name | Type |
| --- | --- |
| `type` | `string` |
| `id` | `string` |

**getAsset**

| Name |
| --- |
| `T` |

**getAsset**

| Name | Type |
| --- | --- |
| `type` | `string` |
| `id` | `string` |
| `fallback?` | `string` |

**getAssetWithState**

| Name |
| --- |
| `T` |

**getAssetWithState**

| Name | Type |
| --- | --- |
| `type` | `string` |
| `id` | `string` |
| `fallback?` | `string` |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**loadAsset**

| Name | Type |
| --- | --- |
| `params` | `IAssetLoadData`<`any`> |
| `parent?` | [`Element`](./Element.html) |

**releaseAsset**

| Name | Type |
| --- | --- |
| `type` | `string` |
| `id` | `string` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IAssetsSystemData`](./../interfaces/IAssetsSystemData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IAssetsSystemData`](./../interfaces/IAssetsSystemData.html)[`T`] |

---

### Class: Atlas

xr-frame/Exports/ Atlas

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Atlas.html

**constructor**

| Name | Type | Description |
| --- | --- | --- |
| `_scene` | [`Scene`](./Scene.html) | - |
| `options` | [`IAtlasOptions`](./../interfaces/IAtlasOptions.html) | 初始化参数。 |

**meta**

| Name | Type |
| --- | --- |
| `size` | { `h`: `number` ; `w`: `number` } |
| `size.h` | `number` |
| `size.w` | `number` |

**getFrame**

| Name | Type |
| --- | --- |
| `frameName` | `string` |

**getFrame**

| Name | Type |
| --- | --- |
| `h` | `number` |
| `w` | `number` |
| `x` | `number` |
| `y` | `number` |

**getUVMatrix**

| Name | Type |
| --- | --- |
| `frameName` | `string` |

**getUVST**

| Name | Type |
| --- | --- |
| `frameName` | `string` |

**updateFrame**

| Name | Type |
| --- | --- |
| `frameName` | `string` |
| `onUpdate` | (`texture`: `default`, `region`: { `h`: `number` ; `w`: `number` ; `x`: `number` ; `y`: `number` }, `frameName`: `string`) => `void` |

**CREATE_FROM_GRIDS**

| Name | Type | Description |
| --- | --- | --- |
| `scene` | [`Scene`](./Scene.html) | - |
| `options` | `Object` | - |
| `options.cols` | `number` | - |
| `options.height` | `number` | - |
| `options.rows` | `number` | - |
| `options.space?` | `number` | - |
| `options.width` | `number` | - |
| `onUpdate?` | (`texture`: `default`, `region`: { `col`: `number` ; `h`: `number` ; `row`: `number` ; `w`: `number` ; `x`: `number` ; `y`: `number` }, `frameName`: `string`) => `void` | 初始化时的回调，可以用于一开始绘制图像 |

**CREATE_FROM_TEXTURE**

| Name | Type |
| --- | --- |
| `scene` | [`Scene`](./Scene.html) |
| `texture` | `default` |
| `options` | [`IAtlasCreationOptions`](./../interfaces/IAtlasCreationOptions.html) |

---

### Class: AtlasLoader

xr-frame/Exports/ AtlasLoader

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/AtlasLoader.html

**constructor**

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](./Scene.html) |
| `type` | `string` |

**cancel**

| Name | Type |
| --- | --- |
| `params` | `IAssetLoadData`<[`IAtlasLoaderOptions`](./../interfaces/IAtlasLoaderOptions.html)> |

**load**

| Name | Type |
| --- | --- |
| `params` | `IAtlasLoadData` |
| `callbacks` | `Object` |
| `callbacks.onError` | (`error`: `Error`) => `void` |
| `callbacks.onLoaded` | (`value`: [`Atlas`](./Atlas.html)) => `void` |
| `callbacks.onLoading` | (`progress`: `number`) => `void` |

**release**

| Name | Type |
| --- | --- |
| `params` | `IAssetLoadData`<[`IAtlasLoaderOptions`](./../interfaces/IAtlasLoaderOptions.html)> |
| `value` | [`Atlas`](./Atlas.html) |

---

### Class: BoundBall

xr-frame/Exports/ BoundBall

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/BoundBall.html

**constructor**

| Name | Type |
| --- | --- |
| `raw?` | `Float32Array` |
| `offset?` | `number` |

**center**

| Name | Type |
| --- | --- |
| `val` | [`Vector3`](./Vector3.html) |

**radius**

| Name | Type |
| --- | --- |
| `val` | `number` |

**initByPointRadius**

| Name | Type |
| --- | --- |
| `center` | [`Vector3`](./Vector3.html) |
| `radius` | `number` |

**initByPoints**

| Name | Type |
| --- | --- |
| `points` | [`Vector3`](./Vector3.html)[] |

**setValue**

| Name | Type |
| --- | --- |
| `center` | [`Vector3`](./Vector3.html) |
| `radius` | `number` |

**createFromCenterAndRadius**

| Name | Type |
| --- | --- |
| `center` | [`Vector3`](./Vector3.html) |
| `radius` | `number` |

---

### Class: BoundBox

xr-frame/Exports/ BoundBox

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/BoundBox.html

**constructor**

| Name | Type |
| --- | --- |
| `raw?` | `Float32Array` |
| `offset?` | `number` |

**center**

| Name | Type |
| --- | --- |
| `val` | [`Vector3`](./Vector3.html) |

**size**

| Name | Type |
| --- | --- |
| `val` | [`Vector3`](./Vector3.html) |

**addPoint**

| Name | Type |
| --- | --- |
| `corner` | [`Vector3`](./Vector3.html) |

**initByPoints**

| Name | Type |
| --- | --- |
| `points` | [`Vector3`](./Vector3.html)[] |
| `length?` | `number` |

**setValue**

| Name | Type |
| --- | --- |
| `center` | [`Vector3`](./Vector3.html) |
| `size` | [`Vector3`](./Vector3.html) |

**createFromCenterAndSize**

| Name | Type | Description |
| --- | --- | --- |
| `center` | [`Vector3`](./Vector3.html) | 中心 |
| `size` | [`Vector3`](./Vector3.html) | 尺寸 |

---

### Class: Camera

xr-frame/Exports/ Camera

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Camera.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`ICameraData`](./../interfaces/ICameraData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`ICameraData`](./../interfaces/ICameraData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`ICameraData`](./../interfaces/ICameraData.html) |

**onTick**

| Name | Type |
| --- | --- |
| `deltaTime` | `number` |
| `data` | [`ICameraData`](./../interfaces/ICameraData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`ICameraData`](./../interfaces/ICameraData.html) |
| `preData` | [`ICameraData`](./../interfaces/ICameraData.html) |

**changeProjectMatrix**

| Name | Type | Description |
| --- | --- | --- |
| `manual` | `boolean` | 是否要设置为手动模式。 |
| `mat4?` | `Float32Array` | [`Matrix4`](./Matrix4.html) | 手动模式下，要设置的值。 |

**changeViewMatrix**

| Name | Type | Description |
| --- | --- | --- |
| `manual` | `boolean` | 是否要设置为手动模式。 |
| `mat4?` | `Float32Array` | [`Matrix4`](./Matrix4.html) | 手动模式下，要设置的值。 |

**convertClipPositionToWorld**

| Name | Type |
| --- | --- |
| `clipPos` | [`Vector3`](./Vector3.html) |
| `dst?` | [`Vector3`](./Vector3.html) |

**convertWorldPositionToClip**

| Name | Type |
| --- | --- |
| `worldPos` | [`Vector3`](./Vector3.html) |
| `dst?` | [`Vector3`](./Vector3.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`ICameraData`](./../interfaces/ICameraData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setBackgroundRenderStates**

| Name | Type | Description |
| --- | --- | --- |
| `states` | `Object` | 同[Material.setRenderStates](./Material.html#setRenderStates) |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`ICameraData`](./../interfaces/ICameraData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`ICameraData`](./../interfaces/ICameraData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`ICameraData`](./../interfaces/ICameraData.html)[`T`] |

---

### Class: CameraOrbitControl

xr-frame/Exports/ CameraOrbitControl

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/CameraOrbitControl.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`ICameraOrbitControlData`](./../interfaces/ICameraOrbitControlData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`ICameraOrbitControlData`](./../interfaces/ICameraOrbitControlData.html) |

**onTick**

| Name | Type |
| --- | --- |
| `deltaTime` | `number` |
| `data` | [`ICameraOrbitControlData`](./../interfaces/ICameraOrbitControlData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`ICameraOrbitControlData`](./../interfaces/ICameraOrbitControlData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`ICameraOrbitControlData`](./../interfaces/ICameraOrbitControlData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`ICameraOrbitControlData`](./../interfaces/ICameraOrbitControlData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`ICameraOrbitControlData`](./../interfaces/ICameraOrbitControlData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`ICameraOrbitControlData`](./../interfaces/ICameraOrbitControlData.html)[`T`] |

---

### Class: CapsuleShape

xr-frame/Exports/ CapsuleShape

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/CapsuleShape.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`ICapsuleShapeData`](./../interfaces/ICapsuleShapeData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IShapeData`](./../interfaces/IShapeData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IShapeData`](./../interfaces/IShapeData.html) |

**onTick**

| Name | Type |
| --- | --- |
| `dateTime` | `number` |
| `data` | [`ICapsuleShapeData`](./../interfaces/ICapsuleShapeData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`ICapsuleShapeData`](./../interfaces/ICapsuleShapeData.html) |
| `preData` | [`ICapsuleShapeData`](./../interfaces/ICapsuleShapeData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IShapeData`](./../interfaces/IShapeData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**initDelegates**

| Name | Type |
| --- | --- |
| `el` | [`Element`](./Element.html) |

**setAsShadow**

| Name | Type |
| --- | --- |
| `root` | `GLTFAbstractShape`<[`ICapsuleShapeData`](./../interfaces/ICapsuleShapeData.html)> |
| `transform` | `TQS` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IShapeData`](./../interfaces/IShapeData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IShapeData`](./../interfaces/IShapeData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IShapeData`](./../interfaces/IShapeData.html)[`T`] |

---

### Class: Color

xr-frame/Exports/ Color

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Color.html

**constructor**

| Name | Type |
| --- | --- |
| `r?` | `number` |
| `g?` | `number` |
| `b?` | `number` |
| `a?` | `number` |

**a**

| Name | Type |
| --- | --- |
| `val` | `number` |

**b**

| Name | Type |
| --- | --- |
| `val` | `number` |

**g**

| Name | Type |
| --- | --- |
| `val` | `number` |

**r**

| Name | Type |
| --- | --- |
| `val` | `number` |

**equals**

| Name | Type |
| --- | --- |
| `target` | [`Color`](./Color.html) |

**mix**

| Name | Type |
| --- | --- |
| `color` | [`Color`](./Color.html) |
| `dst?` | [`Color`](./Color.html) |

**set**

| Name | Type |
| --- | --- |
| `val` | [`Color`](./Color.html) |

**setRGBA**

| Name | Type |
| --- | --- |
| `r` | `number` |
| `g` | `number` |
| `b` | `number` |
| `a` | `number` |

**setValue32**

| Name | Type |
| --- | --- |
| `v32` | `number` |

**blendColorHex**

| Name | Type |
| --- | --- |
| `colorHexA` | `number` |
| `colorHexB` | `number` |
| `type` | `BlendType` |

**diffc**

| Name | Type |
| --- | --- |
| `v` | `number` |
| `c` | `number` |
| `diff` | `number` |

**fromFloatArray**

| Name | Type |
| --- | --- |
| `arr` | `number`[] |

**fromHex**

| Name | Type |
| --- | --- |
| `hex` | `number` |

**fromHexString**

| Name | Type |
| --- | --- |
| `hexString` | `string` |

**getValue32FromRGBA**

| Name | Type |
| --- | --- |
| `r` | `number` |
| `g` | `number` |
| `b` | `number` |
| `a` | `number` |

**hsvV2rgb**

| Name | Type |
| --- | --- |
| `h` | `number` |
| `s` | `number` |
| `v` | `number` |
| `dst?` | [`Vector3`](./Vector3.html) |

**multiplyColorHex**

| Name | Type |
| --- | --- |
| `colorHexA` | `number` |
| `colorHexB` | `number` |
| `type` | `BlendType` |

**percentRoundFn**

| Name | Type |
| --- | --- |
| `num` | `number` |

**randomMix**

| Name | Type |
| --- | --- |
| `colorHexA` | `number` |
| `colorHexB` | `number` |
| `randomSeed` | `number` |

**rgb2hsv**

| Name | Type |
| --- | --- |
| `r` | `number` |
| `g` | `number` |
| `b` | `number` |
| `dst?` | [`Vector3`](./Vector3.html) |

---

### Class: CubeShape

xr-frame/Exports/ CubeShape

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/CubeShape.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`ICubeShapeData`](./../interfaces/ICubeShapeData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IShapeData`](./../interfaces/IShapeData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IShapeData`](./../interfaces/IShapeData.html) |

**onTick**

| Name | Type |
| --- | --- |
| `dateTime` | `number` |
| `data` | [`ICubeShapeData`](./../interfaces/ICubeShapeData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`ICubeShapeData`](./../interfaces/ICubeShapeData.html) |
| `preData` | [`ICubeShapeData`](./../interfaces/ICubeShapeData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IShapeData`](./../interfaces/IShapeData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**initDelegates**

| Name | Type |
| --- | --- |
| `el` | [`Element`](./Element.html) |

**setAsShadow**

| Name | Type |
| --- | --- |
| `root` | `GLTFAbstractShape`<[`ICubeShapeData`](./../interfaces/ICubeShapeData.html)> |
| `transform` | `TQS` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IShapeData`](./../interfaces/IShapeData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IShapeData`](./../interfaces/IShapeData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IShapeData`](./../interfaces/IShapeData.html)[`T`] |

---

### Class: CubeTextureLoader

xr-frame/Exports/ CubeTextureLoader

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/CubeTextureLoader.html

**constructor**

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](./Scene.html) |
| `type` | `string` |

**cancel**

| Name | Type |
| --- | --- |
| `params` | `IAssetLoadData`<[`ICubeTextureLoaderOptions`](./../interfaces/ICubeTextureLoaderOptions.html)> |

**load**

| Name | Type |
| --- | --- |
| `params` | `ICubeTextureLoadData` |
| `callbacks` | `Object` |
| `callbacks.onError` | (`error`: `Error`) => `void` |
| `callbacks.onLoaded` | (`value`: `default`) => `void` |
| `callbacks.onLoading` | (`progress`: `number`) => `void` |

**release**

| Name | Type |
| --- | --- |
| `params` | `ICubeTextureLoadData` |
| `value` | `default` |

---

### Class: Effect

xr-frame/Exports/ Effect

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Effect.html

**constructor**

| Name | Type | Description |
| --- | --- | --- |
| `_scene` | [`Scene`](./Scene.html) | - |
| `description` | [`IEffectAsset`](./../interfaces/IEffectAsset.html) | 配置。 |

---

### Class: Element

xr-frame/Exports/ Element

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Element.html

**constructor**

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

**name**

| Name | Type |
| --- | --- |
| `value` | `string` |

**addChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**addComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**addComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |
| `options?` | `T`[`"__DATA_TYPE"`] |

**dfs**

| Name | Type |
| --- | --- |
| `T` | extends `unknown` |

**dfs**

| Name | Type |
| --- | --- |
| `callback` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `T` |
| `defaultParams?` | `T` |
| `excludeRoot?` | `boolean` |
| `stop` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `boolean` |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `index` | `number` |

**getChildByClass**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByClass**

| Name | Type |
| --- | --- |
| `clz` | (...`args`: `any`[]) => `T` |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildByName**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getChildrenByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildrenByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clzName` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |

**removeChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**removeComponent**

| Name | Type |
| --- | --- |
| `clz` | () => [`Component`](./Component.html)<`any`> |

**setAttribute**

| Name | Type |
| --- | --- |
| `name` | `string` |
| `value` | `string` |

**setId**

| Name | Type |
| --- | --- |
| `id` | `string` |

---

### Class: Env

xr-frame/Exports/ Env

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Env.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IEnvData`](./../interfaces/IEnvData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IEnvData`](./../interfaces/IEnvData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IEnvData`](./../interfaces/IEnvData.html) |

**onTick**

| Name | Type | Description |
| --- | --- | --- |
| `deltaTime` | `number` | 单位为毫秒(ms)。 |
| `data` | [`IEnvData`](./../interfaces/IEnvData.html) | - |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IEnvData`](./../interfaces/IEnvData.html) |
| `preData` | [`IEnvData`](./../interfaces/IEnvData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IEnvData`](./../interfaces/IEnvData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IEnvData`](./../interfaces/IEnvData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IEnvData`](./../interfaces/IEnvData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IEnvData`](./../interfaces/IEnvData.html)[`T`] |

---

### Class: EnvData

xr-frame/Exports/ EnvData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/EnvData.html

**constructor**

| Name | Type |
| --- | --- |
| `options` | [`IEnvDataOptions`](./../interfaces/IEnvDataOptions.html) |

---

### Class: EnvDataLoader

xr-frame/Exports/ EnvDataLoader

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/EnvDataLoader.html

**constructor**

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](./Scene.html) |
| `type` | `string` |

**cancel**

| Name | Type |
| --- | --- |
| `params` | `IAssetLoadData`<[`IEnvDataLoaderOptions`](./../interfaces/IEnvDataLoaderOptions.html)> |

**load**

| Name | Type |
| --- | --- |
| `params` | `IEnvDataLoadData` |
| `callbacks` | `Object` |
| `callbacks.onError` | (`error`: `Error`) => `void` |
| `callbacks.onLoaded` | (`value`: [`EnvData`](./EnvData.html)) => `void` |
| `callbacks.onLoading` | (`progress`: `number`) => `void` |

**release**

| Name | Type |
| --- | --- |
| `params` | `IEnvDataLoadData` |
| `value` | [`EnvData`](./EnvData.html) |

---

### Class: EventManager

xr-frame/Exports/ EventManager

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/EventManager.html

**constructor**

| Name | Type |
| --- | --- |
| `_el` | [`Element`](./Element.html) |
| `_triggerElementEvent` | `TFrameworkEventTrigger` |

**add**

| Name | Type |
| --- | --- |
| `TEvent` | `any` |

**add**

| Name | Type |
| --- | --- |
| `type` | `string` |
| `callback` | [`TEventCallback`](./../modules.html#TEventCallback)<`TEvent`> |
| `priority?` | `number` |

**addOnce**

| Name | Type |
| --- | --- |
| `TEvent` | `any` |

**addOnce**

| Name | Type |
| --- | --- |
| `type` | `string` |
| `callback` | [`TEventCallback`](./../modules.html#TEventCallback)<`TEvent`> |
| `priority?` | `number` |

**clear**

| Name | Type |
| --- | --- |
| `type` | `string` |

**flush**

| Name | Type |
| --- | --- |
| `type` | `string` |

**has**

| Name | Type |
| --- | --- |
| `type` | `string` |

**remove**

| Name | Type |
| --- | --- |
| `TEvent` | `any` |

**remove**

| Name | Type |
| --- | --- |
| `type` | `string` |
| `callback` | [`TEventCallback`](./../modules.html#TEventCallback)<`TEvent`> |

**trigger**

| Name | Type |
| --- | --- |
| `TEvent` | `any` |

**trigger**

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `type` | `string` | `undefined` | 要触发的事件类型。 |
| `event?` | `TEvent` | `undefined` | 事件的值。 |
| `immediately` | `boolean` | `true` | 是否要将事件立即分发，如果不则会先缓存，之后在每一帧更新前统一分发，避免不必要的分发。 |
| `toXML` | `boolean` | `true` | 是否要派发到`xml`绑定的事件中。 |
| `bubbles` | `boolean` | `false` | 是否要进行事件冒泡。 |

---

### Class: GLTF

xr-frame/Exports/ GLTF

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/GLTF.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IGLTFData`](./../interfaces/IGLTFData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IGLTFData`](./../interfaces/IGLTFData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IGLTFData`](./../interfaces/IGLTFData.html) |

**onTick**

| Name | Type | Description |
| --- | --- | --- |
| `deltaTime` | `number` | 单位为毫秒(ms)。 |
| `data` | [`IGLTFData`](./../interfaces/IGLTFData.html) | - |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IGLTFData`](./../interfaces/IGLTFData.html) |
| `preData` | [`IGLTFData`](./../interfaces/IGLTFData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IGLTFData`](./../interfaces/IGLTFData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**getInternalNodeByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getPrimitivesByMeshName**

| Name | Type | Description |
| --- | --- | --- |
| `name` | `string` | Mesh节点的`name` |

**getPrimitivesByNodeName**

| Name | Type | Description |
| --- | --- | --- |
| `name` | `string` | Node节点的`name`（而非Mesh节点） |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IGLTFData`](./../interfaces/IGLTFData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IGLTFData`](./../interfaces/IGLTFData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IGLTFData`](./../interfaces/IGLTFData.html)[`T`] |

---

### Class: GLTFLoader

xr-frame/Exports/ GLTFLoader

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/GlTFLoader.html

**constructor**

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](./Scene.html) |
| `type` | `string` |

**cancel**

| Name | Type |
| --- | --- |
| `params` | `IGLTFLoadData` |

**load**

| Name | Type |
| --- | --- |
| `param` | `IGLTFLoadData` |
| `callbacks` | `Object` |
| `callbacks.onError` | (`error`: `Error`) => `void` |
| `callbacks.onLoaded` | (`value`: [`GLTFModel`](./GLTFModel.html)) => `void` |
| `callbacks.onLoading` | (`progress`: `number`) => `void` |

**release**

| Name | Type |
| --- | --- |
| `params` | `IGLTFLoadData` |
| `value` | [`GLTFModel`](./GLTFModel.html) |

---

### Class: GLTFModel

xr-frame/Exports/ GLTFModel

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/GLTFModel.html

**constructor**

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](./Scene.html) |
| `model` | `GLTFRootLoaded` |

**createFromBuffer**

| Name | Type |
| --- | --- |
| `scene` | [`Scene`](./Scene.html) |
| `buffer` | `ArrayBuffer` |
| `options` | [`IGLTFLoaderOptions`](./../interfaces/IGLTFLoaderOptions.html) |

---

### Class: Geometry

xr-frame/Exports/ Geometry

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Geometry.html

**constructor**

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](./Scene.html) |
| `vertexLayout` | `default` |
| `vBuffer` | `ArrayBufferView` |
| `iBuffer` | `ArrayBufferView` |
| `indexType` | [`EIndexType`](./../enums/EIndexType.html) |

**addSubMesh**

| Name | Type | Description |
| --- | --- | --- |
| `length` | `number` | 索引长度 |
| `offset` | `number` | 索引起始偏移 |
| `materialIndex?` | `number` | - |

**getIndiceLength**

| Name | Type |
| --- | --- |
| `subMeshIndex` | `number` |

**getIndiceStart**

| Name | Type |
| --- | --- |
| `subMeshIndex` | `number` |

**getMaterialIndex**

| Name | Type |
| --- | --- |
| `subMeshIndex` | `number` |

**modifySubMesh**

| Name | Type | Description |
| --- | --- | --- |
| `subMeshIndex` | `number` | - |
| `length` | `number` | 索引长度 |
| `offset` | `number` | 索引起始偏移 |

**setBoundBall**

| Name | Type |
| --- | --- |
| `center` | [`Vector3`](./Vector3.html) |
| `radius` | `number` |

**setBoundBox**

| Name | Type | Default value |
| --- | --- | --- |
| `center` | [`Vector3`](./Vector3.html) | `undefined` |
| `size` | [`Vector3`](./Vector3.html) | `undefined` |
| `autoUpdateBall` | `boolean` | `true` |

**uploadIndexBuffer**

| Name | Type |
| --- | --- |
| `offset` | `number` |
| `buffer` | `Uint16Array` | `Uint32Array` |

**uploadVertexBuffer**

| Name | Type |
| --- | --- |
| `offset` | `number` |
| `buffer` | `ArrayBufferView` |

---

### Class: GizmoSystem

xr-frame/Exports/ GizmoSystem

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/GizmoSystem.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IGizmoSystemData`](./../interfaces/IGizmoSystemData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IGizmoSystemData`](./../interfaces/IGizmoSystemData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IGizmoSystemData`](./../interfaces/IGizmoSystemData.html) |

**onTick**

| Name | Type |
| --- | --- |
| `deltaTime` | `number` |
| `data` | [`IGizmoSystemData`](./../interfaces/IGizmoSystemData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IGizmoSystemData`](./../interfaces/IGizmoSystemData.html) |
| `preData` | [`IGizmoSystemData`](./../interfaces/IGizmoSystemData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IGizmoSystemData`](./../interfaces/IGizmoSystemData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IGizmoSystemData`](./../interfaces/IGizmoSystemData.html)[`T`] |

---

### Class: ImageLoader

xr-frame/Exports/ ImageLoader

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/ImageLoader.html

**constructor**

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](./Scene.html) |
| `type` | `string` |

**cancel**

| Name | Type |
| --- | --- |
| `params` | `IAssetLoadData`<[`IImageLoaderOptions`](./../interfaces/IImageLoaderOptions.html)> |

**load**

| Name | Type |
| --- | --- |
| `params` | `IImageLoadData` |
| `callbacks` | `Object` |
| `callbacks.onError` | (`error`: `Error`) => `void` |
| `callbacks.onLoaded` | (`value`: [`IImage`](./../interfaces/IImage.html)) => `void` |
| `callbacks.onLoading` | (`progress`: `number`) => `void` |

**release**

| Name | Type |
| --- | --- |
| `params` | `IImageLoadData` |
| `value` | [`IImage`](./../interfaces/IImage.html) |

---

### Class: KeyframeAnimation

xr-frame/Exports/ KeyframeAnimation

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/KeyframeAnimation.html

**constructor**

| Name | Type | Description |
| --- | --- | --- |
| `_scene` | [`Scene`](./Scene.html) | 场景实例。 |
| `data` | [`IKeyframeAnimationData`](./../interfaces/IKeyframeAnimationData.html) | 初始化动画数据。 |

**onInit**

| Name | Type |
| --- | --- |
| `data` | [`IKeyframeAnimationData`](./../interfaces/IKeyframeAnimationData.html) |

**onPause**

| Name | Type |
| --- | --- |
| `el` | [`Element`](./Element.html) |

**onPlay**

| Name | Type |
| --- | --- |
| `el` | [`Element`](./Element.html) |
| `clipName` | `string` |
| `options` | [`IKeyframeAnimationOptions`](./../interfaces/IKeyframeAnimationOptions.html) |

**onResume**

| Name | Type |
| --- | --- |
| `el` | [`Element`](./Element.html) |

**onStop**

| Name | Type |
| --- | --- |
| `el` | [`Element`](./Element.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `el` | [`Element`](./Element.html) |
| `progress` | `number` |
| `reverse` | `boolean` |

---

### Class: KeyframeLoader

xr-frame/Exports/ KeyframeLoader

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/KeyframeLoader.html

**constructor**

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](./Scene.html) |
| `type` | `string` |

**cancel**

| Name | Type |
| --- | --- |
| `params` | `IAssetLoadData`<[`IKeyframeLoaderOptions`](./../interfaces/IKeyframeLoaderOptions.html)> |

**load**

| Name | Type |
| --- | --- |
| `params` | `IKeyframeLoadData` |
| `callbacks` | `Object` |
| `callbacks.onError` | (`error`: `Error`) => `void` |
| `callbacks.onLoaded` | (`value`: [`KeyframeAnimation`](./KeyframeAnimation.html)) => `void` |
| `callbacks.onLoading` | (`progress`: `number`) => `void` |

**release**

| Name | Type |
| --- | --- |
| `params` | `IAssetLoadData`<[`IKeyframeLoaderOptions`](./../interfaces/IKeyframeLoaderOptions.html)> |
| `value` | [`KeyframeAnimation`](./KeyframeAnimation.html) |

---

### Class: Light

xr-frame/Exports/ Light

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Light.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`ILightData`](./../interfaces/ILightData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`ILightData`](./../interfaces/ILightData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`ILightData`](./../interfaces/ILightData.html) |

**onTick**

| Name | Type |
| --- | --- |
| `deltaTime` | `number` |
| `data` | [`ILightData`](./../interfaces/ILightData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`ILightData`](./../interfaces/ILightData.html) |
| `preData` | [`ILightData`](./../interfaces/ILightData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`ILightData`](./../interfaces/ILightData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`ILightData`](./../interfaces/ILightData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`ILightData`](./../interfaces/ILightData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`ILightData`](./../interfaces/ILightData.html)[`T`] |

---

### Class: Material

xr-frame/Exports/ Material

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Material.html

**constructor**

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](./Scene.html) |

**alphaCutOff**

| Name | Type |
| --- | --- |
| `value` | `number` |

**alphaMode**

| Name | Type |
| --- | --- |
| `value` | `"OPAQUE"` | `"BLEND"` | `"MASK"` |

**renderQueue**

| Name | Type |
| --- | --- |
| `value` | `number` |

**clearRenderState**

| Name | Type |
| --- | --- |
| `TKey` | extends keyof [`IRenderStates`](./../interfaces/IRenderStates.html) |

**clearRenderState**

| Name | Type |
| --- | --- |
| `key` | `TKey` |

**clearRenderStates**

| Name | Type |
| --- | --- |
| `states` | `Object` |

**getFloat**

| Name | Type |
| --- | --- |
| `key` | `string` |

**getMacro**

| Name | Type |
| --- | --- |
| `key` | `string` |

**getMatrix**

| Name | Type |
| --- | --- |
| `key` | `string` |

**getRenderState**

| Name | Type |
| --- | --- |
| `key` | `string` |

**getTexture**

| Name | Type |
| --- | --- |
| `key` | `string` |

**getVector**

| Name | Type |
| --- | --- |
| `key` | `string` |

**initByEffect**

| Name | Type |
| --- | --- |
| `effect` | [`Effect`](./Effect.html) |
| `defaultUniforms?` | `Object` |

**resetTexture**

| Name | Type |
| --- | --- |
| `key` | `string` |

**setFloat**

| Name | Type |
| --- | --- |
| `key` | `string` |
| `value` | `number` |

**setMacro**

| Name | Type |
| --- | --- |
| `key` | `string` |
| `value` | `number` | `boolean` |

**setMacros**

| Name | Type |
| --- | --- |
| `marcos` | `Object` |

**setMatrix**

| Name | Type |
| --- | --- |
| `key` | `string` |
| `value` | [`Matrix3`](./Matrix3.html) | [`Matrix4`](./Matrix4.html) |

**setRenderState**

| Name | Type |
| --- | --- |
| `TKey` | extends keyof [`IRenderStates`](./../interfaces/IRenderStates.html) |

**setRenderState**

| Name | Type |
| --- | --- |
| `key` | `TKey` |
| `value` | [`IRenderStates`](./../interfaces/IRenderStates.html)[`TKey`] |

**setRenderStates**

| Name | Type |
| --- | --- |
| `states` | [`IRenderStates`](./../interfaces/IRenderStates.html) |

**setTexture**

| Name | Type |
| --- | --- |
| `key` | `string` |
| `value` | `default` |

**setTextureAsset**

| Name | Type |
| --- | --- |
| `key` | `string` |
| `assetId` | `string` |

**setVector**

| Name | Type |
| --- | --- |
| `key` | `string` |
| `value` | [`Vector3`](./Vector3.html) | [`Vector2`](./Vector2.html) | [`Vector4`](./Vector4.html) |

---

### Class: Matrix3

xr-frame/Exports/ Matrix3

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Matrix3.html

**constructor**

| Name | Type |
| --- | --- |
| `raw?` | `Float32Array` |
| `offset?` | `number` |

**inverse**

| Name | Type |
| --- | --- |
| `dst?` | [`Matrix3`](./Matrix3.html) |

**multiply**

| Name | Type | Description |
| --- | --- | --- |
| `m` | [`Matrix3`](./Matrix3.html) | 右乘矩阵 |
| `dst?` | [`Matrix3`](./Matrix3.html) | - |

**rotate**

| Name | Type | Description |
| --- | --- | --- |
| `radians` | `number` | 旋转幅度，用弧度表示 |
| `dst?` | [`Matrix3`](./Matrix3.html) | - |

**scale**

| Name | Type | Description |
| --- | --- | --- |
| `sx` | `number` | x轴缩放 |
| `sy` | `number` | y轴缩放 |
| `dst?` | [`Matrix3`](./Matrix3.html) | - |

**setArray**

| Name | Type |
| --- | --- |
| `value` | `ArrayLike`<`number`> |
| `offset?` | `number` |

**transformPoint**

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector2`](./Vector2.html) | 点 |
| `dst?` | [`Vector2`](./Vector2.html) | - |

**translate**

| Name | Type | Description |
| --- | --- | --- |
| `tx` | `number` | x轴位移 |
| `ty` | `number` | y轴位移 |
| `dst?` | [`Matrix3`](./Matrix3.html) | - |

**createFromArray**

| Name | Type | Description |
| --- | --- | --- |
| `array` | `number`[] | 数据源，长度必须为9，否则会抛出异常 |

**createFromTypedArray**

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `array` | `Float32Array` | `undefined` | 数据源 |
| `offset` | `number` | `0` | - |

---

### Class: Matrix4

xr-frame/Exports/ Matrix4

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Matrix4.html

**constructor**

| Name | Type |
| --- | --- |
| `raw?` | `Float32Array` |
| `offset?` | `number` |

**axisRotate**

| Name | Type | Description |
| --- | --- | --- |
| `axis` | [`Vector3`](./Vector3.html) | 轴向量 |
| `angleInRadians` | `number` | 旋转幅度，用弧度表示 |
| `dst?` | [`Matrix4`](./Matrix4.html) | - |

**decomposeTransRotMatScale**

| Name | Type | Description |
| --- | --- | --- |
| `dstTranslation` | [`Vector3`](./Vector3.html) | 目标位移向量 |
| `dstRotationMatrix` | [`Matrix4`](./Matrix4.html) | 目标旋转矩阵 |
| `dstScale` | [`Vector3`](./Vector3.html) | 目标缩放分量 |

**getColumn**

| Name | Type | Description |
| --- | --- | --- |
| `column` | `number` | 列数 |
| `dst?` | [`Vector4`](./Vector4.html) | - |

**getRow**

| Name | Type | Description |
| --- | --- | --- |
| `row` | `number` | 行数 |
| `dst?` | [`Vector4`](./Vector4.html) | - |

**getValue**

| Name | Type | Description |
| --- | --- | --- |
| `column` | `number` | 列数 |
| `row` | `number` | 行数 |

**inverse**

| Name | Type |
| --- | --- |
| `dst?` | [`Matrix4`](./Matrix4.html) |

**multiply**

| Name | Type | Description |
| --- | --- | --- |
| `m` | [`Matrix4`](./Matrix4.html) | 右乘矩阵 |
| `dst?` | [`Matrix4`](./Matrix4.html) | - |

**rotateByQuaternion**

| Name | Type | Description |
| --- | --- | --- |
| `quaternion` | [`Quaternion`](./Quaternion.html) | 四元数 |
| `dst?` | [`Matrix4`](./Matrix4.html) | - |

**scale**

| Name | Type | Description |
| --- | --- | --- |
| `sx` | `number` | x轴缩放 |
| `sy` | `number` | y轴缩放 |
| `sz` | `number` | z轴缩放 |
| `dst?` | [`Matrix4`](./Matrix4.html) | - |

**set**

| Name | Type | Description |
| --- | --- | --- |
| `val` | [`Matrix4`](./Matrix4.html) | 目标 |

**setArray**

| Name | Type |
| --- | --- |
| `value` | `ArrayLike`<`number`> |
| `offset?` | `number` |

**setColumn**

| Name | Type | Description |
| --- | --- | --- |
| `vec` | [`Vector4`](./Vector4.html) | 列向量 |
| `column` | `number` | 列数 |

**setRow**

| Name | Type | Description |
| --- | --- | --- |
| `vec` | [`Vector4`](./Vector4.html) | 行向量 |
| `row` | `number` | 行数 |

**setValue**

| Name | Type | Description |
| --- | --- | --- |
| `value` | `number` | 值 |
| `column` | `number` | 列数 |
| `row` | `number` | 行数 |

**transformDirection**

| Name | Type | Description |
| --- | --- | --- |
| `dir` | [`Vector3`](./Vector3.html) | 方向 |
| `dst?` | [`Vector3`](./Vector3.html) | - |

**transformPoint**

| Name | Type | Description |
| --- | --- | --- |
| `p` | [`Vector3`](./Vector3.html) | 点 |
| `dst?` | [`Vector3`](./Vector3.html) | - |

**transformVector**

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector4`](./Vector4.html) | 向量 |
| `dst?` | [`Vector4`](./Vector4.html) | - |

**translate**

| Name | Type | Description |
| --- | --- | --- |
| `tx` | `number` | x轴位移 |
| `ty` | `number` | y轴位移 |
| `tz` | `number` | z轴位移 |
| `dst?` | [`Matrix4`](./Matrix4.html) | - |

**transpose**

| Name | Type |
| --- | --- |
| `dst?` | [`Matrix4`](./Matrix4.html) |

**xRotate**

| Name | Type | Description |
| --- | --- | --- |
| `rx` | `number` | 旋转幅度，用弧度表示 |
| `dst?` | [`Matrix4`](./Matrix4.html) | - |

**yRotate**

| Name | Type | Description |
| --- | --- | --- |
| `ry` | `number` | 旋转幅度，用弧度表示 |
| `dst?` | [`Matrix4`](./Matrix4.html) | - |

**zRotate**

| Name | Type | Description |
| --- | --- | --- |
| `rz` | `number` | 旋转幅度，用弧度表示 |
| `dst?` | [`Matrix4`](./Matrix4.html) | - |

**composeFromRST3**

| Name | Type | Description |
| --- | --- | --- |
| `m3` | [`Matrix3`](./Matrix3.html) | 二维RST矩阵 |
| `dst?` | [`Matrix4`](./Matrix4.html) | - |

**composeTQS**

| Name | Type | Description |
| --- | --- | --- |
| `translation` | [`Vector3`](./Vector3.html) | 位移向量 |
| `rotation` | [`Quaternion`](./Quaternion.html) | 旋转四元数 |
| `scale` | [`Vector3`](./Vector3.html) | 缩放向量 |
| `dst?` | [`Matrix4`](./Matrix4.html) | - |

**composeTRS**

| Name | Type | Description |
| --- | --- | --- |
| `translation` | [`Vector3`](./Vector3.html) | 位移向量 |
| `rotation` | [`Matrix4`](./Matrix4.html) | 旋转矩阵 |
| `scale` | [`Vector3`](./Vector3.html) | 缩放向量 |
| `dst?` | [`Matrix4`](./Matrix4.html) | - |

**createFromArray**

| Name | Type | Description |
| --- | --- | --- |
| `array` | `number`[] | 数据源，长度必须为16，否则会抛出异常 |

**createFromTypedArray**

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `array` | `Float32Array` | `undefined` | 数据源 |
| `offset` | `number` | `0` | - |

**createRotationAxis**

| Name | Type | Description |
| --- | --- | --- |
| `axis` | [`Vector3`](./Vector3.html) | 旋转轴 |
| `angleInRadians` | `number` | 旋转幅度，用弧度表示 |
| `dst?` | [`Matrix4`](./Matrix4.html) | - |

**createRotationX**

| Name | Type | Description |
| --- | --- | --- |
| `rad` | `number` | 旋转幅度，用弧度表示 |
| `dst?` | [`Matrix4`](./Matrix4.html) | - |

**createRotationY**

| Name | Type | Description |
| --- | --- | --- |
| `rad` | `number` | 旋转幅度，用弧度表示 |
| `dst?` | [`Matrix4`](./Matrix4.html) | - |

**createRotationZ**

| Name | Type | Description |
| --- | --- | --- |
| `rad` | `number` | 旋转轴 |
| `dst?` | [`Matrix4`](./Matrix4.html) | - |

**fromQuaternion**

| Name | Type | Description |
| --- | --- | --- |
| `quat` | [`Quaternion`](./Quaternion.html) | 四元数 |
| `dst?` | [`Matrix4`](./Matrix4.html) | - |

**lookAt**

| Name | Type | Description |
| --- | --- | --- |
| `position` | [`Vector3`](./Vector3.html) | 相机位置 |
| `target` | [`Vector3`](./Vector3.html) | 相机目标位置 |
| `up` | [`Vector3`](./Vector3.html) | 上方向 |
| `dst?` | [`Matrix4`](./Matrix4.html) | - |

**orthographic**

| Name | Type | Description |
| --- | --- | --- |
| `left` | `number` | 左平面 |
| `right` | `number` | 右平面 |
| `bottom` | `number` | 上平面 |
| `top` | `number` | 下平面 |
| `near` | `number` | 近平面 |
| `far` | `number` | 远平面 |
| `dst?` | [`Matrix4`](./Matrix4.html) | - |

**perspective**

| Name | Type | Description |
| --- | --- | --- |
| `fieldOfViewRadians` | `number` | 视野大小，用弧度表示 |
| `aspect` | `number` | 宽高比 |
| `near` | `number` | 近平面 |
| `far` | `number` | 远平面 |
| `dst?` | [`Matrix4`](./Matrix4.html) | - |

---

### Class: Mesh

xr-frame/Exports/ Mesh

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Mesh.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IMeshData`](./../interfaces/IMeshData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IMeshData`](./../interfaces/IMeshData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IMeshData`](./../interfaces/IMeshData.html) |

**onTick**

| Name | Type |
| --- | --- |
| `deltaTime` | `number` |
| `data` | [`IMeshData`](./../interfaces/IMeshData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IMeshData`](./../interfaces/IMeshData.html) |
| `preData` | [`IMeshData`](./../interfaces/IMeshData.html) |

**material**

| Name | Type |
| --- | --- |
| `value` | [`Material`](./Material.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IMeshData`](./../interfaces/IMeshData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IMeshData`](./../interfaces/IMeshData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IMeshData`](./../interfaces/IMeshData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IMeshData`](./../interfaces/IMeshData.html)[`T`] |

---

### Class: MeshShape

xr-frame/Exports/ MeshShape

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/MeshShape.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IMeshShapeData`](./../interfaces/IMeshShapeData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IShapeData`](./../interfaces/IShapeData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IShapeData`](./../interfaces/IShapeData.html) |

**onTick**

| Name | Type |
| --- | --- |
| `dateTime` | `number` |
| `data` | [`IMeshShapeData`](./../interfaces/IMeshShapeData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IMeshShapeData`](./../interfaces/IMeshShapeData.html) |
| `preData` | [`IMeshShapeData`](./../interfaces/IMeshShapeData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IShapeData`](./../interfaces/IShapeData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**initDelegates**

| Name | Type |
| --- | --- |
| `el` | [`Element`](./Element.html) |

**setAsShadow**

| Name | Type |
| --- | --- |
| `root` | `GLTFAbstractShape`<[`IMeshShapeData`](./../interfaces/IMeshShapeData.html)> |
| `transform` | `TQS` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IShapeData`](./../interfaces/IShapeData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IShapeData`](./../interfaces/IShapeData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IShapeData`](./../interfaces/IShapeData.html)[`T`] |

---

### Class: NodeSystem

xr-frame/Exports/ NodeSystem

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/NodeSystem.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`INodeSystemData`](./../interfaces/INodeSystemData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`INodeSystemData`](./../interfaces/INodeSystemData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`INodeSystemData`](./../interfaces/INodeSystemData.html) |

**onTick**

| Name | Type |
| --- | --- |
| `deltaTime` | `number` |
| `data` | [`INodeSystemData`](./../interfaces/INodeSystemData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`INodeSystemData`](./../interfaces/INodeSystemData.html) |
| `preData` | [`INodeSystemData`](./../interfaces/INodeSystemData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`INodeSystemData`](./../interfaces/INodeSystemData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`INodeSystemData`](./../interfaces/INodeSystemData.html)[`T`] |

---

### Class: OBB

xr-frame/Exports/ OBB

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/OBB.html

**center**

| Name | Type |
| --- | --- |
| `pos` | [`Vector3`](./Vector3.html) |

**depth**

| Name | Type |
| --- | --- |
| `d` | `number` |

**height**

| Name | Type |
| --- | --- |
| `h` | `number` |

**width**

| Name | Type |
| --- | --- |
| `w` | `number` |

**setForward**

| Name | Type |
| --- | --- |
| `forward` | [`Vector3`](./Vector3.html) |

**setValues**

| Name | Type |
| --- | --- |
| `cenX` | `number` |
| `cenY` | `number` |
| `cenZ` | `number` |
| `forward` | [`Vector3`](./Vector3.html) |
| `w` | `number` |
| `h` | `number` |
| `d` | `number` |

---

### Class: Particle

xr-frame/Exports/ Particle

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Particle.html

**billboardMode**

| Name | Type |
| --- | --- |
| `value` | `number` |

**data**

| Name | Type |
| --- | --- |
| `value` | [`IParticleData`](./../interfaces/IParticleData.html) |

**emitterPosition**

| Name | Type |
| --- | --- |
| `value` | [`Vector3`](./Vector3.html) |

**material**

| Name | Type |
| --- | --- |
| `value` | [`Material`](./Material.html) |

**useBillboard**

| Name | Type |
| --- | --- |
| `value` | `boolean` |

**useRampGradients**

| Name | Type |
| --- | --- |
| `value` | `boolean` |

**useSpriteSheet**

| Name | Type |
| --- | --- |
| `value` | `boolean` |

**addAlphaGradient**

| Name | Type | Description |
| --- | --- | --- |
| `gradient` | `number` | 指定所处粒子生命周期的阶段 |
| `alpha` | `number` | 指定粒子颜色透明度的左区间[0-1] |
| `alpha2?` | `number` | 指定粒子颜色透明度的右区间[0-1] |

**addColorGradient**

| Name | Type | Description |
| --- | --- | --- |
| `gradient` | `number` | 指定所处粒子生命周期的阶段 |
| `color1` | [`Vector4`](./Vector4.html) | 指定粒子颜色的左区间 |
| `color2?` | [`Vector4`](./Vector4.html) | 指定粒子颜色的右区间 |

**addColorRemapGradient**

| Name | Type | Description |
| --- | --- | --- |
| `gradient` | `number` | 指定所处粒子生命周期的阶段 |
| `min` | `number` | 指定粒子透明度值的左区间 |
| `max?` | `number` | 指定粒子透明度值的右区间 |

**addDragGradient**

| Name | Type | Description |
| --- | --- | --- |
| `gradient` | `number` | 指定所处粒子生命周期的阶段 |
| `drag` | `number` | - |
| `drag2?` | `number` | - |

**addLimitSpeedGradient**

| Name | Type | Description |
| --- | --- | --- |
| `gradient` | `number` | 指定所处粒子生命周期的阶段 |
| `limitSpeed` | `number` | 指定粒子限制速度的左区间 |
| `limitSpeed2?` | `number` | 指定粒子限制速度的右区间 |

**addRampGradient**

| Name | Type | Description |
| --- | --- | --- |
| `gradient` | `any` | 指定粒子颜色变化图的具体位置，对应具体值应为(1-alpha) |
| `color` | `any` | 指定该位置的颜色 |

**addSizeGradient**

| Name | Type | Description |
| --- | --- | --- |
| `gradient` | `number` | 指定所处粒子生命周期的阶段 |
| `size` | `number` | 指定粒子尺寸的左区间 |
| `size2?` | `number` | 指定粒子尺寸的右区间 |

**addSpeedScaleGradient**

| Name | Type | Description |
| --- | --- | --- |
| `gradient` | `number` | 指定所处粒子生命周期的阶段 |
| `speed` | `number` | 指定粒子速度的左区间 |
| `speed2?` | `number` | 指定粒子速度的右区间 |

**createBoxEmitter**

| Name | Type | Description |
| --- | --- | --- |
| `direction1` | [`Vector3`](./Vector3.html) | 粒子运动方向左区间 |
| `direction2` | [`Vector3`](./Vector3.html) | 粒子运动方向右区间 |
| `minEmitBox` | [`Vector3`](./Vector3.html) | 粒子生成位置最小允许坐标 |
| `maxEmitBox` | [`Vector3`](./Vector3.html) | 粒子生成位置最大允许坐标 |

**createPointEmitter**

| Name | Type | Description |
| --- | --- | --- |
| `direction1` | [`Vector3`](./Vector3.html) | 粒子运动方向左区间 |
| `direction2` | [`Vector3`](./Vector3.html) | 粒子运动方向右区间 |

**createSphereEmitter**

| Name | Type | Description |
| --- | --- | --- |
| `radius` | `number` | 球形半径 |
| `radiusRange` | `number` | 球形区域内的覆盖范围[0-1] |
| `arc` | `number` | 粒子在球形内生成的角度区间[0-360] |
| `randomizeDirection` | `number` | 粒子运动方向偏离程度[0-1] |

**createSubEmitter**

| Name | Type |
| --- | --- |
| `data` | [`IParticleData`](./../interfaces/IParticleData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IParticleData`](./../interfaces/IParticleData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**initParticle**

| Name | Type |
| --- | --- |
| `data` | [`IParticleData`](./../interfaces/IParticleData.html) |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IParticleData`](./../interfaces/IParticleData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IParticleData`](./../interfaces/IParticleData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IParticleData`](./../interfaces/IParticleData.html)[`T`] |

**start**

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `delay` | `number` | `0` | 设定粒子延时几秒后再播放。 |

---

### Class: PhysicsSystem

xr-frame/Exports/ PhysicsSystem

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/PhysicsSystem.html

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IPhysicsSystemData`](./../interfaces/IPhysicsSystemData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IPhysicsSystemData`](./../interfaces/IPhysicsSystemData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IPhysicsSystemData`](./../interfaces/IPhysicsSystemData.html) |
| `preData` | [`IPhysicsSystemData`](./../interfaces/IPhysicsSystemData.html) |

**gravity**

| Name | Type |
| --- | --- |
| `v` | [`Vector3`](./Vector3.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**ignoreLayerCollision**

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `layer1` | `number` | `undefined` | - |
| `layer2` | `number` | `undefined` | - |
| `ignore` | `boolean` | `true` | `true`表示**不**碰撞。 |

**raycast**

| Name | Type |
| --- | --- |
| `desc` | [`RaycastDesc`](./../modules.html#RaycastDesc) |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IPhysicsSystemData`](./../interfaces/IPhysicsSystemData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IPhysicsSystemData`](./../interfaces/IPhysicsSystemData.html)[`T`] |

---

### Class: PostProcess

xr-frame/Exports/ PostProcess

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/PostProcess.html

**constructor**

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](./Scene.html) |
| `options` | [`IPostProcessOptions`](./../interfaces/IPostProcessOptions.html) |

---

### Class: Quaternion

xr-frame/Exports/ Quaternion

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Quaternion.html

**constructor**

| Name | Type |
| --- | --- |
| `raw?` | `Float32Array` |
| `offset?` | `number` |

**w**

| Name | Type |
| --- | --- |
| `val` | `number` |

**x**

| Name | Type |
| --- | --- |
| `val` | `number` |

**y**

| Name | Type |
| --- | --- |
| `val` | `number` |

**z**

| Name | Type |
| --- | --- |
| `val` | `number` |

**add**

| Name | Type | Description |
| --- | --- | --- |
| `quat` | [`Quaternion`](./Quaternion.html) | 目标四元数 |
| `dst?` | [`Quaternion`](./Quaternion.html) | - |

**angleTo**

| Name | Type |
| --- | --- |
| `q` | [`Quaternion`](./Quaternion.html) |

**dot**

| Name | Type |
| --- | --- |
| `q` | [`Quaternion`](./Quaternion.html) |

**equal**

| Name | Type | Description |
| --- | --- | --- |
| `quat` | [`Quaternion`](./Quaternion.html) | 目标四元数 |

**fromPhysics**

| Name | Type |
| --- | --- |
| `v` | `RawQuaternion` |

**invert**

| Name | Type |
| --- | --- |
| `dst?` | [`Quaternion`](./Quaternion.html) |

**multiply**

| Name | Type | Description |
| --- | --- | --- |
| `quat` | [`Quaternion`](./Quaternion.html) | 目标四元数 |
| `dst?` | [`Quaternion`](./Quaternion.html) | - |

**premultiply**

| Name | Type |
| --- | --- |
| `q` | [`Quaternion`](./Quaternion.html) |

**rotateTowards**

| Name | Type |
| --- | --- |
| `q` | `any` |
| `step` | `any` |

**set**

| Name | Type | Description |
| --- | --- | --- |
| `quat` | [`Quaternion`](./Quaternion.html) | 目标四元数 |

**setArray**

| Name | Type |
| --- | --- |
| `value` | `ArrayLike`<`number`> |
| `offset?` | `number` |

**setFromEulerAngles**

| Name | Type |
| --- | --- |
| `euler` | [`Vector3`](./Vector3.html) |

**setFromUnitVectors**

| Name | Type |
| --- | --- |
| `vFrom` | `any` |
| `vTo` | `any` |

**setFromYawRollPitch**

| Name | Type |
| --- | --- |
| `yaw` | `number` |
| `roll` | `number` |
| `pitch` | `number` |

**setValue**

| Name | Type |
| --- | --- |
| `x` | `number` |
| `y` | `number` |
| `z` | `number` |
| `w` | `number` |

**slerp**

| Name | Type | Description |
| --- | --- | --- |
| `right` | [`Quaternion`](./Quaternion.html) | 目标四元数 |
| `t` | `number` | 插值系数，越接近 1 则结果越接近目标 |
| `dst?` | [`Quaternion`](./Quaternion.html) | - |

**sub**

| Name | Type | Description |
| --- | --- | --- |
| `quat` | [`Quaternion`](./Quaternion.html) | 目标四元数 |
| `dst?` | [`Quaternion`](./Quaternion.html) | - |

**toEulerAngles**

| Name | Type |
| --- | --- |
| `dst?` | [`Vector3`](./Vector3.html) |

**transformVector3**

| Name | Type |
| --- | --- |
| `vec` | [`Vector3`](./Vector3.html) |

**createFromArray**

| Name | Type | Description |
| --- | --- | --- |
| `array` | `number`[] | 数据源，长度必须为4，否则会抛出异常 |

**createFromAxisAngle**

| Name | Type | Description |
| --- | --- | --- |
| `axis` | [`Vector3`](./Vector3.html) | 旋转轴 |
| `rad` | `number` | 旋转幅度 |
| `dst?` | [`Quaternion`](./Quaternion.html) | - |

**createFromMatrix4**

| Name | Type |
| --- | --- |
| `mat` | [`Matrix4`](./Matrix4.html) |
| `dst?` | [`Quaternion`](./Quaternion.html) |

**createFromNumber**

| Name | Type | Description |
| --- | --- | --- |
| `x` | `number` | x |
| `y` | `number` | y |
| `z` | `number` | z |
| `w` | `number` | w |

**createFromTypedArray**

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `array` | `Float32Array` | `undefined` | 数据源 |
| `offset` | `number` | `0` | - |

**createFromUnitVectors**

| Name | Type |
| --- | --- |
| `vFrom` | [`Vector3`](./Vector3.html) |
| `vTo` | [`Vector3`](./Vector3.html) |

**fromEulerAngles**

| Name | Type | Description |
| --- | --- | --- |
| `euler` | [`Vector3`](./Vector3.html) | 欧拉角，x代表pitch，y代表yaw，z代表roll |
| `dst?` | [`Quaternion`](./Quaternion.html) | - |

**fromPhysics**

| Name | Type |
| --- | --- |
| `v` | `RawQuaternion` |

**lookRotation**

| Name | Type | Description |
| --- | --- | --- |
| `forward` | [`Vector3`](./Vector3.html) | 前方向 |
| `up` | [`Vector3`](./Vector3.html) | 上方向 |
| `dst?` | [`Quaternion`](./Quaternion.html) | - |

---

### Class: RawLoader

xr-frame/Exports/ RawLoader

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/RawLoader.html

**constructor**

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](./Scene.html) |
| `type` | `string` |

**cancel**

| Name | Type |
| --- | --- |
| `params` | `IAssetLoadData`<[`IRawLoaderOptions`](./../interfaces/IRawLoaderOptions.html)> |

**load**

| Name | Type |
| --- | --- |
| `params` | `IRawLoadData` |
| `callbacks` | `Object` |
| `callbacks.onError` | (`error`: `Error`) => `void` |
| `callbacks.onLoaded` | (`value`: `string` | `ArrayBuffer`) => `void` |
| `callbacks.onLoading` | (`progress`: `number`) => `void` |

**release**

| Name | Type |
| --- | --- |
| `params` | `IAssetLoadData`<[`IRawLoaderOptions`](./../interfaces/IRawLoaderOptions.html)> |
| `value` | `string` | `ArrayBuffer` |

---

### Class: RaycastHit

xr-frame/Exports/ RaycastHit

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/RaycastHit.html

**constructor**

| Name | Type |
| --- | --- |
| `scene` | [`Scene`](./Scene.html) |
| `nativeComp?` | `RaycastHit` |

**distance**

| Name | Type |
| --- | --- |
| `v` | `number` |

**normal**

| Name | Type |
| --- | --- |
| `v` | [`Vector3`](./Vector3.html) |

**point**

| Name | Type |
| --- | --- |
| `v` | [`Vector3`](./Vector3.html) |

---

### Class: RenderSystem

xr-frame/Exports/ RenderSystem

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/RenderSystem.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IRenderSystemData`](./../interfaces/IRenderSystemData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IRenderSystemData`](./../interfaces/IRenderSystemData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IRenderSystemData`](./../interfaces/IRenderSystemData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IRenderSystemData`](./../interfaces/IRenderSystemData.html) |
| `preData` | [`IRenderSystemData`](./../interfaces/IRenderSystemData.html) |

**changeFeatures**

| Name | Type |
| --- | --- |
| `features` | `Object` |

**changeMacros**

| Name | Type |
| --- | --- |
| `macros` | `Object` |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IRenderSystemData`](./../interfaces/IRenderSystemData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**getFeature**

| Name | Type |
| --- | --- |
| `key` | `string` |

**getMacro**

| Name | Type |
| --- | --- |
| `key` | `string` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IRenderSystemData`](./../interfaces/IRenderSystemData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IRenderSystemData`](./../interfaces/IRenderSystemData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IRenderSystemData`](./../interfaces/IRenderSystemData.html)[`T`] |

**useRenderGraph**

| Name | Type |
| --- | --- |
| `rg` | `default`<`any`> |

---

### Class: RenderTexture

xr-frame/Exports/ RenderTexture

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/RenderTexture.html

**constructor**

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](./Scene.html) |
| `options` | [`IRenderTextureOptions`](./../interfaces/IRenderTextureOptions.html) |

**IS**

| Name | Type |
| --- | --- |
| `obj` | `any` |

---

### Class: Scene

xr-frame/Exports/ Scene

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Scene.html

**constructor**

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

**name**

| Name | Type |
| --- | --- |
| `value` | `string` |

**addChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**addComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**addComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |
| `options?` | `T`[`"__DATA_TYPE"`] |

**createEffect**

| Name | Type |
| --- | --- |
| `description` | [`IEffectAsset`](./../interfaces/IEffectAsset.html) |

**createElement**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> |

**createElement**

| Name | Type | Description |
| --- | --- | --- |
| `clz` | (...`args`: `any`) => `T` | - |
| `attributes?` | `Object` | 初始化的属性，同于`xml`中对应的标签属性。 |

**createGeometry**

| Name | Type |
| --- | --- |
| `vertexLayout` | `default` |
| `vBuffer` | `ArrayBufferView` |
| `iBuffer` | `ArrayBufferView` |
| `indexType?` | [`EIndexType`](./../enums/EIndexType.html) |

**createImage**

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `autoRelease` | `boolean` | `true` | 此图片在第一次时候后是否释放原始数据，默认释放。 |

**createMaterial**

| Name | Type |
| --- | --- |
| `effect` | [`Effect`](./Effect.html) |
| `defaultUniforms?` | `Object` |

**createPostProcess**

| Name | Type |
| --- | --- |
| `options` | [`IPostProcessOptions`](./../interfaces/IPostProcessOptions.html) |

**createRenderTexture**

| Name | Type |
| --- | --- |
| `options?` | [`IRenderTextureOptions`](./../interfaces/IRenderTextureOptions.html) |

**createTexture**

| Name | Type |
| --- | --- |
| `options` | [`ITextureOptions`](./../interfaces/ITextureOptions.html) |

**createUniformBlock**

| Name | Type |
| --- | --- |
| `descriptor` | `default` |

**createUniformBlockDesc**

| Name | Type |
| --- | --- |
| `options` | [`IUniformDescriptorOptions`](./../interfaces/IUniformDescriptorOptions.html) |

**createVertexLayout**

| Name | Type |
| --- | --- |
| `options` | [`IVertexLayoutOptions`](./../interfaces/IVertexLayoutOptions.html) |

**createVideoTexture**

| Name | Type |
| --- | --- |
| `options?` | [`IVideoTextureOptions`](./../interfaces/IVideoTextureOptions.html) |

**dfs**

| Name | Type |
| --- | --- |
| `T` | extends `unknown` |

**dfs**

| Name | Type |
| --- | --- |
| `callback` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `T` |
| `defaultParams?` | `T` |
| `excludeRoot?` | `boolean` |
| `stop` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `boolean` |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `index` | `number` |

**getChildByClass**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByClass**

| Name | Type |
| --- | --- |
| `clz` | (...`args`: `any`[]) => `T` |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildByName**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getChildrenByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildrenByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clzName` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |

**getElementById**

| Name | Type |
| --- | --- |
| `id` | `string` |

**getNodeById**

| Name | Type |
| --- | --- |
| `nodeId` | `string` |

**removeChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**removeComponent**

| Name | Type |
| --- | --- |
| `clz` | () => [`Component`](./Component.html)<`any`> |

**setAttribute**

| Name | Type |
| --- | --- |
| `name` | `string` |
| `value` | `string` |

**setId**

| Name | Type |
| --- | --- |
| `id` | `string` |

---

### Class: Shape<T>

xr-frame/Exports/ Shape

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Shape.html

**Type parameters**

| Name | Type |
| --- | --- |
| `T` | extends [`IShapeData`](./../interfaces/IShapeData.html) = `any` |

**constructor**

| Name | Type |
| --- | --- |
| `T` | extends [`IShapeData`](./../interfaces/IShapeData.html) = `any` |

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | `T` |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IShapeData`](./../interfaces/IShapeData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IShapeData`](./../interfaces/IShapeData.html) |

**onTick**

| Name | Type |
| --- | --- |
| `dateTime` | `number` |
| `data` | `T` |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | `T` |
| `preData` | `T` |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IShapeData`](./../interfaces/IShapeData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**initDelegates**

| Name | Type |
| --- | --- |
| `el` | [`Element`](./Element.html) |

**setAsShadow**

| Name | Type |
| --- | --- |
| `root` | `GLTFAbstractShape`<`T`> |
| `transform` | `TQS` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IShapeData`](./../interfaces/IShapeData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IShapeData`](./../interfaces/IShapeData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IShapeData`](./../interfaces/IShapeData.html)[`T`] |

---

### Class: ShapeGizmos

xr-frame/Exports/ ShapeGizmos

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/ShapeGizmos.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IShapeGizmosData`](./../interfaces/IShapeGizmosData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IShapeGizmosData`](./../interfaces/IShapeGizmosData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IShapeGizmosData`](./../interfaces/IShapeGizmosData.html) |

**onTick**

| Name | Type |
| --- | --- |
| `deltaTime` | `number` |
| `data` | [`IShapeGizmosData`](./../interfaces/IShapeGizmosData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IShapeGizmosData`](./../interfaces/IShapeGizmosData.html) |
| `preData` | [`IShapeGizmosData`](./../interfaces/IShapeGizmosData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IShapeGizmosData`](./../interfaces/IShapeGizmosData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IShapeGizmosData`](./../interfaces/IShapeGizmosData.html)[`T`] |

---

### Class: ShapeInteract

xr-frame/Exports/ ShapeInteract

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/ShapeInteract.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IShapeInteractData`](./../interfaces/IShapeInteractData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IShapeInteractData`](./../interfaces/IShapeInteractData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IShapeInteractData`](./../interfaces/IShapeInteractData.html) |

**onTick**

| Name | Type | Description |
| --- | --- | --- |
| `deltaTime` | `number` | 单位为毫秒(ms)。 |
| `data` | [`IShapeInteractData`](./../interfaces/IShapeInteractData.html) | - |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IShapeInteractData`](./../interfaces/IShapeInteractData.html) |
| `preData` | [`IShapeInteractData`](./../interfaces/IShapeInteractData.html) |

**bounceCombine**

| Name | Type |
| --- | --- |
| `v` | `CombineMode` |

**frictionCombine**

| Name | Type |
| --- | --- |
| `v` | `CombineMode` |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IShapeInteractData`](./../interfaces/IShapeInteractData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IShapeInteractData`](./../interfaces/IShapeInteractData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IShapeInteractData`](./../interfaces/IShapeInteractData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IShapeInteractData`](./../interfaces/IShapeInteractData.html)[`T`] |

---

### Class: ShareSystem

xr-frame/Exports/ ShareSystem

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/ShareSystem.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IShareSystemData`](./../interfaces/IShareSystemData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IShareSystemData`](./../interfaces/IShareSystemData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IShareSystemData`](./../interfaces/IShareSystemData.html) |

**onTick**

| Name | Type |
| --- | --- |
| `deltaTime` | `number` |
| `data` | [`IShareSystemData`](./../interfaces/IShareSystemData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IShareSystemData`](./../interfaces/IShareSystemData.html) |
| `preData` | [`IShareSystemData`](./../interfaces/IShareSystemData.html) |

**captureToArrayBuffer**

| Name | Type |
| --- | --- |
| `options` | [`IShareCaptureOptions`](./../interfaces/IShareCaptureOptions.html) |

**captureToArrayBufferAsync**

| Name | Type |
| --- | --- |
| `options` | [`IShareCaptureOptions`](./../interfaces/IShareCaptureOptions.html) |

**captureToDataURL**

| Name | Type |
| --- | --- |
| `options` | [`IShareCaptureOptions`](./../interfaces/IShareCaptureOptions.html) |

**captureToDataURLAsync**

| Name | Type |
| --- | --- |
| `options` | [`IShareCaptureOptions`](./../interfaces/IShareCaptureOptions.html) |

**captureToFriends**

| Name | Type |
| --- | --- |
| `options` | [`IShareCaptureOptions`](./../interfaces/IShareCaptureOptions.html) |

**captureToLocalPath**

| Name | Type |
| --- | --- |
| `options` | [`IShareCaptureOptions`](./../interfaces/IShareCaptureOptions.html) |
| `callback` | (`fp`: `string`) => `void` | `Promise`<`void`> |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**recordStart**

| Name | Type |
| --- | --- |
| `options?` | [`IShareRecordOptions`](./../interfaces/IShareRecordOptions.html) |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IShareSystemData`](./../interfaces/IShareSystemData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IShareSystemData`](./../interfaces/IShareSystemData.html)[`T`] |

---

### Class: SphereShape

xr-frame/Exports/ SphereShape

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/SphereShape.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`ISphereShapeData`](./../interfaces/ISphereShapeData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IShapeData`](./../interfaces/IShapeData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IShapeData`](./../interfaces/IShapeData.html) |

**onTick**

| Name | Type |
| --- | --- |
| `dateTime` | `number` |
| `data` | [`ISphereShapeData`](./../interfaces/ISphereShapeData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`ISphereShapeData`](./../interfaces/ISphereShapeData.html) |
| `preData` | [`ISphereShapeData`](./../interfaces/ISphereShapeData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IShapeData`](./../interfaces/IShapeData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**initDelegates**

| Name | Type |
| --- | --- |
| `el` | [`Element`](./Element.html) |

**setAsShadow**

| Name | Type |
| --- | --- |
| `root` | `GLTFAbstractShape`<[`ISphereShapeData`](./../interfaces/ISphereShapeData.html)> |
| `transform` | `TQS` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IShapeData`](./../interfaces/IShapeData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IShapeData`](./../interfaces/IShapeData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IShapeData`](./../interfaces/IShapeData.html)[`T`] |

---

### Class: Spherical

xr-frame/Exports/ Spherical

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Spherical.html

**constructor**

| Name | Type |
| --- | --- |
| `radius?` | `number` |
| `phi?` | `number` |
| `theta?` | `number` |

**copy**

| Name | Type |
| --- | --- |
| `other` | [`Spherical`](./Spherical.html) |

**set**

| Name | Type |
| --- | --- |
| `radius` | `number` |
| `phi` | `number` |
| `theta` | `number` |

**setFromCartesianCoords**

| Name | Type |
| --- | --- |
| `x` | `number` |
| `y` | `number` |
| `z` | `number` |

**setFromVector3**

| Name | Type |
| --- | --- |
| `vector` | [`Vector3`](./Vector3.html) |

**toVector3**

| Name | Type |
| --- | --- |
| `vector?` | [`Vector3`](./Vector3.html) |

---

### Class: Text

xr-frame/Exports/ Text

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Text.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`ITextData`](./../interfaces/ITextData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`ITextData`](./../interfaces/ITextData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`ITextData`](./../interfaces/ITextData.html) |

**onTick**

| Name | Type |
| --- | --- |
| `deltaTime` | `number` |
| `data` | [`ITextData`](./../interfaces/ITextData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`ITextData`](./../interfaces/ITextData.html) |
| `preData` | [`ITextData`](./../interfaces/ITextData.html) |

**FillRenderData**

| Name | Type |
| --- | --- |
| `vertexF32` | `Float32Array` |
| `indexU16` | `Uint16Array` |
| `batchArray` | `ICharacterData`[] |

**QueryGlyphs**

| Name | Type |
| --- | --- |
| `scene` | [`Scene`](./Scene.html) |
| `characters` | `string` |
| `italic` | `boolean` |
| `bold` | `boolean` |
| `fontSize` | `number` |
| `fontFamily` | `string` |

**Typesetting**

| Name | Type |
| --- | --- |
| `glyphs` | `IGlyph`[] |
| `batchArrays` | `ICharacterData`[][] |
| `batchIndexs` | `number`[] |
| `wrapWidth` | `number` |
| `wrapHeight` | `number` |
| `lineHeight` | `number` |
| `anchor` | `number`[] |
| `padding` | `number`[] |
| `vertAlign` | `EVertAlignment` |
| `horzAlign` | `EHorzAlignment` |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`ITextData`](./../interfaces/ITextData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`ITextData`](./../interfaces/ITextData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`ITextData`](./../interfaces/ITextData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`ITextData`](./../interfaces/ITextData.html)[`T`] |

---

### Class: TextureLoader

xr-frame/Exports/ TextureLoader

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/TextureLoader.html

**constructor**

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](./Scene.html) |
| `type` | `string` |

**cancel**

| Name | Type |
| --- | --- |
| `params` | `IAssetLoadData`<[`ITextureLoaderOptions`](./../interfaces/ITextureLoaderOptions.html)> |

**load**

| Name | Type |
| --- | --- |
| `params` | `ITextureLoadData` |
| `callbacks` | `Object` |
| `callbacks.onError` | (`error`: `Error`) => `void` |
| `callbacks.onLoaded` | (`value`: `default`) => `void` |
| `callbacks.onLoading` | (`progress`: `number`) => `void` |

**release**

| Name | Type |
| --- | --- |
| `params` | `ITextureLoadData` |
| `value` | `default` |

---

### Class: TickSystem

xr-frame/Exports/ TickSystem

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/TickSystem.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`ITickSystemData`](./../interfaces/ITickSystemData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`ITickSystemData`](./../interfaces/ITickSystemData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`ITickSystemData`](./../interfaces/ITickSystemData.html) |

**onTick**

| Name | Type |
| --- | --- |
| `deltaTime` | `number` |
| `data` | [`ITickSystemData`](./../interfaces/ITickSystemData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`ITickSystemData`](./../interfaces/ITickSystemData.html) |
| `preData` | [`ITickSystemData`](./../interfaces/ITickSystemData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`ITickSystemData`](./../interfaces/ITickSystemData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`ITickSystemData`](./../interfaces/ITickSystemData.html)[`T`] |

---

### Class: Transform

xr-frame/Exports/ Transform

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Transform.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`ITransformData`](./../interfaces/ITransformData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`ITransformData`](./../interfaces/ITransformData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`ITransformData`](./../interfaces/ITransformData.html) |

**onTick**

| Name | Type | Description |
| --- | --- | --- |
| `deltaTime` | `number` | 单位为毫秒(ms)。 |
| `data` | [`ITransformData`](./../interfaces/ITransformData.html) | - |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`ITransformData`](./../interfaces/ITransformData.html) |
| `preData` | [`ITransformData`](./../interfaces/ITransformData.html) |

**layer**

| Name | Type |
| --- | --- |
| `value` | `number` |

**visible**

| Name | Type |
| --- | --- |
| `value` | `boolean` |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`ITransformData`](./../interfaces/ITransformData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`ITransformData`](./../interfaces/ITransformData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`ITransformData`](./../interfaces/ITransformData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`ITransformData`](./../interfaces/ITransformData.html)[`T`] |

**setLocalMatrix**

| Name | Type |
| --- | --- |
| `mat` | [`Matrix4`](./Matrix4.html) |

---

### Class: Vector2

xr-frame/Exports/ Vector2

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Vector2.html

**constructor**

| Name | Type |
| --- | --- |
| `raw?` | `Float32Array` |
| `offset?` | `number` |

**x**

| Name | Type |
| --- | --- |
| `val` | `number` |

**y**

| Name | Type |
| --- | --- |
| `val` | `number` |

**add**

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector2`](./Vector2.html) | 目标向量 |
| `dst?` | [`Vector2`](./Vector2.html) | - |

**dot**

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector2`](./Vector2.html) | 目标向量 |

**equal**

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector2`](./Vector2.html) | 目标向量 |

**lerp**

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector2`](./Vector2.html) | 目标向量 |
| `f` | `number` | 插值系数 |
| `dst?` | [`Vector2`](./Vector2.html) | - |

**normalize**

| Name | Type |
| --- | --- |
| `dst?` | [`Vector2`](./Vector2.html) |

**scale**

| Name | Type | Description |
| --- | --- | --- |
| `f` | `number` | 缩放比 |
| `dst?` | [`Vector2`](./Vector2.html) | - |

**set**

| Name | Type | Description |
| --- | --- | --- |
| `val` | [`Vector2`](./Vector2.html) | 目标向量 |

**setArray**

| Name | Type |
| --- | --- |
| `value` | `ArrayLike`<`number`> |
| `offset?` | `number` |

**setValue**

| Name | Type | Description |
| --- | --- | --- |
| `x` | `number` | x值 |
| `y` | `number` | y值 |

**sub**

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector2`](./Vector2.html) | 目标向量 |
| `dst?` | [`Vector2`](./Vector2.html) | - |

**createFromArray**

| Name | Type | Description |
| --- | --- | --- |
| `array` | `number`[] | 数据源，长度必须为2，否则会抛出异常 |

**createFromNumber**

| Name | Type | Description |
| --- | --- | --- |
| `x` | `number` | x |
| `y` | `number` | y |

**createFromTypedArray**

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `array` | `Float32Array` | `undefined` | 数据源 |
| `offset` | `number` | `0` | - |

---

### Class: Vector3

xr-frame/Exports/ Vector3

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Vector3.html

**constructor**

| Name | Type |
| --- | --- |
| `raw?` | `Float32Array` |
| `offset?` | `number` |

**x**

| Name | Type |
| --- | --- |
| `val` | `number` |

**y**

| Name | Type |
| --- | --- |
| `val` | `number` |

**z**

| Name | Type |
| --- | --- |
| `val` | `number` |

**add**

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector3`](./Vector3.html) | 目标向量 |
| `dst?` | [`Vector3`](./Vector3.html) | - |

**angleTo**

| Name | Type | Description |
| --- | --- | --- |
| `location` | [`Vector3`](./Vector3.html) | 目标点 |
| `dst?` | [`Vector3`](./Vector3.html) | - |

**applyMatrix4**

| Name | Type |
| --- | --- |
| `m` | [`Matrix4`](./Matrix4.html) |

**applyMatrix4Raw**

| Name | Type |
| --- | --- |
| `m` | `Float32Array` |

**applyQuaternion**

| Name | Type |
| --- | --- |
| `q` | [`Quaternion`](./Quaternion.html) |

**cross**

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector3`](./Vector3.html) | 目标向量 |
| `dst?` | [`Vector3`](./Vector3.html) | - |

**distanceTo**

| Name | Type | Description |
| --- | --- | --- |
| `p` | [`Vector3`](./Vector3.html) | 目标点 |

**dot**

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector3`](./Vector3.html) | 目标向量 |

**equal**

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector3`](./Vector3.html) | 目标向量 |

**fromArray**

| Name | Type |
| --- | --- |
| `array` | `Float32Array` |
| `offset` | `number` |

**fromPhysics**

| Name | Type |
| --- | --- |
| `v` | `any` |

**get**

| Name | Type |
| --- | --- |
| `i` | `number` |

**lerp**

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector3`](./Vector3.html) | 目标向量 |
| `f` | `number` | 插值系数 |
| `dst?` | [`Vector3`](./Vector3.html) | - |

**normalize**

| Name | Type |
| --- | --- |
| `dst?` | [`Vector3`](./Vector3.html) |

**scale**

| Name | Type | Description |
| --- | --- | --- |
| `f` | `number` | 缩放比 |
| `dst?` | [`Vector3`](./Vector3.html) | - |

**scaleXYZ**

| Name | Type | Description |
| --- | --- | --- |
| `x` | `number` | x缩放比 |
| `y` | `number` | y缩放比 |
| `z` | `number` | z缩放比 |
| `dst?` | [`Vector3`](./Vector3.html) | - |

**set**

| Name | Type |
| --- | --- |
| `v` | [`Vector3`](./Vector3.html) |

**setArray**

| Name | Type |
| --- | --- |
| `value` | `ArrayLike`<`number`> |
| `offset?` | `number` |

**setFromArray**

| Name | Type |
| --- | --- |
| `xyz` | `number`[] |

**setFromMatrixColumn**

| Name | Type |
| --- | --- |
| `m` | [`Matrix4`](./Matrix4.html) |
| `index` | `number` |

**setFromMatrixPosition**

| Name | Type |
| --- | --- |
| `worldMatrix` | [`Matrix4`](./Matrix4.html) |

**setFromMatrixScale**

| Name | Type |
| --- | --- |
| `m` | [`Matrix4`](./Matrix4.html) |

**setValue**

| Name | Type | Description |
| --- | --- | --- |
| `x` | `number` | x |
| `y` | `number` | y |
| `z` | `number` | z |

**sub**

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector3`](./Vector3.html) | 目标向量 |
| `dst?` | [`Vector3`](./Vector3.html) | - |

**transformDirection**

| Name | Type |
| --- | --- |
| `m` | [`Matrix4`](./Matrix4.html) |

**transformDirectionRaw**

| Name | Type |
| --- | --- |
| `raw` | `Float32Array` |

**createFromArray**

| Name | Type | Description |
| --- | --- | --- |
| `array` | `number`[] | 数据源，长度必须为3，否则会抛出异常 |

**createFromNumber**

| Name | Type | Description |
| --- | --- | --- |
| `x` | `number` | x |
| `y` | `number` | y |
| `z` | `number` | z |

**createFromTypedArray**

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `array` | `Float32Array` | `undefined` | 数据源 |
| `offset` | `number` | `0` | - |

**fromPhysics**

| Name | Type |
| --- | --- |
| `v` | `any` |

**transformCoordinate**

| Name | Type |
| --- | --- |
| `coordinate` | [`Vector3`](./Vector3.html) |
| `transform` | [`Matrix4`](./Matrix4.html) |
| `dst?` | [`Vector3`](./Vector3.html) |

**transformQuat**

| Name | Type | Description |
| --- | --- | --- |
| `source` | [`Vector3`](./Vector3.html) | 源向量 |
| `rotation` | [`Quaternion`](./Quaternion.html) | 用于旋转的四元数 |
| `dst?` | [`Vector3`](./Vector3.html) | - |

---

### Class: Vector4

xr-frame/Exports/ Vector4

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Vector4.html

**constructor**

| Name | Type |
| --- | --- |
| `raw?` | `Float32Array` |
| `offset?` | `number` |

**w**

| Name | Type |
| --- | --- |
| `val` | `number` |

**x**

| Name | Type |
| --- | --- |
| `val` | `number` |

**y**

| Name | Type |
| --- | --- |
| `val` | `number` |

**z**

| Name | Type |
| --- | --- |
| `val` | `number` |

**add**

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector4`](./Vector4.html) | 目标向量 |
| `dst?` | [`Vector4`](./Vector4.html) | - |

**dot**

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector4`](./Vector4.html) | 目标向量 |

**equal**

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector4`](./Vector4.html) | 目标向量 |

**lerp**

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector4`](./Vector4.html) | 目标向量 |
| `f` | `number` | 插值系数 |
| `dst?` | [`Vector4`](./Vector4.html) | - |

**scale**

| Name | Type | Description |
| --- | --- | --- |
| `f` | `number` | 缩放比 |
| `dst?` | [`Vector4`](./Vector4.html) | - |

**set**

| Name | Type |
| --- | --- |
| `v` | [`Vector4`](./Vector4.html) |

**setArray**

| Name | Type |
| --- | --- |
| `value` | `ArrayLike`<`number`> |
| `offset?` | `number` |

**setValue**

| Name | Type | Description |
| --- | --- | --- |
| `x` | `number` | x值 |
| `y` | `number` | y值 |
| `z` | `number` | z值 |
| `w` | `number` | w值 |

**sub**

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector4`](./Vector4.html) | 目标向量 |
| `dst?` | [`Vector4`](./Vector4.html) | - |

**createFromArray**

| Name | Type | Description |
| --- | --- | --- |
| `array` | `number`[] | 数据源，长度必须为4，否则会抛出异常 |

**createFromNumber**

| Name | Type |
| --- | --- |
| `x` | `number` |
| `y` | `number` |
| `z` | `number` |
| `w` | `number` |

**createFromTypedArray**

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `array` | `Float32Array` | `undefined` | 数据源 |
| `offset` | `number` | `0` | - |

---

### Class: VideoSystem

xr-frame/Exports/ VideoSystem

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/VideoSystem.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IVideoSystemData`](./../interfaces/IVideoSystemData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IVideoSystemData`](./../interfaces/IVideoSystemData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IVideoSystemData`](./../interfaces/IVideoSystemData.html) |

**onTick**

| Name | Type |
| --- | --- |
| `deltaTime` | `number` |
| `data` | [`IVideoSystemData`](./../interfaces/IVideoSystemData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IVideoSystemData`](./../interfaces/IVideoSystemData.html) |
| `preData` | [`IVideoSystemData`](./../interfaces/IVideoSystemData.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IVideoSystemData`](./../interfaces/IVideoSystemData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends `never` |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IVideoSystemData`](./../interfaces/IVideoSystemData.html)[`T`] |

---

### Class: VideoTexture

xr-frame/Exports/ VideoTexture

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/VideoTexture.html

**constructor**

| Name | Type | Description |
| --- | --- | --- |
| `scene` | [`Scene`](./Scene.html) | - |
| `options` | [`IVideoTextureOptions`](./../interfaces/IVideoTextureOptions.html) | - |
| `onReady` | (`vt`: [`VideoTexture`](./VideoTexture.html), `error?`: `Error`) => `void` | 创建成功时的回调。 |
| `onEnd?` | () => `void` | 播放结束时的回调。 |

**seek**

| Name | Type | Description |
| --- | --- | --- |
| `pos` | `number` | 事件，单位为s |

---

### Class: VideoTextureLoader

xr-frame/Exports/ VideoTextureLoader

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/VideoTextureLoader.html

**constructor**

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](./Scene.html) |
| `type` | `string` |

**cancel**

| Name | Type |
| --- | --- |
| `params` | `IAssetLoadData`<[`IVideoTextureLoaderOptions`](./../interfaces/IVideoTextureLoaderOptions.html)> |

**load**

| Name | Type |
| --- | --- |
| `params` | `IVideoTextureLoadData` |
| `callbacks` | `Object` |
| `callbacks.onError` | (`error`: `Error`) => `void` |
| `callbacks.onLoaded` | (`value`: [`VideoTexture`](./VideoTexture.html)) => `void` |
| `callbacks.onLoading` | (`progress`: `number`) => `void` |

**release**

| Name | Type |
| --- | --- |
| `params` | `IVideoTextureLoadData` |
| `value` | [`VideoTexture`](./VideoTexture.html) |

---

### Class: XRARTracker

xr-frame/Exports/ XRARTracker

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/XRARTracker.html

**constructor**

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

**name**

| Name | Type |
| --- | --- |
| `value` | `string` |

**addChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**addComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**addComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |
| `options?` | `T`[`"__DATA_TYPE"`] |

**dfs**

| Name | Type |
| --- | --- |
| `T` | extends `unknown` |

**dfs**

| Name | Type |
| --- | --- |
| `callback` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `T` |
| `defaultParams?` | `T` |
| `excludeRoot?` | `boolean` |
| `stop` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `boolean` |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `index` | `number` |

**getChildByClass**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByClass**

| Name | Type |
| --- | --- |
| `clz` | (...`args`: `any`[]) => `T` |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildByName**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getChildrenByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildrenByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clzName` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |

**removeChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**removeComponent**

| Name | Type |
| --- | --- |
| `clz` | () => [`Component`](./Component.html)<`any`> |

**setAttribute**

| Name | Type |
| --- | --- |
| `name` | `string` |
| `value` | `string` |

**setId**

| Name | Type |
| --- | --- |
| `id` | `string` |

---

### Class: XRAssetLoad

xr-frame/Exports/ XRAssetLoad

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/XRAssetLoad.html

**constructor**

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

**name**

| Name | Type |
| --- | --- |
| `value` | `string` |

**addChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**addComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**addComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |
| `options?` | `T`[`"__DATA_TYPE"`] |

**dfs**

| Name | Type |
| --- | --- |
| `T` | extends `unknown` |

**dfs**

| Name | Type |
| --- | --- |
| `callback` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `T` |
| `defaultParams?` | `T` |
| `excludeRoot?` | `boolean` |
| `stop` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `boolean` |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `index` | `number` |

**getChildByClass**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByClass**

| Name | Type |
| --- | --- |
| `clz` | (...`args`: `any`[]) => `T` |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildByName**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getChildrenByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildrenByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clzName` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |

**removeChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**removeComponent**

| Name | Type |
| --- | --- |
| `clz` | () => [`Component`](./Component.html)<`any`> |

**setAttribute**

| Name | Type |
| --- | --- |
| `name` | `string` |
| `value` | `string` |

**setId**

| Name | Type |
| --- | --- |
| `id` | `string` |

---

### Class: XRAssetPostProcess

xr-frame/Exports/ XRAssetPostProcess

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/XRAssetPostProcess.html

**constructor**

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

**name**

| Name | Type |
| --- | --- |
| `value` | `string` |

**addChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**addComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**addComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |
| `options?` | `T`[`"__DATA_TYPE"`] |

**dfs**

| Name | Type |
| --- | --- |
| `T` | extends `unknown` |

**dfs**

| Name | Type |
| --- | --- |
| `callback` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `T` |
| `defaultParams?` | `T` |
| `excludeRoot?` | `boolean` |
| `stop` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `boolean` |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `index` | `number` |

**getChildByClass**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByClass**

| Name | Type |
| --- | --- |
| `clz` | (...`args`: `any`[]) => `T` |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildByName**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getChildrenByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildrenByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clzName` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |

**removeChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**removeComponent**

| Name | Type |
| --- | --- |
| `clz` | () => [`Component`](./Component.html)<`any`> |

**setAttribute**

| Name | Type |
| --- | --- |
| `name` | `string` |
| `value` | `string` |

**setId**

| Name | Type |
| --- | --- |
| `id` | `string` |

---

### Class: XRAssetRenderTexture

xr-frame/Exports/ XRAssetRenderTexture

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/XRAssetRenderTexture.html

**constructor**

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

**name**

| Name | Type |
| --- | --- |
| `value` | `string` |

**addChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**addComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**addComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |
| `options?` | `T`[`"__DATA_TYPE"`] |

**dfs**

| Name | Type |
| --- | --- |
| `T` | extends `unknown` |

**dfs**

| Name | Type |
| --- | --- |
| `callback` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `T` |
| `defaultParams?` | `T` |
| `excludeRoot?` | `boolean` |
| `stop` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `boolean` |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `index` | `number` |

**getChildByClass**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByClass**

| Name | Type |
| --- | --- |
| `clz` | (...`args`: `any`[]) => `T` |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildByName**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getChildrenByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildrenByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clzName` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |

**removeChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**removeComponent**

| Name | Type |
| --- | --- |
| `clz` | () => [`Component`](./Component.html)<`any`> |

**setAttribute**

| Name | Type |
| --- | --- |
| `name` | `string` |
| `value` | `string` |

**setId**

| Name | Type |
| --- | --- |
| `id` | `string` |

---

### Class: XRAssets

xr-frame/Exports/ XRAssets

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/XRAssets.html

**constructor**

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

**name**

| Name | Type |
| --- | --- |
| `value` | `string` |

**addChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**addComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**addComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |
| `options?` | `T`[`"__DATA_TYPE"`] |

**dfs**

| Name | Type |
| --- | --- |
| `T` | extends `unknown` |

**dfs**

| Name | Type |
| --- | --- |
| `callback` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `T` |
| `defaultParams?` | `T` |
| `excludeRoot?` | `boolean` |
| `stop` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `boolean` |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `index` | `number` |

**getChildByClass**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByClass**

| Name | Type |
| --- | --- |
| `clz` | (...`args`: `any`[]) => `T` |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildByName**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getChildrenByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildrenByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clzName` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |

**removeChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**removeComponent**

| Name | Type |
| --- | --- |
| `clz` | () => [`Component`](./Component.html)<`any`> |

**setAttribute**

| Name | Type |
| --- | --- |
| `name` | `string` |
| `value` | `string` |

**setId**

| Name | Type |
| --- | --- |
| `id` | `string` |

---

### Class: XRCamera

xr-frame/Exports/ XRCamera

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/XRCamera.html

**constructor**

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

**name**

| Name | Type |
| --- | --- |
| `value` | `string` |

**addChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**addComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**addComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |
| `options?` | `T`[`"__DATA_TYPE"`] |

**dfs**

| Name | Type |
| --- | --- |
| `T` | extends `unknown` |

**dfs**

| Name | Type |
| --- | --- |
| `callback` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `T` |
| `defaultParams?` | `T` |
| `excludeRoot?` | `boolean` |
| `stop` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `boolean` |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `index` | `number` |

**getChildByClass**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByClass**

| Name | Type |
| --- | --- |
| `clz` | (...`args`: `any`[]) => `T` |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildByName**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getChildrenByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildrenByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clzName` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |

**removeChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**removeComponent**

| Name | Type |
| --- | --- |
| `clz` | () => [`Component`](./Component.html)<`any`> |

**setAttribute**

| Name | Type |
| --- | --- |
| `name` | `string` |
| `value` | `string` |

**setId**

| Name | Type |
| --- | --- |
| `id` | `string` |

---

### Class: XREnv

xr-frame/Exports/ XREnv

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/XREnv.html

**constructor**

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

**name**

| Name | Type |
| --- | --- |
| `value` | `string` |

**addChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**addComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**addComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |
| `options?` | `T`[`"__DATA_TYPE"`] |

**dfs**

| Name | Type |
| --- | --- |
| `T` | extends `unknown` |

**dfs**

| Name | Type |
| --- | --- |
| `callback` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `T` |
| `defaultParams?` | `T` |
| `excludeRoot?` | `boolean` |
| `stop` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `boolean` |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `index` | `number` |

**getChildByClass**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByClass**

| Name | Type |
| --- | --- |
| `clz` | (...`args`: `any`[]) => `T` |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildByName**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getChildrenByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildrenByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clzName` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |

**removeChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**removeComponent**

| Name | Type |
| --- | --- |
| `clz` | () => [`Component`](./Component.html)<`any`> |

**setAttribute**

| Name | Type |
| --- | --- |
| `name` | `string` |
| `value` | `string` |

**setId**

| Name | Type |
| --- | --- |
| `id` | `string` |

---

### Class: XRGLTF

xr-frame/Exports/ XRGLTF

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/XRGLTF.html

**constructor**

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

**name**

| Name | Type |
| --- | --- |
| `value` | `string` |

**addChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**addComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**addComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |
| `options?` | `T`[`"__DATA_TYPE"`] |

**dfs**

| Name | Type |
| --- | --- |
| `T` | extends `unknown` |

**dfs**

| Name | Type |
| --- | --- |
| `callback` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `T` |
| `defaultParams?` | `T` |
| `excludeRoot?` | `boolean` |
| `stop` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `boolean` |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `index` | `number` |

**getChildByClass**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByClass**

| Name | Type |
| --- | --- |
| `clz` | (...`args`: `any`[]) => `T` |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildByName**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getChildrenByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildrenByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clzName` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |

**removeChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**removeComponent**

| Name | Type |
| --- | --- |
| `clz` | () => [`Component`](./Component.html)<`any`> |

**setAttribute**

| Name | Type |
| --- | --- |
| `name` | `string` |
| `value` | `string` |

**setId**

| Name | Type |
| --- | --- |
| `id` | `string` |

---

### Class: XRLight

xr-frame/Exports/ XRLight

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/XRLight.html

**constructor**

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

**name**

| Name | Type |
| --- | --- |
| `value` | `string` |

**addChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**addComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**addComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |
| `options?` | `T`[`"__DATA_TYPE"`] |

**dfs**

| Name | Type |
| --- | --- |
| `T` | extends `unknown` |

**dfs**

| Name | Type |
| --- | --- |
| `callback` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `T` |
| `defaultParams?` | `T` |
| `excludeRoot?` | `boolean` |
| `stop` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `boolean` |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `index` | `number` |

**getChildByClass**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByClass**

| Name | Type |
| --- | --- |
| `clz` | (...`args`: `any`[]) => `T` |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildByName**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getChildrenByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildrenByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clzName` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |

**removeChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**removeComponent**

| Name | Type |
| --- | --- |
| `clz` | () => [`Component`](./Component.html)<`any`> |

**setAttribute**

| Name | Type |
| --- | --- |
| `name` | `string` |
| `value` | `string` |

**setId**

| Name | Type |
| --- | --- |
| `id` | `string` |

---

### Class: XRMaterial

xr-frame/Exports/ XRMaterial

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/XRMaterial.html

**constructor**

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

**name**

| Name | Type |
| --- | --- |
| `value` | `string` |

**addChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**addComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**addComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |
| `options?` | `T`[`"__DATA_TYPE"`] |

**dfs**

| Name | Type |
| --- | --- |
| `T` | extends `unknown` |

**dfs**

| Name | Type |
| --- | --- |
| `callback` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `T` |
| `defaultParams?` | `T` |
| `excludeRoot?` | `boolean` |
| `stop` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `boolean` |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `index` | `number` |

**getChildByClass**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByClass**

| Name | Type |
| --- | --- |
| `clz` | (...`args`: `any`[]) => `T` |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildByName**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getChildrenByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildrenByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clzName` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |

**removeChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**removeComponent**

| Name | Type |
| --- | --- |
| `clz` | () => [`Component`](./Component.html)<`any`> |

**setAttribute**

| Name | Type |
| --- | --- |
| `name` | `string` |
| `value` | `string` |

**setId**

| Name | Type |
| --- | --- |
| `id` | `string` |

---

### Class: XRMesh

xr-frame/Exports/ XRMesh

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/XRMesh.html

**constructor**

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

**name**

| Name | Type |
| --- | --- |
| `value` | `string` |

**addChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**addComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**addComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |
| `options?` | `T`[`"__DATA_TYPE"`] |

**dfs**

| Name | Type |
| --- | --- |
| `T` | extends `unknown` |

**dfs**

| Name | Type |
| --- | --- |
| `callback` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `T` |
| `defaultParams?` | `T` |
| `excludeRoot?` | `boolean` |
| `stop` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `boolean` |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `index` | `number` |

**getChildByClass**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByClass**

| Name | Type |
| --- | --- |
| `clz` | (...`args`: `any`[]) => `T` |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildByName**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getChildrenByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildrenByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clzName` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |

**removeChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**removeComponent**

| Name | Type |
| --- | --- |
| `clz` | () => [`Component`](./Component.html)<`any`> |

**setAttribute**

| Name | Type |
| --- | --- |
| `name` | `string` |
| `value` | `string` |

**setId**

| Name | Type |
| --- | --- |
| `id` | `string` |

---

### Class: XRNode

xr-frame/Exports/ XRNode

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/XRNode.html

**constructor**

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

**name**

| Name | Type |
| --- | --- |
| `value` | `string` |

**addChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**addComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**addComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |
| `options?` | `T`[`"__DATA_TYPE"`] |

**dfs**

| Name | Type |
| --- | --- |
| `T` | extends `unknown` |

**dfs**

| Name | Type |
| --- | --- |
| `callback` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `T` |
| `defaultParams?` | `T` |
| `excludeRoot?` | `boolean` |
| `stop` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `boolean` |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `index` | `number` |

**getChildByClass**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByClass**

| Name | Type |
| --- | --- |
| `clz` | (...`args`: `any`[]) => `T` |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildByName**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getChildrenByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildrenByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clzName` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |

**removeChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**removeComponent**

| Name | Type |
| --- | --- |
| `clz` | () => [`Component`](./Component.html)<`any`> |

**setAttribute**

| Name | Type |
| --- | --- |
| `name` | `string` |
| `value` | `string` |

**setId**

| Name | Type |
| --- | --- |
| `id` | `string` |

**IS**

| Name | Type |
| --- | --- |
| `element` | [`Element`](./Element.html) |

---

### Class: XRParticle

xr-frame/Exports/ XRParticle

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/XRParticle.html

**constructor**

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

**name**

| Name | Type |
| --- | --- |
| `value` | `string` |

**addChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**addComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**addComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |
| `options?` | `T`[`"__DATA_TYPE"`] |

**dfs**

| Name | Type |
| --- | --- |
| `T` | extends `unknown` |

**dfs**

| Name | Type |
| --- | --- |
| `callback` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `T` |
| `defaultParams?` | `T` |
| `excludeRoot?` | `boolean` |
| `stop` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `boolean` |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `index` | `number` |

**getChildByClass**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByClass**

| Name | Type |
| --- | --- |
| `clz` | (...`args`: `any`[]) => `T` |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildByName**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getChildrenByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildrenByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clzName` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |

**removeChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**removeComponent**

| Name | Type |
| --- | --- |
| `clz` | () => [`Component`](./Component.html)<`any`> |

**setAttribute**

| Name | Type |
| --- | --- |
| `name` | `string` |
| `value` | `string` |

**setId**

| Name | Type |
| --- | --- |
| `id` | `string` |

---

### Class: XRShadow

xr-frame/Exports/ XRShadow

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/XRShadow.html

**constructor**

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

**name**

| Name | Type |
| --- | --- |
| `value` | `string` |

**addChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**addComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**addComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |
| `options?` | `T`[`"__DATA_TYPE"`] |

**dfs**

| Name | Type |
| --- | --- |
| `T` | extends `unknown` |

**dfs**

| Name | Type |
| --- | --- |
| `callback` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `T` |
| `defaultParams?` | `T` |
| `excludeRoot?` | `boolean` |
| `stop` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `boolean` |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `index` | `number` |

**getChildByClass**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByClass**

| Name | Type |
| --- | --- |
| `clz` | (...`args`: `any`[]) => `T` |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildByName**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getChildrenByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildrenByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clzName` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |

**removeChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**removeComponent**

| Name | Type |
| --- | --- |
| `clz` | () => [`Component`](./Component.html)<`any`> |

**setAttribute**

| Name | Type |
| --- | --- |
| `name` | `string` |
| `value` | `string` |

**setId**

| Name | Type |
| --- | --- |
| `id` | `string` |

---

### Class: XRText

xr-frame/Exports/ XRText

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/XRText.html

**constructor**

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

**name**

| Name | Type |
| --- | --- |
| `value` | `string` |

**addChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**addComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**addComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |
| `options?` | `T`[`"__DATA_TYPE"`] |

**dfs**

| Name | Type |
| --- | --- |
| `T` | extends `unknown` |

**dfs**

| Name | Type |
| --- | --- |
| `callback` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `T` |
| `defaultParams?` | `T` |
| `excludeRoot?` | `boolean` |
| `stop` | (`element`: [`Element`](./Element.html), `params?`: `T`) => `boolean` |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildAtIndex**

| Name | Type |
| --- | --- |
| `index` | `number` |

**getChildByClass**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByClass**

| Name | Type |
| --- | --- |
| `clz` | (...`args`: `any`[]) => `T` |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildByName**

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](./Element.html)<`T`> = [`Element`](./Element.html) |

**getChildByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getChildrenByFilter**

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](./Element.html)) => `boolean` |

**getChildrenByName**

| Name | Type |
| --- | --- |
| `name` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clzName` | `string` |

**getComponent**

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](./Component.html)<`any`, `T`> |

**getComponent**

| Name | Type |
| --- | --- |
| `clz` | () => `T` |

**removeChild**

| Name | Type |
| --- | --- |
| `child` | [`Element`](./Element.html) |

**removeComponent**

| Name | Type |
| --- | --- |
| `clz` | () => [`Component`](./Component.html)<`any`> |

**setAttribute**

| Name | Type |
| --- | --- |
| `name` | `string` |
| `value` | `string` |

**setId**

| Name | Type |
| --- | --- |
| `id` | `string` |

---

### Class: Rigidbody

xr-frame/Exports/ Rigidbody

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Rigidbody.html

**onAdd**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IRigidbodyData`](./../interfaces/IRigidbodyData.html) |

**onRelease**

| Name | Type |
| --- | --- |
| `data` | [`IRigidbodyData`](./../interfaces/IRigidbodyData.html) |

**onRemove**

| Name | Type |
| --- | --- |
| `parent` | [`Element`](./Element.html) |
| `data` | [`IRigidbodyData`](./../interfaces/IRigidbodyData.html) |

**onTick**

| Name | Type |
| --- | --- |
| `dateTime` | `number` |
| `data` | [`IRigidbodyData`](./../interfaces/IRigidbodyData.html) |

**onUpdate**

| Name | Type |
| --- | --- |
| `data` | [`IRigidbodyData`](./../interfaces/IRigidbodyData.html) |
| `preData` | [`IRigidbodyData`](./../interfaces/IRigidbodyData.html) |

**angularDamping**

| Name | Type |
| --- | --- |
| `v` | `number` |

**angularVelocity**

| Name | Type |
| --- | --- |
| `v` | [`Vector3`](./Vector3.html) |

**centerOfMass**

| Name | Type |
| --- | --- |
| `v` | [`Vector3`](./Vector3.html) |

**collisionDetectionMode**

| Name | Type |
| --- | --- |
| `v` | `CollisionDetectionMode` |

**detectCollisions**

| Name | Type |
| --- | --- |
| `v` | `boolean` |

**freezeRotation**

| Name | Type |
| --- | --- |
| `v` | `boolean` |

**inertiaTensor**

| Name | Type |
| --- | --- |
| `v` | `number` |

**isKinematic**

| Name | Type |
| --- | --- |
| `v` | `boolean` |

**linearDamping**

| Name | Type |
| --- | --- |
| `v` | `number` |

**mass**

| Name | Type |
| --- | --- |
| `v` | `number` |

**maxAngularVelocity**

| Name | Type |
| --- | --- |
| `v` | `number` |

**maxDepenetrationVelocity**

| Name | Type |
| --- | --- |
| `v` | `number` |

**position**

| Name | Type |
| --- | --- |
| `v` | [`Vector3`](./Vector3.html) |

**positionConstraints**

| Name | Type |
| --- | --- |
| `v` | `boolean`[] |

**rotation**

| Name | Type |
| --- | --- |
| `v` | [`Quaternion`](./Quaternion.html) |

**rotationConstraints**

| Name | Type |
| --- | --- |
| `v` | `boolean`[] |

**sleepThreshold**

| Name | Type |
| --- | --- |
| `v` | `number` |

**solverIterations**

| Name | Type |
| --- | --- |
| `v` | `number` |

**solverVelocityIterations**

| Name | Type |
| --- | --- |
| `v` | `number` |

**useGravity**

| Name | Type |
| --- | --- |
| `v` | `boolean` |

**velocity**

| Name | Type |
| --- | --- |
| `v` | [`Vector3`](./Vector3.html) |

**AddExplosionForce**

| Name | Type | Description |
| --- | --- | --- |
| `explosionForce` | `number` | 爆炸力的大小。 |
| `explosionPosition` | [`Vector3`](./Vector3.html) | 爆炸球体的球心位置。 |
| `explosionRadius` | `number` | 爆炸球体的半径。 |
| `upwardsModifier` | `number` | 使用相对数值来修改推力的*作用位置*的y坐标。 |
| `mode` | `ForceMode` | 力的类型。 |

**AddForceAtPosition**

| Name | Type | Description |
| --- | --- | --- |
| `force` | [`Vector3`](./Vector3.html) | 世界坐标下矢量形式的力，作用在position位置上。 |
| `position` | [`Vector3`](./Vector3.html) | 力的作用位置。 |
| `mode` | `ForceMode` | 力的类型。 |

**addForce**

| Name | Type | Description |
| --- | --- | --- |
| `force` | [`Vector3`](./Vector3.html) | 世界坐标下矢量形式的力，作用在物体质心上。 |
| `mode` | `ForceMode` | 力的类型。 |

**addRelativeForce**

| Name | Type | Description |
| --- | --- | --- |
| `force` | [`Vector3`](./Vector3.html) | **局部**坐标下矢量形式的力，作用在物体质心上。 |
| `mode` | `ForceMode` | 力的类型。 |

**addRelativeTorque**

| Name | Type | Description |
| --- | --- | --- |
| `torque` | [`Vector3`](./Vector3.html) | **局部**坐标下矢量形式的力矩。 |
| `mode` | `ForceMode` | 力矩的类型。 |

**addTorque**

| Name | Type | Description |
| --- | --- | --- |
| `torque` | [`Vector3`](./Vector3.html) | 世界坐标下矢量形式的力矩。 |
| `mode` | `ForceMode` | 力矩的类型。 |

**applyData**

| Name | Type |
| --- | --- |
| `data` | [`IRigidbodyData`](./../interfaces/IRigidbodyData.html) |

**closestPointOnBounds**

| Name | Type |
| --- | --- |
| `position` | [`Vector3`](./Vector3.html) |

**getData**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IRigidbodyData`](./../interfaces/IRigidbodyData.html) |

**getData**

| Name | Type |
| --- | --- |
| `key` | `T` |

**getPointVelocity**

| Name | Type | Description |
| --- | --- | --- |
| `worldPoint` | [`Vector3`](./Vector3.html) | 世界坐标下的位置（其实在刚体外也可以）。 |

**getRelativePointVelocity**

| Name | Type | Description |
| --- | --- | --- |
| `relativePoint` | [`Vector3`](./Vector3.html) | **局部**坐标下的位置（其实在刚体外也可以）。 |

**movePosition**

| Name | Type | Description |
| --- | --- | --- |
| `position` | [`Vector3`](./Vector3.html) | 位移的终点 |

**moveRotation**

| Name | Type |
| --- | --- |
| `rotation` | [`Quaternion`](./Quaternion.html) |

**setData**

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IRigidbodyData`](./../interfaces/IRigidbodyData.html)> |

**setDataOne**

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IRigidbodyData`](./../interfaces/IRigidbodyData.html) |

**setDataOne**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IRigidbodyData`](./../interfaces/IRigidbodyData.html)[`T`] |

**setDensity**

| Name | Type |
| --- | --- |
| `density` | `number` |

---

### Interface: IComponentSchema

xr-frame/Exports/ IComponentSchema

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IComponentSchema.html

---

### Interface: IARRawData

xr-frame/Exports/ IARRawData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IARRawData.html

---

### Interface: IARSystemData

xr-frame/Exports/ IARSystemData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IARSystemData.html

---

### Interface: IARTrackerData

xr-frame/Exports/ IARTrackerData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IARTrackerData.html

---

### Interface: IARTrackerRawData

xr-frame/Exports/ IARTrackerRawData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IARTrackerRawData.html

**angle**

| Name | Type |
| --- | --- |
| `pitch` | `number` |
| `roll` | `number` |
| `yaw` | `number` |
| `z_score` | `number` |

**origin**

| Name | Type |
| --- | --- |
| `x` | `number` |
| `y` | `number` |

**size**

| Name | Type |
| --- | --- |
| `height` | `number` |
| `width` | `number` |

---

### Interface: IAnimationPlayOptions

xr-frame/Exports/ IAnimationPlayOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IAnimationPlayOptions.html

---

### Interface: IAnimationSystemData

xr-frame/Exports/ IAnimationSystemData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IAnimationSystemData.html

---

### Interface: IAnimatorAutoPlay

xr-frame/Exports/ IAnimatorAutoPlay

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IAnimatorAutoPlay.html

---

### Interface: IAnimatorData

xr-frame/Exports/ IAnimatorData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IAnimatorData.html

---

### Interface: IAssetMaterialData

xr-frame/Exports/ IAssetMaterialData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IAssetMaterialData.html

---

### Interface: IAssetPostProcessData

xr-frame/Exports/ IAssetPostProcessData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IAssetPostProcessData.html

---

### Interface: IAssetRenderTextureData

xr-frame/Exports/ IAssetRenderTextureData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IAssetRenderTextureData.html

---

### Interface: IAssetsData

xr-frame/Exports/ IAssetsData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IAssetsData.html

---

### Interface: IAssetsSystemData

xr-frame/Exports/ IAssetsSystemData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IAssetsSystemData.html

---

### Interface: IAtlasCreationOptions

xr-frame/Exports/ IAtlasCreationOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IAtlasCreationOptions.html

---

### Interface: IAtlasLoaderOptions

xr-frame/Exports/ IAtlasLoaderOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IAtlasLoaderOptions.html

---

### Interface: IAtlasOptions

xr-frame/Exports/ IAtlasOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IAtlasOptions.html

**meta**

| Name | Type |
| --- | --- |
| `size` | { `h`: `number` ; `w`: `number` } |
| `size.h` | `number` |
| `size.w` | `number` |

---

### Interface: IAttachment

xr-frame/Exports/ IAttachment

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IAttachment.html

---

### Interface: ICameraData

xr-frame/Exports/ ICameraData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ICameraData.html

---

### Interface: ICameraOrbitControlData

xr-frame/Exports/ ICameraOrbitControlData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ICameraOrbitControlData.html

---

### Interface: ICapsuleShapeData

xr-frame/Exports/ ICapsuleShapeData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ICapsuleShapeData.html

---

### Interface: ICubeShapeData

xr-frame/Exports/ ICubeShapeData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ICubeShapeData.html

---

### Interface: ICubeTextureLoaderOptions

xr-frame/Exports/ ICubeTextureLoaderOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ICubeTextureLoaderOptions.html

---

### Interface: IDataValueHandler<TDataValue>

xr-frame/Exports/ IDataValueHandler

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IDataValueHandler.html

**Type parameters**

| Name |
| --- |
| `TDataValue` |

**create**

| Name | Type |
| --- | --- |
| `value` | `string` |
| `defaultValue` | `any` |
| `scene` | [`Scene`](./../classes/Scene.html) |

---

### Interface: IDownloader

xr-frame/Exports/ IDownloader

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IDownloader.html

**LOAD**

| Name | Type |
| --- | --- |
| `options` | `Object` |
| `options.onError` | (`error`: `Error`) => `void` |
| `options.onLoad` | (`res`: { `data`: `ArrayBuffer` ; `filePath`: `string` }) => `void` |
| `options.encoding` | `"binary"` | `"utf-8"` |
| `options.src` | `string` |

---

### Interface: IEffectAsset

xr-frame/Exports/ IEffectAsset

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IEffectAsset.html

---

### Interface: IEngineSettings

xr-frame/Exports/ IEngineSettings

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IEngineSettings.html

**audio**

| Name | Type | Description |
| --- | --- | --- |
| `globalVolume?` | `number` | 全局音量 |
| `maxRealVoices?` | `number` | 真实音频数量上限 |

---

### Interface: IEntityComponents

xr-frame/Exports/ IEntityComponents

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IEntityComponents.html

---

### Interface: IEnvData

xr-frame/Exports/ IEnvData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IEnvData.html

---

### Interface: IEnvDataLoaderOptions

xr-frame/Exports/ IEnvDataLoaderOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IEnvDataLoaderOptions.html

---

### Interface: IEnvDataOptions

xr-frame/Exports/ IEnvDataOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IEnvDataOptions.html

**diffuse**

| Name | Type | Description |
| --- | --- | --- |
| `coefficients` | `Float32Array` | 球谐系数SH9。 |

**skybox**

| Name | Type | Description |
| --- | --- | --- |
| `half` | `boolean` | 是否只使用贴图的上半部分，一般在和`specular`共用贴图的时候为`true`。 |
| `map` | `default` | 贴图。 |

**specular**

| Name | Type | Description |
| --- | --- | --- |
| `map` | `default` | 贴图。 |
| `mipmapCount?` | `number` | 使用的mipmap级数。 |
| `mipmaps` | `boolean` | 是否使用mipmap。 |
| `rgbd` | `boolean` | 是否使用`rgbd`编码来。 |
| `type` | `"2D"` | 贴图类型，目前只支持2D。 |

---

### Interface: IEventBridge

xr-frame/Exports/ IEventBridge

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IEventBridge.html

**bindEntitiesToBones**

| Name | Type |
| --- | --- |
| `entities` | { `id`: `number` }[] |
| `boneEntities` | { `id`: `number` }[] |

**bindEntityToBone**

| Name | Type |
| --- | --- |
| `entity` | `Object` |
| `entity.id` | `number` |
| `boneEntity` | `Object` |
| `boneEntity.id` | `number` |

**entityAddChild**

| Name | Type |
| --- | --- |
| `entity` | `number` |
| `child` | `number` |

**entityAddChildAtIndex**

| Name | Type |
| --- | --- |
| `entity` | `number` |
| `child` | `number` |
| `index` | `number` |

**entityClear**

| Name | Type |
| --- | --- |
| `entity` | `number` |

**entityRemoveFromParent**

| Name | Type |
| --- | --- |
| `entity` | `number` |

**entitySetActive**

| Name | Type |
| --- | --- |
| `entity` | `number` |
| `active` | `boolean` |

**entitySetLocalMatrixDirty**

| Name | Type |
| --- | --- |
| `entity` | `number` |

**setRootEntity**

| Name | Type |
| --- | --- |
| `entity` | `number` |

**unbindEntitiesFromBones**

| Name | Type |
| --- | --- |
| `entities` | { `id`: `number` }[] |

**unbindEntityFromBone**

| Name | Type |
| --- | --- |
| `entity` | `Object` |
| `entity.id` | `number` |

---

### Interface: IFeatures

xr-frame/Exports/ IFeatures

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IFeatures.html

---

### Interface: IFontSetting

xr-frame/Exports/ IFontSetting

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IFontSetting.html

---

### Interface: IGLTFData

xr-frame/Exports/ IGLTFData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IGLTFData.html

---

### Interface: IGLTFLoaderOptions

xr-frame/Exports/ IGLTFLoaderOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IGLTFLoaderOptions.html

---

### Interface: IGLTFModelOptions

xr-frame/Exports/ IGLTFModelOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IGLTFModelOptions.html

---

### Interface: IGizmoSystemData

xr-frame/Exports/ IGizmoSystemData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IGizmoSystemData.html

---

### Interface: IGlyphInfo

xr-frame/Exports/ IGlyphInfo

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IGlyphInfo.html

---

### Interface: IHandle

xr-frame/Exports/ IHandle

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IHandle.html

---

### Interface: IImage

xr-frame/Exports/ IImage

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IImage.html

**onerror**

| Name | Type |
| --- | --- |
| `error` | `Error` |

---

### Interface: IImageLoaderOptions

xr-frame/Exports/ IImageLoaderOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IImageLoaderOptions.html

---

### Interface: IKeyframeAnimationData

xr-frame/Exports/ IKeyframeAnimationData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IKeyframeAnimationData.html

---

### Interface: IKeyframeAnimationInfo

xr-frame/Exports/ IKeyframeAnimationInfo

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IKeyframeAnimationInfo.html

---

### Interface: IKeyframeAnimationOptions

xr-frame/Exports/ IKeyframeAnimationOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IKeyframeAnimationOptions.html

---

### Interface: IKeyframeLoaderOptions

xr-frame/Exports/ IKeyframeLoaderOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IKeyframeLoaderOptions.html

---

### Interface: ILightData

xr-frame/Exports/ ILightData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ILightData.html

---

### Interface: ILoaderOptionsSchema

xr-frame/Exports/ ILoaderOptionsSchema

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ILoaderOptionsSchema.html

---

### Interface: ILongIntNativeMap

xr-frame/Exports/ ILongIntNativeMap

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ILongIntNativeMap.html

**del**

| Name | Type |
| --- | --- |
| `key1` | `number` |
| `key2` | `number` |

**get**

| Name | Type |
| --- | --- |
| `key1` | `number` |
| `key2` | `number` |

**set**

| Name | Type |
| --- | --- |
| `key1` | `number` |
| `key2` | `number` |
| `value` | `number` |

---

### Interface: IMeshData

xr-frame/Exports/ IMeshData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IMeshData.html

---

### Interface: IMeshShapeData

xr-frame/Exports/ IMeshShapeData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IMeshShapeData.html

---

### Interface: INativeMap<T>

xr-frame/Exports/ INativeMap

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/INativeMap.html

**Type parameters**

| Name |
| --- |
| `T` |

**del**

| Name | Type |
| --- | --- |
| `key` | `T` |

**get**

| Name | Type |
| --- | --- |
| `key` | `T` |

**set**

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | `number` |

---

### Interface: INodeSystemData

xr-frame/Exports/ INodeSystemData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/INodeSystemData.html

---

### Interface: IParticleData

xr-frame/Exports/ IParticleData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IParticleData.html

---

### Interface: IPhysicsSystemData

xr-frame/Exports/ IPhysicsSystemData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IPhysicsSystemData.html

---

### Interface: IPostProcessOptions

xr-frame/Exports/ IPostProcessOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IPostProcessOptions.html

---

### Interface: IRawLoaderOptions

xr-frame/Exports/ IRawLoaderOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IRawLoaderOptions.html

---

### Interface: IRealDownloader

xr-frame/Exports/ IRealDownloader

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IRealDownloader.html

**load**

| Name | Type |
| --- | --- |
| `options` | `Object` |
| `options.onError` | (`error`: `Error`) => `void` |
| `options.onLoad` | (`res`: { `data`: `ArrayBuffer` ; `filePath`: `string` }) => `void` |
| `options.encoding` | `"binary"` | `"utf-8"` |
| `options.src` | `string` |

---

### Interface: IRect

xr-frame/Exports/ IRect

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IRect.html

---

### Interface: IRenderPassDescriptor

xr-frame/Exports/ IRenderPassDescriptor

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IRenderPassDescriptor.html

---

### Interface: IRenderStates

xr-frame/Exports/ IRenderStates

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IRenderStates.html

---

### Interface: IRenderSystemData

xr-frame/Exports/ IRenderSystemData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IRenderSystemData.html

---

### Interface: IRenderTarget

xr-frame/Exports/ IRenderTarget

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IRenderTarget.html

---

### Interface: IRenderTextureOptions

xr-frame/Exports/ IRenderTextureOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IRenderTextureOptions.html

---

### Interface: IRigidbodyData

xr-frame/Exports/ IRigidbodyData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IRigidbodyData.html

---

### Interface: IShapeData

xr-frame/Exports/ IShapeData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IShapeData.html

---

### Interface: IShapeDragEvent

xr-frame/Exports/ IShapeDragEvent

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IShapeDragEvent.html

---

### Interface: IShapeGizmosData

xr-frame/Exports/ IShapeGizmosData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IShapeGizmosData.html

---

### Interface: IShapeInteractData

xr-frame/Exports/ IShapeInteractData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IShapeInteractData.html

---

### Interface: IShapeTouchEvent

xr-frame/Exports/ IShapeTouchEvent

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IShapeTouchEvent.html

---

### Interface: IShareCaptureOptions

xr-frame/Exports/ IShareCaptureOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IShareCaptureOptions.html

---

### Interface: IShareSystemData

xr-frame/Exports/ IShareSystemData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IShareSystemData.html

---

### Interface: ISphereShapeData

xr-frame/Exports/ ISphereShapeData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ISphereShapeData.html

---

### Interface: ISubMesh

xr-frame/Exports/ ISubMesh

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ISubMesh.html

---

### Interface: ITextData

xr-frame/Exports/ ITextData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ITextData.html

---

### Interface: ITextureLoaderOptions

xr-frame/Exports/ ITextureLoaderOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ITextureLoaderOptions.html

---

### Interface: ITextureOptions

xr-frame/Exports/ ITextureOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ITextureOptions.html

---

### Interface: ITextureWrapper

xr-frame/Exports/ ITextureWrapper

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ITextureWrapper.html

---

### Interface: ITickSystemData

xr-frame/Exports/ ITickSystemData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ITickSystemData.html

---

### Interface: ITransformData

xr-frame/Exports/ ITransformData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ITransformData.html

---

### Interface: IUniformDescriptorOptions

xr-frame/Exports/ IUniformDescriptorOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IUniformDescriptorOptions.html

---

### Interface: IVertexDataDescriptorOptions

xr-frame/Exports/ IVertexDataDescriptorOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IVertexDataDescriptorOptions.html

---

### Interface: IVertexLayoutOptions

xr-frame/Exports/ IVertexLayoutOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IVertexLayoutOptions.html

---

### Interface: IVideoSystemData

xr-frame/Exports/ IVideoSystemData

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IVideoSystemData.html

---

### Interface: IVideoTextureLoaderOptions

xr-frame/Exports/ IVideoTextureLoaderOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IVideoTextureLoaderOptions.html

---

### Interface: IVideoTextureOptions

xr-frame/Exports/ IVideoTextureOptions

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IVideoTextureOptions.html

---

### Interface: IView

xr-frame/Exports/ IView

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IView.html

---

### Interface: IViewAction

xr-frame/Exports/ IViewAction

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IViewAction.html

---

### Interface: ICollideEvent

xr-frame/Exports/ ICollideEvent

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ICollideEvent.html

---

### Interface: IContactPoint

xr-frame/Exports/ IContactPoint

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IContactPoint.html

---

### Interface: IOverlapEvent

xr-frame/Exports/ IOverlapEvent

官方 / Source: https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IOverlapEvent.html

---

<!-- pages: 213 -->
