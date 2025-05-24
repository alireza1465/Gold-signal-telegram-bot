import os
import time
import requests
from analyzer import get_gold_price, analyze_price

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_signal():
    price = get_gold_price()
    signal = analyze_price(price)
    message = f"{signal}\nقیمت فعلی: {price}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

if __name__ == "__main__":
    while True:
        send_signal()
        time.sleep(60)  # هر ۶۰ ثانیه یک‌بار
