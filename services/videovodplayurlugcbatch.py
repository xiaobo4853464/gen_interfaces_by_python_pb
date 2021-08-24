# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoVodPlayurlugcbatch(BaseClient):
    SERVICE_NAME="video.vod.playurlugcbatch"

    @grpc_proxy(path="video.vod.playurlugcbatch.PlayurlService/ProtobufPlayurl")
    def ProtobufPlayurl(self,keys:list=None, qn:int=None, uip:str=None, platform:str=None, fnver:int=None, fnval:int=None, mid:int=None, force_host:int=None, preview:bool=None, fourk:bool=None, flv_proj:bool=None, backup_num:int=None, net_type:dict=None, tf_type:dict=None, req_source:dict=None):
        """"""
    @grpc_proxy(path="video.vod.playurlugcbatch.PlayurlService/Playurl2")
    def Playurl2(self,keys:list=None, qn:int=None, uip:str=None, platform:str=None, fnver:int=None, fnval:int=None, mid:int=None, force_host:int=None, preview:bool=None, fourk:bool=None, flv_proj:bool=None, backup_num:int=None, net_type:dict=None, tf_type:dict=None, req_source:dict=None):
        """"""
