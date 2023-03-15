import sys
import asyncio
import requests
import re
import string
from pyrogram.types import Message
from aiohttp import ClientSession
from pyrogram import filters, Client
from strings import get_command
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

#########
#الاوامر        
@app.on_message(
    filters.command(["اوامرليندا","الاوامر"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bab3ef34f85794b507843.jpg",
        caption=f"""**اهلـين حبـي أليـك قائمة اوامـر التشغيل في في المجموعه** {message.from_user.mention}
        
**اليك قائـمة الاوامــر**
          

»**لتشغيل اغنيه اكتب : تشغيل او شغل**
»**لأنهاء الاغنيه اكتب : ايقاف او انهاء**
»**لايقاف الاغنيه مؤقت اكتب : قفي**
»**لتكملة الاغنيه من الايقاف المؤقت اكتب : كمل او استمر**
»**لتخطي الاغنيه اكتب : تخطي او التالي**
»**لكتم البوت في المحادثه اكتب : اسڪتي**
»**لألغاء كتم البوت في المحادثه اكتب : اتكلم او تكلمي**
»**لتحميـل الاغانـي اڪتب : بحث او تحميل**
»**لتشغيـل في القناه : اڪتب القناه او** : /channel.""",
      reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("تحديثات ليندا ♪", url=f"https://t.me/FH_KP")
                ]
            ]
        ),
    )  
@app.on_message(
    filters.command(["بوت الحذف"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7bc5810a111c94694e66a.jpg",
        caption=f"""فڪـر قبـل لا تحذف 🥺..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("بـوت الحـذف", url=f"https://t.me/DTeLebot"),
                ],[
                InlineKeyboardButton(
                        "تحديثات لنـدا", url=f"https://t.me/FH_KP"),
                ]
            ]
        ),
    )
@app.on_message(
    filters.command(["/channel","القناه"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bab3ef34f85794b507843.jpg",
        caption=f"""**اهلـين حبـي أليـك قائمة اوامـر التشغيل في القناه** {message.from_user.mention}
        
**اليك قائـمة الاوامــر**
          

» **خطوات تشغيل في القناه**

» **لتشغيل في قناتك**

‌‏« **قم بانشاء جروب مربوط بقناتك**

» **تقوم باضافة البوت @LANDHLBOT في القناه والجروب ادمن**

» **لربط القناتك بالمجموعه ارسل  الامر التالي في المجموعة**
            
 /channelplay + معرف قناتك

/ channelplay @FH_KP مثـل

» **أوامـر التشغـل في القنـوات**
/cplay ـ **لتشغيـل اڪتب** 
/cskip ـ **لتخطـي التشغيـل اڪتب** 
/cstop ـ **لايقاف التشغيـل اڪتب**.""",
      reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("تحديثات ليندا ♪", url=f"https://t.me/FH_KP")
                ]
            ]
        ),
    )
@app.on_message(
    filters.command(["احبك"],""))
def reply_to_timo(Client, message):
    message.reply_text(
        f"""ياقلبي​​​​​​​​​​​​​​​​​​​​​  ‹⇡ٴ⁽😍❤₎⇣›""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("تحديثات ليندا ♪", url=f"https://t.me/FH_KP")
                ]
            ]
        ),
    ) 
@app.on_message(
    filters.command(["مين انا"],""))
def reply_to_timo(Client, message):
    message.reply_text(
        f"""انت قلبي ❤😻""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("تحديثات ليندا ♪", url=f"https://t.me/FH_KP")
                ]
            ]
        ),
    )       
@app.on_message(
    filters.command(["انا مين"],""))
def reply_to_timo(Client, message):
    message.reply_text(
        f"""ـ• ﺂٰنـُـٰٰت ﺂٰلـُُـٰ؏ـٖمـࢪَٰٰي َ،🤭♥️ ֆ ۦٰ،""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("تحديثات ليندا ♪", url=f"https://t.me/FH_KP")
                ]
            ]
        ),
    )           
@app.on_message(
    filters.command(["الرابط"],""))
async def invitelink(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        return await message.reply_text("قم برفعي مسؤول في المجموعة أولا ؟")
    await message.reply_text(f"**تم إنشاء رابط الدعوة بنجاح :**\n {invitelink}")
    
