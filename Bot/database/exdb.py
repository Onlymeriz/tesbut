from pyrogram.filters import chat
from . import cli
from typing import Dict, List, Union
import asyncio
from datetime import datetime, timedelta
from pymongo import MongoClient

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

expiration_date = datetime.utcnow() + timedelta(days=30)

# Retrieve expired env files
expired_env_files = collection.find({"created_at": {"$lt": expiration_date}})

# Remove expired env files from load_dotenv
for env_file in expired_env_files:
    os.environ.pop(env_file["filename"])

# Remove expired env files from database
collection.delete_many({"created_at": {"$lt": expiration_date}})


