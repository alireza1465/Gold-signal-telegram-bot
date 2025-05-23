import random

def get_gold_price():
    # شبیه‌سازی قیمت طلا (در واقعیت اینو از سایت‌ها می‌گیریم)
    return random.uniform(2300, 2500)

def analyze_price(price):
    if price < 2350:
        return "📈 سیگنال خرید: قیمت پایین است"
    elif price > 2450:
        return "📉 سیگنال فروش: قیمت بالا است"
    else:
        return "⏳ هنوز سیگنال واضحی وجود ندارد"
