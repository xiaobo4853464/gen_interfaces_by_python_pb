# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class GarbActivty(BaseClient):
    SERVICE_NAME = "garb.activty"

    @grpc_proxy(path="garb.activty.v1.GarbActivity/GrantGameAssistByBiz")
    def GrantGameAssistByBiz(self, source: str = None, token: str = None, mid: int = None, items: list = None, gameId: str = None):
        """"""
        
    @grpc_proxy(path="garb.activty.v1.GarbActivity/GrantUserLotteryTimes")
    def GrantUserLotteryTimes(self, lotteryId: str = None, mid: int = None, ver: str = None, limit: int = None, expireTime: int = None, num: int = None, biz: str = None, token: str = None):
        """"""
        
    @grpc_proxy(path="garb.activty.v1.GarbActivity/LotteryDrawByTimes")
    def LotteryDrawByTimes(self, lotteryId: str = None, mid: int = None, ver: str = None, game_id: str = None, invite_token: str = None):
        """"""
        
