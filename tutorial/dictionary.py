import sys
import json

from json_settings import Settings
from json_settings import DictionarySetting 
from json_settings import StringSetSetting
from json_settings import SettingErrorMessage


class MainSettings(Settings):

    @Settings.assign
    def __init__(self, values):
        self.entries = EntryDictionarySetting 

class EntryDictionarySetting(DictionarySetting):
    @DictionarySetting.assign
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

    with open("dictionary.json", 'r') as f:
        values = json.loads(f.read())

    try:
        my_cool_settings = MainSettings(values)
    except SettingErrorMessage as e:
        sys.exit(e)
    
    print(f"Element type: {type(my_cool_settings.entries['cheap_car'])}")
    print(f"First element.kind: {my_cool_settings.entries['cheap_car'].kind}")
    print(f"First element.cost: {my_cool_settings.entries['cheap_car'].cost}")
    print(f"Third element.kind: {my_cool_settings.entries['cheap_plane'].kind}")
    print(f"Third element.cost: {my_cool_settings.entries['cheap_plane'].cost}")
    