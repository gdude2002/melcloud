# coding=utf-8
from datetime import datetime

from dataclasses import dataclass

__author__ = "Gareth Coles"


@dataclass
class WeatherObservation:
    condition: int
    condition_name: str
    date: datetime
    day: int
    humidity: int
    icon: str
    id: int
    sunrise: datetime
    sunset: datetime
    temperature: int
    weather_type: int
