---
title: hexo安装问题收集
tags:
  - hexo
categories: hexo
description: hexo安装问题收集 
abbrlink: 5b81
date: 2019-06-19 12:15:08
---
hexo安装问题收集

<!--less-->  

## Hexo更换主题yelee,首页右面却没有显示文章

解决方法是把yelee文件夹下的_config.yml文件修改一下，如下，大概是在234行，在onload前面加一个“#”，注释掉这一行后就能正常运行了。

	search: 
	#on: true  
	#onload: false #这里有更改，把on前面的‘#’去掉
	## true: get search.xml file when the page has loaded
	## false: get the file when search box gets focus
	## 文章字数+阅读时长统计

## hexo d 发布不上，需要安装一个插件

	npm install --save hexo-deployer-git

## Yelee主题字数统计，阅读时长
修改themes\yelee\layout\_partial\

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/Hexo_1_1.png) 



## You must install peer dependencies yourself.的解决办法

	npm WARN checkPermissions Missing write access to D:\work\code\hexo\node_modules\fsevents
	npm WARN babel-eslint@10.0.2 requires a peer of eslint@>= 4.12.1 but none is installed. You must install peer dependencies yourself.
	npm WARN mini-css-extract-plugin@0.4.0 requires a peer of webpack@^4.4.0 but none is installed. You must install peer dependencies yourself.
	npm WARN webpack-cli@3.0.4 requires a peer of webpack@^4.x.x but none is installed. You must install peer dependencies yourself.

出现这个问题，原因在于npm 版本太低，更新npm即可解决

	npm install -g npm

## 总结
一分耕耘，一分收获，支持



	