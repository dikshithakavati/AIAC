def discount(price, category):
    if category == "student":
        return price * 0.9 if price > 1000 else price * 0.95
    return price * 0.85 if price > 2000 else price
a = discount(1500, "student")
print("cost after applying discount:",a)
