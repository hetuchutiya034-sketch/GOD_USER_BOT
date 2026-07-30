import os
from core.logger import log

def update_repo():
    try:
        os.system("git pull")
        log("✅ Repo Updated")
    except Exception as e:
        log(f"Update Error: {e}")
