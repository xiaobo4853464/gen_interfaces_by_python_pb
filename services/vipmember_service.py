# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VipmemberService(BaseClient):
    SERVICE_NAME = "vipmember.service"

    @grpc_proxy(path="vipmember.service.v1.VipMember/Ping")
    def Ping(self, ):
        """"""
        
    @grpc_proxy(path="vipmember.service.v1.VipMember/IncrVipDuration")
    def IncrVipDuration(self, mid: int = None, days: int = None, idempotent_no: str = None, extra: list = None):
        """"""
        
    @grpc_proxy(path="vipmember.service.v1.VipMember/DecrVipDuration")
    def DecrVipDuration(self, mid: int = None, days: int = None, idempotent_no: str = None, extra: list = None):
        """"""
        
    @grpc_proxy(path="vipmember.service.v1.VipMember/SignAutoRenew")
    def SignAutoRenew(self, mid: int = None, pay_channel_id: int = None, idempotent_no: str = None):
        """"""
        
    @grpc_proxy(path="vipmember.service.v1.VipMember/CancelAutoRenew")
    def CancelAutoRenew(self, mid: int = None, idempotent_no: str = None):
        """"""
        
    @grpc_proxy(path="vipmember.service.v1.VipMember/BanVip")
    def BanVip(self, mid: int = None, operator: str = None, idempotent_no: str = None):
        """"""
        
    @grpc_proxy(path="vipmember.service.v1.VipMember/UnbanVip")
    def UnbanVip(self, mid: int = None, operator: str = None, idempotent_no: str = None):
        """"""
        
    @grpc_proxy(path="vipmember.service.v1.VipMember/FrozenVip")
    def FrozenVip(self, mid: int = None, reason: str = None, duration: int = None, idempotent_no: str = None):
        """"""
        
    @grpc_proxy(path="vipmember.service.v1.VipMember/UnfrozenVip")
    def UnfrozenVip(self, mid: int = None, logout: bool = None, idempotent_no: str = None):
        """"""
        
    @grpc_proxy(path="vipmember.service.v1.VipMember/VipUserInfo")
    def VipUserInfo(self, mid: int = None, bind_master: bool = None):
        """"""
        
    @grpc_proxy(path="vipmember.service.v1.VipMember/StreamVipUserInfos")
    def StreamVipUserInfos(self, filter: list = None):
        """"""
        
    @grpc_proxy(path="vipmember.service.v1.VipMember/VipChangeHistory")
    def VipChangeHistory(self, idempotent_no: str = None):
        """"""
        
    @grpc_proxy(path="vipmember.service.v1.VipMember/VipChangeHistories")
    def VipChangeHistories(self, mid: int = None, pn: int = None, ps: int = None):
        """"""
        
