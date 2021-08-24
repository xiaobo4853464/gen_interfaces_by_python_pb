# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class (BaseClient):
    SERVICE_NAME=""

    @grpc_proxy(path="SaberDqcService/SubmitJob")
    def SubmitJob(self,saberJob:list=None, operator:list=None):
        """"""
    @grpc_proxy(path="SaberDqcService/GetSourceSql")
    def GetSourceSql(self,name:str=None, fields:list=None, properties:list=None):
        """"""
    @grpc_proxy(path="SaberDqcService/SetJobAlarm")
    def SetJobAlarm(self,jobId:str=None, alrams:list=None):
        """"""
