import json

from json_settings import Settings

class MyCoolSetting(Settings):

    @Settings.assign
    def __init__(self, value: dict):
        self.my_integer = int

if __name__ == "__main__":

    with open("primitive.json", 'r') as f:
        values = json.loads(f.read())

    my_cool_setting = MyCoolSetting(values)

    print(my_cool_setting.my_integer)
    print(type(my_cool_setting.my_integer))