from telegram import Update
from telegram.ext import ContextTypes

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سیگنال تستی ارسال شد")
