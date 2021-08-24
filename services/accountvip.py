# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class AccountVip(BaseClient):
    SERVICE_NAME="account.vip"

    @grpc_proxy(path="account.vip.Vip/RegisterOpenID")
    def RegisterOpenID(self,mid:int=None, app_id:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/OpenBindByOutOpenID")
    def OpenBindByOutOpenID(self,open_id:str=None, out_open_id:str=None, app_id:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/UserInfoByOpenID")
    def UserInfoByOpenID(self,ip:str=None, open_id:str=None, app_id:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/BindInfoByMid")
    def BindInfoByMid(self,mid:int=None, app_id:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/BilibiliPrizeGrant")
    def BilibiliPrizeGrant(self,prize_key:str=None, unique_no:str=None, open_id:str=None, app_id:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/BilibiliVipGrant")
    def BilibiliVipGrant(self,open_id:str=None, out_open_id:str=None, out_order_no:str=None, duration:int=None, app_id:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/CreateAssociateOrder")
    def CreateAssociateOrder(self,mid:int=None, month:int=None, platform:str=None, mobi_app:str=None, device:str=None, appId:int=None, appSubId:str=None, orderType:int=None, dtype:int=None, returnUrl:str=None, coupon_token:str=None, bmid:int=None, panel_type:str=None, build:int=None, IP:str=None, pay_sdk_version:str=None, device_type:str=None, terminal_type:str=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/AssociatePanel")
    def AssociatePanel(self,mid:int=None, SortTp:int=None, IP:str=None, MobiApp:str=None, Device:str=None, Platform:str=None, Plat:int=None, PanelType:str=None, SubType:int=None, Month:int=None, Build:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/OpenAuthCallBack")
    def OpenAuthCallBack(self,mid:int=None, third_code:str=None, app_id:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/EleRedPackages")
    def EleRedPackages(self,):
        """"""
    @grpc_proxy(path="account.vip.Vip/EleSpecailFoods")
    def EleSpecailFoods(self,):
        """"""
    @grpc_proxy(path="account.vip.Vip/EleVipGrant")
    def EleVipGrant(self,order_no:str=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/FrozenVip")
    def FrozenVip(self,mid:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/UnfrozenVip")
    def UnfrozenVip(self,mid:int=None, logout:bool=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/VipUserPanel")
    def VipUserPanel(self,mid:int=None, sortTp:int=None, ip:str=None, mobiApp:str=None, device:str=None, platform:str=None, plat:int=None, panelType:str=None, subType:int=None, month:int=None, build:int=None, lang:str=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/CouponBySuitID")
    def CouponBySuitID(self,mid:int=None, sid:int=None, mobiApp:str=None, device:str=None, platform:str=None, panelType:str=None, build:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/ActivityInfo")
    def ActivityInfo(self,Token:str=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/AssembleInfo")
    def AssembleInfo(self,token:str=None, act_token:str=None, mid:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/OrderCreate")
    def OrderCreate(self,mid:int=None, month:int=None, platform:str=None, mobi_app:str=None, device:str=None, appId:int=None, appSubId:str=None, orderType:int=None, dtype:int=None, returnUrl:str=None, coupon_token:str=None, bmid:int=None, panel_type:str=None, build:int=None, IP:str=None, plan_id:str=None, pay_channel:str=None, pay_channel_id:str=None, real_channel:str=None, pay_contract_no:str=None, currency:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/AssembleHandle")
    def AssembleHandle(self,mid:int=None, actToken:str=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/WelfareList")
    def WelfareList(self,tid:int=None, recommend:int=None, ps:int=None, pn:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/WelfareTypeList")
    def WelfareTypeList(self,):
        """"""
    @grpc_proxy(path="account.vip.Vip/WelfareInfo")
    def WelfareInfo(self,id:int=None, mid:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/WelfareReceive")
    def WelfareReceive(self,wid:int=None, mid:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/MyWelfare")
    def MyWelfare(self,mid:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/TipsMine")
    def TipsMine(self,platform:str=None, mid:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/Price")
    def Price(self,mid:int=None, device:str=None, mobi_app:str=None, month:int=None, sub_type:int=None, coupon_token:str=None, platform:str=None, panel_type:str=None, build:int=None, ignore_auto_renew_status:int=None, app_id:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/Float")
    def Float(self,platform:str=None, mobi_app:str=None, device:str=None, panel_type:str=None, build:int=None, AppID:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/PrivilegeReceive")
    def PrivilegeReceive(self,mid:int=None, type:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/MyPrivilege")
    def MyPrivilege(self,mid:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/HasReceivedPrivilege")
    def HasReceivedPrivilege(self,mid:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/AutoRenewStatus")
    def AutoRenewStatus(self,mid:int=None, type:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/TipsRenew")
    def TipsRenew(self,position:int=None, mid:int=None, platform:int=None, build:str=None, partition:int=None, buvid:str=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/Rescision")
    def Rescision(self,mid:int=None, deviceType:int=None, payChannel:str=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/AutoRenewMng")
    def AutoRenewMng(self,mid:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/CodeOpen")
    def CodeOpen(self,batch_id:int=None, code:str=None, ts:int=None, ip:str=None, mid:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/ResourcesGetUsageTimeList")
    def ResourcesGetUsageTimeList(self,mid:int=None, batch_code_id:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/CodesUseTimeList")
    def CodesUseTimeList(self,mid:int=None, batch_code_ids:int=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/ReportOfflineDownloadNum")
    def ReportOfflineDownloadNum(self,mid:int=None, num:int=None, buvid:str=None, build:int=None, mobi_app:str=None, device:str=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/TipsVip")
    def TipsVip(self,position:int=None, mid:int=None, platform:str=None, mobi_app:str=None, build:str=None, biz_type:str=None, biz_partition:str=None, item_type:str=None, item_id:int=None, device:str=None, content_type:int=None, buvid:str=None):
        """"""
    @grpc_proxy(path="account.vip.Vip/OGVSendVip")
    def OGVSendVip(self,batch_token:str=None, appkey:str=None, mid:int=None, remark:str=None, buvid:str=None):
        """"""
