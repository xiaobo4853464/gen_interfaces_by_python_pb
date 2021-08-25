# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoVodPlayurlbusinesssign(BaseClient):
    SERVICE_NAME = "video.vod.playurlbusinesssign"

    @grpc_proxy(path="video.vod.playurlbusinesssign.PlayurlService/Download")
    def Download(self, cid: int = None, qn: int = None, fnver: int = None, fnval: int = None, platform: str = None, uip: str = None, backup: int = None, mid: int = None, force_host: int = None, is_sign: bool = None, cdn: str = None, tag: str = None):
        """"""
        
    @grpc_proxy(path="video.vod.playurlbusinesssign.PlayurlService/DownloadForDialTest")
    def DownloadForDialTest(self, sid: int = None, objkey: str = None, type: str = None):
        """"""
        
