import os
import time
import requests

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_signal():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    message = "سیگنال تستی ارسال شد (ربات روشن است)"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

if __name__ == "__main__":
    while True:
        send_signal()
        time.sleep(60)
