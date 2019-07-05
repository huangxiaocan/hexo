---
title: Hexo教程：腾讯云Centos7.2搭建hexo博客三部曲  
tags:
  - hexo  
categories: hexo  
description: 腾讯云Centos7.2搭建hexo博客三部曲  
abbrlink: 7b7e  
date: 2019-06-19 12:15:08  
---
本篇内容用来讲述如何将 hexo 博客部署到腾讯云的服务器上。
只要通过三步即可成功部署：

1，云服务器端 git 的配置  
2，Nginx 的配置  
3，本地端 hexo 的设置更改  

<!--less-->  

下面开始正式讲解如何部署。

## 准备工作

### 前期准备

1，一个腾讯云服务器  
2，hexo 本地博客
顺便说下我的服务器环境：  

操作系统	CPU	内存	带宽  
CentOS 7.2 64位	1核	2GB	1Mbps


### 进入云服务器中

1，首先点击下边网站，登录你的进入云服务器的控制台 
腾讯云服务器的控制台：https://console.cloud.tencent.com/cvm/index  

2，左边菜单选择云主机，然后找到你的服务器。点击登录

3，输入密码，进入 云服务器 CentOS中。（初始密码在控制台右上角的消息列表中）

## 云服务器安装git
### 安装依赖库和编译工具  
安装依赖库：
``` bash
$ yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel   
```  
安装编译工具：
``` bash
$ yum install gcc perl-ExtUtils-MakeMaker package
```  
### 安装下载 git  
选择一个目录来存放下载下来的 git 安装包。这里选择了/usr/local/src 目录  
``` bash
$ cd /usr/local/src  
```  
到官网找一个新版稳定的源码包下载到 /usr/local/src 文件夹里 
``` bash
$ wget https://www.kernel.org/pub/software/scm/git/git-2.16.2.tar.gz
```  
### 解压编译 git
在当前目录下解压 git-2.16.2.tar.gz  
``` bash
$ wget tar -zvxf git-2.16.2.tar.gz
```  
进入 git-2.16.2.tar.gz 目录下  
``` bash
$ cd git-2.16.2
```   
执行编译  
``` bash
$ make all prefix=/usr/local/git
```   
安装 git 到 /usr/local/git 目录下  
``` bash
$ make install prefix=/usr/local/git
```   
### 配置 git 环境变量
将 git 加入 PATH 目录中  
``` bash
$ echo 'export PATH=$PATH:/usr/local/git/bin' >> /etc/bashrc
```  
使 git 环境变量生效  
``` bash
$ source /etc/bashrc
```   
查看 git 版本  
``` bash
$ git --version
```  
如果此时能查看到 git 的版本号，说明我们已经安装成功了。  
创建 git 仓库，用于存放博客网站资源
在 home/git 的目录下，创建一个名为hexoBlog的裸仓库（bare repo）。   
如果没有 home/git 目录，需要先创建；然后修改目录的所有权和用户权限。  
``` bash   
$ mkdir /home/git/  
```   
``` bash   
$ chown -R $USER:$USER /home/git/ 
```  
``` bash   
$ chmod -R 755 /home/git/ 
```  
然后，执行如下命令：  
``` bash   
$ cd /home/git/
```  
``` bash   
$ git init --bare hexoBlog.git   
```     
刚才这一步主要创建一个裸的 git 仓库。  
创建一个新的 git 钩子，用于自动部署。  
在 /home/git/hexoBlog.git 下，有一个自动生成的 hooks 文件夹。我们需要在里边新建一个新的钩子文件 post-receive。   
``` bash   
$ vim /home/git/hexoBlog.git/hooks/post-receive  
```   
按 i 键进入文件的编辑模式，在该文件中添加两行代码（将下边的代码粘贴进去)，指定 Git 的工作树（源代码）和 Git 目录（配置文件等）   
``` bash   
$ git --work-tree=/home/hexoBlog --git-dir=/home/git/hexoBlog.git checkout -f 
```  
然后，按 Esc 键退出编辑模式，输入:wq 保存退出。  
修改文件权限，使得其可执行。  
``` bash   
$ chmod +x /home/git/hexoBlog.git/hooks/post-receive 
```  
到这里，我们的 git 仓库算是完全搭建好了。下面进行 Nginx 的配置。  

