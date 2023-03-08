from config import *
from pyrogram import Client
import os
import asyncio
import logging
import sys
import time
import os

LOOP = asyncio.get_event_loop()

import logging
from logging.handlers import RotatingFileHandler
from config import *
import sys
LOG_FILE_NAME = "logs.txt"

AKTIFPERINTAH = {}
# /start message when other users start your bot


app = Client(
  name="app",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN,
  workers=BOT_WORKERS,
  plugins=dict(root="Bot/modules/bot"),
  in_memory=True,
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