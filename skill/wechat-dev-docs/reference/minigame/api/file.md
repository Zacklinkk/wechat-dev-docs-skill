# 微信小游戏 API 结构化参考 — file

> 由 tools/build/build_reference.py 生成。仅含事实(标题/简介/属性·参数表/深链)。
> 需要完整说明与示例时:`uv run <skill>/tools/fetch_doc.py <url>`。正文版权归腾讯。

### wx.saveFileToDisk(Object object)

基础库 2.11.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/wx.saveFileToDisk.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| filePath | string |  | 是 | 待保存文件路径 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

---

### FileSystemManager wx.getFileSystemManager()

微信 Windows 版：支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/wx.getFileSystemManager.html

---

### FileStats

相关文档:文件系统

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileStats.html

---

### FileSystemManager

相关文档:文件系统

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.html

---

### FileSystemManager.access(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.access.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| path | string |  | 是 | 要判断是否存在的文件/目录路径 (本地路径) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.accessSync(string path)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.accessSync.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.appendFile(Object object)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.appendFile.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | filePath | string |  | 是 | 要追加内容的文件路径 (本地路径) |
|  | data | string/ArrayBuffer |  | 是 | 要追加的文本或二进制数据 |
|  | encoding | string | utf8 | 否 | 指定写入文件的字符编码 |
|  | | 合法值 | 说明 | | --- | --- | | ascii |  | | base64 |  | | binary |  | | hex |  | | ucs2 | 以小端序读取 | | ucs-2 | 以小端序读取 | | utf16le | 以小端序读取 | | utf-16le | 以小端序读取 | | utf-8 |  | | utf8 |  | | latin1 |  | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| ascii |  |
| base64 |  |
| binary |  |
| hex |  |
| ucs2 | 以小端序读取 |
| ucs-2 | 以小端序读取 |
| utf16le | 以小端序读取 |
| utf-16le | 以小端序读取 |
| utf-8 |  |
| utf8 |  |
| latin1 |  |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.appendFileSync(string filePath, string|ArrayBuffer data, string encoding)

基础库 2.1.0 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.appendFileSync.html

