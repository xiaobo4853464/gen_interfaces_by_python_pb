# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoSkynetT1000(BaseClient):
    SERVICE_NAME = "video.skynet.t1000"

    @grpc_proxy(path="video.skynet.t1000.v1.T1000/GetBlackIPListByVendor")
    def GetBlackIPListByVendor(self, vendor: int = None):
        """"""
        
    @grpc_proxy(path="video.skynet.t1000.v1.T1000/GetBlackIPList")
    def GetBlackIPList(self, ):
        """"""
        
