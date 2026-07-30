from pyrogram import Client, filters
import random

JOKES = ["😂 Joke 1", "🤣 Joke 2"]

@Client.on_message(filters.command("joke", [".", "/"]))
async def joke(_, m):
    await m.reply(random.choice(JOKES))
