# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DatacenterServiceAkuya(BaseClient):
    SERVICE_NAME="datacenter.service.akuya"

    @grpc_proxy(path="datacenter.service.akuya.v1.AkuyaService/GetTableInfo")
    def GetTableInfo(self,sql:str, business:str, version:str=None):
        """"""
    @grpc_proxy(path="datacenter.service.akuya.v1.AkuyaService/Query")
    def Query(self,sql:str, business:str, version:str=None):
        """"""
    @grpc_proxy(path="datacenter.service.akuya.v1.AkuyaService/Ping")
    def Ping(self,):
        """"""
