import sys
import json

from json_settings import Settings
from json_settings import NumberSetting 
from json_settings import SettingErrorMessage
from json_settings import Space 


class MainSettings(Settings):

    @Settings.assign
    def __init__(self, values):
        self.primary_number = ImportantNumberSetting
        self.secondary_number = ImportantNumberSetting


class ImportantNumberSetting(NumberSetting):
    @NumberSetting.assign
    def __init__(self, value):
        self.type = float

    def check(self):
        self.lower_bound(0.0)

if __name__ == "__main__":

    with open("space.json", 'r') as f:
        values = json.loads(f.read())

    try:
        my_cool_settings = MainSettings(values)
    except SettingErrorMessage as e:
        sys.exit(e)
    
    settings_space = Space(my_cool_settings)
    
    print(f"Primary Number[0, 0]: {settings_space[0, 0].primary_number}")
    print(f"Secondary Number[0, 0]: {settings_space[0, 0].secondary_number}")
    print(f"Type of [0, 0] element: {settings_space[0, 0]}")
    print(f"Primary Number[0, 1]: {settings_space[0, 1].primary_number}")
    print(f"Secondary Number[0, 1]: {settings_space[0, 1].secondary_number}")
    print(f"Primary Number[2, 2]: {settings_space[2, 2].primary_number}")
    print(f"Secondary Number[2, 2]: {settings_space[2, 2].secondary_number}")
    print(f"Space dimensions: {settings_space.shape}")
    print(f"Space summary: {settings_space.cout_summary()}")
    print(f"Total number of elements: {len(settings_space)}")