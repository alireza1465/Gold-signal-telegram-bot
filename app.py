import telebot

# 🔑 توکن رباتت
TOKEN = "7635073258:AAHEd2yddm0ihR-l8Z_0P8UetkerdC77-gs"

bot = telebot.TeleBot(TOKEN)

# ❗ حذف Webhook برای جلوگیری از خطای 409
bot.remove_webhook()

# ✅ پاسخ به دستور /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! ربات سیگنال طلا فعال شد ✅")

# ✅ فعال کردن Polling (دریافت پیام‌ها)
bot.polling()
