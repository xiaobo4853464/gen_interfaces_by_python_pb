# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class Livelivedm(BaseClient):
    SERVICE_NAME="live.livedm"
            
    @grpc_proxy(path="live.livedm.v1.DM/SendMsg")
    def SendMsg(self,uid:int, roomid:int, msg:str, rnd:str=None, ip:str=None, fontsize:int=None, mode:int=None, platform:str=None, msgtype:int=None, bubble:int=None, lancer:list=None, riskResult:int=None, not_ordinary_msgtype:int=None):
        """"""

    @grpc_proxy(path="live.livedm.v1.DM/GetHistory")
    def GetHistory(self,roomid:int):
        """"""

    @grpc_proxy(path="live.livedm.v1.DM/DelHistoryDMByRoomid")
    def DelHistoryDMByRoomid(self,roomid:int):
        """"""

    @grpc_proxy(path="live.livedm.v1.DM/AuditContentConfList")
    def AuditContentConfList(self,page:int=None, pagesize:int=None):
        """"""

    @grpc_proxy(path="live.livedm.v1.DM/CreateAuditContentConf")
    def CreateAuditContentConf(self,conf_title:str, start_time:str, end_time:str, conf_type:int=None, roomids:int=None):
        """"""

    @grpc_proxy(path="live.livedm.v1.DM/UdateAuditContentConf")
    def UdateAuditContentConf(self,id:int, conf_title:str, start_time:str, end_time:str, conf_type:int=None, roomids:int=None):
        """"""

    @grpc_proxy(path="live.livedm.v1.DM/DeleteAuditContentConf")
    def DeleteAuditContentConf(self,id:int):
        """"""

    @grpc_proxy(path="live.livedm.v1.DM/GetAuditContentConf")
    def GetAuditContentConf(self,id:int):
        """"""

    @grpc_proxy(path="live.livedm.v1.DM/SetAuditorNum")
    def SetAuditorNum(self,uname:str, id:int):
        """"""

    @grpc_proxy(path="live.livedm.v1.DM/GetAuditorNumAndDanmuNum")
    def GetAuditorNumAndDanmuNum(self,id:int):
        """"""

    @grpc_proxy(path="live.livedm.v1.DM/GetDanmuLists")
    def GetDanmuLists(self,id:int):
        """"""

    @grpc_proxy(path="live.livedm.v1.DM/SetDanmuSendList")
    def SetDanmuSendList(self,id:int, data:list):
        """"""

    @grpc_proxy(path="live.livedm.v1.DM/AuditBan")
    def AuditBan(self,uid:int, ban_days:int, operator:str, operate_reason:str, ban_evidence:str):
        """"""

    @grpc_proxy(path="live.livedm.v1.DM/AuditBanInfo")
    def AuditBanInfo(self,uid:int):
        """"""

        