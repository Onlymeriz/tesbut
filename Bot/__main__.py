import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message
from Bot import *
from Bot.database.exdb import *
import os
from pyrogram import Client, filters
import pyrogram
from pyrogram import Client


@app.on_message()
async def start(client, message):
    # Kirim pesan permintaan nomor telepon
    await message.reply_text("Silakan kirim nomor telepon Anda untuk membuat string session.")

@app.on_message(pyrogram.filters.regex(r"\+\d+"))
async def generate_session(client, message):
    # Mengambil nomor telepon dari pesan pengguna
    phone_number = message.text
    
    # Membuat string session
    with bot:
        session = await bot.create_session_string(phone_number)
        
    # Kirim string session ke pengguna
    await message.reply_text(f"Ini adalah string session Anda:\n\n{session}")
    
# Jalankan bot
app.run()
