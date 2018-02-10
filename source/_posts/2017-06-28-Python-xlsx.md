---
title: "xlsxWriter构造xlsx文件 - Python自动化运维"
date: 2017-06-28 08:00:00
updated: 2017-06-22 09:23:35
tags: ["Python"]
---
xlsxWriter支持多种excle功能；与excel完美兼容；写大文件，速度快且只占用很小的内存空间, 不支持读或者改现有的excel文件

1. 安装Pip & Python 2.7 (or 3.6),并配置环境变量(默认安装会自动添加)
2. 设置Notepad++作为IDE开发工具:运行中输入命令cmd /k python "$(FULL_CURRENT_PATH)" & ECHO. & PAUSE & EXIT
3. 安装第三方库: pip install xlsxwriter

Examples:
 
```python
 #coding: utf-8

 import xlsxwriter

 

 workbook = xlsxwriter.Workbook('E:\\python\\pyauto\\3\\XlsxWriter\\chart.xlsx')

 worksheet = workbook.add_worksheet()

 

art = workbook.add_chart({'type': 'column'})



tle = [u'业务名称',u'星期一',u'星期二',u'星期三',u'星期四',u'星期五',u'星期六',u'星期日',u'平均流量']

 buname= [u'业务官网',u'新闻中心',u'购物频道',u'体育频道',u'亲子频道']

 

 data = [

     [150,152,158,149,155,145,148],

     [89,88,95,93,98,100,99],

     [201,200,198,175,170,198,195],

     [75,77,78,78,74,70,79],

     [88,85,87,90,93,88,84],

 ]

 format=workbook.add_format()

 format.set_border(1)

 

rmat_title=workbook.add_format()

rmat_title.set_border(1)

itle.set_color('#cccccc')

itle.set_align('center')

 format_title.set_bold()



 format_ave=workbook.add_format()

 format_ave.set_border(1)

 format_ave.set_num_format('0.00')

 

    worksheet.write_row('A1',title,format_title)

    worksheet.write_column('A2', buname,format)

    worksheet.write_row('B2', data[0],format)

    worksheet.write_row('B3', data[1],format)

    worksheet.write_row('B4', data[2],format)

    worksheet.write_row('B5', data[3],format)

    worksheet.write_row('B6', data[4],format)

    # Insert an image.

    worksheet.insert_image('B25', 'E:\\python\\pyauto\\3\\XlsxWriter\\img\\python-logo.png')

    

    def chart_series(cur_row):

        worksheet.write_formula('I'+cur_row, \

         '=AVERAGE(B'+cur_row+':H'+cur_row+')',format_ave)

        chart.add_series({

            'categories': '=Sheet1!$B$1:$H$1',

            'values':     '=Sheet1!$B$'+cur_row+':$H$'+cur_row,

            'line':       {'color': 'black'},

            'name':	'=Sheet1!$A$'+cur_row,

        })

    

    for row in range(2, 7):

        chart_series(str(row))

    

    #chart.set_table()

    #chart.set_style(30)

    chart.set_size({'width': 577, 'height': 287})

    chart.set_title ({'name': u'业务流量周报图表'})

    chart.set_y_axis({'name': 'Mb/s'})

    

    worksheet.insert_chart('A8', chart)

    workbook.close()

  

