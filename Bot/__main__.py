import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from uvloop import install
from pyrogram.types import Message
from Bot import *
from Bot.database.exdb import *
import os
from itertools import count
from pyrogram import Client, filters
from pyrogram.errors import SessionPasswordNeeded
from pyrogram.session import Session


import os
import importlib
from pyrogram import Client, idle

command_filter = filters.private & filters.command("buat") & filters.user(ADMINS) & ~filters.via_bot


filename = ".env"

if os.path.isfile(filename):
    with open(filename, "r") as file:
        contents = file.read()
    session_list = re.findall(r"(SESSION\d+)=.*", contents)
    session_index = len(session_list) + 2
else:
    session_index = 2

@app.on_message(command_filter)
async def create_env(client, message):
    global session_index  # tambahkan ini
    with open(filename, "a") as file:
        file.write(f"\nSESSION{session_index}={message.text.split()[2]}")
        load_dotenv()
    await message.reply_text(f"Session berhasil disimpan pada {filename} dengan Posisi SESSION{session_index}.")
    session_index += 1
    
    
    
app.run()

