from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, SUPPORT_GROUP
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import sudo_users_only


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


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""
**<b>𝐇𝐞𝐲 👋 {message.from_user.first_name}**
𝐈 𝐚𝐦 [{BOT_NAME}](https://t.me/{BOT_USERNAME}), 𝐔𝐬𝐞 𝐦𝐞 𝐭𝐨 𝐩𝐥𝐚𝐲 𝐦𝐮𝐬𝐢𝐜 𝐢𝐧 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩𝐬 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭.
𝐇𝐨𝐬𝐭𝐞𝐝 𝐎𝐧 𝐕𝐏𝐒, 𝐒𝐨 𝐧𝐨 𝐥𝐚𝐠

🎵 𝗔𝗱𝗱𝘆 𝗢𝗩𝗘𝗥 𝗣𝗢𝗪𝗘𝗥𝗘𝗗💜

🥴𝐍𝐞𝐞𝐝 𝐇𝐞𝐥𝐩!
𝐔𝐬𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐁𝐞𝐥𝐨𝐰 𝐓𝐨 𝐊𝐧𝐨𝐰 𝐌𝐨𝐫𝐞 𝐀𝐛𝐨𝐮𝐭 𝐌𝐞 𝐚𝐧𝐝 𝐌𝐲 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬😁
:-) **𝗙𝗼𝗿 𝗠𝗼𝗿𝗲 𝗜𝗻𝗳𝗼, 𝗦𝗲𝗻𝗱 /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ 𝐀𝐝𝐝 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "𝐇𝐨𝐰 𝐓𝐨 𝐔𝐬𝐞?💎", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "🤔𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", callback_data="cbcmds"
                    )
                ],[
                    InlineKeyboardButton(
                        "💬 𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url=f"https://t.me/AddySupport"
                    ),
                    InlineKeyboardButton(
                        "🔊 𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url=f"https://t.me/AddyUpdates")
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞💞", url="https://t.me/AddyxD"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""𝐎𝐧𝐞 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 𝐎𝐧𝐥𝐢𝐧𝐞 ✅\n<b>😇𝐔𝐩𝐭𝐢𝐦𝐞✌:</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url=f"https://t.me/AddySupport"
                    ),
                    InlineKeyboardButton(
                        "🔊 𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url=f"https://t.me/AddyUpdates"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 **𝐇𝐞𝐲𝐚** {message.from_user.mention()}</b>

𝐍𝐞𝐞𝐝 𝐇𝐞𝐥𝐩? 
𝐔𝐬𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐁𝐞𝐥𝐨𝐰 𝐓𝐨 𝐊𝐧𝐨𝐰 𝐌𝐨𝐫𝐞 𝐀𝐛𝐨𝐮𝐭 𝐌𝐞
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="𝐇𝐨𝐰 𝐓𝐨 𝐔𝐬𝐞?💎", callback_data=f"cbguide"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>𝐇𝐞𝐲𝐚👋🏻 {message.from_user.mention} 𝐖𝐥𝐜𝐦 𝐓𝐨 𝐇𝐞𝐥𝐩 𝐌𝐞𝐧𝐮!</b>

𝐇𝐞𝐫𝐞 𝐢𝐧 𝐓𝐡𝐢𝐬 𝐌𝐞𝐧𝐮 𝐘𝐨𝐮 𝐖𝐢𝐥𝐥 𝐆𝐞𝐭 𝐒𝐨𝐦𝐞 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐌𝐞𝐧𝐮
𝐀𝐧𝐝 𝐢𝐧 𝐞𝐚𝐜𝐡 𝐌𝐞𝐧𝐮 𝐓𝐡𝐞𝐫𝐞 𝐢𝐬 𝐁𝐫𝐢𝐞𝐟 𝐄𝐱𝐩𝐥𝐚𝐧𝐚𝐭𝐢𝐨𝐧 𝐎𝐟 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎀 𝗕𝗮𝘀𝗶𝗰 𝗖𝗠𝗗𝘀", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "😮 𝗔𝗱𝘃𝗮𝗻𝗰𝗲𝗱 𝗖𝗠𝗗𝘀", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "😎 𝗔𝗱𝗺𝗶𝗻 𝗖𝗠𝗗𝘀", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "🤩 𝗦𝘂𝗱𝗼 𝗖𝗠𝗗𝘀", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "😆 𝗢𝘄𝗻𝗲𝗿 𝗖𝗠𝗗𝘀", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "😝 𝗙𝘂𝗻 𝗖𝗠𝗗𝘀", callback_data="cbfun"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᑭIᑎGIᑎG....")
    delta_ping = time() - start
    await m_reply.edit_text(
        " `𝐏𝐨𝐧𝐠!!`\n"
        f" `{delta_ping * 1000:.3f} ᴹˢ`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐮𝐬💚:\n"
        f"• **𝚄𝚙𝚝𝚒𝚖𝚎:** `{uptime}`\n"
        f"• **𝚂𝚝𝚊𝚛𝚝 𝚃𝚒𝚖𝚎:** `{START_TIME_ISO}`"
    )
