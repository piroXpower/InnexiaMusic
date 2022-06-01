import random
from pyrogram.types import InlineKeyboardButton

def play_markup(_, chat_id):
    buttons = [
        [           
            InlineKeyboardButton(
                text="Menu",
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Close",
                callback_data="close"
            )
        ],
    ]
    return buttons

playboard = play_markup
