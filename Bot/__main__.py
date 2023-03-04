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

async def main():
    await app.start()
    LOGGER("Ubot").info("Memulai Ubot Pyro..")
    LOGGER("Ubot").info("Loading Everything.")
    for all_module in ALL_MODULES:
        importlib.import_module("Ubot.modules" + all_module)
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            LOGGER("Ubot").info("Startup Completed")
            LOGGER("√").info(f"Started as {ex.first_name} | {ex.id} ")
            await add_user(ex.id)
            user_active_time = await get_active_time(ex.id)
            active_time_str = str(user_active_time.days) + " Hari " + str(user_active_time.seconds // 3600) + " Jam"
            expired_date = await get_expired_date(ex.id)
            remaining_days = (expired_date - datetime.now()).days
            msg = f"{ex.first_name} ({ex.id}) - Masa Aktif: {active_time_str}"
            ids.append(ex.id)
            await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, pyro, py(), active_time_str, remaining_days, CMD_HNDLR))
            await get_active_users()
        except Exception as e:
            LOGGER("X").info(f"{e}")
            if "string session is invalid" in str(e):
                with open(".env", "r") as file:
                    lines = file.readlines()
                    for i, line in enumerate(lines):
                        if "SESSION" in line and str(session_index) in line:
                            LOGGER("X").info(f"String session eror pada SESSION{session_index}.")
                            del lines[i]
                            with open(".env", "w") as file:
                                file.writelines(lines)
                            await bot.send_message(BOTLOG_CHATID, f"String session pada SESSION{session_index} telah dihapus karena eror.")
                            break
                        elif i == 199:
                            LOGGER("X").info(f"Semua SESSION digunakan.")
                            await bot.send_message(BOTLOG_CHATID, "Semua SESSION telah digunakan.")
            else:
                LOGGER("X").info(f"Gagal memulai bot: {e}")
    await idle()
    for ex_id in ids:
        await remove_user(ex_id)




    
# Jalankan bot
app.run()
