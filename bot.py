# (c) @AbirHasan2005

import os
import asyncio
import traceback
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from configs import Config
from handlers.check_user_status import handle_user_status
from handlers.force_sub_handler import handle_force_sub
from handlers.broadcast_handlers import main_broadcast_handler
from handlers.database import Database

db = Database(Config.DATABASE_URL, Config.BOT_USERNAME)
Bot = Client(Config.BOT_USERNAME, bot_token=Config.BOT_TOKEN, api_id=Config.API_ID, api_hash=Config.API_HASH)


@Bot.on_message(filters.private)
async def _(bot: Client, cmd: Message):
    await handle_user_status(bot, cmd)


@Bot.on_message(filters.command("start") & filters.private)
async def start(bot: Client, cmd: Message):
    if cmd.from_user.id in Config.BANNED_USERS:
        await cmd.reply_text("Sorry, You are banned.")
        return
    usr_cmd = cmd.text.split("_")[-1]
    if usr_cmd == "/start":
        chat_id = cmd.from_user.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await bot.send_message(
                Config.LOG_CHANNEL,
                f"#NEW_USER: \n\nNew User [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id}) started @{Config.BOT_USERNAME} !!"
            )
        if Config.UPDATES_CHANNEL is not None:
            back = await handle_force_sub(bot, cmd)
            if back == 400:
                return
            else:
                pass
        await cmd.reply_text(
            Config.HOME_TEXT.format(cmd.from_user.first_name, cmd.from_user.id),
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("👨‍🔧updates channel👨‍🔧", url="https://t.me/disneygrou"),
                        InlineKeyboardButton("🤖support group🤖", url="https://t.me/disneyteamchat")
                    ],
                    [
                        InlineKeyboardButton("About Bot", callback_data="aboutbot"),
                        InlineKeyboardButton("About Dev", callback_data="aboutdevs")
                    ]
                ]
            )
        )
    else:
        if Config.UPDATES_CHANNEL is not None:
            back = await handle_force_sub(bot, cmd)
            if back == 400:
                return
            else:
                pass
        try:
            file_id = int(usr_cmd)
            send_stored_file = None
            if Config.FORWARD_AS_COPY is True:
                send_stored_file = await bot.copy_message(chat_id=cmd.from_user.id, from_chat_id=Config.DB_CHANNEL,
                                                          message_id=file_id)
            elif Config.FORWARD_AS_COPY is False:
                send_stored_file = await bot.forward_messages(chat_id=cmd.from_user.id, from_chat_id=Config.DB_CHANNEL,
                                                              message_ids=file_id)
            await send_stored_file.reply_text(
                f"**Here is Sharable Link of this file:** https://t.me/{Config.BOT_USERNAME}?start=AbirHasan2005_{file_id}\n\n__To Retrive the Stored File, just open the link!__",
                disable_web_page_preview=True, quote=True)
        except Exception as err:
            await cmd.reply_text(f"Something went wrong!\n\n**Error:** `{err}`")


