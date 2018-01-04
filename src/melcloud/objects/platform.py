# coding=utf-8
from typing import ClassVar, List
from melcloud.constants import LANGUAGES
from melcloud.exceptions import MELCloudError
from melcloud.objects.account import Account
from melcloud.objects.building import Building
from melcloud.objects.connection import BaseConnection
from melcloud.objects.device import Device
from melcloud.objects.floor import Floor
from melcloud.objects.preset import Preset
from melcloud.sync.connection import SyncConnection
from melcloud.utils import rename_key, str_to_datetime, replace_key

__author__ = "Gareth Coles"


class MELCloud:
    def __init__(self, language: LANGUAGES, connection: ClassVar[BaseConnection]=SyncConnection):
        self.language: LANGUAGES = language
        self.connection: BaseConnection = connection(self)

        self.logged_in: bool = False
        self.has_loaded_devices: bool = False
        self.account: Account = None
        self.buildings: List[Building] = []

    def reset(self):
        self.logged_in = False
        self.has_loaded_devices = False
        self.account = None
        self.buildings.clear()

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

        replace_key(d, "expiry", str_to_datetime)

        del d["language_code"]
        d["language"] = self.language

        self.account = Account(**d)
        self.logged_in = True

        return self.account

    def handle_device_list(self, data):
        for d in data:
            rename_key(d, "address_line1", "address_line_1")
            rename_key(d, "address_line2", "address_line_2")
            rename_key(d, "fp_defined", "FP_defined")
            rename_key(d, "fp_enabled", "FP_enabled")
            rename_key(d, "fp_max_temperature", "FP_max_temperature")
            rename_key(d, "fp_min_temperature", "FP_min_temperature")
            rename_key(d, "hm_defined", "HM_defined")
            rename_key(d, "hm_enabled", "HM_enabled")
            rename_key(d, "hm_end_date", "HM_end_date")
            rename_key(d, "hm_start_date", "HM_start_date")
            rename_key(d, "time_zone", "timezone")
            rename_key(d, "time_zone_city", "timezone_city")
            rename_key(d, "time_zone_continent", "timezone_continent")

            replace_key(d, "date_built", str_to_datetime)
            replace_key(d, "end_date", str_to_datetime)
            replace_key(d, "HM_end_date", str_to_datetime)
            replace_key(d, "HM_start_date", str_to_datetime)
            replace_key(d, "i_date_built", str_to_datetime)
            replace_key(d, "location_lookup_date", str_to_datetime)

            # TODO: Find someone with areas/clients/devices in the "structures" section
            structure = d["structure"]

            del d["structure"]
            del d["quantized_coordinates"]

            floor_objects = []
            device_objects = []

            floors = structure["floors"]

            for f in floors:
                devices = f["devices"]
                floor_device_objects = []

                del f["areas"]  # TODO: ???

                for dev in devices:
                    dev.update(dev["device"])
                    dev.update(dev["permissions"])

                    presets = []

                    for p in dev["presets"]:
                        rename_key(p, "operation_mode_zone1", "operation_mode_zone_1")
                        rename_key(p, "operation_mode_zone2", "operation_mode_zone_2")
                        rename_key(p, "set_cool_flow_temperature_zone1", "set_cool_flow_temperature_zone_1")
                        rename_key(p, "set_cool_flow_temperature_zone2", "set_cool_flow_temperature_zone_2")
                        rename_key(p, "set_heat_flow_temperature_zone1", "set_heat_flow_temperature_zone_1")
                        rename_key(p, "set_heat_flow_temperature_zone2", "set_heat_flow_temperature_zone_2")
                        rename_key(p, "set_temperature_zone1", "set_temperature_zone_1")
                        rename_key(p, "set_temperature_zone2", "set_temperature_zone_2")
                        presets.append(Preset(**p))

                    dev["presets"] = presets

                    del dev["device"]
                    del dev["permissions"]
                    del dev["units"]  # TODO: ???
                    del dev["list_history24_formatters"]  # What even is this?

                    rename_key(dev, "booster_heater1_status", "booster_heater_1_status")
                    rename_key(dev, "booster_heater2_plus_status", "booster_heater_2_plus_status")
                    rename_key(dev, "booster_heater2_status", "booster_heater_2_status")
                    rename_key(dev, "cooling_energy_consumed_rate1", "cooling_energy_consumed_rate_1")
                    rename_key(dev, "cooling_energy_consumed_rate2", "cooling_energy_consumed_rate_2")
                    rename_key(dev, "cooling_energy_produced_rate1", "cooling_energy_produced_rate_1")
                    rename_key(dev, "cooling_energy_produced_rate2", "cooling_energy_produced_rate_2")
                    rename_key(dev, "csv_report1min", "CSV_report_1_min")
                    rename_key(dev, "decc_report", "DECC_report")
                    rename_key(dev, "dip_switch1", "dip_switch_1")
                    rename_key(dev, "dip_switch2", "dip_switch_2")
                    rename_key(dev, "dip_switch3", "dip_switch_3")
                    rename_key(dev, "dip_switch4", "dip_switch_4")
                    rename_key(dev, "effective_p_cycle", "effective_pcycle")
                    rename_key(dev, "error_code2_digit", "error_code_2_digit")
                    rename_key(dev, "flow_temperature_zone1", "flow_temperature_zone_1")
                    rename_key(dev, "flow_temperature_zone2", "flow_temperature_zone_2")
                    rename_key(dev, "ftc_model", "FTC_model")
                    rename_key(dev, "ftc_revision", "FTC_revision")
                    rename_key(dev, "ftc_version", "FTC_version")
                    rename_key(dev, "has_ftc45_settings", "has_FTC_45_settings")
                    rename_key(dev, "has_simplified_zone2", "has_simplified_zone_2")
                    rename_key(dev, "has_thermostat_zone1", "has_thermostat_zone_1")
                    rename_key(dev, "has_thermostat_zone2", "has_thermostat_zone_2")
                    rename_key(dev, "has_zone2", "has_zone_2")
                    rename_key(dev, "heating_energy_consumed_rate1", "heating_energy_consumed_rate_1")
                    rename_key(dev, "heating_energy_consumed_rate2", "heating_energy_consumed_rate_2")
                    rename_key(dev, "heating_energy_produced_rate1", "heating_energy_produced_rate_1")
                    rename_key(dev, "heating_energy_produced_rate2", "heating_energy_produced_rate_2")
                    rename_key(dev, "hot_water_energy_consumed_rate1", "hot_water_energy_consumed_rate_1")
                    rename_key(dev, "hot_water_energy_consumed_rate2", "hot_water_energy_consumed_rate_2")
                    rename_key(dev, "hot_water_energy_produced_rate1", "hot_water_energy_produced_rate_1")
                    rename_key(dev, "hot_water_energy_produced_rate2", "hot_water_energy_produced_rate_2")
                    rename_key(dev, "idle_zone1", "idle_zone_1")
                    rename_key(dev, "idle_zone2", "idle_zone_2")
                    rename_key(dev, "is_ftc_model_supported", "is_FTC_model_supported")
                    rename_key(dev, "last_ftc_revision", "last_FTC_revision")
                    rename_key(dev, "last_ftc_version", "last_FTC_version")
                    rename_key(dev, "operation_mode_zone1", "operation_mode_zone_1")
                    rename_key(dev, "operation_mode_zone2", "operation_mode_zone_2")
                    rename_key(dev, "p_cycle", "pcycle")
                    rename_key(dev, "prohibit_cooling_zone1", "prohibit_cooling_zone_1")
                    rename_key(dev, "prohibit_cooling_zone2", "prohibit_cooling_zone_2")
                    rename_key(dev, "prohibit_heating_zone1", "prohibit_heating_zone_1")
                    rename_key(dev, "prohibit_heating_zone2", "prohibit_heating_zone_2")
                    rename_key(dev, "rate1_start_time", "rate_1_start_time")
                    rename_key(dev, "rate2_start_time", "rate_2_start_time")
                    rename_key(dev, "refridgerent_address", "refrigerant_address")
                    rename_key(dev, "regist_reason", "registration_reason")
                    rename_key(dev, "regist_retry", "registration_retry")
                    rename_key(dev, "return_temperature_zone1", "return_temperature_zone_1")
                    rename_key(dev, "return_temperature_zone2", "return_temperature_zone_2")
                    rename_key(dev, "room_temperature_zone1", "room_temperature_zone_1")
                    rename_key(dev, "room_temperature_zone2", "room_temperature_zone_2")
                    rename_key(dev, "set_cool_flow_temperature_zone1", "set_cool_flow_temperature_zone_1")
                    rename_key(dev, "set_cool_flow_temperature_zone2", "set_cool_flow_temperature_zone_2")
                    rename_key(dev, "set_heat_flow_temperature_zone1", "set_heat_flow_temperature_zone_1")
                    rename_key(dev, "set_heat_flow_temperature_zone2", "set_heat_flow_temperature_zone_2")
                    rename_key(dev, "set_temperature_zone1", "set_temperature_zone_1")
                    rename_key(dev, "set_temperature_zone2", "set_temperature_zone_2")
                    rename_key(dev, "sp_timeout", "SP_timeout")
                    rename_key(dev, "ssl_expiration_date", "SSL_expiration_date")
                    rename_key(dev, "target_hc_temperature_zone1", "target_hc_temperature_zone_1")
                    rename_key(dev, "target_hc_temperature_zone2", "target_hc_temperature_zone_2")
                    rename_key(dev, "thermostat_status_zone1", "thermostat_status_zone_1")
                    rename_key(dev, "thermostat_status_zone2", "thermostat_status_zone_2")
                    rename_key(dev, "thermostat_temperature_zone1", "thermostat_temperature_zone_1")
                    rename_key(dev, "thermostat_temperature_zone2", "thermostat_temperature_zone_2")
                    rename_key(dev, "thermostat_type_zone1", "thermostat_type_zone_1")
                    rename_key(dev, "thermostat_type_zone2", "thermostat_type_zone_2")
                    rename_key(dev, "time_zone", "timezone")
                    rename_key(dev, "time_zone_id", "timezone_id")
                    rename_key(dev, "valve_status2_way", "valve_status_2_way")
                    rename_key(dev, "valve_status2_way2a", "valve_status_2_way_2a")
                    rename_key(dev, "valve_status2_way2b", "valve_status_2_way_2b")
                    rename_key(dev, "valve_status3_way", "valve_status_3_way")
                    rename_key(dev, "water_pump1_status", "water_pump_1_status")
                    rename_key(dev, "water_pump2_status", "water_pump_2_status")
                    rename_key(dev, "water_pump3_status", "water_pump_3_status")
                    rename_key(dev, "water_pump4_status", "water_pump_4_status")
                    rename_key(dev, "zone1_in_cool_mode", "zone_1_in_cool_mode")
                    rename_key(dev, "zone1_in_heat_mode", "zone_1_in_heat_mode")
                    rename_key(dev, "zone1_in_room_mode", "zone_1_in_room_mode")
                    rename_key(dev, "zone1_name", "zone_1_name")
                    rename_key(dev, "zone2_in_cool_mode", "zone_2_in_cool_mode")
                    rename_key(dev, "zone2_in_heat_mode", "zone_2_in_heat_mode")
                    rename_key(dev, "zone2_in_room_mode", "zone_2_in_room_mode")
                    rename_key(dev, "zone2_master", "zone_2_master")
                    rename_key(dev, "zone2_name", "zone_2_name")

                    device_obj = Device(**dev)

                    floor_device_objects.append(device_obj)
                    device_objects.append(device_obj)

                f["devices"] = floor_device_objects
                floor = Floor(**f)
                floor_objects.append(floor)

            building = Building(**d, devices=device_objects, floors=floor_objects)
            self.buildings.append(building)
