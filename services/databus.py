# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class Databus(BaseClient):
    SERVICE_NAME="databus"

    @grpc_proxy(path="databus.v2.Producer/Send")
    def Send(self,producer_id:list, messages:list, policy:str=None):
        """"""
    @grpc_proxy(path="databus.v2.Balancer/AuthPick")
    def AuthPick(self,app_id:str, token:str, topic:str, subscription:str=None, producer:str=None):
        """"""
    @grpc_proxy(path="databus.v2.Consumer/Subscribe")
    def Subscribe(self,consumer_id:list, subscription:list=None):
        """"""
    @grpc_proxy(path="databus.v2.Consumer/Recv")
    def Recv(self,consumer_id:list, max_received_messages:int=None, max_wait_timeout:int=None):
        """"""
    @grpc_proxy(path="databus.v2.Consumer/Ack")
    def Ack(self,consumer_id:list, message_id:list):
        """"""
    @grpc_proxy(path="databus.v2.Consumer/Nack")
    def Nack(self,consumer_id:list, message_id:list):
        """"""
    @grpc_proxy(path="databus.v2.Consumer/UnSubscribe")
    def UnSubscribe(self,consumer_id:list):
        """"""
