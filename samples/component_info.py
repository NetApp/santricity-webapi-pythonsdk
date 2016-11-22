#/usr/bin/python

from netapp.santricity.configuration import Configuration
from netapp.santricity.api_client import ApiClient
from netapp.santricity.api.v2.storage_systems_api import StorageSystemsApi
from netapp.santricity.api.v2.volumes_api import VolumesApi
from netapp.santricity.api.v2.hardware_api import HardwareApi

from pprint import pprint

config = Configuration()
config.host = "http://localhost:8080"  # Add ip address of the proxy here
config.username = "rw"
config.password = "rw"

api_client = ApiClient()
config.api_client = api_client

storage_system = StorageSystemsApi(api_client=api_client)

# Get storage system status
ssr = storage_system.get_all_storage_systems()

for ss in ssr:
    print "\n##################################\n" \
          "Storage System wwn - " + ss.wwn + ", Status : " + ss.status

    # Get all volumes info for each storage system
    volume_api = VolumesApi(api_client=api_client)
    volumes = volume_api.get_all_volumes(system_id=ss.id)

    for vol in volumes:
        print "\n##################################\n" \
              "Volume " + vol.wwn + ", info : \n"
        pprint(vol)

    # Get all volume group info for each storage system
    vgs = volume_api.get_all_storage_pools(system_id=ss.id)
    for vg in vgs:
        print "\n##################################\n" \
              "Volume Group info for " + vg.world_wide_name
        pprint(vg)

    # Get all drives info for each storage system
    hardware_api = HardwareApi(api_client=api_client)
    drives = hardware_api.get_all_drives(system_id=ss.id)
    for drive in drives:
        print "\n##################################\n" \
              "Drive data for driveWwn: " + drive.world_wide_name
        pprint(drive)

    # Get FC Port WWN:
    hardware_inventory = hardware_api.get_hardware_information(system_id=ss.id)
    fibre_ports = hardware_inventory.fibre_ports
    for fiber_port in fibre_ports:
        print "fiber Port WWN: " + fiber_port.nice_address_id

    # Get controller & product info
    controllers = hardware_api.get_all_controllers(system_id=ss.id)
    for controller in controllers:
        print "\n##################################\n" \
              "Controller info "
        print "Controller Ref: " + controller.controller_ref
        print "Controller status: " + controller.status
        print "Controller type: " + controller.board_id
        print "Firmware Version: " + controller.app_version

        print "\n##################################\n" \
              "Controller host interfaces:  "
        for host_interface in controller.host_interfaces:
            print "Port WWN: " + host_interface.fibre.nice_address_id

    # Get object bundle
    object_graph = storage_system.get_object_graph(system_id=ss.id)
    component_bundle = object_graph.component_bundle

    # Get Thermal Sensor info
    thermal_sensors = component_bundle.thermal_sensor
    for sensor in thermal_sensors:
        print "\n##################################\n" \
              "Thermal sensor info for : " + sensor.thermal_sensor_ref
        print(sensor)

    # Get power supply info
    power_supplies = component_bundle.power_supply
    for power in power_supplies:
        print "\n##################################\n" \
              "Power Supply info for : " + power.power_supply_ref
        print(power)

    # Get fan info
    fans = component_bundle.fan
    for fan in fans:
        print "\n##################################\n" \
              "Fan info for :" + fan.fan_ref
        pprint(fan)

    # Get battery info
    batteries = component_bundle.battery
    for battery in batteries:
        print "\n##################################\n" \
              "Battery info for :" + battery.battery_ref
        pprint(battery)
