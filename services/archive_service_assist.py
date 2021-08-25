# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class ArchiveServiceAssist(BaseClient):
    SERVICE_NAME = "archive.service.assist"

    @grpc_proxy(path="archive.service.assist.v1.Assist/Logs")
    def Logs(self, mid: int = None, assist_mid: int = None, stime: int = None, etime: int = None, pn: int = None, ps: int = None):
        """"""
        
    @grpc_proxy(path="archive.service.assist.v1.Assist/LogCnt")
    def LogCnt(self, mid: int = None, assist_mid: int = None, stime: int = None, etime: int = None):
        """"""
        
    @grpc_proxy(path="archive.service.assist.v1.Assist/AddLog")
    def AddLog(self, mid: int = None, assist_mid: int = None, tp: int = None, act: int = None, sub_id: int = None, obj_idstr: str = None, detail: str = None):
        """"""
        
    @grpc_proxy(path="archive.service.assist.v1.Assist/CancelLog")
    def CancelLog(self, mid: int = None, assist_mid: int = None, log_id: int = None):
        """"""
        
    @grpc_proxy(path="archive.service.assist.v1.Assist/LogInfo")
    def LogInfo(self, id: int = None, mid: int = None, assist_mid: int = None):
        """"""
        
    @grpc_proxy(path="archive.service.assist.v1.Assist/LogObj")
    def LogObj(self, mid: int = None, obj_id: int = None, tp: int = None, act: int = None):
        """"""
        
    @grpc_proxy(path="archive.service.assist.v1.Assist/AddAssist")
    def AddAssist(self, mid: int = None, assist_mid: int = None):
        """"""
        
    @grpc_proxy(path="archive.service.assist.v1.Assist/DelAssist")
    def DelAssist(self, mid: int = None, assist_mid: int = None):
        """"""
        
    @grpc_proxy(path="archive.service.assist.v1.Assist/Assists")
    def Assists(self, mid: int = None):
        """"""
        
    @grpc_proxy(path="archive.service.assist.v1.Assist/AssistsMidsTotal")
    def AssistsMidsTotal(self, mid: int = None, assmids: int = None):
        """"""
        
    @grpc_proxy(path="archive.service.assist.v1.Assist/Assist")
    def Assist(self, mid: int = None, assist_mid: int = None, tp: int = None):
        """"""
        
    @grpc_proxy(path="archive.service.assist.v1.Assist/AssistIDs")
    def AssistIDs(self, mid: int = None):
        """"""
        
    @grpc_proxy(path="archive.service.assist.v1.Assist/Exit")
    def Exit(self, mid: int = None, assist_mid: int = None):
        """"""
        
    @grpc_proxy(path="archive.service.assist.v1.Assist/AssistUps")
    def AssistUps(self, assist_mid: int = None, pn: int = None, ps: int = None):
        """"""
        
