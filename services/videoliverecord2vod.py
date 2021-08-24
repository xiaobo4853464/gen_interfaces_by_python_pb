# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoLiveRecord2vod(BaseClient):
    SERVICE_NAME="video.live.record2vod"

    @grpc_proxy(path="video.live.record2vod.v1.Record2VOD/FragmentMerge")
    def FragmentMerge(self,room_id:int=None, live_key:str=None, mid:int=None, start_time:int=None, end_time:int=None):
        """"""
    @grpc_proxy(path="video.live.record2vod.v1.Record2VOD/GetFragmentsByLiveKey")
    def GetFragmentsByLiveKey(self,room_id:int=None, live_key:str=None, start_time:int=None, end_time:int=None):
        """"""
    @grpc_proxy(path="video.live.record2vod.v1.Record2VOD/GetDownloadByCID")
    def GetDownloadByCID(self,cid:int=None, uip:str=None):
        """"""
