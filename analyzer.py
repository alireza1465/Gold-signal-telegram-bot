import requests

def get_gold_price():
    url = "https://api.metals.live/v1/spot"
    response = requests.get(url)
    data = response.json()
    for item in data:
        if isinstance(item, dict) and "gold" in item:
            return item["gold"]
    return None

def analyze_price(price):
    if price is None:
        return "قیمت طلا در دسترس نیست."
    if price < 2300:
        return f"قیمت فعلی طلا: {price}\n📉 سیگنال: خرید"
    elif price > 2350:
        return f"قیمت فعلی طلا: {price}\n📈 سیگنال: فروش"
    else:
        return f"قیمت فعلی طلا: {price}\n⏸️ سیگنال: صبر کن"
