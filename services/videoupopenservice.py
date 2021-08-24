# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class VideoupOpenService(BaseClient):
    SERVICE_NAME="videoup.open.service"

    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/ArcVideos")
    def ArcVideos(self,aids:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/VideoViewPoints")
    def VideoViewPoints(self,aid:int=None, cid:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/VideoGuides")
    def VideoGuides(self,aid:int=None, cid:int=None, mid:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/ArcBgmList")
    def ArcBgmList(self,aid:int=None, cid:int=None, cache:bool=None, mtype:int=None, from:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/ArcMaterialList")
    def ArcMaterialList(self,aid:int=None, cid:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/AppMaterialView")
    def AppMaterialView(self,platform:str, build:int, aid:int=None, cid:int=None, mobi_app:str=None, device:str=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/AppMaterialAll")
    def AppMaterialAll(self,MaterialIDs:int=None, BgmIDs:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/ArcCommercial")
    def ArcCommercial(self,aid:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/AppPre")
    def AppPre(self,mid:int=None, tmid:int=None, ip:str=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/AndAppPreV3")
    def AndAppPreV3(self,uid:int=None, build:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/IosAppPreV3")
    def IosAppPreV3(self,uid:int=None, build:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/IosAppMineAcademy")
    def IosAppMineAcademy(self,uid:int=None, build:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/IosAppMineCreative")
    def IosAppMineCreative(self,uid:int=None, build:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/AppPreBeUpper")
    def AppPreBeUpper(self,uid:int=None, build:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/AppPreSubmit")
    def AppPreSubmit(self,uid:int=None, build:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/AppPreCreative")
    def AppPreCreative(self,uid:int=None, build:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/AppPreHotAct")
    def AppPreHotAct(self,uid:int=None, build:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/AppPreAcademy")
    def AppPreAcademy(self,uid:int=None, build:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/UpdateSectionsEpCnt")
    def UpdateSectionsEpCnt(self,ids:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/OpenArcs")
    def OpenArcs(self,mid:int=None, pn:int=None, ps:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/OpenArcsReverseOrder")
    def OpenArcsReverseOrder(self,mid:int=None, pn:int=None, ps:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/Arcs")
    def Arcs(self,mid:int=None, pn:int=None, ps:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/UpArcsSearch")
    def UpArcsSearch(self,mid:int=None, pn:int=None, ps:int=None, keyword:str=None, states:int=None, order:str=None, sort:str=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/UndeletedArcCnt")
    def UndeletedArcCnt(self,mid:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/OpenArcsWithMission")
    def OpenArcsWithMission(self,mid:int=None, pn:int=None, ps:int=None, start:int=None, end:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/LatestOpenArcs")
    def LatestOpenArcs(self,mid:int=None, pn:int=None, ps:int=None, start:int=None, end:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/OpenArcsByDuration")
    def OpenArcsByDuration(self,mid:int=None, pn:int=None, ps:int=None, start:int=None, end:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/LatestOpenArcCount")
    def LatestOpenArcCount(self,mid:int=None, start:int=None, end:int=None, typeId:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/LatestArcCount")
    def LatestArcCount(self,mid:int=None, start:int=None, end:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/FlowJudges")
    def FlowJudges(self,business:int=None, gid:int=None, oids:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/ArcViewAddit")
    def ArcViewAddit(self,aid:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/VideosFilename")
    def VideosFilename(self,ids:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/Videos")
    def Videos(self,ids:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/CreateSeason")
    def CreateSeason(self,id:int=None, title:str=None, desc:str=None, cover:str=None, mid:int=None, attribute:int=None, show:int=None, signState:int=None, state:int=None, partState:int=None, rejectReason:str=None, ctime:int=None, mtime:int=None, actSeason:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/EditSeason")
    def EditSeason(self,id:int=None, title:str=None, desc:str=None, cover:str=None, mid:int=None, attribute:int=None, show:int=None, signState:int=None, state:int=None, partState:int=None, rejectReason:str=None, ctime:int=None, mtime:int=None, actSeason:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/UpdateSeasonState")
    def UpdateSeasonState(self,id:int=None, state:int=None, mid:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/Seasons")
    def Seasons(self,mid:int=None, pager:list=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/GetSeason")
    def GetSeason(self,mid:int=None, seasonId:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/ActiveSeasonsCount")
    def ActiveSeasonsCount(self,id:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/SeasonEps")
    def SeasonEps(self,id:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/GetPositiveSection")
    def GetPositiveSection(self,id:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/AddSection")
    def AddSection(self,id:int=None, type:int=None, seasonId:int=None, title:str=None, order:int=None, state:int=None, partState:int=None, rejectReason:str=None, ctime:int=None, mtime:int=None, epCount:int=None, cover:str=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/EditSessionSection")
    def EditSessionSection(self,id:int=None, type:int=None, seasonId:int=None, title:str=None, order:int=None, state:int=None, partState:int=None, rejectReason:str=None, ctime:int=None, mtime:int=None, epCount:int=None, cover:str=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/Sections")
    def Sections(self,seasonId:int=None, pager:list=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/SectionsBySeasonIds")
    def SectionsBySeasonIds(self,ids:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/GetSection")
    def GetSection(self,id:int=None, mid:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/UpdateSectionState")
    def UpdateSectionState(self,id:int=None, state:int=None, seasonId:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/UpdateSectionsStateBySeasonId")
    def UpdateSectionsStateBySeasonId(self,seasonId:int=None, state:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/SortSections")
    def SortSections(self,Sorts:list=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/ActiveSectionsMaxOrder")
    def ActiveSectionsMaxOrder(self,id:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/ActiveSectionCnt")
    def ActiveSectionCnt(self,id:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/ListActiveSections")
    def ListActiveSections(self,id:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/IsEpsInSection")
    def IsEpsInSection(self,sectionId:int=None, epIds:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/ListEpisodes")
    def ListEpisodes(self,sectionId:int=None, from:int=None, pager:list=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/AddEpisodes")
    def AddEpisodes(self,episodes:list=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/EditEpisode")
    def EditEpisode(self,id:int=None, title:str=None, aid:int=None, cid:int=None, seasonId:int=None, sectionId:int=None, order:int=None, attribute:int=None, state:int=None, rejectReason:str=None, ctime:int=None, mtime:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/UpdateEpisodeState")
    def UpdateEpisodeState(self,id:int=None, state:int=None, sectionId:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/UpdateEpsStateBySectionId")
    def UpdateEpsStateBySectionId(self,sectionId:int=None, state:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/UpdateEpsStateBySeasonId")
    def UpdateEpsStateBySeasonId(self,seasonId:int=None, state:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/SortEpisodes")
    def SortEpisodes(self,Sorts:list=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/GetEpisode")
    def GetEpisode(self,id:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/ActiveEpisodeByAid")
    def ActiveEpisodeByAid(self,id:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/ChangeEpSection")
    def ChangeEpSection(self,seasonId:int=None, sectionId:int=None, epId:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/ActiveEpisodesMaxOrder")
    def ActiveEpisodesMaxOrder(self,id:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/SeasonWhiteGroups")
    def SeasonWhiteGroups(self,):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/IsVideoUp")
    def IsVideoUp(self,mid:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/ArcsDynamicView")
    def ArcsDynamicView(self,aids:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/ArcMaterials")
    def ArcMaterials(self,AID:int=None, MTp:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/BgmUsedCntByMaterialIds")
    def BgmUsedCntByMaterialIds(self,type:int=None, materialIds:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/BgmPickCntByMid")
    def BgmPickCntByMid(self,mid:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/ArchiveState")
    def ArchiveState(self,aid:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/ArchiveSimple")
    def ArchiveSimple(self,aid:int=None):
        """"""
    @grpc_proxy(path="videoup.open.service.v1.VideoUpOpen/ArchiveSimpleBatch")
    def ArchiveSimpleBatch(self,aids:int=None):
        """"""
