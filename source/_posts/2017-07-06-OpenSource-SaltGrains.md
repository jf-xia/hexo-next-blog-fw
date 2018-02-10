---
title: "saltstack grains 示例"
date: 2017-07-06 08:00:00
updated: 2017-07-07 14:12:04
tags: ["Python","运维","Saltstack"]
---
GRAINS 组件是saltstack中非常重要的一个组件，其主要用于记录Minion的一些静态信息，如比：CPU、内存、磁盘、网络等。grains信息是每
次客户端启动后自动上报给master的，一旦这些静态信息发生改变需要重启minion 或者 重新同步下 grains。除此之外我们还可以自定义Grains的
一些信息。自定义的方法有三种：1、通过Minion配置文件定义；2、通过Grains相关模块定义；3、通过python脚本定义。
  
1.查看Grains相关的命令及用法(sys.list_functions or sys.doc) salt '*' sys.list_functions grains
![blob.png](/uploads/ueditor/php/upload/image/20170706/1499305756.png)
2.获取主机item信息(grains.ls or grains.items) salt '*' grains.items
![blob.png](/uploads/ueditor/php/upload/image/20170706/1499305728.png)
3.根据Grains的分组应用,筛选win系统 salt -G 'os:Windows'  test.ping
![blob.png](/uploads/ueditor/php/upload/image/20170706/1499305854.png)
4.通过Grains模块定义Grains
![blob.png](/uploads/ueditor/php/upload/image/20170706/1499305927.png)
5.使用自定义python脚本获取grains信息 - 获取主机系统时间
  
默认自定义脚本需要存放在master的/srv/salt/_grains目录下，这里使用mkdir -p创建即可。这里一个获取系统时间的脚本内容如下：
  
[root@saltmaster _grains]# cat get_time.py
#!/usr/bin/env python
# coding=utf-8
from datetime import datetime
def get_server_time():
 grains = {}
 grains['server_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
 return grains
使用sync_grains命令同步脚本到minion主机上去，并通过grains.item命令获取相关信息即可，如下：
  
[root@saltmaster _grains]# salt '*' saltutil.sync_grains
serverb.pod0.example.com:
 \- grains.get_time
irora200:
 \- grains.get_time
[root@saltmaster _grains]# salt '*' grains.item server_time
serverb.pod0.example.com:
 \----------
 server_time:
  2014-04-02 23:53:23
irora200:
 \----------
 server_time:
  2014-04-02 15:53:23
执行同步命令后，自定义脚本会上传到minion的/var/cache/salt/minion/extmods/grains目录下。
  
[root@irora200 grains]# ls
get_time.py  get_time.pyc
[root@irora200 grains]# pwd
/var/cache/salt/minion/extmods/grains
  
  
进阶: 使用grains搭建自动监控工具 <http://rfyiamcool.blog.51cto.com/1030776/1266437/>
