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

	public class MyLinkedList<E> implements Iterable<E> { //迭代器接口
	  6     private Node first;
	  7     private Node last;
	  8     private int size;
	  9     
	 10     public int size() {
	 11         return size;
	 12     }
	 13     
	 14     public void rangeCheck(int index) {
	 15         if(index<0||index>=size) {
	 16             try {
	 17                 throw new MyException();
	 18             } catch (MyException e) {
	 19                 e.printIndex();
	 20             }
	 21         }
	 22     }
	 23     
	 24     public Node node(int index) {  //遍历,获得当前位序值
	 25         if(index<=(size>>1)) {  //右移一位相当于除以2
	 26             Node x = first;
	 27             for(int i=0;i<index;++i)
	 28                 x=x.next;
	 29             return x;
	 30         }else {
	 31             Node x = last;
	 32             for(int i=size-1;i>index;--i)
	 33                 x=x.prev;
	 34             return x;
	 35         }
	 36     }
	 37     
	 38     public boolean isEmpty(){
	 39         return size==0;
	 40     }
	 41     
	 42     public boolean contains(Object o) {
	 43         return indexOf(o)>=0;
	 44     }
	 45     
	 46     public int indexOf(Object o) {
	 47         for(int i=0;i<size;++i) {
	 48             if(node(i).object.equals(o))
	 49                 return i;
	 50         }
	 51         return -1;
	 52     }
	 53     
	 54     private Node getNode(int index) {
	 55         rangeCheck(index);
	 56         return node(index);
	 57     }
	 58     
	 59     @SuppressWarnings("unchecked")
	 60     private E elementData(int index){
	 61         return (E)getNode(index).object;
	 62     }
	 63     
	 64     public E get(int index) {
	 65         return elementData(index);
	 66     }
	 67     
	 68     public E set(int index,E element) {
	 69         rangeCheck(index);
	 70         E oldValue = elementData(index);
	 71         node(index).object = element;
	 72         return oldValue;
	 73     }
	 74     
	 75     public void add(E elemnt) {
	 76         Node n = new Node();
	 77         n.object = elemnt;
	 78         if(first==null) {
	 79             n.prev = null;
	 80             n.next = null;
	 81             first = last = n;
	 82         }else {
	 83             last.next = n;
	 84             n.prev = last;
	 85             n.next = null;
	 86             last = n;
	 87         }
	 88         ++size;
	 89     }
	 90     
	 91     public void add(int index,E element) {
	 92         Node n = new Node();
	 93         n.object = element;
	 94         if(index>0) {
	 95             Node temp = getNode(index-1);
	 96             if(index!=size)
	 97                 temp.next.prev = n;
	 98             n.next = temp.next;
	 99             temp.next = n;
	100             n.prev = temp;
	101             if(index==size)
	102                 last = n;
	103             ++size;
	104         }else if(index==0) {
	105             if(first==null) {
	106                 n.prev = null;
	107                 n.next = null;
	108                 first = last = n;
	109             }else {
	110                 n.prev = null;
	111                 n.next = first;
	112                 first.prev = n;
	113                 first = n;
	114             }
	115             ++size;
	116         }else {
	117             try {
	118                 throw new MyException();
	119             }catch(MyException e) {
	120                 e.printIndex();
	121             }
	122         }
	123     }
	124     
	125     public void remove(int index) {
	126         Node temp =getNode(index);
	127         if(!(temp==first&&temp==last)) {
	128             if(temp==first) {
	129                 temp.next.prev = null;
	130                 first = temp.next;
	131             }else if(temp==last) {
	132                 temp.prev.next = null;
	133                 last = temp.prev;
	134             }else {
	135                 temp.next.prev = temp.prev;
	136                 temp.prev.next = temp.next;
	137             }
	138         }
	139         temp = null;
	140         --size;
	141     }
	142     
	143     public boolean remove(E element) {
	144         int i = 0;
	145         for(Node temp = first;temp!=null;temp=temp.next) {
	146             if(temp.object.equals(element)) {
	147                 remove(i);
	148                 return true;
	149             }
	150             ++i;
	151         }
	152         return false;
	153     }
	154 
	155     @Override
	156     public Iterator<E> iterator() {
	157         return new MyIter();
	158     }
	159     
	160     private class MyIter implements Iterator<E> {
	161         
	162         //计数器-->指针 游标
	163         private int cursor;
	164         private int lastRet = -1;
	165 
	166         //判断是否存在下一个
	167         @Override
	168         public boolean hasNext() {
	169             return cursor != size;
	170         }
	171 
	172         //返回游标当前位置，并把游标移到下一位置
	173         @SuppressWarnings("unchecked")
	174         @Override
	175         public E next() {
	176             if(!hasNext()) {
	177                 try {
	178                     throw new MyException();
	179                 } catch (MyException e) {
	180                     e.printnext();
	181                 }
	182             }
	183             lastRet = cursor;
	184             return (E)node(cursor++).object;
	185         }
	186         
	187         @Override
	188         public void remove(){
	189             if(lastRet<0) {
	190                 try {
	191                     throw new MyException();
	192                 } catch (MyException e) {
	193                     e.printremove();
	194                 }
	195             }
	196             MyLinkedList.this.remove(lastRet);
	197             cursor = lastRet;
	198             lastRet = -1;
	199         }
	200     }

Java中方法参数的传递规则？

	值传递

Java中throw和throws的区别是什么？

	1、throws出现在方法函数头；而throw出现在函数体。 
	2、throws表示出现异常的一种可能性，并不一定会发生这些异常；throw则是抛出了异常，执行throw则一定抛出了某种异常对象。 
	3、两者都是消极处理异常的方式（这里的消极并不是说这种方式不好），只是抛出或者可能抛出异常，但是不会由函数去处理异常，真正的处理异常由函数的上层调用处理。



重载和重写的区别？

	方法的重载和重写都是实现多态的方式，区别在于前者实现的是编译时的多态性，而后者实现的是运行时的多态性。重载发生在一个类中，同名的方法如果有不同的参数列表（参数类型不同、参数个数不同或者二者都不同）则视为重载；重写发生在子类与父类之间，重写要求子类被重写方法与父类被重写方法有相同的参数列表，有兼容的返回类型，比父类被重写方法更好访问，不能比父类被重写方法声明更多的异常（里氏代换原则）。重载对返回类型没有特殊的要求，不能根据返回类型进行区分

手写ArrayList的实现，在笔试中如何过关斩将?

	public class MyArrayList {
 
	private Object[] elementData; // 底层数组
	private int size; // 数组大小
 
	// 获得数组大小
	public int size() {
		return size;
	}
 
	// 无参构造函数
	public MyArrayList() {
		this(10);
	}
 
	// 含参构造函数
	public MyArrayList(int initialCapacity) {
		if (initialCapacity < 0) {
			try {
				throw new Exception();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		elementData = new Object[initialCapacity];
	}
 
	// 判断是否为空
	public boolean isEmpty() {
		return size == 0;
	}
 
	// 根据下标获取对象
	public Object get(int index) {
		rangeCheck(index);
		return elementData[index];
	}
 
	public boolean add(Object obj) {
		ensureCapacity();
		elementData[size] = obj;
		size++;
		return true;
	}
 
	// 插入操作
	public void add(int index, Object obj) {
		rangeCheck(index);
		ensureCapacity();
		System.arraycopy(elementData, index, elementData, index + 1, size - index);
		elementData[index] = obj;
		size++;
	}
 
	// 删除操作
	public Object remove(int index) {
		rangeCheck(index);
		int arrnums = size - index - 1;
		Object oldValue = elementData[index];
		if (arrnums > 0) {
			System.arraycopy(elementData, index, elementData, index, arrnums);
		}
		elementData[--size] = null;
		return oldValue;
	}
 
	public boolean remove(Object obj) {
		for (int i = 0; i < size; i++) {
			if (get(i).equals(obj)) {
				remove(i);
			}
			break;
		}
		return true;
	}
 
	public Object set(int index, Object obj) {
		rangeCheck(index);
		Object oldValue = elementData[index];
		elementData[index] = obj;
		return oldValue;
	}
 
	// 检查容量，必要时扩容处理
	private void ensureCapacity() {
		if (size == elementData.length) {
			Object[] newArray = new Object[size + (size >> 1)];
			System.arraycopy(elementData, 0, newArray, 0, size);
			elementData = newArray;
		}
	}
 
	// 检查下标是否合法
	public void rangeCheck(int index) {
		if (index < 0 || index >= size) {
			try {
				throw new Exception();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
	}
 
	public static void main(String[] args) {
		MyArrayList mylist = new MyArrayList();
		mylist.add("哈哈");
		mylist.add("呵呵");
		mylist.add("哦哦");
		mylist.add("哈哈");
		mylist.add(1, "手写代码");
		String old = (String) mylist.remove(3); // 返回的是旧值
		System.out.println(old);
		System.out.println(mylist.remove("哦哦"));
		System.out.println(mylist.isEmpty());
		System.out.println(mylist.get(1));
		System.out.println(mylist.size());
		System.out.println(mylist.set(2, "你好啊")); // 返回旧值
		System.out.println(mylist.get(2));
	}
 
	}


finally语句块你踩过哪些坑？

	finally语句并不是每次都执行，只有线程执行过try语句块，finally语句块才会执行。如果线程执行到try语句块之前就return的话，finally语句是不会执行的。如例程中第一种情况，在try语句块之前执行return语句将会直接退出函数。
	只要线程进入过try语句块，不论有没有抛出异常，finally语句块都会执行。如例程中的第二种和第三种情况，线程执行进入try语句块，不管有没有出现异常，finally语句都正常执行。
	finally 语句块是在结果返回之前执行的。根据第二种和第三种情况，可以发现finally语句执行在main函数打印结果之前。

为什么重写equals方法需同时重写hashCode方法？

	两个对象相等，hashcode一定相等

	两个对象不等，hashcode不一定不等

	hashcode相等，两个对象不一定相等

	hashcode不等，两个对象一定不等

equals() 与 == 的区别？

	== 比较的是变量(栈)内存中存放的对象的(堆)内存地址，用来判断两个对象的地址是否相同，即是否是指相同一个对象。比较的是真正意义上的指针操作。

	equals用来比较的是两个对象的内容是否相等，由于所有的类都是继承自java.lang.Object类的，所以适用于所有对象，如果没有对该方法进行覆盖的话，调用的仍然是Object类中的方法，而Object中的equals方法返回的却是==的判断。

StringBuffer和StringBuilder的区别，从源码角度分析?

	都是final修饰的v类，不能被继承，同时继承的类和实现的接口相同
	StringBuffer比StringBuilder多了个缓存char类型数组成员变量，它的作用是，在多次调用tostring方法时，可以输出缓存的数据值，因此每次涉及到StringBuffer中字符串变化时都需要清除这个字段的数据，典型的线程安全，牺牲了时间和空间保证了数据安全；


你知道HashMap的数据结构吗？

	HashMap实际上是一个“链表散列”的数据结构，即数组和链表的结合体。

为何HashMap的数组长度一定是2的次幂？

HashMap何时扩容以及它的扩容机制？

	当向容器添加元素的时候，会判断当前容器的元素个数，如果大于等于阈值---即当前数组的长度乘以加载因子的值的时候，就要自动扩容
	
	扩容的算法是什么：
	
	扩容就是重新计算容量，向HashMap对象里不停的添加元素，而HashMap对象内部的数组无法装载更多的元素时，对象就需要扩大数组的长度，以便能装入更多的元素。当然Java里的数组是无法自动扩容的，方法是使用一个新的数组代替已有的容量小的数组


HashMap的key一般用字符串,能用其他对象吗？

	可以，能用其他对象，必须是immutable的，但是自实现的类必须Override两个方法：equals()和hashCode()。因为为了要计算hashCode()，就要防止键值改变，如果键值在放入时和获取时返回不同的hashcode的话，那么就不能从HashMap中找到你想要的对象

HashMap的key和value都能为null么?如果key能为null,那么它是怎么样查找值的？

HashMap是线程安全的吗？如何实现线程安全？

从源码角度分析HashSet实现原理？

HashTable与HashMap的实现原理有什么不同？

String方法intern() 你真的会用吗？

什么是自动拆装箱？

String.valueOf和Integer.toString的区别？

	只有String.valueOf()方法会首先对转换的对象进行判空检测，如果为空，则返回“null”字符串，以至于不会报出空指针异常

三、Java多线程

线程的生命周期包括哪几个阶段？

	新建状态（New）：当线程对象对创建后，即进入了新建状态，如：Thread t = new MyThread();

	就绪状态（Runnable）：当调用线程对象的start()方法（t.start();），线程即进入就绪状态。处于就绪状态的线程，只是说明此线程已经做好了准备，随时等待CPU调度执行，并不是说执行了t.start()此线程立即就会执行；

	运行状态（Running）：当CPU开始调度处于就绪状态的线程时，此时线程才得以真正执行，即进入到运行状态。注：就     绪状态是进入到运行状态的唯一入口，也就是说，线程要想进入运行状态执行，首先必须处于就绪状态中；
	
	阻塞状态（Blocked）：处于运行状态中的线程由于某种原因，暂时放弃对CPU的使用权，停止执行，此时进入阻塞状态，直到其进入到就绪状态，才 有机会再次被CPU调用以进入到运行状态。根据阻塞产生的原因不同，阻塞状态又可以分为三种：

	1.等待阻塞：运行状态中的线程执行wait()方法，使本线程进入到等待阻塞状态；

	2.同步阻塞 -- 线程在获取synchronized同步锁失败(因为锁被其它线程所占用)，它会进入同步阻塞状态；

	3.其他阻塞 -- 通过调用线程的sleep()或join()或发出了I/O请求时，线程会进入到阻塞状态。当sleep()状态超时、join()等待线程终止或者超时、或者I/O处理完毕时，线程重新转入就绪状态。

	死亡状态（Dead）：线程执行完了或者因异常退出了run()方法，该线程结束生命周期。

多线程有几种实现方式？

	继承Thread类、实现Runnable接口、实现Callable接口通过FutureTask包装器来创建Thread线程、使用ExecutorService、Callable、Future实现有返回结果的多线程。

请谈谈什么是进程，什么是线程？

	进程是资源（CPU、内存等）分配的基本单位，它是程序执行时的一个实例。程序运行时系统就会创建一个进程，并为它分配资源，然后把该进程放入进程就绪队列，进程调度器选中它的时候就会为它分配CPU时间，程序开始真正运行。

	线程是程序执行时的最小单位，它是进程的一个执行流，是CPU调度和分派的基本单位，一个进程可以由很多个线程组成，线程间共享进程的所有资源，每个线程有自己的堆栈和局部变量。线程由CPU独立调度执行，在多CPU环境下就允许多个线程同时运行。同样多线程也可以实现并发操作，每个请求分配一个线程来处理

启动线程是用start()方法还是run()方法？

	run()

说说线程安全问题，什么实现线程安全，如何实现线程安全？

	多线程编程中的三个核心概念:原子性,可见性,顺序性

	http://www.jasongj.com/java/thread_safe/

sychronized和Lock的区别？

	1.首先synchronized是java内置关键字，在jvm层面，Lock是个java类；

	2.synchronized无法判断是否获取锁的状态，Lock可以判断是否获取到锁；

	3.synchronized会自动释放锁(a 线程执行完同步代码会释放锁 ；b 线程执行过程中发生异常会释放锁)，Lock需在finally中手工释放锁（unlock()方法释放锁），否则容易造成线程死锁；

	4.用synchronized关键字的两个线程1和线程2，如果当前线程1获得锁，线程2线程等待。如果线程1阻塞，线程2则会一直等待下去，而Lock锁就不一定会等待下去，如果尝试获取不到锁，线程可以不用一直等待就结束了；

	5.synchronized的锁可重入、不可中断、非公平，而Lock锁可重入、可判断、可公平（两者皆可）

	6.Lock锁适合大量同步的代码的同步问题，synchronized锁适合代码少量的同步问题

sleep()和wait()的区别？

	Sleep是线程类Thread 的方法，它是使当前线程暂时睡眠，可以放在任何位置

	wait是使当前线程暂时放弃对象的使用权进行等待，必须放在同步方法或同步块里

深入分析ThreadLocal的实现原理？

	ThreadLocal ，也叫线程本地变量，可能很多朋友都知道ThreadLocal为变量在每个线程中都创建了所使用的的变量副本。使用起来都是在线程的本地工作内存中操作，并且提供了set和get方法来访问拷贝过来的变量副本。底层也是封装了ThreadLocalMap集合类来绑定当前线程和变量副本的关系，各个线程独立并且访问安全

你看过AbstractQueuedSynchronizer源码阅读吗，请说说实现原理？

谈谈对synchronized的偏向锁、轻量级锁、重量级锁的理解？

通过三种方式实现生产者消费者模式？

	1.使用Object的wait/notify的消息通知机制；
	2.使用Lock的Condition的await/signal的消息通知机制；
	3.使用BlockingQueue实现。本文主要将这三种实现方式进行总结归纳

JVM层面分析sychronized如何保证线程安全的？

	从字节码层面，在Java虚拟机规范中，可以看到，synchronized在Java虚拟机中的实现原理，就是说Java虚拟机在执行同步代码块的时候，其实它是基于进入和退出monitor对象来实现方法同步的，也就是说，它有两个字节码指令分别就是monitorenter和monitorexit，当进入代码块的时候monitorente，当代码块执行完毕之后就会执行monitorexit

	https://blog.csdn.net/G_66_hero/article/details/85706626

JDK层面分析sychronized如何保证线程安全的？

如何写一个线程安全的单例？

	单例模式是常见的设计模式之一：目的是节省内存，限制了实例的个数；有利于java GC回收机制。

　　

	单例模式的三个好处：
	
	1.控制资源的使用，通过线程同步来控制资源的并发访问
	
	2.控制实例的产生个数，来达到节约资源的目的
	
	3.作为通信媒介使用，在不建立连接的情况下，让两个不先关的进程和线程之间实现通信

 

	单例模式分类：　饿汉模式（在类加载时便会创建对象）；

	懒汉模式（在外部第一次请求实例时才会创建实例）；

	登记式模式

 

	单例模式特点：

	1.单例类只有一个实例
	
	2.单例类必须自己创建自己唯一的实例
	
	3.单例类必须自己给其他类提供这一实例

 

	1.懒汉模式：类加载时不会初始化，当外部第一次请求实例时才会创建实例；而且第一次创建后不在创建该实例；

	特点是：运行时获取对象的速度比较慢，但加载的时候比较快，它在整个生命的应用周期只占用一部分资源

	//单例模式-懒汉式单例
	public class LazySingleton {
	     //私有静态对象,加载时候不做初始化
	     private static LazySingleton jjy=null;
	     // 私有构造方法,避免外部创建实例
	     private LazySingleton(){}
	
	     /**
	      * 静态工厂方法,返回此类的唯一实例. 
	      * 当发现实例没有初始化的时候,才初始化.
	      * @return LazySingleton
	      */
	     synchronized public static LazySingleton getJjy(){
	         if(jjy==null){
	             jjy=new LazySingleton();
	         }
	         return jjy;
	     }
	}

	2，饿汉模式：类加载时就会初始化，创建实例；

	特点是：运行时获取对象速度比较快，但加载时速度比较慢，会一直占用资源  （程序打开加载比较慢，但运行速度快---从用户体验角度来说推荐饿汉）

	//单例模式-饿汉式单例
	public class EagerSingleton {
	//私有静态对象,加载时候不做初始化
	private static EagerSingleton jjy=new EagerSingleton();
	// 私有构造方法,避免外部创建实例
	private EagerSingleton(){}
	
	/**
	* 静态工厂方法,返回此类的唯一实例. 
	* 
	*
	*/
	synchronized public static EagerSingleton getJjy(){
	
	return jjy;
	}
	}


通过AQS实现一个自定义的Lock？

ThreadLocal什么时候会出现OOM的情况？为什么？

为什么wait, notify 和 notifyAll这些方法不在thread类里面？

你真的理解CountDownLatch与CyclicBarrier使用场景吗？

出现死锁，如何排查定位问题？

notify和notifyAll的区别？

线程池启动线程submit和execute有什么不同？

SimpleDateFormat是线程安全的吗？如何解决？

	可知SimpleDateFormat维护的用于format和parse方法计算日期-时间的calendar被清空了，如果此时线程A将calendar清空且没有设置新值，线程B也进入parse方法用到了SimpleDateFormat对象中的calendar对象，此时就会产生线程安全问题

	每次用完立即销毁

请谈谈ConcurrentHashmap底层实现原理？

	ConcurrentHashMap的数据结构（数组+链表+红黑树），桶中的结构可能是链表，也可能是红黑树，红黑树是为了提高查找效率。

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

	方法区、堆、栈（虚拟机栈、本地方法栈）、程序计数器

JVM堆中对象是如何创建的?

	类加载检查，为对象分配内存，内存空间初始化，对象设置，init

JVM对象的结构？

	对象的结构有：

　　　　1.Header（对象头),其组成主要有两部分：

　　　　　　　　1.自身运行时的数据(Mark Word)，包括：

　　　　　　　　　　　　1.哈希值

　　　　　　　　　　　　2.GC分代年龄。

　　　　　　　　　　　　3.锁状态标志

　　　　　　　　　　　　4。线程所持有的锁

　　　　　　　　　　　　5.偏向线程ID

　　　　　　　　　　　　6.偏向时间戳

　　　　　　　　自身运行时的数据(Mark Word)说占多少多内存呢？其实是根据32位，64位的虚拟机而定的。但是它包含的数据远远超过其本身内存。

　　　　　　　　那它是如何做到将这些数据存储的 呢？

JVM垃圾回收-如何判断对象是否是垃圾对象？

	一、引用计数算法

       引用计数算法就是在对象中添加了一个引用计数器，当有地方引用这个对象时，引用计数器的值就加1，当引用失效的时候，引用计数器的值就减1。当引用计数器的值为0时，jvm就开始回收这个对象。如果时当栈指向堆时，如果指向了一个对象，那么堆中的引用计数器的值就会加1，当这个栈指向null时，对象的引用计数器就减1。

        这种方法虽然很简单、高效，但是JVM一般不会选择这个方法，因为这个方法会出现一个问题：当对象之间相互指向时，两个对象的引用计数器的值都会加1，而由于两个对象时相互指向，所以引用不会失效，这样JVM就无法回收。

	二、可达性分析算法

        针对引用计数算法的BUG，JVM现在了另一种比较实际的方法:定义一个名为"GC Roots"的对象作为起始点，这个"GC Roots"可以有多个，从这些节点开始向下搜索，搜索所走过的路径称为引用链(Reference Chain)，当一个对象到GC Roots没有任何引用链相连时，则证明此对象是不可用的，即可以进行垃圾回收

JVM垃圾回收算法有哪些？

		3.1 标记-清除算法
		3.2 复制算法
		3.3 标记-整理算法
		3.4 分代收集算法
			3.4.1 年轻代（Young Generation）的回收算法
			3.4.2 年老代（Old Generation）的回收算法
			3.4.3 持久代（Permanent Generation）的回收算法

JVM垃圾收集器有哪些？

	Serial收集器，ParNew收集器，Parallel Scavenge（并行回收）收集器，Serial Old 收集器，Parallel Old 收集器，CMS收集器，G1收集器

JVM内存是如何分配的？



从一道面试题分析类的加载过程？

JVM双亲委派机制？

JVM可以作为GC Root的对象有哪些？

请写出几段可以导致内存溢出、内存泄漏、栈溢出的代码？

哪些情况会导致Full GC？

频繁GC问题或内存溢出问题，如何定位？

## SQL性能优化

数据库三范式是什么？

	第一范式：当关系模式R的所有属性都不能在分解为更基本的数据单位时，称R是满足第一范式的，简记为1NF。满足第一范式是关系模式规范化的最低要求，否则，将有很多基本操作在这样的关系模式中实现不了。

	第二范式：如果关系模式R满足第一范式，并且R得所有非主属性都完全依赖于R的每一个候选关键属性，称R满足第二范式，简记为2NF。

	第三范式：设R是一个满足第一范式条件的关系模式，X是R的任意属性集，如果X非传递依赖于R的任意一个候选关键字，称R满足第三范式，简记为3NF

数据库的事务、ACID及隔离级别？

	原子性(Atomicity)：一个事务必须被视为一个不可分割的最小工作单元，整个事务中的所有操作要么全部提交，要么全部失败回滚，不可能执行其中的一部分操作

	一致性(Consistency)：数据库总是从一个一致性状态转移到另一个一致性状态，例如：银行账户A有1000元，其他账户有10000元，他们相互之间不管怎么转账，总量都不变

	隔离性(Isolation)：通常来说，一个事务所做的修改在最终提交以前，其他事务是不可见的

	持久性(Durability)：一旦事务提交，其所做的修改就会永久保存到数据库中

 

	SQL标准中定义了四种隔离级别：

	READ UNCOMMITTED(未提交读)：事务中的修改即使没有提交，对其他事务也都是可见的，事务可以读取未提交的数据，这称之为脏读

	READ COMMITTED(提交读)：大多数据库系统默认隔离级别是该项，但MySQL不是，COMMITED满足隔离性，也称不可重复读，同一个事务，多次执行相同的select，结果不一样

	REPEATED READ(可重复读)：保证了同一个事务中多次读取同样记录的结果是一致的，但是无法解决幻读问题，幻读是指当某个事务在读取某个范围内记录时，另一个事务又在该范围内插入了新的记录，当之前的的事务再次读取该范围内的记录时会产生幻行，MySQL默认隔离级别

	SERIALIZABLE(可串行化)：SERIALIZABLE是最高的隔离级别，它通过强制事务串行执行，避免了前面说的幻读问题，简单来说，SERIALIZABLE会在读取的每一行数据上加锁，可能导致大量超时和锁争用，只有在非常确保数据的一致性而且可接受没有并发的情况下才考虑使用该锁

不考虑事务的隔离性，容易产生哪三种情况？

	脏读：A事务中读取到了B事务中未提交的数据，造成数据错误

	不可重复读：A事务中读取到了B事务中已提交的数据，在特定情景下会产生影响，比如生成统一的数据报表

	虚读（幻读）：A事务中读取到了B事务中已提交的新插入的数据，影响同上

数据库连接池原理？

	https://blog.csdn.net/guobinhui/article/details/85157805

什么是B-Tree？

	https://www.cnblogs.com/dongguacai/p/7239599.html

什么是B+Tree？
	
	https://www.cnblogs.com/dongguacai/p/7241860.html

MySQL数据库索引结构？

	一、Mysql索引主要有两种结构：B+Tree索引和Hash索引
	Hash索引

	mysql中，只有Memory(Memory表只存在内存中，断电会消失，适用于临时表)存储引擎显示支持Hash索引，是Memory表的默认索引类型，尽管Memory表也可以使用B+Tree索引。Hash索引把数据以hash形式组织起来，因此当查找某一条记录的时候，速度非常快。但是因为hash结构，每个键只对应一个值，而且是散列的方式分布。所以它并不支持范围查找和排序等功能。

 

	B+Tree索引

	B+Tree是mysql使用最频繁的一个索引数据结构，是Inodb和Myisam存储引擎模式的索引类型。相对Hash索引，B+Tree在查找单条记录的速度比不上Hash索引，但是因为更适合排序等操作，所以它更受欢迎。毕竟不可能只对数据库进行单条记录的操作。

什么是索引？什么条件适合建立索引？什么条件不适合建立索引？


	1>数据库中索引的结构是一种排序的数据结构。

	2>数据库索引是通过B树和变形的B+树实现的。

	3>什么情况下不适合建立索引？

		1.对于在查询过程中很少使用或参考的列，不应该创建索引。

		2.对于那些只有很少数据值的列，不应该创建索引。

		3.对于那些定义为image，text和bit数据类型的列，不应该创建索引。

		4.当修改性能远大于检索性能，不应该建立索引。

	4>建立索引的优点？

		1.通过创建唯一性的索引，可以保证表中每一行数据的唯一性；
		2.可以大大加快表中数据的检索素的，这也是创建索引的主要原因；
		3.可以加快表与表之间的链接，特别是在实现表与表之间的参考完整性实现有特别的意义；
		4.通过使用索引，可以在查询的过程中，使用优化隐藏器，提高系统性能。

 

	5>建立索引的缺点？

		1.创建索引和维护索引耗时，时间随着数据的增加而增加，成正比；

		2.索引需要占物理空间，除了数据表占数据空间外，每一个索引还要占一定的物理空间，如果建立聚簇索引，占得物理空间会更大；

		3.当对表中的数据进行维护时，对索引也要进行维护，这样就降低了数据的维护速度。
		可以在数据库中建立三种索引：唯一索引，主键索引，聚集索引。

		唯一索引(unique) :不允许任意两行具有相同索引值的索引。

		主键索引(primary):数据表中经常有一列或多列组合，其职唯一标识要求主键中的每表中的每一行，则该列称为主键。个值都是唯一的，当查询时使用主键索引，他还允许对数据的快速访问。

		聚集索引()：表中行的物理顺序和表中的逻辑顺序相同。一个标志能有一个聚集索引。

		如果一个索引不是聚集索引，则表中的数据的物理顺序和表中的逻辑顺序不相同。

索引失效的原因有哪些？如何优化避免索引失效？

	https://blog.csdn.net/u010793461/article/details/79851372

MySQL如何启动慢查询日志？

	show variables like 'slow_query_log';

MySQL如何使用show Profile进行SQL分析？

一条执行慢的SQL如何进行优化，如何通过Explain+SQL分析性能？

	https://blog.csdn.net/qq_35216516/article/details/80523773

什么是行锁、表锁、读锁、写锁，说说它们各自的特性？

什么情况下行锁变表锁？

什么情况下会出现间隙锁？

谈谈你对MySQL的in和exists用法的理解？

MySQL的数据库引擎有哪些，如何确定在项目中要是用的存储引擎？

	MyISAM、InnoDB、MERGE、MEMORY(HEAP)、BDB(BerkeleyDB)、EXAMPLE、FEDERATED、ARCHIVE、CSV、BLACKHOLE。

count(*)、count(列名)和count(1)的区别？

union和union all的区别？

	UNION用的比较多union all是直接连接，取到得是所有值，记录可能有重复   union 是取唯一值，记录没有重复   

## Spring框架

Spring的IOC和AOP机制？

Spring中Autowired和Resource关键字的区别？

	历史：@Autowired是属于spring注解，org.springframework.beans.factory.annotation.Autowired

		@Resource 不属于Spring的注解，jdk1.6支持的注解   javax.annotation.Resource

	共同点：

		装备bean，写在字段上，或写在setter方法

	不同点：

		@Autowired  默认按类型装备

		依赖对象必须存在，如果允许null值，可以设置它的required属性为false     @Autowired(required=false)

		也可以使用名称装配，配合@Qualifire 注解

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

	从以上很容易看出，单例是线程不安全的，会导致属性的重复性利用。

	最佳实践：

		1、不要在controller中定义成员变量。

		2、万一必须要定义一个非静态成员变量时候，则通过注解@Scope("prototype")，将其设置为多例模式

## MyBatis框架

MyBatis中#和$的区别？

	#相当于对数据 加上 双引号，$相当于直接显示数据

MyBatis一级缓存原理以及失效情况？

	一级缓存是Session会话级别的缓存，位于表示一次数据库会话的SqlSession对象之中，又被称之为本地缓存。一级缓存是MyBatis内部实现的一个特性，用户不能配置，默认情况下自动支持的缓存，用户没有定制它的权利（不过这也不是绝对的，可以通过开发插件对它进行修改）

	https://blog.csdn.net/Gaomb_1990/article/details/80641964

MyBatis二级缓存的使用？

	如果要实现MyBatis的二级缓存，一般来说有如下两种方式：

	1. 采用MyBatis内置的Cache机制。

	2. 采用三方Cache框架， 比如EhCache, OSCache等等

MyBatis拦截器原理？

看过MyBatis源码吗，请说说它的工作流程？

	读取mybatis全局配置文件

	将定义好的mybatis全局配置文件进行读取，并包装称为一个InputStream对象。这个比较简单，就不详细分析

	解析配置文件

	由SqlSessionFactoryBuilder类的bulid方法驱动，对包装好的XML文件进行解析。很容易看到，其具体的解析任务是交给XMLConfigBuilder对象完成，

	Configuration作为解析配置文件过程中，最重要的一个类，它的作用主要如下： 
	a.读入配置文件 
	b.提供单例，为后续创建SessionFactory服务提供配置参数 
	c. 初始化配置信息

	Mybatis的几乎所有配置文件信息都是存储在由XMLConfigBuilder构建的Configuration对象中，那么它是如何去构建的


	https://blog.csdn.net/jackFXX/article/details/80292186

## Java高级部分

Dubbo负载均衡策略？

	Dubbo提供的负载均衡策略

	Random LoadBalance：随机策略。按照概率设置权重，比较均匀，并且可以动态调节提供者的权重。
	RoundRobin LoadBalance：轮询策略。轮询，按公约后的权重设置轮询比率。会存在执行比较慢的服务提供者堆积请求的情况，比如一个机器执行的非常慢，但是机器没有挂调用（如果挂了，那么当前机器会从Zookeeper的服务列表删除），当很多新的请求到达该机器后，由于之前的请求还没有处理完毕，会导致新的请求被堆积，久而久之，所有消费者调用这台机器上的请求都被阻塞。
	LeastActive LoadBalance：最少活跃调用数。如果每个提供者的活跃数相同，则随机选择一个。在每个服务提供者里面维护者一个活跃数计数器，用来记录当前同时处理请求的个数，也就是并发处理任务的个数。所以如果这个值越小说明当前服务提供者处理的速度很快或者当前机器的负载比较低，所以路由选择时候就选择该活跃度最小的机器。如果一个服务提供者处理速度很慢，由于堆积，那么同时处理的请求就比较多，也就是活跃调用数目越大，这也使得慢的提供者收到更少请求，因为越慢的提供者的活跃度越来越大。
	ConsistentHash LoadBalance：一致性Hash策略。一致性Hash，可以保证相同参数的请求总是发到同一提供者，当某一台提供者挂了时，原本发往该提供者的请求，基于虚拟节点，平摊到其他提供者，不会引起剧烈变动。

Dubbo中Zookeeper做注册中心，如果注册中心集群都挂掉，发布者和订阅者之间还能通信么？

	可以的，启动dubbo时，消费者会从zk拉取注册的生产者的地址接口等数据，缓存在本地。每次调用时，按照本地存储的地址进行调用

Dubbo完整的一次调用链路介绍？

请说说SpringBoot自动装配原理？

	Spring Boot四大核心：

	自动配置：针对很多Spring应用程序和常见的应用功能，Spring Boot能自动提供相关配置。
	起步依赖：告诉Spring Boot需要什么功能， 它就能引入需要的依赖库
	Actuator：让你能够深入运行中的Spring Boot应用程序，一探Spring Boot程序的内部信息。
	命令行界面：这是Spring Boot的可选特性，主要针对Groovy语言使用。

	@EnableAutoConfiguration



有用过SpringCloud吗，请说说SpringCloud和Dubbo有什么不一样？

	相同点：SpringCloud 和Dubbo可以实现RPC远程调用框架，可以实现服务治理。

 

	不同点:

	SpringCloud是一套目前比较网站微服务框架了，整合了分布式常用解决方案遇到了问题注册中心Eureka、负载均衡器Ribbon ，客户端调用工具Rest和Feign，分布式配置中心Config，服务保护Hystrix，网关Zuul Gateway ，服务链路Zipkin，消息总线Bus等。

 

	从架构上分析

		Dubbo内部实现功能没有SpringCloud强大（全家桶），只是实现服务治理，缺少分布式配置中心、网关、链路、总线等，如果需要用到这些组件，需要整合其他框架。

 

	从更新迭代速度分析

		Dubbo目前更新速度没有SpringCloud快，到SpringCloud2.0后SpringCloud会越来完善和稳定。

 

	从开发背景角度分析

	Dubbo的开发背景是阿里巴巴， 在中国也推出了非常多的优秀的开源框架
	但是在SpringCloud的背景是Spring家族，Spring是专注于企业级开源框架开发，在中国，或者在整个世界上Spring框架都应用的非常广泛。所有相对来说SpringCloud的背景比Dubbo更加强大。

 

	最后总结下：如果学习Dubbo的话，学习其他的分布式解决方案需要自己组装，反而如果学习SpringCloud，它已经把整个常用分布式解决都整合好了。

什么是WebService，如何基于WebService开发接口？

谈谈项目中分布式事务应用场景？

使用Redis如何实现分布式锁？

	使用Redis实现分布式锁最简单的方案是在获取锁之前先查询一下以该锁为key对应的value存不存在，如果存在，则说明该锁被其他客户端获取了，否则的话就尝试获取锁，获取锁的方法很简单，只要以该锁为key，设置一个随机的值就行了。比如，我们有一批任务需要由多个分布式线程处理，每个任务都有一个taskId，为了保证每个任务只被执行一次，在工作线程执行任务之前，先获取该任务的锁，锁的key可以为taskId

请谈谈单点登录原理？

Tomcat如何优化？

	https://blog.csdn.net/u010195563/article/details/80966025

后台系统怎么防止请求重复提交？

	分布式锁

Linux常见命令有哪些？

请说说什么是Maven的依赖、继承以及聚合？

Git暂存区和工作区的区别？

Git如何创建、回退以及撤销版本？

常见的设计模式有哪些？

	设计模式就是经过前人无数次的实践总结出的，设计过程中可以反复使用的、可以解决特定问题的设计方法。

	单例(饱汉模式、饥汉模式)
	1、构造方法私有化，除了自己类中能创建外其他地方都不能创建

	2、在自己的类中创建一个单实例（饱汉模式是一出来就创建创建单实例，而饥汉模式需要的时候才创建）

	3、提供一个方法获取该实例对象(创建时需要进行方法同步)

	工厂模式:Spring IOC就是使用了工厂模式.
		对象的创建交给一个工厂去创建。

	代理模式:Spring AOP就是使用的动态代理。
 
