from pyrogram import Client, filters
import random

SHAYARI = ["💔 Dard shayari", "❤️ Love shayari"]

@Client.on_message(filters.command("shayari", [".", "/"]))
async def shayari(_, m):
    await m.reply(random.choice(SHAYARI))
