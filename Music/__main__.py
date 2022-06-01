import asyncio
from pytgcalls import idle
from Music import LOG_CHAT
from Music.Client.tgcalls import call_py, Bot, sex as abhi

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await Bot.start()
    await Bot.send_message(
                           LOG_CHAT,
                           "<b>InnexiaMusic Bot Successfully Started!</b>"
    ), 

    print("[INFO]: STARTING PYTGCALLS CLIENT")

    await call_py.start()
    await idle()
    await abhi.send_message(
                            LOGGER,
                            "<b>Innexia Music Assistant Successfully Started!</b>"
    ), 
    await abhi.join_chat("RexomaSupport"), 
    await abhi.join_chat("RexomaUpdate") 
    print("[INFO]: STOPPING BOT & USERBOT")    
    await Bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
