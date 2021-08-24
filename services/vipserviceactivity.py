# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VipServiceActivity(BaseClient):
    SERVICE_NAME="vip.service.activity"

    @grpc_proxy(path="vip.service.activity.v1.VipActivity/Theme")
    def Theme(self,mid:int=None):
        """"""
    @grpc_proxy(path="vip.service.activity.v1.VipActivity/Themes")
    def Themes(self,mids:int=None):
        """"""
    @grpc_proxy(path="vip.service.activity.v1.VipActivity/ThemeBooking")
    def ThemeBooking(self,mid:int=None):
        """"""
    @grpc_proxy(path="vip.service.activity.v1.VipActivity/ThemeState")
    def ThemeState(self,mid:int=None, state:int=None):
        """"""
    @grpc_proxy(path="vip.service.activity.v1.VipActivity/CardBooking")
    def CardBooking(self,mid:int=None):
        """"""
    @grpc_proxy(path="vip.service.activity.v1.VipActivity/MyBooking")
    def MyBooking(self,mid:int=None):
        """"""
    @grpc_proxy(path="vip.service.activity.v1.VipActivity/TenYearVipBenefits")
    def TenYearVipBenefits(self,mid:int=None):
        """"""
    @grpc_proxy(path="vip.service.activity.v1.VipActivity/TenYearVipHonor")
    def TenYearVipHonor(self,mid:int=None):
        """"""
    @grpc_proxy(path="vip.service.activity.v1.VipActivity/TenYearVipBenefitsReceive")
    def TenYearVipBenefitsReceive(self,mid:int=None):
        """"""
    @grpc_proxy(path="vip.service.activity.v1.VipActivity/TenYearVipSizeSave")
    def TenYearVipSizeSave(self,mid:int=None, t_size:int=None):
        """"""
    @grpc_proxy(path="vip.service.activity.v1.VipActivity/TenYearVipAddressSave")
    def TenYearVipAddressSave(self,mid:int=None, address:str=None):
        """"""
    @grpc_proxy(path="vip.service.activity.v1.VipActivity/LotteryTimesCheck")
    def LotteryTimesCheck(self,mid:int=None, lottery_id:str=None):
        """"""
    @grpc_proxy(path="vip.service.activity.v1.VipActivity/MatchUserVipType")
    def MatchUserVipType(self,mid:int=None, match_type:int=None):
        """"""
    @grpc_proxy(path="vip.service.activity.v1.VipActivity/UserActivityOrderList")
    def UserActivityOrderList(self,act_token:str=None, mid:int=None):
        """"""
