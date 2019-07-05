---
title: Python3教程
tags:
  - python3
categories: python3
description: python3快速入门
abbrlink: 18ba
---

## Python的概述与环境安装 
### Python语言介绍和发展历史
Python是一门高级的、面向对象的、解释性、脚本语言。   
高级语言：贴近开发者，对应底层语言，底层语言贴近机器；java、C#、php 。  
面向对象对应于面向过程，是开发人员在开发过程当中的思路，是程序员的世界观，Python 一切皆 对象。  
解释性对应于编译性语言。   
解释性语言： 解释型语言在程序执行时，有一个编译的过程，这样解释性语言每执行一次就要翻译一次。   
编译性语言： 编译型语言在程序执行之前，有一个单独的编译过程，将程序翻译成机器语言，以后执行这个程序的时候， 就不用再进行翻译了。   
脚本语言是一种解释性的语言,例如vbscript,javascript,installshield script,ActionScript等等,它 不像c\c++等可以编译成二进制代码,以可执行文件的形式存在.脚本语言不需要编译，可以直接用，由解 释器来负责解释。 脚本语言一般都是以文本形式存在,类似于一种命令。   
Python 起源 Python的作者，Guido von Rossum（吉多·范罗苏姆）我们称他为‘龟叔’，荷兰人。1982 年， Guido从阿姆斯特丹大学获得了数学和计算机硕士学位。然而，尽管他算得上是一位数学家，但他更加享 受计算机带来的乐趣。用他的话说，尽管拥有数学和计算机双料资质，他总趋向于做计算机相关的工作， 并热衷于做任何和编程相关的活儿。在那个时候，Guido 接触并使用过诸如 Pascal [ˈpæskəl]、C、 Fortran[ˈfɔ:træn] 等语言。这些语言的基本设计原则是让机器能更快运行。   
在 80 年代，虽然 IBM 和苹果已经掀起了个人电脑浪潮，但这些个人电脑的配置很低。
比如早期的 Macintosh(麦金塔电脑)，只有8MHz的CPU主频和 128KB的 RAM，一个大的数组就能占满内存。所 有的编译器的核心是做优化，以便让程序能够运行。为了增进效率，语言也迫使程序员像计算机一样思考， 以便能写出更符合机器口味的程序。   
在那个时代，程序员恨不得用手榨取计算机每一寸的能力。有人甚至认为C语言的指针是在浪费内存。    
至于动态类型，内存自动管理，面向对象…… 别想了，那会让你的电脑陷入瘫痪。      
这种编程方式让Guido感到苦恼。Guido知道如何用 C语言写出一个功能，但整个编写过程需要耗 费大量的时间，即使他已经准确的知道了如何实现。他的另一个选择是shell。      
BourneShell(是一个交换 式的命令解释器和命令编程语言)作为UNIX系统的解释器已经长期存在。UNIX的管理员们常常用shell 去写一些简单的脚本，以进行一些系统维护的工作，比如定期备份、文件系统管理等等。   
shell可以像胶水一样，将UNIX下的许多功能连接在一起。   
许多C语言下上百行的程序，在shell下只用几行就可以完成。    
然而，shell的本质是调用命令。它并不是一个真正的语言。   
比如说，shell 没有数值型的数据类型，加法 运算都很复杂。    
总之，shell不能全面的调动计算机的功能。      
HOW TO用于定义一个函数。    
一个Python程序员应该很容易理解这段程序。    
ABC语言使用冒号和 缩进来表示程序块、行尾没有分号、for和if结构中也没有括号() 、赋值采用的是PUT，而不是更常见的 等号。这些改动让ABC程序读起来像一段文字。     
尽管已经具备了良好的可读性和易用性，ABC语言最终 没有流行起来。    
在当时，ABC语言编译器需要比较高配置的电脑才能运行。而这些电脑的使用者通常精通计算机，它 们更多考虑程序的效率，而非它的学习难度。除了硬件上的困难外，ABC语言的设计也存在一些致命的问 题： 可拓展性差。    
ABC语言不是模块化语言。    
如果想在ABC 语言中增加功能，比如对图形化的支持，就必须改动很多 地方，它不能直接进行IO。   
ABC语言不能直接操作文件系统。尽管你可以通过诸如文本流的方式导入数据，但ABC 无法直接读 写文件。输入输出的困难对于计算机语言来说是致命的。
你能想像一个打不开车门的跑车么？    
尽管ABC语言很特别，但学习难度 也很大；    
传播困难ABC编译器很大，必须被保存在磁带上；    
当时Guido在访问的时候，就必须有一个大磁带来给别人安装 ABC编译器。    
这样，ABC语言就很 难快速传播。     
1989 年，为了打发圣诞节假期（寂寞难耐），Guido开始写Python语言的编译器。
Python这个 名字，来自Guido所挚爱的电视剧Monty Python's Flying Circus(飞行马戏团)。
他希望这个新的叫做 Python的语言，能符合他的理想：创造一种C和shell之间，功能全面，易学易用，可拓展的语言。   Guido作为一个语言设计爱好者，已经有过设计语言的尝试。    
这一次， 也不过是一次纯粹的hacking(搬 运)行为。   
一门语言的诞生 1991 年，第一个Python编译器诞生。   
它是用C语言实现的，并能够调用C语言的库文件。   
从一出 生，Python已经具有了 ：类，函数，异常处理，包含表和词典在内的核心数据类型，以及模块为基础的 拓展系统。 
Python语法很多来自 C，但又受到ABC 语言的强烈影响。来自ABC语言的一些规定直到今 天还富有争议，比如强制缩进。 但这些语法规定让Python容易读。    
另一方面，Python聪明的选择服从 一些惯例，特别是C语言的惯例，比如回归等号赋值。Guido认为，如果“常识”上确立的东西，没有必 要过度纠结。     
Python从一开始就特别在意可拓展性。Python可以在多个层次上拓展。从高层上，你可 以直接引入. py文件。在底层，你可以引用C语言的库。    
Python程序员可以快速的使用Python写. py 文件作为拓展模块。但当性能是考虑的重要因素时，Python程序员可以深入底层，写C程序，编译为.so 文件引入到Python中使用。   
Python就好像是使用钢构建房一样，先规定好大的框架。   
而程序员可以在 此框架下相当自由的拓展或更改。    
最初的Python完全由Guido本人开发。    
Python得到Guido同事的 欢迎。    
他们迅速的反馈使用意见，并参与到Python的改进。Guido和一些同事构成Python的核心团队。    
他们将自己大部分的业余时间用于 hack(熟练地编辑) Python。   
随后，Python 拓 展到研究所之外。    
Python将许多机器层面上的细节隐藏，交给编译器处理，并凸显出逻辑层面的编程思考。
Python 程序 员可以花更多的时间用于思考程序的逻辑，而不是具体的实现细节。这一特征吸引了广大的程序员。 
Python 开始流行。
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/20190624220026_龟叔.png)  
人生苦短，我用Python   
启示录  
Python崇尚优美、清晰、简单，是一个优秀并广泛使用的语言。
Python在TIOBE排行榜中排行第三，它是Google的第三大开发语言，Dropbox的基础语言，豆瓣的服务器语言。   
Python的发展史可以 作为一个代表，带给我许多启示。    
在Python的开发过程中，社区起到了重要的作用。    
Guido自认为自己不是全能型的程序员，所以他只负责制订框架。如果问题太复杂，他会选择绕过去， 也就是cut the corner（走捷径）。    
这些问题最终由社区中的其他人解决。   
社区中的人才是异常丰富的， 就连创建网站，筹集基金这样与开发稍远的事情，也有人乐意于处理。如今的项目开发越来越复杂，越来 越庞大，合作以及开放的心态成为项目最终成功的关键。     
Python从其他语言中学到了很多，无论是已经进入历史的ABC，还是依然在使用的C和Perl，以 及许多没有列出的其他 语言。可以说，Python的成功代表了它所有借鉴的语言的成功。    
同样，Ruby借 鉴了 Python，它的成功也代表了Python某些方面的成功。   
每个语言都是混合体，都有它优秀的地方， 但也有各种各样的缺陷。    
同时，一个语言“好与不好”的评 判，往往受制于平台、硬件、时代等等外部原因。    
程序员经历过许 多语言之争。    
其实，以开放的心态来接受各个语言，说不定哪一天，程序员也可以如Guido那样，混合出 自己的语言。    
关键点常识 Python/ˈpaɪθən/的发音与拼写 Python的意思是蟒蛇，源于作者喜欢的一部电视剧 Python的作者是Guido van Rossum（吉多·范罗苏姆） Python是龟叔在1989 年圣诞节期间，为了打发无聊的圣诞节而用C编写的一个编程语言 Python正式诞生于1991 年 Python的解释器如今有多个语言实现，我们常用的是CPython（官方版本的C语言实现），其他还 有Jython（可以运行在Java平台）、IronPython（可以运行在.NET和 Mono平台）、PyPy（Python 实现的，支持JIT即时编译）   
Python目前有两个版本，Python2和Python3，最新版分别为2.7.15 和3.7，现阶段大部分公司 用的是Python2 和Python3 Life is shot, you need Python. 人生苦短，我用Python。    
2019 年3月份 编程语言流行排行榜 （https://www.tiobe.com/tiobe-index/）
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/20190624222131python_top.png) 
### Python优缺点 
#### 优点   
简单————Python是一种代表简单主义思想的语言。阅读一个良好的Python程序就感觉像是在 读英语一样，Python的这种伪代码本质是它最大的优点之一。它使你能够专注于解决问题而不是去搞明 白语言本身。   
易学————就如同你即将看到的一样，Python极其容易上手。前面已经提到了，Python有极其 简单的语法。   
免费、开源————Python是FLOSS（自由/开放源码软件）之一。简单地说，你可以自由地发布 这个软件的拷贝、阅读它的源代码、对它做改动、把它的一部分用于新的自由软件中。FLOSS是基于一个 团体分享知识的概念。这是为什么Python如此优秀的原因之一——它是由一群希望看到一个更加优秀的 Python的人创造并经常改进着的。   
高层语言————当你用Python语言编写程序的时候，你无需考虑诸如如何管理你的程序使用的内 存一类的底层细节。 
可移植性————由于它的开源本质，Python已经被移植在许多平台上（经过改动使它能够工作在 不同平台上）。如果你小心地避免使用依赖于系统的特性，那么你的所有Python程序无需修改就可以在 下述任何平台上面运行。这些平台包括Linux、Windows、FreeBSD、Macintosh、Solaris、OS/2、 Amiga、AROS、AS/400、BeOS、OS/390、z/OS、PalmOS、QNX、VMS、Psion、AcomRISCOS、 VxWorks、PlayStation、SharpZaurus、WindowsCE甚至还有PocketPC、Symbian以及Google 基于linux开发的Android平台！   
解释性————这一点需要一些解释。一个用编译性语言比如C或C++写的程序可以从源文件（即 C或C++语言）转换到一个你的计算机使用的语言（二进制代码，即0和1）。这个过程通过编译器和不 同的标记、选项完成。当你运行你的程序的时候，连接/转载器软件把你的程序从硬盘复制到内存中并且运 行。 而Python语言写的程序不需要编译成二进制代码，你可以直接从源代码运行程序。在计算机内部， Python解释器把源代码转换成称为字节码的中间形式，然后再把它翻译成计算机使用的机器语言并运行。 事实上，由于你不再需要担心如何编译程序，如何确保连接转载正确的库等等，所有这一切使得使用 Python更加简单。由于你只需要把你的Python程序拷贝到另外一台计算机上，它就可以工作了，这也 使得你的Python程序更加易于移植。    
面向对象————Python既支持面向过程的编程也支持面向对象的编程。在“面向过程”的语言中，
程序是由过程或仅仅是可重用代码的函数构建起来的。在“面向对象”的语言中，程序是由数据和功能组 合而成的对象构建起来的。与其他主要的语言如C++和Java相比，Python以一种非常强大又简单的方 式实现面向对象编程。    
可扩展性————如果你需要你的一段关键代码运行得更快或者希望某些算法不公开，你可以把你的 部分程序用C或C++编写，然后在你的Python程序中使用它们。    
丰富的库————Python标准库确实很庞大。它可以帮助你处理各种工作，包括正则表达式、文档 生成、单元测试、线程、数据库、网页浏览器、CGI、FTP、电子邮件、XML、XML-RPC、HTML、WAV 文件、密码系统、GUI（图形用户界面）、Tk和其他与系统有关的操作。记住，只要安装了Python，所 有这些功能都是可用的。这被称作Python的“功能齐全”理念。除了标准库以外，还有许多其他高质量 的库，如wxPython、Twisted（是用Python实现的基于事件驱动的网络引擎框架）和Python图像库 等等。   
规范的代码————Python采用强制缩进的方式使得代码具有极佳的可读性。      
#### 缺点 
1. 速度慢 由于Python是解释型语言，所有它的速度会比，C、C++慢一些，但是不影响使用。由 于，现在的硬件配置都非常高，基本上没有影响，除非是一些实时性比较强的程序可能会受到一些影响， 但是也有解决办法，可以嵌入C程序。
2. 强制缩进 如果你有其他语言的编程经验，例如：C语言或者Java语言，那么Python的强制缩进 一开始会让你很不习惯。但是如果你习惯了Python的缩进语法，你会觉得它非常优雅。 
3. 单行语句 由于Python可以在尾部不写分号，所以一行只能有一条语句，这可能也算是一个不足 吧，不过这真的微不足道。   
Python应用场景    
Web应用开发 Python经常被用于Web开发。比如，通过mod_wsgi模块，Apache可以运行用Python编写的 Web程序。Python定义了WSGI（是Python应用程序或框架和Web服务器之间的一种接口）标准应 用接口来协调Http服务器与基于Python的Web程序之间的通信。一些Web框架，如 Django,flask,tornado,Zope等，可以让程序员轻松地开发和管理复杂的Web程序。 操作系统管理、服务器运维的自动化脚本 在很多操作系统里，Python是标准的系统组件。 大多数Linux发行版以及NetBSD、OpenBSD 和Mac OS X都集成了Python，可以在终端下直接运行Python。有一些Linux发行版的安装器使用 Python语言编写，比如Ubuntu的Ubiquity安装器,RedHatLinux和Fedora的Anaconda安装器。 GentooLinux使用Python来编写它的Portage包管理系统。Python标准库包含了多个调用操作系统 功能的库。 通过pywin32这个第三方软件包， Python能够访问Windows的COM服务及其它WindowsAPI。 使用IronPython，Python程序能够直接调用.Net Framework。一般说来，Python编写的系统管理 脚本在可读性、性能、代码重用度、扩展性几方面都优于普通的shell脚本。 科学计算 NumPy,SciPy,Matplotlib可以让Python程序员编写科学计算程序。 桌面软件 PyQt、PySide、wxPython、PyGTK是Python快速开发桌面应用程序的利器。 服务器软件（网络软件） Python对于各种网络协议的支持很完善，因此经常被用于编写服务器软件、网络爬虫。第三方库 Twisted[ˈtwɪstɪd] 支持异步网络编程和多数标准的网络协议(包含客户端和服务器)，并且提供了多种工 具，被广泛用于编写高性能的服务器软件。 游戏 很多游戏使用C++编写图形显示等高性能模块，而使用Python或者Lua编写游戏的逻辑、服务器。
相较于Python，Lua的功能更简单、体积更小；而Python则支持更多的特性和数据类型。 YouTube、Google、Yahoo!、NASA都在内部大量地使用Python。 上课主要以Python3.5.0 为主(为什么要以3为主呢？) Python核心团队计划在2020年停止支持Python2。 NumPy项目自2010年以来一直支持Python 2和Python3，并且发现支持Python2对我们有限的资源增加了负担；因此，我们最终计划将停止支持 Python 2。 到2018年12月31日为止，所有的NumPy版本都将完全支持Python2 和Python3。 从2019年1月1日开始，任何新的功能版本都只支持Python3。 国内是Python2和Python3并存，官方和我现在极力推荐使用Python3 
### Python2与Python3的比较 
print语句    
Python2中print是一个语句，无论想输出什么，直接放到print关键字后面即可。   
Python3里，print()是一个函数，像其他函数一样，print()需要你将要输出的东西作为参数传给它。 Python2 Python3 备注 
print print() 输出一个空白行，Python3需要调用不带参数的print()
print 1 print(1) 输出一个值，将值传入print()函数
print 1, 2 print(1,2) 输出使用空格分割的两个值，使用两个参数调用print()
<>比较运算符 Python2支持<>作为!=的同义词，Python3只支持!=, 不再支持<> 1.2. 3 unicode字符串 Python2中有两种字符串类型：Unicode字符串和非Unicode字符串。Python3中只有一种类型： Unicode字符串。 1.2. 4 long长整型 Python2有为非浮点数准备的int和long类型。 int类型的最大值不能超过sys.maxint，而且这个 最大值是平台相关的。可以通过在数字的末尾附上一个L来定义长整型，显然，它比int类型表示的数字 范围更大。 在Python3里，只有一种整数类型int，大多数情况下，它很像Python2里的长整型。由于已经不 存在两种类型的整数，所以就没有必要使用特殊的语法去区别他们。 
### Python3的安装 
Python3安装 直接到官网https://www.Python.org/下载，安装就可以了。 安装比较简单，点exe文件一直下一步就可以了（注意：安装的时候有个选择是否添加环境变量，这 个选是，之后就不用添加环境变量了）如果没有，请添加环境变量。 右键点击计算机 点击属性 高级系统设置 环境变量 系统变量里的path 编辑添加安装Python的路径 （例如D:xuegod;D:\xuegod\script)
（这样命令窗口运行Python输入Python，运行 Python） 注意：我们选择64位安装包,Python的安装目录中不要有中文.   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/20190624223854python_官网.png)  
第一步  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/20190624223924python_version.png) 
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/20190624223951python_download.png)   
第二步：可以install now，或者是自定义（推荐大家都自定义安装）
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190624224307_install_1.png)
第三步：
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190624224326_install_2.png)
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190624224340_install_3.png)  
安装完成   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190624224355_install_4.png)
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190624224410_install_5.png)
### Python环境变量配置
配置环境变量   
    	-->右键点击我的电脑   
    	-->点击属性   
		-->点击高级系统设置   
		-->点击环境变量   
		-->在系统变量里寻找path（没有新建）   
		-->有path的点击添加   
		-->将你 Python 安装目录(D:\xuegod)以及 Python 中 scripts 的文件路径(D:\xuegod\Scripts) 添加到path中。   
   	恭喜你整个Python已经安装成功  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625102449_python_path1.png)
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625102508_python_path2.png)
### Python安装目录介绍
#### 安装目录介绍   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625102524_python_menu.png)
DLLS: Python的动态链接库，跟编译器有关，和Python编程关系不大    
Doc: Python 的参考书，有很多实例   
Include: Python 编译器的C语言头文件源码   
Lib: 这个库很重要，是Python的标准库，你扩充的库都安装在这里面。   
Libs： Python的内置库，语法存在的地方   
Scripts: 项目用到的各种脚本   
Tcl：包含Python默认内置的GUI工具Tkiner   
Tools目录：Python 提供的一些工具   
Tcl: 桌面编程包   
Python目录 lib 和libs有什么区别？   
Lib是Python的标准库， 我们安装的第三方模块都在这里面， libs是Python的内置库，下载Python 的时候自带的。所以我们不要把API（应用程序接口）放到libs中，要放到lib中。   
#### Python脚本结构  
.py 文件     
以 .py 作扩展名的文件是 Python 源代码文件，由 Python.exe 解释，可在控制台下运行。当然， 也可用文本编辑器进行修改。  
.pyc 文件   
以 .pyc 作扩展名的文件是 Python 编译文件。.pyc 文件是不能用文本编辑器进行编辑的，其优点 是 .pyc 文件的执行速度要远快于 .py 文件。至于为什么要有 .pyc 文件，这个需求太明显了，因为 .py 文件是可直接看到源码的，若是软件开发商的话，不可能把源码泄漏出去？所以，就需编译成 .pyc 后再 发布。   
.pyw 文件     
.pyc 文件执行时，桌面会出现类似 CMD 命令的黑色 shell 窗口，十分难看，于是 .pyw 文件就 应运而生了。
.pyw 文件与 .pyc 文件的执行，本质上并没什么区别，只是 .pyw 文件执行的时候不会出 现类似 CMD 命令的黑色 shell 窗口。.pyw 文件格式主要是设计用来运行纯 GUI 图形用户界面程序 的。 纯 GUI 图形用户界面程序的用户不需要看到类似 CMD 命令的黑色 shell 控制台窗口。.pyw 文 件运行时，所有 stdout、stderr 输出无效，所有原 stdin 的读取只会得到 EOF。 值得一提的是，开发纯 GUI 图形用户界面程序时，可暂时把 .pyw 改成 .py，以便运行时调出控制台窗 口，看到所有错误信息，方便修改、调试。    
.pyo 文件    
.pyo 文件是优化编译后的程序。“Python-O 源文件”即可将源程序编译为 .pyo 文件。同样， .pyo 文件也是不能用文本编辑器进行编辑的。    
.pyd 文件   
.pyd 文件并不是用 Python 编写成的， .pyd 文件一般是其他语言编写的 Python 扩展模块。 .pyd 文件是用 D 语言按照一定格式编写，并处理成二进制的文件。    
窗用 Python.exe 运行 .py ，用 Pythonw.exe 运行 .pyw 。    
这纯粹是因为安装视窗版 Python 时，扩展名 .py 自动被登记为用 Python.exe 运行的文件， 而 .pyw 则被登记为用 Pythonw.exe 运行。   
.py 和 .pyw 之间的“其它差别”全都是 Python.exe 和 Pythonw.exe 之间的差别。 跟 Python.exe 比较起来，Pythonw.exe 有以下的不同：    
(1）执行时不会弹出控制台窗口（也叫 DOS 窗口）    
(2）所有向原有的 stdout 和 stderr 的输出都无效    
(3）所有从原有的 stdin 的读取都只会得到 EOF .pyw 格式是被设计来运行开发完成的纯图形界面程序的。 纯图形界面程序的用户不需要看到控制台窗口。      
#### Python成熟的编译器   
Sublime   
Pycharm   
IPython IDLE Python gui (IDLE是Python自带的简单的集成开发环境)      
我们主要使用pycharm，PyCharm是一种Python IDE，带有一整套可以帮助用户在使用 Python 语言开发时提高其效率的工具，比如调试、语法高亮、Project管理、代码跳转、智能提示、自动完成、 单元测试、版本控制。   
此外，该IDE提供了一些高级功能，以用于支持Django框架下的专业Web开发     
安装包下载地址：https://www.jetbrains.com/pycharm/download/#section=windows 
激活码（有效期至2020年3月）：
  
	MTW881U3Z5-eyJsaWNlbnNlSWQiOiJNVFc4ODFVM1o1IiwibGljZW5zZWVOYW1lIjoiTnNzIEltIiwiYXNzaWduZWVOYW1lIjoiIiwiYXNzaWduZWVFbWFpbCI6IiIsImxpY2Vuc2VSZXN0cmljdGlvbiI6IkZvciBlZHVjYXRpb25hbCB1c2Ugb25seSIsImNoZWNrQ29uY3VycmVudFVzZSI6ZmFsc2UsInByb2R1Y3RzIjpbeyJjb2RlIjoiSUkiLCJwYWlkVXBUbyI6IjIwMTktMTEtMDYifSx7ImNvZGUiOiJBQyIsInBhaWRVcFRvIjoiMjAxOS0xMS0wNiJ9LHsiY29kZSI6IkRQTiIsInBhaWRVcFRvIjoiMjAxOS0xMS0wNiJ9LHsiY29kZSI6IlBTIiwicGFpZFVwVG8iOiIyMDE5LTExLTA2In0seyJjb2RlIjoiR08iLCJwYWlkVXBUbyI6IjIwMTktMTEtMDYifSx7ImNvZGUiOiJETSIsInBhaWRVcFRvIjoiMjAxOS0xMS0wNiJ9LHsiY29kZSI6IkNMIiwicGFpZFVwVG8iOiIyMDE5LTExLTA2In0seyJjb2RlIjoiUlMwIiwicGFpZFVwVG8iOiIyMDE5LTExLTA2In0seyJjb2RlIjoiUkMiLCJwYWlkVXBUbyI6IjIwMTktMTEtMDYifSx7ImNvZGUiOiJSRCIsInBhaWRVcFRvIjoiMjAxOS0xMS0wNiJ9LHsiY29kZSI6IlBDIiwicGFpZFVwVG8iOiIyMDE5LTExLTA2In0seyJjb2RlIjoiUk0iLCJwYWlkVXBUbyI6IjIwMTktMTEtMDYifSx7ImNvZGUiOiJXUyIsInBhaWRVcFRvIjoiMjAxOS0xMS0wNiJ9LHsiY29kZSI6IkRCIiwicGFpZFVwVG8iOiIyMDE5LTExLTA2In0seyJjb2RlIjoiREMiLCJwYWlkVXBUbyI6IjIwMTktMTEtMDYifSx7ImNvZGUiOiJSU1UiLCJwYWlkVXBUbyI6IjIwMTktMTEtMDYifV0sImhhc2giOiIxMDgyODE0Ni8wIiwiZ3JhY2VQZXJpb2REYXlzIjowLCJhdXRvUHJvbG9uZ2F0ZWQiOmZhbHNlLCJpc0F1dG9Qcm9sb25nYXRlZCI6ZmFsc2V9-aKyalfjUfiV5UXfhaMGgOqrMzTYy2rnsmobL47k8tTpR/jvG6HeL3FxxleetI+W+Anw3ZSe8QAMsSxqVS4podwlQgIe7f+3w7zyAT1j8HMVlfl2h96KzygdGpDSbwTbwOkJ6/5TQOPgAP86mkaSiM97KgvkZV/2nXQHRz1yhm+MT+OsioTwxDhd/22sSGq6KuIztZ03UvSciEmyrPdl2ueJw1WuT9YmFjdtTm9G7LuXvCM6eav+BgCRm+wwtUeDfoQqigbp0t6FQgkdQrcjoWvLSB0IUgp/f4qGf254fA7lXskT2VCFdDvi0jgxLyMVct1cKnPdM6fkHnbdSXKYDWw==-MIIElTCCAn2gAwIBAgIBCTANBgkqhkiG9w0BAQsFADAYMRYwFAYDVQQDDA1KZXRQcm9maWxlIENBMB4XDTE4MTEwMTEyMjk0NloXDTIwMTEwMjEyMjk0NlowaDELMAkGA1UEBhMCQ1oxDjAMBgNVBAgMBU51c2xlMQ8wDQYDVQQHDAZQcmFndWUxGTAXBgNVBAoMEEpldEJyYWlucyBzLnIuby4xHTAbBgNVBAMMFHByb2QzeS1mcm9tLTIwMTgxMTAxMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxcQkq+zdxlR2mmRYBPzGbUNdMN6OaXiXzxIWtMEkrJMO/5oUfQJbLLuMSMK0QHFmaI37WShyxZcfRCidwXjot4zmNBKnlyHodDij/78TmVqFl8nOeD5+07B8VEaIu7c3E1N+e1doC6wht4I4+IEmtsPAdoaj5WCQVQbrI8KeT8M9VcBIWX7fD0fhexfg3ZRt0xqwMcXGNp3DdJHiO0rCdU+Itv7EmtnSVq9jBG1usMSFvMowR25mju2JcPFp1+I4ZI+FqgR8gyG8oiNDyNEoAbsR3lOpI7grUYSvkB/xVy/VoklPCK2h0f0GJxFjnye8NT1PAywoyl7RmiAVRE/EKwIDAQABo4GZMIGWMAkGA1UdEwQCMAAwHQYDVR0OBBYEFGEpG9oZGcfLMGNBkY7SgHiMGgTcMEgGA1UdIwRBMD+AFKOetkhnQhI2Qb1t4Lm0oFKLl/GzoRykGjAYMRYwFAYDVQQDDA1KZXRQcm9maWxlIENBggkA0myxg7KDeeEwEwYDVR0lBAwwCgYIKwYBBQUHAwEwCwYDVR0PBAQDAgWgMA0GCSqGSIb3DQEBCwUAA4ICAQAF8uc+YJOHHwOFcPzmbjcxNDuGoOUIP+2h1R75Lecswb7ru2LWWSUMtXVKQzChLNPn/72W0k+oI056tgiwuG7M49LXp4zQVlQnFmWU1wwGvVhq5R63Rpjx1zjGUhcXgayu7+9zMUW596Lbomsg8qVve6euqsrFicYkIIuUu4zYPndJwfe0YkS5nY72SHnNdbPhEnN8wcB2Kz+OIG0lih3yz5EqFhld03bGp222ZQCIghCTVL6QBNadGsiN/lWLl4JdR3lJkZzlpFdiHijoVRdWeSWqM4y0t23c92HXKrgppoSV18XMxrWVdoSM3nuMHwxGhFyde05OdDtLpCv+jlWf5REAHHA201pAU6bJSZINyHDUTB+Beo28rRXSwSh3OUIvYwKNVeoBY+KwOJ7WnuTCUq1meE6GkKc4D/cXmgpOyW/1SmBz3XjVIi/zprZ0zf3qH5mkphtg6ksjKgKjmx1cXfZAAX6wcDBNaCL+Ortep1Dh8xDUbqbBVNBL4jbiL3i3xsfNiyJgaZ5sX7i8tmStEpLbPwvHcByuf59qJhV/bZOl8KqJBETCDJcY6O2aqhTUy+9x93ThKs1GKrRPePrWPluud7ttlgtRveit/pcBrnQcXOl1rHq7ByB8CFAxNotRUYL9IF5n3wJOgkPojMy6jetQA5Ogc8Sm7RG6vg1yow==

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625102549_setup1.png)  
点击next  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625102615_setup2.png)    
自定义文件安装路径  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625102632_setup3.png)  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625102646_setup4.png)   
点击install    
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625102705_setup5.png)   
等待安装好，点击next  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625102720_setup6.png)  
点击finish  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625102732_setup7.png)   
之后就进入激活阶段   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625102751_setup8.png)  
已经发过激活码，配置好后，直接出现以下界面。   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625102813_setup9.png)  
安装好 pycharm 后点开就会出现以上界面点击 Create New project （创建新的 project）   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625102827_setup10.png)  
然后点击create，就会直接创建一个文件夹。然后就可以在里面创建相应的py文件。 配置Python3.exe。运行项目时用Python3 运行  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625102842_setup11.png) 
### Python脚本运行
安装完成，打开命令窗口（键盘：win+R）：输入Python    
注意：使用最高管理员权限打开cmd，否则后面pip安装模块时会出现各种错误。  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625110544_py37_1.png)   
打印Python的第一个程序hello world   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625110841_py37_2.png)
更新pip （在 Windows命令提示符(cmd)中输入以下命令进行 pip的更新:Python-m pip install-U pip）   
更新pip   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625111212_py37_3.png)   
安装cmder   
上面的cmd之后，为了更好的让大家使用cmd中的操作，咱们在这里引用一个新的软件cmder， 是一个比cmd更加强大的应用软件，其命令和linux命令相同但比cmd更加强大。  
 
