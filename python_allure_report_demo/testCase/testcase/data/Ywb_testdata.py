# -*- coding:utf8 -*-

# ------------------------------ case:  account----------------------

testdata_YWB_login_userdata_001= {
            'phone':'18301212965',
            "passWord":"123qwe",
    }
# ------------------------------ case: ----------------------

testdata_YWB_salesmanquery_data_001= {
			"salesmanId":"s1520841050603Sbb9ed6f5-91f5-4989-b14b-3aeafd7031fc",
			"number":0,
    }
# ------------------------------ case: ----------------------
testdata_ywb_addorder_001={"accountId":"809","address":"北京市市辖区朝阳区还得大家庭教育基金会","area":"75.0","b_dosage":"","city":"市辖区","cityCode":"110100","county":"朝阳区","countyCode":"110105","cropId":"2","crops_highly":"1.5米及其以下","crops_name":"中稻","customer":"3","detailsAddress":"伊顿慧智双语幼儿园北京宝星校园","drugType":"0,1,2,6","farmlandArea":"75.0","farmlands":"F1528783867698","formalType":"1","guideName":"小八路","guidePhone":"14430036003","invoice":"2","latitude":"39.999785686240536","longitude":"116.48228599399104","discountRatio":"100","assembledAddress":"北京市北京市朝阳区朝阳区","isLongReserve":"1","imgNote":"[]","medicineService":"0","salesmanNote":"备注","settlementPrice":"10.0","assembledAddressLatitude":"39.92147","assembledAddressLongitude":"116.443108","days":"4","sprayingTimeStamp":"1532188800","medicineUrl":"","name":"小八路","orderNote":"业务宝，正式，拜访人","orderType":"1","order_money":"750","phone":"14430036003","province":"北京市","provinceCode":"110000","salesmanId":"s1520841050603Sbb9ed6f5-91f5-4989-b14b-3aeafd7031fc","spraying_time":"2018-08-02  至2018-08-05 ","teleAddress":"北京市朝阳区望京街道伊顿慧智双语幼儿园北京宝星校园","transitionsNumber":"0","type":"1","unit_price":"10.0","userType":"0","weatherId":"32e4cc07-f79a-4add-ac3e-56469992514a"}

# ------------------------------ case: ----------------------
#1,正式，2演示，3测试 4长预约单
#formalType=1
ywb_formalType_list={
	"normal":"1","yanshi":"2","test":"3","longreserve":"4",
}
#订单展示：期望时间
ywb_order_work_time={"spraying_time":"2018-08-01  至2018-08-01 ","days":"1",}
#详情-期望时间
ywb_order_sprayingTimeStamp={"sprayingTimeStamp":"1533744000",}
