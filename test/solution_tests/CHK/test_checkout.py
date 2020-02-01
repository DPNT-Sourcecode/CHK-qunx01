from solutions.CHK import checkout_solution


class TestSum:

    def test_checkout_with_zero_items(self):
        assert checkout_solution.checkout('') == 0

    def test_checkout_with_one_item(self):
        assert checkout_solution.checkout('A') == 50
        assert checkout_solution.checkout('B') == 30
        assert checkout_solution.checkout('C') == 20
        assert checkout_solution.checkout('D') == 15


