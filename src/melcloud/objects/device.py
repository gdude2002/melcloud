# coding=utf-8
from datetime import datetime
from typing import List

from dataclasses import dataclass

from melcloud.objects.preset import Preset
from melcloud.objects.weather import WeatherObservation
from melcloud.utils import str_to_datetime

__author__ = "Gareth Coles"


@dataclass
class Device:
    access_level: int
    adaptor_type: int
    allow_dual_room_temperature: bool
    area_id: int
    area_name: str
    boiler_status: bool
    booster_heater_1_status: bool
    booster_heater_2_plus_status: bool
    booster_heater_2_status: bool
    building_country: int
    building_id: int
    building_name: str
    can_cool: bool
    can_estimate_energy_usage: bool
    can_heat: bool
    can_measure_energy_consumed: bool
    can_measure_energy_produced: bool
    can_set_eco_hot_water: bool
    can_set_flow_temperature: bool
    can_set_forced_hot_water: bool
    can_set_operation_mode: bool
    can_set_power: bool
    can_set_tank_temperature: bool
    can_set_tank_water_temperature: bool
    can_set_temperature_increment_override: bool
    can_use_room_temperature_cooling: bool
    cooling_energy_consumed_rate_1: int
    cooling_energy_consumed_rate_2: int
    cooling_energy_produced_rate_1: int
    cooling_energy_produced_rate_2: int
    CSV_report_1_min: bool
    current_energy_consumed: int
    current_energy_mode: object  # ???
    current_energy_produced: int
    daily_energy_consumed_date: datetime
    daily_energy_produced_date: datetime
    date_created: datetime
    DECC_report: bool
    defrost_mode: int
    detected_country: int
    device_id: int
    device_name: str
    device_type: int
    diagnostic_end_date: object  # ???
    diagnostic_mode: int
    dip_switch_1: int
    dip_switch_2: int
    dip_switch_3: int
    dip_switch_4: int
    direct_access: bool
    eco_hot_water: bool
    effective_flags: 1
    effective_pcycle: int
    end_date: datetime
    error_code: int
    error_code_2_digit: int
    expected_command: int
    firmware_app_version: int
    firmware_deployment: object  # ???
    firmware_update_aborted: bool
    firmware_web_version: int
    firmware_wlan_version: int
    flash_writes: int
    floor_id: int
    floor_name: str
    flow_temperature: int
    flow_temperature_boiler: int
    flow_temperature_zone_1: int
    flow_temperature_zone_2: int
    forced_hot_water_mode: bool
    FTC_model: int
    FTC_revision: str
    FTC_version: int
    has_eco_cute_settings: bool
    has_energy_consumed_meter: bool
    has_energy_produced_meter: bool
    has_error: bool
    has_error_messages: bool
    has_FTC_45_settings: bool
    has_hot_water_tank: bool
    has_simplified_zone_2: bool
    has_thermostat_zone_1: bool
    has_thermostat_zone_2: bool
    has_zone_2: bool
    heating_energy_consumed_rate_1: int
    heating_energy_consumed_rate_2: int
    heating_energy_produced_rate_1: int
    heating_energy_produced_rate_2: int
    heating_function_enabled: bool
    heat_pump_frequency: int
    hide_dry_mode_control: bool
    hide_outdoor_temperature: bool
    hide_room_temperature: bool
    hide_supply_temperature: bool
    hide_vane_controls: bool
    holiday_mode: bool
    hot_water_energy_consumed_rate_1: int
    hot_water_energy_consumed_rate_2: int
    hot_water_energy_produced_rate_1: int
    hot_water_energy_produced_rate_2: int
    idle_zone_1: bool
    idle_zone_2: bool
    image_id: int
    immersion_heater_status: bool
    installation_date: datetime
    is_FTC_model_supported: bool
    last_effective_flags: int
    last_FTC_revision: str
    last_FTC_version: int
    last_reset: datetime
    last_service_date: datetime
    last_time_stamp: datetime
    local_ip_address: str
    location: int
    mac_address: str
    max_indoor_units: int
    max_outdoor_units: int
    max_pcycle: int
    max_set_temperature: int
    max_tank_temperature: int
    max_temperature: int
    max_temperature_control_units: int
    min_pcycle: int
    min_set_temperature: int
    min_temperature: int
    offline: bool
    operation_mode: int
    operation_mode_zone_1: int
    operation_mode_zone_2: int
    outdoor_temperature: int
    owner: object  # ???
    owner_country: int
    owner_email: str
    owner_id: int
    owner_name: str
    passcode: object  # ???
    pcycle: int
    pending_request_special_functions: int
    pending_send_special_functions: int
    position: str
    power: bool
    prohibit_cooling_zone_1: bool
    prohibit_cooling_zone_2: bool
    prohibit_heating_zone_1: bool
    prohibit_heating_zone_2: bool
    prohibit_hot_water: bool
    protocol_version: int
    rate_1_start_time: object  # ???
    rate_2_start_time: object  # ???
    record_num_max: int
    refrigerant_address: int
    registrations: int
    registration_reason: object  # ???
    registration_retry: object  # ???
    request_special_functions: int
    return_temperature: int
    return_temperature_boiler: int
    return_temperature_zone_1: int
    return_temperature_zone_2: int
    room_temperature_zone_1: float
    room_temperature_zone_2: float
    scene: object  # ???
    secondary_zone_heat_curve: bool
    send_special_functions: int
    serial_number: int
    server_communication_disabled: bool
    server_timer_desired: bool
    server_timer_enabled: bool
    set_cool_flow_temperature_zone_1: int
    set_cool_flow_temperature_zone_2: int
    set_heat_flow_temperature_zone_1: int
    set_heat_flow_temperature_zone_2: int
    set_tank_water_temperature: int
    set_temperature_zone_1: int
    set_temperature_zone_2: int
    special_functions_state: int
    SP_timeout: object  # ???
    SSL_expiration_date: object  # ???
    tank_water_temperature: int
    target_hc_temperature_zone_1: int
    target_hc_temperature_zone_2: int
    temperature_increment: float
    temperature_increment_override: int
    thermostat_status_zone_1: bool
    thermostat_status_zone_2: bool
    thermostat_temperature_zone_1: int
    thermostat_temperature_zone_2: int
    thermostat_type_zone_1: bool
    thermostat_type_zone_2: bool
    timezone: int
    timezone_id: int
    type: int
    unit_status: int
    unit_version: int
    valve_status_2_way: bool
    valve_status_2_way_2a: bool
    valve_status_2_way_2b: bool
    valve_status_3_way: bool
    water_pump_1_status: bool
    water_pump_2_status: bool
    water_pump_3_status: bool
    water_pump_4_status: bool
    wifi_adapter_status: str  # Enum later???
    wifi_signal_strength: int
    zone_1_in_cool_mode: bool
    zone_1_in_heat_mode: bool
    zone_1_in_room_mode: bool
    zone_1_name: str
    zone_2_in_cool_mode: bool
    zone_2_in_heat_mode: bool
    zone_2_in_room_mode: bool
    zone_2_master: bool
    zone_2_name: str

    presets: List[Preset]

    has_pending_command: bool = None
    last_communication: datetime = None
    next_communication: datetime = None
    prohibit_zone1: bool = None
    prohibit_zone2: bool = None
    scene_owner: object = None  # ???
    weather_observations: List[WeatherObservation] = None

    def update_from_device_info(self, data):
        if self.weather_observations is None:
            self.weather_observations = []

        self.weather_observations.clear()

        self.has_pending_command = data["has_pending_command"]
        self.last_communication = str_to_datetime(data["last_communication"])
        self.next_communication = str_to_datetime(data["next_communication"])
        self.prohibit_zone1 = data["prohibit_zone1"]
        self.prohibit_zone2 = data["prohibit_zone2"]
        self.scene_owner = data["scene_owner"]

        for observation in data["weather_observations"]:
            self.weather_observations.append(WeatherObservation(**observation))
