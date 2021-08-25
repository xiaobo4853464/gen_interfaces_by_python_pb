# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class ControlService(BaseClient):
    SERVICE_NAME = "control.service"

    @grpc_proxy(path="control.service.v1.Control/VipOnlyVideoPlay")
    def VipOnlyVideoPlay(self, mid: int = None, buvid: str = None):
        """"""
        
