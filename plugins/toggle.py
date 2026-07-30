from pyrogram import Client, filters
from database import set_toggle, get_toggle

@Client.on_message(filters.command("autobio", ["."]))
async def autobio(_, m):
    state = not get_toggle("autobio")
    set_toggle("autobio", state)
    await m.reply(f"AutoBio {'ON' if state else 'OFF'}")
