# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoLiveReplay(BaseClient):
    SERVICE_NAME="video.live.replay"

    @grpc_proxy(path="video.live.replay.v1.Replay/FragmentStarted")
    def FragmentStarted(self,id:int=None, room_id:int=None, cdn:int=None, bucket:str=None, objkey:str=None, md5:str=None, size:int=None, start_time:str=None, duration:int=None, resolution_width:int=None, resolution_height:int=None, ctime:str=None, mtime:str=None, index:int=None, live_key:str=None, state:int=None, resource:str=None):
        """"""
    @grpc_proxy(path="video.live.replay.v1.Replay/FragmentCreated")
    def FragmentCreated(self,id:int=None, room_id:int=None, cdn:int=None, bucket:str=None, objkey:str=None, md5:str=None, size:int=None, start_time:str=None, duration:int=None, resolution_width:int=None, resolution_height:int=None, ctime:str=None, mtime:str=None, index:int=None, live_key:str=None, state:int=None, resource:str=None):
        """"""
    @grpc_proxy(path="video.live.replay.v1.Replay/FragmentUploading")
    def FragmentUploading(self,id:int=None, room_id:int=None, cdn:int=None, bucket:str=None, objkey:str=None, md5:str=None, size:int=None, start_time:str=None, duration:int=None, resolution_width:int=None, resolution_height:int=None, ctime:str=None, mtime:str=None, index:int=None, live_key:str=None, state:int=None, resource:str=None):
        """"""
    @grpc_proxy(path="video.live.replay.v1.Replay/FragmentUploaded")
    def FragmentUploaded(self,id:int=None, room_id:int=None, cdn:int=None, bucket:str=None, objkey:str=None, md5:str=None, size:int=None, start_time:str=None, duration:int=None, resolution_width:int=None, resolution_height:int=None, ctime:str=None, mtime:str=None, index:int=None, live_key:str=None, state:int=None, resource:str=None):
        """"""
    @grpc_proxy(path="video.live.replay.v1.Replay/Query")
    def Query(self,room_id:int=None, start_time:str=None, end_time:str=None):
        """"""
    @grpc_proxy(path="video.live.replay.v1.Replay/QueryByLiveKey")
    def QueryByLiveKey(self,room_id:int=None, live_key:str=None):
        """"""
    @grpc_proxy(path="video.live.replay.v1.Replay/FragmentMerge")
    def FragmentMerge(self,room_id:int=None, live_key:str=None, mid:int=None):
        """"""
    @grpc_proxy(path="video.live.replay.v1.Replay/StockFragmentMerge")
    def StockFragmentMerge(self,room_id:int=None, live_key:str=None, start_time:str=None, end_time:str=None):
        """"""
    @grpc_proxy(path="video.live.replay.v1.Replay/FragmentRescue")
    def FragmentRescue(self,live_key:str=None, bucket:str=None, objkey:str=None):
        """"""
    @grpc_proxy(path="video.live.replay.v1.Replay/GetFragmentsByLiveKey")
    def GetFragmentsByLiveKey(self,room_id:int=None, live_key:str=None):
        """"""
    @grpc_proxy(path="video.live.replay.v1.Replay/FragmentMergeBan")
    def FragmentMergeBan(self,):
        """"""
