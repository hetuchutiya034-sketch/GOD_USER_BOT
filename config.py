import os
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")
BOT_TOKEN = os.getenv("BOT_TOKEN")    
MONGO_URL = os.getenv("MONGO_URL")
