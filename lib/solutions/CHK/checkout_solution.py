# noinspection PyUnusedLocal
# skus = unicode string
from typing import List

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


@dataclass
class GroupOffer:
    number: int
    members: List[str]
    price: int


def group_offer_price_calculator(frequencies, prices, group_offers):
    price = 0
    frequencies_copy = deepcopy(frequencies)

    for group_offer in group_offers:
        total_frequency = 0
        for group_sku in group_offer.members:
            total_frequency += frequencies_copy[group_sku]

        n_offers = total_frequency // group_offer.number
        price += n_offers * group_offer.price

        n_to_reduce = n_offers * group_offer.number
        for sku in sorted(
            group_offer.members,
            key=lambda x: prices[x],
            reverse=True
        ):
            current_n_to_reduce = min(frequencies_copy[sku], n_to_reduce)
            frequencies_copy[sku] -= current_n_to_reduce
            n_to_reduce -= current_n_to_reduce

    return price, frequencies_copy


def multibuy_offer_price_calculator(frequencies, multibuy_offers):
    frequencies_copy = deepcopy(frequencies)

    for sku, multibuy_offer in multibuy_offers.items():
        multibuy_offer = multibuy_offers[sku]
        n_offers = frequencies_copy[sku] // multibuy_offer.number

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
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 70,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 20,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 17,
        'Y': 20,
        'Z': 21,
    }

    discount_offers = {
        'A': [
            DiscountOffer(number=5, price=200),
            DiscountOffer(number=3, price=130),
        ],
        'B': [DiscountOffer(number=2, price=45)],
        'F': [DiscountOffer(number=3, price=20)],
        'H': [
            DiscountOffer(number=10, price=80),
            DiscountOffer(number=5, price=45),
        ],
        'K': [DiscountOffer(number=2, price=120)],
        'P': [DiscountOffer(number=5, price=200)],
        'Q': [DiscountOffer(number=3, price=80)],
        'U': [DiscountOffer(number=4, price=120)],
        'V': [
            DiscountOffer(number=3, price=130),
            DiscountOffer(number=2, price=90),
        ],
    }

    multibuy_offers = {
        'E': MultibuyOffer(number=2, other_item='B'),
        'N': MultibuyOffer(number=3, other_item='M'),
        'R': MultibuyOffer(number=3, other_item='Q'),
    }

    group_offers = [
        GroupOffer(number=3, members=['S', 'T', 'X', 'Y', 'Z'], price=45),
    ]

    frequencies = Counter(skus)

    if any([sku not in prices.keys() for sku in frequencies.keys()]):
        return -1

    calculators = [
        lambda freqs: group_offer_price_calculator(freqs, prices, group_offers),
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

