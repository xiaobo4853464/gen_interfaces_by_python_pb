# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoLiveTvctrl(BaseClient):
    SERVICE_NAME = "video.live.tvctrl"

    @grpc_proxy(path="video.live.tvctrl.v1.TVControl/DelaySettings")
    def DelaySettings(self, room_ids: int = None, delay_seconds: int = None):
        """"""
        
    @grpc_proxy(path="video.live.tvctrl.v1.TVControl/Shutdown")
    def Shutdown(self, room_id: int = None):
        """"""
        
    @grpc_proxy(path="video.live.tvctrl.v1.TVControl/Recover")
    def Recover(self, room_id: int = None):
        """"""
        
    @grpc_proxy(path="video.live.tvctrl.v1.TVControl/GetDelayStreamList")
    def GetDelayStreamList(self, ):
        """"""
        
    @grpc_proxy(path="video.live.tvctrl.v1.TVControl/GetDelayRoomList")
    def GetDelayRoomList(self, ):
        """"""
        
