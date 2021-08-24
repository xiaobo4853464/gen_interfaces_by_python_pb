# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoVodPlayurlpgcbatch(BaseClient):
    SERVICE_NAME="video.vod.playurlpgcbatch"

    @grpc_proxy(path="video.vod.playurlpgcbatch.PlayurlService/ProtobufPlayurl")
    def ProtobufPlayurl(self,keys:list=None, platform:str=None, uip:str=None, force_host:int=None, fnver:int=None, fnval:int=None, qn:int=None, is_sp:bool=None, mid:int=None, fourk:bool=None, strategy:int=None, net_type:dict=None, tf_type:dict=None):
        """"""
