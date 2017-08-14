# tumblr-source-list

一个简单的Tumblr资源工具，用于获取指定用户的图片或视频信息

当前版本： 0.170814.2 fixed

### 工具下载

克隆本仓库到本地 命令如下

```
git clone https://github.com/seanhuai/tumblr-source-list
```
### 使用方法

运行 app.py 文件，同时传递参数

#### 用户模式

```
tumblr-source-list> python .\app.py username username mediatype limit
```

`app.py username` 后接 用户名（即用户二级域名）、媒体类型（photo 或 video）和 获取**内容页数**。

>**内容页数**：limit 指后台获取的内容页数，1 页约为 20 篇指定类型贴。由于汤不热允许博主设置每页显示数目，所以和实际显示的前台页数不同。

示例：

```
tumblr-source-list> python .\app.py username u44002 photo 3 
```

本例获取 u44002 用户近 3 页的图片内容

```
tumblr-source-list> python .\app.py username u44002 video 5 
```

本例获取 u44002 用户近 5 页的视频内容

生成的列表文件位于用户同名文件夹，请使用下载工具完成下载

#### 链接模式

```
tumblr-source-list> python .\app.py posturl url
```

`app.py posturl` 后接 内容所在网页地址。

示例：

```
tumblr-source-list> python .\app.py posturl https://wsyghf.tumblr.com/post/150478441406/
```

本例获取 wsyghf 用户指定的图片内容

![](http://68.media.tumblr.com/ad6ae078e300136120d1127c4e8c4b4a/tumblr_odkypczpCM1utv5hpo6_1280.jpg)

```
tumblr-source-list> python .\app.py posturl https://donshofer.tumblr.com/post/163730046536/
```

本例获取 donshofer 用户指定的图片内容

![](https://68.media.tumblr.com/dad7984efd2c3bb47ccd088c2556edf6/tumblr_ou2wjnqOFS1rjk2kao3_1280.jpg)

两例均为图片，视频为同样使用方法。

生成的列表文件位于用户同名文件夹，请使用下载工具完成下载。

### 代理设置

在中国大陆使用，需设置网络代理。

默认设置代理为监听本地 1080 端口，适用 Shadowsocks 用户。

更改代理设置，修改 packages/_profiles.py host/port 变量值即可。

### 获取限制

官方限制，每一认证密钥每小时访问次数仅限 1000 次，同一密钥同一天限制访问 5000 次。

更换密钥，或设置备用密钥，修改 packages/_profiles.py api 变量值（组）即可。

### 常见问题

1. 返回 401 错误：apikey 不正确，或输入的网址格式错误
2. 返回 429 错误：超出 api 获取限制，请自行注册 apikey，详情访问 api.tumblr.com
3. 获取内容页数不符：**获取内容页数**指后台获取的内容页数，1 页约为 20 篇指定类型贴
4. 显示中文乱码：字符编码不兼容，修改终端字符编码

### 更新计划

近期将发布工作在 Windows 平台的 exe 程序。

下一版本计划：实现根据关键字搜索并获取内容，实现多 key 负载均衡。