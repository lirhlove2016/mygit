#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

"""
英文状态下的
数据格式：pilot2p:b_1.10.1_201807091703,commit:1012b1086a57680e9aca932646737344e25fe6cb

"""


Branch_allCommit=['pilot','reaper','fgis','statistic','statistic2']
Branch_type=['backend']
Branch_name=[]

#prerelease,预发布环境

jobnames_prerelease=[
            "Android_Business_createTag_QA",
            "Android_Harvest_createTag_QA",
            "Android_Pilot_createTag_QA",
            "FE_AdminWeb__QA",
            "FE_AdminWeb_createTag_QA",
            "FE_FireRobberH5Client__QA",
            "FE_FireRobberH5Client_createTag_QA",
            "FE_H5UtilPages__QA",
            "FE_H5UtilPages_createTag_QA",
            "FE_HarvestH5__QA",
            "FE_HarvestH5_createTag_QA",
            "FE_HarvestManagentSystem__QA",
            "FE_HarvestManagentSystem_createTag_QA",
            "FE_ManagementSystem__QA",
            "FE_ManagementSystem_createTag_QA",
            "FE_ManagementSystemOld__QA",
            "FE_ManagementSystemOld_createTag_QA",
            "FE_PilotH5__QA",
            "FE_PilotH5_createTag_QA",
            "FE_PilotUniversity__QA",
            "FE_PilotUniversity_createTag_QA",
            "FE_StatisticalSystem__QA"
            "FE_StatisticalSystem_createTag_QA",
            ]

#ceshi
jobnames_ceshi=[
    "single_backend_host_test",
    "single_backend_slave_test",
    "project single_pilot2p_host_test",
    "project single_pilot2p_slave_test",
    "single_reaper_host_test",
    "single_reaper_slave_test",
    "single_fgis_host_test",	
    "single_statistic2_host_test",	
    "single_statistic2_slave_test",	
    "single_statistic_host_test",
    "single_statistic_slave_test",
    "Android_Business",
    "Android_Harvest",
    "Android_pilot",
    "FE_FireRobberH5Client__QA",
    "FE_H5UtilPages__QA",
    "FE_AdminWeb__QA",
    "FE_HarvestH5__QA",
    "FE_HarvestManagentSystem__QA",
    "FE_ManagementSystem__QA",
    "FE_ManagementSystemOld__QA",
    "FE_PilotH5__QA",
    "FE_PilotUniversity__QA",
    "FE_StatisticalSystem__QA",
    ]

#3打药上线版本,只打前端
jobnames_release=[
            "Android_Business_createTag_QA",
            "Android_Harvest_createTag_QA",
            "Android_Pilot_createTag_QA",
            "FE_AdminWeb__QA",
            "FE_AdminWeb_createTag_QA",
            "FE_FireRobberH5Client__QA",
            "FE_FireRobberH5Client_createTag_QA",
            "FE_H5UtilPages__QA",
            "FE_H5UtilPages_createTag_QA",
            "FE_HarvestH5__QA",
            "FE_HarvestH5_createTag_QA",
            "FE_HarvestManagentSystem__QA",
            "FE_HarvestManagentSystem_createTag_QA",
            "FE_ManagementSystem__QA",
            "FE_ManagementSystem_createTag_QA",
            "FE_ManagementSystemOld__QA",
            "FE_ManagementSystemOld_createTag_QA",
            "FE_PilotH5__QA",
            "FE_PilotH5_createTag_QA",
            "FE_PilotUniversity__QA",
            "FE_PilotUniversity_createTag_QA",
            "FE_StatisticalSystem__QA"
            "FE_StatisticalSystem_createTag_QA",
            ]

#online
jobnames_online=[
    "Android_Business",  #不上传到应用市场
    "Android_Harvest",  #上传all
    "Android_pilot",    #上传all
    "FE_FireRobberH5Client__QA",
    "FE_H5UtilPages__QA",
    "FE_AdminWeb__QA",
    "FE_HarvestH5__QA",
    "FE_HarvestManagentSystem__QA",
    "FE_ManagementSystem__QA",
    "FE_ManagementSystemOld__QA",
    "FE_PilotH5__QA",
    "FE_PilotUniversity__QA",
    "FE_StatisticalSystem__QA",
    ]


