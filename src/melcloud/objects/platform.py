# coding=utf-8
from inflection import underscore as to_underscore
from melcloud.constants import LANGUAGES
from melcloud.exceptions import MELCloudError
from melcloud.objects.building import Building
from melcloud.utils import fix_dict_keys

__author__ = "Gareth Coles"


class Platform:
    _login_email = ""
    _login_password = ""
    language = None
    logged_in = False
    loaded_devices = False

    buildings = None
    context_key = None

    client = None
    terms = None
    al = None
    ml = None
    cmi = None
    is_staff = None
    cutf = None
    caa = None
    receive_country_notifications = None
    receive_all_notifications = None
    caca = None
    caga = None
    maximum_devices = None
    show_diagnostics = None
    country = None
    real_client = None
    name = None
    use_fahrenheit = None
    duration = None
    expiry = None
    cmsc = None
    partner_application_version = None
    email_settings_reminder_shown = None
    email_unit_errors = None
    email_comms_errors = None
    is_impersonated = None
    language_code = None
    country_name = None
    currency_symbol = None
    support_email_address = None
    date_seperator = None
    time_seperator = None
    atw_logo_file = None
    decc_report = None
    csv_report_1min = None
    hide_preset_panel = None
    email_settings_reminder_required = None
    terms_text = None
    map_zoom = None
    map_longitude = None
    map_latitude = None

    def __init__(self, email: str, password: str, language: LANGUAGES):
        self._login_email = email
        self._login_password = password
        self.language = language

        self.buildings = {}

    def _raise_error(self, data):
        if "ErrorId" in data and data["ErrorId"]:
            raise MELCloudError(int(data["ErrorID"]), data.get("ErrorMessage"))

    def _parse_login(self, data):
        self._raise_error(data)
        login_data = fix_dict_keys(data)["login_data"]

        for key, value in login_data.items():
            if key == "language":
                continue

            setattr(self, key, value)

        if self.context_key:
            self.logged_in = True

    def _parse_devices(self, data):
        self._raise_error(data)
        self.loaded_devices = True

        for building in data:
            b = Building(building)
            self.buildings[b.id] = b

        return self.buildings
