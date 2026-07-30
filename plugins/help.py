from pyrogram import Client, filters

HELP_TEXT = """
😈 SEHTANI USERBOT 💀

⚡ BASIC
.ping — check bot
.help — show help

🎵 MUSIC
.play song
.stop

🤖 AI
.ai text

👁️ TRACK
.tracker on/off

⚙️ SYSTEM
.stats
"""

@Client.on_message(filters.command("help", [".", "/"]))
async def help_cmd(_, m):
    await m.reply(HELP_TEXT)
