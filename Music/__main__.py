import asyncio
from pytgcalls import idle
from Music import LOGGER
from pyrogram_bot.abhi import Bot, calls, abhi

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await Bot.start()
    await Bot.send_message(LOGGER, " <b> InnexiaMusic Bot Successfully Started </b> ") 
    print("[INFO]: STARTING PYTGCALLS CLIENT")
    await calls.start()
    await abhi.send_message(LOGGER, " <b> Innexia Music Assistant Successfully Started </b> ") 
    await idle()
    print("[INFO]: STOPPING BOT & USERBOT")
    await Bot.send_message(LOGGER, "**Error Occurred Bot And Assistant Being Stopped**") 
    await Bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
