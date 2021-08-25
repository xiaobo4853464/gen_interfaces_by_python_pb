# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VipinfoBckService(BaseClient):
    SERVICE_NAME = "vipinfo.bck.service"

    @grpc_proxy(path="vipinfo.bck.service.v1.VipInfo/Info")
    def Info(self, mid: int = None, buvid: str = None, with_control: bool = None):
        """"""
        
    @grpc_proxy(path="vipinfo.bck.service.v1.VipInfo/Infos")
    def Infos(self, mids: int = None):
        """"""
        
    @grpc_proxy(path="vipinfo.bck.service.v1.VipInfo/Ping")
    def Ping(self, ):
        """"""
        
    @grpc_proxy(path="vipinfo.bck.service.v1.VipInfo/CombineInfo")
    def CombineInfo(self, mid: int = None, buvid: str = None, with_control: bool = None):
        """"""
        
