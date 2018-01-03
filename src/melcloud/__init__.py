# coding=utf-8
__author__ = "Gareth Coles"

from melcloud.constants import __version__

from melcloud.async.platform import AsyncPlatform
from melcloud.sync.platform import SyncPlatform


__all__ = ["__version__", "AsyncPlatform", "SyncPlatform"]
