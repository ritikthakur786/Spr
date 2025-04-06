import asyncio
from os.path import exists
from sqlite3 import connect

from aiohttp import ClientSession
from pyrogram import Client
from Python_ARQ import ARQ

SESSION_NAME = "spr"
DB_NAME = "db.sqlite3"
API_ID = 6
API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
ARQ_API_URL = "https://arq.hamker.dev"

# Config import
if exists("config.py"):
    from config import *
else:
    from sample_config import *


session = ClientSession()


# SQLite DB Connection
conn = connect(DB_NAME)

# Pyrogram Bot Client
spr = Client(
    SESSION_NAME,
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
)

async def main():
    await spr.start()

    # Get Bot Info
    bot = await spr.get_me()
    BOT_ID = bot.id
    BOT_USERNAME = bot.username

    # HTTP Session + ARQ setup
    async with ClientSession() as session:
        arq = ARQ(ARQ_API_URL, ARQ_API_KEY, session)

        print(f"Bot @{BOT_USERNAME} started with ID {BOT_ID}!")

        # Wait forever until stopped (Heroku worker will keep this alive)
        await asyncio.Event().wait()

    await spr.stop()

if __name__ == "__main__":
    asyncio.run(main())
