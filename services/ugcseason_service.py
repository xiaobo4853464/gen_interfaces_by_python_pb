# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class UgcseasonService(BaseClient):
    SERVICE_NAME = "ugcseason.service"

    @grpc_proxy(path="ugcseason.service.v1.UGCSeason/Season")
    def Season(self, seasonID: int):
        """"""
        
    @grpc_proxy(path="ugcseason.service.v1.UGCSeason/Seasons")
    def Seasons(self, season_ids: int):
        """"""
        
    @grpc_proxy(path="ugcseason.service.v1.UGCSeason/View")
    def View(self, seasonID: int):
        """"""
        
    @grpc_proxy(path="ugcseason.service.v1.UGCSeason/Views")
    def Views(self, season_ids: int = None, ep_size: int = None):
        """"""
        
    @grpc_proxy(path="ugcseason.service.v1.UGCSeason/Stat")
    def Stat(self, seasonID: int):
        """"""
        
    @grpc_proxy(path="ugcseason.service.v1.UGCSeason/Stats")
    def Stats(self, seasonIDs: int):
        """"""
        
    @grpc_proxy(path="ugcseason.service.v1.UGCSeason/UpperList")
    def UpperList(self, mid: int, pageNum: int = None, pageSize: int = None):
        """"""
        
