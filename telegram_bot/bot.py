### **`telegram_bot/bot.py`** - Main logic for the Telegram bot using Telethon

import os
from telethon import TelegramClient, events, Button
from dotenv import load_dotenv
from config.settings import settings

# Load environment variables from secrets.env file
load_dotenv(dotenv_path="config/secrets.env")

api_id = settings.telegram_api_id
api_hash = settings.telegram_api_hash
bot_token = settings.telegram_bot_token

client = TelegramClient('bot', api_id, api_hash)

@client.on(events.NewMessage(pattern='/startgame'))
async def start_game(event):

    await event.respond(
        "Click the button below to start the chess game!",
        buttons=[
            Button.url("Start Chess Game", f"https://bot-bee.online/chessboard")
        ]
    )

@client.on(events.NewMessage(pattern='/move'))
async def process_move(event):
    move = event.raw_text.split()[1]
    await event.respond(f"Move: {move}")

client.start(bot_token=bot_token)
client.run_until_disconnected()