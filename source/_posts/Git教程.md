---
title: Git入门
tags:
  - Git
categories: Git
description: Git入门
abbrlink: eba2
---
## 快速入门

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/git_1_1.png)
  
作者   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/git_1_2.png) 

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/git_1_3.png)

### 为什么学习git

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/git_1_4.png)  
 
### Git安装
下载window git 
 
	Msysgit https://git-scm.com/download/win 
 
这个网站在国外，下载速度可能有点慢  
还有一种图形化界面的代码管理器，sourcetree，有想了解的可以下载了解一下  

 配置用心信息 
 
	git config --global user.name "tyler"
	git config --global user.email "tyler@163.com"

查看是否配置好

	git config --list

## Git仓库创建和及工作量
### 创建仓库
初始化版本库

	git init

添加文件到版本库

	git add

	git commit

查看仓库状态

	git status


### 工作流

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/git_4.png) 

把暂存区的数据回退到工作区

	git reset HEAD base_demo.txt
	git checkout base_deme.txt

查看日志

	git log

回退到上一次提交的版本

	git reset --hard logid

## Git主要功能
### 远程仓库

创建SSH key,邮箱必须为你注册github的邮箱

	ssh-keygen -t ras -C "youremail@example.com"

添加远程仓库

	git remote add origin git@github.com:tylerdemo/tyler_muke.git

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/git_5.png) 

### 克隆仓库

	git clone git@github.com:tylerderdemo/demo4.git

### 标签管理
查看所有标签

	git tag

创建标签 

	git tag name 

制定提交信息

	git tag -a name -m "comment"

删除标签

	git tag -d name

标签发布 

	git push origin name

### 分支管理

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/git_8.png) 

创建分支name

	git branch name

查看分支

	git branch

切换分支到name

	git checkout name


## 资源
### 视频地址 

	https://www.imooc.com/learn/1052