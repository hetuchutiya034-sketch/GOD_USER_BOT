from pyrogram import Client
from config import API_ID, API_HASH, SESSION
from core.god_core import run_core

app = Client(
    "sehtani_userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION,
    plugins=dict(root="plugins")
)

@app.on_message()
async def start_core(client, message):
    await run_core(client)

print("😈 SEHTANI USERBOT STARTED 💀")
app.run()
