---
title: Java教程
tags:
  - java
categories: java
description: Java快速入门
abbrlink: b9cb
---

## Java教程
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/java.jpg) 
### Java快速入门

本章的主要内容是快速掌握Java程序的基础知识，了解并使用变量和各种数据类型，介绍基本的程序流程控制语句。
通过本章的学习，可以编写基本的Java程序。
### Java简介
Java最早是由SUN公司（已被Oracle收购）的詹姆斯·高斯林（高司令，人称Java之父）在上个世纪90年代初开发的一种编程语言，最初被命名为Oak，目标是针对小型家电设备的嵌入式应用，结果市场没啥反响。谁料到互联网的崛起，让Oak重新焕发了生机，于是SUN公司改造了Oak，在1995年以Java的名称正式发布，原因是Oak已经被人注册了，因此SUN注册了Java这个商标。随着互联网的高速发展，Java逐渐成为最重要的网络编程语言。

Java介于编译型语言和解释型语言之间。编译型语言如C、C++，代码是直接编译成机器码执行，但是不同的平台（x86、ARM等）CPU的指令集不同，因此，需要编译出每一种平台的对应机器码。解释型语言如Python、Ruby没有这个问题，可以由解释器直接加载源码然后运行，代价是运行效率太低。而Java是将代码编译成一种“字节码”，它类似于抽象的CPU指令，然后，针对不同平台编写虚拟机，不同平台的虚拟机负责加载字节码并执行，这样就实现了“一次编写，到处运行”的效果。当然，这是针对Java开发者而言。对于虚拟机，需要为每个平台分别开发。为了保证不同平台、不同公司开发的虚拟机都能正确执行Java字节码，SUN公司制定了一系列的Java虚拟机规范。从实践的角度看，JVM的兼容性做得非常好，低版本的Java字节码完全可以正常运行在高版本的JVM上。

随着Java的发展，SUN给Java又分出了三个不同版本：

	Java SE：Standard Edition
	
	Java EE：Enterprise Edition
	
	Java ME：Micro Edition

这三者之间有啥关系呢？   

	┌───────────────────────────┐   
	│Java EE                    │     
	│    ┌────────────────────┐ │   
	│    │Java SE             │ │   
	│    │    ┌─────────────┐ │ │   
	│    │    │   Java ME   │ │ │   
	│    │    └─────────────┘ │ │    
	│    └────────────────────┘ │   
	└───────────────────────────┘
简单来说，Java SE就是标准版，包含标准的JVM和标准库，而Java EE是企业版，它只是在Java SE的基础上加上了大量的API和库，以便方便开发Web应用、数据库、消息服务等，Java EE的应用使用的虚拟机和Java SE完全相同。

Java ME就和Java SE不同，它是一个针对嵌入式设备的“瘦身版”，Java SE的标准库无法在Java ME上使用，Java ME的虚拟机也是“瘦身版”。

毫无疑问，Java SE是整个Java平台的核心，而Java EE是进一步学习Web应用所必须的。我们熟悉的Spring等框架都是Java EE开源生态系统的一部分。不幸的是，Java ME从来没有真正流行起来，反而是Android开发成为了移动平台的标准之一，因此，没有特殊需求，不建议学习Java ME。

因此我们推荐的Java学习路线图如下：

首先要学习Java SE，掌握Java语言本身、Java核心开发技术以及Java标准库的使用；

如果继续学习Java EE，那么Spring框架、数据库开发、分布式架构就是需要学习的；

如果要学习大数据开发，那么Hadoop、Spark、Flink这些大数据平台就是需要学习的，他们都基于Java或Scala开发；

如果想要学习移动开发，那么就深入Android平台，掌握Android App开发。

无论怎么选择，Java SE的核心技术是基础，这个教程的目的就是让你完全精通Java SE！

Java版本
从1995年发布1.0版本开始，到目前为止，最新的Java版本是Java 12：

	时间	版本
	1995	1.0
	1998	1.2
	2000	1.3
	2002	1.4
	2004	1.5 / 5.0
	2005	1.6 / 6.0
	2011	1.7 / 7.0
	2014	1.8 / 8.0
	2017/9	1.9 / 9.0
	2018/3	10
	2018/9	11
	2019/3	12
本教程使用的Java版本是最新版的Java 12。

名词解释
初学者学Java，经常听到JDK、JRE这些名词，它们到底是啥？

	JDK：Java Development Kit
	JRE：Java Runtime Environment
简单地说，JRE就是运行Java字节码的虚拟机。但是，如果只有Java源码，要编译成Java字节码，就需要JDK，因为JDK除了包含JRE，还提供了编译器、调试器等开发工具。

