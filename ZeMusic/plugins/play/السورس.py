import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["السورس","‹ السورس ›"," ","السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/d26a24c11bd88d3bd305a.jpg",
        caption = f"""<b>𝘄𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 . .<b>\n<a href="https://t.me/u_s16"> 𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗔𝗡𝗛𝗔𝗧</a></b>""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 𝗦𝗔𝗡𝗛𝗔𝗧", url=f"https://t.me/iyyx2"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗔𝗡𝗛𝗔𝗧", url=f"https://t.me/u_s16"),         
                ],

            ]

        ),

    )


