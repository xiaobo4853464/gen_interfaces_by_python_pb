# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DynamicServiceExtendService(BaseClient):
    SERVICE_NAME = "dynamic.service.extend.service"

    @grpc_proxy(path="dynamic.service.extend.service.v1.Extend/Ping")
    def Ping(self, ):
        """"""
        
    @grpc_proxy(path="dynamic.service.extend.service.v1.Extend/BatchGet")
    def BatchGet(self, dyn_ids: int = None):
        """"""
        
    @grpc_proxy(path="dynamic.service.extend.service.v1.Extend/Create")
    def Create(self, dyn_id: int = None, extends: list = None):
        """"""
        
    @grpc_proxy(path="dynamic.service.extend.service.v1.Extend/Update")
    def Update(self, dyn_id: int = None, content: str = None, type: int = None):
        """"""
        
    @grpc_proxy(path="dynamic.service.extend.service.v1.Extend/BatchGetValid")
    def BatchGetValid(self, dyn_ids: int = None):
        """"""
        
