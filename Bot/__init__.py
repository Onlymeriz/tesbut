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



app = Client(
  name="app",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN,
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