from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from analyzer import get_gold_price, analyze_price
import os

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام علیرضا! ربات سیگنال طلا آماده است 🚀")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price = get_gold_price()
    result = analyze_price(price)
    await update.message.reply_text(f"{result}\nقیمت لحظه‌ای طلا: {price}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.run_polling()
