#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlwt
import xlrd
from case.test_badh_api import testAPI

my_request=testAPI()

oldfile=r"E:\mysoft\myworksapce\project\API_py_scripts\case\myapidata.xlsx"


rb=xlrd.open_workbook(oldfile)
wb=cppy(rb)
sheet=wb.get_sheet(0)


sucnum,datas,key_names=my_request.test_bdh_api()
print(suc_num,key_names)


book = xlwt.Workbook(encoding='utf-8', style_compression=0)
'''
Workbook类初始化时有encoding和style_compression参数
encoding:设置字符编码，一般要这样设置：w = Workbook(encoding='utf-8')，就可以在excel中输出中文了。
默认是ascii。当然要记得在文件头部添加：
style_compression:表示是否压缩，不常用。
'''


sheet = book.add_sheet('test', cell_overwrite_ok=True)

# 向表test中添加数据
sheet.write(0, 0, 'EnglishName')  # 其中的'0-行, 0-列'指定表中的单元，'EnglishName'是向该单元写入的内容
sheet.write(1, 0, 'Marcovaldo')

sheet.write(0, 1, txt1.decode('utf-8'))  # 此处需要将中文字符串解码成unicode码，否则会报错



# 最后，将以上操作保存到指定的Excel文件中
book.save(r'e:\test1.xls')  # 在字符串前加r，声明为raw字符串，这样就不会处理其中的转义了。否则，可能会报错
