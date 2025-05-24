from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from analyzer import get_gold_price, analyze_price
import os

# دریافت توکن از محیط
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام علیرضا! ربات سیگنال طلا آماده است 🚀")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price = get_gold_price()
    signal = analyze_price(price)
    await update.message.reply_text(signal)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.run_polling()
