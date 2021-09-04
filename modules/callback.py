from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import authorized_users_only
from config import BOT_NAME, BOT_USERNAME, OWNER_NAME, UPDATES_CHANNEL, SUPPORT_GROUP, ASSISTANT_NAME
from modules.play import cb_admin_check


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>𝐇𝐞𝐲 👋 {message.from_user.first_name}**
𝐈 𝐚𝐦 [{BOT_NAME}](https://t.me/{BOT_USERNAME}), 𝐔𝐬𝐞 𝐦𝐞 𝐭𝐨 𝐩𝐥𝐚𝐲 𝐦𝐮𝐬𝐢𝐜 𝐢𝐧 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩𝐬 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭.
𝐇𝐨𝐬𝐭𝐞𝐝 𝐎𝐧 𝐕𝐏𝐒, 𝐒𝐨 𝐧𝐨 𝐥𝐚𝐠

🎵 𝗔𝗱𝗱𝘆 𝗢𝗩𝗘𝗥 𝗣𝗢𝗪𝗘𝗥𝗘𝗗💜

🥴𝐍𝐞𝐞𝐝 𝐇𝐞𝐥𝐩!
𝐔𝐬𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐁𝐞𝐥𝐨𝐰 𝐓𝐨 𝐊𝐧𝐨𝐰 𝐌𝐨𝐫𝐞 𝐀𝐛𝐨𝐮𝐭 𝐌𝐞 𝐚𝐧𝐝 𝐌𝐲 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬😁
:-) **𝗙𝗼𝗿 𝗠𝗼𝗿𝗲 𝗜𝗻𝗳𝗼, 𝗦𝗲𝗻𝗱 /help**
</b>**""",
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


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
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
                ],
                [
                    InlineKeyboardButton(
                        "🏡𝐁𝐚𝐜𝐤", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>𝗛𝗲𝗿𝗲 𝗔𝗿𝗲 𝗕𝗮𝘀𝗶𝗰 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀😋</b>

🎧 [ 𝐆𝐫𝐨𝐮𝐩 𝐂𝐌𝐃𝐬 ]

/play (song name) - play song from youtube
/fplay (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/video (video name) - download video from youtube detailed
/lyrics - (song name) lyrics scrapper
/userbotjoin - invite the assistant for join to your group

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 𝐁𝐚𝐜𝐤", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>𝗛𝗲𝗿𝗲 𝗔𝗿𝗲 𝗔𝗱𝘃𝗮𝗻𝗰𝗲𝗱 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀</b>

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/admincache - refresh the admin cache
/ping - check the bot ping status
/uptime - check the bot uptime status
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 𝐁𝐚𝐜𝐤", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>𝗛𝗲𝗿𝗲 𝗔𝗿𝗲 𝗔𝗱𝗺𝗶𝗻 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀</b>

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/userbotjoin - invite assistant join to your group
/auth - authorized user for using music bot
/deauth - unauthorized for using music bot
/player - open the player settings panel
/musicplayer (on / off) - disable / enable music player in your group
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 𝐁𝐚𝐜𝐤", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>𝗛𝗲𝗿𝗲 𝗔𝗿𝗲 𝗦𝘂𝗱𝗼 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀</b>

/userbotleaveall - order the assistant to leave from all group
/gcast - send a broadcast message trought the assistant
/stats - show the bot statistic
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 𝐁𝐚𝐜𝐤", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>𝗛𝗲𝗿𝗲 𝗔𝗿𝗲 𝗢𝘄𝗻𝗲𝗿 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀</b>

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

📝 𝐍𝐨𝐭𝐞: 𝘼𝙡𝙡 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙤𝙬𝙣𝙚𝙙 𝙗𝙮 𝙩𝙝𝙞𝙨 𝙗𝙤𝙩 𝙘𝙖𝙣 𝙗𝙚 𝙚𝙭𝙚𝙘𝙪𝙩𝙚𝙙 𝙗𝙮 𝙩𝙝𝙚 𝙤𝙬𝙣𝙚𝙧 𝙤𝙛 𝙩𝙝𝙚 𝙗𝙤𝙩 𝙬𝙞𝙩𝙝𝙤𝙪𝙩 𝙖𝙣𝙮 𝙚𝙭𝙘𝙚𝙥𝙩𝙞𝙤𝙣𝙨.
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 𝐁𝐚𝐜𝐤", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>𝗛𝗲𝗿𝗲 𝗔𝗿𝗲 𝗙𝘂𝗻 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀</b>

/chika - check it by yourself
/wibu - check it by yourself
/asupan - check it by yourself
/truth - check it by yourself
/dare - check it by yourself
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 𝐁𝐚𝐜𝐤", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""𝐇𝐨𝐰 𝐓𝐨 𝐔𝐬𝐞 𝐌𝐞❓:

1.) ꜰɪʀꜱᴛ, ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
2.) ᴛʜᴇɴ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀꜱ ᴀᴅᴍɪɴ ᴀɴᴅ ɢɪᴠᴇ ᴀʟʟ ᴘᴇʀᴍɪꜱꜱɪᴏɴꜱ ᴇxᴄᴇᴘᴛ ᴀɴᴏɴʏᴍᴏᴜꜱ ᴀᴅᴍɪɴ.
3.) ᴀᴅᴅ @{ASSISTANT_NAME} ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴏʀ ᴛʏᴘᴇ /userbotjoin ᴛᴏ ɪɴᴠɪᴛᴇ ʜɪᴍ.
4.) ᴛᴜʀɴ ᴏɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ꜰɪʀꜱᴛ ʙᴇꜰᴏʀᴇ ꜱᴛᴀʀᴛ ᴛᴏ ᴘʟᴀʏ ᴍᴜꜱɪᴄ.

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤔𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 𝗖𝗹𝗼𝘀𝗲", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
@cb_admin_check
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**𝗛𝗲𝗿𝗲 𝗶𝘀 𝘁𝗵𝗲 𝗖𝗼𝗻𝘁𝗿𝗼𝗹 𝗠𝗲𝗻𝘂 𝗢𝗳 𝗕𝗼𝘁:**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏸ 𝐏𝐚𝐮𝐬𝐞𝐝!", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "▶️ 𝐑𝐞𝐬𝐮𝐦𝐞𝐝!", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⏩ 𝐒𝐤𝐢𝐩!", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "⏹ 𝐄𝐧𝐝!", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 𝗖𝗹𝗼𝘀𝗲", callback_data="close"
                    )
                ]
            ]
        )
    )



@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
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
                ],
                [
                    InlineKeyboardButton(
                        "🏡𝐁𝐚𝐜𝐤", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""𝐇𝐨𝐰 𝐓𝐨 𝐔𝐬𝐞 𝐌𝐞❓:

1.) ꜰɪʀꜱᴛ, ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
2.) ᴛʜᴇɴ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀꜱ ᴀᴅᴍɪɴ ᴀɴᴅ ɢɪᴠᴇ ᴀʟʟ ᴘᴇʀᴍɪꜱꜱɪᴏɴꜱ ᴇxᴄᴇᴘᴛ ᴀɴᴏɴʏᴍᴏᴜꜱ ᴀᴅᴍɪɴ.
3.) ᴀᴅᴅ @{ASSISTANT_NAME} ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴏʀ ᴛʏᴘᴇ /userbotjoin ᴛᴏ ɪɴᴠɪᴛᴇ ʜɪᴍ.
4.) ᴛᴜʀɴ ᴏɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ꜰɪʀꜱᴛ ʙᴇꜰᴏʀᴇ ꜱᴛᴀʀᴛ ᴛᴏ ᴘʟᴀʏ ᴍᴜꜱɪᴄ.

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 𝐁𝐚𝐜𝐤", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
