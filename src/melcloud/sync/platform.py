# coding=utf-8
import requests

from melcloud.constants import URL_LOGIN, LANGUAGES, URL_LIST_DEVICES, KEY_HEADER
from melcloud.exceptions import NotLoggedInError
from melcloud.objects.platform import Platform

__author__ = "Gareth Coles"


class SyncPlatform(Platform):
    def __init__(self, email: str, password: str, language: LANGUAGES):
        super().__init__(email, password, language)
        self.session = requests.session()

    def login(self):
        if self.logged_in:
            self.logged_in = False
            self.context_key = None

        resp = self.session.post(
            URL_LOGIN, data={
                "AppVersion": "1.9.3.0",
                "CaptchaChallenge": "",
                "CaptchaResponse": "",
                "Email": self._login_email,
                "Password": self._login_password,
                "Language": self.language.value,
                "Persist": "true"
            }
        )

        self._parse_login(resp.json())

    def get_devices(self, reload=False):
        if not self.logged_in:
            raise NotLoggedInError()

        if not reload and self.loaded_devices:
            return
        else:
            self.buildings.clear()

        resp = self.session.get(URL_LIST_DEVICES, headers={KEY_HEADER: self.context_key})
        return self._parse_devices(resp.json())
