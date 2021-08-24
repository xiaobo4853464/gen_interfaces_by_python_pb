# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VasResource(BaseClient):
    SERVICE_NAME="vas.resource"

    @grpc_proxy(path="vas.resource.v1.Resource/ResourceInfo")
    def ResourceInfo(self,batch_id:int=None, appkey:str=None):
        """"""
    @grpc_proxy(path="vas.resource.v1.Resource/ResourceInfosByBizId")
    def ResourceInfosByBizId(self,biz_id:int=None):
        """"""
    @grpc_proxy(path="vas.resource.v1.Resource/ResourceInfoByTokenV2")
    def ResourceInfoByTokenV2(self,token:str=None, appkey:str=None):
        """"""
    @grpc_proxy(path="vas.resource.v1.Resource/ResourceUse")
    def ResourceUse(self,batch_id:int=None, batch_token:str=None, mid:int=None, order_no:str=None, remark:str=None, with_detail:bool=None, appkey:str=None, ts:int=None, sign:str=None):
        """"""
    @grpc_proxy(path="vas.resource.v1.Resource/ResourceUseAsync")
    def ResourceUseAsync(self,batch_token:str=None, mid:int=None, order_no:str=None, remark:str=None, appkey:str=None, ts:int=None, sign:str=None):
        """"""
    @grpc_proxy(path="vas.resource.v1.Resource/ResourceUsage")
    def ResourceUsage(self,relation_id:str=None):
        """"""
    @grpc_proxy(path="vas.resource.v1.Resource/ResourceUsageCount")
    def ResourceUsageCount(self,batch_token:str=None, mid:int=None):
        """"""
    @grpc_proxy(path="vas.resource.v1.Resource/ResourceUseByPhone")
    def ResourceUseByPhone(self,batch_id:int=None, batch_token:str=None, telephone:str=None, order_no:str=None, remark:str=None, vip_type:int=None, tv_resource_id:int=None, third_id:str=None, with_detail:bool=None, appkey:str=None, ts:int=None, sign:str=None):
        """"""
    @grpc_proxy(path="vas.resource.v1.Resource/ResourcePreStore")
    def ResourcePreStore(self,batch_token:str=None, telephone:str=None, order_no:str=None, remark:str=None, vip_type:int=None, tv_resource_id:int=None, third_id:str=None, appkey:str=None):
        """"""
    @grpc_proxy(path="vas.resource.v1.Resource/ResourcePreStoreGive")
    def ResourcePreStoreGive(self,tel:str=None, mid:int=None, change_time:int=None):
        """"""
    @grpc_proxy(path="vas.resource.v1.Resource/ResourcesGetUsageTimeList")
    def ResourcesGetUsageTimeList(self,mid:int=None, batch_code_id:int=None):
        """"""
    @grpc_proxy(path="vas.resource.v1.Resource/ResourceOpenRecord")
    def ResourceOpenRecord(self,batch_token:str=None, order_no:str=None, appkey:str=None, sign:str=None, ts:int=None):
        """"""
    @grpc_proxy(path="vas.resource.v1.Resource/ResourceGrantRecords")
    def ResourceGrantRecords(self,mid:int=None, order_no:str=None):
        """"""
    @grpc_proxy(path="vas.resource.v1.Resource/CodeInfo")
    def CodeInfo(self,code:str=None):
        """"""
    @grpc_proxy(path="vas.resource.v1.Resource/CodeOpen")
    def CodeOpen(self,batch_id:int=None, code:str=None, ts:int=None, ip:str=None, mid:int=None):
        """"""
    @grpc_proxy(path="vas.resource.v1.Resource/CodeOpened")
    def CodeOpened(self,biz_appkey:str=None, bis_sign:str=None, bis_ts:int=None, start_time:int=None, end_time:int=None, cursor:int=None):
        """"""
    @grpc_proxy(path="vas.resource.v1.Resource/CodesUseTimeList")
    def CodesUseTimeList(self,mid:int=None, batch_code_ids:int=None):
        """"""
