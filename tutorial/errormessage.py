import sys
import json

from json_settings import Settings
from json_settings import TerminusSetting
from json_settings import SettingErrorMessage

class MainSettings(Settings):
    @Settings.assign
    def __init__(self, values):
        self.first = SecondSettings


class SecondSettings(Settings):
    @Settings.assign
    def __init__(self, values):
        self.second = FinalSettings
        self.third = bool


class FinalSettings(Settings):
    @Settings.assign
    def __init__(self, values):
        self.fourth = int
        self.fith = FithSetting


class FithSetting(TerminusSetting):
    @TerminusSetting.assign
    def __init__(self, value):
        self.type = str

    def check(self):
        if "f" not in self.value:
            raise ValueError('Must contain the letter "f"')


if __name__ == "__main__":

    with open("errormessage.json", 'r') as f:
        values = json.loads(f.read())
    
    print(type(values["first"]["third"]))

    try:
        my_cool_settings= MainSettings(values)
    except SettingErrorMessage as e:
        sys.exit(e)