二者关系如下：

	  ┌─    ┌──────────────────────────────────┐
	  │     │     Compiler, debugger, etc.     │
	  │     └──────────────────────────────────┘
	 JDK ┌─ ┌──────────────────────────────────┐
	  │  │  │                                  │
	  │ JRE │      JVM + Runtime Library       │
	  │  │  │                                  │
	  └─ └─ └──────────────────────────────────┘
	        ┌───────┐┌───────┐┌───────┐┌───────┐
	        │Windows││ Linux ││ macOS ││others │
	        └───────┘└───────┘└───────┘└───────┘
要学习Java开发，当然需要安装JDK了。

那JSR、JCP……又是啥？

JSR规范：Java Specification Request
JCP组织：Java Community Process
为了保证Java语言的规范性，SUN公司搞了一个JSR规范，凡是想给Java平台加一个功能，比如说访问数据库的功能，大家要先创建一个JSR规范，定义好接口，这样，各个数据库厂商都按照规范写出Java驱动程序，开发者就不用担心自己写的数据库代码在MySQL上能跑，却不能跑在PostgreSQL上。

所以JSR是一系列的规范，从JVM的内存模型到Web程序接口，全部都标准化了。而负责审核JSR的组织就是JCP。

一个JSR规范发布时，为了让大家有个参考，还要同时发布一个“参考实现”，以及一个“兼容性测试套件”：

RI：Reference Implementation
TCK：Technology Compatibility Kit
比如有人提议要搞一个基于Java开发的消息服务器，这个提议很好啊，但是光有提议还不行，得贴出真正能跑的代码，这就是RI。如果有其他人也想开发这样一个消息服务器，如何保证这些消息服务器对开发者来说接口、功能都是相同的？所以还得提供TCK。

通常来说，RI只是一个“能跑”的正确的代码，它不追求速度，所以，如果真正要选择一个Java的消息服务器，一般是没人用RI的，大家都会选择一个有竞争力的商用或开源产品。

### 安装JDK
因为Java程序必须运行在JVM之上，所以，我们第一件事情就是安装JDK。

搜索JDK 12，确保从Oracle的官网下载最新的稳定版JDK： 

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/l.jpg)  
找到Java SE 12.x的下载链接，下载安装即可。

设置环境变量
安装完JDK后，需要设置一个JAVA_HOME的环境变量，它指向JDK的安装目录。在Windows下，它是安装目录，类似：

	C:\Program Files\Java\jdk-12
在Mac下，它在~/.bash_profile里，它是：

	export JAVA_HOME=`/usr/libexec/java_home -v 12`
然后，把JAVA_HOME的bin目录附加到系统环境变量PATH上。在Windows下，它长这样：

	Path=%JAVA_HOME%\bin;<现有的其他路径>
在Mac下，它在~/.bash_profile里，长这样：

	export PATH=$JAVA_HOME%\bin:$PATH
把JAVA_HOME的bin目录添加到PATH中是为了在任意文件夹下都可以运行java。打开命令提示符窗口，输入命令java -version，如果一切正常，你会看到如下输出：

	┌────────────────────────────────────────────────────────┐
	│Command Prompt                                    - □ x │
	├────────────────────────────────────────────────────────┤
	│Microsoft Windows [Version 10.0.0]                      │
	│(c) 2015 Microsoft Corporation. All rights reserved.    │
	│                                                        │
	│C:\> java -version                                      │
	│java version "12" ...                                   │
	│Java(TM) SE Runtime Environment                         │
	│Java HotSpot(TM) 64-Bit Server VM                       │
	│                                                        │
	│C:\>                                                    │
	│                                                        │
	│                                                        │
	└────────────────────────────────────────────────────────┘
如果你看到的版本号不是12，而是11、1.8之类，说明系统存在多个JDK，且默认JDK不是JDK 12，需要把JDK 12提到PATH前面。

如果你得到一个错误输出：

	┌────────────────────────────────────────────────────────┐
	│Command Prompt                                    - □ x │
	├────────────────────────────────────────────────────────┤
	│Microsoft Windows [Version 10.0.0]                      │
	│(c) 2015 Microsoft Corporation. All rights reserved.    │
	│                                                        │
	│C:\> java -version                                      │
	│'java' is not recognized as an internal or external comm│
	│and, operable program or batch file.                    │
	│                                                        │
	│C:\>                                                    │
	│                                                        │
	│                                                        │
	│                                                        │
	└────────────────────────────────────────────────────────┘
这是因为系统无法找到Java虚拟机的程序java.exe，需要检查JAVA_HOME和PATH的配置。

可以参考如何设置或更改PATH系统变量。

