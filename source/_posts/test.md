---
title: test
date: 2017-06-22 13:56:26
updated: 2017-06-25 13:56:26
comments: true
tags: [ddd]
---
<p>scapy是python写的一个功能强大的交互式数据包处理程序，可用来发送、嗅探、解析和伪造网络数据包，常常被用到网络攻击和测试中。它可以代替hping,arpspoof.ARP SK,arping,p0f,甚至是部分nmap,Tcpdump和tshark。</p><p><br/></p><ol class=" list-paddingleft-2" style="list-style-type: decimal;"><li><p>安装Pip &amp; Python 2.7 (or 3.6), <strong>MS Visual C++ 9.0(https://www.microsoft.com/en-us/download/details.aspx?id=44266)</strong></p></li><li><p>设置vim作为IDE开发工具:运行中输入命令&nbsp;cmd /k python &quot;$(FULL_CURRENT_PATH)&quot; &amp; ECHO. &amp; PAUSE &amp; EXIT</p></li><li><p>安装第三方库:&nbsp;pip install scapy, 及相关插件https://github.com/zlorb/scapy.git</p></li></ol><p><br/></p><p>Examples:</p><pre class="brush:python;toolbar:false">#&nbsp;--&nbsp;coding:&nbsp;utf-8&nbsp;--
import&nbsp;os,sys,time,subprocess
import&nbsp;warnings,logging
warnings.filterwarnings(&quot;ignore&quot;,&nbsp;category=DeprecationWarning)
logging.getLogger(&quot;scapy.runtime&quot;).setLevel(logging.ERROR)
from&nbsp;scapy.all&nbsp;import&nbsp;traceroute
domains&nbsp;=&nbsp;raw_input(&#39;Please&nbsp;input&nbsp;one&nbsp;or&nbsp;more&nbsp;IP/domain:&nbsp;&#39;)
target&nbsp;=&nbsp;&nbsp;domains.split(&#39;&nbsp;&#39;)
dport&nbsp;=&nbsp;[80]
if&nbsp;len(target)&nbsp;&gt;=&nbsp;1&nbsp;and&nbsp;target[0]!=&#39;&#39;:
&nbsp;&nbsp;&nbsp;&nbsp;res,unans&nbsp;=&nbsp;traceroute(target,dport=dport,retry=-2)
&nbsp;&nbsp;&nbsp;&nbsp;res.graph(target=&quot;&gt;&nbsp;test.svg&quot;)
&nbsp;&nbsp;&nbsp;&nbsp;time.sleep(1)
&nbsp;&nbsp;&nbsp;&nbsp;subprocess.Popen(&quot;/usr/bin/convert&nbsp;test.svg&nbsp;test.png&quot;,&nbsp;shell=True)
else:
&nbsp;&nbsp;&nbsp;&nbsp;print&nbsp;&quot;IP/domain&nbsp;number&nbsp;of&nbsp;errors,exit&quot;</pre><p><br/></p><p><br/></p><p><br/></p>