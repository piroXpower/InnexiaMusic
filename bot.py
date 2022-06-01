import asyncio
from pytgcalls import idle
from Music import LOG_CHAT
from Music.Client.tgcalls import Mikki, sex, Bot

loop = asyncio.get_event_loop()

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await Bot.start()
    await Bot.send_message(
                           LOG_CHAT,
                           "<b>InnexiaMusic Bot Successfully Started!</b>"
    ), 

    print("[INFO]: STARTING PYTGCALLS CLIENT")
    await sex.start()
    await sex.send_message(LOG_CHAT, "<b> Assistant Successfully Started </b>") 
    await Mikki.start()
    try:
        await Mikki.stream_call(
            LOG_CHAT, 
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        print("Please Turn On Voice Chat In LOG_CHAT") 
        sys.exit()
    await idle() 
    await sex.join_chat("RexomaSupport"), 
    await sex.join_chat("RexomaUpdate") 
    print("[INFO]: STOPPING BOT & USERBOT")    
    await Bot.stop()

loop.run_until_complete(start_bot())
