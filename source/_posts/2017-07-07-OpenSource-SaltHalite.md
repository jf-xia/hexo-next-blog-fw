---
title: "saltstack web开源组件halite"
date: 2017-07-07 13:00:00
updated: 2017-07-06 13:09:20
tags: ["Python","运维","Saltstack"]
---
官方文挡: https://docs.saltstack.com/en/latest/topics/tutorials/halite.html
  
安装步骤:
1.克隆地址: Git clone https://github.com/saltstack/halite
2.生成index.html文件: ./halite/halite/genindex.py -C  
3.安装salt-api:  yum install salt-api
4.配置master文件 /etc/salt/master
 
 
 rest_cherrypy:
  host: 0.0.0.0
  port: 8080
  debug: true
ic: /ui/
 /ui/halite/h
    external_auth :                      -- 开启扩展认证系统
       pam :                              -- 使用 pam 作为扩展的认证系统
         coocla :                          -- 需要进行认证的系统用户名
           - . *                          -- 认证通过后可以使用任何模块
           - '@runner'                    -- 认证通过后可以使用 runner
5.配置Halite设置,需要在/etc/salt/master中配置halite的设置，halite支持CherryPy,Paste,Gevent
6.重启master $ /etc/init.d/salt-master restart
7.添加登陆用户 $ useradd admin  $ echo admin|passwd –stdin admin
启动 $ python server_bottle.py -d -C -l debug -s cherrypy
8.打开http://ip:8080/app，通过admin/admin登陆即可
  
效果图:
![blob.png](/uploads/ueditor/php/upload/image/20170706/1499304373.png)
