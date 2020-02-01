# noinspection PyUnusedLocal
# skus = unicode string
from dataclasses import dataclass
from collections import Counter


@dataclass
class SpecialOffer:
    number: int
    price: int


def checkout(skus):
    if not isinstance(skus, str):
        return -1

    if not skus:
        return 0

    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
    }

    special_offers = {
        'A': SpecialOffer(number=3, price=130),
        'B': SpecialOffer(number=2, price=45),
    }

    frequencies = Counter(skus)
    if any([sku not in prices.keys() for sku in frequencies.keys()]):
        return -1

    price = 0
    for sku, number in frequencies.items():
        if sku in special_offers:
            special_offer = special_offers[sku]
            price += number // special_offer.number * special_offer.price
            price += number % special_offer.number * prices[sku]
        else:
            price += number * prices[sku]

    return price