## 云服务器端安装Nginx
### 安装 Nginx   
``` bash
$ yum install -y nginx
```  
### 启动 Nginx  
``` bash
$ service nginx start
```  
### 测试 Nginx 服务器  
``` bash
$ wget http://127.0.0.1 
```  
能够正常获取以下欢迎页面说明Nginx安装成功。   
					
	Connecting to 127.0.0.1:80... connected.
	HTTP request sent, awaiting response... 200 OK
	Length: 43704 (43K) [text/html]
	Saving to: ‘index.html’
	
	100%[=======================================>] 43,704      --.-K/s   in 0s
	
	2018-03-09 23:04:09 (487 MB/s) - ‘index.html’ saved [43704/43704]  
 
测试网页是否能打开   
在浏览器中输入服务器 ip 地址，就是服务器的公网 ip。 
配置 Nginx 托管文件目录
接下来，创建 /home/hexoBlog目录，用于 Nginx 托管。   
``` bash
$ mkdir /home/hexoBlog/
```   
``` bash
$ chown -R $USER:$USER /home/hexoBlog/  
```  
``` bash
$ chmod -R 755 /home/hexoBlog/
```   
查看 Nginx 的默认配置的安装位置 
``` bash
$ nginx -t
```  
### 修改Nginx的默认配置，其中 cd 后边就是刚才查到的安装位置（每个人可能都不一样）
``` bash
$ vim /etc/nginx/nginx.conf
```  
按方向键，找到如下位置  

	server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /home/hexoBlog;    #需要修改
	
	server_name www.bujige.net; #需要修改
	
	# Load configuration files for the default server block.
	include /etc/nginx/default.d/*.conf;
	location / {
	}
	error_page 404 /404.html;
	    location = /40x.html {
	}

按i键进入插入模式，将其中的 root 值改为 /home/hexoBlog （刚才创建的托管仓库目录）。
将 server_name 值改成你的域名。   
重启 Nginx 服务   
``` bash
$ service nginx restart
```  
至此，服务器端配置就结束了。接下来，就剩下本地 hexo 的配置更改了。

## 本地安装hexo介绍
### hexo是什么？
Hexo 的中文官网：http://hexo.io/zh-cn/  
作者 Tommy Chen：https://zespia.tw/  
在我的理解里面：Hexo 是一个基于 Node.js 快速、简洁且高效的博客框架，可以将 Markdown 文件快速的生成静态网页，托管在GitHub Pages 或者Coding Pages 上。   
而官网自己是这样说的：   
Hexo 是一个快速、简洁且高效的博客框架。Hexo 使用 Markdown（或其他渲染引擎）解析文章，在几秒内，即可利用靓丽的主题生成静态网页。   
### 为什么要用hexo?  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/hexo_.png)    
因为其他博客框架太烂了   
想自己管理博客，不受其他品台的约束  
### 本文环境介绍和软件准备
系统：

	window 10 专业版（64位）

所需软件：

	Git:Git-2.14.1-64-bit
	Markdown
	Node.js:node-v87.0-x64	

## 部署开始
### git客户端安装
双击运行 Git-2.14.1-64-bit.exe，接下来一律下一步，不需要多余的选择，假设你安装的目录位置跟我一样：C:\Program Files\Git
打开 Git Bash（路径：C:\Program Files\Git\git-bash.exe），输入：git --version
如下图，如果出现：git version 2.14.1.windows.1，这表示安装成功  

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/hexo_1_2.png)  
 
### Node.js 源设置
在安装 Hexo 之前，先说一下 Node.js 的源，Node.js 官方源默认是：http://registry.npmjs.org，但是由于在国外，说不定你使用的时候就抽风无法下载任何软件。所以我们决定暂时使用淘宝提供的源，淘宝源官网：http://npm.taobao.org/  
在 Git Bash 中我们执行下面这一句（这是一整句的）：

	alias cnpm="npm --registry=https://registry.npm.taobao.org \--cache=$HOME/.npm/.cache/cnpm \--disturl=https://npm.taobao.org/dist \--userconfig=$HOME/.cnpmrc"

### 安装 Hexo 框架
安装 Hexo（注意，现在是 cnpm 开头了，不是 npm 了）：

	cnpm install -g hexo-cli

Mac下执行：

	sudo cnpm install -g hexo-cli

安装时间不一定很快，有可能需要等 3 ~ 5 分钟。
安装完有 WARN 警告也没关系的。
### 创建Hexo项目
现在假设我要创建一个名为 hexo 的项目，项目目录就放在：D:\work\code 目录下，所以我们在 D:\work\code 目录下创建一个 hexo 目录。现在这个项目的全路径是：D:\work\code\hexo
打开 Git Bash:
进入该目录：cd D:\work\code\hexo
然后执行：hexo init，这个时间也会比较长，也有可能要等几分钟，有显示 WARN 也不用管
安装完成之后，D:\work\code\hexo 目录结构是这样的：

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/hexo_1_3.png)  

现在我们启动 hexo 本地服务，看下默认的博客是怎样的？
命令：

	hexo server

现在用浏览器访问：http://localhost:4000/，效果如下图

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/hexo_1_4.png) 

如果要停止 hexo 服务：在 Git Bash 下按 Ctrl + C 即可

### 选用其他主题
由于默认主题太大众了，所以现在我们换个主题。   
你可以去这里找主题：
   
	hexo-theme：https://hexo.io/themes/   
	hexo-github-theme-list：https://github.com/hexojs/hexo/wiki/Themes 
  
有那些好看的hexo主题？：

	http://www.zhihu.com/question/24422335 
  
我这里选择的 yelee：GitHub链接 

	https://github.com/MOxFIVE/hexo-theme-yelee 
  
Yelee主题使用说明: http://moxfive.coding.me/yelee/   
原因是能最大化衬托出：目录、文章内容、代码块。因为我对这个博客的定位就是用来放技术类内容，所以不会让它太杂或是太花。只是目前这个颜色偏浅，后续还需要调整。   
现在假设你跟我要用的模板是一样： 
还是让 Git Bash 保持在 D:\work\code\hexo 目录下，然后输入命令：

	git clone https://github.com/huangxiaocan/hexo-theme-yelee.git

这样就在 D:\work\code\hexo\themes 目录下生成了一个 yelle 文件夹，里面有我们刚刚 clone 下来的主题内容

下载好主题文件之后，我们现在要修改 D:\work\code\hexo 目录下的项目配置文件：_config.yml，把对应的主题目录名改下，编辑如下图

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/hexo_1_5.png)  

更改主题目录名后，我们还要重新生成主题静态内容：
继续在 Git Bash 中输入命令：
重新生成静态博客的所有内容：

	hexo generate

重启 hexo 本地服务：

	hexo server

重新访问：http://localhost:4000/，效果如下图   

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/hexo_1_6.png)   

### 把本地的博客内容发布到 服务器上Git
要把本地的静态博客同步到 Github，我们还需要先安装两个跟部署相关的 hexo 插件：  
继续在 Git Bash 中输入：  

	cnpm install hexo -server --save
	cnpm install hexo-deployer-git --save

编辑全局 hexo 的配置文件：_config.yml   
官网对此配置的介绍：https://hexo.io/zh-cn/docs/configuration.html  
我自己的编辑内容初稿（你需要认真看的是含有中文注释的内容）： 

	# Hexo Configuration
	## Docs: https://hexo.io/docs/configuration.html
	## Source: https://github.com/hexojs/hexo/
	
	# Site 这一块区域主要是设置博客的主要说明，需要注意的是：每个冒号后面都是有一个空格，然后再书写自己的内容的s
	title: 泊寓码农  #网站标题
	subtitle: Talk is cheap. Show me the code
	description: 这里是 www.boyu01.com 一部分
	author: huangc
	email: 571522149@qq.com
	language: zh-CN
	timezone:   #网站时区。Hexo 默认使用您电脑的时区
	
	
	# URL 这一块一般可以设置的是 url 这个参数，比如我要设置绑定域名的，这里就需要填写我的域名信息
	## If your site is put in a subdirectory, set url as 'http://yoursite.com/child' and root as '/child/'
	url: http://boyumanong.top
	root: /
	
	abbrlink:
	  alg: crc16 #support crc16(default) and crc32
	  rep: hex    #support dec(default) and hex
	
	# 更改 permalink 值
	permalink: p/:abbrlink.html
	
	
	# Directory
	source_dir: source #源文件夹，这个文件夹用来存放内容。
	public_dir: public #公共文件夹，这个文件夹用于存放生成的站点文件
	tag_dir: tags #标签文件夹
	archive_dir: archives #归档文件夹
	category_dir: categories #分类文件夹
	code_dir: downloads/code #nclude code 文件夹
	i18n_dir: :lang #国际化（i18n）文件夹
	skip_render:  #跳过指定文件的渲染，您可使用 glob 表达式来匹配路径
	
	# Writing
	new_post_name: :year-:month-:day.:title.md #新建文章默认文件名
	default_layout: post # 默认布局
	titlecase: false # Transform title into titlecase
	external_link: true # 在新标签中打开一个外部链接，默认为true
	filename_case: 0 
	render_drafts: false #是否渲染_drafts目录下的文章，默认为false
	post_asset_folder: true #启动 Asset 文件夹
	relative_link: false #把链接改为与根目录的相对位址，默认false
	future: true #显示未来的文章，默认false
	highlight:  #代码块的设置
	  enable: true
	  line_number: true
	  auto_detect: false
	  tab_replace:
	
	# Category & Tag #分类和标签的设置
	default_category: uncategorized #默认分类
	category_map:
	tag_map:
	
	# Date / Time format
	## Hexo uses Moment.js to parse and display date
	## You can customize the date format as defined in
	## http://momentjs.com/docs/#/displaying/format/
	date_format: YYYY-MM-DD
	time_format: HH:mm:ss
	
	# Pagination
	## Set per_page to 0 to disable pagination
	per_page: 10
	pagination_dir: page
	
	# Extensions
	## Plugins: https://hexo.io/plugins/
	## Themes: https://hexo.io/themes/
	theme: yelee # next  
	
	search:
	  path: search.xml
	  field: all
	
	html_minifier:
	  enable: true
	  ignore_error: false
	  exclude:
	
	css_minifier:
	  enable: true
	  exclude:
	    - '*.min.css'
	
	js_minifier:
	  enable: true
	  mangle: true
	  output:
	  compress:
	  exclude:
	    - '*.min.js'
	
	image_minifier:
	  enable: true
	  interlaced: false
	  multipass: false
	  optimizationLevel: 2
	  pngquant: false
	  progressive: false
	
	# Deployment
	## 这里是重点，这里是修改发布地址，因为我们前面已经加了 SSH 密钥信息在 Github 设置里面了，所以只要我们电脑里面持有那两个密钥文件就可以无需密码地跟 Github 做同步。
	## 需要注意的是这里的 repo 采用的是 ssh 的地址，而不是 https 的。分支我们默认采用 master 分支，以后你翅膀硬了要换其他也无所谓。
	## Docs: https://hexo.io/docs/deployment.html
	## commend : hexo c  hexo g  hexo s  hexo d
	deploy:
	  type: git
	  repo: root@CVM 你的云服务器的IP地址:/home/git/hexoBlog
	  branch: master
	      #github: git@github.com:chenjh0611/chenjh0611.github.io.git,master
	      #coding: git@git.coding.net:chenjh0719/chenjh0719.git,master
      

编辑全局配置后我们需要重新部署：  
继续在 Git Bash 中输入命令：  
先清除掉已经生成的旧文件：

	hexo clean  

再生成一次静态文件：

	hexo generate 
  
在本地预览下：

	hexo server   

本地没问题之后，

	Ctrl + C 停掉本地预览

使用部署命令部署到 Github 上：

	hexo deploy

有弹出下面提示框，请输入你的服务器密码
 
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/hexo_1_7.png)  

访问服务器地址进行检查：

	http://ip

通过上面几次流程我们也就可以总结：以后，每次发表新文章要部署都按这样的流程来：

	cd 你的 hexo 目录
	hexo clean
	hexo generate
	hexo deploy

也因为这几个命令太频繁了，所以又有了精简版的命令：
  
	hexo clean == hexo clean
	hexo g == hexo generate
	hexo s == hexo server
	hexo d == hexo deploy

打开你的公网 IP，看是不是已经部署成功了。  

最后一步，更改域名解析。这一步不再做介绍。
## 安装Markdown编辑器提高效率
MarkdownPad 2是一款较不错的Markdown编辑器，可快速将文本转换为美观的HTML/XHTML的网页格式代码，且操作方便，用户可以通过键盘快捷键和工具栏按钮来使用或者移除Markdown格式，左右栏的分割方式令用户可以实时看到HTML格式的Markdown文档。如果你喜欢在简书、CSDN等平台发表文章，也想掌握这门简单的轻量级的标记语言Markdown，又担心离线无处编辑，欢迎尝试。  
### 官网下载地址：  

	http://markdownpad.com/download/markdownpad2-setup.exe

### 百度网盘地址：

	https://pan.baidu.com/s/1eSKXqka

### 破解码如下:

	Email address：Soar360@live.com  
	License key：GBPduHjWfJU1mZqcPM3BikjYKF6xKhlKIys3i1MU2eJHqWGImDHzWdD6xhMNLGVpbP2M5SN6bnxn2kSE8qHqNY5QaaRxmO3YSMHxlv2EYpjdwLcPwfeTG7kUdnhKE0vVy4RidP6Y2wZ0q74f47fzsZo45JE2hfQBFi2O9Jldjp1mW8HUpTtLA2a5/sQytXJUQl/QKO0jUQY4pa5CCx20sV1ClOTZtAGngSOJtIOFXK599sBr5aIEFyH0K7H4BoNMiiDMnxt1rD8Vb/ikJdhGMMQr0R4B+L3nWU97eaVPTRKfWGDE8/eAgKzpGwrQQoDh+nzX1xoVQ8NAuH+s4UcSeQ==

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/hexo_1_8.png)

如果是win10还需要安装一个组件awesomium_v1.6.6_sdk_win.exe，否则会出现错误提示

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/hexo_1_9.png)

破解和安装组件后需要重启软件 才可以正常的使用，重启MarkdownPad2就可以用了!  

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/hexo_1_10.png)

## 又拍云存储
博客中显示的图片，我采用的是又拍云存储进行保存
https://console.upyun.com/services/hc-image-upyun/filemanage/

## 结束语
我希望从这一篇你也可以为自己搭建一个属于你自己的博客，在博客中畅写。
最后，祝你搭建博客成功，创造属于你的世界！

参考资料：  
[将hexo部署到腾讯云上](https://www.jianshu.com/p/271449df801f "hexo腾讯云").    
[Hexo 教程：Hexo 博客部署到腾讯云教程](https://www.fogsail.net/2018/02/22/20180222/ "hexo").        
[markdown的下载安装破解](https://code.skyheng.com/post/36308.html "markdown").     
[Hexo搭建技术博客部署在阿里云服务器上教程](https://code.skyheng.com/post/36551.html "hexo阿里云").   