# coding=utf-8
from requests import Session

from melcloud.constants import URL_LOGIN, KEY_HEADER, URL_LIST_DEVICES
from melcloud.exceptions import NotLoggedInError
from melcloud.objects.connection import BaseConnection
from melcloud.utils import fix_dict_keys, fix_list_keys

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from melcloud.objects.platform import MELCloud

__author__ = "Gareth Coles"


class SyncConnection(BaseConnection):

    def __init__(self, platform: "MELCloud"):
        super().__init__(platform)
        self.session = Session()

    def login(self, email: str, password: str):
        if self.platform.logged_in:
            self.platform.reset()

        response = self.session.post(
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

        self.session.headers[KEY_HEADER] = self.platform.handle_login(fix_dict_keys(response.json())).context_key

    def load_devices(self, reload=False):
        if not self.platform.logged_in:
            raise NotLoggedInError()

        if not reload and self.platform.has_loaded_devices:
            return
        else:
            self.platform.clear_devices()

        response = self.session.get(URL_LIST_DEVICES)
        return self.platform.handle_device_list(fix_list_keys(response.json()))