趣味实战： 

    print('\n'.join([''.join([('Love'[(x-y)%len('Love')]if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625112301_love.png)
### 实战：解决windows下python多版本冲突问题   
可能有很多人有疑惑，后期在工作当中我们不同的项目会指定不同的python版本，如果同一台机器 上我们安装不同的版本（如下图所示），我们该如何操作不同版本的python呢？  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625112327_python_version_many.png)  
上面的 图片中我们很明显了解到我的电脑里，会有 3 个版本的 python，启动了 3 个版本 python 并没有产生冲突，我是如何解决这个问题的？   
解决： python 解释器重命名   
如下图所示   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625112400_many_1.png)    
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625112415_many2.png) 
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625112430_many3.png)   
现在我们的电脑多版本共存，也就是这三者之间并不冲突，并行关系，但是pip的命令也是一样的， 我们需要解决利用pip来安装到不同的python版本中。   
解决方案：利用脚本安装   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625113110_django_1.png)   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625113132_digango_2.png)  
下载软件百度链接： https://pan.baidu.com/s/1vItLQblghxHUnF_oRcyXQA 密码：3ewm 

## Python数字，字符串
### python变量使用 
#### 变量    
在程序中，有时我们需要对2个数据进行求和，那么该怎样做呢？   
大家类比一下现实生活中，比如去超市买东西，往往咱们需要一个菜篮子，用来进行存储物品，等到 所有的物品都购买完成后，在收银台进行结账即可。  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625144739_第二章_1.png)   
如果在程序中，需要把2个数据，或者多个数据进行求和的话，那么就需要把这些数据先存储起来， 然后把它们累加起来即可，变量就是用来存东西的。   
如果在程序中，需要把2个数据，或者多个数据进行求和的话，那么就需要把这些数据先存储起来， 然后把它们累加起来即可，变量就是用来存东西的。    
在Python中，存储一个数据，需要一个叫做变量的东西，如下示例: 
 
	num1 = 100 #num1就是一个变量，就好比一个小菜篮子。   
	num2 = 87 #num2也是一个变量  
	result= num1+num2#把num1和num2这两个"菜篮子"中的数据进行累加，然后放到 result 变量中。   

