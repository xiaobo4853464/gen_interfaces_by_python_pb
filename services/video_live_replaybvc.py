# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoLiveReplaybvc(BaseClient):
    SERVICE_NAME = "video.live.replaybvc"

    @grpc_proxy(path="video.live.replaybvc.v1.Notify/QueryStreamStatus")
    def QueryStreamStatus(self, stream_name: str = None):
        """"""
        
    @grpc_proxy(path="video.live.replaybvc.v1.Notify/FragmentStarted")
    def FragmentStarted(self, stream_name: str = None, bucket: str = None, objkey: str = None, start_time: str = None, size: int = None, md5: str = None, duration: int = None, resolution_width: int = None, resolution_height: int = None):
        """"""
        
    @grpc_proxy(path="video.live.replaybvc.v1.Notify/FragmentCreated")
    def FragmentCreated(self, stream_name: str = None, bucket: str = None, objkey: str = None, start_time: str = None, size: int = None, md5: str = None, duration: int = None, resolution_width: int = None, resolution_height: int = None):
        """"""
        
    @grpc_proxy(path="video.live.replaybvc.v1.Notify/FragmentUploading")
    def FragmentUploading(self, stream_name: str = None, bucket: str = None, objkey: str = None, start_time: str = None, size: int = None, md5: str = None, duration: int = None, resolution_width: int = None, resolution_height: int = None):
        """"""
        
    @grpc_proxy(path="video.live.replaybvc.v1.Notify/FragmentUploaded")
    def FragmentUploaded(self, stream_name: str = None, bucket: str = None, objkey: str = None, start_time: str = None, size: int = None, md5: str = None, duration: int = None, resolution_width: int = None, resolution_height: int = None):
        """"""
        