JDK
细心的童鞋可以在JAVA_HOME的bin目录下找到很多可执行文件：

	java：这个可执行程序其实就是JVM，运行Java程序，就是启动JVM，然后让JVM执行指定的编译后的代码；
	javac：这是Java的编译器，它用于把Java源码文件（以.java后缀结尾）编译为Java字节码文件（以.class后缀结尾）；
	jar：用于把一组.class文件打包成一个.jar文件，便于发布；
	javadoc：用于从Java源码中自动提取注释并生成文档；
	jdb：Java调试器，用于开发阶段的运行调试。
### 第一个Java程序
我们来编写第一个Java程序。

打开文本编辑器，输入以下代码：

	public class Hello {
	    public static void main(String[] args) {
	        System.out.println("Hello, world!");
	    }
	}
在一个Java程序中，你总能找到一个类似：

	public class Hello {
	    ...
	}
的定义，这个定义被称为class（类），这里的类名是Hello，大小写敏感，class用来定义一个类，public表示这个类是公开的，public、class都是Java的关键字，必须小写，Hello是类的名字，按照习惯，首字母H要大写。而花括号{}中间则是类的定义。

注意到类的定义中，我们定义了一个名为main的方法：

    public static void main(String[] args) {
        ...
    }
方法是可执行的代码块，一个方法除了方法名main，还有用()括起来的方法参数，这里的main方法有一个参数，参数类型是String[]，参数名是args，public、static用来修饰方法，这里表示它是一个公开的静态方法，void是方法的返回类型，而花括号{}中间的就是方法的代码。

方法的代码每一行用;结束，这里只有一行代码，就是：

        System.out.println("Hello, world!");
它用来打印一个字符串到屏幕上。

Java规定，某个类定义的public static void main(String[] args)是Java程序的固定入口方法，因此，Java程序总是从main方法开始执行。

注意到Java源码的缩进不是必须的，但是用缩进后，格式好看，很容易看出代码块的开始和结束，缩进一般是4个空格或者一个tab。

最后，当我们把代码保存为文件时，文件名必须是Hello.java，而且文件名也要注意大小写，因为要和我们定义的类名Hello完全保持一致。

如何运行Java程序
Java源码本质上是一个文本文件，我们需要先用javac把Hello.java编译成字节码文件Hello.class，然后，用java命令执行这个字节码文件：

	┌──────────────────┐
	│    Hello.java    │<─── source code
	└──────────────────┘
	          │ compile
	          ▼
	┌──────────────────┐
	│   Hello.class    │<─── byte code
	└──────────────────┘
	          │ execute
	          ▼
	┌──────────────────┐
	│    Run on JVM    │
	└──────────────────┘
因此，可执行文件javac是编译器，而可执行文件java就是虚拟机。

第一步，在保存Hello.java的目录下执行命令javac Hello.java：

	$ javac Hello.java
如果源代码无误，上述命令不会有任何输出，而当前目录下会产生一个Hello.class文件：

	$ ls
	Hello.class	Hello.java
第二步，执行Hello.class，使用命令java Hello：

	$ java Hello
	Hello, world!
注意：给虚拟机传递的参数Hello是我们定义的类名，虚拟机自动查找对应的class文件并执行。

有一些童鞋可能知道，直接运行java Hello.java也是可以的：

	$ java Hello.java 
	Hello, world!
这是Java 11新增的一个功能，它可以直接运行一个单文件源码！

需要注意的是，在实际项目中，单个不依赖第三方库的Java源码是非常罕见的，所以，绝大多数情况下，我们无法直接运行一个Java源码文件，原因是它需要依赖其他的库。

小结

	一个Java源码只能定义一个public类型的class，并且class名称和文件名要完全一致；
	
	使用javac可以将.java源码编译成.class字节码；
	
	使用java可以运行一个已编译的Java程序，参数是类名。

### Java代码助手
Java代码运行助手可以让你在线输入Java代码，然后通过本机运行的一个Java程序来执行代码。原理如下：

在网页输入代码；

点击Run按钮，代码被发送到本机正在运行的Java代码运行助手；

Java代码运行助手将代码保存为临时文件，然后调用Java虚拟机执行代码；

网页显示代码执行结果：  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/1.png)  
下载
点击右键，目标另存为：下载练习：LearnJava.java （推荐使用IDE练习插件快速下载）

运行
在存放LearnJava.java的目录下运行命令：

	C:\Users\michael\Downloads> java LearnJava.java
如果看到Ready for Java code on port 39193...表示运行成功。

不要关闭命令行窗口，最小化放到后台运行即可：

	┌────────────────────────────────────────────────────────┐
	│Command Prompt                                    - □ x │
	├────────────────────────────────────────────────────────┤
	│Microsoft Windows [Version 10.0.0]                      │
	│(c) 2015 Microsoft Corporation. All rights reserved.    │
	│                                                        │
	│C:\Users\michael\Downloads> java LearnJava.java         │
	│Ready for Java code on port 39193...                    │
	│Press Ctrl + C to exit...                               │
	│                                                        │
	│                                                        │
	│                                                        │
	│                                                        │
	│                                                        │
	└────────────────────────────────────────────────────────┘
