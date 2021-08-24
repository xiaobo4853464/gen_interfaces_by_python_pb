# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class CardService(BaseClient):
    SERVICE_NAME="card.service"

    @grpc_proxy(path="card.service.v1.Card/Card")
    def Card(self,id:int=None):
        """"""
    @grpc_proxy(path="card.service.v1.Card/CardHots")
    def CardHots(self,):
        """"""
    @grpc_proxy(path="card.service.v1.Card/CardsByGid")
    def CardsByGid(self,gid:int=None):
        """"""
    @grpc_proxy(path="card.service.v1.Card/UserCard")
    def UserCard(self,mid:int=None):
        """"""
    @grpc_proxy(path="card.service.v1.Card/UserCards")
    def UserCards(self,mids:int=None):
        """"""
    @grpc_proxy(path="card.service.v1.Card/Equip")
    def Equip(self,arg:list=None):
        """"""
    @grpc_proxy(path="card.service.v1.Card/DemountEquip")
    def DemountEquip(self,mid:int=None):
        """"""
    @grpc_proxy(path="card.service.v1.Card/AllGroup")
    def AllGroup(self,mid:int=None):
        """"""
