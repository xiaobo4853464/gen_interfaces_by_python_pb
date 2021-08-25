# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class ComBilibiliMainDynamicService(BaseClient):
    SERVICE_NAME = "com.bilibili.main.dynamic.service"

    @grpc_proxy(path="com.bilibili.main.dynamic.service.DynamicSearchService/Search")
    def Search(self, keywords: str = None, start: int = None, limit: int = None, mid: int = None):
        """"""
        
    @grpc_proxy(path="com.bilibili.main.dynamic.service.DynamicSearchService/SuggestSearch")
    def SuggestSearch(self, keywords: str = None, start: int = None, limit: int = None, mid: int = None, app: str = None):
        """"""
        
    @grpc_proxy(path="com.bilibili.main.dynamic.service.DynamicSearchService/RecommendWords")
    def RecommendWords(self, mid: int = None):
        """"""
        
    @grpc_proxy(path="com.bilibili.main.dynamic.service.DynamicSearchService/PersonalSearch")
    def PersonalSearch(self, keywords: str = None, start: int = None, limit: int = None, mid: int = None, upId: int = None):
        """"""
        
