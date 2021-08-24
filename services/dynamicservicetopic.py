# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DynamicServiceTopic(BaseClient):
    SERVICE_NAME="dynamic.service.topic"

    @grpc_proxy(path="dynamic.service.topic.v1.Topic/BatchGetStats")
    def BatchGetStats(self,topic_ids:int=None):
        """"""
    @grpc_proxy(path="dynamic.service.topic.v1.Topic/IsIncluded")
    def IsIncluded(self,rids:int=None, topic_id:int=None):
        """"""
    @grpc_proxy(path="dynamic.service.topic.v1.Topic/BriefDyns")
    def BriefDyns(self,topic_id:int=None, sortby:int=None, types:str=None, page_size:int=None, offset:str=None):
        """"""
    @grpc_proxy(path="dynamic.service.topic.v1.Topic/TopicLight")
    def TopicLight(self,uid:int=None, topic_id:int=None, topic_name:str=None, history_offset:str=None, type_list:str=None, version_ctrl:list=None, info_ctrl:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.topic.v1.Topic/HotList")
    def HotList(self,uid:int=None, hot_list_type:int=None, meta_data:list=None, offset:int=None, page_size:int=None):
        """"""
    @grpc_proxy(path="dynamic.service.topic.v1.Topic/RcmdActList")
    def RcmdActList(self,uid:int=None, meta_data:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.topic.v1.Topic/BatchFetchTopicCnts")
    def BatchFetchTopicCnts(self,topic_ids:int=None):
        """"""
    @grpc_proxy(path="dynamic.service.topic.v1.Topic/HasDyns")
    def HasDyns(self,topic_id:int=None, pick_id:int=None, sort_by:int=None, uid:int=None, types:int=None):
        """"""
    @grpc_proxy(path="dynamic.service.topic.v1.Topic/ListDyns")
    def ListDyns(self,topic_id:int=None, topic_name:str=None, uid:int=None, sort_by:int=None, page_size:int=None, pick_id:int=None, with_top:bool=None, offset:list=None, types:int=None, version_ctrl:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.topic.v1.Topic/RcmdTopicsBigCard")
    def RcmdTopicsBigCard(self,mid:int=None, meta_data:list=None, traceId:str=None):
        """"""
    @grpc_proxy(path="dynamic.service.topic.v1.Topic/TopicSearch")
    def TopicSearch(self,mid:int=None, meta_data:list=None, word:str=None, ip:str=None):
        """"""
