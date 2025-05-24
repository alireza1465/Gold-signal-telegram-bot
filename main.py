from telegram import Update
from telegram.ext import Application, CommandHandler
from analyzer import get_gold_price, analyze_price
import os

# دریافت توکن از متغیر محیطی
TOKEN = os.getenv("TOKEN")

# دستور start
async def start(update: Update, context):
    await update.message.reply_text("🚀 سلام علیرضا! ربات سیگنال طلا آماده است")

# دستور signal
async def signal(update: Update, context):
    price = get_gold_price()
    signal = analyze_price(price)
    await update.message.reply_text(f"قیمت فعلی: {price}\nسیگنال: {signal}")

# اجرای ربات
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.run_polling()
