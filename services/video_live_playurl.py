# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoLivePlayurl(BaseClient):
    SERVICE_NAME = "video.live.playurl"

    @grpc_proxy(path="video.live.playurl.LivePlayUrlService/GrpcPlayurl")
    def GrpcPlayurl(self, cid: int = None, quality: int = None, uip: int = None, uipv6: list = None, uipstr: str = None, free_type: int = None, ptype: int = None, https_url_req: bool = None, bvc_path: str = None, wsTime: int = None, wsSecret: str = None, uid: int = None, appkey: str = None, platform: str = None, build: int = None, cookie_str: str = None, access_key: str = None, room_ids: int = None, req_biz: str = None, uuid: str = None, mask: int = None, device_name: str = None):
        """"""
        
    @grpc_proxy(path="video.live.playurl.LivePlayUrlService/GrpcMultiPlayurl")
    def GrpcMultiPlayurl(self, cid: int = None, quality: int = None, uip: int = None, uipv6: list = None, uipstr: str = None, free_type: int = None, ptype: int = None, https_url_req: bool = None, bvc_path: str = None, wsTime: int = None, wsSecret: str = None, uid: int = None, appkey: str = None, platform: str = None, build: int = None, cookie_str: str = None, access_key: str = None, room_ids: int = None, req_biz: str = None, uuid: str = None, mask: int = None, device_name: str = None):
        """"""
        
