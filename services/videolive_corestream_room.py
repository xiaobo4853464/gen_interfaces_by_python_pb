# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoLive_coreStream_room(BaseClient):
    SERVICE_NAME="video.live_core.stream_room"

    @grpc_proxy(path="video.live_core.stream_room.v1.StreamRoomServer/SetStreamRoom")
    def SetStreamRoom(self,StreamData:list=None, RoomId:int=None):
        """"""
    @grpc_proxy(path="video.live_core.stream_room.v1.StreamRoomServer/BatchSetStreamRoom")
    def BatchSetStreamRoom(self,StreamData:list=None, RoomId:int=None):
        """"""
    @grpc_proxy(path="video.live_core.stream_room.v1.StreamRoomServer/DelStream")
    def DelStream(self,StreamName:str=None):
        """"""
    @grpc_proxy(path="video.live_core.stream_room.v1.StreamRoomServer/DelRoom")
    def DelRoom(self,roomId:int=None):
        """"""
    @grpc_proxy(path="video.live_core.stream_room.v1.StreamRoomServer/GetStreamDataByRoomId")
    def GetStreamDataByRoomId(self,RoomId:int=None):
        """"""
    @grpc_proxy(path="video.live_core.stream_room.v1.StreamRoomServer/GetRoomByStreamName")
    def GetRoomByStreamName(self,StreamName:str=None):
        """"""
    @grpc_proxy(path="video.live_core.stream_room.v1.StreamRoomServer/GetStreamNamesByRoomId")
    def GetStreamNamesByRoomId(self,RoomId:int=None):
        """"""
    @grpc_proxy(path="video.live_core.stream_room.v1.StreamRoomServer/GetStreamDataByStreamName")
    def GetStreamDataByStreamName(self,StreamName:str=None):
        """"""
