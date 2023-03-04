import os
from os import getenv
from dotenv import load_dotenv

load_dotenv(".env")

API_ID = int(getenv("API_ID", "22156937"))

API_HASH = getenv("API_HASH", "0f8f66b06b1c53b9263bcfb1123e9c85")

BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_URL = getenv("MONGO_URL", "")