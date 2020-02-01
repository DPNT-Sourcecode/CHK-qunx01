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
        assert checkout_solution.checkout('K') == 70
        assert checkout_solution.checkout('L') == 90
        assert checkout_solution.checkout('M') == 15
        assert checkout_solution.checkout('N') == 40
        assert checkout_solution.checkout('O') == 10
        assert checkout_solution.checkout('P') == 50
        assert checkout_solution.checkout('Q') == 30
        assert checkout_solution.checkout('R') == 50
        assert checkout_solution.checkout('S') == 20
        assert checkout_solution.checkout('T') == 20
        assert checkout_solution.checkout('U') == 40
        assert checkout_solution.checkout('V') == 50
        assert checkout_solution.checkout('W') == 20
        assert checkout_solution.checkout('X') == 17
        assert checkout_solution.checkout('Y') == 20
        assert checkout_solution.checkout('Z') == 21

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
        assert checkout_solution.checkout('HHHHH') == 45
        assert checkout_solution.checkout('HHHHHHHHH') == 85
        assert checkout_solution.checkout('HHHHHHHHHH') == 80

    def test_checkout_special_offer_K(self):
        assert checkout_solution.checkout('KK') == 120
        assert checkout_solution.checkout('KKK') == 120 + 70
        assert checkout_solution.checkout('KKKK') == 120 + 120

    def test_checkout_special_offer_N(self):
        assert checkout_solution.checkout('NNNM') == 120
        assert checkout_solution.checkout('NNM') == 40 + 40 + 15

    def test_checkout_special_offer_P(self):
        assert checkout_solution.checkout('PPPPP') == 200
        assert checkout_solution.checkout('PPPPPP') == 200 + 50

    def test_checkout_special_offer_Q(self):
        assert checkout_solution.checkout('QQQ') == 80
        assert checkout_solution.checkout('QQQQ') == 80 + 30

    def test_checkout_special_offer_R(self):
        assert checkout_solution.checkout('RRRQ') == 3 * 50
        assert checkout_solution.checkout('RRQ') == 2 * 50 + 30

    def test_checkout_special_offer_U(self):
        assert checkout_solution.checkout('UUUU') == 3 * 40
        assert checkout_solution.checkout('UUUUU') == 4 * 40

    def test_checkout_special_offer_V(self):
        assert checkout_solution.checkout('VV') == 90
        assert checkout_solution.checkout('VVV') == 130
        assert checkout_solution.checkout('VVVVV') == 90 + 130
        assert checkout_solution.checkout('VVVV') == 130 + 50

    def test_checkout_group_offer(self):
        assert checkout_solution.checkout('SSS') == 45

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
