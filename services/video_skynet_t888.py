# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoSkynetT888(BaseClient):
    SERVICE_NAME = "video.skynet.t888"

    @grpc_proxy(path="video.skynet.t888.v1.T888/GetUnusualUsersData")
    def GetUnusualUsersData(self, ):
        """"""
        
    @grpc_proxy(path="video.skynet.t888.v1.T888/GetOnlineUser")
    def GetOnlineUser(self, ):
        """"""
        
    @grpc_proxy(path="video.skynet.t888.v1.T888/GetBrushResp")
    def GetBrushResp(self, room_id: int = None):
        """"""
        
    @grpc_proxy(path="video.skynet.t888.v1.T888/GetStreamBandWidth")
    def GetStreamBandWidth(self, ):
        """"""
        
    @grpc_proxy(path="video.skynet.t888.v1.T888/GetNerveStreamUsers")
    def GetNerveStreamUsers(self, ):
        """"""
        
    @grpc_proxy(path="video.skynet.t888.v1.T888/GetBrushRoomList")
    def GetBrushRoomList(self, ):
        """"""
        
