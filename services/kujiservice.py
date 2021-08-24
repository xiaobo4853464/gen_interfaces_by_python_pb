# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class KujiService(BaseClient):
    SERVICE_NAME="kuji.service"

    @grpc_proxy(path="kuji.service.v1.VasKuji/GrantDrawChance")
    def GrantDrawChance(self,mid:int=None, activity_id:int=None, draw_type:int=None, grant_size:int=None, grant_token:str=None):
        """"""
    @grpc_proxy(path="kuji.service.v1.VasKuji/AssistGrant")
    def AssistGrant(self,mid:int=None, activity_id:int=None, type:int=None, grant_size:int=None, grant_token:str=None, source:str=None):
        """"""
