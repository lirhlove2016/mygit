#!/usr/bin/env python
# -*- coding:utf-8 -*-


import jenkins
from time import sleep

import os
import sys
import time
import re

import jenkinsproject_name as jenkinsjob
import readtxt  

#filename=jenkinsjob.readtxt_fliename
filename=os.getcwd()+'/data.txt'

#jenkins_url
jenkins_server_url=jenkinsjob.DICT__NTGJ_JENKINS_SERVER['URL']
#user
username=jenkinsjob.DICT__NTGJ_JENKINS_SERVER['USERNAME']
password=jenkinsjob.DICT__NTGJ_JENKINS_SERVER['PASSWORD']

#username='fronter', password='fronter123'



#封装函数
def build_jenkins_job(jenkins_server_url,username,password,params):
    server=jenkins.Jenkins(jenkins_server_url, username=username, password=password,timeout=5)

    jenkinsProjectName=params['Job_name']
    param_name=params['param_name']
    param_value=params['param_value']

    print(params)

    nextBuildNumber = server.get_job_info(jenkinsProjectName)['nextBuildNumber']

    #buildParam="1"
    buildParam=param_value
        
    server.build_job(jenkinsProjectName, {param_name:param_value})

    print("正在触发构建项目：%s:Branch %s ，请稍等。。。"%(jenkinsProjectName,buildParam))
    # wait 10 seconds to make sure jenkins is triggered
    sleep(10)

    # Get jenkins is building
    building = server.get_build_info(jenkinsProjectName,nextBuildNumber)['building']

    if building:
        print('---------------building  start------------------------')

    while building:
        try:
            sleep(1)
            building = server.get_build_info(jenkinsProjectName,nextBuildNumber)['building']
            sys.stdout.write("*")
            sys.stdout.flush()

        except Exception as e:
            building = False
            print("ERROR: build Fail")      
            
    else:
            print("")
                  
            #获取job名为job_name的job的最后次构建号
            lastBuildNumber=server.get_job_info(jenkinsProjectName)['lastCompletedBuild']['number']

            #获取job名为job_name的job的某次构建的执行结果状态
            result=server.get_build_info(jenkinsProjectName,lastBuildNumber)['result']
            print("%s job  bulid_number of %s the result: %s " % (jenkinsProjectName,lastBuildNumber,result))

            if "SUCCESS" in result:
                print('项目：%s :Branch %s,BUILD SUCCESSFUL'%(jenkinsProjectName,buildParam))
            elif "FAILURE" in result:
                # get build console output log
                info = server.get_build_console_output(jenkinsProjectName,nextBuildNumber)
                print("-------------Fail : build_console_output-------------\n")
                print(info)
            return result
                  

#单独调用
#NTGJ_JENKINS
#param={'Job_name':"Android_Business","param_name":"Branch","param_value":"origin/dev_2.0.38"}          
#result=build_jenkins_job(jenkins_server_url,username,password,param)

#单独执行：调用txt文件，英文状态下
#step:1-选择打包环境
env=readtxt.get_env_version()


#step:2,打包版本（txt文件）
#格式data.txt,格式：Android_Business：origin/dev_2.0.38


filename1=r"E:\mysoft\myworksapce\NTGJ_jenkins_job_demo_py\data.txt"
res=readtxt.read_from_txt(filename1)
readtxt.print_info(res)

#
'''
#step:3 打包
for i  in range(len(res)):
    job_result={}
    param={}
    param['Job_name']=res[i]['job_name']
    param['param_name']='Branch'
    param['param_value']=res[i]['param_value']

    
    if env=='4':
        if param['Job_name'] in ['Android_Harvest','Android_pilot']::
            param['channel']='all'

    elif env=='1':
        if param['Job_name'] in ['Android_Harvest','Android_pilot']::
            param['channel']='inner'
        
        
    #判断打包版本
    if env=='1' and 's_' in res[i]['param_value']:
        print('现在是测试环境，不能打包s_,t_,r_版本')
        
        job_result[param['Job_name']]='version error'
        continue
    elif env=='2' and ['dev_','t','r']  in res[i]['param_value']:
        
        print('现在是预发布试环境，不能打包dev_,t_,r_版本')
        job_result[param['Job_name']]='version error'
        continue
    elif env=='4' and  ['dev','b_','s_'] in es[i]['param_value']:             
        job_result[param['Job_name']]='version error'
        print('现在是上线环境，只能打t_,r_版本')
        continue
    elif env=='3' and ['dev','b'] in es[i]['param_value']:
        print('现在是打包上线版本号，不能从s_打包')        
        job_result[param['Job_name']]='version error'
        continue
    else:               
        result=build_jenkins_job(jenkins_server_url,username,password,param)
        job_result[param['Job_name']]=result

print(job_result)

'''

'''
#单独执行一个：方法一：直接给参数
#样例：param={'Job_name':"Android_Business","param_name":"Branch","param_value":"origin/dev_2.0.38"}  

#2多次调用,参数
param=[{'Job_name':"jmeter_copy","param_name":"env","param_value":"1"},
        {'Job_name':"jmeter_copy","param_name":"env","param_value":"1"}]
for p in param:
    print(p)
    result=build_jenkins_job(jenkins_server_url,username,password,p)
    print("Build result: %s " % (result))
    
'''    
