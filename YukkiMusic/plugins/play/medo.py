import os
import random
import requests
from datetime import datetime
from sys import version_info
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import app
from YukkiMusic.utils.decorators.admins import AdminActual
from strings import get_command



disable_cut = []

@app.on_message(filters.regex("^بوت$") & filters.group)
def searchMusic(c: Client, m: Message):
        ch = m.chat.id
        if ch in disable_cut:
          return
        txt = [
            "**لبيـه**",
"**وش تريد** ",
"**عندي ايم ترا**",
"**خيـر ياطير",
"اسمـي لينـدا**",
"**اي يقلبــي**",
"**عيـوني**",
"**يكفي بوت اسمي لينـدا**",
"**أمـر يالغالي**",
"**وش اشغل لك**",
"**أمـرني وش اشغل لك**",
                       ]