说明:  
所谓变量，可以理解为菜篮子，如果需要存储多个数据，最简单的方式是有多个变量； 程序就是用来处理数据的，而变量就是用来存储数据的；   
#### 变量的类型   
生活中的“类型”的例子:   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625145310_第二章_2.png)  
程序中:  
为了更充分的利用内存空间以及更有效率的管理内存，变量是有不同的类型的，如下所示:  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625145334_第二章_3.png)  
怎样知道一个变量的类型呢？   
在python中，只要定义了一个变量，而且它有数据，那么它的类型就已经确定了，不需要咱们开发 者主动的去说明它的类型，系统会自动辨别。   
可以使用type(变量的名字)，来查看变量的类型。以上知识让我们知道了，什么是变量，变量的类型 是什么？接下来让我们学习，变量的起名，以及标识符相关规范。   
#### 标示符和关键字    
标示符   
什么是标示符，看下图:  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625145357_第二章_4.png)   
火星文：挖掘机技术哪家强，中国山东找蓝翔  
标示符是自己定义的，直指程序员的本心，就是开发人员在程序中自定义的一些符号和名称，如变量 名 、函数名等  
标示符的命名规则   
标示符由字母、下划线和数字组成，且数字不能开头。   
思考：下面的标示符哪些是正确的，哪些不正确为什么   

	fromNo12  
	from#12 #错误   
	my_Boolean  
	my-Boolean #错误  
	Obj2  
	2ndObj #错误   
	myInt  
	test1  
	Mike2jack  
	My_tExt   
	_test  
	test!32 #错误   
	haha(da)tt #错误   
	int #错误   
	jack_rose   
	jack&rose #错误  
	GUI  
	G.U.I #错误   

