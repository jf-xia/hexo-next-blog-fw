---
title: "dnspython - Python自动化运维"
date: 2017-06-19 08:00:00
updated: 2017-06-19 16:20:53
tags: ["Python"]
---
1. 安装Pip & Python 2.7 (or 3.6),并配置环境变量(默认安装会自动添加)
2. 设置Notepad++作为IDE开发工具:运行中输入命令cmd /k python "$(FULL_CURRENT_PATH)" & ECHO. & PAUSE & EXIT
3. 安装第三方库: pip install dnspython

Examples:
 
```python
 # -- coding: utf-8 --
 import dns.resolver
 
 domain = raw_input('Please input an domain: ')

 #!根据域名获取A地址
 A = dns.resolver.query(domain, 'A')
r i in A.response.answer:
     for j in i.items:
         print j.address

 #!根据域名获取MX地址
 MX = dns.resolver.query(domain, 'MX')
 MX:
        print 'MX preference =', i.preference, 'mail exchanger =', i.exchange
    
    #!根据域名获取NS地址
    ns = dns.resolver.query(domain, 'NS')
    for i in ns.response.answer:
         for j in i.items:
              print j.to_text()
    
    #!根据域名获取CNAME地址
    cname = dns.resolver.query(domain, 'CNAME')
    for i in cname.response.answer:
        for j in i.items:
            print j.to_text()
```
