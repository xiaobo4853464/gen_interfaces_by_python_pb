# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class PushServiceBroadcast(BaseClient):
    SERVICE_NAME = "push.service.broadcast"

    @grpc_proxy(path="push.service.broadcast.Zerg/ServerList")
    def ServerList(self, platform: str = None):
        """"""
        
