# coding=utf-8
from typing import ClassVar
from melcloud.constants import LANGUAGES
from melcloud.exceptions import MELCloudError
from melcloud.objects.account import Account
from melcloud.objects.connection import BaseConnection
from melcloud.sync.connection import SyncConnection
from melcloud.utils import rename_key

__author__ = "Gareth Coles"


class MELCloud:
    def __init__(self, language: LANGUAGES, connection: ClassVar[BaseConnection]=SyncConnection):
        self.language: LANGUAGES = language
        self.connection: BaseConnection = connection(self)

        self.logged_in: bool = False
        self.has_loaded_devices: bool = False
        self.account: Account = None

    def reset(self):
        self.logged_in = False
        self.has_loaded_devices = False
        self.account = None

    def clear_devices(self):
        pass

    def login(self, email: str, password: str):
        return self.connection.login(email, password)

    def load_devices(self, reload=False):
        return self.connection.load_devices(reload)

    def raise_on_error(self, data):
        if data.get("error_id"):
            raise MELCloudError(int(data["error_id"]), data.get("error_message"))

    def handle_login(self, data) -> Account:
        self.raise_on_error(data)
        d = data["login_data"]

        # Sanitize data for our dataclass' expected args
        rename_key(d, "al", "AL")
        rename_key(d, "caa", "CAA")
        rename_key(d, "caca", "CACA")
        rename_key(d, "caga", "CAGA")
        rename_key(d, "client", "client_id")
        rename_key(d, "cmi", "CMI")
        rename_key(d, "cmsc", "CMSC")
        rename_key(d, "csv_report1min", "CSV_report_1_min")
        rename_key(d, "cutf", "CUTF")
        rename_key(d, "date_seperator", "date_separator")
        rename_key(d, "time_seperator", "time_separator")
        rename_key(d, "decc_report", "DECC_report")
        rename_key(d, "ml", "ML")

        del d["language_code"]
        d["language"] = self.language

        self.account = Account(**d)
        self.logged_in = True
        return self.account

    def handle_device_list(self, data):
        self.raise_on_error(data)
