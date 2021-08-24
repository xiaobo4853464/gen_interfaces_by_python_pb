# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DynamicServiceLocalcitySvr(BaseClient):
    SERVICE_NAME="dynamic.service.localcity.svr"

    @grpc_proxy(path="dynamic.service.localcity.svr.v1.LocalCitySvr/Switch")
    def Switch(self,switch:int=None, uid:int=None):
        """"""
    @grpc_proxy(path="dynamic.service.localcity.svr.v1.LocalCitySvr/TabShow")
    def TabShow(self,ip_addr:str=None, uid:int=None):
        """"""
    @grpc_proxy(path="dynamic.service.localcity.svr.v1.LocalCitySvr/Dynamic")
    def Dynamic(self,city_id:int, uid:int, lat:float=None, lng:float=None, page_size:int=None, offset:str=None, lbs_state:int=None, refresh_city:int=None, exp_conf:list=None, city_code:int=None, build_time:int=None):
        """"""
    @grpc_proxy(path="dynamic.service.localcity.svr.v1.LocalCitySvr/GetUserPrivacy")
    def GetUserPrivacy(self,uid:int=None):
        """"""
    @grpc_proxy(path="dynamic.service.localcity.svr.v1.LocalCitySvr/UpdateUserPrivacy")
    def UpdateUserPrivacy(self,uid:int=None, dyn_status:int=None):
        """"""
    @grpc_proxy(path="dynamic.service.localcity.svr.v1.LocalCitySvr/ClickReport")
    def ClickReport(self,uid:int=None, dynamic_id:int=None, click_time:str=None, ip:str=None, city_id:int=None, lng:str=None, lat:str=None):
        """"""
