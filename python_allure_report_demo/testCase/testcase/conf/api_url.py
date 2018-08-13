# -*- coding:utf8 -*-

# ------------------------------ admin login url     ---------------------
API_URL = {
	"fsdlogin":"/flyHandApp/api/user/loginPassword",
    "fsdregister":"/flyHandApp/api/user/loginTest",
    "fsdusersetpassword":"/flyHandApp/api/user/loginAdd",
    "fsdcheckaccount":"/flyHandApp/api/user/checkAccountRegisted",
    "fsdsms":"/flyHandApp/api/user/getSmsCheckCode?phone=test",
    "addtools":"/flyHandApp/api/user/addTool/v1?userId=id&token=TOKEN",
    "syslogin":"/management/sys/login",
    "freezeflyaccount":"/management/user/updateFlyUserAccountState",
    "createflyuserteam":"/flyHandApp/api/team/createFlyUserTeam?userId=id&token=TOKEN",
    "addoperatecar":"/flyHandApp/api/reserve/addOperateCar?userId=id&token=TOKEN",
    "addplane":"/flyHandApp/api/user/addTool/v1?access_phone=PHONE&userId=id&token=TOKEN",
    "getplaneid":"/flyHandApp/api/user/oneToolList?access_phone=PHONE&userId=id&token=TOKEN",
    "updatexy":"/flyHandApp/api/user/updateXY?x=XVALUE&y=YVALUE&access_phone=PHONE&userId=id&token=TOKEN",
    "flyuserauth":"/flyHandApp/api/user/authInfoUpload/V1?userId=id&token=TOKEN",
    "getsmscheckcode":"/flyHandApp/api/user/getSmsCheckCode",
    "getcarid":"/flyHandApp/api/reserve/getOperateCarList?access_phone=PHONE&userId=id&token=TOKEN",
    "getclendar":"/flyHandApp/api/reserve/getReserveCalendar",
    "getreservecalendar":"/flyHandApp/api/reserve/getReserveCalendar?access_phone=PHONE&userId=id&token=TOKEN",
    "querycropprice":"/flyHandApp/api/reserve/queryCropPricing?access_phone=PHONE&userId=id&token=TOKEN",
    "sysflyauth":"/management/user/putFlyAuth",
    "addreserveorder":"/flyHandApp/api/reserve/addReserve?access_phone=PHONE&userId=id&token=TOKEN",
    "queryflyuser":"/management/user/queryFlyUserTeamList2",
    "sysflyuserauth":"/management/user/updateFlyUserAuthState", 
	"msgcenter":"/msgcenter/api/v2/getusermsg?userId=id&token=TOKEN",
	"orderPromptQuery":"/flyHandApp/api/order/orderPromptQuery?access_phone=PHONE&userId=id&token=TOKEN",
	"updateorderstate":"/flyHandApp/api/order/updateOrderState?access_phone=PHONE&userId=id&token=TOKEN",
	"updateorderreport":"/flyHandApp/api/order/updateOrderState?access_phone=PHONE&userId=id&token=TOKEN",
	"orderBoundQuery":"/flyHandApp/api/order/orderBoundQuery?access_phone=PHONE&userId=id&token=TOKEN",
	"getteaminfo":"/flyHandApp/api/team/getTeamManageInfo?access_phone=PHONE&userId=id&token=TOKEN",

    }


	
API_SYS_URL={
	"syslogin":"/management/sys/login",
	"checkflyauth":"/management/user/putFlyAuth",
	"checkflyuserauth":"/management/user/updateFlyUserAuthState",
	"queryflyuser":"/management/user/queryFlyUserTeamList2",
	"queryflyorderlist":"/management/order/queryFlyOrderList",
	"queryflyuser":"/management/user/queryAssignFlyUser",
	"publishorder":"/management/order/publishOrder",

}
API_YWB_URL={
	"addorder":"/businessTreasure/api/order/addOrderQuery?access_phone=PHONE&userId=id&token=TOKEN",
	"ywblogin":"/businessTreasure/api/user/loginP",
	"salesmanquery":"/businessTreasure/api/user/salesmanQuery?access_phone=PHONE&userId=id&token=TOKEN",
	"cropsAllQuery":"/businessTreasure/api/tool/cropsAllQuery?access_phone=PHONE&userId=id&token=TOKEN",
	"addorder":"/businessTreasure/api/order/addOrderQuery?access_phone=PHONE&userId=id&token=TOKEN",
	

}

API_MD_URL={
		"getwxuserinfo":"/wechatH5/api/tool/getWxUserInfo",
		"getframlist":"/wechatH5/api/farmer/getFarmerList",
		"wxaddorder":"/wechatH5/api/order/addOrder",
		"getcanuservoucherlist":"/wechatH5/api/voucher/getCanUseVoucherList",
		"getfullareamsg":"/wechatH5/api/fullarea/getFullAreaMsg",
		"getorderunitpricelist":"/wechatH5/api/order/getOrderUnitPriceList",
		"getchoosevoucherchangemoney":"/wechatH5/api/voucher/getChooseVoucherChangeMoney",
		"getbalance":"/wechatH5/api/wallet/getBalance",
		"savecouponcode":"/wechatH5/api/voucher/saveCouponCode",
		"getsmscheckcode":"/wechatH5/api/user/getSmsCheckCode",
		"orderprepay":"/wechatH5/api/wallet/orderPrePay",
		"orderinfo":"/wechatH5/api/order/getOrderInfo",
		"getcroplist":"/wechatH5/api/order/getCropList",
		"getcancelreason":"/wechatH5/api/order/getOrderCancelReason",
		"cancelcenter":"/wechatH5/api/order/cancelOrderCenter",
		"wxcancelorderdetail":"/wechatH5/api/order/wechatCancelOrderDetailFlow",
		"getprovincelist":"/wechatH5/api/order/queryProvinceList",
		
		
}



