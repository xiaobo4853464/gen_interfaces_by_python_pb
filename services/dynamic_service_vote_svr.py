# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DynamicServiceVoteSvr(BaseClient):
    SERVICE_NAME = "dynamic.service.vote.svr"

    @grpc_proxy(path="dynamic.service.vote.svr.v1.VoteSvr/ListFeedVotes")
    def ListFeedVotes(self, uid: int = None, vote_ids: int = None):
        """"""
        
    @grpc_proxy(path="dynamic.service.vote.svr.v1.VoteSvr/DoVote")
    def DoVote(self, vote_id: int = None, votes: int = None, status: int = None, voter_uid: int = None, dynamic_id: int = None, op_bit: int = None):
        """"""
        
