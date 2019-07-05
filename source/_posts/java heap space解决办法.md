---
title: java heap space解决办法
tags:
  - java
  - heap
categories: java heap
description: 'java.lang.OutOfMemoryError:java heap space解决办法'
abbrlink: 86b0
---
## java heap space 介绍
java.lang.OutOfMemoryError: PermGen space   
PermGen space的全称是Permanent Generation space,是指内存的永久保存区域, 
这块内存主要是被JVM存放Class和Meta信息的,Class在被Loader时就会被放到PermGen space中, 
它和存放类实例(Instance)的Heap区域不同,GC(Garbage Collection)不会在主程序运行期对 
PermGen space进行清理，所以如果你的应用中有很多CLASS的话,就很可能出现PermGen space错误, 
这种错误常见在web服务器对JSP进行pre compile的时候。如果你的WEB APP下都用了大量的第三方jar, 其大小 
超过了jvm默认的大小(4M)那么就会产生此错误信息了。
 
### 解决方法： 手动设置MaxPermSize大小 

修改TOMCAT_HOME/bin/catalina.sh 
在“echo "Using CATALINA_BASE:   CATALINABASE"”上面加入以下行：JAVAOPTS="−server−XX:PermSize=64M−XX:MaxPermSize=128m建议：将相同的第三方jar文件移置到tomcat/shared/lib目录下，这样可以达到减少jar文档重复占用内存的目的。二、java.lang.OutOfMemoryError:JavaheapspaceHeapsize设置JVM堆的设置是指java程序运行过程中JVM可以调配使用的内存空间的设置.JVM在启动的时候会自动设置Heapsize的值，其初始空间(即−Xms)是物理内存的1/64，最大空间(−Xmx)是物理内存的1/4。可以利用JVM提供的−Xmn−Xms−Xmx等选项可进行设置。Heapsize的大小是YoungGeneration和TenuredGeneraion之和。提示：在JVM中如果98％的时间是用于GC且可用的Heapsize不足2％的时候将抛出此异常信息。提示：HeapSize最大不要超过可用物理内存的80％，一般的要将−Xms和−Xmx选项设置为相同，而−Xmn为1/4的−Xmx值。解决方法：手动设置Heapsize修改TOMCATHOME/bin/catalina.sh在“echo"UsingCATALINABASE:CATALINA_BASE"”上面加入以下行： 
JAVA_OPTS="-server -Xms800m -Xmx800m   -XX:MaxNewSize=256m" 

## 检查分析原因所在
1，首先检查程序有没有限入死循环 
2，这个问题主要还是由这个问题 java.lang.OutOfMemoryError: Java heap space 引起的。第一次出现这样的的问题以后，引发了其他的问题。在网上一查可能是JAVA的堆栈设置太小的原因。 
### 跟据网上的答案大致有这两种解决方法： 
1、设置环境变量   

解决方法：手动设置Heap size   
修改TOMCAT_HOME/bin/catalina.sh   
set JAVA_OPTS= -Xms32m -Xmx512m    
可以根据自己机器的内存进行更改。   

2、java -Xms32m -Xmx800m className    
就是在执行JAVA类文件时加上这个参数，其中className是需要执行的确类名。（包括包名）    
这个解决问题了。而且执行的速度比没有设置的时候快很多。    

如果在测试的时候可能会用Eclispe 这时候就需要在Eclipse ->run -arguments 中的VM arguments 中输入-Xms32m -Xmx800m这个参数就可以了。    

后来在Eclilpse中修改了启动参数，在VM arguments 加入了-Xms32m -Xmx800m，问题解决。   



### 实例1
以下给出1G内存环境下java jvm 的参数设置参考：   

	JAVA_OPTS="-server -Xms800m -Xmx800m -XX:PermSize=64M -XX:MaxNewSize=256m -XX:MaxPermSize=128m -Djava.awt.headless=true "    

很大的web工程，用tomcat默认分配的内存空间无法启动，如果不是在myeclipse中启动tomcat可以对tomcat这样设置： 

TOMCAT_HOME\bin\catalina.bat 中添加这样一句话： 

      set JAVA_OPTS= -Xmx1024M -Xms512M -XX:MaxPermSize=256m 

如果要在myeclipse中启动，上述的修改就不起作用了，可如下设置： 

	Myeclipse->preferences->myeclipse->servers->tomcat->tomcat×.×->JDK面板中的    

	Optional Java VM arguments中添加：-Xmx1024M -Xms512M -XX:MaxPermSize=256m 

以上是转贴，但本人遇见的问题是：在myeclipse中启动Tomcat时，提示"java.lang.OutOfMemoryError: Java heap space"，解决办法就是： 

	Myeclipse->preferences->myeclipse->servers->tomcat->tomcat×.×->JDK面板中的 

	Optional Java VM arguments中添加：-Xmx1024M -Xms512M -XX:MaxPermSize=256m 

挺灵的。 
--------------------------------------------------------- 
tomcat 启动内存设置 
其初始空间(即-Xms)是物理内存的1/64，最大空间(-Xmx)是物理内存的1/4。可以利用JVM提供的-Xmn -Xms -Xmx等选项可 
进行设置 
### 实例2
以下给出1G内存环境下java jvm 的参数设置参考： 
  
	JAVA_OPTS="-server -Xms800m -Xmx800m -XX:PermSize=64M -XX:MaxNewSize=256m -XX:MaxPermSize=128m -Djava.awt.headless=true "   
	JAVA_OPTS="-server -Xms768m -Xmx768m -XX:PermSize=128m -XX:MaxPermSize=256m -XX:  
	NewSize=192m -XX:MaxNewSize=384m" 
	CATALINA_OPTS="-server -Xms768m -Xmx768m -XX:PermSize=128m -XX:MaxPermSize=256m 
     -XX:NewSize=192m -XX:MaxNewSize=384m" 

Linux： 

	在/usr/local/apache-tomcat-5.5.23/bin目录下的catalina.sh 
	添加：JAVA_OPTS='-Xms512m -Xmx1024m' 
	要加“m”说明是MB，否则就是KB了，在启动tomcat时会报内存不足。 
	 Xms：初始值 
     -Xmx：最大值 
	 -Xmn：最小值 

Windows 

	在catalina.bat最前面加入 

	set JAVA_OPTS=-Xms128m -Xmx350m 

	如果用startup.bat启动tomcat,OK设置生效.够成功的分配200M内存. 
	但是如果不是执行startup.bat启动tomcat而是利用windows的系统服务启动tomcat服务,上面的设置就不生效了, 
	就是说set JAVA_OPTS=-Xms128m -Xmx350m 没起作用.上面分配200M内存就OOM了.. 
	windows服务执行的是bin\tomcat.exe.他读取注册表中的值,而不是catalina.bat的设置. 

解决办法: 

修改注册表

	HKEY_LOCAL_MACHINE\SOFTWARE\Apache Software Foundation\Tomcat Service Manager\Tomcat5\Parameters\JavaOptions 

原值为 

	-Dcatalina.home="C:\ApacheGroup\Tomcat 5.0" 
	-Djava.endorsed.dirs="C:\ApacheGroup\Tomcat 5.0\common\endorsed" 
	-Xrs 
	加入 -Xms300m -Xmx350m 
	重起tomcat服务,设置生效 

如果对你的问题解决有所帮助，请点击推荐，谢谢合作！

看过此文人都会关注：

http://www.cnblogs.com/swite/p/6293391.html