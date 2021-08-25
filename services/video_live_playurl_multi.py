# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoLivePlayurl_multi(BaseClient):
    SERVICE_NAME = "video.live.playurl_multi"

    @grpc_proxy(path="video.live.playurl_multi.LivePlayUrlService/GrpcMultiPlayurl")
    def GrpcMultiPlayurl(self, room_ids: int = None, quality: int = None, platform: str = None, uipstr: str = None, uid: int = None, https_url_req: bool = None, build: int = None, req_biz: str = None, device_name: str = None, mask: int = None, uipv6: list = None, uip: int = None, uuid: str = None, net_status: int = None):
        """"""
        
