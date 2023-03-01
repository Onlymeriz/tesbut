import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message
from Bot import *

# Fungsi untuk membuat file .env dan mengisi nama session di dalamnya


# Fungsi yang akan dijalankan ketika pengguna memasukkan nama file .env dan session name
import os
from pyrogram import Client, filters

# Membuat klien Pyrogram

# Definisikan perintah untuk membuat file .env
@app.on_message(filters.command("create_env") & filters.private)
async def create_env(client, message):
    # Looping untuk membuat file .env1 sampai .env100
    for i in range(1, 101):
        filename = f".env{i}"
        if not os.path.isfile(filename):
            # Jika file belum ada, maka buat file baru dan isi dengan string session
            with open(filename, "w") as file:
                file.write(f"SESSION={message.text.split(' ')[1]}")
            # Kirim file .env ke pengguna
            await message.reply_document(filename)
            break

# Jalankan bot
app.run()
