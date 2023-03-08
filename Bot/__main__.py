import os
from dotenv import load_dotenv
from uvloop import install
from pyrogram.types import Message
from Bot import *
from pyrogram import filters
from Bot.database.exdb import *
import os
import re
from itertools import count
from Bot import app

from pyrogram import Client, filters
from pyrogram.types import Message

import re

import re
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

no plugin loaded from "Bot/modules/bot"

app = Client(
  name="app",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN,
  workers=BOT_WORKERS,
  in_memory=True,
  )

app.run()
for all_module in ALL_MODULES:
        importlib.import_module("Bot.modules" + all_module)