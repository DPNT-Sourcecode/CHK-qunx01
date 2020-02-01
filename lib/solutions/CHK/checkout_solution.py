# noinspection PyUnusedLocal
# skus = unicode string
from dataclasses import dataclass
from collections import Counter


@dataclass
class SpecialOffer:
    number: int
    price: int


def discount_offer_price_calculator(frequencies, special_offers):
    price = 0

    frequencies_copy = Counter()

    for sku, number in frequencies.items():
        if sku in special_offers:
            special_offer = special_offers[sku]
            n_offers = number // special_offer.number
            leftovers = number % special_offer.number

            price += n_offers * special_offer.price
            frequencies_copy[sku] = leftovers

        else:
            frequencies_copy[sku] = number

    return price, frequencies_copy


def default_price_calculator(frequencies, prices):
    price = 0
    for sku, number in frequencies.items():
        price += number * prices[sku]
    return price, Counter()


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

    if 'E' and 'B' in frequencies:
        frequencies['B'] = max(0, frequencies['B'] - frequencies['E'] // 2)

    price = 0

    current_price, frequencies = discount_offer_price_calculator(frequencies, special_offers)
    price += current_price

    current_price, frequencies = default_price_calculator(frequencies, prices)
    price += current_price

    return price




