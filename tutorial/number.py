import sys
import json

from json_settings import Settings
from json_settings import NumberSetting 
from json_settings import SettingErrorMessage


class MainSettings(Settings):

    @Settings.assign
    def __init__(self, values):
        self.important_number = ImportantNumberSetting


class ImportantNumberSetting(NumberSetting):
    @NumberSetting.assign
    def __init__(self, value):
        self.type = float

    def check(self):
        self.lower_bound(0.0)

if __name__ == "__main__":

    with open("number.json", 'r') as f:
        values = json.loads(f.read())

    try:
        my_cool_settings = MainSettings(values)
    except SettingErrorMessage as e:
        sys.exit(e)
    
    print(f"Important Number is: {my_cool_settings.important_number}")