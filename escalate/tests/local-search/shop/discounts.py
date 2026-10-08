from shop.config import DISCOUNT_CODES


def lookup(code):
    return DISCOUNT_CODES.get(code.strip(), 0.0)
