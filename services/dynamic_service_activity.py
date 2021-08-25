# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DynamicServiceActivity(BaseClient):
    SERVICE_NAME = "dynamic.service.activity"

    @grpc_proxy(path="dynamic.service.activity.v1.ActPromoRPC/DynamicAttachedPromo")
    def DynamicAttachedPromo(self, dynamics: list = None):
        """"""
        
