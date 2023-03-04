import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message
from Bot import *
from Bot.database.exdb import *
import os
from pyrogram import Client, filters
from pyrogram.errors import SessionPasswordNeeded
from pyrogram.session import Session


load_dotenv()

ADMINS = [1970636001, 951454060, 902478883, 2099942562, 2067434944, 1947740506, 1897354060, 1694909518]

@app.on_message(
    filters.private & filters.command("buat") & filters.user(ADMINS) & ~filters.via_bot
)
async def create_env(client, message):
    session_index = 1
    while True:
        filename = f".env{session_index}"
        if os.path.isfile(filename):
            with open(filename, "r") as file:
                contents = file.read()
                if message.text.split()[1] in contents:
                    await message.reply_text(f"Session sudah tersimpan pada {filename}.")
                    return
            session_index += 1
        else:
            with open(filename, "w") as file:
                file.write(f"SESSION{session_index}={message.text.split()[1]}")
                load_dotenv()
            await message.reply_text(f"Session berhasil disimpan pada {filename} dengan Posisi SESSION{session_index}.")
            break

    
# Jalankan bot
app.run()
