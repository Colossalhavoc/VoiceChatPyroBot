from pyrogram import filters
from pyrogram.handlers import MessageHandler
from strings import get_string as _


async def start(client, message):
    await message.reply_text(_("send_yt_link"))

__handlers__ = [
    [
        MessageHandler(
            start,
            filters.command("start", "/")
            & filters.private
        )
    ]
]
