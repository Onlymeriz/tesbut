import asyncio
import logging
import os
import sys
import json
import asyncio
import time
import spamwatch
import telegram.ext as tg


from ptbcontrib.postgres_persistence import PostgresPersistence

StartTime = time.time()

def get_user_list(__init__, key):
    with open("{}/Bot/{}".format(os.getcwd(), __init__), "r") as json_file:
        return json.load(json_file)[key]

# enable logging
FORMAT = "[Kynan] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)

logging.getLogger('ptbcontrib.postgres_persistence.postgrespersistence').setLevel(logging.WARNING)

LOGGER = logging.getLogger('[Kynan]')
LOGGER.info("Kynan is starting. | An Kynan Robot Parts. | Licensed under GPLv3.")

# if version < 3.9, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 8:
    LOGGER.error(
        "You MUST have a python version of at least 3.8! Multiple features depend on this. Bot quitting."
    )
    sys.exit(1)

ENV = bool(os.environ.get("ENV", False))

TOKEN = os.environ.get("TOKEN", None)

from Bot.config import Development as Config

TOKEN = Config.TOKEN

  

defaults = tg.Defaults(run_async=True)
updater = tg.Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher


BOT_ID = dispatcher.bot.id
BOT_NAME = dispatcher.bot.first_name
BOT_USERNAME = dispatcher.bot.username


loop = asyncio.get_event_loop()


# make sure the regex handler can take extra kwargs
