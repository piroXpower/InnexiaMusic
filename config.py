## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", None)
LOG_CHAT = int(getenv("LOG_CHAT")) 
API_ID = int(getenv("API_ID", "12281520"))
API_HASH = getenv("API_HASH", "")
OWNER_NAME = getenv("OWNER_NAME", None)
ALIVE_NAME = getenv("ALIVE_NAME", None)
BOT_USERNAME = getenv("BOT_USERNAME", None)
ASSISTANT_NAME = getenv("ASSISTANT_NAME",None)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", None)
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "160"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TeamRexoma/InnexiaMusic")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
YOUTUBE_URL = getenv("YT_URL", "https://te.legra.ph/file/6cf9d6f9ef58a4886f506.png") 
