# coding=utf-8
import re

from melcloud.objects.preset import Preset
from melcloud.utils import fix_dict_keys

__author__ = "Gareth Coles"
zone_regex = re.compile(r"zone\d_name")


class Device:
    def __init__(self, data):
        data = fix_dict_keys(data)

        self.presets = {}
        self.id = data["device_id"]
        self.name = data["device_name"]
        self.zone_count = 0

        for k, v in data.items():
            if k in ["presets", "device", "permissions", "device_id", "device_name"]:
                continue

            if zone_regex.match(k):
                self.zone_count += 1

            setattr(self, k, v)

        if "device" in data:
            for k, v in fix_dict_keys(data["device"]).items():
                setattr(self, k, v)

        if "permissions" in data:
            for k, v in fix_dict_keys(data["permissions"]).items():
                setattr(self, k, v)

        if "presets" in data:
            for preset in data["presets"]:
                p = Preset(preset)
                self.presets[p.id] = p

    def __str__(self):
        return f"<Device {self.id} ({self.name}) with {self.zone_count} zones>"
