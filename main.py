import asyncio
from pyrogram import idle
from core.clients import user, bot, vc
from core.god_core import run_core
from core.logger import log

# ========= START SYSTEM =========

async def start_all():
    try:
        # Start userbot
        await user.start()
        log("👤 Userbot Started")

        # Start bot
        await bot.start()
        log("🤖 Bot Started")

        # Start voice client
        await vc.start()
        log("🎵 VC Client Started")

        # Start core system
        await run_core(user)

        log("😈 SEHTANI SYSTEM FULLY STARTED 💀")

    except Exception as e:
        log(f"❌ Startup Error: {e}")

# ========= MAIN =========

async def main():
    await start_all()
    await idle()  # keep running

if __name__ == "__main__":
    asyncio.run(main())
