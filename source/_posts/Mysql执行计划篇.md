---
title: Mysql执行计划篇
tags:
  - Mysql
categories: Mysql
description: MYSQL 执行计划（explain详解）
---

## 执行计划explain详解
下面是一个执行计划的例子

![avatar](https://raw.githubusercontent.com/huangxiaocan/hexo/master/source/_posts/hexo-image/hexo/explan1.png)  

### id

	select查询的序列号

### select_type

	a.SIMPLE：查询中不包含子查询或者UNION
	b.PRIMARY:查询中若包含任何复杂的子部分，最外层查询的标记
	c.SUBQUERY：在SELECT或WHERE列表中包含了子查询，该子查询的标记
	d.DERIVED（衍生）：在FROM列表中包含的子查询的标记
	e.若第二个SELECT出现在UNION之后，则被标记为UNION；若UNION包含在 FROM子句的子查询中，外层SELECT将被标记为：DERIVED
	f.从UNION表获取结果的SELECT被标记为：UNION RESULT

### table

	输出的行所引用的表

### type

	联合查询所使用的类型，表示MySQL在表中找到所需行的方式，又称“访问类型”。
	type显示的是访问类型，是较为重要的一个指标，结果值从好到坏依次是：
	system > const > eq_ref > ref > fulltext > ref_or_null > index_merge > unique_subquery > index_subquery > range > index > ALL ，一般来说，得保证查询至少达到range级别，最好能达到ref。
	index: 扫描全部索引树
	range: 扫描部分索引，索引范围扫描，对索引的扫描开始于某一点，返回匹配值域的行，常见于between、<、>等的查询
	ref: 非唯一性索引扫描，返回匹配某个单独值的所有行。常见于使用非唯一索引即唯一索引的非唯一前缀进行的查找
	eq_ref：唯一性索引扫描，对于每个索引键，表中只有一条记录与之匹配。常见于主键或唯一索引扫描
	const, system: 当MySQL对查询某部分进行优化，并转换为一个常量时，使用这些类型访问。如将主键置于where列表中，MySQL就能将该查询转换为一个常量。system是const类型的特例，当查询的表只有一行的情况下， 使用system。
	NULL: MySQL在优化过程中分解语句，执行时甚至不用访问表或索引。

### possible_keys

	指出MySQL能使用哪个索引在该表中找到行。查询涉及到的字段上若存在索引，则该索引将被列出，但不一定被查询使用。如果是空的，没有相关的索引。这时要提高性能，可通过检验WHERE子句，看是否引用某些字段，或者检查字段不是适合索引

### key

	显示MySQL实际决定使用的键。如果没有索引被选择，键是NULL

### key_len

	显示MySQL决定使用的键长度。表示索引中使用的字节数，可通过该列计算查询中使用的索引的长度。如果键是NULL，长度就是NULL。文档提示特别注意这个值可以得出一个多重主键里mysql实际使用了哪一部分。

### rows

	这个数表示mysql要遍历多少数据才能找到，表示MySQL根据表统计信息及索引选用情况，估算的找到所需的记录所需要读取的行数，在innodb上可能是不准确的

### SQL语句的一般执行顺序

	(1)from
	(3) join
	(2) on
	(4) where
	(5)group by(开始使用select中的别名，后面的语句中都可以使用)
	(6) avg,sum....
	(7)having
	(8) select
	(9) distinct
	(10) order by




select_type	说明
SIMPLE	简单查询
PRIMARY	最外层查询
SUBQUERY	映射为子查询
DERIVED	子查询
UNION	联合
UNION RESULT	使用联合的结果
table : 正在访问的表名

type	说明
ALL	全数据表扫描
index	全索引表扫描
RANGE	对索引列进行范围查找
INDEX_MERGE	合并索引，使用多个单列索引搜索
REF	根据索引查找一个或多个值
EQ_REF	搜索时使用primary key 或 unique类型
CONST	常量，表最多有一个匹配行,因为仅有一行,在这行的列值可被优化器剩余部分认为是常数,const表很快,因为它们只读取一次。
SYSTEM	系统，表仅有一行(=系统表)。这是const联接类型的一个特例。
性能：all < index < range < index_merge < ref_or_null < ref < eq_ref < system/const
性能在 range 之下基本都可以进行调优

possible_keys : 可能使用的索引

key : 真实使用的

key_len : MySQL中使用索引字节长度

rows : mysql 预估为了找到所需的行而要读取的行数

extra	说明
Using index	此值表示mysql将使用覆盖索引，以避免访问表。
Using where	mysql 将在存储引擎检索行后再进行过滤，许多where条件里涉及索引中的列，当(并且如果)它读取索引时，就能被存储引擎检验，因此不是所有带where子句的查询都会显示“Using where”。有时“Using where”的出现就是一个暗示：查询可受益于不同的索引。
Using temporary	mysql 对查询结果排序时会使用临时表。
Using filesort	mysql会对结果使用一个外部索引排序，而不是按索引次序从表里读取行。mysql有两种文件排序算法，这两种排序方式都可以在内存或者磁盘上完成，explain不会告诉你mysql将使用哪一种文件排序，也不会告诉你排序会在内存里还是磁盘上完成。
Range checked for each record(index map: N)	没有好用的索引，新的索引将在联接的每一行上重新估算，N是显示在possible_keys列中索引的位图，并且是冗余的
limit
limit 匹配后就不会继续进行扫描

mysql> SELECT * FROM user WHERE email = 'klvchen123@126.com' LIMIT 1;
+-----+------------+--------------------+-------+
| nid | name       | email              | extra |
+-----+------------+--------------------+-------+
| 123 | klvchen123 | klvchen123@126.com | 123   |
+-----+------------+--------------------+-------+
1 row in set (0.01 sec)
正确使用索引
使用 like 语句时，%在右边才会使用索引。
没用使用索引

使用索引

or 条件中有未建立索引的列才,索引失效
没用使用索引

使用索引

条件的类型不一致
没用使用索引

使用索引

!= 号
没用使用索引

例外：如果是主键，则会走索引
> 号
没用使用索引

例外：如果是主键或索引是整数类型，则会走索引
order by
没用使用索引

例外：如果 order by 是主键或索引是整数类型，则会走索引
组合索引
遵循最左前缀
# 若 name 和 email 组成组合索引
create index ix_name_email on user(name,email);

name and email -- 使用索引
email and name -- 不使用索引
name                  -- 使用索引
email                  -- 不使用索引
没用使用索引



分类: MySQL