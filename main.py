from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# دریافت توکن از متغیر محیطی
TOKEN = os.getenv("TOKEN")

# تعریف دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام علیرضا! ربات سیگنال طلا آماده است 🚀")

# تعریف دستور /signal
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سیگنال تستی ارسال شد!")

# راه‌اندازی ربات
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.run_polling()
