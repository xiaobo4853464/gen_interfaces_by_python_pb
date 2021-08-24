# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoLiveStreamng(BaseClient):
    SERVICE_NAME="video.live.streamng"

    @grpc_proxy(path="video.live.streamng.v1.Stream/GetSingleScreeShot")
    def GetSingleScreeShot(self,room_id:int=None, start_time:str=None, end_time:str=None, channel:str=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/GetMultiScreenShot")
    def GetMultiScreenShot(self,room_ids:str=None, ts:int=None, channel:str=None, exact:bool=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/GetOriginScreenShotPic")
    def GetOriginScreenShotPic(self,room_ids:str=None, ts:int=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/GetPeriodPic")
    def GetPeriodPic(self,room_ids:int=None, start_time:str=None, end_time:str=None, channel:str=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/CreateOfficalStream")
    def CreateOfficalStream(self,stream_name:str=None, key:str=None, room_id:int=None, debug:str=None, uid:int=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/GetStreamInfo")
    def GetStreamInfo(self,room_id:int=None, stream_name:str=None, trid:str=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/GetMultiStreamInfo")
    def GetMultiStreamInfo(self,room_ids:int=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/ChangeSrc")
    def ChangeSrc(self,room_id:int=None, src:int=None, source:str=None, operate_name:str=None, reason:str=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/GetStreamLastTime")
    def GetStreamLastTime(self,room_id:int=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/GetStreamNameByRoomID")
    def GetStreamNameByRoomID(self,room_id:int=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/GetRoomIDByStreamName")
    def GetRoomIDByStreamName(self,stream_name:str=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/GetAdapterStreamByStreamName")
    def GetAdapterStreamByStreamName(self,stream_names:str=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/GetSrcByRoomID")
    def GetSrcByRoomID(self,room_id:int=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/GetLineListByRoomID")
    def GetLineListByRoomID(self,room_id:int=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/GetUpStreamRtmp")
    def GetUpStreamRtmp(self,room_id:int=None, free_flow:str=None, ip:str=None, area_id:int=None, attentions:int=None, uid:int=None, platform:str=None, port:str=None, build:int=None, bestIp:str=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/StreamCut")
    def StreamCut(self,room_id:int=None, cut_time:int=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/Ping")
    def Ping(self,):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/Close")
    def Close(self,):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/ClearStreamStatus")
    def ClearStreamStatus(self,room_id:int=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/CheckLiveStreamList")
    def CheckLiveStreamList(self,room_id:int=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/OpenNotify")
    def OpenNotify(self,ts:int=None, type:int=None, vendor:int=None, stream_name:str=None, sign:str=None, token:str=None, key:str=None, extras:str=None, open:bool=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/CreateTmpBackupStream")
    def CreateTmpBackupStream(self,room_id:int=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/DeleteTmpBackupStream")
    def DeleteTmpBackupStream(self,room_id:int=None, streams:str=None, cut:int=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/GetTmpBackupStreamRtmp")
    def GetTmpBackupStreamRtmp(self,room_id:int=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/CreateBackupStream")
    def CreateBackupStream(self,room_id:int=None):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/GetSrcMap")
    def GetSrcMap(self,):
        """"""
    @grpc_proxy(path="video.live.streamng.v1.Stream/GetSpeedAddr")
    def GetSpeedAddr(self,room_id:int=None, free_flow:str=None, ip:str=None, area_id:int=None, attentions:int=None, uid:int=None, platform:str=None, port:str=None, build:int=None, bestIp:str=None):
        """"""
