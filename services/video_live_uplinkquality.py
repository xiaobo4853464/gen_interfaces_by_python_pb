# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoLiveUplinkquality(BaseClient):
    SERVICE_NAME = "video.live.uplinkquality"

    @grpc_proxy(path="video.live.uplinkquality.v1.QualityUpLink/GetQualityData")
    def GetQualityData(self, streamName: str = None, key: str = None, build: int = None, platform: str = None, freeTab: str = None, roomId: int = None):
        """"""
        
    @grpc_proxy(path="video.live.uplinkquality.v1.QualityUpLink/QualityCallback")
    def QualityCallback(self, streamName: str = None, addrChanged: bool = None, reason: str = None, time: int = None, recommendAddr: str = None, platform: str = None, roomId: int = None, autoReport: bool = None, extensions: str = None, build: int = None):
        """"""
        
