# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class GarbService(BaseClient):
    SERVICE_NAME="garb.service"

    @grpc_proxy(path="garb.service.v1.Garb/UserEquip")
    def UserEquip(self,partID:int=None, mid:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/UserEquipMulti")
    def UserEquipMulti(self,partID:int=None, mids:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/UserAsset")
    def UserAsset(self,partID:int=None, mid:int=None, itemID:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/UserAssetList")
    def UserAssetList(self,partID:int=None, mid:int=None, group:str=None, pn:int=None, ps:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/GrantByAdmin")
    def GrantByAdmin(self,mids:int=None, partID:int=None, itemID:int=None, addSecond:int=None, adminID:int=None, adminName:str=None, notify:bool=None, fan:bool=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/GrantByExpire")
    def GrantByExpire(self,mids:int=None, item_id:int=None, expire:int=None, token:str=None, fan:bool=None, notify:bool=None, remark:str=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/GrantByBiz")
    def GrantByBiz(self,mids:int=None, ids:int=None, addSecond:int=None, token:str=None, business:str=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/GrantSuit")
    def GrantSuit(self,mids:int=None, suitID:int=None, addSecond:int=None, token:str=None, business:str=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/GrantSuitEquip")
    def GrantSuitEquip(self,mid:int=None, itemId:int=None, addSecond:int=None, token:str=None, business:str=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/GrantItemEquip")
    def GrantItemEquip(self,mid:int=None, itemId:int=None, addSecond:int=None, token:str=None, business:str=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/GrantSuitByExpireLimit")
    def GrantSuitByExpireLimit(self,mid:int=None, suitID:int=None, expireAtTime:int=None, token:str=None, business:str=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/WithdrawSuitByBiz")
    def WithdrawSuitByBiz(self,mid:int=None, suitID:int=None, expireAtTime:int=None, isRemove:bool=None, token:str=None, business:str=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/GrantPendantByOID")
    def GrantPendantByOID(self,mids:int=None, oids:int=None, addSecond:int=None, token:str=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/UserLoadEquip")
    def UserLoadEquip(self,mid:int=None, itemID:int=None, index:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/UserLoadEquipByOID")
    def UserLoadEquipByOID(self,mid:int=None, oid:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/UserUnloadEquip")
    def UserUnloadEquip(self,mid:int=None, partID:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/UserUpdateAsset")
    def UserUpdateAsset(self,mid:int=None, assetID:int=None, expiredTime:int=None, notify:bool=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/UserDeleteAsset")
    def UserDeleteAsset(self,mid:int=None, assetID:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/UserDeleteAssetByAdmin")
    def UserDeleteAssetByAdmin(self,mid:int=None, assetID:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/UserEmojiAccessInfo")
    def UserEmojiAccessInfo(self,mid:int=None, itemIDs:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/UserAssetHistory")
    def UserAssetHistory(self,partID:int=None, mid:int=None, ps:int=None, pn:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/UserFanInfo")
    def UserFanInfo(self,mid:int=None, suitItemID:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/UserFanInfoList")
    def UserFanInfoList(self,mid:int=None, suitItemIDs:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/UserFanRoll")
    def UserFanRoll(self,mid:int=None, suitItemID:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/UserWallet")
    def UserWallet(self,mid:int=None, platform:str=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/UserSetting")
    def UserSetting(self,mid:int=None, type:str=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/SetUserSetting")
    def SetUserSetting(self,mid:int=None, type:str=None, value:str=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/SpaceBGUserEquip")
    def SpaceBGUserEquip(self,mid:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/SpaceBGUserAssetList")
    def SpaceBGUserAssetList(self,mid:int=None, group:str=None, pn:int=None, ps:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/SpaceBGUserAssetListWithFan")
    def SpaceBGUserAssetListWithFan(self,mid:int=None, group:str=None, pn:int=None, ps:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/SpaceBG")
    def SpaceBG(self,ItemID:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/PendantEquipMulti")
    def PendantEquipMulti(self,mids:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/CardBGEquipMulti")
    def CardBGEquipMulti(self,mids:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/SailingEquipMulti")
    def SailingEquipMulti(self,mids:int=None, upMID:int=None, otype:int=None, oid:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/TradeCreate")
    def TradeCreate(self,itemID:int=None, platform:str=None, currency:str=None, addMonth:int=None, mid:int=None, serviceType:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/TradeQuery")
    def TradeQuery(self,orderID:str=None, mid:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/MallGroupList")
    def MallGroupList(self,partID:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/MallItem")
    def MallItem(self,itemID:int=None, partID:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/MallList")
    def MallList(self,partID:int=None, groupID:int=None, pn:int=None, ps:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/MallSuit")
    def MallSuit(self,itemID:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/SkinUserEquip")
    def SkinUserEquip(self,mid:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/SkinList")
    def SkinList(self,ids:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/SkinColorUserList")
    def SkinColorUserList(self,mid:int=None, mobiAPP:str=None, build:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/Items")
    def Items(self,ids:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/FanRank")
    def FanRank(self,itemID:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/FanRecentRank")
    def FanRecentRank(self,itemID:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/HandleVIPExpired")
    def HandleVIPExpired(self,mid:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/HandleItemInvalid")
    def HandleItemInvalid(self,itemID:int=None, refund:bool=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/LoadingUserEquip")
    def LoadingUserEquip(self,mid:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/PlayIconUserEquip")
    def PlayIconUserEquip(self,mid:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/DynamicGarbInfo")
    def DynamicGarbInfo(self,mid:int=None, itemIDs:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/UserReserve")
    def UserReserve(self,itemID:int=None, mid:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/ThumbupUserEquip")
    def ThumbupUserEquip(self,mid:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/UserAssetUnlock")
    def UserAssetUnlock(self,mid:int=None, itemId:int=None, business:str=None, addSecond:int=None, token:str=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/BNJUserFanNumBought")
    def BNJUserFanNumBought(self,mid:int=None, suitID:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/UserMultbuy")
    def UserMultbuy(self,itemID:int=None, mid:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/AppointActivityLog")
    def AppointActivityLog(self,mid:int=None, sid:int=None, timeVersion:int=None, state:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/AppointActivityTotalLog")
    def AppointActivityTotalLog(self,sid:int=None, total:int=None, timeVersion:int=None):
        """"""
    @grpc_proxy(path="garb.service.v1.Garb/SuitBaseItems")
    def SuitBaseItems(self,suitID:int=None):
        """"""
