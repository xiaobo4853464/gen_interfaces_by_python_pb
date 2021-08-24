# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoLivePlayurl_tv(BaseClient):
    SERVICE_NAME="video.live.playurl_tv"

    @grpc_proxy(path="video.live.playurl_tv.LivePlayUrlService/Metrics")
    def Metrics(self,):
        """"""
    @grpc_proxy(path="video.live.playurl_tv.LivePlayUrlService/HttpAlive")
    def HttpAlive(self,):
        """"""
    @grpc_proxy(path="video.live.playurl_tv.LivePlayUrlService/GrpcPlayurl")
    def GrpcPlayurl(self,cid:int=None, quality:int=None, stream_type:int=None, stream_len:int=None, uipstr:str=None, ptype:int=None, https_url_req:bool=None, mask:int=None, req_biz:str=None, uid:int=None, appkey:str=None, platform:str=None, format:int=None, build:int=None, access_key:str=None, device_name:str=None, decrease_qn:bool=None, uuid:str=None, uip:int=None, uipv6:list=None):
        """"""
