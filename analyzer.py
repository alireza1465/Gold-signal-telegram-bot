def get_gold_price():
    # این فقط یک عدد تستی است؛ بعداً به API متصل می‌کنیم
    return 2350

def analyze_price(price):
    if price > 2400:
        return "سیگنال فروش"
    elif price < 2300:
        return "سیگنال خرید"
    else:
        return "منتظر بمانید"
