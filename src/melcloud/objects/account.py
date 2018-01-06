# coding=utf-8
from datetime import datetime
from dataclasses import dataclass

from melcloud.constants import Languages

__author__ = "Gareth Coles"


@dataclass
class Account:
    AL: int
    atw_logo_file: str
    CAA: bool
    CACA: bool
    CAGA: bool
    client_id: int
    CMI: bool
    CMSC: bool
    context_key: str
    country: int
    country_name: str
    CSV_report_1_min: bool
    currency_symbol: str
    CUTF: bool
    date_separator: str
    DECC_report: bool
    duration: int
    email_comms_errors: int
    email_settings_reminder_required: bool
    email_settings_reminder_shown: bool
    email_unit_errors: int
    expiry: datetime
    hide_preset_panel: bool
    is_impersonated: bool
    is_staff: bool
    language: Languages
    map_latitude: float
    map_longitude: float
    map_view: bool
    map_zoom: int
    maximum_devices: int
    ML: int
    name: str
    partner_application_version: str
    real_client: int
    receive_all_notifications: bool
    receive_country_notifications: bool
    show_diagnostics: bool
    support_email_address: str
    terms: int
    terms_text: str
    time_separator: str
    use_fahrenheit: bool
