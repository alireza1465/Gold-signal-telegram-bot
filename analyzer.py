import requests

def get_gold_price():
    response = requests.get("https://api.metals.live/v1/spot")
    data = response.json()
    for item in data:
        if "gold" in item:
            return float(item["gold"])
    return 0

def analyze_price(price):
    if price < 2300:
        return f"📉 قیمت فعلی طلا: {price}$ \n📢 سیگنال: خرید کن ✅"
    elif price > 2400:
        return f"📈 قیمت فعلی طلا: {price}$ \n📢 سیگنال: بفروش ❌"
    else:
        return f"💤 قیمت فعلی طلا: {price}$ \n📢 سیگنال: صبر کن ⏳"
