# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DynamicServiceFeed(BaseClient):
    SERVICE_NAME="dynamic.service.feed"

    @grpc_proxy(path="dynamic.service.feed.v1.Feed/UpdateNum")
    def UpdateNum(self,uid:int=None, offsets:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.v1.Feed/ClickEntrance")
    def ClickEntrance(self,icon_type:dict=None, show_uid:int=None):
        """"""
