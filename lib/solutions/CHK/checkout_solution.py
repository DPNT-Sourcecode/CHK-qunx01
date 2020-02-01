# noinspection PyUnusedLocal
# skus = unicode string
from dataclasses import dataclass
from collections import Counter
from copy import deepcopy


@dataclass
class DiscountOffer:
    number: int
    price: int


@dataclass
class MultibuyOffer:
    number: int
    other_item: str


def multibuy_offer_price_calculator(frequencies, multibuy_offers):
    price = 0

    frequencies_copy = deepcopy(frequencies)

    for sku, multibuy_offer in multibuy_offers.items():
        multibuy_offer = multibuy_offers[sku]
        n_offers = frequencies[sku] // multibuy_offer.number
        frequencies_copy[multibuy_offer.other_item] = max(0, frequencies[multibuy_offer.other_item] - n_offers)

    return price, frequencies_copy


def discount_offer_price_calculator(frequencies, discount_offers):
    price = 0
    frequencies_copy = Counter()

    for sku, number in frequencies.items():
        if sku in discount_offers:
            discount_offer = discount_offers[sku]
            n_offers = number // discount_offer.number
            leftovers = number % discount_offer.number

            price += n_offers * discount_offer.price
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

    discount_offers = {
        'A': DiscountOffer(number=3, price=130),
        'B': DiscountOffer(number=2, price=45),
    }

    multibuy_offers = {
        'E': MultibuyOffer(number=2, other_item='B')
    }

    frequencies = Counter(skus)

    if any([sku not in prices.keys() for sku in frequencies.keys()]):
        return -1

    price = 0

    current_price, frequencies = multibuy_offer_price_calculator(frequencies, multibuy_offers)
    price += current_price

    current_price, frequencies = discount_offer_price_calculator(frequencies, discount_offers)
    price += current_price

    current_price, frequencies = default_price_calculator(frequencies, prices)
    price += current_price

    return price


