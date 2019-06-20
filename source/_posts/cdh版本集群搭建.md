---
title: cdh版本集群搭建 
tags:
  - 大数据  
categories: 大数据  
description: cdh版本集群搭建(服务器搭建) 
## 步骤

vi sudoers
#编辑添加普通用户权限为root，在root权限相应的位置下添加

%用户名  ALL=(ALL)  OPASSWD: ALL
#保存要先 :wq!保存强制退出

#服务器搭建(如没有生效断开重新连接就会生效)

# 1.关闭防火墙 （每个节点）

	启动： systemctl start firewalld 
	查看状态：systemctl status firewalld 
	停止： systemctl disable firewalld
	禁用： systemctl stop firewalld
	 或者：
	systemctl stop firewalld.service
	systemctl disable firewalld
	先停止，再关闭比



# 2.修改主机名（每个节点）命令行直接输入

    hostnamectl set-hostname 主机名


#3.ip映射关系:（每个节点）如需使用用户名在web端访问需要在本地hosts文件添加如下对应操作
	vi  /etc/hosts 
	ip    主机名
在提示符下输入reboot命令，重新启动服务器

打通master至slave[1~2]节点的SSH免密登陆 （master至slave[1~2]是相应的主机名）

在主节点上执行 ssh-keygen -t rsa三次回车，生成无密码的密钥对，root用户下默认在~/.ssh/目录中，如没有.ssh目录则使用mkdir ~/.ssh新建一个即可。

```
$ ssh-keygen -t rsa
```   
分发到所有节点 ：   
```
$ ssh-copy-id slave1
```   
```
$ ssh-copy-id slave2
```


测试ssh登录

```
$ ssh slave2
```

退出:exit


#安装上传软件
	yum -y install lrzsz

#4.关闭SELinux(所有节点)
	vi /etc/selinux/config
 	修改
	SELINUX=disabled 
#重启生效（服务器不需重启）

#5.禁用交换分区 (所有节点)
	sysctl -w vm.swappiness=0 
 	echo 0 > /proc/sys/vm/swappiness 


#6.配置时间同步(主机)

#首先安装NTP(全部机器)
	yum install ntp -y
#开机启动
	chkconfig ntpd on

	service ntpd start

添加Yam依赖  

	yum install chkocnfig python bind-utils psmisc libxslt zlib sqlite cyrus-sasl-plain cyrus-sasl-gssapi fuse fuse-libs redhat-lsb -y

开始配置
# 1.安装Java环境变量rpm包安装（rpm解压为全局变量，如下载其他java请配置环境变量）
	rpm  -ivh  安装包名称 

# 2.安装Mysql 卸载Linux系统上自带的mysql插件
 #查找mysql相关安装：
    rpm -qa|grep -i mysql
# 如存在请删除
    卸载命令：rpm –ev {包名}
# 查找旧版本mysql相关的安装目录命令：
    find / -name mysql
#若查找到相关目录使用命令：rm –rf {目录名}
#最后使用命令：重新检查一遍系统中是否安装mysql
	rpm -qa|grep -i mysql
	下载mysql安装包后如下操作这里下载包为 tar.gz结尾
	tar -xzvf 包文件名.tar.gz
	移动重命名
	mv mysql文件 /usr/local/mysql
# 修改配置
	cd/usr/local/mysql

	mkdir data
#主目录权限管理-》查看组和用户情况
	cat /etc/group | grep mysql
	cat /etc/passwd |grep mysql
#若存在，则删除原mysql用户，会删除其对应的组和用户
	userdel -r mysql
#在查看就会发现没有，说明你已经删掉了。
	cat /etc/group | grep mysql
	cat /etc/passwd |grep mysql
#创建mysql组和mysql用户
	groupadd mysql
	useradd -r -g mysql mysql
	chown -R mysql:mysql /usr/local/mysql
	创建配置文件及相关目录
	修改配置文件：/etc/my.cnf，配置不对的话,后面初始化不全,会拿不到默认密码。
	
	vim /etc/my.cnf

	修改内容:
	basedir=/usr/local/mysql
	datadir=/usr/local/mysql/data
	port = 3306
	按esc键返回
	:wq! 保存退出
#安装和初始化数据库进入bin目录:

	cd /usr/local/mysql/bin/
	初始化数据库:（这时有一个数据库的初始密码在最后显示要复制保存起来，不然后期数据库进不去）
	
	./mysqld --initialize --user=mysql --basedir=/usr/local/mysql--datadir=/usr/local/mysql/data
	安全启动:
	./mysqld_safe --user=mysql &
	查看mysql进程，ps -ef | grep mysql
	进入bin目录:
	
	cd /usr/local/mysql/bin/
	登录mysql:
	
	./mysql -u root -p
	保存的初始密码输入
	
	进入数据库后
	mysql>show databases;
	修改数据密码
	mysql>set password=password("123456");
设置远程登录权限

	mysql>grant all privileges on *.* to 'root'@'%' identified by '123456';
立即生效:

	mysql> flush privileges;
退出quit 或者 exit;

	mysql> quit;

#安装 Cloudera Manager #无聊参考安装路径https://www.cnblogs.com/irich/p/6883839.html


#上传Cloudera Manager 然后解压发送到opt目录
	tar -xvf cm文件名.tar.gz -C /opt
# 修改配置 
	vi /opt/cm文件名/etc/cloudera-scm-agent/config.ini
	server_host=master  #修改这里
#同步到其他节点
	scp -r /opt/cm文件名/ slave1:/opt
	scp -r /opt/cm文件名/ slave2:/opt
# 创建 SCM 用户 (所有节点都需要执行 )
	useradd --system --home=/opt/cm文件名/run/cloudera-scm-server/ --no-create-home --shell=/bin/false --comment "Cloudera SCM User" cloudera-scm 
#上传MySQL的jar到/usr/share下的java(没有目录自己创建)
	mkdir java
	(#上MySQL的jar到cm/share/cmf/lib/目录中
	cd cm-5.10.1/share/cmf/lib/ 
#初始化 Cloudera Manager 数据库 
	/opt/cm文件名/share/cmf/schema/scm_prepare_database.sh mysql cdh -h master -ucdh -pcdh --scm-host master scm scm scm
#在这里后面的参数分别是：数据库类型 数据库名称 数据库主机名 数据库用户名 密码 --scm-host cdhserver主机名 scm scm scm

#上传3个文件到主机的的/opt/cloudera/parcel-repo/目录中（底下是根据自己上传的cdh的parcel文件版本视情况而定底下是例子）
	CDH-5.10.1-1.cdh5.10.1.p0.10-el6.parcel.sha1
	CDH-5.10.1-1.cdh5.10.1.p0.10-el6.parcel
	manifest.json
#修改sha1的名字
	cp CDH-5.10.1-1.cdh5.10.1.p0.10-el6.parcel.sha1 CDH-5.10.1-1.cdh5.10.1.p0.10-el6.parcel.sha
#在master节点启动 CM服务和代理
	/opt/cm文件名/etc/init.d/cloudera-scm-server start
	/opt/cm文件名/etc/init.d/cloudera-scm-agent start
#在slave1、slave2 启动 CM 代理
	/opt/cm文件名/etc/init.doudera-scm-agent start
	进入cdh的可视化界面 http://master:7180
	用户名，密码都是admin
（	进入后组件选择性搭建 组件可选择自动安装这个过程很长需要耐心等待）