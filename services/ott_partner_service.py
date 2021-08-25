# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class OttPartnerService(BaseClient):
    SERVICE_NAME = "ott.partner.service"

    @grpc_proxy(path="ott.partner.service.OTTPartner/MediaList")
    def MediaList(self, id: int = None, media_kind: dict = None, pn: int = None, ps: int = None):
        """"""
        
    @grpc_proxy(path="ott.partner.service.OTTPartner/PageData")
    def PageData(self, page_id: int = None):
        """"""
        
