from pyrogram.filters import chat
from . import cli
import asyncio
from typing import Dict, List, Union
import asyncio
from datetime import datetime, timedelta
import os

collection = cli["Kyran"]["envs"]

# Fungsi untuk mengecek apakah pengguna sudah terdaftar atau belum
def create_env_file(session_string):
    # Looping untuk membuat file .env1 sampai .env100
    for i in range(1, 201):
        filename = f".env{i}"
        if not os.path.isfile(filename):
            # Jika file belum ada, maka buat file baru dan isi dengan session_string
            with open(filename, "w") as file:
                file.write(session_string)
            # Simpan file ke database
            env_file = {"filename": filename, "created_at": datetime.utcnow()}
            collection.insert_one(env_file)
            # Kirim file .env ke pengguna
            return filename


async def remove_expired_files():
    # Set expiration date for env file
    expiration_date = datetime.utcnow() + timedelta(days=30)

    # Retrieve expired env files
    expired_env_files = collection.find({"created_at": {"$lt": expiration_date}})

    # Remove expired env files from load_dotenv
    async for env_file in expired_env_files:
        os.environ.pop(env_file["filename"])

    # Remove expired env files from database
    await collection.delete_many({"created_at": {"$lt": expiration_date}})

@app.on_startup
async def start_scheduler(client):
    scheduler.add_job(remove_expired_files, "interval", days=1)