from config import *
from pyrogram import Client
import os
import asyncio
import logging
import sys
import time
import os
from ast import parse

LOOP = asyncio.get_event_loop()

import logging
from logging.handlers import RotatingFileHandler
from config import *
import sys
LOG_FILE_NAME = "logs.txt"

AKTIFPERINTAH = {}
# /start message when other users start your bot

def LOGGER(name: str) -> logging.Logger:
    """ get a Logger object """
    return logging.getLogger(name)

class User(Client):
    """ modded client for SessionMakerUser """
    def __init__(self):
        super().__init__(
            name="tu",
            api_hash=API_HASH,
            api_id=APP_ID,
            workers=BOT_WORKERS,
            in_memory=True,
            parse_mode=enums.ParseMode.HTML
        )
        self.LOGGER = LOGGER


app = Client(
  name="app",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN,
  workers=BOT_WORKERS,
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