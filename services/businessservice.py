# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class BusinessService(BaseClient):
    SERVICE_NAME="business.service"

    @grpc_proxy(path="business.service.Biz/GetBusiness")
    def GetBusiness(self,app_key:str=None):
        """"""
    @grpc_proxy(path="business.service.Biz/GetBusinessById")
    def GetBusinessById(self,id:int=None):
        """"""
    @grpc_proxy(path="business.service.Biz/ListBusinesses")
    def ListBusinesses(self,domain:str=None):
        """"""
    @grpc_proxy(path="business.service.Biz/MatchBusinessWhiteList")
    def MatchBusinessWhiteList(self,business_id:int=None, mid:int=None):
        """"""
    @grpc_proxy(path="business.service.Biz/WhitelistedMidsByBizId")
    def WhitelistedMidsByBizId(self,biz_id:int=None):
        """"""
