# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoLivePlayurl_one(BaseClient):
    SERVICE_NAME="video.live.playurl_one"

    @grpc_proxy(path="video.live.playurl_one.LivePlayUrlService/GrpcPlayurl")
    def GrpcPlayurl(self,cid:int=None, quality:int=None, stream_type:int=None, stream_len:int=None, uipstr:str=None, free_type:int=None, ptype:int=None, https_url_req:bool=None, mask:int=None, uid:int=None, appkey:str=None, platform:str=None, build:int=None, cookie_str:str=None, access_key:str=None, device_name:str=None, req_biz:str=None, format:int=None, uuid:str=None, uip:int=None, uipv6:list=None, net_status:int=None):
        """"""
