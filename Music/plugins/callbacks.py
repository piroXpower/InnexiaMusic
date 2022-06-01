import yt_dlp
from Music.Client.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup)
from Music.plugins.keyboard import play_markup

