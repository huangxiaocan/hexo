---
title: Java面试题总结
tags:
  - Java面试题
categories: Java面试题
description: Java面试题总结
abbrlink: f61b
---

## 开场白

简单的介绍一下自己的工作经历与职责，在校或者工作中主要的工作内容，
主要负责的内容；（你的信息一清二白的写在简历上，能答出来的最好写在上面，模棱两可不是很清楚的最好不要写，否则会被问的很尴尬）  
介绍下自己最满意的，有技术亮点的项目或平台，重点介绍下自己负责那部分的技术细节；（主要对自己做过的事情是否有清晰的描述）  

## Java基础

什么是字符串常量池？

	https://www.cnblogs.com/childhooding/p/4642445.html

String为什么是不可变的？

	jdk1.6成员变量有4个，jdk1.7成员变量有2个，value是字符数组，用final定义的，所以不可变
	通过反射可以破坏 String 的不可变性。

	String str = "123";
	System.out.println(str);
	Field field = String.class.getDeclaredField("value");
	field.setAccessible(true);
	char[] value = (char[]) field.get(str);
	value[1] = '3';

String s = new String("xyz");究竟产生了几个对象，从JVM角度谈谈？

	一个是string池中的对象，一个是堆中的对象，并把堆中的对象交给s持有。
		

String拼接字符串效率低，你知道原因吗？

	JAVA编译器会将"+"转换成了StringBuilder，假设内容在一个for循环里面，虽然Java有垃圾回收器，但这个回收器的工作时间是不定的。如果不断产生这样的垃圾，那么仍然会占用大量的资源

你真的了解String的常见API吗？

	length();//计算字符串的长度

	charAt();//截取一个字符
	
	getChars();//截取多个字符
	
	equals();//比较两个字符串
	
	equalsIgnoreCase();//比较两个字符串,忽略大小写
	
	startsWith();//startsWith()方法决定是否以特定字符串开始
	
	endWith();//方法决定是否以特定字符串结束
	
	indexOf();//查找字符或者子串第一次出现的地方。
	
	lastIndexOf();//查找字符或者子串是后一次出现的地方。
	
	substring();//截取字符串
	
	concat();//连接两个字符串
	
	replace();//替换
	
	trim();//去掉起始和结尾的空格
	
	valueOf();//转换为字符串
	
	toLowerCase();//转换为小写
	
	toUpperCase();// 转换为大写


Java中的subString()真的会引起内存泄露么？

	这个bug发生在jdk1.6版本，后续修复了。原因是比如我们有一个1G的字符串a，我们使用substring(0,2)得到了一个只有两个字符的字符串b，如果b的生命周期要长于a或者手动设置a为null，当垃圾回收进行后，a被回收掉，b没有回收掉，那么这1G的内存占用依旧存在，因为b持有这1G大小的字符数组的引用。
	所以推荐的方式是substring中生成的字符串与原字符串共享内容数组，这样避免了每次进行substring重新进行字符数组复制。
	jdk1.7之后substring的实现抛弃了之前的内容字符数组共享的机制，对于子字符串（自身除外）采用了数组复制实现单个字符串持有自己的应该拥有的内容来避免内存泄漏


浅析Java中的final关键字？

	修饰类，修饰方法，修饰变量

浅析Java中的static关键字？

在《Java编程思想》P86页有这样一段话：

	“static方法就是没有this的方法。在static方法内部不能调用非静态方法，反过来是可以的。而且可以在没有创建任何对象的前提下，仅仅通过类本身来调用static方法。这实际上正是static方法的主要用途。”
	被static关键字修饰的方法或者变量不需要依赖于对象来进行访问，只要类被加载了，就可以通过类名去进行访问
	static可以用来修饰类的成员方法、类的成员变量，另外可以编写static代码块来优化程序性能

你对Java中的volatile关键字了解多少？

	在Java内存模型详解中我们曾经介绍过，Java语言为了解决并发编程中存在的原子性、可见性和有序性问题，提供了一系列和并发处理相关的关键字，比如synchronized、volatile、final、concurren包等。在前一篇文章中，我们也介绍了synchronized的用法及原理

	volatile通常被比喻成”轻量级的synchronized“，也是Java并发编程中比较重要的一个关键字。和synchronized不同，volatile是一个变量修饰符，只能用来修饰变量。无法修饰方法及代码块等。

	volatile的用法比较简单，只需要在声明一个可能被多线程同时访问的变量时，使用volatile修饰就可以了。

