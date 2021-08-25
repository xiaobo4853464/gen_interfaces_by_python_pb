# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DynamicServicePublish(BaseClient):
    SERVICE_NAME = "dynamic.service.publish"

    @grpc_proxy(path="dynamic.service.publish.v1.Publish/CreateTunnelDyn")
    def CreateTunnelDyn(self, uid: int = None, rid: int = None, tunnel_type: dict = None):
        """"""
        
    @grpc_proxy(path="dynamic.service.publish.v1.Publish/GetDynContent")
    def GetDynContent(self, uid: int = None, dyn_ids: int = None):
        """"""
        
