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

## 问题1 
最近在用Hexo搭建博客，刚刚更换了Yelee主题，在搭建完成后发现了一个BUG，在所有文章列表中有文章，首页左面正常显示，但是首页右面却没有显示文章

解决方法是把yelee文件夹下的_config.yml文件修改一下，如下，大概是在234行，在onload前面加一个“#”，注释掉这一行后就能正常运行了。

	search: 
	#on: true  
	#onload: false #这里有更改，把on前面的‘#’去掉
	## true: get search.xml file when the page has loaded
	## false: get the file when search box gets focus
	## 文章字数+阅读时长统计
## 问题2
hexo d 发布不上，需要安装一个插件

	npm install --save hexo-deployer-git


	