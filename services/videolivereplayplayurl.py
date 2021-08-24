# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoLiveReplayplayurl(BaseClient):
    SERVICE_NAME="video.live.replayplayurl"

    @grpc_proxy(path="video.live.replayplayurl.v1.PlayurlService/Query")
    def Query(self,uip:str=None, expire:int=None, req:list=None, force_host:int=None, platform:str=None, mid:int=None, backup_num:int=None, qn:int=None, download:int=None):
        """"""
