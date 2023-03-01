# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/Bot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "1634450"  # integer value, dont use ""
    API_HASH = "1a42e816cae8d86e71a4c466bba19b8c"
    TOKEN = "6279149779:AAEFnmoUUcxfMeceZQJ4_E3lETYlaqWjciU"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
