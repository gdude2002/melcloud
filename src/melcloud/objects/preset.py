# coding=utf-8
from melcloud.utils import fix_dict_keys

__author__ = "Gareth Coles"


class Preset:
    def __init__(self, data):
        data = fix_dict_keys(data)

        for k, v in data.items():
            setattr(self, k, v)

    def __str__(self):
        return f"<Preset {self.number} ({self.number_description})>"
