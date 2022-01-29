import os
from pyrogram import Client, idle
import asyncio
from pytgcalls import idle as pyidle
from Config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME
from pyrogram import Client
from pytgcalls import PyTgCalls

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "HellMusic"},
)

user = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)

ProMusic = PyTgCalls(user, overload_quiet_mode=True)

bot.start()
print("HELL MUSIC STARTED")
ProMusic.start()
print("HELL MUSIC CLIENT STARTED")
pyidle()
idle()
