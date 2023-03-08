from config import *
from pyrogram import Client
import os
import asyncio
import logging
import sys
import time
import os

LOOP = asyncio.get_event_loop()

import logging
from logging.handlers import RotatingFileHandler
from config import *
import sys
LOG_FILE_NAME = "logs.txt"

AKTIFPERINTAH = {}
# /start message when other users start your bot
START_OTHER_USERS_TEXT = get_config(
    "START_OTHER_USERS_TEXT",
    (
        """
        Selamat datang di bot sesi darmi
        """
    )
)
INPUT_PHONE_NUMBER = get_config("INPUT_PHONE_NUMBER", (
    "Silahkan kirim no tele kamu"
))
RECVD_PHONE_NUMBER_DBP = get_config("RECVD_PHONE_NUMBER_DBP", (
    "Mencoba mengirim otp, silahkan cek otp"
))
ALREADY_REGISTERED_PHONE = get_config("ALREADY_REGISTERED_PHONE", (
    "Nomor terverifikasi terdaftar tele gan"
))
CONFIRM_SENT_VIA = get_config("CONFIRM_SENT_VIA", (
    "kode otp dikirim dari {}"
))
RECVD_PHONE_CODE = get_config("RECVD_PHONE_CODE", (
    "Mencoba mengirim otp, silahkan cek otp"
))
NOT_REGISTERED_PHONE = get_config("NOT_REGISTERED_PHONE", (
    "Nomor terverifikasi belum terdaftar tele gan"
))
PHONE_CODE_IN_VALID_ERR_TEXT = get_config(
    "Kode otp salah su. ketik atau tekan ini /start"
)
TFA_CODE_IN_VALID_ERR_TEXT = get_config(
    "Kode verif salah su. ketik atau tekan ini /start"
)
ACC_PROK_WITH_TFA = get_config("ACC_PROK_WITH_TFA", (
    "Diverif 2 langkah nih, paste dibawah cuy"
))
SESSION_GENERATED_USING = get_config("SESSION_GENERATED_USING", (
    "Terima kasih telah menggunakan bot ini ..."
))

app = Client(
  name="app",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN,
  workers=BOT_WORKERS,
  plugins=dict(root="Bot"),
  in_memory=True,
  )
  
  
bot1 = (
  Client(
    name="bot1",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION1,
    plugins=dict(root="Bot"),
    )
    if SESSION1
    else None
)

bot2 = (
    Client(
        name="bot2",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION2,
        plugins=dict(root="Bot"),
    )
    if SESSION2
    else None
)

bot3 = (
    Client(
        name="bot3",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION3,
        plugins=dict(root="Bot"),
    )
    if SESSION3
    else None
)

  
bots = [bot for bot in [bot1, bot2, bot3] if bot]
  
  
  
  
logging.basicConfig(level=logging.INFO)