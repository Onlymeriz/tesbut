from config import *
from pyrogram import Client
import os
import logging

API_ID="1634450"
API_HASH="1a42e816cae8d86e71a4c466bba19b8c"
BOT_TOKEN="6279149779:AAEFnmoUUcxfMeceZQJ4_E3lETYlaqWjciU"

app = Client(
  name="app",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN,
  )
  
  logging.basicConfig(level=logging.INFO)