from pyrogram import Client
from pyrogram_bot.abhi import Bot, abhi, calls
from pytgcalls import PyTgCalls, idle

call_py = PyTgCalls(abhi, overload_quiet_mode=True)

with Client("Pyrogram Bot", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()
with abhi as app:
    me_abhi = app.get_me()
