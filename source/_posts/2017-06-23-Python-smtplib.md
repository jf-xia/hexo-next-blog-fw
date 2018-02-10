---
title: "smtplib发送邮件 - Python自动化运维"
date: 2017-06-23 08:00:00
updated: 2017-06-19 17:18:04
tags: ["Python"]
---
  
1. 安装Pip & Python 2.7 (or 3.6),并配置环境变量(默认安装会自动添加)
2. 设置Notepad++作为IDE开发工具:运行中输入命令cmd /k python "$(FULL_CURRENT_PATH)" & ECHO. & PAUSE & EXIT
3. 安装第三方库: pip install smtplib

Examples:
 
```python
 # -- coding: utf-8 --


 import smtplib


 from email.mime.multipart import MIMEMultipart


 from email.mime.text import MIMEText


 from email.mime.image import MIMEImage








 HOST = "m.xxx.com"


 TO = "jianfeng.xia@xxx.com"


 EmailUser = "Task.system"


 EmailPass = "gta@2017"


 FROM = "Task.system@xxx.com"


BJECT = u"官网业务服务质量周报"





 def addimg(src,imgid):


        fp = open(src, 'rb')


        msgImage = MIMEImage(fp.read())


        fp.close()


        msgImage.add_header('Content-ID', imgid)


        return msgImage


    


    msg = MIMEMultipart('related')


    msgtext = MIMEText("<font color=red>官网业务周平均延时图表:<br><img src=\"cid:weekly\" border=\"1\"><br>详细内容见附件。</font>","html","utf-8")


    msg.attach(msgtext)


    #msg.attach(addimg("img/weekly.png","weekly"))


    


    #attach = MIMEText(open("doc/week_report.xlsx", "rb").read(), "base64", "utf-8")


    #attach["Content-Type"] = "application/octet-stream"


    #attach["Content-Disposition"] = "attachment; filename=\"业务服务质量周报(12周).xlsx\"".decode("utf-8").encode("gb18030")


    #msg.attach(attach)


    


    msg['Subject'] = SUBJECT


    msg['From']=FROM


    msg['To']=TO


    try:


        server = smtplib.SMTP()


        server.connect(HOST,"587")


        server.starttls()


        server.login(EmailUser, EmailPass)


        server.sendmail(FROM, TO, msg.as_string())


        server.quit()


        print "邮件发送成功！"


    except Exception, e:  


        print "失败："+str(e)

  

