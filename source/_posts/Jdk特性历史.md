---
title: Jdk新特性历史
tags:
  - JDK
categories: JDK
description: Jdk新特性历史
---
## JDK新特性历史
### Java 8 新特性

	Java 8 (又称为 jdk 1.8) 是 Java 语言开发的一个主要版本。 Oracle 公司于 2014 年 3 月 18 日发布 Java 8 ，它支持函数式编程，新的 JavaScript 引擎，新的日期 API，新的Stream API 等。
	
	新特性
	Java8 新增了非常多的特性，我们主要讨论以下几个：
	
	Lambda 表达式 − Lambda允许把函数作为一个方法的参数（函数作为参数传递进方法中。
	
	方法引用 − 方法引用提供了非常有用的语法，可以直接引用已有Java类或对象（实例）的方法或构造器。与lambda联合使用，方法引用可以使语言的构造更紧凑简洁，减少冗余代码。
	
	默认方法 − 默认方法就是一个在接口里面有了一个实现的方法。
	
	新工具 − 新的编译工具，如：Nashorn引擎 jjs、 类依赖分析器jdeps。
	
	Stream API −新添加的Stream API（java.util.stream） 把真正的函数式编程风格引入到Java中。
	
	Date Time API − 加强对日期与时间的处理。
	
	Optional 类 − Optional 类已经成为 Java 8 类库的一部分，用来解决空指针异常。
	
	Nashorn, JavaScript 引擎 − Java 8提供了一个新的Nashorn javascript引擎，它允许我们在JVM上运行特定的javascript应用。

### Java 9 新特性

	Java 9 发布于 2017 年 9 月 22 日，带来了很多新特性，其中最主要的变化是已经实现的模块化系统。接下来我们会详细介绍 Java 9 的新特性。
	
	Java 9 新特性
	模块系统：模块是一个包的容器，Java 9 最大的变化之一是引入了模块系统（Jigsaw 项目）。
	REPL (JShell)：交互式编程环境。
	HTTP 2 客户端：HTTP/2标准是HTTP协议的最新版本，新的 HTTPClient API 支持 WebSocket 和 HTTP2 流以及服务器推送特性。
	改进的 Javadoc：Javadoc 现在支持在 API 文档中的进行搜索。另外，Javadoc 的输出现在符合兼容 HTML5 标准。
	多版本兼容 JAR 包：多版本兼容 JAR 功能能让你创建仅在特定版本的 Java 环境中运行库程序时选择使用的 class 版本。
	集合工厂方法：List，Set 和 Map 接口中，新的静态工厂方法可以创建这些集合的不可变实例。
	私有接口方法：在接口中使用private私有方法。我们可以使用 private 访问修饰符在接口中编写私有方法。
	进程 API: 改进的 API 来控制和管理操作系统进程。引进 java.lang.ProcessHandle 及其嵌套接口 Info 来让开发者逃离时常因为要获取一个本地进程的 PID 而不得不使用本地代码的窘境。
	改进的 Stream API：改进的 Stream API 添加了一些便利的方法，使流处理更容易，并使用收集器编写复杂的查询。
	改进 try-with-resources：如果你已经有一个资源是 final 或等效于 final 变量,您可以在 try-with-resources 语句中使用该变量，而无需在 try-with-resources 语句中声明一个新变量。
	改进的弃用注解 @Deprecated：注解 @Deprecated 可以标记 Java API 状态，可以表示被标记的 API 将会被移除，或者已经破坏。
	改进钻石操作符(Diamond Operator) ：匿名类可以使用钻石操作符(Diamond Operator)。
	改进 Optional 类：java.util.Optional 添加了很多新的有用方法，Optional 可以直接转为 stream。
	多分辨率图像 API：定义多分辨率图像API，开发者可以很容易的操作和展示不同分辨率的图像了。
	改进的 CompletableFuture API ： CompletableFuture 类的异步机制可以在 ProcessHandle.onExit 方法退出时执行操作。
	轻量级的 JSON API：内置了一个轻量级的JSON API
	响应式流（Reactive Streams) API: Java 9中引入了新的响应式流 API 来支持 Java 9 中的响应式编程。