@Bot.on_message((filters.document | filters.video | filters.audio) & ~filters.edited)
async def main(bot: Client, message: Message):
    if message.chat.type == "private":
        chat_id = message.from_user.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await bot.send_message(
                Config.LOG_CHANNEL,
                f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) started @{Config.BOT_USERNAME} !!"
            )
        if Config.UPDATES_CHANNEL is not None:
            back = await handle_force_sub(bot, message)
            if back == 400:
                return
            else:
                pass
        if message.from_user.id in Config.BANNED_USERS:
            await message.reply_text("Sorry, You are banned!\n\nContact [Support Group](https://t.me/disneyteamchat)",
                                     disable_web_page_preview=True)
            return
        if Config.OTHER_USERS_CAN_SAVE_FILE is False:
            return
        editable = await message.reply_text("Please wait ...")
        try:
            forwarded_msg = await message.forward(Config.DB_CHANNEL)
            file_er_id = forwarded_msg.message_id
            await forwarded_msg.reply_text(
                f"#PRIVATE_FILE:\n\n[{message.from_user.first_name}](tg://user?id={message.from_user.id}) Got File Link!",
                parse_mode="Markdown", disable_web_page_preview=True)
            share_link = f"https://t.me/{Config.BOT_USERNAME}?start=DisneyTeam_{file_er_id}"
            await editable.edit(
                f"**Your File Stored in my Database!**\n\nHere is the Permanent Link of your file: {share_link} \n\nJust Click the link to get your file!",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Open Link", url=share_link)],
                     [InlineKeyboardButton("👨‍🔧updates Channel👨‍🔧", url="https://t.me/disneygrou"),
                      InlineKeyboardButton("🤖Support Group🤖", url="https://t.me/disneyteamchat")]]
                ),
                disable_web_page_preview=True
            )
        except FloodWait as sl:
            await asyncio.sleep(sl.x)
            await bot.send_message(
                chat_id=Config.LOG_CHANNEL,
                text=f"#FloodWait:\nGot FloodWait of `{str(sl.x)}s` from `{str(message.chat.id)}` !!",
                parse_mode="Markdown",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(message.chat.id)}")]
                    ]
                )
            )
        except Exception as err:
            await editable.edit(f"Something Went Wrong!\n\n**Error:** `{err}`")
            await bot.send_message(
                chat_id=Config.LOG_CHANNEL,
                text=f"#ERROR_TRACEBACK:\nGot Error from `{str(message.chat.id)}` !!\n\n**Traceback:** `{err}`",
                parse_mode="Markdown",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(message.chat.id)}")]
                    ]
                )
            )
    elif message.chat.type == "channel":
        if (message.chat.id == Config.LOG_CHANNEL) or (message.chat.id == int(Config.UPDATES_CHANNEL)) or message.forward_from_chat or message.forward_from:
            return
        elif int(message.chat.id) in Config.BANNED_CHAT_IDS:
            await bot.leave_chat(message.chat.id)
            return
        else:
            pass
        try:
            forwarded_msg = await message.forward(Config.DB_CHANNEL)
            file_er_id = forwarded_msg.message_id
            share_link = f"https://t.me/{Config.BOT_USERNAME}?start=DisneyTeam_{file_er_id}"
            CH_edit = await bot.edit_message_reply_markup(message.chat.id, message.message_id,
                                                          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(
                                                              "Get Sharable Stored Link", url=share_link)]]))
            if message.chat.username:
                await forwarded_msg.reply_text(
                    f"#CHANNEL_BUTTON:\n\n[{message.chat.title}](https://t.me/{message.chat.username}/{CH_edit.message_id}) Channel's Broadcasted File's Button Added!")
            else:
                private_ch = str(message.chat.id)[4:]
                await forwarded_msg.reply_text(
                    f"#CHANNEL_BUTTON:\n\n[{message.chat.title}](https://t.me/c/{private_ch}/{CH_edit.message_id}) Channel's Broadcasted File's Button Added!")
        except FloodWait as sl:
            await asyncio.sleep(sl.x)
            await bot.send_message(
                chat_id=Config.LOG_CHANNEL,
                text=f"#FloodWait:\nGot FloodWait of `{str(sl.x)}s` from `{str(message.chat.id)}` !!",
                parse_mode="Markdown",
                disable_web_page_preview=True
            )
        except Exception as err:
            await bot.send_message(
                chat_id=Config.LOG_CHANNEL,
                text=f"#ERROR_TRACEBACK:\nGot Error from `{str(message.chat.id)}` !!\n\n**Traceback:** `{err}`",
                parse_mode="Markdown",
                disable_web_page_preview=True
            )


@Bot.on_message(filters.private & filters.command("broadcast") & filters.user(Config.BOT_OWNER) & filters.reply)
async def broadcast_handler_open(_, m: Message):
    await main_broadcast_handler(m, db)


@Bot.on_message(filters.private & filters.command("status") & filters.user(Config.BOT_OWNER))
async def sts(_, m: Message):
    total_users = await db.total_users_count()
    await m.reply_text(text=f"**Total Users in DB:** `{total_users}`", parse_mode="Markdown", quote=True)


@Bot.on_message(filters.private & filters.command("ban_user") & filters.user(Config.BOT_OWNER))
async def ban(c: Client, m: Message):
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to ban any user from the bot.\n\nUsage:\n\n`/ban_user user_id ban_duration ban_reason`\n\nEg: `/ban_user 1234567 28 You misused me.`\n This will ban user with id `1234567` for `1` day for the reason `You misused me`.",
            quote=True
        )
        return
    try:
        user_id = int(m.command[1])
        ban_duration = int(m.command[2])
        ban_reason = ' '.join(m.command[3:])
        ban_log_text = f"Banning user {user_id} for {ban_duration} days for the reason {ban_reason}."
        try:
            await c.send_message(
                user_id,
                f"You are banned to use this bot for **{ban_duration}** day(s) for the reason __{ban_reason}__ \n\n**Message from the admin**"
            )
            ban_log_text += '\n\nUser notified successfully!'
        except:
            traceback.print_exc()
            ban_log_text += f"\n\nUser notification failed! \n\n`{traceback.format_exc()}`"
        await db.ban_user(user_id, ban_duration, ban_reason)
        print(ban_log_text)
        await m.reply_text(
            ban_log_text,
            quote=True
        )
    except:
        traceback.print_exc()
        await m.reply_text(
            f"Error occoured! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True
        )


@Bot.on_message(filters.private & filters.command("unban_user") & filters.user(Config.BOT_OWNER))
async def unban(c: Client, m: Message):
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to unban any user.\n\nUsage:\n\n`/unban_user user_id`\n\nEg: `/unban_user 1234567`\n This will unban user with id `1234567`.",
            quote=True
        )
        return
    try:
        user_id = int(m.command[1])
        unban_log_text = f"Unbanning user {user_id}"
        try:
            await c.send_message(
                user_id,
                f"Your ban was lifted!"
            )
            unban_log_text += '\n\nUser notified successfully!'
        except:
            traceback.print_exc()
            unban_log_text += f"\n\nUser notification failed! \n\n`{traceback.format_exc()}`"
        await db.remove_ban(user_id)
        print(unban_log_text)
        await m.reply_text(
            unban_log_text,
            quote=True
        )
    except:
        traceback.print_exc()
        await m.reply_text(
            f"Error occoured! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True
        )


