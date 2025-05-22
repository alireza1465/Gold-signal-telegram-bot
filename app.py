import telebot
import requests

BOT_TOKEN = '7635073258:AAHEd2yddm0ihR-l8Z_0P8UetkerdC77-gs'
CHAT_ID = 'Alireza1465'

bot = telebot.TeleBot(BOT_TOKEN)

def get_gold_price():
    url = 'https://api.metals.live/v1/spot'
    response = requests.get(url)
    data = response.json()
    gold_price = data[0]['gold']
    return gold_price

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! ربات سیگنال طلا فعال شد ✅")

@bot.message_handler(commands=['price'])
def send_gold_price(message):
    price = get_gold_price()
    bot.send_message(message.chat.id, f"💰 قیمت لحظه‌ای طلا: {price} دلار")

bot.infinity_polling()
