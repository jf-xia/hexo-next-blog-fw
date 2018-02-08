---
title: "*Exchange 2010高可用部署"
date: 2017-03-07 08:00:00
updated: 2017-03-15 09:14:33
tags: ["开发"]
---
Exchange 2010 SP2 高可用性（一）部署CAS/HUB服务器

首先来说一下我的环境，我的实验环境为单域环境，域名为非常经典的contoso.net。环境中会用到4台Exchange Server 2010
SP2服务器，我们用其中的2台来部署Exchange的CAS/HUB角色，通过Windows的负载均衡技术。...

Exchange 2010 SP2 高可用性（二）创建CAS服务器阵列

CAS服务器(客户端访问服务器)是面向客户端的一个门户，客户端不管是通过OWA、POP3、IMAP或者Outlook
Anywhere方式访问邮箱，都需要首先连接到CAS服务器上，因此CAS服务器非常的重要，为了减轻单台CAS服务器的负担和避免单点故障的

Exchange 2010 SP2 高可用性（三）部署邮箱服务器

邮箱服务器是Exchange的重要角色之一，它的主要作用是承载所有用户的邮箱，除此之外还有联盟邮箱、仲裁邮箱等，同样是很重要的，单台邮箱服务器一旦损坏，那我
们的工作就得停滞，数据也有可能会丢失，所以这里我们部署...

详情见http://www.exchangecn.com/exchange2010/20150627_4290.html

