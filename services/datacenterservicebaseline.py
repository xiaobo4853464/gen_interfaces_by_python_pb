# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DatacenterServiceBaseline(BaseClient):
    SERVICE_NAME="datacenter.service.baseline"

    @grpc_proxy(path="datacenter.service.baseline.BaselineTagServer/queryItemsByTagName")
    def queryItemsByTagName(self,tagType:dict=None, tagContent:str=None, itemType:dict=None):
        """"""
    @grpc_proxy(path="datacenter.service.baseline.BaselineTagServer/queryTagsByItemId")
    def queryTagsByItemId(self,itemType:dict=None, itemId:str=None, tagType:dict=None):
        """"""
