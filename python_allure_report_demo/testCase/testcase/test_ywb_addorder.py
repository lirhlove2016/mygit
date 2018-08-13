#-*- coding: utf-8 -*-
'''
后台派单给飞手 
3.x
'''

import unittest
import string
import json
import sys
import time
import datetime
import os

#from common import HTMLTestRunner
from common.basic_http import * 
from common.FSD_UserLogin import FSDLogin

from conf import server_config as device
from conf import api_url as api

from  data import Ywb_testdata as ywbuser


my_obj = FSDLogin()

'''
数据部分  start
------------------
'''
#ywb
ywblogindata=ywbuser.testdata_YWB_login_userdata_001
ywbsalesmanquerydata=ywbuser.testdata_YWB_salesmanquery_data_001
ywb_phone=ywblogindata['phone']
ywb_addorder_data=ywbuser.testdata_ywb_addorder_001


'''
数据部分  end
-----------
'''

class Test_addorder(unittest.TestCase):
    """ywb add order"""
	        
    def setUp(self):
        print('---------TEST START-------------')

    #case1--ywb add order
    def test_ywb_add_order(self):
        """ywb add order"""
        #step1:ywb login   
        ret=my_obj.ywb_login(ywblogindata)
        if ret[0]!=0:
            token=ret[2]
            accountId=ret[1]
        else:
            print('error')

        #2.ywb salsmanquery
        userid=accountId
        ret=my_obj.ywb_salesmanquery(userid,token,ywbsalesmanquerydata,ywb_phone)
        if ret!=1:
            print('error')
            return "error"


        #step3:ywb add order
        #拜访人，不带药，不开发票
        
        ret=my_obj.ywb_addorder(userid,token,ywb_phone,ywb_addorder_data)
        if ret[0]==1:
            order_numbe=ret[1]       
        else:
            print('error')


        
        
    def tearDown(self):
            print('-------TEST END----------------- ')


if __name__ == '__main__':
    #unittest.main()
    
    suite = unittest.TestSuite()
    suite.addTest(Test_addorder("test_ywb_add_order"))
    runner = unittest.TextTestRunner()
    runner.run(suite)


    
    

