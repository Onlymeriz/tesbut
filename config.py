import os
from os import getenv
from dotenv import load_dotenv

load_dotenv(".env")

API_ID = int(getenv("API_ID", "22156937"))

API_HASH = getenv("API_HASH", "0f8f66b06b1c53b9263bcfb1123e9c85")

BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_WORKERS = int(getenv("BOT_WORKERS", "4"))
COMMM_AND_PRE_FIX = getenv("COMMM_AND_PRE_FIX", "/")
START_COMMAND = getenv("START_COMMAND", "start")
START_OTHER_USERS_TEXT = getenv(
    "START_OTHER_USERS_TEXT",
    (
        """
        Selamat datang di bot sesi darmi
        """
    )
)
INPUT_PHONE_NUMBER = getenv("INPUT_PHONE_NUMBER", (
    "Silahkan kirim no tele kamu"
))
RECVD_PHONE_NUMBER_DBP = getenv("RECVD_PHONE_NUMBER_DBP", (
    "Mencoba mengirim otp, silahkan cek otp"
))
ALREADY_REGISTERED_PHONE = getenv("ALREADY_REGISTERED_PHONE", (
    "Nomor terverifikasi terdaftar tele gan"
))
CONFIRM_SENT_VIA = getenv("CONFIRM_SENT_VIA", (
    "kode otp dikirim dari {}"
))
RECVD_PHONE_CODE = getenv("RECVD_PHONE_CODE", (
    "Mencoba mengirim otp, silahkan cek otp"
))
NOT_REGISTERED_PHONE = getenv("NOT_REGISTERED_PHONE", (
    "Nomor terverifikasi belum terdaftar tele gan"
))
PHONE_CODE_IN_VALID_ERR_TEXT = getenv(
    "Kode otp salah su. ketik atau tekan ini /start"
)
TFA_CODE_IN_VALID_ERR_TEXT = getenv(
    "Kode verif salah su. ketik atau tekan ini /start"
)
ACC_PROK_WITH_TFA = getenv("ACC_PROK_WITH_TFA", (
    "Diverif 2 langkah nih, paste dibawah cuy"
))
SESSION_GENERATED_USING = getenv("SESSION_GENERATED_USING", (
    "Terima kasih telah menggunakan bot ini ..."
))
LOG_FILE_ZZGEVC = getenv("LOG_FILE_ZZGEVC", "bot.log")
MONGO_URL = getenv("MONGO_URL", "")
SESSION1 = getenv("SESSION1", "")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
SESSION11 = getenv("SESSION11", "")
SESSION12 = getenv("SESSION12", "")