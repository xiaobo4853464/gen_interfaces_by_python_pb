# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VipinfoService(BaseClient):
    SERVICE_NAME="vipinfo.service"

    @grpc_proxy(path="vipinfo.service.v1.VipInfo/Info")
    def Info(self,mid:int=None, buvid:str=None, with_control:bool=None):
        """"""
    @grpc_proxy(path="vipinfo.service.v1.VipInfo/Infos")
    def Infos(self,mids:int=None):
        """"""
    @grpc_proxy(path="vipinfo.service.v1.VipInfo/TimeInfo")
    def TimeInfo(self,mid:int=None):
        """"""
    @grpc_proxy(path="vipinfo.service.v1.VipInfo/CleanCache")
    def CleanCache(self,mid:int=None, ip:str=None, channel:str=None):
        """"""
    @grpc_proxy(path="vipinfo.service.v1.VipInfo/Label")
    def Label(self,mid:int=None):
        """"""
    @grpc_proxy(path="vipinfo.service.v1.VipInfo/CombineInfo")
    def CombineInfo(self,mid:int=None, buvid:str=None, with_control:bool=None):
        """"""
    @grpc_proxy(path="vipinfo.service.v1.VipInfo/CombineInfos")
    def CombineInfos(self,mids:int=None):
        """"""
