import random

def get_gold_price():
    # شبیه‌سازی قیمت لحظه‌ای طلا
    return random.uniform(2300, 2500)

def analyze_price(price):
    if price < 2350:
        return f"💰 قیمت فعلی طلا: {price:.2f} ➤ سیگنال: خرید ✅"
    elif price > 2450:
        return f"💰 قیمت فعلی طلا: {price:.2f} ➤ سیگنال: فروش ❌"
    else:
        return f"💰 قیمت فعلی طلا: {price:.2f} ➤ سیگنال: نگهداری 📊"
