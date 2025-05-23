import asyncio
import os
from telegram import Bot
from analyzer import get_gold_price, analyze_price

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

async def send_signal():
    while True:
        price = get_gold_price()
        signal = analyze_price(price)
        try:
            await bot.send_message(chat_id=CHAT_ID, text=signal)
        except Exception as e:
            print("Error:", e)
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(send_signal())
