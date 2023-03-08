


from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from pyrogram.errors import (
    PasswordHashInvalid
)
from Bot import AKTIFPERINTAH, app

@app.on_message(
    filters.text &
    filters.private,
    group=3
)
async def recv_tg_tfa_message(_, message: Message):

    w_s_dict = AKTIFPERINTAH.get(message.chat.id)
    if not w_s_dict:
        return
    phone_number = w_s_dict.get("PHONE_NUMBER")
    loical_ci = w_s_dict.get("USER_CLIENT")
    is_tfa_reqd = bool(w_s_dict.get("IS_NEEDED_TFA"))
    if not is_tfa_reqd or not phone_number:
        return
    tfa_code = message.text
    try:
        await loical_ci.check_password(tfa_code)
    except PasswordHashInvalid:
        await message.reply_text(
            "Kode verif salah su. ketik atau tekan ini /start",
        )
        del AKTIFPERINTAH[message.chat.id]
    else:
        saved_message_ = await message.reply_text(
            "<code>" + str(await loical_ci.export_session_string()) + "</code>"
        )
        await saved_message_.reply_text(
            "Terima kasih telah menggunakan bot ini ...",
            quote=True
        )
    raise message.stop_propagation()
