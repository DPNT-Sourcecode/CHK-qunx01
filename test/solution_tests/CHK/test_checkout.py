from solutions.CHK import checkout_solution


class TestSum:

    def test_checkout_with_zero_items(self):
        assert checkout_solution.checkout('') == 0

    def test_checkout_with_one_item(self):
        assert checkout_solution.checkout('A') == 50
        assert checkout_solution.checkout('B') == 30
        assert checkout_solution.checkout('C') == 20
        assert checkout_solution.checkout('D') == 15

    def test_checkout_with_multiple_different_items(self):
        assert checkout_solution.checkout('A B C') == 100
        assert checkout_solution.checkout('A B D') == 95

    def test_checkout_special_offer_A(self):
        assert checkout_solution.checkout('A A A') == 130
        assert checkout_solution.checkout('A A A A') == 180
