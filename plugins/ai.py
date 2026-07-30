from pyrogram import Client, filters
import aiohttp

async def ask(q):
    url = f"https://api.affiliateplus.xyz/api/chatbot?message={q}"
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as r:
            return (await r.json())["message"]

@Client.on_message(filters.command("ai", [".", "/"]))
async def ai(_, m):
    if len(m.command) < 2:
        return await m.reply("Use: .ai text")

    reply = await ask(m.text.split(None,1)[1])
    await m.reply(reply)
