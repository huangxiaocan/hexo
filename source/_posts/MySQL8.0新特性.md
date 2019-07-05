---
title: MySQL8.0新特性
tags:
  - 新特性
categories: 新特性
description: MySQL8.0新特性
abbrlink: 2d20
---
## 快速入门
### MySql8.0新特性概览
![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql_1_1.png)  

## 账户与安全
### 用户创建和授权
MySql8.0创建用户和用户授权的命令需要分开执行：
	
	create user 'tony'@'%' identified by 'Tony@2018';
	grant all privileges on *.* to 'tony'@'%';

Mysql5.7创建用户和授权：

	grant user 'tony'@'%' identified by 'Tony@2018';
	grant all privileges on *.* to 'tony'@'%';

### 认证插件更新
MySql8.0中默认的身份认证插件是caching_sha2_password,替代了之前的mysql_native_password。

查看mysql版本的默认插件

	show variables like 'default_authentication';	

mysql5.7版本的默认插件如下图  
![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql_1_2.png) 

mysql8.0版本的默认插件如下图  
![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql_1_3.png)


![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql_1_4.png)

修改mysql8.0用5.7版本的插件mysql_native_password的两种方式
1，执行如下脚本：

	alter user 'tony'@'%' identified with mysql_native_password by 'Tony@2019'

2，修改mysql的my.ini文件，把有mysql_native_password的这行前面的注释去掉
### 密码管理
摘要：MySql8.0开始允许限制重复使用以前的密码  

password_history = 3

password_reuse_interval = 90

password_require_current = on

查看密码变量

	show variables like 'password';

![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql_1_5.png)
### 角色管理

## 优化器索引
### 隐式索引

### 降序索引

### 函数索引

## 通用表表达式
### 非递归CTE

### 递归CTE

### 递归限制

## 窗口函数
### 窗口函数基本概念

### 专用窗口函数

### 窗口定义

## InnoDB 增强

### 集成数据字典

### 原子DDL操作

### 自增列持久化

### 死锁检查控制

### 锁定语句选项

### 其他改进功能

## JSON增强

### 内联路径操作符

### JSON聚合函数

### JSON实用函数

### JSON合并函数

### JSON表函数

## 资源
### 视频地址

	https://www.imooc.com/learn/1102