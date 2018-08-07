# -*- coding:utf8 -*-
# -------------------------- case: jenkins server----------------------
DICT__NTGJ_JENKINS_SERVER = {"URL": "http://10.0.1.4:8091/jenkins/login?from=%2Fjenkins%2F",
                        "USERNAME": "tester",
                        "PASSWORD": "tester123",
                        }

# -------------------------- case: read txt filename 配置文件路径---------------------- 
#filename=os.getcwd()+'/data.txt'
#readtxt_fliename="E:\\mysoft\\NTGJ_jenkins_job_demo_py\\data.txt"


# -------------------------- case: jenkins dev to b tag 开发提测---------------------- 

BUILD_NTGJ_DEV_TO_B_TAG=[{'Job_name':"FE_AdminWeb__QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"FE_FireRobberH5Client__QA","param_name":"Branch","param_value":"1"},
			{'Job_name': "FE_H5UtilPages__QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"FE_HarvestH5__QA","param_name":"Branch","param_value":"1"},
			{'Job_name': "FE_HarvestManagentSystem__QA","param_name":"Branch","param_value":"1"},
			{'Job_name': "FE_ManagementSystem__QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"FE_ManagementSystemOld__QA","param_name":"Branch","param_value":"1"},
			{'Job_name': "FE_PilotH5__QA","param_name":"Branch","param_value":"1"},
			{'Job_name': "FE_PilotUniversity__QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"FE_StatisticalSystem__QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"Android_Business","param_name":"Branch","param_value":"1"},
			{'Job_name':"Android_pilot","param_name":"Branch","param_value":"1"},
			{'Job_name':"Android_Harvest","param_name":"Branch","param_value":"1"},
			{'Job_name':"single_pilot2p_host_test","param_name":"Branch","param_value":"1"},
			{'Job_name':"single_pilot2p_slave_test","param_name":"Branch","param_value":"1"},
			{'Job_name':"single_backend_host_test","param_name":"Branch","param_value":"1"},
			{'Job_name':"single_backend_slave_test","param_name":"Branch","param_value":"1"},
			{'Job_name':"single_statistic2_host_test","param_name":"Branch","param_value":"1"},
			{'Job_name':"single_statistic2_slave_test","param_name":"Branch","param_value":"1"},
			{'Job_name':"single_statistic_host_test","param_name":"Branch","param_value":"1"},
			{'Job_name':"single_statistic_slave_test","param_name":"Branch","param_value":"1"},
			{'Job_name':"single_fgis_host_test","param_name":"Branch","param_value":"1"},
			]



#后端
DICT__NTGJ_SERVER_jenkinsProjectName_DEV_TO_TEST= {"pilot": "single_pilot2p_host_test",
                        "backend":"single_backend_host_test",
                        "reaper": "single_reaper_host_test",
                        "fgis": "single_fgis_host_test", #测试上只打一个
                        "statistic2": "single_statistic2_host_test",
						"statistic":"single_statistic_host_test",
                        }

#app
DICT__NTGJ_APP_jenkinsProjectName_DEV_TO_TEST= {"business": "Android_Business",
                        "pilot":"Android_pilot",
                        "havest": "Android_Harvest",
                        }
#前端
DICT__NTGJ_FE_jenkinsProjectName_DEV_TO_TEST = {
						  "FE_AW":"FE_AdminWeb__QA",
                        "FE_FRHC":"FE_FireRobberH5Client__QA",
                         "FE_HUP": "FE_H5UtilPages__QA",
						  "FE_HH":"FE_HarvestH5__QA",
                         "FE_HMS": "FE_HarvestManagentSystem__QA",
                          "FE_MS": "FE_ManagementSystem__QA",
						 "FE_MSO":"FE_ManagementSystemOld__QA",
                          "FE_PH": "FE_PilotH5__QA",
                          "FE_PU": "FE_PilotUniversity__QA",
						  "FE_SS":"FE_StatisticalSystem__QA",

                        }						


						
						
# -------------------case: jenkins build b to s tag-and s to t/r打预发布---------------------
#后端由开发打
#app
DICT__NTGJ_APP_jenkinsProjectName_BUILD_B_TO_ST= {"business": "Android_Business_createTag_QA",
                        "pilot":"Android_Pilot_createTag_QA",
                        "havest":"Android_Harvest_createTag_QA",
                        }
#前端
DICT__NTGJ_APP_jenkinsProjectName_BUILD_B_TO_ST = {
						 "FE_AW":"FE_AdminWeb_createTag_QA",
                       "FE_FRHC":"FE_FireRobberH5Client_createTag_QA",
                        "FE_HUP":"FE_H5UtilPages_createTag_QA",
						 "FE_HH":"FE_HarvestH5_createTag_QA",
                        "FE_HMS":"FE_HarvestManagentSystem_createTag_QA",
                         "FE_MS":"FE_ManagementSystem_createTag_QA",
						"FE_MSO":"FE_ManagementSystemOld_createTag_QA",
                         "FE_PH":"FE_PilotH5_createTag_QA",
                         "FE_PU":"FE_PilotUniversity_createTag_QA",
						 "FE_SS":"FE_StatisticalSystem_createTag_QA",
                        }						
						
BUILD_NTGJ_B_TO_S_OR_T_TAG=[{'Job_name':"FE_AdminWeb_createTag_QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"FE_FireRobberH5Client_createTag_QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"FE_H5UtilPages_createTag_QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"FE_HarvestH5_createTag_QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"FE_HarvestManagentSystem_createTag_QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"FE_ManagementSystem_createTag_QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"FE_ManagementSystemOld_createTag_QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"FE_PilotH5_createTag_QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"FE_PilotUniversity_createTag_QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"FE_StatisticalSystem_createTag_QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"Android_Business_createTag_QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"Android_Pilot_createTag_QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"Android_Harvest_createTag_QA","param_name":"Branch","param_value":"1"},
			]						
						
						

# -------------------------case: jenkins build t to online--正式上线--------------------
#开发打完后端包后
#app
DICT__NTGJ_APP_jenkinsProjectName_BUILD_T_TO_ONLINE = {"business": "Android_Business",
                        "pilot":"Android_pilot",
                        "havest": "Android_Harvest",
                        }
#前端
DICT__NTGJ_FE_jenkinsProjectName_BUILD_T_TO_ONLINE = {"FE_AW": "FE_AdminWeb__QA",
                        "FE_FRHC":"FE_FireRobberH5Client__QA",
                        "FE_HUP":"FE_H5UtilPages__QA",
						"FE_HH":"FE_HarvestH5__QA",
                        "FE_HMS":"FE_HarvestManagentSystem__QA",
                        "FE_MS":"FE_ManagementSystem__QA",
						"FE_MSO":"FE_ManagementSystemOld__QA",
                        "FE_PH":"FE_PilotH5__QA",
                        "FE_PU":"FE_PilotUniversity__QA",
						"FE_SS":"FE_StatisticalSystem__QA",
                        }						

BUILD_NTGJ_S_TO_ONLINE_TAG=[{'Job_name':"FE_AdminWeb__QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"FE_FireRobberH5Client__QA","param_name":"Branch","param_value":"1"},
			{'Job_name': "FE_H5UtilPages__QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"FE_HarvestH5__QA","param_name":"Branch","param_value":"1"},
			{'Job_name': "FE_HarvestManagentSystem__QA","param_name":"Branch","param_value":"1"},
			{'Job_name': "FE_ManagementSystem__QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"FE_ManagementSystemOld__QA","param_name":"Branch","param_value":"1"},
			{'Job_name': "FE_PilotH5__QA","param_name":"Branch","param_value":"1"},
			{'Job_name': "FE_PilotUniversity__QA","param_name":"Branch","param_value":"1"},
			{'Job_name':"FE_StatisticalSystem__QA","param_name":"Branch","param_value":"1"},
			]

# -------------------------case: jenkins :--------------------







