# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoVodPlayurlcamp(BaseClient):
    SERVICE_NAME="video.vod.playurlcamp"

    @grpc_proxy(path="video.vod.playurlcamp.PlayurlService/ProtobufPlayurl")
    def ProtobufPlayurl(self,cid:int=None, qn:int=None, uip:str=None, platform:str=None, fnver:int=None, fnval:int=None, backup_num:int=None, force_host:int=None):
        """"""