python中的标识符是区分大小写的  ：
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625154609_第二章_13.png)   
#### 命名规则和方法   
见名知意：   
起一个有意义的名字，尽量做到看一眼就知道是什么意思(提高代码可读性) 。   
比如: 名字 就定义为 name , 定义学生 用 student。   
驼峰命名法：  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625145432_第二章_6.png)   
小驼峰式命名法（lower camel case）： 
第一个单词以小写字母开始；第二个单词的首字母大写， 例如：  

	myName、aDog   

大驼峰式命名法（uppercamelcase）： 
每一个单字的首字母都采用大写字母，例如：  
 
	FirstName、 LastName    

不过在程序员中还有一种命名法比较流行，就是用下划线“_”来连接所有的单词，比如send_buf   
Python推荐就是用下划线“_”来连接所有的单词。   
注意：一定要注意关键字命名。   
查看关键字：   

	import keyword  
	keyword.kwlist  
	['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']   

上面咱们学习了命名，接下来学习变量的赋值。     
#### 变量赋值的三种方式   
传统赋值   

	name = “xuegod"  

链式赋值   

	name = user = “xuegod”  
 
序列解包赋值   

	name,age = “xuegod”，10   

注意：两边的变量和常量要对等。  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625145501_第二章_7.png)   
#### python 虚拟机（面试题）
1.垃圾回收机制   
当一个常量被生成，会占用一份内存，这时候如果有变量指向该常量，那么该常量的引用计数为1， python 虚拟机规定，当一个常量的引用计数为0，也就是没有变量指向的时候，该常量占用的内存会被 回收。   
例如： 

	name = user = ‘xuegod’  
 
