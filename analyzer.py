import requests

def get_gold_price():
    # نمونه ساده قیمت‌گذاری فرضی (برای تست)
    url = "https://api.metals.live/v1/spot/gold"
    response = requests.get(url)
    data = response.json()
    price = data[0]["gold"]
    return price

def analyze_price(price):
    # الگوریتم ساده برای سیگنال‌دهی
    if price < 2000:
        return "سیگنال خرید ✅"
    elif price > 2300:
        return "سیگنال فروش ❌"
    else:
        return "منتظر بمانید ⏳"
