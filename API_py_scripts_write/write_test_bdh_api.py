# coding:utf-8
import json
import unittest
import time
import os

#import HTMLTestRunner
from common.readexcel import ExcelUtil
from common.Api_request import ApiRequest 
import conf

#from common import writeexcel

testxlsx = r"E:\mysoft\myworksapce\project\API_PY_scripts\case\myapidata.xlsx"
newfile=r"E:\mysoft\myworksapce\project\API_py_scripts_demo\case\result\result.xlsx"

testxlsx=conf.testxlsx
newfile=conf.newfile

class testAPI(unittest.TestCase):

    def setUp(self):
        self.suc_num=0
        self.datas=[]
        self.key_names=[]
        
    def test_bdh_api(self):               
        #获取数据
        data,key_names= ExcelUtil(testxlsx).dict_data()
        print(key_names)
        reals=[]
        count=len(data)
        print('count',count)
        suc_num=0
        for i in range(len(data)):
            print('----正在进行接口测试，开始第%d个请求---------------'%(i+1))
            datalist=[]    
            datalist=data[i]
            
            url="http://"+datalist['url'].strip()+ datalist['path'].strip()
            datas=datalist['params']
            method=datalist['method']
            headers={}
            headers['content-type']=datalist['headers']
            
            print(method,url,datas,headers)            
            my_request=ApiRequest(method,url,datas,headers)
            r=my_request.api_request()

            print('status_code',my_request.get_code())
            print('response',r.json())
            res=r.json()
            datalist['realresult']=r.json()
            #期望结果
            ex_result=datalist['expectedresult']
            
            if ex_result in res:
                print('{0}、{1}:测试成功。json数据为:{2}'.format(i + 1, datalist['casename'], r.json))
                datalist['result']='测试成功'
                suc_num=suc_num+1
            else:
                print('{0}、{1}:测试失败'.format(i + 1, datalist['casename']))
                datalist['result']='测试失败'

            #报错所有数据
            reals.append(datalist)
            #print(datalist)

        self.suc_num=suc_num
        self.datas=reals
        self.key_names=key_names
        #写入excel
        self.write_eccel_datas()
        
        return suc_num,reals,key_names

    def write_eccel_datas(self):
        write_excel(newfile,self.datas,self.key_names)
                      

    
if __name__=="__main__":
    unittest.main()
    

    
    