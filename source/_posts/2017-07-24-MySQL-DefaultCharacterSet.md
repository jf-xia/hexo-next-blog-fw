---
title: "mysql中通过my.cnf设置默认字符集utf-8"
date: 2017-07-24 08:00:00
updated: 2017-07-23 22:44:01
tags: ["MySQL"]
---
/etc/my.cnf

[client]

default-character-set=utf8

[mysql]

default-character-set=utf8

[mysqld]

init_connect='SET collation_connection = utf8_unicode_ci'

init_connect='SET NAMES utf8'

character-set-server=utf8

collation-server=utf8_unicode_ci

skip-character-set-client-handshake

*注意：在 mysqld 中使用 default-character-set 设置， mysql 启动会报错而无法启动。

关于utf8字符集，我们国内默认选择：utf8_general_ci而不是utf8_unicode_ci，

区别在于字符对比上

请看mysql上面的例子：

对与general来说 ß = s 是为true的

但是对于unicode来说 ß = ss 才是为true的，

其实他们的差别主要在德语和法语上，所以对于我们中国人来说，一般使用general，因为general更快

如果你对德语和法语的对比有更高的要求，才使用unicode，它比general更准确一些（按照德语和法语的标准来说，在对比或者排序上更准确）

看看这个文档：<http://dev.mysql.com/doc/refman/5.0/en/charset-unicode-sets.html>

另外还有utf8_bin_ci也是比较常用的哦，在字符对比时，unicode和general都不是大小写敏感的，所以如果要求大小写敏感的话，就使用bin

