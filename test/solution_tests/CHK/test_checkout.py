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
        assert checkout_solution.checkout('F') == 10
        assert checkout_solution.checkout('G') == 20
        assert checkout_solution.checkout('H') == 10
        assert checkout_solution.checkout('I') == 35
        assert checkout_solution.checkout('J') == 60
        assert checkout_solution.checkout('K') == 80
        assert checkout_solution.checkout('L') == 90
        assert checkout_solution.checkout('M') == 15
        assert checkout_solution.checkout('N') == 40
        assert checkout_solution.checkout('O') == 10
        assert checkout_solution.checkout('P') == 50
        assert checkout_solution.checkout('Q') == 30
        assert checkout_solution.checkout('R') == 50
        assert checkout_solution.checkout('S') == 30
        assert checkout_solution.checkout('T') == 20
        assert checkout_solution.checkout('U') == 40
        assert checkout_solution.checkout('V') == 50
        assert checkout_solution.checkout('W') == 20
        assert checkout_solution.checkout('X') == 90
        assert checkout_solution.checkout('Y') == 10
        assert checkout_solution.checkout('Z') == 50

    def test_checkout_with_multiple_different_items(self):
        assert checkout_solution.checkout('ABC') == 100
        assert checkout_solution.checkout('ABD') == 95
        assert checkout_solution.checkout('ABE') == 120

    def test_checkout_special_offer_A(self):
        assert checkout_solution.checkout('AAA') == 130
        assert checkout_solution.checkout('AAAA') == 180
        assert checkout_solution.checkout('AAAAA') == 200

    def test_checkout_special_offer_B(self):
        assert checkout_solution.checkout('BB') == 45
        assert checkout_solution.checkout('BBB') == 75

    def test_checkout_special_offer_E(self):
        assert checkout_solution.checkout('EEB') == 80
        assert checkout_solution.checkout('BEE') == 80
        assert checkout_solution.checkout('EEBEE') == 160
        assert checkout_solution.checkout('EEBEBE') == 160

    def test_checkout_special_offer_F(self):
        assert checkout_solution.checkout('FF') == 20
        assert checkout_solution.checkout('FFF') == 20
        assert checkout_solution.checkout('FFFF') == 30
        assert checkout_solution.checkout('FFFFF') == 40
        assert checkout_solution.checkout('FFFFFF') == 40

    def test_checkout_special_offer_H(self):
        assert checkout_solution.checkout('HHHH') == 40
        assert checkout_solution.checkout('HHHHH') == 45
        assert checkout_solution.checkout('HHHHHHHHH') == 85
        assert checkout_solution.checkout('HHHHHHHHHH') == 80

    def test_checkout_special_offer_K(self):
        assert checkout_solution.checkout('KK') == 150
        assert checkout_solution.checkout('KKK') == 230
        assert checkout_solution.checkout('KKKK') == 300

    def test_checkout_special_offer_N(self):
        assert checkout_solution.checkout('NNNM') == 120

    def test_checkout_multiple_items_with_offers(self):
        assert checkout_solution.checkout('AAABB') == 175
        assert checkout_solution.checkout('AAAABBB') == 255
        assert checkout_solution.checkout('ABCDABCADA') == 295
        assert checkout_solution.checkout('AAAABBBBEE') == 335
        assert checkout_solution.checkout('AAAAABBBBEE') == 355
        assert checkout_solution.checkout('AAAAABBBBEEFFFFFF') == 395

    def test_checkout_illegal_if_input_is_not_string(self):
        assert checkout_solution.checkout(1) == -1
        assert checkout_solution.checkout([1.2, 1.5]) == -1

    def test_checkout_illegal_if_input_contains_non_existing_item(self):
        assert checkout_solution.checkout('ABa') == -1
        assert checkout_solution.checkout('Hello, World!') == -1


