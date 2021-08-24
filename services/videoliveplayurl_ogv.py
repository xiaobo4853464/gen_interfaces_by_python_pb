# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoLivePlayurl_ogv(BaseClient):
    SERVICE_NAME="video.live.playurl_ogv"

    @grpc_proxy(path="video.live.playurl_ogv.LivePlayUrlService/GrpcPlayurl")
    def GrpcPlayurl(self,cid:int=None, quality:int=None, stream_type:int=None, stream_len:int=None, uipstr:str=None, free_type:int=None, ptype:int=None, https_url_req:bool=None, format:int=None, uid:int=None, appkey:str=None, platform:str=None, build:int=None, cookie_str:str=None, access_key:str=None, device_name:str=None, req_biz:str=None, uuid:str=None, uip:int=None, uipv6:list=None):
        """"""
