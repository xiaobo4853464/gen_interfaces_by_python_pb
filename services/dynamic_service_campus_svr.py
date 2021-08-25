# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DynamicServiceCampusSvr(BaseClient):
    SERVICE_NAME = "dynamic.service.campus.svr"

    @grpc_proxy(path="dynamic.service.campus.svr.v1.CampusSvr/SchoolSearch")
    def SchoolSearch(self, keywords: str = None, page_size: int = None, offset: int = None):
        """"""
        
    @grpc_proxy(path="dynamic.service.campus.svr.v1.CampusSvr/SchoolRecommend")
    def SchoolRecommend(self, mid: int = None, latitude: float = None, longitude: float = None, ip: str = None):
        """"""
        
    @grpc_proxy(path="dynamic.service.campus.svr.v1.CampusSvr/UserCheck")
    def UserCheck(self, mid: int = None):
        """"""
        
    @grpc_proxy(path="dynamic.service.campus.svr.v1.CampusSvr/TabShow")
    def TabShow(self, ip_addr: str = None, uid: int = None):
        """"""
        
    @grpc_proxy(path="dynamic.service.campus.svr.v1.CampusSvr/SetDecision")
    def SetDecision(self, uid: int = None, result: int = None):
        """"""
        
    @grpc_proxy(path="dynamic.service.campus.svr.v1.CampusSvr/Pages")
    def Pages(self, uid: int = None, campus_id: int = None, campus_name: str = None, ip_addr: str = None, lat: float = None, lng: float = None):
        """"""
        
    @grpc_proxy(path="dynamic.service.campus.svr.v1.CampusSvr/AlumniDynamics")
    def AlumniDynamics(self, uid: int = None, campus_id: int = None, first_time: int = None, version_ctrl: list = None, info_ctrl: list = None, attention_info: list = None):
        """"""
        
    @grpc_proxy(path="dynamic.service.campus.svr.v1.CampusSvr/Subscribe")
    def Subscribe(self, uid: int = None, campus_id: int = None, campus_name: str = None):
        """"""
        
    @grpc_proxy(path="dynamic.service.campus.svr.v1.CampusSvr/SetRecent")
    def SetRecent(self, uid: int = None, campus_id: int = None, campus_name: str = None):
        """"""
        
