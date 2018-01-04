# coding=utf-8
from abc import ABCMeta
from weakref import ref

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from melcloud.objects.platform import MELCloud

__author__ = "Gareth Coles"


class BaseConnection(metaclass=ABCMeta):
    def __init__(self, platform: "MELCloud"):
        self._platform = ref(platform)

    @property
    def platform(self) -> "MELCloud":
        return self._platform()

    def login(self, email: str,  password: str):
        raise NotImplementedError()

    def load_devices(self, reload=False):
        raise NotImplementedError()
