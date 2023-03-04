import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message
from Bot import *
from Bot.database.exdb import *
import os
from pyrogram import Client, filters
from pyrogram.errors import SessionPasswordNeeded
from pyrogram.session import Session


def fix_phone_number(phone_number):
    # Menghilangkan karakter selain digit
    phone_number = "".join(filter(str.isdigit, phone_number))

    # Menghilangkan angka 0 pada awal nomor telepon
    if phone_number.startswith("0"):
        phone_number = phone_number[1:]

    # Menambahkan awalan internasional jika tidak ada
    if not phone_number.startswith("+"):
        phone_number = "+62" + phone_number

    return phone_number

# Fungsi untuk membuat session
def create_session(phone_number):
    # Membuat session menggunakan nomor telepon pengguna
    with app:
        try:
            app.send_code(phone_number)
            # Meminta kode verifikasi
            code = None
            while code is None:
                message = app.listen(filters.private & filters.regex(r"^\d{4,6}$"))
                code = message.text

            session = app.sign_in(phone_number, code)

        # Jika dibutuhkan password tambahan
        except SessionPasswordNeeded:
            password = input("Akun Anda dilindungi oleh kata sandi. Silakan masukkan kata sandi: ")
            session = app.sign_in(phone_number, password)

    # Mengembalikan session
    return session

# Handler untuk menerima pesan dari pengguna
@app.on_message(filters.private)
async def handle_message(client, message):
    # Jika pengguna mengirimkan nomor telepon
    if message.contact is not None:
        # Mengambil nomor telepon dari pesan
        phone_number = message.contact.phone_number

        # Memperbaiki nomor telepon
        phone_number = fix_phone_number(phone_number)

        # Membuat session menggunakan nomor telepon
        session = await create_session(phone_number)

        # Mengirimkan string session ke pengguna
        await app.send_message(message.chat.id, f"String session Anda adalah: {session.stringify()}")

    # Jika pengguna membalas pesan yang dikirimkan oleh bot
    elif message.reply_to_message is not None:
        # Mengambil kode verifikasi dari pesan
        code = message.text.strip()

        # Memperbarui kode verifikasi pada session
        session = Session.try_load_or_create_new("session_file_name_here", lambda: None)
        session = session.update(code)

        # Menyimpan session ke file
        session.save()

        # Mengirimkan pesan berhasil memperbarui session
        await app.send_message(message.chat.id, "Session berhasil diperbarui!")
    
# Jalankan bot
app.run()
