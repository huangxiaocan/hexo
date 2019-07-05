---
title: 用Jenkins自动化搭建测试环境
tags:
  - Jenkins
  - java
  - 自动化
categories: 前端
description: 用Jenkins自动化搭建测试环境
abbrlink: c061
---
## 快速入门

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/jenkins/Jenkins_1_1.png)

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/jenkins/Jenkins_1_2.png)

## Jenkins简介
通用的开源平台  
常用于自动化测试，持续集成

## jenkins安装
### 下载Jenkins
打开网址：https://jenkins.io/zh/

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/jenkins/Jenkins_1_3.png)

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/jenkins/Jenkins_1_4.png)

### 第一次启动
下载好图上的jenkins.war包
运行命令：

	java -jar jenkins.war

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/jenkins/Jenkins_1_5.png)

打开浏览器输入：http://localhost:8080

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/jenkins/Jenkins_1_6.png)

打开initialAdminPassword   
C:\Users\admin\.jenkins\secrets\initialAdminPassword  
复制密码-->粘贴密码   
点击继续 

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/jenkins/Jenkins_1_7.png)

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/jenkins/Jenkins_1_8.png)

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/jenkins/Jenkins_1_9.png)

## jenkins插件安装
在jenkins管理页面单击系统管理--->插件管理--->可选插件

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/jenkins/Jenkins_1_10.png)

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/jenkins/Jenkins_1_11.png)

输入以下两个插件

	Rebuilder
	Safe Restart

安装插件报错

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/jenkins/Jenkins_1_12.png)

## 资源
### 视频地址
https://www.imooc.com/learn/1008