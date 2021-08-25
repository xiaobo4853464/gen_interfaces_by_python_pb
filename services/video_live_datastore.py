# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoLiveDatastore(BaseClient):
    SERVICE_NAME = "video.live.datastore"

    @grpc_proxy(path="video.live.datastore.v1.DataStore/Get")
    def Get(self, data: list):
        """"""
        
    @grpc_proxy(path="video.live.datastore.v1.DataStore/Set")
    def Set(self, data: list):
        """"""
        
    @grpc_proxy(path="video.live.datastore.v1.DataStore/Del")
    def Del(self, data: list):
        """"""
        
    @grpc_proxy(path="video.live.datastore.v1.DataStore/Ttl")
    def Ttl(self, data: list):
        """"""
        
    @grpc_proxy(path="video.live.datastore.v1.DataStore/Expire")
    def Expire(self, data: list):
        """"""
        
    @grpc_proxy(path="video.live.datastore.v1.DataStore/Ping")
    def Ping(self, ):
        """"""
        
    @grpc_proxy(path="video.live.datastore.v1.DataStore/Close")
    def Close(self, ):
        """"""
        
