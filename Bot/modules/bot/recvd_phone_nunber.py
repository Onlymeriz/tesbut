


from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from Bot import AKTIFPERINTAH, User


@Client.on_message(
    filters.text &
    filters.private,
    group=1
)
async def recvd_ph_no_message(_, message: Message):
    w_s_dict = AKTIFPERINTAH.get(message.chat.id)
    if not w_s_dict:
        return
    status_message = w_s_dict.get("START")
    if not status_message:
        return
    del w_s_dict["START"]
    status_message = await message.reply_text(
        "Mencoba mengirim otp, silahkan cek otp",
    )
    loical_ci = User()
    w_s_dict["PHONE_NUMBER"] = message.text
    await loical_ci.connect()
    w_s_dict["SENT_CODE_R"] = await loical_ci.send_code(
        w_s_dict["PHONE_NUMBER"]
    )
    w_s_dict["USER_CLIENT"] = loical_ci

    status_message = await status_message.edit_text(
        "Nomor terverifikasi terdaftar tele gan \n\n Kode otp dikirim dari {SENT_CODE_R}",
    )
    w_s_dict["MESSAGE"] = status_message
    AKTIFPERINTAH[message.chat.id] = w_s_dict
    raise message.stop_propagation()
