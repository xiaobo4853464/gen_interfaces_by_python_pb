# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DynamicServiceTopicExt(BaseClient):
    SERVICE_NAME = "dynamic.service.topic.ext"

    @grpc_proxy(path="dynamic.service.topic.ext.v1.TopicExt/ListTopicAdditiveCards")
    def ListTopicAdditiveCards(self, topic_ids: int = None):
        """"""
        
