from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VIPMUSIC import app
from config import BOT_USERNAME
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ˹ ᴍᴜsɪᴄ™ ˼ ʙᴏᴛ ✪
 
 ❍ • ʙsᴅᴋ ʀᴇᴘᴏ ʟᴇɢᴀ ◉‿◉ •
 
 ❍ • ᴘᴇʜʟᴇ ᴀɴᴊᴀʟɪ ᴋᴏ ᴅɪᴅɪ ʙᴏʟ •
 
 ❍ • ᴄʜᴜᴘ ᴄʜᴜᴘ ʙᴏᴛ ʟᴇᴋᴇ ɴɪᴋᴀʟ •
 
 ❍ • ʀᴇᴘᴏs ᴛᴏ ɴᴀʜɪ ᴍɪʟᴇɢᴀ ʙᴇᴛᴀ ⊂◉‿◉ •
 
 ❍ • ᴀɢʀ ᴄʜᴀʜɪʏᴇ ᴛᴏ ᴀɴᴊᴀʟɪ ᴋᴏ ᴅɪᴅɪ ʙᴏʟɴᴀ ᴘᴀᴅᴇɢᴀ •
 
 ❍ • ʀᴀᴅʜᴇ ʀᴀᴅʜᴇ •
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url="https://t.me/+b1gc4qrvfLZlNGI1"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/AnjaliOwnerBot"),
          ],
               [
                InlineKeyboardButton("𝗨𝗣𝗗𝗔𝗧𝗘𝗦", url="https://t.me/ANJALINETWORK"),

],
[
              InlineKeyboardButton("𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/TheAnjaliRobot"),
              InlineKeyboardButton("︎𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/TheAnjaliMusicBot"),

        ]]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_photo(
        photo="https://envs.sh/bJh.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
