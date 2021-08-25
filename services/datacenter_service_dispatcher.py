# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DatacenterServiceDispatcher(BaseClient):
    SERVICE_NAME = "datacenter.service.dispatcher"

    @grpc_proxy(path="datacenter.service.dispatcher.DispatcherServer/SubmitSql")
    def SubmitSql(self, sql: str = None, params: list = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.dispatcher.DispatcherServer/FetchJobStatus")
    def FetchJobStatus(self, job_id: str = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.dispatcher.DispatcherServer/GetLog")
    def GetLog(self, job_id: str = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.dispatcher.DispatcherServer/GetResult")
    def GetResult(self, job_id: str = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.dispatcher.DispatcherServer/KillSql")
    def KillSql(self, job_id: str = None):
        """"""
        
