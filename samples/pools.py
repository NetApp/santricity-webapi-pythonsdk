#/usr/local/bin/python

from netapp.santricity.configuration import Configuration
from netapp.santricity.api_client import ApiClient
from netapp.santricity.api.v2.storage_systems_api import StorageSystemsApi
from netapp.santricity.api.v2.volumes_api import VolumesApi
from netapp.santricity.api.v2.hardware_api import HardwareApi
from netapp.santricity.models.v2.drive_selection_request import DriveSelectionRequest
from netapp.santricity.models.v2.storage_pool_create_request import StoragePoolCreateRequest
from netapp.santricity.models.v2.volume_create_request import VolumeCreateRequest

from pprint import pprint

config = Configuration()
config.host = "http://localhost:8080" # Add ip address of the proxy here
config.username = "rw"
config.password = "rw"

api_client = ApiClient()
config.api_client = api_client

storage_system = StorageSystemsApi(api_client=api_client)

# Get storage system status
ssr = storage_system.get_all_storage_systems()

print ssr[0].id

# 1. Dynamically get a list of drives
drv_sel_req = DriveSelectionRequest()
drv_sel_req.drive_count = 5
api_hdw = HardwareApi(api_client=api_client)
drive_sel = api_hdw.select_drives(system_id=ssr[0].id, body=drv_sel_req)
drive_list = []
for d in drive_sel:
    drive_list.append(d.drive_ref)

# 2. Create Volume group/ Storage Pools
vol_api = VolumesApi(api_client=api_client)
sp_req_obj = StoragePoolCreateRequest()
sp_req_obj.raid_level = 'raid6'
sp_req_obj.name = "99_1"
sp_req_obj.disk_drive_ids = drive_list

sp_h = vol_api.new_storage_pool(system_id=ssr[0].id, body=sp_req_obj)
pprint(sp_h)

# 3. Create volumes
vol_req_obj = VolumeCreateRequest()
vol_req_obj.name = "99_data"
vol_req_obj.pool_id = sp_h.id
vol_req_obj.size_unit = "gb"
vol_req_obj.size = 2
vol_req_obj.seg_size = 128

vol_h = vol_api.new_volume(system_id=ssr[0].id, body=vol_req_obj)
pprint(vol_h)