就是变量name，变量user 指向常量‘xuegod’这个内存  
如何查看一个变量的id呢？  
内置函数id（）  
Id(name) 和 id（user）对比，你会惊讶的发现指向的 id竟然相同，那么就说明有两个指针指向 ‘xuegod’这个内存。   
例子：  

	del(name) 删除了指针name   
	del(user) 删除了指针user 
 
我们再来访问，name和user就会发现如下图：  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625145533第二章_8.png)   
也就是指向‘xuegod’的内存的所有指针都已经被删除了，引用计数 0   
2.python是强类型的动态脚本语言
强类型：不允许不同类型相加。例如：整形+字符串会报类型错误。   
动态：不使用显示数据类型声明，且确定一个变量的类型是在给它赋值的时候。   
脚本语言：一般是解释性语言，运行代码只需要一个解释器，不需要编辑。  
 
	A = 1  
	A =‘xuegod’  

#### python 输出、输入 
##### Print：输出  
Python2 的输出是print，而python3 的输出直接变成一个函数print（）   
例如：print（”hello,world !”）  

	print(''' へ ／| /＼7 ∠＿/ / │ ／ ／ │ Z ＿,＜ ／ /`ヽ │ ヽ / 〉 Y ` / / ｲ● ､ ● ⊂⊃〈 / () へ | ＼〈 >ｰ ､_ ィ │ ／／ / へ / ﾉ＜| ＼＼ ヽ_ﾉ (_／ │／／ 7 |／ ＞―r￣￣`ｰ―＿ ''')

##### input 输入   
1.python2 版本   
在Python2中，获取键盘输入的数据的方法是采用 raw_input ()和input()两种函数。   
看如下示例:   

	raw_input()  
	raw_input()的小括号中放入的是提示信息，用来在获取数据之前给用户的一个简单提示；   
	raw_input()在从键盘获取了数据以后，会存放到等号左边的变量中；   
	raw_input()会把用户输入的任何值都作为字符串来对待。   
	input()   
	input()函数与raw_input()类似，但其接受的输入必须是表达式；  
	input()接受表达式输入，并把表达式的结果赋值给等号左边的变量；   
	raw_input()输入的都当成字符串（和Python3的input()功能一样） 
	input()输出的是输入的数据类型   

2.python3 版本中  
没有raw_input()函数，只有input()  
并且 python3 中的input与python2中的raw_input()功能一样   
案例：   

	name = input('请输入你的姓名:')   
	python 程序当中 不print 就不会打印   
	print(name)
 
输出结果： 
 
	请输入你的姓名:for   
	for 

### python数字类型
#### Python数字类型介绍    
整型： int型， 例子：1为整型。   
浮点型： float型， 例子：2.1为浮点型。   
长整型： long型， 例子：2L 为长整形，数字后面加 L 就是长整形，理论上长整型的界限为 2147483647   
Long的爱恨情仇：  
因为python2.x版本长整型的不严谨， python 3版本取消了长整型。 在python 2.x版本对MySQL 操作时，导出的整形数可能就是长整型。   
#### python 数字类型转换 
我们可以通过类型函数（type（变量名））查看数字类型   

	print(type(1))   
	print(type(1.0))   

输出：   

	<class 'int'>  
	<class 'float'>  

也可以通过运算改变数字类型： 
  
	print(type(3//2))   
	print(type(3/2))   

输出：  

	<class 'int'>   
	<class 'float'>  
 
#### python 数字类型运算符   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625161944_第二章_14.png)   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625162031_第二章_15.png)   
### python字符串类型  
#### python 字符串类型概述   
字符串定义：   
字符串是一个有序的，不可修改的，以引号包围的序列  
什么是python字符串：双引号或者单引号中的数据，就是字符串   

	>>> a = 100 #数字类型  
	>>> b = 'hello world' #字符串类型  
	 
引号：   
单引号：‘ ’   
双引号： “ ”  
三单引号：’’’(多用于代码的注释)   
三双引号：”””(多用于代码的注释)   
单引号和双引号区别？   
都是字符串的标准格式，只是为了区分英语中的一些语义 
  
	print("for's name is for")  
 
三引号：字符串内容可换行（多用于注释）。 
 
	print(''' 1 2 3 ''') 

'''我是多行注释，可以写很多很多行的功能说明  
 
这就是我牛X之处   
哈哈哈'''  
注释：  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625145655_第二章_9.png)   
字符串存储的另外一种方式： 
  
	>>> a = 'for'   
	>>> b = ' is'   
	>>> c = ' cool'   
	>>> d = a+b+c    
	>>> d  
	'for is cool'   
	字符串当中的特殊字符：  
	特殊字符就是在字符串当中起到特殊含义的字符。  
	“\” 转义符 将字符串当中的具有特殊含义的字符的特殊含义取消掉和续行；   
	“\n”换行；   
	“\t”水平制表符，tab键。   

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625163124_第二章_16.png)   
（\a的时候win会颤抖下，发出不明觉厉的声响）   
字符串格式化操作：   
在字符串当中以指定的格式符号进行占位，然后我们将指定的数据传入字符串   

	%s 字符串占位符 
	%d 数字占位符 
	%f 浮点型数字占位符 
	%.2f 控制浮点型数字占位符
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625145723_第二章_10.png)   
（对于学渣的我来说，知道分数和不知道分数同样纠结），当然只要我足够快乐，父母的巴掌就打不到我。   

