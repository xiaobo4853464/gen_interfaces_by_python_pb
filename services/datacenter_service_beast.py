# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DatacenterServiceBeast(BaseClient):
    SERVICE_NAME = "datacenter.service.beast"

    @grpc_proxy(path="datacenter.service.beast.v1.BeastDataCollectCommonField/findCommonFieldById")
    def findCommonFieldById(self, reqLong: int = None):
        """"""
        
