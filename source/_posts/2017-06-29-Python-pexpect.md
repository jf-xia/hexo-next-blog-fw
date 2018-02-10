---
title: "pexpect命令行交互(Linux Only) - Python自动化运维"
date: 2017-06-29 08:00:00
updated: 2017-06-22 09:23:36
tags: ["Python"]
---
Pexpect是一个纯Python模块,可以用来和ssh、ftp、passwd、telnet等命令行命令进行交互使用

1. 安装Pip & Python 2.7 (or 3.6),并配置环境变量(默认安装会自动添加)
2. 设置Notepad++作为IDE开发工具:运行中输入命令cmd /k python "$(FULL_CURRENT_PATH)" & ECHO. & PAUSE & EXIT
3. 安装第三方库: pip install pexpect

Examples:
 
```python
 from pexpect import pxssh

 import getpass

y:

  s = pxssh.pxssh()

  hostname = raw_input('hostname: ')

  username = rawsername: ')

  password = getpass.getpass('password: ')

  s.login (hostname, username, password)

  s.sendline ('uptime')  # run a command

     s.prompt()             # match the prompt

  print s.before         # print everything before the prompt.

        s.sendline ('ls -l')

        s.prompt()

        print s.before

        s.sendline ('df')

        s.prompt()

        print s.before

        s.logout()

    except pxssh.ExceptionPxssh, e:

        print "pxssh failed on login."

        print str(e)

  

Hacker Example: 用Pxssh暴力破解SSH密码:http://book.51cto.com/art/201601/504626.htm

