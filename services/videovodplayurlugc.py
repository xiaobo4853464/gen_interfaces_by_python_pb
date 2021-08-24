# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoVodPlayurlugc(BaseClient):
    SERVICE_NAME="video.vod.playurlugc"

    @grpc_proxy(path="video.vod.playurlugc.PlayurlService/ProtobufPlayurl")
    def ProtobufPlayurl(self,cid:int=None, qn:int=None, uip:str=None, platform:str=None, fnver:int=None, fnval:int=None, mid:int=None, backup_num:int=None, preview:bool=None, download:int=None, force_host:int=None, is_sp:bool=None, fourk:bool=None, flv_proj:bool=None, net_type:dict=None, tf_type:dict=None, cookie:str=None, pcdn_params:str=None, req_source:dict=None):
        """"""
    @grpc_proxy(path="video.vod.playurlugc.PlayurlService/Playurl2")
    def Playurl2(self,cid:int=None, qn:int=None, uip:str=None, platform:str=None, fnver:int=None, fnval:int=None, mid:int=None, backup_num:int=None, preview:bool=None, download:int=None, force_host:int=None, is_sp:bool=None, fourk:bool=None, flv_proj:bool=None, net_type:dict=None, tf_type:dict=None, cookie:str=None, pcdn_params:str=None, req_source:dict=None):
        """"""
