# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from data import dm_pb2 as data_dot_dm__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DMStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMsg = channel.unary_unary(
                '/live.livedm.v1.DM/SendMsg',
                request_serializer=data_dot_dm__pb2.SendMsgReq.SerializeToString,
                response_deserializer=data_dot_dm__pb2.SendMsgResp.FromString,
                )
        self.GetHistory = channel.unary_unary(
                '/live.livedm.v1.DM/GetHistory',
                request_serializer=data_dot_dm__pb2.HistoryReq.SerializeToString,
                response_deserializer=data_dot_dm__pb2.HistoryResp.FromString,
                )
        self.DelHistoryDMByRoomid = channel.unary_unary(
                '/live.livedm.v1.DM/DelHistoryDMByRoomid',
                request_serializer=data_dot_dm__pb2.DelHistoryDMByRoomidReq.SerializeToString,
                response_deserializer=data_dot_dm__pb2.DelHistoryDMByRoomidResp.FromString,
                )
        self.AuditContentConfList = channel.unary_unary(
                '/live.livedm.v1.DM/AuditContentConfList',
                request_serializer=data_dot_dm__pb2.AudiContentConfListReq.SerializeToString,
                response_deserializer=data_dot_dm__pb2.AudiContentConfListResp.FromString,
                )
        self.CreateAuditContentConf = channel.unary_unary(
                '/live.livedm.v1.DM/CreateAuditContentConf',
                request_serializer=data_dot_dm__pb2.CreateAuditContentConfReq.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.UdateAuditContentConf = channel.unary_unary(
                '/live.livedm.v1.DM/UdateAuditContentConf',
                request_serializer=data_dot_dm__pb2.UpdateAuditContentConfReq.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.DeleteAuditContentConf = channel.unary_unary(
                '/live.livedm.v1.DM/DeleteAuditContentConf',
                request_serializer=data_dot_dm__pb2.DeleteAuditContentConfReq.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetAuditContentConf = channel.unary_unary(
                '/live.livedm.v1.DM/GetAuditContentConf',
                request_serializer=data_dot_dm__pb2.GetAuditContentConfReq.SerializeToString,
                response_deserializer=data_dot_dm__pb2.GetAuditContentConfResp.FromString,
                )
        self.SetAuditorNum = channel.unary_unary(
                '/live.livedm.v1.DM/SetAuditorNum',
                request_serializer=data_dot_dm__pb2.SetAuditorNumReq.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetAuditorNumAndDanmuNum = channel.unary_unary(
                '/live.livedm.v1.DM/GetAuditorNumAndDanmuNum',
                request_serializer=data_dot_dm__pb2.GetAuditorNumAndDanmuNumReq.SerializeToString,
                response_deserializer=data_dot_dm__pb2.GetAuditorNumAndDanmuNumResp.FromString,
                )
        self.GetDanmuLists = channel.unary_unary(
                '/live.livedm.v1.DM/GetDanmuLists',
                request_serializer=data_dot_dm__pb2.GetDanmuListsReq.SerializeToString,
                response_deserializer=data_dot_dm__pb2.GetDanmuListsResp.FromString,
                )
        self.SetDanmuSendList = channel.unary_unary(
                '/live.livedm.v1.DM/SetDanmuSendList',
                request_serializer=data_dot_dm__pb2.SetDanmuSendListReq.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.AuditBan = channel.unary_unary(
                '/live.livedm.v1.DM/AuditBan',
                request_serializer=data_dot_dm__pb2.AuditBanReq.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.AuditBanInfo = channel.unary_unary(
                '/live.livedm.v1.DM/AuditBanInfo',
                request_serializer=data_dot_dm__pb2.AuditBanInfoReq.SerializeToString,
                response_deserializer=data_dot_dm__pb2.AuditBanInfoResp.FromString,
                )


class DMServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendMsg(self, request, context):
        """服务相关接口
        发送弹幕
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHistory(self, request, context):
        """获取弹幕历史
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelHistoryDMByRoomid(self, request, context):
        """删除历史弹幕
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuditContentConfList(self, request, context):
        """后台相关接口
        获取先审后发配置列表
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateAuditContentConf(self, request, context):
        """新增先审后发配置
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UdateAuditContentConf(self, request, context):
        """修改先审后发配置
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAuditContentConf(self, request, context):
        """删除先审后发配置
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAuditContentConf(self, request, context):
        """查询先审后发配置
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAuditorNum(self, request, context):
        """注册审核人数
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAuditorNumAndDanmuNum(self, request, context):
        """获取当前审核人数以及弹幕池弹幕数量
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDanmuLists(self, request, context):
        """获取待审核弹幕列表
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDanmuSendList(self, request, context):
        """审核通过发送弹幕内容
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuditBan(self, request, context):
        """rpc SetDanmuSendList (SetDanmuSendListReq) returns (google.protobuf.Empty){
        option (google.api.http) = {
        post:"/live.livedm.v1.DM/SetDanmuSendList"
        };
        };
        先审后发后台封禁
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuditBanInfo(self, request, context):
        """先审后发后获取用户封禁信息
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DMServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendMsg': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMsg,
                    request_deserializer=data_dot_dm__pb2.SendMsgReq.FromString,
                    response_serializer=data_dot_dm__pb2.SendMsgResp.SerializeToString,
            ),
            'GetHistory': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHistory,
                    request_deserializer=data_dot_dm__pb2.HistoryReq.FromString,
                    response_serializer=data_dot_dm__pb2.HistoryResp.SerializeToString,
            ),
            'DelHistoryDMByRoomid': grpc.unary_unary_rpc_method_handler(
                    servicer.DelHistoryDMByRoomid,
                    request_deserializer=data_dot_dm__pb2.DelHistoryDMByRoomidReq.FromString,
                    response_serializer=data_dot_dm__pb2.DelHistoryDMByRoomidResp.SerializeToString,
            ),
            'AuditContentConfList': grpc.unary_unary_rpc_method_handler(
                    servicer.AuditContentConfList,
                    request_deserializer=data_dot_dm__pb2.AudiContentConfListReq.FromString,
                    response_serializer=data_dot_dm__pb2.AudiContentConfListResp.SerializeToString,
            ),
            'CreateAuditContentConf': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAuditContentConf,
                    request_deserializer=data_dot_dm__pb2.CreateAuditContentConfReq.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UdateAuditContentConf': grpc.unary_unary_rpc_method_handler(
                    servicer.UdateAuditContentConf,
                    request_deserializer=data_dot_dm__pb2.UpdateAuditContentConfReq.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'DeleteAuditContentConf': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAuditContentConf,
                    request_deserializer=data_dot_dm__pb2.DeleteAuditContentConfReq.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetAuditContentConf': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAuditContentConf,
                    request_deserializer=data_dot_dm__pb2.GetAuditContentConfReq.FromString,
                    response_serializer=data_dot_dm__pb2.GetAuditContentConfResp.SerializeToString,
            ),
            'SetAuditorNum': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAuditorNum,
                    request_deserializer=data_dot_dm__pb2.SetAuditorNumReq.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetAuditorNumAndDanmuNum': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAuditorNumAndDanmuNum,
                    request_deserializer=data_dot_dm__pb2.GetAuditorNumAndDanmuNumReq.FromString,
                    response_serializer=data_dot_dm__pb2.GetAuditorNumAndDanmuNumResp.SerializeToString,
            ),
            'GetDanmuLists': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDanmuLists,
                    request_deserializer=data_dot_dm__pb2.GetDanmuListsReq.FromString,
                    response_serializer=data_dot_dm__pb2.GetDanmuListsResp.SerializeToString,
            ),
            'SetDanmuSendList': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDanmuSendList,
                    request_deserializer=data_dot_dm__pb2.SetDanmuSendListReq.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'AuditBan': grpc.unary_unary_rpc_method_handler(
                    servicer.AuditBan,
                    request_deserializer=data_dot_dm__pb2.AuditBanReq.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'AuditBanInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.AuditBanInfo,
                    request_deserializer=data_dot_dm__pb2.AuditBanInfoReq.FromString,
                    response_serializer=data_dot_dm__pb2.AuditBanInfoResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'live.livedm.v1.DM', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DM(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendMsg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/live.livedm.v1.DM/SendMsg',
            data_dot_dm__pb2.SendMsgReq.SerializeToString,
            data_dot_dm__pb2.SendMsgResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetHistory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/live.livedm.v1.DM/GetHistory',
            data_dot_dm__pb2.HistoryReq.SerializeToString,
            data_dot_dm__pb2.HistoryResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelHistoryDMByRoomid(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/live.livedm.v1.DM/DelHistoryDMByRoomid',
            data_dot_dm__pb2.DelHistoryDMByRoomidReq.SerializeToString,
            data_dot_dm__pb2.DelHistoryDMByRoomidResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AuditContentConfList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/live.livedm.v1.DM/AuditContentConfList',
            data_dot_dm__pb2.AudiContentConfListReq.SerializeToString,
            data_dot_dm__pb2.AudiContentConfListResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateAuditContentConf(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/live.livedm.v1.DM/CreateAuditContentConf',
            data_dot_dm__pb2.CreateAuditContentConfReq.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UdateAuditContentConf(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/live.livedm.v1.DM/UdateAuditContentConf',
            data_dot_dm__pb2.UpdateAuditContentConfReq.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAuditContentConf(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/live.livedm.v1.DM/DeleteAuditContentConf',
            data_dot_dm__pb2.DeleteAuditContentConfReq.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAuditContentConf(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/live.livedm.v1.DM/GetAuditContentConf',
            data_dot_dm__pb2.GetAuditContentConfReq.SerializeToString,
            data_dot_dm__pb2.GetAuditContentConfResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAuditorNum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/live.livedm.v1.DM/SetAuditorNum',
            data_dot_dm__pb2.SetAuditorNumReq.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAuditorNumAndDanmuNum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/live.livedm.v1.DM/GetAuditorNumAndDanmuNum',
            data_dot_dm__pb2.GetAuditorNumAndDanmuNumReq.SerializeToString,
            data_dot_dm__pb2.GetAuditorNumAndDanmuNumResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDanmuLists(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/live.livedm.v1.DM/GetDanmuLists',
            data_dot_dm__pb2.GetDanmuListsReq.SerializeToString,
            data_dot_dm__pb2.GetDanmuListsResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetDanmuSendList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/live.livedm.v1.DM/SetDanmuSendList',
            data_dot_dm__pb2.SetDanmuSendListReq.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AuditBan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/live.livedm.v1.DM/AuditBan',
            data_dot_dm__pb2.AuditBanReq.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AuditBanInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/live.livedm.v1.DM/AuditBanInfo',
            data_dot_dm__pb2.AuditBanInfoReq.SerializeToString,
            data_dot_dm__pb2.AuditBanInfoResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
