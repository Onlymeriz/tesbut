import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from uvloop import install
from pyrogram.types import Message
from Bot import *
from Bot.database.exdb import *
import os
from itertools import count
from pyrogram import Client, filters
from pyrogram.errors import SessionPasswordNeeded
from pyrogram.session import Session


import os
import importlib
from pyrogram import Client, idle

# Menentukan nama modul yang akan dimuat
ALL_MODULES = ["modul1", "modul2"]

# Membuat objek Pyrogram


# Menentukan ID group log
BOTLOG_CHATID = -1001812143750

# Menyimpan daftar ID pengguna yang terdaftar
ids = []

async def main():
    # Memulai bot
    await app.start()
    LOGGER("Ubot").info("Memulai Ubot Pyro..")
    LOGGER("Ubot").info("Loading Everything.")
    
    # Memuat semua modul yang didefinisikan dalam daftar ALL_MODULES
    for all_module in ALL_MODULES:
        importlib.import_module("Ubot.modules" + all_module)
    
    # Menjalankan setiap bot dan menambahkannya ke daftar ID pengguna
    for bot in bots:
        try:
            # Memulai bot
            await bot.start()
            
            # Mendapatkan informasi profil bot
            ex = await bot.get_me()
            
            # Bergabung dengan grup
            await join(bot)
            
            LOGGER("Ubot").info("Startup Completed")
            LOGGER("√").info(f"Started as {ex.first_name} | {ex.id} ")
            
            # Menambahkan pengguna ke daftar terdaftar
            await add_user(ex.id)
            
            # Mendapatkan waktu aktif pengguna
            user_active_time = await get_active_time(ex.id)
            active_time_str = str(user_active_time.days) + " Hari " + str(user_active_time.seconds // 3600) + " Jam"
            
            # Mendapatkan tanggal kadaluarsa pengguna
            expired_date = await get_expired_date(ex.id)
            
            # Menghitung sisa hari aktif pengguna
            remaining_days = (expired_date - datetime.now()).days
            
            # Mengirim pesan ke log group
            msg = f"{ex.first_name} ({ex.id}) - Masa Aktif: {active_time_str}"
            ids.append(ex.id)
            await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, pyro, py(), active_time_str, remaining_days, CMD_HNDLR))
            
            # Mendapatkan pengguna aktif saat ini
            await get_active_users()
            
        except Exception as e:
            LOGGER("X").info(f"{e}")
            # Jika terdapat duplikat string session atau string session eror, maka hapus string session tersebut dan kirimkan pesan ke log group
            if "Session is already running" in str(e) or "API_ID is invalid" in str(e):
                session_file = os.path.join(".", ex.id + ".session")
                if os.path.exists(session_file):
                    os.remove(session_file)
                    LOGGER("Ubot").info(f"Session file for {ex.first_name} has been removed due to error: {e}")
                    await bot.send_message(BOTLOG_CHATID, f"Session file for {ex.first_name} has been removed due to error: {e}")
    await idle()
    for ex_id in ids:
      await remove_user(ex_id)
      
      
if __name__ == "__main__":
   install()
   LOOP.run_until_complete(main())
   LOGGER("Info").info("Starting Ubot Pyro Userbot")

    
    # Menjaga bot tetap hid

