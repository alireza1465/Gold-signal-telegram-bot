def get_gold_price():
    import random
    return round(random.uniform(2000, 2500), 2)

def analyze_price(price):
    if price < 2100:
        return "سیگنال خرید: قیمت پایین است"
    elif price > 2400:
        return "سیگنال فروش: قیمت بالا است"
    else:
        return "در حال بررسی بازار..."
