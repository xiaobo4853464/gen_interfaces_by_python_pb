# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class ArchiveHonorService(BaseClient):
    SERVICE_NAME = "archive.honor.service"

    @grpc_proxy(path="archive.honor.service.v1.ArchiveHonor/Honor")
    def Honor(self, aid: int, build: int = None, mobi_app: str = None, device: str = None):
        """"""
        
    @grpc_proxy(path="archive.honor.service.v1.ArchiveHonor/Honors")
    def Honors(self, aids: int = None, build: int = None, mobi_app: str = None, device: str = None):
        """"""
        
