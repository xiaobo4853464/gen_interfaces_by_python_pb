# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class TaishanApi(BaseClient):
    SERVICE_NAME="taishan.api"

    @grpc_proxy(path="taishan.api.TaishanProxy/put")
    def put(self,table:str=None, record:list=None, auth:list=None):
        """"""
    @grpc_proxy(path="taishan.api.TaishanProxy/expire")
    def expire(self,table:str=None, key:str=None, ttl:int=None, auth:list=None):
        """"""
    @grpc_proxy(path="taishan.api.TaishanProxy/get")
    def get(self,table:str=None, record:list=None, auth:list=None):
        """"""
    @grpc_proxy(path="taishan.api.TaishanProxy/count")
    def count(self,table:str=None, key:str=None, auth:list=None):
        """"""
    @grpc_proxy(path="taishan.api.TaishanProxy/scan")
    def scan(self,table:str=None, start_rec:list=None, end_rec:list=None, limit:int=None, auth:list=None):
        """"""
    @grpc_proxy(path="taishan.api.TaishanProxy/del")
    def del(self,table:str=None, record:list=None, auth:list=None):
        """"""
    @grpc_proxy(path="taishan.api.TaishanProxy/cas")
    def cas(self,table:str=None, cond:list=None, records:list=None, auth:list=None):
        """"""
    @grpc_proxy(path="taishan.api.TaishanProxy/incr")
    def incr(self,table:str=None, key:str=None, increment:int=None, auth:list=None):
        """"""
    @grpc_proxy(path="taishan.api.TaishanProxy/pop")
    def pop(self,table:str=None, key:str=None, index:int=None, auth:list=None):
        """"""
    @grpc_proxy(path="taishan.api.TaishanProxy/push")
    def push(self,table:str=None, key:str=None, values:str=None, auth:list=None):
        """"""
    @grpc_proxy(path="taishan.api.TaishanProxy/batch_get")
    def batch_get(self,table:str=None, records:list=None, auth:list=None):
        """"""
    @grpc_proxy(path="taishan.api.TaishanProxy/batch_put")
    def batch_put(self,table:str=None, records:list=None, auth:list=None):
        """"""
    @grpc_proxy(path="taishan.api.TaishanProxy/batch_del")
    def batch_del(self,table:str=None, records:list=None, auth:list=None):
        """"""
