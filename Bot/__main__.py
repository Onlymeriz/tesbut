import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message
from Bot import *

# Fungsi untuk membuat file .env dan mengisi nama session di dalamnya


# Fungsi yang akan dijalankan ketika pengguna memasukkan nama file .env dan session name
@app.on_message(filters.command(["create_env"]))
async def create_env_file(client, message):
    # Ambil argumen nama file .env dari pesan
    env_file_name = message.text.split(" ")[1] + ".env"

    # Tanyakan kepada pengguna untuk memberikan string session
    await message.reply("Silakan berikan string session:")

    # Tangkap string session dari pesan balasan pengguna
    @app.on_message(filters.private & filters.text)
    async def get_string_session(client, message):
        # Simpan string session ke dalam file .env
        with open(env_file_name, "w") as f:
            f.write(f"STRING_SESSION={message.text}")
        await message.reply(f"File {env_file_name} berhasil dibuat dan string session berhasil disimpan.")

        # Hapus callback tangkap string session
        app.remove_handler(get_string_session)

# Jalankan bot Pyrogram
app.run()
