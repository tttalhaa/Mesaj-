from pyrogram import Client as Bot

from config import API_ID, API_HASH, BOT_TOKEN


Client = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="main.py ")
)

Client.run() 
