# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoLivecoreStreamstar(BaseClient):
    SERVICE_NAME="video.livecore.streamstar"

    @grpc_proxy(path="video.livecore.streamstar.v1.StreamStar/Ping")
    def Ping(self,):
        """"""
    @grpc_proxy(path="video.livecore.streamstar.v1.StreamStar/SayHello")
    def SayHello(self,name:str):
        """"""
    @grpc_proxy(path="video.livecore.streamstar.v1.StreamStar/SayHelloURL")
    def SayHelloURL(self,name:str):
        """"""
    @grpc_proxy(path="video.livecore.streamstar.v1.StreamStar/UpsetStream")
    def UpsetStream(self,streamName:str=None, resetKey:int=None):
        """"""
    @grpc_proxy(path="video.livecore.streamstar.v1.StreamStar/PushStat")
    def PushStat(self,streamName:str=None):
        """"""
    @grpc_proxy(path="video.livecore.streamstar.v1.StreamStar/StreamPull")
    def StreamPull(self,streamName:str=None):
        """"""
