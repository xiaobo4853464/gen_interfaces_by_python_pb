# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DynamicServiceFeedSvr(BaseClient):
    SERVICE_NAME="dynamic.service.feed.svr"

    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/UpdateNum")
    def UpdateNum(self,uid:int=None, offsets:list=None, version_ctrl:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/VideoNew")
    def VideoNew(self,uid:int=None, update_baseline:str=None, assist_baseline:str=None, type_list:str=None, version_ctrl:list=None, info_ctrl:list=None, attention_info:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/VideoHistory")
    def VideoHistory(self,uid:int=None, offset:str=None, page:int=None, type_list:str=None, version_ctrl:list=None, info_ctrl:list=None, attention_info:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/DynBriefs")
    def DynBriefs(self,uid:int=None, dyn_ids:int=None, version_ctrl:list=None, info_ctrl:list=None, attention_users:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/VideoPersonal")
    def VideoPersonal(self,uid:int=None, host_uid:int=None, is_preload:bool=None, offset:str=None, version_ctrl:list=None, info_ctrl:list=None, attention_users:list=None, footprint:str=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/DynPostInfo")
    def DynPostInfo(self,uid:int=None, dyns:list=None, version_ctrl:list=None, info_ctrl:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/UpListViewMore")
    def UpListViewMore(self,uid:int=None, sort_type:int=None, version_ctrl:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/UpListSearch")
    def UpListSearch(self,mid:int=None, name:str=None, real_ip:str=None, version_ctrl:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/WebEntranceInfo")
    def WebEntranceInfo(self,uid:int=None, video_offset:int=None, article_offset:int=None, alltype_offset:int=None, need_head_icon:bool=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/GeneralNew")
    def GeneralNew(self,uid:int=None, update_baseline:str=None, type_list:str=None, version_ctrl:list=None, info_ctrl:list=None, attention_info:list=None, rcmd_ups_param:list=None, ad_param:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/GeneralHistory")
    def GeneralHistory(self,uid:int=None, history_offset:str=None, page:int=None, type_list:str=None, ad_param:list=None, version_ctrl:list=None, info_ctrl:list=None, attention_info:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/UnLogin")
    def UnLogin(self,app_meta:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/UnLoginFeed")
    def UnLoginFeed(self,fake_uid:int=None, is_refresh:bool=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/GeneralPersonal")
    def GeneralPersonal(self,uid:int=None, host_uid:int=None, is_preload:bool=None, offset:str=None, version_ctrl:list=None, info_ctrl:list=None, attention_users:list=None, footprint:str=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/ListWordText")
    def ListWordText(self,uid:int=None, rids:int=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/ListWidget")
    def ListWidget(self,uid:int=None, rids:int=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/ListUpRecommend")
    def ListUpRecommend(self,uid:int=None, dislikeTs:int=None, version_ctrl:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/UnloginLight")
    def UnloginLight(self,fake_uid:int=None, history_offset:str=None, type_list:str=None, version_ctrl:list=None, info_ctrl:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/DynLight")
    def DynLight(self,uid:int=None, history_offset:str=None, page:int=None, type_list:str=None, ad_param:list=None, version_ctrl:list=None, info_ctrl:list=None, attention_info:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/SpaceHistory")
    def SpaceHistory(self,uid:int=None, host_uid:int=None, history_offset:str=None, page:int=None, version_ctrl:list=None, info_ctrl:list=None, attention_info:list=None, type_list:str=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/DynDetail")
    def DynDetail(self,uid:int=None, host_uid:int=None, dyn_id:int=None, dyn_revs_id:list=None, ad_param:list=None, version_ctrl:list=None, info_ctrl:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/LikeList")
    def LikeList(self,uid:int=None, dyn_id:int=None, dyn_revs_id:list=None, uid_offset:int=None, page_number:int=None, page_size:int=None, version_ctrl:list=None, attention_info:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/RepostList")
    def RepostList(self,uid:int=None, dyn_id:int=None, dyn_revs_id:list=None, offset:str=None, page_size:int=None, version_ctrl:list=None, info_ctrl:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/HotRepostList")
    def HotRepostList(self,uid:int=None, dyn_id:int=None, dyn_revs_id:list=None, offset:str=None, page_size:int=None, version_ctrl:list=None, info_ctrl:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/TvUpList")
    def TvUpList(self,uid:int=None, version_ctrl:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/TvFeed")
    def TvFeed(self,uid:int=None, offset:str=None, version_ctrl:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/TvPersonal")
    def TvPersonal(self,uid:int=None, up_item:list=None, offset:str=None, version_ctrl:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/DynSimpleInfos")
    def DynSimpleInfos(self,dyn_ids:int=None, dyn_revs_id:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/FetchDynIdByRevs")
    def FetchDynIdByRevs(self,dyn_revs_ids:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/Search")
    def Search(self,s:str=None, page_num:int=None, page_size:int=None, uid:int=None, meta:list=None, attention_info:list=None, info_ctrl:list=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/AtList")
    def AtList(self,uid:int=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/AtSearch")
    def AtSearch(self,uid:int=None, keyword:str=None):
        """"""
    @grpc_proxy(path="dynamic.service.feed.svr.v1.Feed/MixUpList")
    def MixUpList(self,uid:int=None, last_req_timestamp:int=None, version_ctrl:list=None, from:dict=None):
        """"""
