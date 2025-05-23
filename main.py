import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام علیرضا! ربات سیگنال طلا آماده است 🚀")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://api.metals.live/v1/spot/gold")
    gold_price = response.json()[0]
    signal = "📈 سیگنال خرید" if gold_price < 2350 else "📉 سیگنال فروش"
    await update.message.reply_text(f"قیمت طلا: {gold_price}$\n{signal}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        webhook_url=f"{WEBHOOK_URL}/{TOKEN}"
    )
