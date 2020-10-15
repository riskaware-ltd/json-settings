import sys
import json

from json_settings import Settings
from json_settings import StringSetSetting
from json_settings import SettingErrorMessage 


class MainSettings(Settings):

    @Settings.assign
    def __init__(self, values):
        self.vehicle_type = VehicleTypeSetting


class VehicleTypeSetting(StringSetSetting):
    @StringSetSetting.assign
    def __init__(self, value):
        self.options = [
            "car",
            "plane",
            "boat"
        ]

if __name__ == "__main__":

    with open("stringset.json", 'r') as f:
        values = json.loads(f.read())

    try:
        my_cool_settings = MainSettings(values)
    except SettingErrorMessage as e:
        sys.exit(e)
    