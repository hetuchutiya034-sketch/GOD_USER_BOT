from pyrogram import filters, Client
from core.clients import vc
from pytgcalls.types.input_stream import AudioPiped
import yt_dlp

@Client.on_message(filters.command("play", ["."]))
async def play(_, m):
    if len(m.command) < 2:
        return await m.reply("Use: .play song")

    q = m.text.split(None,1)[1]

    ydl = yt_dlp.YoutubeDL({"format":"bestaudio","outtmpl":"song.mp3"})
    ydl.download([f"ytsearch:{q}"])

    await vc.join_group_call(m.chat.id, AudioPiped("song.mp3"))
    await m.reply("🎵 Playing")

@Client.on_message(filters.command("stop", ["."]))
async def stop(_, m):
    await vc.leave_group_call(m.chat.id)
    await m.reply("⏹ Stopped")
