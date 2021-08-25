# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DatacenterServiceTagCore(BaseClient):
    SERVICE_NAME = "datacenter.service.tag.core"

    @grpc_proxy(path="datacenter.service.tag.core.v1.tag/insert")
    def insert(self, tagType: int = None, tagName: str = None, bizType: int = None, createUserId: int = None, tagCode: str = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.tag.core.v1.tag/batchInsert")
    def batchInsert(self, insertTags: list = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.tag.core.v1.tag/updateById")
    def updateById(self, tagId: int = None, tagType: int = None, tagName: str = None, bizType: int = None, createUserId: int = None, tagCode: str = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.tag.core.v1.tag/tagDeleteByIdsCascade")
    def tagDeleteByIdsCascade(self, item: int = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.tag.core.v1.tag/tagDeleteCascade")
    def tagDeleteCascade(self, tags: list = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.tag.core.v1.tag/queryById")
    def queryById(self, reqLong: int = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.tag.core.v1.tag/queryByIds")
    def queryByIds(self, item: int = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.tag.core.v1.tag/queryTags")
    def queryTags(self, createUserId: int = None, tagName: str = None, bizType: int = None, tagType: int = None, pageSize: int = None, pageNum: int = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.tag.core.v1.tag/queryTagIdsByNames")
    def queryTagIdsByNames(self, createUserId: int = None, tagNames: list = None, bizType: int = None, tagType: int = None, pageSize: int = None, pageNum: int = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.tag.core.v1.tag/queryTagsByItem")
    def queryTagsByItem(self, item: list = None, tag: list = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.tag.core.v1.tag/queryTagsByCommonItem")
    def queryTagsByCommonItem(self, item: list = None, tag: list = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.tag.core.v1.tag/queryTagsByItems")
    def queryTagsByItems(self, item: list = None, tag: list = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.tag.core.v1.tag/queryTagsByCommonItems")
    def queryTagsByCommonItems(self, item: list = None, tag: list = None):
        """"""
        
    @grpc_proxy(path="datacenter.service.tag.core.v1.tag/tagDeleteById")
    def tagDeleteById(self, item: int = None):
        """"""
        
