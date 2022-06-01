import os
from os import getenv
from pyrogram import Client
from pytgcalls import PyTgCalls, idle
from config import API_ID, API_HASH, SESSION_NAME, BOT_TOKEN

Bot = Client(
    "Bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

sex = Client(
      api_id=API_ID, 
      api_hash=API_HASH, 
      session_name=SESSION_NAME
) 
user = PyTgCalls(sex,
    cache_duration=100,
    overload_quiet_mode=True,)

call_py = PyTgCalls(sex, overload_quiet_mode=True)

with Client("Bot", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()
with sex as app:
    me_sex = app.get_me()
