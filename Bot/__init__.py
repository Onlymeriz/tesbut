
from pyrogram import Client

api_id = "11432539"

api_hash = "a0dc7b4be20d3cf304345a6aca3d31f8"

string_session = "BQAhIHQASRFm9xQX_UJ2wI5M5aqTeEcr9pXjiHGhxoEYdl7OvJjwHWZJEZDr0E1KID1KRncSwj8en-K5-ebDuM2f1BaFjVZNItQn00PbS3w8MRDfu1-UOGE96Qc9-OafCmP8WDBWNwBHccKMHNkuuox_AqAQlMKtO4w78CDJyii2kyXkaXkK9Jkw5vxl-TOQHl5Etn3m7pMPjUiEsD3Ql3DnLs9-dt12CO4HxSerG5Roqt5brgJ1zBYIPBZTsbRVGCmpM1QrLRf_UlifSZLZ53jizeB-2n9QItOefspkEfVga2mI5r_lFwljM7xeQ3zj4A5GY44YXKDPSJRglqkI-SY_IabgWAAAAAB1M49qAA"

app_password = "6279149779:AAEFnmoUUcxfMeceZQJ4_E3lETYlaqWjciU"

app = Client(
    "my_bot",
    api_id=api_id,
    api_hash=api_hash,
    session_string=string_session,
    bot_token=app_password
)

app.start()
