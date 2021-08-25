# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DynamicServiceRevs(BaseClient):
    SERVICE_NAME = "dynamic.service.revs"

    @grpc_proxy(path="dynamic.service.revs.v1.Revs/FetchRevs")
    def FetchRevs(self, items: list = None):
        """"""
        
