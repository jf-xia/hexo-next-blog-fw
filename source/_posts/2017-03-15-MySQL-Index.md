---
title: "MySQL索引笔记"
date: 2017-03-15 08:00:00
updated: 2017-04-05 16:11:32
tags: ["MySQL"]
---
# Mysql中的Btree与Hash索引比较

**B-Tree 索引特征 O(log(n))**  

B-Tree索引可以被用在像=,>,>=,<,<=和BETWEEN这些比较操作符上。而且还可以用于LIKE操作符，只要它的查询条件是一个不以通配符开头的常量。

** Hash 索引特征 O(1)**

Hash类型的索引有一些区别于以上所述的特征：
1. 它们只能用于对等比较，例如=和<=>操作符（但是快很多）。它们不能被用于像<这样的范围查询条件。假如系统只需要使用像“键值对”的这样的存储结构，尽量使用
hash类型索引。  
2. 优化器不能用hash索引来为ORDER BY操作符加速。（这类索引不能被用于搜索下一个次序的值）  
3. mysql不能判断出两个值之间有多少条数据（这需要使用范围查询操作符来决定使用哪个索引）。假如你将一个MyISAM表转为一个依靠hash索引的MEMOR
Y表，可能会影响一些语句（的性能）。  
4. 只有完整的键才能被用于搜索一行数据。（假如用B-tree索引，任何一个键的片段都可以用于查找。我觉得可能意味着带通配符LIKE操作符会不起作用）。

**索引、提交频率对InnoDB表写入速度的影响:**
1. 关于索引对写入速度的影响：
 1. 如果有自增列做主键，相对完全没索引的情况，写入速度约提升 3.11%；
 2. 如果有自增列做主键，并且二级索引，相对完全没索引的情况，写入速度约降低 27.37%；

因此，InnoDB表最好总是有一个自增列做主键。
2. 关于提交频率对写入速度的影响（以表中只有自增列做主键的场景，一次写入数据30万行数据为例）：
 1. 等待全部数据写入完成后，最后再执行commit提交的效率最高；
 2. 每10万行提交一次，相对一次性提交，约慢了1.17%；
 3. 每1万行提交一次，相对一次性提交，约慢了3.01%；
 4. 每1千行提交一次，相对一次性提交，约慢了23.38%；
 5. 每100行提交一次，相对一次性提交，约慢了24.44%；
 6. 每10行提交一次，相对一次性提交，约慢了92.78%；
 7. 每行提交一次，相对一次性提交，约慢了546.78%，也就是慢了5倍；


因此，最好是等待所有事务结束后再批量提交，而不是每执行完一个SQL就提交一次。
曾经有一次对比测试mysqldump启用extended-insert和未启用导出的SQL脚本，后者比前者慢了不止5倍。
重要：这个建议并不是绝对成立的，要看具体的场景。如果是一个高并发的在线业务，就需要尽快提交事务，避免锁范围被扩大。但如果是在非高并发的业务场景，尤其是做数据批量导入的场景下，就建议采用批量提交的方式。

下面是详细的测试案例过程，有兴趣的同学可以看看：
```sql
DROP TABLE IF EXISTS `mytab`;
CREATE TABLE `mytab` (
`id` int(10) unsigned NOT NULL AUTO_INCREMENT,
`c1` int(11) NOT NULL DEFAULT '0',
`c2` int(11) NOT NULL DEFAULT '0',
`c3` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
`c4` varchar(200) NOT NULL DEFAULT ”,
PRIMARY KEY (`id`)
) ENGINE=InnoDB;
DELIMITER $$$
DROP PROCEDURE IF EXISTS `insert_mytab`;
CREATE PROCEDURE `insert_mytab`(in rownum int, in commitrate int)
BEGIN
DECLARE i INT DEFAULT 0;
SET AUTOCOMMIT = 0;
WHILE i < rownum DO INSERT INTO mytab(c1, c2, c3,c4) VALUES( FLOOR(RAND()*rownum),FLOO(RAND()*rownum),NOW(), REPEAT(CHAR(ROUND(RAND()*255)),200)); SET i = i+1; /* 达到每COMMITRATE 频率时提交一次 */ IF (commitrate > 0) AND (i % commitrate = 0) THEN
COMMIT;
SELECT CONCAT('commitrate: ', commitrate, ' in ', I);
END IF;
END WHILE;
COMMIT;
SELECT 'ALL COMMIT;';
END; $$$
  
测试调用
call insert_mytab(300000, 1); — 每次一提交
 call insert_mytab(300000, 10); — 每10次一提交
 call insert_mytab(300000, 100); — 每100次一提交
 call insert_mytab(300000, 1000); — 每1千次一提交
 call insert_mytab(300000, 10000); — 每1万次提交
 call insert_mytab(300000, 100000); — 每10万次一提交
 call insert_mytab(300000, 0); — 一次性提交

```