from pyrogram import Client, filters
from pyrogram.types import Message
import re
import os
from handlers.link_handler import handle_link

BOT_TOKEN = "توکن_بات_تو_اینجا_بذار"

app = Client("auto_downloader_bot", bot_token=BOT_TOKEN)


@app.on_message(filters.private | filters.group & filters.text)
async def on_message(client: Client, message: Message):
    urls = re.findall(r'(https?://[^\s]+)', message.text or "")
    if not urls:
        return
    for url in urls:
        await message.reply_chat_action("upload_document")
        await handle_link(client, message, url)


@app.on_message(filters.command("start") & filters.private)
async def start_handler(client: Client, message: Message):
    await message.reply(
        "سلام!\n"
        "کافیه لینک هر فایل، ویدیو، موزیک یا هر محتوایی که میخوای دانلود کنی رو اینجا بفرستی، من برات می‌فرستم.\n"
        "از لینک‌های تلگرام پشتیبانی نمی‌کنم.\n"
        "با من همراه باش 🚀"
    )


if __name__ == "__main__":
    app.run()
