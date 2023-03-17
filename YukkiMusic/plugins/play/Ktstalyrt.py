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

@app.on_message
filters.command(["المطور","السورس"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/9e11855b92847621a8ecc.jpg",
        caption=f"""𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 & 𝗌𝗈𝗎𝗋𝖼𝖾 moon .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "aBs Ahmed", url=f"https://t.me/r6r8r")
                ],[
                    InlineKeyboardButton(
                       "Source Moon", url=f"https://t.me/sssssso")
              
                 ],

            ]

        ),

    )
