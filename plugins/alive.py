import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("/start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1838d6ee695608a4fff29.jpg",
        caption=f"""**

╭─────────╮

│ᯓ 𝐒𝐎𝐔𝐑𝐂𝐄 ꕸ


│╭────────╯

││╔╦╦╦═╦╗╔═╦═╦══╦═╗ 

││║║║║╩╣╚╣═╣║║║║║╩╣

│╰╚══╩═╩═╩═╩═╩╩╩╩═╝

│╭ᯓтαℓαsнαηεᯓمرحبا انآ بــــوت 

││

│╰ᯓ لتشغيل الاغاني 

│ 

│╭ᯓ ❬اضف البوت الى المجموعة❭ 

││

│╰ᯓ ❬ارفع البوت ادمن في المجموعة❭

│

│╭ᯓ لتحكم ف البوت اتبع زر الاوامر

│╰────────╮

│ᯓ 𝐓𝑳𝐀𝐒𝐇𝐀𝐍𝐘 ꕸ

╰─────────╯

**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 𝗌𝗈!𝗇g .", url=f"https://t.me/vvyvv6")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "aditya"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/6111837a4b2586e21e96c.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "البوت يعمل بنجاح 👍🏻.", url=f"https://t.me/xl444")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["السورس", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/6111837a4b2586e21e96c.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مطۅࢪ اެݪسۅࢪس", url=f"https://t.me/RR8R9")
                ]
            ]
        ),
    )
