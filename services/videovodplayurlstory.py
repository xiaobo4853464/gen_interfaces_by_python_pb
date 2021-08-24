# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoVodPlayurlstory(BaseClient):
    SERVICE_NAME="video.vod.playurlstory"

    @grpc_proxy(path="video.vod.playurlstory.PlayurlService/Playurl")
    def Playurl(self,cids:int=None, uip:str=None, platform:str=None, mid:int=None, force_host:int=None, net_type:dict=None, tf_type:dict=None, backup_num:int=None):
        """"""
