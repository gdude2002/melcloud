# coding=utf-8
from datetime import datetime
from typing import List

from dataclasses import dataclass

from melcloud.objects.device import Device
from melcloud.objects.floor import Floor

__author__ = "Gareth Coles"


@dataclass
class Building:
    access_level: int
    address_line_1: str
    address_line_2: str
    building_type: int
    city: str
    cooling_disabled: bool
    country: int
    date_built: datetime
    direct_access: bool
    district: str
    end_date: datetime
    expanded: bool
    FP_defined: bool
    FP_enabled: bool
    FP_max_temperature: bool
    FP_min_temperature: bool
    has_gas_supply: bool
    HM_defined: bool
    HM_enabled: bool
    HM_end_date: datetime
    HM_start_date: datetime
    id: int
    i_date_built: datetime
    latitude: float
    location: int
    location_lookup_date: datetime
    longitude: float
    max_temperature: int
    min_temperature: int
    name: str
    owner: object  # ???
    postcode: str
    property_type: int
    timezone: int
    timezone_city: int
    timezone_continent: int

    floors: List[Floor]
    devices: List[Device]

    def get_floor(self, floor_id):
        for floor in self.floors:
            if floor.id == floor_id:
                return floor

    def get_device(self, device_id):
        for device in self.devices:
            if device.device_id == device_id:
                return device