i++是线程安全的吗？如何解决线程安全性？

	使用AtomicInteger

	熟悉并发的同学一定知道在java中处理并发主要有两种方式：

	1，synchronized关键字，这个大家应当都各种面试和笔试中经常遇到。

	2，volatile修饰符的使用，相信这个修饰符大家平时在项目中使用的也不是很多。

 

	这里重点说一下volatile:

	Volatile修饰的成员变量在每次被线程访问时，都强迫从共享内存重新读取该成员的值，而且，当成员变量值发生变化时，强迫将变化的值重新写入共享内存，这样两个不同的线程在访问同一个共享变量的值时，始终看到的是同一个值。

 

	java语言规范指出：为了获取最佳的运行速度，允许线程保留共享变量的副本，当这个线程进入或者离开同步代码块时，才与共享成员变量进行比对，如果有变化再更新共享成员变量。这样当多个线程同时访问一个共享变量时，可能会存在值不同步的现象。

 

	而volatile这个值的作用就是告诉VM：对于这个成员变量不能保存它的副本，要直接与共享成员变量交互。

 

	建议：当多个线程同时访问一个共享变量时，可以使用volatile，而当访问的变量已在synchronized代码块中时，不必使用。

	缺点：使用volatile将使得VM优化失去作用，导致效率较低，所以要在必要的时候使用。


从字节码角度深度解析 i++ 和 ++i 线程安全性原理？

	在jvm中有这么一个数据结构叫java栈，当线程启动的时候，会分配一块内存当做该线程的栈，每个栈由一系列的栈帧组成。每个栈帧对应一个方法，当线程执行方法时，就是栈帧出栈，入栈的过程。 
	每个栈帧包含三部分数据：本地变量（参数+方法内的变量）、操作数栈和其他数据，本文主要涉及本地变量和操作数栈。 


请谈谈什么是CAS？

	CAS（compare and swap, 比较并交换），是原子操作的一种，可用于在多线程编程中实现不被打断的数据交换操作，从而避免多线程同时改写某一数据时由于执行顺序不确定性以及中断的不可预知性产生的数据不一致问题。
	简单来说，CAS可以保证多线程对数据写操作时数据的一致性。

从源码角度看看ArrayList的实现原理？

	一、ArrayList的基本特点
	快速随机访问
	允许存放多个null元素
	底层是Object数组
	增加元素个数可能很慢(可能需要扩容),删除元素可能很慢(可能需要移动很多元素),改对应索引元素比较快
	二、ArrayList的继承关系
	可以看到继承了AbstractList,此类提供 List 接口的骨干实现，以最大限度地减少实现”随机访问”数据存储（如数组）支持的该接口所需的工作.对于连续的访问数据（如链表），应优先使用 AbstractSequentialList，而不是此类.
	
	实现了List接口,意味着ArrayList元素是有序的,可以重复的,可以有null元素的集合.
	
	实现了RandomAccess接口标识着其支持随机快速访问,实际上,我们查看RandomAccess源码可以看到,其实里面什么都没有定义.因为ArrayList底层是数组,那么随机快速访问是理所当然的,访问速度O(1).
	
	实现了Cloneable接口,标识着可以它可以被复制.注意,ArrayList里面的clone()复制其实是浅复制(不知道此概念的赶快去查资料,这知识点非常重要).
	
	实现了Serializable 标识着集合可被序列化。


手写LinkedList的实现，彻底搞清楚什么是链表？

Java中方法参数的传递规则？

Java中throw和throws的区别是什么？

重载和重写的区别？

手写ArrayList的实现，在笔试中如何过关斩将?

finally语句块你踩过哪些坑？

为什么重写equals方法需同时重写hashCode方法？

equals() 与 == 的区别？

StringBuffer和StringBuilder的区别，从源码角度分析?

你知道HashMap的数据结构吗？

为何HashMap的数组长度一定是2的次幂？

HashMap何时扩容以及它的扩容机制？

HashMap的key一般用字符串,能用其他对象吗？

HashMap的key和value都能为null么?如果key能为null,那么它是怎么样查找值的？

HashMap是线程安全的吗？如何实现线程安全？

从源码角度分析HashSet实现原理？

HashTable与HashMap的实现原理有什么不同？

String方法intern() 你真的会用吗？

什么是自动拆装箱？

String.valueOf和Integer.toString的区别？

三、Java多线程

线程的生命周期包括哪几个阶段？

多线程有几种实现方式？

请谈谈什么是进程，什么是线程？

启动线程是用start()方法还是run()方法？

说说线程安全问题，什么实现线程安全，如何实现线程安全？

sychronized和Lock的区别？

sleep()和wait()的区别？

深入分析ThreadLocal的实现原理？

你看过AbstractQueuedSynchronizer源码阅读吗，请说说实现原理？

谈谈对synchronized的偏向锁、轻量级锁、重量级锁的理解？

通过三种方式实现生产者消费者模式？

JVM层面分析sychronized如何保证线程安全的？

