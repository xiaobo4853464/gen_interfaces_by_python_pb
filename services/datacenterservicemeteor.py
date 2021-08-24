# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DatacenterServiceMeteor(BaseClient):
    SERVICE_NAME="datacenter.service.meteor"

    @grpc_proxy(path="datacenter.service.meteor.v1.Meteor/getEventTypeDivides")
    def getEventTypeDivides(self,reqInt:int=None):
        """"""
    @grpc_proxy(path="datacenter.service.meteor.v1.Meteor/getEventConfig")
    def getEventConfig(self,eventType:dict=None, divideTypeValues:list=None):
        """"""
    @grpc_proxy(path="datacenter.service.meteor.v1.Meteor/sendCometRequest")
    def sendCometRequest(self,applyDetailInfo:str=None, eventId:int=None, applyUserId:int=None, sourceName:str=None, reason:str=None, duration:int=None, requestBody:str=None, dataKey:str=None):
        """"""
    @grpc_proxy(path="datacenter.service.meteor.v1.Meteor/getApplyInfo")
    def getApplyInfo(self,eventType:int=None, eventId:int=None, applyUserId:int=None, nameKey:str=None, page:list=None):
        """"""
    @grpc_proxy(path="datacenter.service.meteor.v1.Meteor/getApplyInfoByProcessId")
    def getApplyInfoByProcessId(self,reqStr:str=None):
        """"""
    @grpc_proxy(path="datacenter.service.meteor.v1.Meteor/callback")
    def callback(self,processId:str=None, status:int=None, applyUserId:int=None, dataKey:str=None):
        """"""
    @grpc_proxy(path="datacenter.service.meteor.v1.Meteor/meteorApply")
    def meteorApply(self,applyUserId:int=None, inventedId:int=None, departmentId:int=None, duration:int=None, reason:str=None, privilegeIds:int=None, privilegeContextMap:list=None, sourceNames:str=None, sourceContextMap:list=None, eventType:int=None, approveUsers:str=None, projectId:int=None, projectName:str=None, projectContext:list=None):
        """"""
    @grpc_proxy(path="datacenter.service.meteor.v1.Meteor/simpleApplyComet")
    def simpleApplyComet(self,username:str=None, reason:str=None, resourceName:str=None, contextMap:list=None, eventType:int=None):
        """"""
    @grpc_proxy(path="datacenter.service.meteor.v1.Meteor/batchApply")
    def batchApply(self,eventType:dict=None, userIds:int=None, privilegeCodes:str=None, sourceContextMap:list=None, duration:int=None, reason:str=None, opUsername:str=None):
        """"""
