# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DatacenterServiceDqc2(BaseClient):
    SERVICE_NAME = "datacenter.service.dqc2"

    @grpc_proxy(path="datacenter.service.dqc2.Dqc2BasicServer/createDqc")
    def createDqc(self, name: str = None, userName: str = None, userId: int = None, departmentName: str = None, departmentId: int = None, alarmRepeatCount: int = None, alarmType: list = None, alarmOwner: str = None, version: int = None, category: str = None, tableName: str = None, executeMode: int = None, filterCondition: str = None, partitionInfo: str = None, ruleList: list = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.dqc2.Dqc2BasicServer/queryShortDqc")
    def queryShortDqc(self, dqcId: int = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.dqc2.Dqc2BasicServer/queryShortDqcByJobId")
    def queryShortDqcByJobId(self, jobId: int = None):
        """"""
        
