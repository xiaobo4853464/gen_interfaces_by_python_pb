# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DatacenterServiceArcherBypass(BaseClient):
    SERVICE_NAME="datacenter.service.archer.bypass"

    @grpc_proxy(path="datacenter.service.archer.bypass.v1.JobManager/createSingleJobProject")
    def createSingleJobProject(self,commonParas:list=None, command:str=None, commandType:int=None, requestParams:str=None, storeType:int=None, storeMeta:str=None, jobType:int=None, MaxRetryCount:int=None, jobStatus:int=None, jobName:str=None, jobDesc:str=None, noticeSwitch:int=None, createUserId:int=None, departmentId:int=None, periodType:int=None, period:str=None, noticeType:int=None, executeResultNotice:int=None, selfDependence:bool=None, expectCostTime:int=None, priority:int=None, checkStart:bool=None, slaReceivers:str=None, slaSecondReceivers:str=None, timeSegment:int=None, dispatchPeriodType:int=None, failureNoticeType:int=None, unInitNoticeType:int=None, startNoticeType:int=None, incompleteNoticeType:int=None, successNoticeType:int=None, exeTimoutNoticeType:int=None, expectFinishTime:str=None, expectStartTime:str=None, alarmEscalate:int=None, addRecommendedParents:bool=None, parentJobIds:int=None):
        """"""
    @grpc_proxy(path="datacenter.service.archer.bypass.v1.JobManager/update")
    def update(self,commonParas:list=None, command:str=None, commandType:int=None, requestParams:str=None, storeType:int=None, storeMeta:str=None, jobType:int=None, MaxRetryCount:int=None, jobStatus:int=None, jobName:str=None, jobDesc:str=None, noticeSwitch:int=None, createUserId:int=None, departmentId:int=None, periodType:int=None, period:str=None, noticeType:int=None, executeResultNotice:int=None, selfDependence:bool=None, expectCostTime:int=None, priority:int=None, checkStart:bool=None, slaReceivers:str=None, slaSecondReceivers:str=None, timeSegment:int=None, dispatchPeriodType:int=None, failureNoticeType:int=None, unInitNoticeType:int=None, startNoticeType:int=None, incompleteNoticeType:int=None, successNoticeType:int=None, exeTimoutNoticeType:int=None, expectFinishTime:str=None, expectStartTime:str=None, alarmEscalate:int=None, addRecommendedParents:bool=None, parentJobIds:int=None):
        """"""
