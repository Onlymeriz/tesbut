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


def create_session(phone_number):
    # Membuat session menggunakan nomor telepon pengguna
    with app:
        try:
            app.send_code(phone_number)
            # Meminta kode verifikasi
            code = input("Masukkan kode verifikasi yang Anda terima: ")
            session = app.sign_in(phone_number, code)

        # Jika dibutuhkan password tambahan
        except SessionPasswordNeeded:
            password = input("Akun Anda dilindungi oleh kata sandi. Silakan masukkan kata sandi: ")
            session = app.sign_in(phone_number, password)

    # Mengembalikan session
    return session

# Fungsi untuk mengirimkan pesan dengan menunggu balasan dari pengguna
async def send_message_and_get_reply(chat_id, text):
    message = await app.send_message(chat_id, text)
    reply = await app.listen(filters.reply & filters.text)
    return reply.text

# Handler untuk menerima pesan dari pengguna
@app.on_message(filters.private)
async def handle_message(client, message):
    # Jika pengguna mengirimkan nomor telepon
    if message.contact is not None:
        # Mengambil nomor telepon dari pesan
        phone_number = message.contact.phone_number

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

    # Jika pengguna mengirimkan pesan lain
    else:
        # Mengirimkan pesan meminta nomor telepon
        await app.send_message(message.chat.id, "Silakan kirimkan nomor telepon Anda menggunakan tombol 'Kirim Kontak' di bawah ini.", reply_markup={"keyboard": [[{"text": "Kirim Kontak", "request_contact": True}]], "resize_keyboard": True})
    
# Jalankan bot
app.run()
