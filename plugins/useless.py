from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime
from helper_func import get_readable_time
from database.database import full_userbase

LWAIT_MSG = "⏳"

@Bot.on_message(filters.command('stats') & filters.chat(AG) & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    now = datetime.now()
    msg = await client.send_message(chat_id=message.chat.id, text=LWAIT_MSG)
    users = await full_userbase()
    delta = now - client.uptime
    time = get_readable_time(delta.seconds)
    await msg.edit(f"#BOT_STATS\n👥Total Users: {len(users)}\n📡Uptime: {time}")
