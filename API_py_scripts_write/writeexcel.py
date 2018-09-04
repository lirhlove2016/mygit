#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlwt
from  xlrd import *
from xlutils.copy import copy
from case import test_bdh_api
from case.test_bdh_api import testAPI

def write_excel_m(old,newfile,datas,names):
    """修改数据"""
    rb =open_workbook(old)
    wb = copy(rb)
    sheet = wb.get_sheet(0)    
    #sheet.write(0,1,"new data")
    for i in range(len(names)):
            sheet.write(0,i,names[i])
    
    wb.save(newfile)
    print ("write finished")

def write_excel(filepath,datas,names):
    """写入数据"""
    f = xlwt.Workbook(encoding='utf-8', style_compression=0)             
    sheet= f.add_sheet(u'sheet1',cell_overwrite_ok=True) 
    n=[]
    for i in range(len(names)):
        sheet.write(0,i,names[i])
        n.append(names[i])
   
    #写入数据
    d=[]
    for i in range(len(datas)):
        value=datas[i]
        print('')
        print("正在写入第{0}行，数据{1}".format(i+1,value)) 
        for j in range(len(names)):         
            key=names[j]                 
            strValue=str(value[key])               
            sheet.write(i+1,j,strValue)       

        d.append(datas[i])                 
    f.save(filepath)
    print ("write finished")

if __name__=="__main__":
    #write_excel_m(old,newfile,datas,key_names)
    
    oldfile=r"E:\mysoft\myworksapce\project\API_py_scripts_demo\case\myapidata.xlsx"
    newfile=r"E:\mysoft\myworksapce\project\API_py_scripts_demo\case\result\result.xlsx"

    my_request=testAPI()
    suc_num,datas,key_names=my_request.test_bdh_api()
  
    write_excel(newfile,datas,key_names)
                   
