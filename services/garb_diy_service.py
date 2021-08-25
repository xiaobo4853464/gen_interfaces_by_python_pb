# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class Garb_diy_service(BaseClient):
    SERVICE_NAME = "garb_diy_service"

    @grpc_proxy(path="garb_diy_service.v1.GarbDiy/GrantDiyPendantByBiz")
    def GrantDiyPendantByBiz(self, mid: int = None, addSecond: int = None, activityID: int = None, business: str = None, token: str = None):
        """"""
        
