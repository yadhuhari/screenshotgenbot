from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from ..screenshotbot import ScreenShotBot

PICS = [
 "https://telegra.ph/file/9ba2b9a7785b2345b4c30.jpg",
 "https://telegra.ph/file/313f5cdc9caae2b1a6fb3.jpg",
 "https://telegra.ph/file/b90945a0324165879af0b.jpg"
]

@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m):

    await m.reply_photo(
        photo=random.choice(PICS),
        caption=f"""Hᴇʟʟᴏ {m.from_user.mention} ✨,
        
I Aᴍ A Pᴏᴡᴇʀғᴜʟ Sᴄʀᴇᴇɴsʜᴏᴛ Gᴇɴᴇʀᴀᴛᴏʀ Bᴏᴛ. I Cᴀɴ Gᴇɴᴇʀᴀᴛᴇ Sᴄʀᴇᴇɴsʜᴏᴛs, Sᴀᴍᴘʟᴇs, Tʀɪᴍ Vɪᴅᴇᴏ, Aɴᴅ Sʜᴀʀᴇ Mᴇᴅɪᴀ Iɴғᴏʀᴍᴀᴛɪᴏɴ.

Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : @mrprincebotx""",       
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sᴏᴜʀᴄᴇ 😉", url="https://github.com/odysseusmax/animated-lamp"
                    ),
                    InlineKeyboardButton("Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ ✨", url="https://t.me/mrprincebotx"),
                ],
                [InlineKeyboardButton("Dᴇᴠᴇʟᴏᴘᴇʀ 👨‍💻", url="https://t.me/YourPrince_X")],
            ]
        ),
    )
