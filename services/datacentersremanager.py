# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DatacenterSreManager(BaseClient):
    SERVICE_NAME="datacenter.sre.manager"

    @grpc_proxy(path="datacenter.sre.manager.v1.Manager/ListMenu")
    def ListMenu(self,):
        """"""
    @grpc_proxy(path="datacenter.sre.manager.v1.Manager/ListPurview")
    def ListPurview(self,value:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.manager.v1.Manager/AuthOpenApi")
    def AuthOpenApi(self,value:str=None):
        """"""
