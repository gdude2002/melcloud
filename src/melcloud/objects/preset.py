# coding=utf-8
from dataclasses import dataclass

__author__ = "Gareth Coles"


@dataclass
class Preset:
    client: int
    configuration: str  # This is a shortened XML version of the object for some reason
    device_location: int
    eco_hot_water: bool
    forced_hot_water_mode: bool
    id: int
    number: int
    number_description: str
    operation_mode_zone_1: int
    operation_mode_zone_2: int
    power: bool
    set_cool_flow_temperature_zone_1: int
    set_cool_flow_temperature_zone_2: int
    set_heat_flow_temperature_zone_1: int
    set_heat_flow_temperature_zone_2: int
    set_tank_water_temperature: int
    set_temperature_zone_1: int
    set_temperature_zone_2: int
