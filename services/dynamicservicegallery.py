# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DynamicServiceGallery(BaseClient):
    SERVICE_NAME="dynamic.service.gallery"

    @grpc_proxy(path="dynamic.service.gallery.v1.Gallery/ListAbtestExpValues")
    def ListAbtestExpValues(self,uid:int=None, requestId:str=None, buvid:str=None, values:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.gallery.v1.Gallery/BatchGetTagMapInfo")
    def BatchGetTagMapInfo(self,tags:int=None):
        """"""
