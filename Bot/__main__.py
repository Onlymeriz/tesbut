import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message
from Bot import *

# Fungsi untuk membuat file .env dan mengisi nama session di dalamnya
def create_env_file(session_name: str):
    with open('.env', 'w') as f:
        f.write(f"API_ID={os.environ.get('API_ID')}\n")
        f.write(f"API_HASH={os.environ.get('API_HASH')}\n")
        f.write(f"BOT_TOKEN={os.environ.get('BOT_TOKEN')}\n")
        f.write(f"SESSION_NAME={session_name}")


# Membuat instance Pyrogram Client


# Fungsi yang akan dijalankan ketika pengguna memasukkan nama file .env dan session name
@bot.on_messa@app.on_message(filters.command(["create_env"]))
async def create_env_file(client, message):
    # Ambil argumen nama file .env dari pesan
    env_file_name = message.text.split(" ")[100] + ".env"

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
