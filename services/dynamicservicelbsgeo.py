# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DynamicServiceLbsGeo(BaseClient):
    SERVICE_NAME="dynamic.service.lbs.geo"

    @grpc_proxy(path="dynamic.service.lbs.geo.v1.LbsGeo/GeoCoder")
    def GeoCoder(self,lat:float=None, lng:float=None, from:str=None):
        """"""
