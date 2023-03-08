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

@app.on_message(filters.command("start"))
def start_command_handler(client: Client, message: Message):
    client.send_message(
        chat_id=message.chat.id,
        text="Halo! Silakan masukkan nomor telepon Anda untuk membuat string session Pyrogram versi 2."
    )

@app.on_message(filters.regex(r"^\+\d{10,12}$"))
def phone_number_handler(client: Client, message: Message):
    phone_number = message.text
    session_name = phone_number
    try:
        client.send_code(phone_number)
        code = input("Masukkan kode verifikasi Anda: ")
        user = client.sign_in(phone_number, code)
        string_session = client.export_session_string()
        client.send_message(
            chat_id=message.chat.id,
            text=f"String session Pyrogram Anda: {string_session}"
        )
    except Exception as e:
        client.send_message(
            chat_id=message.chat.id,
            text=f"Terjadi kesalahan: {e}"
        )

app.run()
