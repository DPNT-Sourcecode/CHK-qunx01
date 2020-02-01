# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter


def checkout(skus):
    if not skus:
        return 0

    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
    }

    skus = skus.split(' ')

    frequencies = Counter(skus)

    price = 0
    for sku, number in frequencies.items():
        if sku == 'A':
            special_price = number // 3 * 130
            price += special_price + (number % 3) * prices[sku]
        elif sku == 'B':
            special_price = number // 2 * 45
            price += special_price + (number % 2) * prices[sku]
        else:
            price += number * prices[sku]

    return price

