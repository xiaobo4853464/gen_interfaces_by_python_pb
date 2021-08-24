# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class Yshaarj(BaseClient):
    SERVICE_NAME="yshaarj"

    @grpc_proxy(path="yshaarj.YShaarjService/CheckStreamTime")
    def CheckStreamTime(self,rids:str=None, intv:str=None):
        """"""
