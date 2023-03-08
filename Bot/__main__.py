import os
from dotenv import load_dotenv
from uvloop import install
from pyrogram.types import Message
from Bot import *
from pyrogram import filters
from Bot.database.exdb import *
import os
import re
from itertools import count
from Bot import app

from pyrogram import Client, filters
from pyrogram.types import Message

import re

@app.on_message(filters.command("start"))
async def start_command_handler(client: Client, message: Message):
    await client.send_message(
        chat_id=message.chat.id,
        text="Halo! Silakan masukkan nomor telepon Anda dengan kode negara +62 atau +23 untuk membuat string session Pyrogram versi 2."
    )

@app.on_message(filters.regex(r"^\+(62)\d{10,12}$"))
async def phone_number_handler(client: Client, message: Message):
    phone_number = message.text
    session_name = phone_number
    try:
        await client.send_code(phone_number)
        code = input("Masukkan kode verifikasi Anda: ")
        user = await client.sign_in(phone_number, code)
        string_session = await client.export_session_string()
        await client.send_message(
            chat_id=message.chat.id,
            text=f"String session Pyrogram Anda: {string_session}"
        )
    except Exception as e:
        await client.send_message(
            chat_id=message.chat.id,
            text=f"Terjadi kesalahan: {e}"
        )




app.run()