@Bot.on_message(filters.private & filters.command("banned_users") & filters.user(Config.BOT_OWNER))
async def _banned_usrs(_, m: Message):
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ''
    async for banned_user in all_banned_users:
        user_id = banned_user['id']
        ban_duration = banned_user['ban_status']['ban_duration']
        banned_on = banned_user['ban_status']['banned_on']
        ban_reason = banned_user['ban_status']['ban_reason']
        banned_usr_count += 1
        text += f"> **user_id**: `{user_id}`, **Ban Duration**: `{ban_duration}`, **Banned on**: `{banned_on}`, **Reason**: `{ban_reason}`\n\n"
    reply_text = f"Total banned user(s): `{banned_usr_count}`\n\n{text}"
    if len(reply_text) > 4096:
        with open('banned-users.txt', 'w') as f:
            f.write(reply_text)
        await m.reply_document('banned-users.txt', True)
        os.remove('banned-users.txt')
        return
    await m.reply_text(reply_text, True)


@Bot.on_callback_query()
async def button(bot: Client, cmd: CallbackQuery):
    cb_data = cmd.data
    if "aboutbot" in cb_data:
        await cmd.message.edit(
            Config.ABOUT_BOT_TEXT,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Source Codes of Bot",
                                             url="https://github.com/Disneyteam75/PyroFilesStoreBot")
                    ],
                    [
                        InlineKeyboardButton("Go Home", callback_data="gotohome"),
                        InlineKeyboardButton("About Dev", callback_data="aboutdevs")
                    ]
                ]
            )
        )
    elif "aboutdevs" in cb_data:
        await cmd.message.edit(
            Config.ABOUT_DEV_TEXT,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Source Codes of Bot",
                                             url="https://github.com/Disneyteam75/PyroFilesStoreBot")
                    ],
                    [
                        InlineKeyboardButton("About Bot", callback_data="aboutbot"),
                        InlineKeyboardButton("Go Home", callback_data="gotohome")
                    ]
                ]
            )
        )
    elif "gotohome" in cb_data:
        await cmd.message.edit(
            Config.HOME_TEXT.format(cmd.message.chat.first_name, cmd.message.chat.id),
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("👨‍🔧updates channel👨‍🔧", url="https://t.me/disneygrou"),
                        InlineKeyboardButton("🤖support group🤖", url="https://t.me/disneyteamchat")
                    ],
                    [
                        InlineKeyboardButton("About Bot", callback_data="aboutbot"),
                        InlineKeyboardButton("About Dev", callback_data="aboutdevs")
                    ]
                ]
            )
        )
    elif "refreshmeh" in cb_data:
        if Config.UPDATES_CHANNEL:
            invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
            try:
                user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), cmd.message.chat.id)
                if user.status == "kicked":
                    await cmd.message.edit(
                        text="Sorry Sir, You are Banned to use me. Contact my [ownet](https://t.me/doreamonfans1).",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await cmd.message.edit(
                    text="**You Still Didn't Join ☹️, Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 Join Updates Channel", url=invite_link.invite_link)
                            ],
                            [
                                InlineKeyboardButton("🔄 Refresh 🔄", callback_data="refreshmeh")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await cmd.message.edit(
                    text="Something went Wrong. Contact my [Support Group](https://t.me/disneyteamchat).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        await cmd.message.edit(
            text=Config.HOME_TEXT.format(cmd.message.chat.first_name, cmd.message.chat.id),
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("👨‍🔧updates channel👨‍🔧", url="https://t.me/disneygrou"),
                        InlineKeyboardButton("🤖support group🤖", url="https://t.me/Disneyteamchat")
                    ],
                    [
                        InlineKeyboardButton("About Bot", callback_data="aboutbot"),
                        InlineKeyboardButton("About Dev", callback_data="aboutdevs")
                    ]
                ]
            )
        )
    elif cb_data.startswith("ban_user_"):
        user_id = cb_data.split("_", 2)[-1]
        if Config.UPDATES_CHANNEL is None:
            await cmd.answer("Sorry Sir, You didn't Set any Updates Channel!", show_alert=True)
            return
        if not int(cmd.from_user.id) == Config.BOT_OWNER:
            await cmd.answer("You are not allowed to do that!", show_alert=True)
            return
        try:
            await bot.kick_chat_member(chat_id=int(Config.UPDATES_CHANNEL), user_id=int(user_id))
            await cmd.answer("User Banned from Updates Channel!", show_alert=True)
        except Exception as e:
            await cmd.answer(f"Can't Ban Him!\n\nError: {e}", show_alert=True)


Bot.run()
