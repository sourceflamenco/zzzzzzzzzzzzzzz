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

@app.on_message(filters.regex("^تعطيل ردود البـوت$") & filters.group)
async def descut(client, message):
      a = await app.get_chat_member(message.chat.id, message.from_user.id)
      id = message.from_user.id
      cid = message.chat.id
      if cid in disable_cut:
        return await message.reply_text("")

      if not a.can_manage_chat:
         await message.reply_text("**- هذا الأمر يخص المشرفين بس !**")

          
      if a.can_manage_chat:
        disable_cut.append(cid)
        await message.reply_text(f"- بواسطة {message.from_user.mention}\n- تم تعطيل صراحه")
        
@app.on_message(filters.regex("^تفعيل ردود البـوت$") & filters.group)
async def enacut(client, message):
      a = await app.get_chat_member(message.chat.id, message.from_user.id)
      id = message.from_user.id
      cid = message.chat.id
      if cid not in disable_cut:
        return await message.reply_text("")
        

      if not a.can_manage_chat:
         await message.reply_text("**- هذا الأمر يخص المشرفين بس !**")
      
      if a.can_manage_chat:
        disable_cut.remove(cid)
        await message.reply_text(f"- بواسطة {message.from_user.mention}\n- تم تفعيل صراحه")        
        
        
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
        word = random.choice(txt)
        m.reply_text(f"")
