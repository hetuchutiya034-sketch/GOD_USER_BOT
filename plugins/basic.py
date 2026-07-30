from pyrogram import Client, filters
import time

@Client.on_message(filters.command("ping", [".", "/"]))
async def ping(_, m):
    start = time.time()
    msg = await m.reply("🏓 Pinging...")
    end = time.time()
    await msg.edit(f"🏓 Pong: {round((end-start)*1000)} ms")
