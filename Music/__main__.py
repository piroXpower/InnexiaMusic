import asyncio
from pytgcalls import idle
from Music import LOGGER
from Client.tgcalls import call_py
from pyrogram_bot.abhi import Bot, abhi

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await Bot.start()
    await Bot.send_message(
                           LOG_CHAT,
                           "<b>InnexiaMusic Bot Successfully Started!</b>"
    ), 

    print("[INFO]: STARTING PYTGCALLS CLIENT")

    await calls_py.start()
    await abhi.send_message(
                            LOGGER,
                            "<b>Innexia Music Assistant Successfully Started!</b>"
    ), 
    await abhi.join_chat("RexomaSupport"), 
    await abhi.join_chat("RexomaUpdate") 
    await idle()

    print("[INFO]: STOPPING BOT & USERBOT")

    await Bot.send_message(
                           LOGGER,
                           "<b>Error Occurred Bot And Assistant Being Stopped</b>"
    ), 

    await Bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
