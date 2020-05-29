# coding=utf-8
from aiohttp import ClientSession

from melcloud.constants import URL_LOGIN, KEY_HEADER, URL_LIST_DEVICES, URL_GET_DEVICE
from melcloud.exceptions import NotLoggedInError
from melcloud.objects.connection import BaseConnection
from melcloud.utils import fix_dict_keys, fix_list_keys

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from melcloud.objects.platform import MELCloud

__author__ = "Gareth Coles"


class AsyncConnection(BaseConnection):
    def __init__(self, platform: "MELCloud"):
        super().__init__(platform)
        self.context_key: str = None

    async def login(self, email: str, password: str):
        if self.platform.logged_in:
            self.platform.reset()

        async with ClientSession() as session:
            response = await session.post(
                URL_LOGIN, data={
                    "AppVersion": "1.9.3.0",
                    "CaptchaChallenge": "",
                    "CaptchaResponse": "",
                    "Email": email,
                    "Password": password,
                    "Language": self.platform.language.value,
                    "Persist": "true"
                }
            )

        self.context_key = self.platform.handle_login(
            fix_dict_keys(await response.json())
        ).context_key

    async def load_devices(self, reload=False):
        if not self.platform.logged_in:
            raise NotLoggedInError()

        if not reload and self.platform.has_loaded_devices:
            return
        else:
            self.platform.clear_devices()

        async with ClientSession(headers={KEY_HEADER: self.context_key}) as session:
            response = await session.get(URL_LIST_DEVICES)

        self.platform.handle_device_list(
            fix_list_keys(await response.json())
        )

        for building in self.platform.buildings:
            for device in building.devices:
                await self.platform.get_device_info(device.device_id, device.building_id)

    async def get_device_info(self, device_id, building_id):
        if not self.platform.logged_in:
            raise NotLoggedInError()

        async with ClientSession(headers={KEY_HEADER: self.context_key}) as session:
            response = await session.get(URL_GET_DEVICE, params={"id": device_id, "buildingID": building_id})

        self.platform.handle_device_info(
            building_id, fix_dict_keys(await response.json())
        )
