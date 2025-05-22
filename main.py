import telebot
from flask import Flask, request

TOKEN = '7635073258:AAHEd2yddm0ihR-l8Z_0P8UetkerdC77-gs'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام علیرضا! ✅ ربات تحلیلگر طلا فعال است.")

@app.route(f"/{TOKEN}", methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "ربات تحلیلگر طلا اجرا شده ✅", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