打印字符串 
  
	print('My name is %s'%('for'))
	
打印整数 
	
	print('I am %d years old'%(25)) 
	
打印浮点数 

	print('His height is %f m'%(1.70)) 
	
打印浮点数（保留两位小数） 

	print('His height is %.2f'%(1.70)) 
	
运行结果如下： 

	My name is for I am 25 years old His height is 1.700000 m His height is 1.70   

### python字符串的索引(index)  
   
超市储物柜：  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625145818_第二章_11.png)   
在python当中所有有序的序列都是由索引概念的，它们的区别在于序列是否可以被修改；索引在我 们初学的时候我们可以理解为字符串的下标；   
字符串里的每一个个体都被称作字符也是该字符串的一个元素，每一个元素都对应一个索引值（下标） ； 在这里可以用len() 方法看一个序列的长度 索引的用法，取单个元素时，使用字符串[索引值] 索引值为对应元素的索引号；
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625145841_第二章_12.png)   
比如字符串‘while’，可以按照下图理解其下标概念，索引号从0开始；     
字符串截取：字符串[start:end]，得到对应索引范围的元素，该范围包含起始端，不包含结尾端，默 认截取的方向是从左往右的； 
  
	name = 'while'   
	print(name[1:3])   

步长截取：字符串[start:end:step] 按照step步长进行隔取；  
切片的语法：[起始:结束:步长]   
注意：选取的区间属于左闭右开型，即从"起始"位开始，到"结束"位的前一位结束（不包含结束位本 身)。   
老师是想说 可以理解为包头不包尾  
 
	str_test = 'hello world'   
	print(str_test[0:7:2])   
	'hlow'  

默认取法：字符串[start:end:step] 这三个参数都有默认值、start；默认值为0；end 默认值未字 符串结尾元素；step 默认值为1   
若 step > 0, 则表示从左向右进行切片。 此时，start 必须小于end才有结果，否则为空。   
若 step < 0, 还是表示从左到右只不过反过来切片，此时，start 必须大于 end 才有结果，否则为空。 
  
	str_test = 'hello world'   
	print(str_test[0:7])   
	print(str_test[:7])    
	print(str_test[2:])    
	print(str_test[:])   
	print(str_test[::2])   

反取：字符串[负数]，从右往左取(从后面取)   
 
	print(str_test[::-1])    
	print(str_test[::-2])   
	print(str_test[1:9:-1])   
	print(str_test[9:1:-2]) 
  
### python字符串的方法    
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625164355_第二章_17.png)   
index [ˈɪndeks]:索引  
 
	str_test = 'hello world'     
	print(str_test.count('l'))   
	print(str_test.find('world'))   
	print(str_test.rfind('world'))   
	print(str_test.index('o'))   
	print(str_test.rindex('o'))    

运行结果如下： 
  
	3   
	6   
	6    
	4  
	7    
 
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625164631第二章_18.png)   
partition [pɑːˈtɪʃn]：分区    
split [splɪt]:分割 replace [rɪˈpleɪs]：代替   

	str_test = 'hello world'   
	print(str_test.partition('o'))     
	print(str_test.rpartition('o'))  
	my_str = 'hello\n world \n python\n'   
	print(my_str)    
	print(my_str.splitlines())   
	print(str_test.replace('h','w'))  
 
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625164653_第二章_19.png)     
center[ˈsentə(r)]：中心   
format [ˈfɔːmæt]：格式   
strip[strɪp]:除去
   
	str_test = 'for'   
	print(str_test.center(10))   

center这个里面可以加入两个参数 

	print(str_test.center(10,'x')) 

运行结果如下：
 
	for xxxforxxxx ljust这个里面可以加入两个参数   
	print(str_test.ljust(10))   
	print(str_test.ljust(10,'x'))   
	print(str_test.rjust(10,'x'))  
 
运行结果如下：
 
	for forxxxxxxx xxxxxxxfor   
	print(str_test.zfill(10))
   
运行结果如下：   

	0000000for   
 
注意：如果传入的大小小于字符串的长度，字符串不变。  
  
	str_test = ' for '    
	print(str_test.strip())    
	'for' print(str_test.rstrip())   
	' for' print(str_test.lstrip())    
	'for ' python = "{0} is {1}" 
	print(python.format('for','cool'))   

运行结果如下：  
  
	'for is cool' 字符串的变形    

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625164713_第二章_20.png)  
 swap [swɒp]：转换   
capitalize [ˈkæpɪtəlaɪz]：首字母大写 
  
	print('hello'.upper())   

将 字 符 串 当 中 所 有 的 字 母 转 换 为 小 写 

	print('HELLO'.lower())   

将 字 符 串 当 中 所 有 的 字 母 大 小 写 互 换 

	print('Hello'.swapcase())   

将 字 串 符 当 中 的 单 词 首 字 母 大 写 ， 单 词 以 非 字 母 划 分 

	print('hello,world'.title())
 
	
只 有 字 符 串 的 首 字 母 大 写 

	print('hello world'.capitalize()) 

	
把 字 符 串 中 的 t a b 符 号 ( ' \ t ' ) 转 为 空 格 ， t a b 符 号 ( ' \ t ' ) 默 认 的 空 格 数 是 8 print('for \t is \t cool'.expandtabs(10))  

	print('for \t is \t cool'.expandtabs()) print('for \t is \t cool'.expandtabs(4)) 
	
运行结果如下： 

	HELLO hello hELLO Hello,World Hello world for is cool for is cool for is cool  
 
字符串的判断  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625164912_第二章_21.png)  
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625170029_第二章_23.png)    
 
### python 字符串的编码     

encode是编码   
decode是解码   
编码方式对比：   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/微信截图_20190625112145_第二章_24.png)     
python字符串是一种数据类型，但是字符串比较特殊，它有一个编码的问题。  
因为计算机只能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理。最早的计算机在 设计时采用 8个比特（bit）作为一个字节（byte），所以，一个字节能表示的最大的整数就是255（二 进制11111111=十进制255），如果要表示更大的整数，就必须用更多的字节。比如两个字节可以表示 的最大整数是65535，4个字节可以表示的最大整数是4294967295。    
由于计算机是英语国家发明的，最早只有127个字母被编码到计算机里，也就是大小写英文字母、数 字和一些符号，这个编码表被称为ASCII编码，比如大写字母A的编码是65，小写字母a的编码是97。    
但是要处理中文显然一个字节是不够的，至少需要两个字节，而且还不能和ASCII编码冲突，所以， 中国制定了GB2312编码，用来把中文编进去。   
全世界有上百种语言，日本把日文编到Shift_JIS里，韩国把韩文编到Euc-kr里，各国有各国的标准， 就会不可避免地出现冲突，结果就是，在多语言混合的文本中，显示出来会有乱码。   
因此，俗称“万国码”的Unicode应运而生。Unicode把所有语言都统一到一套编码里，这样就不 会再有乱码问题了。   
Unicode标准也在不断发展，但最常用的是用两个字节表示一个字符（如果要用到非常偏僻的字符， 就需要4个字节）。现代操作系统和大多数编程语言都直接支持Unicode  
现在，捋一捋 ASCII编码和Unicode编码的区别：ASCII 编码是1个字节，而Unicode编码通常是 2个字节。   
字母A用ASCII编码是十进制的65，二进制的01000001；   
字符0用ASCII编码是十进制的48，二进制的00110000，注意字符'0'和整数0是不同的；   
汉字中已经超出了 ASCII 编码的范围，用 Unicode 编码是十进制的 20013，二进制的 01001110 00101101  
如果把ASCII 编码的A用 Unicode编码，只需要在前面补 0就可以，因此，A的Unicode 编码是 00000000 01000001。   
新的问题又出现了：如果统一成Unicode编码，乱码问题从此消失了。但是，如果你写的文本基本上 全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。 所以，本着节约的精神，又出现了把 Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把 一个 Unicode字符根据不同的数字大小编码成 1-6个字节，常用的英文字母被编码成 1个字节，汉字通 常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用 UTF-8编码就能节省空间：   
UTF-8编码有一个额外的好处，就是ASCII 编码实际上可以被看成是UTF-8 编码的一部分，所以， 大量只支持 ASCII 编码的历史遗留软件可以在 UTF-8 编码下继续工作。搞清楚了 ASCII、Unicode 和 UTF-8的关系，我们就可以总结一下现在计算机系统通用的字符编码工作方式：   
在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8 编码。用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后， 保存的时候再把Unicode转换为UTF-8保存到文件。浏览网页的时候，服务器会把动态生成的Unicode 内容转换为UTF-8再传输到浏览器    
由于python 的诞生比 Unicode标准发布的时间还要早，所以最早的Python只支持ASCII 编码， 普通的字符串’ABC’在Python内部都是ASCII编码的。Python提供了ord()和chr()函数，可以把字 母和对应的数字相互转换，len()函数可以查字符串的长度：  
  
	u = '学神'  
	print(str1)  
	str2 = u.encode('utf-8')   
	print(str2)   
	u1 = str1.decode('gbk')   
	print(u1)   
	u2 = str2.decode('utf-8')   
	print(u2)   
	运行结果如下：   
	b'\xd1\xa7\xc9\xf1'   
	b'\xe5\xad\xa6\xe7\xa5\x9e'   
	学神  
	学神  

