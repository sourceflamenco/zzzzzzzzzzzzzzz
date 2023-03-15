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











txt = [


            "**اي يقلبـي**.",


            "**عيـون البـوت**",


            "**انت البـوت **",


            "**صعبـه تقـول لينـدا**",


            "**نادني باسمي**",


            "**شتبـي**",


            "**قلب البـوت**",


            "**اشغلتنا قـول ليندا**",


            "**بـوت في عينك**",


            "**لا تكلمني اذا قالت اسمي برد عليك**",


            "**اسمـي لينـدا**",


            "**فيك شي نادني باسمـي**",


            "**أمـرني وش اشغل لك**",


            "**عنـدي اسم**",




        ]


        


@app.on_message(filters.regex("^بوت$") & filters.group)


async def cutt(client: Client, message: Message):


      a = random.choice(txt)


      await message.reply(


        f"{a}")