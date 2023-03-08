from config import *
from pyrogram import Client
import os
import asyncio
import logging
import sys
import time
import os

API_ID="1634450"
API_HASH="1a42e816cae8d86e71a4c466bba19b8c"
BOT_TOKEN="6279149779:AAEFnmoUUcxfMeceZQJ4_E3lETYlaqWjciU"

LOOP = asyncio.get_event_loop()

import logging
from logging.handlers import RotatingFileHandler
from config import *
import sys
LOG_FILE_NAME = "logs.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("asyncio").setLevel(logging.CRITICAL)
logging.getLogger("pytgcalls").setLevel(logging.WARNING)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.client").setLevel(logging.WARNING)
logging.getLogger("pyrogram.session.auth").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.session.session").setLevel(logging.CRITICAL)
logging.basicConfig(level=logging.INFO)

LOGS = logging.getLogger(__name__)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

if not BOT_TOKEN:
   LOGGER(__name__).error("WARNING: BOT TOKEN TIDAK DITEMUKAN, SHUTDOWN BOT")
   sys.exit()

app = Client(
  name="app",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN,
  plugins=dict(root="Bot",
  )
  
  
bot1 = (
  Client(
    name="bot1",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION1,
    plugins=dict(root="Bot"),
    )
    if SESSION1
    else None
)

bot2 = (
    Client(
        name="bot2",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION2,
        plugins=dict(root="Bot"),
    )
    if SESSION2
    else None
)

bot3 = (
    Client(
        name="bot3",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION3,
        plugins=dict(root="Bot"),
    )
    if SESSION3
    else None
)

  
bots = [bot for bot in [bot1, bot2, bot3] if bot]
  
  
  
  
logging.basicConfig(level=logging.INFO)