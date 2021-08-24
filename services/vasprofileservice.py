# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VasProfileService(BaseClient):
    SERVICE_NAME="vas.profile.service"

    @grpc_proxy(path="vas.profile.service.v1.VasProfile/ExportGroupData")
    def ExportGroupData(self,id:int, operator:str):
        """"""
    @grpc_proxy(path="vas.profile.service.v1.VasProfile/ExportTaskState")
    def ExportTaskState(self,task_id:int=None):
        """"""
    @grpc_proxy(path="vas.profile.service.v1.VasProfile/ExportExpGroupData")
    def ExportExpGroupData(self,exp_group_id:int, operator:str):
        """"""
    @grpc_proxy(path="vas.profile.service.v1.VasProfile/VerifyCrowdConds")
    def VerifyCrowdConds(self,mid:int=None, buvid:str=None, conds:list=None):
        """"""
