# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class Xcode(BaseClient):
    SERVICE_NAME="xcode"

    @grpc_proxy(path="xcode.XcodeService/GetStreamInfo")
    def GetStreamInfo(self,streamNames:str=None):
        """"""
    @grpc_proxy(path="xcode.XcodeService/BrushRoom")
    def BrushRoom(self,RoomIds:int=None):
        """"""
    @grpc_proxy(path="xcode.XcodeService/AddRoomConf")
    def AddRoomConf(self,Attach:str=None, OutPut:int=None, RoomId:int=None, Ttl:int=None):
        """"""
    @grpc_proxy(path="xcode.XcodeService/RoomConfStats")
    def RoomConfStats(self,RoomIds:int=None):
        """"""
    @grpc_proxy(path="xcode.XcodeService/RoomDefaultSuffix")
    def RoomDefaultSuffix(self,roomId:int=None):
        """"""
