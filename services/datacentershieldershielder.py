# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DatacenterShielderShielder(BaseClient):
    SERVICE_NAME="datacenter.shielder.shielder"

    @grpc_proxy(path="datacenter.shielder.shielder.v1.ShielderUserRole/insert")
    def insert(self,userRoleInfo:list=None, opUserMsg:list=None):
        """"""
    @grpc_proxy(path="datacenter.shielder.shielder.v1.ShielderUserRole/update")
    def update(self,userRoleInfo:list=None, opUserMsg:list=None):
        """"""
    @grpc_proxy(path="datacenter.shielder.shielder.v1.ShielderUserRole/deleteByUserId")
    def deleteByUserId(self,reqLong:int=None, opUserMsg:list=None):
        """"""
    @grpc_proxy(path="datacenter.shielder.shielder.v1.ShielderUserRole/deleteByRoleId")
    def deleteByRoleId(self,reqLong:int=None, opUserMsg:list=None):
        """"""
    @grpc_proxy(path="datacenter.shielder.shielder.v1.ShielderUserRole/findByUserId")
    def findByUserId(self,reqLong:int=None):
        """"""
