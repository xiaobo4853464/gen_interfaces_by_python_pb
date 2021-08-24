# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoLivePlayurlBatch(BaseClient):
    SERVICE_NAME="video.live.playurl.batch"

    @grpc_proxy(path="video.live.playurl.batch.LivePlayUrlService/GrpcMultiPlayurl")
    def GrpcMultiPlayurl(self,room_ids:int=None, protocol:dict=None, format:dict=None, codec:dict=None, quality:int=None, uipstr:str=None, https_url_req:bool=None, mask:int=None, p2p:list=None, platform:str=None, uid:int=None, build:int=None, net_status:int=None, device_name:str=None, req_biz:str=None, dolby:dict=None, uuid:str=None, uip:int=None, uipv6:list=None):
        """"""
