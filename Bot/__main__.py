import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message
from Bot import *
from Bot.database.exdb import *

# Fungsi untuk membuat file .env dan mengisi nama session di dalamnya


# Fungsi yang akan dijalankan ketika pengguna memasukkan nama file .env dan session name
import os
from pyrogram import Client, filters

# Membuat klien Pyrogram

# Definisikan perintah untuk membuat file .env
@app.on_message(filters.command("buat") & filters.private)
async def create_new_env(client, message):
    for i in range(1, 201):
      session_string = f"SESSION{i}={message.text.split()[1]}"
      env_filename = create_env_file(session_string)
      await message.reply_text(
        f"`Sukses Dikirim dengan nama `{env_filename}")

# Jalankan bot
app.run()
