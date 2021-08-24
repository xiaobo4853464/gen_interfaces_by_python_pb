# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class Api(BaseClient):
    SERVICE_NAME="api"

    @grpc_proxy(path="api.DehakaService/GetStreamBandWidth")
    def GetStreamBandWidth(self,CDN:str=None):
        """"""
    @grpc_proxy(path="api.DehakaService/GetBandWidthUsers")
    def GetBandWidthUsers(self,CDN:str=None):
        """"""
    @grpc_proxy(path="api.DehakaService/GetAllDownStreamURL")
    def GetAllDownStreamURL(self,startTime:int=None, endTime:int=None, roomId:int=None, streamName:str=None, trans:str=None, CDN:str=None):
        """"""
    @grpc_proxy(path="api.DehakaService/GetRoomUsers")
    def GetRoomUsers(self,):
        """"""
