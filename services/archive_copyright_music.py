# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class ArchiveCopyrightMusic(BaseClient):
    SERVICE_NAME = "archive.copyright.music"

    @grpc_proxy(path="archive.copyright.music.v1.MusicMetadata/Ping")
    def Ping(self, ):
        """"""
        
    @grpc_proxy(path="archive.copyright.music.v1.MusicMetadata/SaveMetadata")
    def SaveMetadata(self, Source: dict = None, Artist: str = None, Title: str = None, Album: str = None, ISRC: str = None, Aid: int = None, Auid: int = None, Language: str = None, Style: str = None, MusicType: str = None, MetaId: str = None, Copyright: str = None):
        """"""
        
    @grpc_proxy(path="archive.copyright.music.v1.MusicMetadata/GetMetadata")
    def GetMetadata(self, MetaId: str = None, MusicType: str = None, aegis_state: int = None):
        """"""
        
    @grpc_proxy(path="archive.copyright.music.v1.MusicMetadata/MatchMetadata")
    def MatchMetadata(self, Artist: str = None, Title: str = None, Album: str = None, ISRC: str = None, MusicType: str = None):
        """"""
        
    @grpc_proxy(path="archive.copyright.music.v1.MusicMetadata/GetConfLabels")
    def GetConfLabels(self, ):
        """"""
        
