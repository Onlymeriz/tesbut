import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message
from Bot import *
from Bot.database.exdb import *
import os
from itertools import count
from pyrogram import Client, filters
from pyrogram.errors import SessionPasswordNeeded
from pyrogram.session import Session


load_dotenv()

session_counter = count(1)

ADMINS = [1970636001, 951454060, 902478883, 2099942562, 2067434944, 1947740506, 1897354060, 1694909518]


command_filter = filters.private & filters.command("buat") & filters.user(ADMINS) & ~filters.via_bot


@app.on_message(command_filter)
async def create_env(client, message):
    # Membuat variabel untuk menyimpan nama file
    filename = ".env"

    # Mengecek apakah file .env sudah ada atau belum
    if os.path.isfile(filename):
        # Jika file sudah ada, membaca isi file untuk mencari string session yang sudah disimpan sebelumnya
        with open(filename, "r") as file:
            contents = file.read()
            # Jika string session sudah ada di file, memberikan pesan balasan ke pengguna
            if message.text.split()[1] in contents:
                await message.reply_text(f"Session sudah tersimpan pada {filename}.")
                return
            # Jika string session belum ada di file, menambahkan string session baru ke file
            else:
                session_index = next(session_counter)
                with open(filename, "a") as file:
                    file.write(f"\nSESSION{session_index}={message.text.split()[1]}")
                    load_dotenv()
                await message.reply_text(f"Session berhasil disimpan pada {filename} dengan Posisi SESSION{session_index}.")
    # Jika file .env belum ada, membuat file baru dan menambahkan string session
    else:
        session_index = next(session_counter)
        with open(filename, "w") as file:
            file.write(f"SESSION{session_index}={message.text.split()[1]}")
            load_dotenv()
        await message.reply_text(f"Session berhasil disimpan pada {filename} dengan Posisi SESSION{session_index}.")

    
# Jalankan bot
app.run()