试试效果
需要支持HTML5的浏览器：

IE >= 9
Firefox
Chrome
Sarafi

### 使用IDE
IDE是集成开发环境：Integrated Development Environment的缩写。

使用IDE的好处在于按，可以把编写代码、组织项目、编译、运行、调试等放到一个环境中运行，能极大地提高开发效率。

IDE提升开发效率主要靠以下几点：

编辑器的自动提示，可以大大提高敲代码的速度；

代码修改后可以自动重新编译，并直接运行；

可以方便地进行断点调试。

目前，流行的用于Java开发的IDE有：

Eclipse
Eclipse是由IBM开发并捐赠给开源社区的一个IDE，也是目前应用最广泛的IDE。Eclipse的特点是它本身是Java开发的，并且基于插件结构，即使是对Java开发的支持也是通过插件JDT实现的。

除了用于Java开发，Eclipse配合插件也可以作为C/C++开发环境、PHP开发环境、Rust开发环境等。

IntelliJ Idea
IntelliJ Idea是由JetBrains公司开发的一个功能强大的IDE，分为免费版和商用付费版。JetBrains公司的IDE平台也是基于IDE平台+语言插件的模式，支持Python开发环境、Ruby开发环境、PHP开发环境等，这些开发环境也分为免费版和付费版。

NetBeans
NetBeans是最早由SUN开发的开源IDE，由于使用人数较少，目前已不再流行。

使用Eclipse
你可以使用任何IDE进行Java学习和开发。我们不讨论任何关于IDE的优劣，本教程使用Eclipse作为开发演示环境，原因在于：

完全免费使用；
所有功能完全满足Java开发需求。
如果你使用Eclipse作为开发环境来学习本教程，还可以获得一个额外的好处：教程提供了一个基于Eclipse的IDE练习插件，可以直接在线导入Java工程！

安装Eclipse
Eclipse的发行版提供了预打包的开发环境，包括Java、JavaEE、C++、PHP、Rust等。从这里下载：

我们需要下载的版本是Eclipse IDE for Java Developers：  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/IDE.jpg)  
设置Eclipse
下载并安装完成后，我们启动Eclipse，对IDE环境做一个基本设置：

选择菜单“Eclipse/Window”-“Preferences”，打开配置对话框：
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/ecplise_preferences.jpg)  
我们需要调整以下设置项：

General > Editors > Text Editors
钩上“Show line numbers”，这样编辑器会显示行号；

General > Workspace
钩上“Refresh using native hooks or polling”，这样Eclipse会自动刷新文件夹的改动；

对于“Text file encoding”，如果Default不是UTF-8，一定要改为“Other：UTF-8”，所有文本文件均使用UTF-8编码；

对于“New text file line delimiter”，建议使用Unix，即换行符使用\n而不是Windows的\r\n。

Java > Compiler
将“Compiler compliance level”设置为11，本教程的所有代码均使用Java 12的语法，并且编译到Java 11的版本。

 为什么Compiler compliance level没有12？因为Java 12编译出的class与Java 11完全相同，所以只能选择11。
Java > Installed JREs
在Installed JREs中应该看到Java SE 12，如果还有其他的JRE，可以删除，以确保Java SE 12是默认的JRE。

Eclipse IDE结构
打开Eclipse后，整个IDE由若干个区域组成：

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/lean.jpg)   
中间可编辑的文本区（见1）是编辑器，用于编辑源码；
分布在左右和下方的是视图：
Package Exploroer（见2）是Java项目的视图
Console（见3）是命令行输出视图
Outline（见4）是当前正在编辑的Java源码的结构视图
视图可以任意组合，然后把一组视图定义成一个Perspective（见5），Eclipse预定义了Java、Debug等几个Perspective，用于快速切换。   
新建Java项目
在Eclipse菜单选择“File”-“New”-“Java Project”，填入HelloWorld，JRE选择Java SE 12：  
 
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/helloworld.png)  
暂时不要勾选“Create module-info.java file”，因为模块化机制我们后面才会讲到： 
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/javasettings.png)  
点击“Finish”就成功创建了一个名为HelloWorld的Java工程。

新建Java文件并运行

展开HelloWorld工程，选中源码目录src，点击右键，在弹出菜单中选择“New”-“Class”：
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/class.
在弹出的对话框中，Name一栏填入Hello：
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/javaclass.png) 

点击”Finish“，就自动在src目录下创建了一个名为Hello.java的源文件。我们双击打开这个源文件，填上代码：
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/hellojpg.jpg) 
在Console窗口中就可以看到运行结果：
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/result.png) 