#读取数据函数,返回list类型的训练数据集和测试数据集
def read_from_txt(filename):   

    datalist=[]  #保存所有的job


    with open(filename,encoding='UTF-8') as fr:
        lines2=fr.readlines()
        lines=[]

        for line in lines2:
            #去掉空行
            if line=='\n':
                line=line.strip('\n')
            else:
                lines.append(line)
        
        for line in lines:
          
            listdatas=line.strip().split(',') #去除空白和逗号“,”
            #print('line-----',line)

            jobnamedata={}   #保存一个job_name
            #print('len(listdatas)',len(listdatas))
           
            #每个项目存到一个字典里           
            if len(listdatas)>1:
                    
                    #提取jobname
                    list=listdatas[0].strip().split(':')
                   
                    #print(listdatas[0])
                    #print(listdatas[1])
                    
                    jobnamedata['job_name']=list[0]
                    jobnamedata['param_value']=list[1]
                    #提取commit
                    list2=listdatas[1].strip().split(':')

                    jobnamedata['commit']=list2[1]
                    
            elif len(listdatas)==1:
                    list=listdatas[0].strip().split(':')

                    jobnamedata['job_name']=list[0]
                    jobnamedata['param_value']=list[1]
                    jobnamedata['commit']=""

            
            datalist.append(jobnamedata)
            #print(datalist)                          
    return datalist



#打印信息
def print_info(jobname):   
    print('您将要打包的项目，如下：')
    print('--------------------------------------------------------------------')
    print('序号   项目   版本                         commit号      ')
    print('--------------------------------------------------------------------')

    res=jobname
    for i  in range(len(res)):
            if res[i]['commit']=="":
                print(i+1,"----",res[i]['job_name'],"： ",res[i]['param_value'],)
            else:
                print(i+1,"----",res[i]['job_name'],"：  ",res[i]['param_value'],"   commit：  ",res[i]['commit'])


    print('-------------------------------------------------------------------\n')


#获取打包的参数
def get_job_param_name(jobname):
    
    if jobname in Branch_type:
         param_name='type'
    elif jobname in Branch_allCommit:
         param_name='allCommit'
    else:
         param_name="Branch"
    
    return param_name

#打包环境
"""
env=1,test,(dev-b)开发提测-测试环境
env=2,release,b-s，测试-预发布环境
env=3,prerelease,s-t/r，预发布-上线版本
env=4,online,r/t-online，上线环境

"""
def get_env_version():
    print('您可以选择打包的环境：')
    print('--------------------------------------------------------------------')
    print('序号    所选环境        打包版本      ')
    print('--------------------------------------------------------------------')
    print('1       测试环境        开发提测—进行测试')
    print('2       预发布环境      测试—预发布')
    print('3       上线准备环境    预发布—上线版本')
    print('4       上线环境        上线')
    print('--------------------------------------------------------------------')
    env=input('请选择您将要打包的环境：')
    if env=='1' or  'ceshi':
        env='1'
        print('您选择的是1----测试环境\n')
    elif name=='2' or 'prerelease':
        env='2'
        print('您选择的是2----预发布环境\n')
    elif name=='3':
        env='3'
        print('您选择的是3----上线准备环境\n')
    elif env=='4':
        env='4'
        print('您选择的是4----上线环境\n')
        
    return env


#返回打包集合
def get_env_jobnames(env):
    if env=='1':
        return jobnames_ceshi
    elif env=='2':
        return jobnames_prerelease
    elif env=='3':
        return jobnames_release
    elif env=='4':
        return jobnames_online

#获取jobname
def get_jenkins_jobname(env,jobname):
    env=get_env_version()
    
    if env=='1':
        jobnames=jobnames_ceshi
        if 'pilot' in jobnaes:
            pass
        

    

if __name__=='__main__':
    
    filename=r"E:\mysoft\myworksapce\NTGJ_jenkins_job_demo_py\data.txt"	
		
    res=read_from_txt(filename)
    print_info(res)

    params=[]
    for i  in range(len(res)):
        
        job_name=get_job_param_name(res[i]['job_name'])
        res[i]['param_name']=job_name
        params.append(job_name)

    print(params)
    print('res',res)

    env=get_env_version()
    #print(env)


    '''
    f=open(filename,'r')
    s=[]
    lines=f.readlines()

    for line in lines:
        #print(line)
        if line=='\n':
            line=line.strip('\n')
        else:
            s.append(line)
    print(s)
    f.close()
     '''      
            
    