JDK层面分析sychronized如何保证线程安全的？

如何写一个线程安全的单例？

通过AQS实现一个自定义的Lock？

ThreadLocal什么时候会出现OOM的情况？为什么？

为什么wait, notify 和 notifyAll这些方法不在thread类里面？

你真的理解CountDownLatch与CyclicBarrier使用场景吗？

出现死锁，如何排查定位问题？

notify和notifyAll的区别？

线程池启动线程submit和execute有什么不同？

SimpleDateFormat是线程安全的吗？如何解决？

请谈谈ConcurrentHashmap底层实现原理？

使用synchronized修饰静态方法和非静态方法有什么区别？

当一个线程进入一个对象的一个synchronized方法后,其它线程是否可进入此对象的其方法？

线程池的原理，为什么要创建线程池？创建线程池的方式？

创建线程池有哪几个核心参数？ 如何合理配置线程池的大小？

synchronized修饰的静态方法和非静态方法有什么区别？

## Java Web

什么是Servlet，Servlet生命周期方法？

什么Session和Cookie，它们之间有什么联系？

JSP的八个隐含对象有哪些？

JSP的四个域对象的作用范围？

Post和Get请求的区别？

转发和重定向有什么区别？

JSP自定义标签，如何实现循环打印功能？

Http1.0和Http1.1的区别是什么？

拦截器与过滤器的区别？

## JVM面试题

JVM内存区域如何划分？

JVM堆中对象是如何创建的?

JVM对象的结构？

JVM垃圾回收-如何判断对象是否是垃圾对象？

JVM垃圾回收算法有哪些？

JVM垃圾收集器有哪些？

JVM内存是如何分配的？

从一道面试题分析类的加载过程？

JVM双亲委派机制？

JVM可以作为GC Root的对象有哪些？

请写出几段可以导致内存溢出、内存泄漏、栈溢出的代码？

哪些情况会导致Full GC？

频繁GC问题或内存溢出问题，如何定位？

## SQL性能优化

数据库三范式是什么？

数据库的事务、ACID及隔离级别？

不考虑事务的隔离性，容易产生哪三种情况？

数据库连接池原理？

什么是B-Tree？

什么是B+Tree？

MySQL数据库索引结构？

什么是索引？什么条件适合建立索引？什么条件不适合建立索引？

索引失效的原因有哪些？如何优化避免索引失效？

MySQL如何启动慢查询日志？

MySQL如何使用show Profile进行SQL分析？

一条执行慢的SQL如何进行优化，如何通过Explain+SQL分析性能？

什么是行锁、表锁、读锁、写锁，说说它们各自的特性？

什么情况下行锁变表锁？

什么情况下会出现间隙锁？

谈谈你对MySQL的in和exists用法的理解？

MySQL的数据库引擎有哪些，如何确定在项目中要是用的存储引擎？

count(*)、count(列名)和count(1)的区别？

union和union all的区别？

## Spring框架

Spring的IOC和AOP机制？

Spring中Autowired和Resource关键字的区别？

依赖注入的方式有几种，各是什么?

Spring容器对Bean组件是如何管理的？

Spring容器如何创建？

Spring事务分类？

Spring事务的传播特性？

Spring事务的隔离级别？

Spring的通知类型有哪些？

## SpringMVC框架

SpringMVC完整工作流程，熟读源码流程？

SpringMVC如何处理JSON数据？

SpringMVC拦截器原理，如何自定义拦截器？

SpringMVC如何将请求映射定位到方法上面？结合源码阐述？

SpringMVC常见注解有哪些？

SpringMVC容器和Spring容器的区别？

SpringMVC的控制器是不是单例模式,如果是,有什么问题,怎么解决？

## MyBatis框架

MyBatis中#和$的区别？

MyBatis一级缓存原理以及失效情况？

MyBatis二级缓存的使用？

MyBatis拦截器原理？

看过MyBatis源码吗，请说说它的工作流程？

## Java高级部分

Dubbo负载均衡策略？

Dubbo中Zookeeper做注册中心，如果注册中心集群都挂掉，发布者和订阅者之间还能通信么？

Dubbo完整的一次调用链路介绍？

请说说SpringBoot自动装配原理？

有用过SpringCloud吗，请说说SpringCloud和Dubbo有什么不一样？

什么是WebService，如何基于WebService开发接口？

谈谈项目中分布式事务应用场景？

使用Redis如何实现分布式锁？

请谈谈单点登录原理？

Tomcat如何优化？

后台系统怎么防止请求重复提交？

Linux常见命令有哪些？

请说说什么是Maven的依赖、继承以及聚合？

Git暂存区和工作区的区别？

Git如何创建、回退以及撤销版本？

常见的设计模式有哪些？