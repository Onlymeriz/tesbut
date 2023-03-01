from pyrogram.filters import chat
from . import cli
import asyncio
from typing import Dict, List, Union
import asyncio
from datetime import datetime, timedelta
import os

collection = cli["Kyran"]["envs"]


def create_env_file(session_string, index):
    filename = f".env{index}"
    with open(filename, "w") as file:
        file.write(session_string)
    collection.insert_one({"filename": filename, "created_at": datetime.utcnow()})
    return filename



async def remove_expired_files():
    expiration_date = datetime.utcnow() + timedelta(days=30)
    expired_env_files = collection.find({"created_at": {"$lt": expiration_date}})
    async for env_file in expired_env_files:
        os.environ.pop(env_file["filename"])
    await collection.delete_many({"created_at": {"$lt": expiration_date}})
