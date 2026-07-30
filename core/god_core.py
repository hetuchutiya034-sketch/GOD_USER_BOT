import asyncio
import datetime
from database import get_toggle
from core.logger import log

# ===== AUTO BIO SYSTEM =====
async def auto_bio(client):
    while True:
        try:
            if get_toggle("autobio"):
                await client.update_profile(
                    bio=f"😈 SEHTANI | {datetime.datetime.now().strftime('%H:%M')}"
                )
                log("Auto Bio Updated")
        except Exception as e:
            log(f"AutoBio Error: {e}")
        await asyncio.sleep(60)

# ===== HEALTH MONITOR =====
async def health_check():
    while True:
        log("💀 GOD CORE RUNNING")
        await asyncio.sleep(30)

# ===== RUN CORE =====
async def run_core(client):
    asyncio.create_task(auto_bio(client))
    asyncio.create_task(health_check())
