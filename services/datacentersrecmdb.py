# Generate by automation,Do not modify it. @xiaobo
from invoker.http import BaseClient, grpc_proxy


class DatacenterSreCmdb(BaseClient):
    SERVICE_NAME="datacenter.sre.cmdb"

    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/SaveIdleHosts")
    def SaveIdleHosts(self,IdleHosts:list=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/QueryIdleHosts")
    def QueryIdleHosts(self,count_from:int=None, count_to:int=None, department:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/SendHostsUsageEmail")
    def SendHostsUsageEmail(self,value:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/ListIdleHosts")
    def ListIdleHosts(self,page_num:int=None, page_size:int=None, host:list=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/SetHostOwner")
    def SetHostOwner(self,owner:str=None, hostname:str=None, cluster:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/UpdateHostOwner")
    def UpdateHostOwner(self,owner:str=None, hostname:str=None, cluster:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/SetExpectedDate")
    def SetExpectedDate(self,hostname:str=None, expected_date:int=None, cluster:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/AddFollowUpEvent")
    def AddFollowUpEvent(self,hostname:str=None, desc:str=None, detail:str=None, ctime:int=None, type:dict=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/ListFollowUpEvent")
    def ListFollowUpEvent(self,hostname:str=None, desc:str=None, detail:str=None, ctime:int=None, type:dict=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/ListWorkWXDepartments")
    def ListWorkWXDepartments(self,value:int=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/ListWorkWXDepartmentUsers")
    def ListWorkWXDepartmentUsers(self,value:int=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/CreateOrUpdateDepartment")
    def CreateOrUpdateDepartment(self,id:int=None, name:str=None, workwx_id:int=None, workwx_parent_id:int=None, state:dict=None, ctime:int=None, mtime:int=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/UpdateDepartment")
    def UpdateDepartment(self,id:int=None, name:str=None, workwx_id:int=None, workwx_parent_id:int=None, state:dict=None, ctime:int=None, mtime:int=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/DeleteDepartment")
    def DeleteDepartment(self,id:int=None, name:str=None, workwx_id:int=None, workwx_parent_id:int=None, state:dict=None, ctime:int=None, mtime:int=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/PageDepartment")
    def PageDepartment(self,page_size:int=None, page_number:int=None, name:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/GetDepartmentByWorkWXID")
    def GetDepartmentByWorkWXID(self,value:int=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/GetDepartmentByName")
    def GetDepartmentByName(self,value:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/CreateOrUpdateUser")
    def CreateOrUpdateUser(self,id:int=None, name:str=None, user_id:str=None, workwx_main_department:int=None, email:str=None, english_name:str=None, telephone:str=None, state:dict=None, ctime:int=None, mtime:int=None, department_name:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/UpdateUser")
    def UpdateUser(self,id:int=None, name:str=None, user_id:str=None, workwx_main_department:int=None, email:str=None, english_name:str=None, telephone:str=None, state:dict=None, ctime:int=None, mtime:int=None, department_name:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/DeleteUser")
    def DeleteUser(self,id:int=None, name:str=None, user_id:str=None, workwx_main_department:int=None, email:str=None, english_name:str=None, telephone:str=None, state:dict=None, ctime:int=None, mtime:int=None, department_name:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/PageUser")
    def PageUser(self,page_size:int=None, page_number:int=None, english_name:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/ListUserByWorkwxDepartment")
    def ListUserByWorkwxDepartment(self,value:int=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/GetUserByEnglishName")
    def GetUserByEnglishName(self,value:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/ListSubDepartmentID")
    def ListSubDepartmentID(self,value:int=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/ListRMSServer")
    def ListRMSServer(self,value:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/GetRMSRack")
    def GetRMSRack(self,value:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/GetRMSPackage")
    def GetRMSPackage(self,value:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/GetRMSIDC")
    def GetRMSIDC(self,value:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/CreateOrUpdateServer")
    def CreateOrUpdateServer(self,id:int=None, rms_id:str=None, rms_rack_id:str=None, rms_package_id:str=None, rms_org_id:str=None, name:str=None, code:str=None, sn:str=None, inner_ip:str=None, outer_ip:str=None, mgr_ip:str=None, virtual_ip:str=None, owner:str=None, expire_time:str=None, model:str=None, cpu_model:str=None, memory:str=None, raid:str=None, remark:str=None, sys_status:str=None, disk:str=None, account:str=None, gpu_model:str=None, logistics_sheet:str=None, tapd_sheet:str=None, os_name:str=None, os_version:str=None, os_distribution:str=None, ulocation:str=None, cpu_num_agent:int=None, os_name_agent:str=None, os_version_agent:str=None, os_distribution_agent:str=None, inner_ip_agent:str=None, sn_agent:str=None, model_agent:str=None, manager_ip_agent:str=None, outter_ip_agent:str=None, state:dict=None, ctime:int=None, mtime:int=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/GetServer")
    def GetServer(self,id:int=None, rms_id:str=None, rms_rack_id:str=None, rms_package_id:str=None, rms_org_id:str=None, name:str=None, code:str=None, sn:str=None, inner_ip:str=None, outer_ip:str=None, mgr_ip:str=None, virtual_ip:str=None, owner:str=None, expire_time:str=None, model:str=None, cpu_model:str=None, memory:str=None, raid:str=None, remark:str=None, sys_status:str=None, disk:str=None, account:str=None, gpu_model:str=None, logistics_sheet:str=None, tapd_sheet:str=None, os_name:str=None, os_version:str=None, os_distribution:str=None, ulocation:str=None, cpu_num_agent:int=None, os_name_agent:str=None, os_version_agent:str=None, os_distribution_agent:str=None, inner_ip_agent:str=None, sn_agent:str=None, model_agent:str=None, manager_ip_agent:str=None, outter_ip_agent:str=None, state:dict=None, ctime:int=None, mtime:int=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/PageServer")
    def PageServer(self,page_size:int=None, page_number:int=None, name:str=None, manager_ip:str=None, outer_ip:str=None, sn:str=None, inner_ip:str=None, code:str=None, fuzzy_ip:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/CreateOrUpdateRack")
    def CreateOrUpdateRack(self,id:int=None, rms_id:str=None, rms_idc_id:str=None, name:str=None, sys_status:str=None, floor:str=None, start_time:str=None, remark:str=None, power_spec:int=None, size:str=None, height:int=None, switch_size:int=None, state:dict=None, ctime:int=None, mtime:int=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/GetRack")
    def GetRack(self,id:int=None, rms_id:str=None, rms_idc_id:str=None, name:str=None, sys_status:str=None, floor:str=None, start_time:str=None, remark:str=None, power_spec:int=None, size:str=None, height:int=None, switch_size:int=None, state:dict=None, ctime:int=None, mtime:int=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/PageRack")
    def PageRack(self,page_size:int=None, page_number:int=None, name:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/CreateOrUpdatePackage")
    def CreateOrUpdatePackage(self,id:int=None, rms_id:str=None, name:str=None, detail:str=None, cpu:str=None, mem:str=None, sysdisk:str=None, ssd:str=None, sata:str=None, gpu:str=None, netcard:str=None, power:str=None, remark:str=None, scene:str=None, brand_model:str=None, is_container_pack:str=None, conversion_rate:int=None, associated_pack:str=None, associated_pack_name:str=None, quantity:str=None, ratedpower:str=None, state:dict=None, ctime:int=None, mtime:int=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/GetPackage")
    def GetPackage(self,id:int=None, rms_id:str=None, name:str=None, detail:str=None, cpu:str=None, mem:str=None, sysdisk:str=None, ssd:str=None, sata:str=None, gpu:str=None, netcard:str=None, power:str=None, remark:str=None, scene:str=None, brand_model:str=None, is_container_pack:str=None, conversion_rate:int=None, associated_pack:str=None, associated_pack_name:str=None, quantity:str=None, ratedpower:str=None, state:dict=None, ctime:int=None, mtime:int=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/PagePackage")
    def PagePackage(self,page_size:int=None, page_number:int=None, name:str=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/CreateOrUpdateIDC")
    def CreateOrUpdateIDC(self,id:int=None, rms_id:str=None, name:str=None, code:str=None, type:str=None, start_time:str=None, end_time:str=None, port_bandwidth:str=None, ip_section:str=None, address:str=None, contact:str=None, phone:str=None, email:str=None, remark:str=None, supplier:str=None, core:str=None, rack_quantities:str=None, state:dict=None, ctime:int=None, mtime:int=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/GetIDC")
    def GetIDC(self,id:int=None, rms_id:str=None, name:str=None, code:str=None, type:str=None, start_time:str=None, end_time:str=None, port_bandwidth:str=None, ip_section:str=None, address:str=None, contact:str=None, phone:str=None, email:str=None, remark:str=None, supplier:str=None, core:str=None, rack_quantities:str=None, state:dict=None, ctime:int=None, mtime:int=None):
        """"""
    @grpc_proxy(path="datacenter.sre.cmdb.v1.CMDB/PageIDC")
    def PageIDC(self,page_size:int=None, page_number:int=None, name:str=None):
        """"""