在python中解决编码问题  
由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时， 就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我 们通常在文件开头写上这两行（python3默认为utf-8 所以没必要加文档头）：    
1、# -*- coding: utf-8 -*   
2、#coding=utf-8   


## 列表，元祖，字典，组合
### Python 列表
#### Python 列表的定义
定义一个空列表
注意：列表里面的数据类型是可变的，甚至可以嵌套一个列表
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/python_3_1.png)    
Python 列表操作   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/python_3_2.png) 
### Python 元组
#### 元组的定义   
元组是有序的，不可修改的，以逗号分割的，以小括号包围的序列，可以通过()和 tuple()函数定义。
不能修改，只有在定义的一瞬间可以修改。   
元组的优点:    
由于元组不可变，所以遍历元组比列表要快（较小的性能提升）。    
由于元组不可变，所以元组中的数据被‘写保护’,这也可以联想到，一些软件比较重要的数据都是用元组存储的。    
创建元组：    

	>>> num = (11,22,33,'aa')    
	>>> num   
	(11, 22, 33, 'aa')   
	>>> num = 1,2,3,'a'   
	>>> num   
	(1, 2, 3, 'a')   
	>>> 1,2,3   
	(1, 2, 3)   
	>>> type(num)  
	<class 'tuple'>   

元组一个逗号的秘密  

	>>> num = (2)  
	>>> num    
	>>> type(num)   
	<class 'int'>  
	>>> num = (1,)   
	>>> num   
	(1,)  
	>>> (1+1)*2   
	4  

为什么会出现这种情况呢？，Python 中的（）同样也表示数学运算的一个基本符号，比如（1+1）
*2，所以这就和元组的这个小括号产生了歧义，当元组中只有一个元素，而又没有逗号的时候，它会把这
元素运算出来，这个小括号会被 Python 解释器识别为一个运算符号，所以得到的是那个元素本身的数据
类型   
访问元组  

	>>> num  
	(1, 2, 3, 'a')
	>>> num[1]
	2
	>>> num[2]
	3

修改元组   
说明：Python 中不允许修改元组的数据，包括不能删除其中的元素。
元组是不可变的，也就是说，元组中的元素在被赋值后不能改变。但是，如果元素本身是一个可变数
据类型的列表，那么其嵌套项可以被改变   

	>>> num = (1,'a',[1,2])
	>>> num[2].append(3)
	>>> num
	(1, 'a', [1, 2, 3])
	>>>

元组不能修改   

	>>> num[0] = 2
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	TypeError: 'tuple' object does not support item assignment
	>>>
	
tuple 函数   
tuple 函数的功能与 list 函数基本上一样的，以一个序列作为参数并把它转换为元组，如果参数是元
组，那么该参数就会被原样返回   
列表转元组   

	>>> num = ['诺手','ez','雪人','寒冰']
	>>> num2 = tuple(num)
	>>> num2
	('诺手', 'ez', '雪人', '寒冰')

字符串转元组  

	>>> str1 = 'hello' >>> str1 = tuple(str1)
	>>> str1
	('h', 'e', 'l', 'l', 'o')
	>>> num2
	('诺手', 'ez', '雪人', '寒冰')

元组转元组 
 
	>>> num3 = tuple(num2)
	>>> num3
	('诺手', 'ez', '雪人', '寒冰')
	str1 = 'hello' >>>a = tuple(str1)
	>>>a
	('h', 'e', 'l', 'l', 'o')
	>>>''.join(a)
	'hello'
	>>>a = (1,2,3)
	>>>''.join([str(i) for i in a])
	
嵌套元组访问的示例

	>>> tup1 = (('诺手','寒冰'),('雪人','猴子'),('孙尚香','吃鸡'))
	>>> tup1[0]
	('诺手', '寒冰')
	>>> tup1[1]
	('雪人', '猴子')
	>>> tup1[2]
	('孙尚香', '吃鸡')
	>>> tup1[0][1]
	'寒冰' 
	>>> tup1[1][1]
	'猴子' 
	>>>
	
元组的索引和字符串以及列表完全一致。    
 
	>>> tup2 = (0,1,2,3,4,5,6)
	>>>
	>>> tup2
	(0, 1, 2, 3, 4, 5, 6)
	>>>
	>>> tup2[0]
	0
	>>> tup2[1]
	1
	>>> tup2[-1]
	6
	>>> tup2[0:4]
	(0, 1, 2, 3)
	>>> tup2[0:]
	(0, 1, 2, 3, 4, 5, 6)
	>>> tup2[0:4:2]
	(0, 2)
	>>> tup2[::2]
	(0, 2, 4, 6)
	>>> tup2[::-1]
	(6, 5, 4, 3, 2, 1, 0)
	>>> tup2[1:4:-1]
	()
	>>> tup2[4:1:-1]
	(4, 3, 2)

Python 元组的方法   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/python_3,3.png) 

	>>> tup2
	(0, 1, 2, 3, 4, 5, 6)
	>>> tup2.index(0)
	0
	>>> tup2.index(1)
	1
	>>> tup2.index(2)
	2
	>>> tup2.count(2)
	1
	>>> tup2.count(4)
	1
	>>> tup2.count(10)
	0
	>>>
	
python 元组与列表的区别   
1、元组和列表都是有序的，元组不可修改，列表可修改。   
2、元组和列表的元素可以是任何类型   
3、元组的元素长度可以任意。   
### Python 字典
字典的定义   
一个无序的，可以修改的，元素呈键值对的形式（这种结构类型通常也被称为映射，或者叫关
联数组，也有叫哈希表的），以逗号分割的，以大括号包围的数据类型；   
生活中的字典特点：前几页相当于目录结构，通过偏旁部首可以查找内容。      

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/python_3_4.png)    

Python 字典特性讲解   
字典和列表一样，也能够存储多个数据，字典中的值并没有特殊顺序。  
列表中找某个元素时，是根据下标进行的，如果下标很多，查找数据不方便。当索引不好用时，使用
字典，是你最好的选择  
字典的每个元素由 2 部分组成，键:值。例如 'name':'班长' ,'name'为键，'班长'为值，字典由键值组成   
字典是 Python 基础数据类型当中唯一一个映射关系的数据类型  
由于字典无序，所以我们定义字典和字典生成之后的元素的顺序是不同的  
格式：  

	info = {'name':'for','addr':'beijing','age':18}   

获取字典中的元素  
利用键名   

	>>> info = {'name':'for','addr':'beijing','age':18}
	>>> type(info)
	<class 'dict'>
	>>> info['name']
	'for' 
	>>> info['age']
	
get 方法

	>>> info.get('name')
	'for'

