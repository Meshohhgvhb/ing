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
│ᯓ 𝐒𝐎𝐔𝐑𝐂𝐄 
│╭────────╯
││╔╦╦╦═╦╗╔═╦═╦══╦═╗ 
││║║║║╩╣╚╣═╣║║║║║╩╣
│╰╚══╩═╩═╩═╩═╩╩╩╩═╝
│╭ᯓтαℓαsнαηεᯓمرحبا انآ بــــوت 
││
│╰ᯓ اقوم بتشغيل الموسيقى 
│ 
│╭ᯓ ❬اضف البوت الى المجموعة❭ 
││
│╰ᯓ ❬ارفع البوت ادمن في المجموعة❭
│
│╭ᯓ اوامري مثل اي اوامر تشغيل 
│╰────────╮
│ᯓ 𝐓𝑳𝐀𝐒𝐇𝐀𝐍𝐘 ꕸ
╰─────────╯

**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𖠹s͠o͠u͠r͠c͠e͠ m͠u͠s͠i͠c͠ t͠l͠a͠s͠h͠a͠n͠y͠𖠹", url=f"https://t.me/tlashany2"),
                    ],
            [
                InlineKeyboardButton("اضفنيـ المجموعة ", url=f'https://t.me/MUSIC_TLASHANYBot?startgroup=true'),
               ],
            [ 
                InlineKeyboardButton(

                        "Group t͠l͠a͠s͠h͠a͠n͠y͠ 𖠹", url=f"https://t.me/blacik0"),
                InlineKeyboardButton(
                        "𖠹s͠o͠u͠r͠c͠e͠ t͠l͠a͠s͠h͠a͠n͠y͠𖠹", url=f"https://t.me/m_o_mol"),
                ],
            [ 
                InlineKeyboardButton(

                        "programmer", url=f"https://t.me/m_e_s_h_o"),
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "aditya"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1838d6ee695608a4fff29.jpg",
        caption=f"""
╭─────────╮
│ᯓ 𝐒𝐎𝐔𝐑𝐂𝐄 ꕸ
│╭────────╯
││╔╦╦╦═╦╗╔═╦═╦══╦═╗ 
││║║║║╩╣╚╣═╣║║║║║╩╣
│╰╚══╩═╩═╩═╩═╩╩╩╩═╝
│╭ᯓ البوت يعمل بنجاح👌🏻
│╰────────╮
│ᯓ 𝐓𝑳𝐀𝐒𝐇𝐀𝐍𝐘 ꕸ
╰─────────╯
        
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𖠹s͠o͠u͠r͠c͠e͠ m͠u͠s͠i͠c͠ t͠l͠a͠s͠h͠a͠n͠y͠𖠹", url=f"https://t.me/tlashany2")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["السورس", "سورس"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1838d6ee695608a4fff29.jpg",
        caption=f"""
        
╭─────────╮
│ᯓ 𝐒𝐎𝐔𝐑𝐂𝐄 ꕸ
│╭────────╯
││╔╦╦╦═╦╗╔═╦═╦══╦═╗ 
││║║║║╩╣╚╣═╣║║║║║╩╣
│╰╚══╩═╩═╩═╩═╩╩╩╩═╝
│╭ᯓ مرحبا عزيزي المستخدم
││
│╰ᯓ لقد قمت ببعض التعديلات
│ 
│╭ᯓ على هذا السورس 
││
│╰ᯓ لاكن هذا ليس السورس 
│╭ᯓ الخاص بي ♥
│╰────────╮
│ᯓ 𝐓𝑳𝐀𝐒𝐇𝐀𝐍𝐘 ꕸ
╰─────────╯

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "صاحب السورسـ", url=f"https://t.me/RR8R9"),
                    ],
            [ 
                InlineKeyboardButton(
                        "programmer", url=f"https://t.me/m_e_s_h_o")
                ]
            ]
        ),
    )
