# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DatacenterServiceKeeper(BaseClient):
    SERVICE_NAME="datacenter.service.keeper"

    @grpc_proxy(path="datacenter.service.keeper.v1.KeeperRelation/getDownStreamProjectList")
    def getDownStreamProjectList(self,databaseName:str=None, tableName:str=None):
        """"""
    @grpc_proxy(path="datacenter.service.keeper.v1.KeeperRelation/getProjectOrLogIdByTableName")
    def getProjectOrLogIdByTableName(self,databaseName:str=None, tableName:str=None):
        """"""
    @grpc_proxy(path="datacenter.service.keeper.v1.KeeperRelation/getProjectOrLogIdByTableNames")
    def getProjectOrLogIdByTableNames(self,item:str=None):
        """"""
    @grpc_proxy(path="datacenter.service.keeper.v1.KeeperRelation/getDownStreamTableByLogId")
    def getDownStreamTableByLogId(self,reqStr:str=None):
        """"""
    @grpc_proxy(path="datacenter.service.keeper.v1.KeeperRelation/getDownStreamTablesByLogId")
    def getDownStreamTablesByLogId(self,reqStr:str=None):
        """"""
    @grpc_proxy(path="datacenter.service.keeper.v1.KeeperRelation/getHiveMiscAndJobType")
    def getHiveMiscAndJobType(self,req:list=None):
        """"""
    @grpc_proxy(path="datacenter.service.keeper.v1.KeeperRelation/getHiveMiscAndJobTypeByUserId")
    def getHiveMiscAndJobTypeByUserId(self,reqLong:int=None):
        """"""
    @grpc_proxy(path="datacenter.service.keeper.v1.KeeperRelation/getInputOutputTableNameByProjectIds")
    def getInputOutputTableNameByProjectIds(self,item:int=None):
        """"""
    @grpc_proxy(path="datacenter.service.keeper.v1.KeeperRelation/getRelationJobByTableName")
    def getRelationJobByTableName(self,item:str=None):
        """"""
    @grpc_proxy(path="datacenter.service.keeper.v1.KeeperRelation/getHiveMiscAndJobTypePage")
    def getHiveMiscAndJobTypePage(self,userId:int=None, miscIds:int=None, searchFullTableName:str=None, fullTableNames:str=None, current:int=None, size:int=None, bloodFlag:bool=None):
        """"""
