---
title: Centos7.2部署项目流程
tags:
  - Centos7.2
  - Mysql5.7
  - java1.8
categories: Mysq
description: 最近刚开发完一个珠海大横琴的项目，公司让我部署项目，趁着这个机会，写下部署流程。
abbrlink: c423
---
## 系统环境介绍
执行如下命令：

	uname -r

3.10.0-957.12.2.el7.x86_64	

## 安装JDK1.8
### 安装之前先检查一下系统有没有自带open-jdk命令：

	rpm -qa |grep java
	rpm -qa |grep jdk
	rpm -qa |grep gcj

如果没有输入信息表示没有安装  
如果安装可以使用

	rpm -qa | grep java | xargs rpm -e --nodeps 

批量卸载所有带有Java的文件，这句命令的关键字是java。   
首先检索包含java的列表:  

	yum list java*

检索1.8的列表:
	
	yum list java-1.8*

安装1.8.0的所有文件:

	yum install java-1.8.0-openjdk* -y

耐心等待一会，执行需要一些时间，安装成功如下图： 
 
![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql5.7_1_7.png)  

使用命令检查是否安装成功:

	java -version

java centos7配置查看jdk环境变量

	which java
	ls -lrt /usr/bin/java
	ls -lrt /etc/alternatives/java

![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql5.7_1_8.png)

至此断定jdk安装路径为：/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.212.b04-0.el7_6.x86_64 

	vi   /etc/profile

在最后面加上：

	export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.181-3.b13.el7_5.x86_64
	export JRE_HOME=$JAVA_HOME/jre
	export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
	export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH

保存退出

	source /etc/profile

验证

	echo $JAVA_HOME

## 安装Mysql5.7
因为 centos7.2 默认安装了 mariadb-libs，所以先要卸载掉
### 查看是否安装 mariadb

	rpm -qa | grep mariadb

### 卸载 mariadb

	rpm -e --nodeps mariadb-libs 

### 下载并安装MySQL官方的 Yum Repository

	wget -i -c http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm

![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql5.7_1_1.png) 

### 使用上面的命令就直接下载了安装用的Yum Repository，大概25KB的样子，然后就可以直接yum安装了。

	yum -y install mysql57-community-release-el7-10.noarch.rpm

![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql5.7_1_2.png)

### 之后就开始安装MySQL服务器。

	yum -y install mysql-community-server

这步可能会花些时间，安装完成后就会覆盖掉之前的mariadb。
........
至此MySQL就安装完成了，然后是对MySQL的一些设置

### 首先启动MySQL

	systemctl start  mysqld.service

查看MySQL运行状态，运行状态如图：

	systemctl status mysqld.service

![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql5.7_1_3.png)

### 查看Mysql密码
此时MySQL已经开始正常运行，不过要想进入MySQL还得先找出此时root用户的密码，通过如下命令可以在日志文件中找出密码：

	grep "password" /var/log/mysqld.log

![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql5.7_1_4.png)

### 如下命令进入数据库：
	
	mysql -uroot -p

输入初始密码，此时不能做任何事情，因为MySQL默认必须修改密码之后才能操作数据库：

	ALTER USER 'root'@'localhost' IDENTIFIED BY 'new password';

这里有个问题，新密码设置的时候如果设置的过于简单会报错：

![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql5.7_1_5.png)

原因是因为MySQL有密码设置的规范，具体是与validate_password_policy的值有关：

![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql5.7_1_6.png)

MySQL完整的初始密码规则可以通过如下命令查看：
	
	SHOW VARIABLES LIKE 'validate_password%';

但此时还有一个问题，就是因为安装了Yum Repository，以后每次yum操作都会自动更新，需要把这个卸载掉：

	yum -y remove mysql57-community-release-el7-10.noarch

### 设置Mysql可以远程访问

	GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' 
 
让命令执行生效：

	flush privileges;  

## 安装Nginx
### 添加源
默认情况下Centos7中无Nginx的源，最近发现Nginx官网提供了Centos的源地址，执行以下命令添加源：

	sudo rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm

### 安装Nginx
通过yum search nginx看看是否已经添加源成功。如果成功则执行下列命令安装Nginx  

	sudo yum install -y nginx

启动Nginx并设置开机自动运行

	sudo systemctl start nginx.service
	sudo systemctl enable nginx.service

打开浏览器输入：http://ip,看到如下图说明安装成功

![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql5.7_1_9.png)

### 修改配置文件nginx.conf
此目录为nginx的主配置

	vim /etc/nginx/nginx.conf

![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql5.7_1_10.png)

图中包含着子配置,我们要修改的也是子配置文件，执行如下命令

	vim /etc/nginx/conf.d/default.conf

这是windows，多locaition的配置

