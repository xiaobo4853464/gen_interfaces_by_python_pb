# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DynamicServiceDraw(BaseClient):
    SERVICE_NAME = "dynamic.service.draw"

    @grpc_proxy(path="dynamic.service.draw.v1.Draw/Detail")
    def Detail(self, uid: int = None, ids: int = None, is_audit: int = None, meta_data: list = None):
        """"""
        
