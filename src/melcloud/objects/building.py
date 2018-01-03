# coding=utf-8
from inflection import underscore as to_underscore

from melcloud.objects.device import Device
from melcloud.utils import fix_dict_keys

__author__ = "Gareth Coles"


class Building:
    def __init__(self, data):
        self.devices = {}
        self.floors = {}

        data = fix_dict_keys(data)

        for key, value in data.items():
            if key in ["structure", "quantized_coordinates"]:
                continue

            setattr(self, key, value)

        # TODO: Examples for areas, devices, clients?
        structure = data["structure"]

        for floor in structure["floors"]:
            floor = fix_dict_keys(floor)
            floor_id = floor["id"]
            self.floors[floor_id] = floor.copy()
            self.floors[floor_id]["devices"] = {}

            for device in floor["devices"]:
                d = Device(device)
                self.devices[d.id] = d
                self.floors[floor_id]["devices"][d.id] = d

    def __str__(self):
        return f"<Building {self.id} ({self.name}) with {len(self.devices)} devices>"