![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql5.7_1_11.png)

这是linux，多locaition的配置  

![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql5.7_1_20.png)

图中红色部分就是修改的内容   
修改完之后，执行一下命令重启nginx服务  

	service nginx restart

## 安装redis
### 通过以下命令即可安装redis

	yum install redis

### 安装完毕后，使用下面的命令启动redis服务
启动redis
	
	service redis start

停止redis

	service redis stop

查看redis运行状态

	service redis status

查看redis进程

	ps -ef | grep redis

设置redis为开机自动启动

	chkconfig redis on

进入redis服务
进入本机redis

	redis-cli

列出所有key

	keys *
	

## python环境配置
CentOS 7安装Python3.6过程（让linux系统共存Python2和Python3环境）
### 安装python3.6
CentOS 7系统自带了python2，不过可以不用2版本，直接使用python3运行python脚本就可以，但是千万别去动系统自带的python2，因为有程序依赖目前的python2环境，比如yum，动了yum就无法运行了，其他有的程序也可能会受影响。明白了上面的，然后就来安装Python3.6：

### 安装依赖环境

	yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel

![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql5.7_1_12.png)

### 下载python3
https://www.python.org/downloads

	wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz

![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql5.7_1_13.png)

经过漫长的等待，终于下载好
### 安装python3
包安装在/usr/local/Python3(具体安装位置看个人爱好)
创建目录：

	mkdir -p /usr/local/Python3

解压下载好的Python-3.6.5.tgz包

	tar -zxvf Python-3.6.5.tgz

### 进入解压后的目录，编译安装
	
	cd Python-3.6.5

	./configure --prefiex=/usr/local/Python3

可能会出现一个错误：如下图

![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql5.7_1_14.png)

因为没有按照gcc,解决办法如下命令：

	yum install gcc

安装成功如下图：

![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql5.7_1_15.png)

继续执行
	
	cd Python-3.6.5

	./configure --prefiex=/usr/local/Python3

已经不报错了，如下图：

![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql5.7_1_16.png)

然后make

	make

执行完毕，如下图

![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql5.7_1_17.png)

接着make install

	make install

执行完毕，如下图

![avatar](http://hc-image-upyun.test.upcdn.net/hexo/MySql5.7_1_18.png)

或者两步一起：make && make install

### 安装好了，建立python3的软链


	ln -s /usr/local/Python3/bin/python3 /usr/bin/python3

### 并将/usr/local/Python3/bin加入PATH

	export PATH=$PATH:$HOME/bin:/usr/local/Python3/bin	

按esc,输入：wq,按回车保存退出编辑

修改完记得执行下面的命令，让上一步的修改生效

	source ~/.bash_profile

检查Python3及pip3是否正常可用：

	python3 -V

Python 3.6.5


### 安装 setuptools
	wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-19.6.tar.gz#md5=c607dd118eae682c44ed146367a17e26 

	tar -zxvf setuptools-19.6.tar.gz 
	cd setuptools-19.6
	python3 setup.py build 
	python3 setup.py install

安装pip
	wget --no-check-certificate https://pypi.python.org/packages/source/p/pip/pip-8.0.2.tar.gz#md5=3a73c4188f8dbad6a1e6f6d44d117eeb 

	tar -zxvf pip-8.0.2.tar.gz

	cd pip-8.0.2 
	python3 setup.py build 
	python3 setup.py install
### 下载anaconda3.tar，安装爬虫框架，配置环境变量
假设当前目录为：/usr/local/tyzq/python
解压

	tar -zxvf anaconda3.tar

配置环境变量

  	vim /ect/profiles

在末尾加上

	export PATH=/usr/local/tyzq/python/anaconda3:$PATH
	export PATH=/usr/local/tyzq/python/anaconda3/bin:$PATH

运行python爬虫项目
遇到如下错误信息

	ImportError: libmysqlclient.so.18: cannot open shared object file: No such file or directory

解决办法如下：

	find / -name libmysqlclient.so*

唯独没有libmysqlclient.so.18
那么问题肯定是出在了安装mysql

查询得知缺少mysql-community-libs-compat-5.7.22-1.el7.x86_64.rpm
下载

	wget https://downloads.mysql.com/archives/get/file/mysql-community-libs-compat-5.7.22-1.el7.x86_64.rpm

安装

	rpm -ivh mysql-community-libs-compat-5.7.22-1.el7.x86_64.rpm

再启动项目就可以了。

## 总结
常用命令如下：  
nginx服务  

	service nginx restart
	service nginx start
	service nginx stop

后台运行java服务  

	nohup java -jar *.jar &

后台运行python服务

	nohup python3 *.py &

模糊查询进程

	ps -ef|grep nginx

杀死进程

	kill 进程id

