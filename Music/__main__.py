import asyncio
from pytgcalls import idle
from Music import call_py, bot, LOGGER

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    await bot.send_message(LOGGER, " <b> InnexiaMusic Bot Successfully Started </b> ") 
    print("[INFO]: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    await     .send_message(LOGGER, " <b> Innexia Music Assistant Successfully Started </b> ") 
    await idle()
    print("[INFO]: STOPPING BOT & USERBOT")
    await bot.send_message(LOGGER, "**Error Occurred Bot And Assistant Being Stopped**") 
    await bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
