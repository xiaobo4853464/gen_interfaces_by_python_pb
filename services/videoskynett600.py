# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoSkynetT600(BaseClient):
    SERVICE_NAME="video.skynet.t600"

    @grpc_proxy(path="video.skynet.t600.v1.T600/GetRoomUsers")
    def GetRoomUsers(self,):
        """"""
    @grpc_proxy(path="video.skynet.t600.v1.T600/GetStreamUsers")
    def GetStreamUsers(self,options:int=None):
        """"""
