# coding=utf-8
import asyncio
from melcloud import MELCloud, AsyncConnection
from melcloud.constants import Languages

__author__ = "Gareth Coles"

platform = MELCloud(Languages.EN, connection=AsyncConnection)


async def run():
    await platform.login("<EMAIL ADDRESS>", "<PASSWORD>")

    if platform.logged_in:
        print(f"Logged in as {platform.account.name}")
        await platform.load_devices()

        for building in platform.buildings:
            print(f"Building: {building.id} ({building.name})")

            for floor in building.floors:
                print(f"> Floor: {floor.id} ({floor.name})")

                for device in floor.devices:
                    print(f">> Device: {device.device_id} ({device.device_name})")
                    print(f"   Zone 1: Currently: {device.room_temperature_zone_1}, Target: {device.set_temperature_zone_1}")
                    print(f"   Zone 2: Currently: {device.room_temperature_zone_2}, Target: {device.set_temperature_zone_2}")
                    print(f"   Current weather: {device.weather_observations[0].condition_name}")

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
