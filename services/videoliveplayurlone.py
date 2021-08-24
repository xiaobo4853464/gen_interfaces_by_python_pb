# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoLivePlayurlOne(BaseClient):
    SERVICE_NAME="video.live.playurl.one"

    @grpc_proxy(path="video.live.playurl.one.LivePlayUrlService/GrpcPlayurl")
    def GrpcPlayurl(self,cid:int=None, quality:int=None, stream_type:int=None, stream_len:int=None, uipstr:str=None, free_type:int=None, only_audio:bool=None, only_video:bool=None, https_url_req:bool=None, mask:int=None, uid:int=None, platform:str=None, build:int=None, p2p:int=None, net_status:int=None, device_name:str=None, req_biz:str=None, protocol:dict=None, format:dict=None, codec:dict=None, uuid:str=None, uip:int=None, uipv6:list=None, dolby:dict=None):
        """"""
