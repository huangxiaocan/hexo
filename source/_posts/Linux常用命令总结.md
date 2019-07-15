---
title: Linux常用命令总结
tags:
  - Linux
categories: Linux
description: Linux常用命令总结
abbrlink: 8be9
---
## Linux常用命令总结
### Linux crontab 定时任务
编辑定时任务

	crontab -e

查看定时任务

	crontab -l

定时任务语法：分钟 小时 日 月 星期

	* 12 * * 1 python /usr/local/tyzq/py/zcSpider/crawlall.py > /usr/local/tyzq/py/zcSpider/crawlall_$(date +\%Y\%m\%d).log 2>&1
	

### Linux tail 查看日志
查看末尾100行的日志

	tail -n 100 *.log

### 解压文件

	tar -zxvf *.tar

### 下载文件

	wegt *

### 查看ip

	ifconfig

###  




