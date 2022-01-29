import os
from pyrogram import Client, idle
from pyrogram import Client, idle
from pytgcalls import idle as pyidle
from Config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME
from pyrogram import Client
from pytgcalls import PyTgCalls

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "RaiChu.Player"},
)

user = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)

ProMusic = PyTgCalls(user, overload_quiet_mode=True)
