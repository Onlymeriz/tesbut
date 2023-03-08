

from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)

@Client.on_message(
    filters.command("start") &
    filters.private
)
async def num_start_message(_, message: Message):
    AKTIFPERINTAH[message.chat.id] = {}
    status_message = await message.reply_text(
        "Selamat datang di bot sesi darmi \n Silahkan kirim no tele kamu"
    )
    AKTIFPERINTAH[message.chat.id]["START"] = status_message
    raise message.stop_propagation()
