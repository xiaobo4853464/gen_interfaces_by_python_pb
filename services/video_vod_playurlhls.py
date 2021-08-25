# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoVodPlayurlhls(BaseClient):
    SERVICE_NAME = "video.vod.playurlhls"

    @grpc_proxy(path="video.vod.playurlhls.PlayurlService/HlsScheduler")
    def HlsScheduler(self, cid: int = None, qn: int = None, uip: str = None, platform: str = None, fnver: int = None, fnval: int = None, mid: int = None, backup_num: int = None, preview: bool = None, force_host: int = None, is_sp: bool = None, net_type: dict = None, tf_type: dict = None, type: dict = None, business: dict = None):
        """"""
        
    @grpc_proxy(path="video.vod.playurlhls.PlayurlService/MasterScheduler")
    def MasterScheduler(self, cid: int = None, qn: int = None, uip: str = None, platform: str = None, fnver: int = None, fnval: int = None, mid: int = None, backup_num: int = None, preview: bool = None, force_host: int = None, is_sp: bool = None, net_type: dict = None, tf_type: dict = None, type: dict = None, business: dict = None):
        """"""
        
    @grpc_proxy(path="video.vod.playurlhls.PlayurlService/M3u8Scheduler")
    def M3u8Scheduler(self, cid: int = None, qn: int = None, uip: str = None, platform: str = None, fnver: int = None, fnval: int = None, mid: int = None, backup_num: int = None, preview: bool = None, force_host: int = None, is_sp: bool = None, net_type: dict = None, tf_type: dict = None, type: dict = None, business: dict = None):
        """"""
        
