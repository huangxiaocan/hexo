---
title: Docker入门教程
tags:
  - Docker
categories: Docker
description: Docker入门教程
abbrlink: 448e
---
## 快速入门
### Docker介绍
什么是Docker?  
Docker:an open source project to pack,ship and run any application as a lightweight container  

Node.js:allows to package an application with all of its dependencies into a standardized unit  
  
类比   
1，Docker可以粗糙地理解为轻量级的虚拟机   
2，开挂的chroot   

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/docker/docker_1_1.png)  

### Docker Mac和window安装
1，进入docker官网：http://www.docker.com，注册Docker Hub账号后
点击图片上的Get Start
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/docker/docker_1_2.png)  
2,点击图片上的Get started with Docker DeskTop 
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/docker/docker_1_3.png)
选择适合自己系统的Docker版本进行下载  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/docker/docker_1_4.png) 

下载对应的mac或者window安装包Docker.dmg后，双击进入下一步直到finish

### docker linux 安装
我的linux版本是Centos7.2
此命令执行后，docker会根据linux系统的版本选择最适合的docker版本进行下载安装，wget是下载命令，-qO-是标准输出 让sh来执行

	sudo wget -qO- https://get.docker.com | sh

执行完看到下面的结果
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/docker/docker_1_7.png) 
把这个用户添加到docker的用户组

	sudo usermod -aG docker root

此命令检测docker是否安装成功

    docker info	

执行完docker info 会出现下面的这个报错   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/docker/docker_1_8.png)

需要执行下面的两个命令即可解决

	systemctl daemon-reload

	sudo service docker restart

执行完之后，看到下面的结果，说明就安装成功了  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/docker/docker_1_9.png)
## 实践第一步
### docker架构介绍
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/docker/docker_2_1.png)  

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/docker/docker_2_2.png)
### docker实	战
1,执行第一个docker hello-world程序

	docker run hello-world

出现如下信息

	Unable to find image 'hello-world:latest' locally

说明docker中没有hello-world的镜像，需要从远程服务器中pull下来
看到如下信息说明执行成功

	Unable to find image 'hello-world:latest' locally
	latest: Pulling from library/hello-world
	1b930d010525: Pull complete 
	Digest: sha256:41a65640635299bab090f783209c1e3a3f11934cf7756b09cb2f1e02147c6ed8
	Status: Downloaded newer image for hello-world:latest

执行查看镜像

	docker images

出现如下结果

	REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
	hello-world         latest              fce289e99eb9        6 months ago        1.84kB

2,docker执行nginx

	docker run nginx

查看镜像

	docker images

docker 启动nginx服务 -p表示端口映射 用8080代替80 -d表示直接返回container id

	docker run -p 8080:80 -d nginx

查看当前正在运行的docker

	docker ps

打开浏览器访问地址：http://localhost:8080,看到如下信息，说明nginx启动成功  

	Welcome to nginx

拷贝一个index.html到容器里面

	docker cp index.html 容器id：//user/share/nginx/html

停止服务

	docker stop 容器id

docker在容器内做的操作都是暂时，所以我们需要保存在容器内做的操作，该命令会生成一个新的镜像

	docker commit -m 'fun' 容器id dockerimages备注

查看历史运行过的镜像

	docker ps -a

删除不需要的镜像

	docker rm 容器id

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/docker/docker_1_5.png)
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/docker/docker_1_6.png)
## Dockerfile介绍
### dockerfile介绍
dockerfile 可以通过编写简单的文件自创docker镜像，所需要的代码如下

	FROM alpine:latest
	MAINTAINER xbf
	CMD echo 'hello docker'

创建第一个dockerfile，执行步骤如下
创建一个新的目录
	
	mkdir d1

进入d1目录

	cd d1

查看目录

	ls

创建一个Dockerfile的文件

	touch Dockerfile

用vim编辑器打开

	vim Dockerfile

插入数据

	FROM alpine:latest
	MAINTAINER xbf
	CMD echo 'hello docker'

文件保存退出

	:wq

在d1目录中执行命令生成hello_docker 镜像 -t 表示 标签名 . 表示当前目录

	docker build -t hello_docker .

查看镜像

	docker images

运行这个镜像

	docker run hello_docker


### dockerfile实战
第二个Dockerfile
以启动nginx为例
所需代码如下

	FROM centos
	MAINTAINER xbf
	RUN apt-get update
	RUN apt_get install -y nginx
    COPY index.html /var/www/html
	ENTRYPOINT["/use/sbin/nginx","-g","daemon off"]
	EXPOSE 80

创建第二个Dockerfile操作步骤
创建目录dockerfile2

	mkdir dockerfile2

进入目录

	cd dockerfile2

查看目录

	ls

创建Dockerfile文件

	touch Dockerfile

用vim编辑器打开文件

	vim Dockerfile

插入代码如下

	FROM centos
	MAINTAINER xbf
	RUN apt-get update
	RUN apt_get install -y nginx
    COPY index.html /var/www/html
	ENTRYPOINT["/use/sbin/nginx","-g","daemon off"]
	EXPOSE 80

保存并退出

	:wq

创建index.html文件

	touch index.html

填充数据,随便啥数据都行

	vim index.html

保存退出

	:wq

创建hello_nginx镜像

	docker build -t xbf/hello_nginx .

运行镜像

	docker run -d 8080:80 xbf/hello_nginx 

测试

	curl http://localhost


### 镜像分层
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/docker/docker_3_3.png)  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/docker/docker_3_4.png)  
## 存储
### volume介绍
提供独立于容器之外的持久化存储   
读法（wo len）  
### volume操作

## 镜像仓库
### registy介绍 
镜像仓库   
我们自己可以创建镜像来push到仓库中，共享出去

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/docker/docker_5_1.png)  

从Registry中搜索想要的镜像

	docker search whalesay

并把它拉去下来

	docker pull whalesay

提交自己的镜像到仓库

	docker push myname/whealesay

国内的镜像仓库

	时速云
	aliyun
	daocloud

### registy实战
从官方docker hub 中搜索一个镜像

	docker search whalesay

拉去镜像

	docker pull docker/whalesay

查看镜像

	docker images

运行这个镜像

	docker run docker/whaleasy cowsay Docker很好玩！

打标签重新生成一个镜像

	docker tag docker/whalesay xibeifeng/whalesay

上传xibeifeng/whalesay 到docker hub

	docker push xibeifeng/whalesay

登陆docker hub账号

	docker login

输入你的用户名和密码，push成功。
## 多容器app
### compose介绍
docker-compose安装
mac和window：自带
linux：curl https://github.com/docker/compose
### compose-install-linux
执行命令

	curl -L https://github.com/docker/compose/releases/download/1.8.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose	

授权所有用户都可以执行docker-compose

	chmod +x /usr/local/bin/docker-compose

查看版本信息

	docker-compose --version

### componse实战 

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/docker/docker_6_1.png)  
## 参考资料
### 教学视频地址

	初级：https://www.imooc.com/video/15641

	中级：https://www.imooc.com/learn/824