**string encoding**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| ascii |  |  |
| base64 |  |  |
| binary |  |  |
| hex |  |  |
| ucs2 | 以小端序读取 |  |
| ucs-2 | 以小端序读取 |  |
| utf16le | 以小端序读取 |  |
| utf-16le | 以小端序读取 |  |
| utf-8 |  |  |
| utf8 |  |  |
| latin1 |  |  |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.close(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.close.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| fd | string |  | 是 | 需要被关闭的文件描述符。fd 通过 [FileSystemManager.open](FileSystemManager.open.html) 或 [FileSystemManager.openSync](FileSystemManager.openSync.html) 接口获得 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### undefined FileSystemManager.closeSync(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.closeSync.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| fd | string |  | 是 | 需要被关闭的文件描述符。fd 通过 [FileSystemManager.open](FileSystemManager.open.html) 或 [FileSystemManager.openSync](FileSystemManager.openSync.html) 接口获得 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.copyFile(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.copyFile.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| srcPath | string |  | 是 | 源文件路径，支持本地路径 |
| destPath | string |  | 是 | 目标文件路径，支持本地路径 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.copyFileSync(string srcPath, string destPath)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.copyFileSync.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.fstat(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.fstat.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| fd | string |  | 是 | 文件描述符。fd 通过 [FileSystemManager.open](FileSystemManager.open.html) 或 [FileSystemManager.openSync](FileSystemManager.openSync.html) 接口获得 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| stats | [Stats](Stats.html) | Stats 对象，包含了文件的状态信息 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### Stats FileSystemManager.fstatSync(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.fstatSync.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| fd | string |  | 是 | 文件描述符。fd 通过 [FileSystemManager.open](FileSystemManager.open.html) 或 [FileSystemManager.openSync](FileSystemManager.openSync.html) 接口获得 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.ftruncate(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.ftruncate.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| fd | string |  | 是 | 文件描述符。fd 通过 [FileSystemManager.open](FileSystemManager.open.html) 或 [FileSystemManager.openSync](FileSystemManager.openSync.html) 接口获得 |
| length | number |  | 是 | 截断位置，默认0。如果 length 小于文件长度（单位：字节），则只有前面 length 个字节会保留在文件中，其余内容会被删除；如果 length 大于文件长度，则会对其进行扩展，并且扩展部分将填充空字节（'\0'） |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### undefined FileSystemManager.ftruncateSync(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.ftruncateSync.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| fd | string |  | 是 | 文件描述符。fd 通过 [FileSystemManager.open](FileSystemManager.open.html) 或 [FileSystemManager.openSync](FileSystemManager.openSync.html) 接口获得 |
| length | number |  | 是 | 截断位置，默认0。如果 length 小于文件长度（单位：字节），则只有前面 length 个字节会保留在文件中，其余内容会被删除；如果 length 大于文件长度，则会对其进行扩展，并且扩展部分将填充空字节（'\0'） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.getFileInfo(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.getFileInfo.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | filePath | string |  | 是 | 要读取的文件路径 (本地路径) |
|  | digestAlgorithm | string | md5 | 否 | 计算文件摘要的算法 |
|  | | 合法值 | 说明 | | --- | --- | | md5 | md5 算法 | | sha1 | sha1 算法 | | sha256 | sha256 算法 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| md5 | md5 算法 |
| sha1 | sha1 算法 |
| sha256 | sha256 算法 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| size | number | 文件大小，以字节为单位 |
| digest | string | 按照传入的 digestAlgorithm 计算得出的的文件摘要 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.getSavedFileList(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.getSavedFileList.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | fileList | Array.<Object> | 文件数组 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | filePath | string | 文件路径 (本地路径) | |  | size | number | 本地文件大小，以字节为单位 | |  | createTime | number | 文件保存时的时间戳，从1970/01/01 08:00:00 到当前时间的秒数 | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | filePath | string | 文件路径 (本地路径) |
|  | size | number | 本地文件大小，以字节为单位 |
|  | createTime | number | 文件保存时的时间戳，从1970/01/01 08:00:00 到当前时间的秒数 |

---

### FileSystemManager.mkdir(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.mkdir.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| dirPath | string |  | 是 | 创建的目录路径 (本地路径) |  |
| recursive | boolean | false | 否 | 是否在递归创建该目录的上级目录后再创建该目录。如果对应的上级目录已经存在，则不创建该上级目录。如 dirPath 为 a/b/c/d 且 recursive 为 true，将创建 a 目录，再在 a 目录下创建 b 目录，以此类推直至创建 a/b/c 目录下的 d 目录。 | [2.3.0](../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.mkdirSync(string dirPath, boolean recursive)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.mkdirSync.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.open(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.open.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | filePath | string |  | 是 | 文件路径 (本地路径) |
|  | flag | string | r | 否 | 文件系统标志，默认值: 'r' |
|  | | 合法值 | 说明 | | --- | --- | | a | 打开文件用于追加。 如果文件不存在，则创建该文件 | | ax | 类似于 'a'，但如果路径存在，则失败 | | a+ | 打开文件用于读取和追加。 如果文件不存在，则创建该文件 | | ax+ | 类似于 'a+'，但如果路径存在，则失败 | | as | 打开文件用于追加（在同步模式中）。 如果文件不存在，则创建该文件 | | as+ | 打开文件用于读取和追加（在同步模式中）。 如果文件不存在，则创建该文件 | | r | 打开文件用于读取。 如果文件不存在，则会发生异常 | | r+ | 打开文件用于读取和写入。 如果文件不存在，则会发生异常 | | w | 打开文件用于写入。 如果文件不存在则创建文件，如果文件存在则截断文件 | | wx | 类似于 'w'，但如果路径存在，则失败 | | w+ | 打开文件用于读取和写入。 如果文件不存在则创建文件，如果文件存在则截断文件 | | wx+ | 类似于 'w+'，但如果路径存在，则失败 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| a | 打开文件用于追加。 如果文件不存在，则创建该文件 |
| ax | 类似于 'a'，但如果路径存在，则失败 |
| a+ | 打开文件用于读取和追加。 如果文件不存在，则创建该文件 |
| ax+ | 类似于 'a+'，但如果路径存在，则失败 |
| as | 打开文件用于追加（在同步模式中）。 如果文件不存在，则创建该文件 |
| as+ | 打开文件用于读取和追加（在同步模式中）。 如果文件不存在，则创建该文件 |
| r | 打开文件用于读取。 如果文件不存在，则会发生异常 |
| r+ | 打开文件用于读取和写入。 如果文件不存在，则会发生异常 |
| w | 打开文件用于写入。 如果文件不存在则创建文件，如果文件存在则截断文件 |
| wx | 类似于 'w'，但如果路径存在，则失败 |
| w+ | 打开文件用于读取和写入。 如果文件不存在则创建文件，如果文件存在则截断文件 |
| wx+ | 类似于 'w+'，但如果路径存在，则失败 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| fd | string | 文件描述符 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### string FileSystemManager.openSync(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.openSync.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | filePath | string |  | 是 | 文件路径 (本地路径) |
|  | flag | string | r | 否 | 文件系统标志，默认值: 'r' |
|  | | 合法值 | 说明 | | --- | --- | | a | 打开文件用于追加。 如果文件不存在，则创建该文件 | | ax | 类似于 'a'，但如果路径存在，则失败 | | a+ | 打开文件用于读取和追加。 如果文件不存在，则创建该文件 | | ax+ | 类似于 'a+'，但如果路径存在，则失败 | | as | 打开文件用于追加（在同步模式中）。 如果文件不存在，则创建该文件 | | as+ | 打开文件用于读取和追加（在同步模式中）。 如果文件不存在，则创建该文件 | | r | 打开文件用于读取。 如果文件不存在，则会发生异常 | | r+ | 打开文件用于读取和写入。 如果文件不存在，则会发生异常 | | w | 打开文件用于写入。 如果文件不存在则创建文件，如果文件存在则截断文件 | | wx | 类似于 'w'，但如果路径存在，则失败 | | w+ | 打开文件用于读取和写入。 如果文件不存在则创建文件，如果文件存在则截断文件 | | wx+ | 类似于 'w+'，但如果路径存在，则失败 | | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| a | 打开文件用于追加。 如果文件不存在，则创建该文件 |
| ax | 类似于 'a'，但如果路径存在，则失败 |
| a+ | 打开文件用于读取和追加。 如果文件不存在，则创建该文件 |
| ax+ | 类似于 'a+'，但如果路径存在，则失败 |
| as | 打开文件用于追加（在同步模式中）。 如果文件不存在，则创建该文件 |
| as+ | 打开文件用于读取和追加（在同步模式中）。 如果文件不存在，则创建该文件 |
| r | 打开文件用于读取。 如果文件不存在，则会发生异常 |
| r+ | 打开文件用于读取和写入。 如果文件不存在，则会发生异常 |
| w | 打开文件用于写入。 如果文件不存在则创建文件，如果文件存在则截断文件 |
| wx | 类似于 'w'，但如果路径存在，则失败 |
| w+ | 打开文件用于读取和写入。 如果文件不存在则创建文件，如果文件存在则截断文件 |
| wx+ | 类似于 'w+'，但如果路径存在，则失败 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.read(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.read.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| fd | string |  | 是 | 文件描述符。fd 通过 [FileSystemManager.open](FileSystemManager.open.html) 或 [FileSystemManager.openSync](FileSystemManager.openSync.html) 接口获得 |
| arrayBuffer | ArrayBuffer |  | 是 | 数据写入的缓冲区，必须是 ArrayBuffer 实例 |
| offset | number | 0 | 否 | 缓冲区中的写入偏移量，默认0 |
| length | number | 0 | 否 | 要从文件中读取的字节数，默认0 |
| position | number |  | 否 | 文件读取的起始位置，如不传或传 null，则会从当前文件指针的位置读取。如果 position 是正整数，则文件指针位置会保持不变并从 position 读取文件。 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| bytesRead | number | 实际读取的字节数 |
| arrayBuffer | ArrayBuffer | 被写入的缓存区的对象，即接口入参的 arrayBuffer |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.readCompressedFile(Object object)

基础库 2.21.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.readCompressedFile.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | filePath | string |  | 是 | 要读取的文件的路径 (本地用户文件或代码包文件) |
|  | compressionAlgorithm | string |  | 是 | 文件压缩类型，目前仅支持 'br'。 |
|  | | 合法值 | 说明 | | --- | --- | | br | brotli压缩文件 | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| br | brotli压缩文件 |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | ArrayBuffer | 文件内容 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### ArrayBuffer FileSystemManager.readCompressedFileSync(Object object)

基础库 2.21.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.readCompressedFileSync.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | filePath | string |  | 是 | 要读取的文件的路径 (本地用户文件或代码包文件) |
|  | compressionAlgorithm | string |  | 是 | 文件压缩类型，目前仅支持 'br'。 |
|  | | 合法值 | 说明 | | --- | --- | | br | brotli压缩文件 | | | | | |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| br | brotli压缩文件 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.readdir(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.readdir.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| dirPath | string |  | 是 | 要读取的目录路径 (本地路径) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| files | Array.<string> | 指定目录下的文件名数组。 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### Array.<string> FileSystemManager.readdirSync(string dirPath)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.readdirSync.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.readFile(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.readFile.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- | --- |
|  | filePath | string |  | 是 | 要读取的文件的路径 (本地路径) |  |
|  | encoding | string |  | 否 | 指定读取文件的字符编码，如果不传 encoding，则以 ArrayBuffer 格式读取文件的二进制内容 |  |
|  | | 合法值 | 说明 | | --- | --- | | ascii |  | | base64 |  | | binary |  | | hex |  | | ucs2 | 以小端序读取 | | ucs-2 | 以小端序读取 | | utf16le | 以小端序读取 | | utf-16le | 以小端序读取 | | utf-8 |  | | utf8 |  | | latin1 |  | | | | | | |
|  | position | number |  | 否 | 从文件指定位置开始读，如果不指定，则从文件头开始读。读取的范围应该是左闭右开区间 [position, position+length)。有效范围：[0, fileLength - 1]。单位：byte | [2.10.0](../../guide/runtime/client-lib/compatibility.html) |
|  | length | number |  | 否 | 指定文件的长度，如果不指定，则读到文件末尾。有效范围：[1, fileLength]。单位：byte | [2.10.0](../../guide/runtime/client-lib/compatibility.html) |
|  | success | function |  | 否 | 接口调用成功的回调函数 |  |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |  |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| ascii |  |
| base64 |  |
| binary |  |
| hex |  |
| ucs2 | 以小端序读取 |
| ucs-2 | 以小端序读取 |
| utf16le | 以小端序读取 |
| utf-16le | 以小端序读取 |
| utf-8 |  |
| utf8 |  |
| latin1 |  |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | string/ArrayBuffer | 文件内容 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### string|ArrayBuffer FileSystemManager.readFileSync(string filePath, string encoding, number position, number length)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.readFileSync.html

**string encoding**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| ascii |  |  |
| base64 |  |  |
| binary |  |  |
| hex |  |  |
| ucs2 | 以小端序读取 |  |
| ucs-2 | 以小端序读取 |  |
| utf16le | 以小端序读取 |  |
| utf-16le | 以小端序读取 |  |
| utf-8 |  |  |
| utf8 |  |  |
| latin1 |  |  |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### ReadResult FileSystemManager.readSync(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.readSync.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| fd | string |  | 是 | 文件描述符。fd 通过 [FileSystemManager.open](FileSystemManager.open.html) 或 [FileSystemManager.openSync](FileSystemManager.openSync.html) 接口获得 |
| arrayBuffer | ArrayBuffer |  | 是 | 数据写入的缓冲区，必须是 ArrayBuffer 实例 |
| offset | number | 0 | 否 | 缓冲区中的写入偏移量，默认0 |
| length | number | 0 | 否 | 要从文件中读取的字节数，默认0 |
| position | number |  | 否 | 文件读取的起始位置，如不传或传 null，则会从当前文件指针的位置读取。如果 position 是正整数，则文件指针位置会保持不变并从 position 读取文件。 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.readZipEntry(Object object)

基础库 2.17.3 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.readZipEntry.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | filePath | string |  | 是 | 要读取的压缩包的路径 (本地路径) |
|  | encoding | string |  | 否 | 统一指定读取文件的字符编码，只在 entries 值为"all"时有效。如果 entries 值为"all"且不传 encoding，则以 ArrayBuffer 格式读取文件的二进制内容 |
|  | | 合法值 | 说明 | | --- | --- | | ascii |  | | base64 |  | | binary |  | | hex |  | | ucs2 | 以小端序读取 | | ucs-2 | 以小端序读取 | | utf16le | 以小端序读取 | | utf-16le | 以小端序读取 | | utf-8 |  | | utf8 |  | | latin1 |  | | | | | |
|  | entries | Array.<Object>/'all' |  | 是 | 要读取的压缩包内的文件列表（当传入"all" 时表示读取压缩包内所有文件） |
|  | |  | 结构属性 | 类型 | 默认值 | 必填 | 说明 | | --- | --- | --- | --- | --- | --- | |  | path | string |  | 是 | 压缩包内文件路径 | |  | encoding | string |  | 否 | 指定读取文件的字符编码，如果不传 encoding，则以 ArrayBuffer 格式读取文件的二进制内容 | |  | | 合法值 | 说明 | | --- | --- | | ascii |  | | base64 |  | | binary |  | | hex |  | | ucs2 | 以小端序读取 | | ucs-2 | 以小端序读取 | | utf16le | 以小端序读取 | | utf-16le | 以小端序读取 | | utf-8 |  | | utf8 |  | | latin1 |  | | | | | | |  | position | number |  | 否 | 从文件指定位置开始读，如果不指定，则从文件头开始读。读取的范围应该是左闭右开区间 [position, position+length)。有效范围：[0, fileLength - 1]。单位：byte | |  | length | number |  | 否 | 指定文件的长度，如果不指定，则读到文件末尾。有效范围：[1, fileLength]。单位：byte | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| ascii |  |
| base64 |  |
| binary |  |
| hex |  |
| ucs2 | 以小端序读取 |
| ucs-2 | 以小端序读取 |
| utf16le | 以小端序读取 |
| utf-16le | 以小端序读取 |
| utf-8 |  |
| utf8 |  |
| latin1 |  |

**Object object**

|  | 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | path | string |  | 是 | 压缩包内文件路径 |
|  | encoding | string |  | 否 | 指定读取文件的字符编码，如果不传 encoding，则以 ArrayBuffer 格式读取文件的二进制内容 |
|  | | 合法值 | 说明 | | --- | --- | | ascii |  | | base64 |  | | binary |  | | hex |  | | ucs2 | 以小端序读取 | | ucs-2 | 以小端序读取 | | utf16le | 以小端序读取 | | utf-16le | 以小端序读取 | | utf-8 |  | | utf8 |  | | latin1 |  | | | | | |
|  | position | number |  | 否 | 从文件指定位置开始读，如果不指定，则从文件头开始读。读取的范围应该是左闭右开区间 [position, position+length)。有效范围：[0, fileLength - 1]。单位：byte |
|  | length | number |  | 否 | 指定文件的长度，如果不指定，则读到文件末尾。有效范围：[1, fileLength]。单位：byte |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| ascii |  |
| base64 |  |
| binary |  |
| hex |  |
| ucs2 | 以小端序读取 |
| ucs-2 | 以小端序读取 |
| utf16le | 以小端序读取 |
| utf-16le | 以小端序读取 |
| utf-8 |  |
| utf8 |  |
| latin1 |  |

**Object object**

|  | 属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | entries | Object | 文件读取结果。res.entries 是一个对象，key是文件路径，value是一个对象 FileItem ，表示该文件的读取结果。每个 FileItem 包含 data （文件内容） 和 errMsg （错误信息） 属性。 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | path | Object | 文件路径 | |  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | data | string/ArrayBuffer | 文件内容 | |  | errMsg | string | 错误信息 | | | | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | path | Object | 文件路径 |
|  | |  | 结构属性 | 类型 | 说明 | | --- | --- | --- | --- | |  | data | string/ArrayBuffer | 文件内容 | |  | errMsg | string | 错误信息 | | | |

**Object object**

|  | 结构属性 | 类型 | 说明 |
| --- | --- | --- | --- |
|  | data | string/ArrayBuffer | 文件内容 |
|  | errMsg | string | 错误信息 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.removeSavedFile(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.removeSavedFile.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| filePath | string |  | 是 | 需要删除的文件路径 (本地路径) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.rename(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.rename.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| oldPath | string |  | 是 | 源文件路径，支持本地路径 |
| newPath | string |  | 是 | 新文件路径，支持本地路径 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.renameSync(string oldPath, string newPath)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.renameSync.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.rmdir(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.rmdir.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| dirPath | string |  | 是 | 要删除的目录路径 (本地路径) |  |
| recursive | boolean | false | 否 | 是否递归删除目录。如果为 true，则删除该目录和该目录下的所有子目录以及文件。 | [2.3.0](../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.rmdirSync(string dirPath, boolean recursive)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.rmdirSync.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.saveFile(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.saveFile.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| tempFilePath | string |  | 是 | 临时存储文件路径 (本地路径) |
| filePath | string |  | 否 | 要存储的文件路径 (本地路径) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| savedFilePath | string | 存储后的文件路径 (本地路径) |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### string FileSystemManager.saveFileSync(string tempFilePath, string filePath)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.saveFileSync.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.stat(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.stat.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| path | string |  | 是 | 文件/目录路径 (本地路径) |  |
| recursive | boolean | false | 否 | 是否递归获取目录下的每个文件的 Stats 信息 | [2.3.0](../../guide/runtime/client-lib/compatibility.html) |
| success | function |  | 否 | 接口调用成功的回调函数 |  |
| fail | function |  | 否 | 接口调用失败的回调函数 |  |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |  |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| stats | [Stats](Stats.html)/Array.<[FileStats](FileStats.html)> | 当 recursive 为 false 时，res.stats 是一个 Stats 对象。当 recursive 为 true 且 path 是一个目录的路径时，res.stats 是一个 Array，数组的每一项是一个对象，每个对象包含 path 和 stats。 |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### Stats|Array.<FileStats> FileSystemManager.statSync(string path, boolean recursive)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.statSync.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.truncate(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.truncate.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| filePath | string |  | 是 | 要截断的文件路径 (本地路径) |
| length | number | 0 | 否 | 截断位置，默认0。如果 length 小于文件长度（字节），则只有前面 length 个字节会保留在文件中，其余内容会被删除；如果 length 大于文件长度，则会对其进行扩展，并且扩展部分将填充空字节（'\0'） |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### undefined FileSystemManager.truncateSync(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.truncateSync.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| filePath | string |  | 是 | 要截断的文件路径 (本地路径) |
| length | number | 0 | 否 | 截断位置，默认0。如果 length 小于文件长度（字节），则只有前面 length 个字节会保留在文件中，其余内容会被删除；如果 length 大于文件长度，则会对其进行扩展，并且扩展部分将填充空字节（'\0'） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.unlink(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.unlink.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| filePath | string |  | 是 | 要删除的文件路径 (本地路径) |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.unlinkSync(string filePath)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.unlinkSync.html

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.unzip(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.unzip.html

**Object object**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| zipFilePath | string |  | 是 | 源文件路径，支持本地路径, 只可以是 zip 压缩文件 |
| targetPath | string |  | 是 | 目标目录路径, 支持本地路径 |
| success | function |  | 否 | 接口调用成功的回调函数 |
| fail | function |  | 否 | 接口调用失败的回调函数 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.write(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.write.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | fd | string |  | 是 | 文件描述符。fd 通过 [FileSystemManager.open](FileSystemManager.open.html) 或 [FileSystemManager.openSync](FileSystemManager.openSync.html) 接口获得 |
|  | data | string/ArrayBuffer |  | 是 | 写入的内容，类型为 String 或 ArrayBuffer |
|  | offset | number | 0 | 否 | 只在 data 类型是 ArrayBuffer 时有效，决定 ArrayBuffer 中要被写入的部位，即 ArrayBuffer 中的索引，默认0 |
|  | length | number |  | 否 | 只在 data 类型是 ArrayBuffer 时有效，指定要写入的字节数，默认为 ArrayBuffer 从0开始偏移 offset 个字节后剩余的字节数 |
|  | encoding | string | utf8 | 否 | 只在 data 类型是 String 时有效，指定写入文件的字符编码，默认为 utf8 |
|  | | 合法值 | 说明 | | --- | --- | | ascii |  | | base64 |  | | binary |  | | hex |  | | ucs2 | 以小端序读取 | | ucs-2 | 以小端序读取 | | utf16le | 以小端序读取 | | utf-16le | 以小端序读取 | | utf-8 |  | | utf8 |  | | latin1 |  | | | | | |
|  | position | number |  | 否 | 指定文件开头的偏移量，即数据要被写入的位置。当 position 不传或者传入非 Number 类型的值时，数据会被写入当前指针所在位置。 |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| ascii |  |
| base64 |  |
| binary |  |
| hex |  |
| ucs2 | 以小端序读取 |
| ucs-2 | 以小端序读取 |
| utf16le | 以小端序读取 |
| utf-16le | 以小端序读取 |
| utf-8 |  |
| utf8 |  |
| latin1 |  |

**Object object**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| bytesWritten | number | 实际被写入到文件中的字节数（注意，被写入的字节数不一定与被写入的字符串字符数相同） |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.writeFile(Object object)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.writeFile.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | filePath | string |  | 是 | 要写入的文件路径 (本地路径) |
|  | data | string/ArrayBuffer |  | 是 | 要写入的文本或二进制数据 |
|  | encoding | string | utf8 | 否 | 指定写入文件的字符编码 |
|  | | 合法值 | 说明 | | --- | --- | | ascii |  | | base64 | （注意，选择 base64 编码，data 只需要传 base64 内容本身，不要传 Data URI 前缀，否则会报 fail base64 encode error 错误。例如，传 aGVsbG8= 而不是传 data:image/png;base64,aGVsbG8= ） | | binary |  | | hex |  | | ucs2 | 以小端序读取 | | ucs-2 | 以小端序读取 | | utf16le | 以小端序读取 | | utf-16le | 以小端序读取 | | utf-8 |  | | utf8 |  | | latin1 |  | | | | | |
|  | success | function |  | 否 | 接口调用成功的回调函数 |
|  | fail | function |  | 否 | 接口调用失败的回调函数 |
|  | complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| ascii |  |
| base64 | （注意，选择 base64 编码，data 只需要传 base64 内容本身，不要传 Data URI 前缀，否则会报 fail base64 encode error 错误。例如，传 aGVsbG8= 而不是传 data:image/png;base64,aGVsbG8= ） |
| binary |  |
| hex |  |
| ucs2 | 以小端序读取 |
| ucs-2 | 以小端序读取 |
| utf16le | 以小端序读取 |
| utf-16le | 以小端序读取 |
| utf-8 |  |
| utf8 |  |
| latin1 |  |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### FileSystemManager.writeFileSync(string filePath, string|ArrayBuffer data, string encoding)

以Promise 风格调用：不支持

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.writeFileSync.html

**string encoding**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| ascii |  |  |
| base64 | （注意，选择 base64 编码，data 只需要传 base64 内容本身，不要传 Data URI 前缀，否则会报 fail base64 encode error 错误。例如，传 aGVsbG8= 而不是传 data:image/png;base64,aGVsbG8= ） |  |
| binary |  |  |
| hex |  |  |
| ucs2 | 以小端序读取 |  |
| ucs-2 | 以小端序读取 |  |
| utf16le | 以小端序读取 |  |
| utf-16le | 以小端序读取 |  |
| utf-8 |  |  |
| utf8 |  |  |
| latin1 |  |  |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### WriteResult FileSystemManager.writeSync(Object object)

基础库 2.16.1 开始支持，低版本需做兼容处理。

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/FileSystemManager.writeSync.html

**Object object**

|  | 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
|  | fd | string |  | 是 | 文件描述符。fd 通过 [FileSystemManager.open](FileSystemManager.open.html) 或 [FileSystemManager.openSync](FileSystemManager.openSync.html) 接口获得 |
|  | data | string/ArrayBuffer |  | 是 | 写入的内容，类型为 String 或 ArrayBuffer |
|  | offset | number | 0 | 否 | 只在 data 类型是 ArrayBuffer 时有效，决定 ArrayBuffer 中要被写入的部位，即 ArrayBuffer 中的索引，默认0 |
|  | length | number |  | 否 | 只在 data 类型是 ArrayBuffer 时有效，指定要写入的字节数，默认为 ArrayBuffer 从0开始偏移 offset 个字节后剩余的字节数 |
|  | encoding | string | utf8 | 否 | 只在 data 类型是 String 时有效，指定写入文件的字符编码，默认为 utf8 |
|  | | 合法值 | 说明 | | --- | --- | | ascii |  | | base64 |  | | binary |  | | hex |  | | ucs2 | 以小端序读取 | | ucs-2 | 以小端序读取 | | utf16le | 以小端序读取 | | utf-16le | 以小端序读取 | | utf-8 |  | | utf8 |  | | latin1 |  | | | | | |
|  | position | number |  | 否 | 指定文件开头的偏移量，即数据要被写入的位置。当 position 不传或者传入非 Number 类型的值时，数据会被写入当前指针所在位置。 |

**Object object**

| 合法值 | 说明 |
| --- | --- |
| ascii |  |
| base64 |  |
| binary |  |
| hex |  |
| ucs2 | 以小端序读取 |
| ucs-2 | 以小端序读取 |
| utf16le | 以小端序读取 |
| utf-16le | 以小端序读取 |
| utf-8 |  |
| utf8 |  |
| latin1 |  |

**错误**

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 1300001 | operation not permitted | 操作不被允许（例如，filePath 预期传入一个文件而实际传入一个目录） |
| 1300002 | no such file or directory ${path} | 文件/目录不存在，或者目标文件路径的上层目录不存在 |
| 1300005 | Input/output error | 输入输出流不可用 |
| 1300009 | bad file descriptor | 无效的文件描述符 |
| 1300013 | permission denied | 权限错误，文件是只读或只写 |
| 1300014 | Path permission denied | 传入的路径没有权限 |
| 1300020 | not a directory | dirPath 指定路径不是目录，常见于指定的写入路径的上级路径为一个文件的情况 |
| 1300021 | Is a directory | 指定路径是一个目录 |
| 1300022 | Invalid argument | 无效参数，可以检查length或offset是否越界 |
| 1300036 | File name too long | 文件名过长 |
| 1300066 | directory not empty | 目录不为空 |
| 1300201 | system error | 系统接口调用失败 |
| 1300202 | the maximum size of the file storage limit is exceeded | 存储空间不足，或文件大小超出上限（上限100M） |
| 1300203 | base64 encode error | 字符编码转换失败（例如 base64 格式错误） |
| 1300300 | sdcard not mounted | android sdcard 挂载失败 |
| 1300301 | unable to open as fileType | 无法以fileType打开文件 |
| 1301000 | permission denied, cannot access file path | 目标路径无访问权限（usr目录） |
| 1301002 | data to write is empty | 写入数据为空 |
| 1301003 | illegal operation on a directory | 不可对目录进行此操作（例如，指定的 filePath 是一个已经存在的目录） |
| 1301004 | illegal operation on a package directory | 不可对代码包目录进行此操作 |
| 1301005 | file already exists ${dirPath} | 已有同名文件或目录 |
| 1301006 | value of length is out of range | 传入的 length 不合法 |
| 1301007 | value of offset is out of range | 传入的 offset 不合法 |
| 1301009 | value of position is out of range | position值越界 |
| 1301100 | store directory is empty | store目录为空 |
| 1301102 | unzip open file fail | 压缩文件打开失败 |
| 1301103 | unzip entry fail | 解压单个文件失败 |
| 1301104 | unzip fail | 解压失败 |
| 1301111 | brotli decompress fail | brotli解压失败（例如，指定的 compressionAlgorithm 与文件实际压缩格式不符） |
| 1301112 | tempFilePath file not exist | 指定的 tempFilePath 找不到文件 |
| 1302001 | fail permission denied | 指定的 fd 路径没有读权限/没有写权限 |
| 1302002 | excced max concurrent fd limit | fd数量已达上限 |
| 1302003 | invalid flag | 无效的flag |
| 1302004 | permission denied when open using flag | 无法使用flag标志打开文件 |
| 1302005 | array buffer does not exist | 未传入arrayBuffer |
| 1302100 | array buffer is readonly | arrayBuffer只读 |

---

### ReadResult

文件读取结果。 通过FileSystemManager.readSync接口返回

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/ReadResult.html

---

### Stats

相关文档:文件系统

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/Stats.html

---

### boolean Stats.isDirectory()

相关文档:文件系统

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/Stats.isDirectory.html

---

### boolean Stats.isFile()

相关文档:文件系统

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/Stats.isFile.html

---

### WriteResult

文件写入结果。 通过FileSystemManager.writeSync接口返回

官方 / Source: https://developers.weixin.qq.com/minigame/dev/api/file/WriteResult.html

---

<!-- pages: 54 -->
