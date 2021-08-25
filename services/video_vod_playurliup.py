# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoVodPlayurliup(BaseClient):
    SERVICE_NAME = "video.vod.playurliup"

    @grpc_proxy(path="video.vod.playurliup.PlayurlService/ProtobufPlayurl")
    def ProtobufPlayurl(self, resourceid: str = None, platform: str = None, uip: str = None, backup: int = None, mid: int = None, force_host: int = None):
        """"""
        
