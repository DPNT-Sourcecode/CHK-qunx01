# noinspection PyUnusedLocal
# skus = unicode string


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

    price = 0

    for sku in skus:
        price += prices[sku]

    return price



