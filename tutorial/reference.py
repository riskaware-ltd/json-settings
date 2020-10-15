import json

from json_settings import Settings

class FootwareSettings(Settings):

    @Settings.assign
    def __init__(self, values):
        self.type = str
        self.quantity = int

class MyCoolSetting(Settings):

    @Settings.assign
    def __init__(self, value: dict):
        self.footware = FootwareSettings 
        self.gloves = bool

if __name__ == "__main__":

    with open("reference.json", 'r') as f:
        values = json.loads(f.read())

    my_cool_setting = MyCoolSetting(values)

    print(my_cool_setting.footware.type)
    print(my_cool_setting.footware.quantity)
    print(my_cool_setting.gloves)