# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DatacenterServiceDqc(BaseClient):
    SERVICE_NAME="datacenter.service.dqc"

    @grpc_proxy(path="datacenter.service.dqc.DqcExecutorService/BatchExecuteRules")
    def BatchExecuteRules(self,ruleIdList:list=None, reportId:int=None):
        """"""
    @grpc_proxy(path="datacenter.service.dqc.DqcExecutorService/BatchStopRules")
    def BatchStopRules(self,ruleIdList:list=None, reportId:int=None):
        """"""
