import sys
import json

from json_settings import Settings
from json_settings import ListSetting
from json_settings import StringSetSetting
from json_settings import SettingErrorMessage


class MainSettings(Settings):

    @Settings.assign
    def __init__(self, values):
        self.entries = EntryListSetting 

class EntryListSetting(ListSetting):
    @ListSetting.assign
    def __init__(self, values):
        self.type = EntrySetting

class EntrySetting(Settings):
    @Settings.assign
    def __init__(self, values):
        self.kind = VehicleTypeSetting
        self.cost = int

class VehicleTypeSetting(StringSetSetting):
    @StringSetSetting.assign
    def __init__(self, value):
        self.options = [
            "car",
            "plane",
            "boat"
        ]

if __name__ == "__main__":

    with open("list.json", 'r') as f:
        values = json.loads(f.read())

    try:
        my_cool_settings = MainSettings(values)
    except SettingErrorMessage as e:
        sys.exit(e)
    
    print(f"Element type: {type(my_cool_settings.entries[0])}")
    print(f"First element.kind: {my_cool_settings.entries[0].kind}")
    print(f"First element.cost: {my_cool_settings.entries[0].cost}")
    print(f"Third element.kind: {my_cool_settings.entries[2].kind}")
    print(f"Third element.cost: {my_cool_settings.entries[2].cost}")
