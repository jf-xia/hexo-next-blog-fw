---
title: "比较 WSGI、FastCGI 和 CGI 的异同"
date: 2017-08-14 15:00:00
updated: 2017-08-14 14:46:52
tags: ["PHP","Python"]
---
**扩展阅读：<https://www.biaodianfu.com/cgi-fastcgi-wsgi.html> **
**  
**
**CGI（Common Gateway Interface）**  
  
最初，CGI 是在 1993 年由美国国家超级电脑应用中心（NCSA）为 NCSA HTTPd Web 服务器开发的。
  
这个 Web 服务器使用了 UNIX shell 环境变量 来保存从 Web 服务器传递出去的参数，然后生成一个运行 CGI
的独立进程。CGI的第一个实现是 Perl 写的[1]。
  
效率低下：每一个连接 fork 一个进程处理。
功能十分有限：CGI只能收到一个请求，输出一个响应。很难在CGI体系去对Web请求的控制，例如：用户认证等。
正因为这些问题，在CGI诞生后的很长一段时间，各种Web
Server都还是采用API这种强绑定的方式去支持Web开发，其中Apache的mod_php就属于这种方式。所以后面就有大神提出了FastCGI标准。
  
**FastCGI（Fast Common Gateway Interface）**
  
FastCGI使用进程/线程池来处理一连串的请求。这些进程/线程由FastCGI服务器管理，而不是Web服务器。
当进来一个请求时，Web服务器把环境变量和这个页面请求通过一个Socket长连接传递给FastCGI进程。所以FastCGI有如下的优点：
  
性能：通过进程/线程池规避了CGI开辟新的进程的开销。
兼容：非常容易改造现有CGI标准的程序。
语言无关：FastCGI是一套标准，理论上讲只要能进行标准输出（stdout）的语言都可以作为FastCGI标准的Web后端。
下面是一个简单FastCGI后端的伪代码
void main(void)
{
  int count = 0;
  while(FCGI_Accept() >= 0) {
    printf(“Content-type: text/html\r\n”);
    printf(“\r\n”);
    printf(“Hello world!\r\n”);
    printf(“Request number %d.”, count++);
  }
  exit(0);
}
  
Web Server隔离：FastCGI后端和Web Server运行在不同的进程中，后端的任何故障不会导致Web Server挂掉。
专利：没有Apache mod_php之类的私有API的知识产权问题。
扩展：FastCGI后端和Web Server通过Socket进行通信，两者可以分布式部署并方便进行横向扩展。
所以FastCGI一推出就几乎获得了所有主流Web Server的支持，Apache、Lighttpd、IIS、Cherokee……
  
But，事情总是还有改进的余地的，FastCGI这套工作模式实际上没有什么太大缺陷，但是有些不安分的Python程序猿觉得，FastCGI标准下写异步的Web服务还是不太方便，如果能够收到请求后CGI端去处理，处理完毕后通过Callback回调来返回结果，那样岂不是很Coooool？！所以WSGI就被创造出来了：
  
**WSGI（Web Server Gateway Interface）**
  
Web服务器网关接口（Web Server Gateway Interface，缩写为WSGI）是为Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口。
  
当Web Server收到一个请求后，可以通过Socket把环境变量和一个Callback回调函数传给后端Web应用，Web应用在完成页面组装后通过Call back把内容返回给Web Server。这样做的优点有很多：
  
异步化，通过Callback将Web请求的工作拆解开，可以很方便的在一个线程空间里同时处理多个Web请求。
方便进行各种负载均衡和请求转发，不会造成后端Web应用阻塞。
Web开发有3P：Perl、Python、PHP。Perl是1987年发布的，Python是1989年，PHP是1995年。CGI标准提出的时候正是Perl如日中天的时候，所以CGI的提出当时也是主要为了解决Perl作为Web编程语言的需求。熟悉正则（regex）的程序员可能知道正则的事实标准叫做pcre（Perl兼容正则表达式，Perl Compatible RegularExpressions），这也从一个侧面体现了Perl作为一个古老的语言在当时对各种业界标准的影响。
  
  
作者：auxten
链接：https://zhuanlan.zhihu.com/p/20054757
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
  
