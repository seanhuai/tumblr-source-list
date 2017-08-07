# tumblr-source-list

一个简单的Tumblr资源工具，用于获取指定用户的图片或视频信息

### 工具下载

克隆本仓库到本地 命令如下

```
git clone https://github.com/seanhuai/tumblr-source-list
```
### 使用方法

运行 app.py 文件，同时传递参数

```
tumblr-source-list> python .\app.py username limit mediatype
```

其中 username 为必填项，username 即用户二级域名，如 offo.tumblr.com，则用户名是 offo

limit 为获取内容的页数，如赋值则取值，如未赋值默认值为 3

mediatype 为获取内容的类型，仅限 `pics`、`video` 和 `both` 三种，如未赋值默认值为 `pics`

示例：

```
tumblr-source-list> python .\app.py u44002 
```

本例获取 u44002 用户近期 3 页的图片内容

```
tumblr-source-list> python .\app.py u44002 5 both
```

本例获取 u44002 用户近期 5 页的图片和视频内容

生成的列表文件位于用户同名文件夹，请使用下载工具完成下载

### 代理设置

在中国大陆使用，需设置网络代理。

默认设置代理为监听本地 1080 端口，适用 Shadowsocks 用户。

更改代理设置，修改 getSource() host/port 变量值即可。

### 获取限制

官方限制，每一认证密钥每小时访问次数仅限 1000 次，同一密钥同一天限制访问 5000 次。

更换密钥，修改 getSource() key 变量值即可。

### 更新计划

近期将发布工作在 Windows 平台的 exe 程序。

下一版本计划：实现根据关键字搜索并获取内容，实现多 key 负载均衡。