# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class Sequence(BaseClient):
    SERVICE_NAME = "sequence"

    @grpc_proxy(path="sequence.v1.Seq/AutoIncrement")
    def AutoIncrement(self, business: int = None, token: str = None):
        """"""
        
    @grpc_proxy(path="sequence.v1.Seq/SnowFlake")
    def SnowFlake(self, business: int = None, token: str = None):
        """"""
        
