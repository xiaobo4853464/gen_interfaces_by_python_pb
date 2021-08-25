# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoVodPlayurltv(BaseClient):
    SERVICE_NAME = "video.vod.playurltv"

    @grpc_proxy(path="video.vod.playurltv.PlayurlService/ProtobufPlayurl")
    def ProtobufPlayurl(self, cid: int = None, qn: int = None, uip: str = None, platform: str = None, fnver: int = None, fnval: int = None, mid: int = None, backup_num: int = None, preview: bool = None, download: int = None, force_host: int = None, is_sp: bool = None, fourk: bool = None, business: dict = None, watermark: bool = None):
        """"""
        
