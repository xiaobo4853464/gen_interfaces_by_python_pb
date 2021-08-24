# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoLiveLivehub(BaseClient):
    SERVICE_NAME="video.live.livehub"

    @grpc_proxy(path="video.live.livehub.v1.LiveHub/BnjStart")
    def BnjStart(self,):
        """"""
    @grpc_proxy(path="video.live.livehub.v1.LiveHub/BnjSeek")
    def BnjSeek(self,):
        """"""
