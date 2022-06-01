from pyrogram import Client
from Music import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME
from pytgcalls import PyTgCalls, idle

Bot = Client(
    "Music",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Script.Plugin"),
    )

sex = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=SESSION_NAME,
    
    )

call_py = PyTgCalls(sex,
    cache_duration=100,
    overload_quiet_mode=True,)


with Client("Music", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    Music = app.get_me()
with sex as app:
    me_sex = app.get_me()
