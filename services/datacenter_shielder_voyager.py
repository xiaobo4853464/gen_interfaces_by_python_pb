# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DatacenterShielderVoyager(BaseClient):
    SERVICE_NAME = "datacenter.shielder.voyager"

    @grpc_proxy(path="datacenter.shielder.voyager.v1.ApiService/invoke")
    def invoke(self, apiId: list = None, account: str = None, traceId: str = None, requestId: str = None, data: str = None, signature: str = None):
        """"""
        
