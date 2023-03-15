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


            "**سـم حبيبي**.",


            "**احلى من يناديني**",


            "**أمـرني **",


            "**بعـد عمر ليندا**",


            "**امسڪوه عنـي**",


            "**نعم ياقلبـي؍.💖**",


            "**أمر وش بغيت**",


            "**هـلا**",


            "**لبيه**",


            "**عيـون ليندا**",


            "**هاه**",


            "**ياخي شتبي/ن**",


            "**لاتحتك فينـي**",


            "**عيـونها**",




        ]


        


@app.on_message(filters.regex("^ليندا$") & filters.group)


async def cutt(client: Client, message: Message):


      a = random.choice(txt)


      await message.reply(


        f"{a}")
