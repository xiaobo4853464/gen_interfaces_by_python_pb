# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DatacenterServiceAbtest(BaseClient):
    SERVICE_NAME="datacenter.service.abtest"

    @grpc_proxy(path="datacenter.service.abtest.AbSdkServer/loadExp")
    def loadExp(self,):
        """"""
