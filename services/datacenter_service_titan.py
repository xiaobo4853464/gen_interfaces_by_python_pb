# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DatacenterServiceTitan(BaseClient):
    SERVICE_NAME = "datacenter.service.titan"

    @grpc_proxy(path="datacenter.service.titan.v1.Crowd/queryAllTag")
    def queryAllTag(self, ):
        """"""
        
    @grpc_proxy(path="datacenter.service.titan.v1.Crowd/queryTagByView")
    def queryTagByView(self, viewId: int = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.titan.v1.Crowd/queryCrowd")
    def queryCrowd(self, tagIds: list = None, queryCondition: str = None, viewId: int = None, crowdId: int = None, partition: str = None, extraParam: str = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.titan.v1.Crowd/downLoadCrowd")
    def downLoadCrowd(self, tagIds: list = None, queryCondition: str = None, viewId: int = None, crowdId: int = None, partition: str = None, extraParam: str = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.titan.v1.Crowd/queryCrowdDetail")
    def queryCrowdDetail(self, crowdId: int = None, pageSize: int = None, pageCount: int = None, viewId: int = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.titan.v1.Crowd/upload")
    def upload(self, fileName: str = None, file: str = None, tableName: str = None, extendPath: str = None, apiId: str = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.titan.v1.Crowd/queryCrowdAsync")
    def queryCrowdAsync(self, tagIds: list = None, queryCondition: str = None, viewId: int = None, crowdId: int = None, partition: str = None, extraParam: str = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.titan.v1.Crowd/queryCrowdStatus")
    def queryCrowdStatus(self, crowdId: int = None):
        """"""
        
