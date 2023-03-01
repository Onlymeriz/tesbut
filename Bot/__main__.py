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
@bot.on_message(filters.private & filters.text)
def handle_message(bot: Client, message: Message):
    if message.text.startswith('/start'):
        bot.send_message(
            chat_id=message.chat.id,
            text='Hai! Silakan masukkan nama file .env yang ingin kamu buat.'
        )
    elif message.text.endswith('.env'):
        session_name = input('Silakan masukkan session name yang ingin kamu gunakan: ')
        create_env_file(session_name)
        load_dotenv('.env')
        bot.send_message(
            chat_id=message.chat.id,
            text=f'File .env dengan nama {message.text} sudah berhasil dibuat dan di-load. '
                 f'String session kamu adalah {session_name}.'
        )


# Jalankan bot
bot.run()
