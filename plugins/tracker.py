from pyrogram import Client, filters
from database import set_toggle, get_toggle

@Client.on_message(filters.command("tracker", ["."]))
async def tracker(_, m):
    state = not get_toggle("tracker")
    set_toggle("tracker", state)
    await m.reply(f"Tracker {'ON' if state else 'OFF'}")
