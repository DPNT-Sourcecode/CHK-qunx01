from solutions.CHK import checkout_solution


class TestSum:

    def test_checkout_with_zero_items(self):
        assert checkout_solution.checkout('') == 0

    def test_checkout_with_one_item(self):
        assert checkout_solution.checkout('A') == 50
        assert checkout_solution.checkout('B') == 30
        assert checkout_solution.checkout('C') == 20
        assert checkout_solution.checkout('D') == 15
        assert checkout_solution.checkout('E') == 40

    def test_checkout_with_multiple_different_items(self):
        assert checkout_solution.checkout('ABC') == 100
        assert checkout_solution.checkout('ABD') == 95
        assert checkout_solution.checkout('ABE') == 120

    def test_checkout_special_offer_A(self):
        assert checkout_solution.checkout('AAA') == 130
        assert checkout_solution.checkout('AAAA') == 180

    def test_checkout_special_offer_B(self):
        assert checkout_solution.checkout('BB') == 45
        assert checkout_solution.checkout('BBB') == 75

    def test_checkout_multiple_items_with_offers(self):
        assert checkout_solution.checkout('AAABB') == 175
        assert checkout_solution.checkout('AAAABBB') == 255
        assert checkout_solution.checkout('ABCDABCADA') == 295

    def test_checkout_illegal_if_input_is_not_string(self):
        assert checkout_solution.checkout(1) == -1
        assert checkout_solution.checkout([1.2, 1.5]) == -1

    def test_checkout_illegal_if_input_contains_non_existing_item(self):
        assert checkout_solution.checkout('ABF') == -1
        assert checkout_solution.checkout('Hello, World!') == -1

    def test_checkout_special_offer_E(self):
        assert checkout_solution.checkout('EEB') == 80
        assert checkout_solution.checkout('BEE') == 80
        assert checkout_solution.checkout('EEBEE') == 160
        assert checkout_solution.checkout('EEBEBE') == 160



