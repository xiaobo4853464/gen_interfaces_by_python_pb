# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoVodPlayurlhtml5(BaseClient):
    SERVICE_NAME = "video.vod.playurlhtml5"

    @grpc_proxy(path="video.vod.playurlhtml5.PlayurlService/ProtobufPlayurl")
    def ProtobufPlayurl(self, cid: int = None, qn: int = None, uip: str = None, platform: str = None, fnver: int = None, fnval: int = None, mid: int = None, backup_num: int = None, preview: bool = None, download: int = None, force_host: int = None, is_sp: bool = None, fourk: bool = None):
        """"""
        
