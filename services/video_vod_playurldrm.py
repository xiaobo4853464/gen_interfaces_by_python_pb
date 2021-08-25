# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoVodPlayurldrm(BaseClient):
    SERVICE_NAME = "video.vod.playurldrm"

    @grpc_proxy(path="video.vod.playurldrm.PlayurlService/Scheduler")
    def Scheduler(self, cid: int = None, qn: int = None, uip: str = None, platform: str = None, mid: int = None, is_sp: bool = None, preview: bool = None, net_type: dict = None, tf_type: dict = None):
        """"""
        
    @grpc_proxy(path="video.vod.playurldrm.PlayurlService/File")
    def File(self, cid: int = None, qn: int = None, net_type: dict = None, tf_type: dict = None, ts: int = None, sign: str = None, uip: str = None, platform: str = None, mid: int = None, force_host: int = None):
        """"""
        