注意：get 方法如果没有找到相应的值，就会输出 None，后面也可以带默认的值，工作中常用  
添加和修改  

	>>> info = {'name':'for','addr':'beijing','age':18}
	>>> info['like'] = '玛利' >>> info
	{'name': 'for', 'like': '玛利', 'age': 18, 'addr': 'beijing'}

更改  

	>>> info['like'] = '武藤兰' >>> info
	{'name': 'for', 'like': '武藤兰', 'age': 18, 'addr': 'beijing'}
	>>>
	
删除  

	>>> info
	{'name': 'for', 'like': '武藤兰', 'age': 18, 'addr': 'beijing'}
	>>> del info['like']
	>>> info
	{'name': 'for', 'age': 18, 'addr': 'beijing'}
	>>>
Python 字典的特点  	
因为字典是无序的，所以字典没有索引值；   
因为字典没有索引值，所以字典以键取值，(字典的键相当于列表的索引)；  
因为字典以键取值，所以字典的键唯一且不可修改；  
因为字典的键不可修改，所以列表和字典等可变类型的数据不可以给字典做键  
Python 字典的常见操作    
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/python_3_5.png) 


	>>> info = {'name': 'for', 'age': 18, 'addr': 'beijing'}
	
返回一个包含字典所有 key 的列表

	>>> info.keys()
	dict_keys(['name', 'age', 'addr'])
	>>> info['like'] = '吉泽' >>> info
	{'name': 'for', 'like': '吉泽', 'age': 18, 'addr': 'beijing'}
	>>> info.keys()
	dict_keys(['name', 'like', 'age', 'addr'])

返回一个包含字典所有 vaule 的列表

	>>> info.values()
	dict_values(['for', '吉泽', 18, 'beijing'])

以键取值，如果指定键不存在，默认返回 None,可以指定返回内容

	>>> info.get('like')
	'吉泽' 

设置默认，如果键存在，返回值，如果键不存在，创造键，值默认为 None，值也可以自定义

	setdefault(key,default=None)
	>>> info.setdefault('play')
	>>> info
	{'play': None, 'name': 'for', 'like': '吉泽', 'age': 18, 'addr': 'beijing'}
	>>> info['play'] = '捆绑' >>> info
	{'play': '捆绑', 'name': 'for', 'like': '吉泽', 'age': 18, 'addr': 'beijing'}

以字典格式更新指定键的内容，如果键不存在，创建键和值

	>>> info.update({'cosplay':'ez'})
	>>> info
	{'cosplay': 'ez', 'name': 'for', 'age': 18, 'addr': 'beijing', 'like': '吉泽', 'play': '捆绑'}

返回字典键值呈元组形式的格式

	>>> info.items()
	dict_items([('cosplay', 'ez'), ('name', 'for'), ('age', 18), ('addr', 'beijing'), ('like', '吉泽'), ('play', '捆绑')])

测量字典，键值对的个数（整体）

	>>> len(info)
	6

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/python_3_6.png)   

弹出，返回并删除指定键对应的值

	>>> info = {'cosplay': 'ez', 'name': 'for', 'age': 18, 'addr': 'beijing', 'like': '吉泽', 'play': '捆
	绑'}
	>>> info.pop('age')
	18

随机弹出一个键值元组，这里随机的原因是因为字典无序

	>>> info = {'cosplay': 'ez', 'name': 'for', 'addr': 'beijing', 'like': '吉泽', 'play': '捆绑'}
	>>> info.popitem()
	('cosplay', 'ez')

清空字典

	>>> info1 = {'name':'for','age':10}
	>>> info1
	{'name': 'for', 'age': 10}
	>>> info1.clear()
	>>> info1
	{}
	>>> 'name' in info
	True
	>>> 'namea' in info
	False

通过 for ... in ...:的语法结构，我们可以遍历字符串、列表、元组、字典等数据结构。

	>>> for i in info:
	... print(i)
	... name
	addr
	like
	play
	>>> for i in info.values():
	... print(i)
	...

判断指定的键是否在字典当中

	for
	beijing
	吉泽
	捆绑
	这个了解下  

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/python_3_7.png)  
### Python 集合
集合定义  
集合是一组无序不重复的元素集合。  
集合与之前列表、元组类似，可以存储多个数据，但是这些数据是不重复的。  
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因
为 { } 是用来创建一个空字典。   
创建一个集合  

	>>> s1 = {1,2,3,4}
	>>> type(s)
	<class 'set'>

元组里面没有相同的元素（去重）  

	>>> num = {1,2,3,4,5,6,6}
	>>> num
	{1, 2, 3, 4, 5, 6}
	>>>

集合对象还支持交集(intersection),差集(difference)、并集和对称差集(sysmmetric_difference)  
交集(&)： 两个集合的公共部分  
并集(|): 两者集合合并，没有重复元素  
差集(-)： 只有前项有的元素，不存在后项中的元素。  
对称差集(^)：只在 a 或 b 中，但是不会同时出现在二者中  

	>>> a = set('1234')
	>>> b = set('3456')
	
交集：&两个集合的公共部分  

	>>> a&b
	{'4', '3'}

并集：| 两者集合合并，没有重复元素  

	>>> a|b  
	{'1', '6', '5', '2', '4', '3'}

差集：-只有前项有的元素，不存在后项中的元素。  

	>>> a-b
	{'1', '2'}

对称差集(^)：只存在 a 或者 b 中，但是不会同时出现在二者中 
  
	>>> a^b
	{'1', '6', '5', '2'}
	>>>

set、list、tuple 之间可以相互转换   

字符串转列表  

	>>> b = list(a)
	>>> b
	['h', 'e', 'l', 'l', 'o']

字符串转元组  

	>>> c = tuple(a)
	>>> c
	('h', 'e', 'l', 'l', 'o')

字符串转集合 
 
	>>> d = set(a)
	>>> d
	{'l', 'e', 'o', 'h'}
	>>> a
	'hello' >>> b
	['h', 'e', 'l', 'l', 'o']
	>>> c
	('h', 'e', 'l', 'l', 'o')
	>>> d
	{'l', 'e', 'o', 'h'}
	>>>
	
集合操作  

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/python_3_8.png)  
 
	s.add(x)
	>>> thisset = set(("Google", "Runoob", "Taobao"))
	>>> thisset.add("Facebook")
	>>> print(thisset)
	{'Google', 'Taobao', 'Runoob', 'Facebook'}

还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：

	s.update(x)

注：x 可以是多个值，用逗号分隔开

	>>> thisset = set(("Google", "Runoob", "Taobao"))
	>>> thisset.update({1,3})
	>>> print(thisset)
	{3, 'Google', 'Taobao', 'Runoob', 1}
	>>>
	>>> thisset.update([1,4],[5,6])
	>>> print(thisset)
	{'Taobao', 1, 3, 4, 5, 6, 'Google', 'Runoob'}

移除元素
s.remove(x) 删除集合中的指定元素，当指定的元素不存在的时候会报错

	>>> thisset = set(("Google", "Runoob", "Taobao"))
	>>> thisset.remove("Taobao")
	>>> print(thisset)
	{'Google', 'Runoob'}
	>>>
	>>> thisset.remove("Facebook")
	Traceback (most recent call last):
	File "<pyshell#92>", line 1, in <module>
	thisset.remove("Facebook")
	KeyError: 'Facebook' >>>

s.discard(x) 也是删除集合中的指定元素，且如果元素不存在的时候，不会发生错误

	>>> thisset = set(("Google", "Runoob", "Taobao"))
	>>> thisset.discard("Facebook")
	>>> print(thisset)
	{'Google', 'Taobao', 'Runoob'}
	>>> thisset.discard("Google")
	>>> print(thisset)
	{'Taobao', 'Runoob'}

s.pop() 随机删除集合中的一个元素

	>>> thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
	>>> thisset.pop()
	'Google' >>> print(thisset)
	{'Taobao', 'Runoob', 'Facebook'}

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/python_3_9.png)   
![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/python_3_10.png)     
欢迎阅读此文章，我目前只学习到此处。后续更新。。。。。。。。
## python的运算和流程控制
### Python 运算(布尔值，自增，比较，逻辑)

### Python 流程控制介绍

### Python 

### Python

## python函数编程

## python函数装饰器

## python流程控制

## Python 图形化

## Python socket 网络编程

## Python 进程

## python 多线程

## Python 协程

## Python 开发服务器

## Python 匹配

