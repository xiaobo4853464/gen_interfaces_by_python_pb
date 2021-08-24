# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoLivePlayurlOversea(BaseClient):
    SERVICE_NAME="video.live.playurl.oversea"

    @grpc_proxy(path="video.live.playurl.oversea.LivePlayUrlService/GrpcMultiPlayurl")
    def GrpcMultiPlayurl(self,stream_list:str=None, protocol:dict=None, format:dict=None, codec:dict=None, quality:int=None, uipstr:str=None, https_url_req:bool=None, only_audio:bool=None, platform:str=None, uid:int=None, net_status:int=None, device_name:str=None, req_biz:str=None, dolby:dict=None, uuid:str=None, uip:int=None, uipv6:list=None):
        """"""
