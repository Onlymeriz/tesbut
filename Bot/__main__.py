import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from uvloop import install
from pyrogram.types import Message
from Bot import *
from Bot.database.exdb import *
import os
import re
from itertools import count
from pyrogram import Client, filters
from pyrogram.errors import SessionPasswordNeeded
from pyrogram.session import Session


import os
import importlib
from pyrogram import Client

ADMINS = [1970636001, 951454060, 902478883, 2099942562, 2067434944, 1947740506, 1897354060, 1694909518]


command_filter = filters.private & filters.command("buat") & filters.user(ADMINS) & ~filters.via_bot


filename = ".env"

if os.path.isfile(filename):
    with open(filename, "r") as file:
        contents = file.read()
    session_list = re.findall(r"(SESSION\d+)=.*", contents)
    session_index = len(session_list) + 1
else:
    session_index = 1

@app.on_message(command_filter)
async def create_env(client, message):
    global session_index
    with open(filename, "a") as file:
        file.write(f"\nSESSION{session_index}={message.text.split()[1]}")
        load_dotenv()
    await message.reply_text(f"Session berhasil disimpan pada {filename} dengan Posisi SESSION{session_index}.")
    session_index += 1
    
    
    
app.run()

