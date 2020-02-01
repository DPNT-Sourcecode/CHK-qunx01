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
        price += number * price[sku]

    return price




