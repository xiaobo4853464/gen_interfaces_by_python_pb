# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DynamicServiceIndex(BaseClient):
    SERVICE_NAME="dynamic.service.index"

    @grpc_proxy(path="dynamic.service.index.v1.Index/FetchDesc")
    def FetchDesc(self,dyn_ids:int=None):
        """"""
