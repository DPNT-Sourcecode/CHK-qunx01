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
    minimum: int = 0


def multibuy_offer_price_calculator(frequencies, multibuy_offers):
    frequencies_copy = deepcopy(frequencies)

    for sku, multibuy_offer in multibuy_offers.items():
        multibuy_offer = multibuy_offers[sku]

        if frequencies_copy[sku] >= multibuy_offer.minimum:
            n_offers = frequencies_copy[sku] // multibuy_offer.number
        else:
            n_offers = 0

        frequencies_copy[multibuy_offer.other_item] = max(
            0,
            frequencies_copy[multibuy_offer.other_item] - n_offers
        )

    return 0, frequencies_copy


def discount_offer_price_calculator(frequencies, discount_offers):
    price = 0
    frequencies_copy = deepcopy(frequencies)

    for sku, offers_list in discount_offers.items():
        for discount_offer in offers_list:
            n_items = frequencies_copy[sku]
            n_offers = n_items // discount_offer.number
            leftovers = n_items % discount_offer.number

            price += n_offers * discount_offer.price
            frequencies_copy[sku] = leftovers

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
        'F': 10,
    }

    discount_offers = {
        'A': [
            DiscountOffer(number=5, price=200),
            DiscountOffer(number=3, price=130)
        ],
        'B': [DiscountOffer(number=2, price=45)],
    }

    multibuy_offers = {
        'E': MultibuyOffer(number=2, other_item='B'),
        'F': MultibuyOffer(number=2, other_item='F', minimum=3),
    }

    frequencies = Counter(skus)

    if any([sku not in prices.keys() for sku in frequencies.keys()]):
        return -1

    calculators = [
        lambda freqs: multibuy_offer_price_calculator(freqs, multibuy_offers),
        lambda freqs: discount_offer_price_calculator(freqs, discount_offers),
        lambda freqs: default_price_calculator(freqs, prices),
    ]

    price = 0
    current_frequencies = frequencies
    for calculator in calculators:
        current_price, current_frequencies = calculator(current_frequencies)
        price += current_price

    return price




