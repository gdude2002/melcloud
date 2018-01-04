# coding=utf-8
from datetime import datetime
from typing import List

from dataclasses import dataclass

from melcloud.objects.device import Device

__author__ = "Gareth Coles"


@dataclass
class Floor:
    access_level: int
    building_id: int
    direct_access: bool
    end_date: datetime
    expanded: bool
    id: int
    max_temperature: int
    min_temperature: int
    name: str

    devices: List[Device]
