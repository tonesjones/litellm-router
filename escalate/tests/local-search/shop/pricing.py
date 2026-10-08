from shop.discounts import lookup


def apply_discount(price, code):
    rate = lookup(code.lower())
    return round(price * (1 - rate), 2)
