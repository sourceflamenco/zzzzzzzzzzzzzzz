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

@app.on_message(filters.regex("^السورس$") & filters.group)
async def sourc(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a0c0d07c7ffbe086f9176.mp4",
        caption=f"""𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑻𝒐 𝑺𝒐𝒖𝒓𝒄𝒆 𝒍𝒊𝒏𝒅𝒂 🎶\n\n• ᴅᴇᴠᴇʟᴏᴘᴇʀ » [𝑎𝑙_𝑐𝑎𝑒𝑠𝑎𝑟](t.me/FH_KX)\n• ᴄʜᴀɴɴᴇʟ » [𝒄𝒉𝒂𝒏𝒏𝒆𝒍](t.me/FH_KN)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙴𝚅", user_id=5820455440)
                ],[
                    InlineKeyboardButton(
                       "تحديثات لينـدا", url=f"https://t.me/FH_KP")
              
                 ],

            ]

        ),

    )
