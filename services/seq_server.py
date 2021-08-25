# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class SeqServer(BaseClient):
    SERVICE_NAME = "seq.server"

    @grpc_proxy(path="seq.server.v1.Seq/ID")
    def ID(self, business: int = None, token: str = None, nums: int = None):
        """"""
        
    @grpc_proxy(path="seq.server.v1.Seq/ID32")
    def ID32(self, business: int = None, token: str = None, nums: int = None):
        """"""
        
    @grpc_proxy(path="seq.server.v1.Seq/MultiID")
    def MultiID(self, business: int = None, token: str = None, nums: int = None):
        """"""
        
    @grpc_proxy(path="seq.server.v1.Seq/MultiID32")
    def MultiID32(self, business: int = None, token: str = None, nums: int = None):
        """"""
        
    @grpc_proxy(path="seq.server.v1.Seq/CheckVersion")
    def CheckVersion(self, ):
        """"""
        
