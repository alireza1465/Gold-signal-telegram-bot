import telebot
import requests
import time

# جایگزین کن با توکن واقعی رباتت
bot = telebot.TeleBot("توکن_ربات_شما")

# جایگزین کن با آیدی عددی تلگرام خودت
user_id = 123456789

last_signal = None

def get_gold_price():
    try:
        url = "https://api.metals.dev/v1/latest?symbol=XAU&api_key=demo"
        response = requests.get(url)
        data = response.json()
        return float(data['metals']['XAU']['price'])
    except Exception as e:
        print("Error fetching gold price:", e)
        return None

def check_signal():
    global last_signal
    price = get_gold_price()
    if price:
        if price < 2300 and last_signal != "buy":
            bot.send_message(user_id, f"📉 سیگنال خرید: قیمت فعلی طلا {price} دلار")
            last_signal = "buy"
        elif price > 2350 and last_signal != "sell":
            bot.send_message(user_id, f"📈 سیگنال فروش: قیمت فعلی طلا {price} دلار")
            last_signal = "sell"
        else:
            print(f"No signal change. Price: {price}")

while True:
    check_signal()
    time.sleep(60)
