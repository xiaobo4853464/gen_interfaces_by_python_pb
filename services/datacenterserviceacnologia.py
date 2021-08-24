# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DatacenterServiceAcnologia(BaseClient):
    SERVICE_NAME="datacenter.service.acnologia"

    @grpc_proxy(path="datacenter.service.acnologia.v1.BiPlatform/GraphDataQuery")
    def GraphDataQuery(self,graphInfos:list, businessType:str, globalFilter:list=None):
        """"""
