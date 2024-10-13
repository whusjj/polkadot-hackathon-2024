import unittest
from decimal import Decimal

from demeter.uniswap import helper, liquitidy_math
from tests.common import assert_equal_with_error

D0 = Decimal(1)


class UniLpDataTest(unittest.TestCase):

    def test_delta_gamma_is_0_base(self):
        price = Decimal(1000)
        price_diff = 100
        sqrt = helper.base_unit_price_to_sqrt_price_x96(price, 6, 18, True)
        lower_tick = helper.base_unit_price_to_tick(price - price_diff, 6, 18, True)
        upper_tick = helper.base_unit_price_to_tick(price + price_diff, 6, 18, True)

        liquidity = liquitidy_math.get_liquidity(sqrt, lower_tick, upper_tick, Decimal(1000), Decimal(1), 6, 18)

        low_price_float = float(price) - price_diff
        high_price_float = float(price) + price_diff

        very_low_sqrt = helper.base_unit_price_to_sqrt_price_x96(Decimal(1), 6, 18, True)
        amount0, amount1 = liquitidy_math.get_amounts(very_low_sqrt, lower_tick, upper_tick, liquidity, 6, 18)
        delta, gamma = helper.get_delta_gamma(low_price_float, high_price_float, 1, liquidity, 6, 18, True)
        self.assertTrue(assert_equal_with_error(amount1, Decimal(delta), allowed_error=0.01))
        self.assertTrue(gamma == 0)

        delta, gamma = helper.get_delta_gamma(low_price_float, high_price_float, 2000, liquidity, 6, 18, True)
        self.assertEqual(delta, 0)
        self.assertEqual(gamma, 0)

        delta, gamma = helper.get_delta_gamma(low_price_float, high_price_float, float(price), liquidity, 6, 18, True)
        print(delta, gamma)

        self.assertTrue(assert_equal_with_error(delta, 0.9074351443912998))
        self.assertTrue(assert_equal_with_error(gamma, -0.009749523337042907))

    def test_amount_is_0_base(self):
        """
        verify calculation of net value is right.
        :return:
        :rtype:
        """
        k = 2**96
        price = Decimal(1100)
        price_float = float(price)
        d0 = 6
        d1 = 18
        d = d0 - d1
        sqrt = helper.base_unit_price_to_sqrt_price_x96(price, 6, 18, True)
        lower_tick = helper.base_unit_price_to_tick(Decimal(600), d0, d1, True)
        upper_tick = helper.base_unit_price_to_tick(Decimal(1100), d0, d1, True)
        lower_sqrt = helper.base_unit_price_to_sqrt_price_x96(Decimal(1100), d0, d1, True)
        upper_sqrt = helper.base_unit_price_to_sqrt_price_x96(Decimal(600), d0, d1, True)

        liquidity = liquitidy_math.get_liquidity(sqrt, lower_tick, upper_tick, Decimal(1000), Decimal(1), d0, d1)

        amount0, amount1 = liquitidy_math.get_amounts(sqrt, lower_tick, upper_tick, liquidity, d0, d1)
        net_value_old = amount0 + amount1 * price
        print(amount0, amount1)

        net_value_new = (
            liquidity * 10 ** (0.5 * d) / 10**d0 * price_float**0.5
            - k / upper_sqrt * liquidity / 10**d0
            + liquidity * price_float**0.5 / 10**d1 / 10 ** (0.5 * d)
            - lower_sqrt / k * price_float * liquidity / 10**d1
        )
        print(net_value_old, net_value_new)
        self.assertTrue(assert_equal_with_error(net_value_old, Decimal(net_value_new), allowed_error=0.001))

    def test_delta_gamma_is_1_base(self):
        price = Decimal("1000")
        price_diff = 100
        sqrt = helper.base_unit_price_to_sqrt_price_x96(price, 18, 6, False)
        lower_tick = helper.base_unit_price_to_tick(price - price_diff, 18, 6, False)
        upper_tick = helper.base_unit_price_to_tick(price + price_diff, 18, 6, False)

        liquidity = liquitidy_math.get_liquidity(sqrt, lower_tick, upper_tick, Decimal(1), Decimal(1000), 18, 6)

        low_price_float = float(price) - price_diff
        high_price_float = float(price) + price_diff

        delta, gamma = helper.get_delta_gamma(low_price_float, high_price_float, 2000, liquidity, 18, 6, False)
        self.assertEqual(delta, 0)
        self.assertEqual(gamma, 0)

        very_low_sqrt = helper.base_unit_price_to_sqrt_price_x96(Decimal(1), 18, 6, False)
        amount0, amount1 = liquitidy_math.get_amounts(very_low_sqrt, lower_tick, upper_tick, liquidity, 18, 6)
        delta, gamma = helper.get_delta_gamma(low_price_float, high_price_float, 1, liquidity, 18, 6, False)
        self.assertTrue(assert_equal_with_error(amount0, Decimal(delta), allowed_error=0.01))
        self.assertTrue(gamma == 0)

        delta, gamma = helper.get_delta_gamma(low_price_float, high_price_float, float(price), liquidity, 18, 6, False)
        print(delta, gamma)
        self.assertTrue(assert_equal_with_error(delta, 0.9074351443912998))
        self.assertTrue(assert_equal_with_error(gamma, -0.009749523337042907))

    def test_amount_is_1_base(self):
        """
        verify calculation of net value is right.
        :return:
        :rtype:
        """
        k = 2**96
        price = Decimal(850)
        price_float = float(price)
        d0 = 18
        d1 = 6
        d = d0 - d1
        sqrt = helper.base_unit_price_to_sqrt_price_x96(price, d0, d1, False)
        lower_tick = helper.base_unit_price_to_tick(Decimal(600), d0, d1, False)
        upper_tick = helper.base_unit_price_to_tick(Decimal(1100), d0, d1, False)
        lower_sqrt = helper.base_unit_price_to_sqrt_price_x96(Decimal(600), d0, d1, False)
        upper_sqrt = helper.base_unit_price_to_sqrt_price_x96(Decimal(1100), d0, d1, False)

        liquidity = liquitidy_math.get_liquidity(sqrt, lower_tick, upper_tick, Decimal(1), Decimal(1000), d0, d1)

        amount0, amount1 = liquitidy_math.get_amounts(sqrt, lower_tick, upper_tick, liquidity, d0, d1)
        net_value_old = amount0 * price + amount1
        print(amount0, amount1)

        net_value_new = (
            liquidity * price_float**0.5 * 10 ** (0.5 * d) / 10**d0
            - k / upper_sqrt * liquidity * price_float / 10**d0
            + liquidity * price_float**0.5 / 10**d1 / 10 ** (0.5 * d)
            - lower_sqrt / k * liquidity / 10**d1
        )
        print(net_value_old, net_value_new)
        self.assertTrue(assert_equal_with_error(net_value_old, Decimal(net_value_new), allowed_error=0.001))

    def test_tick_and_base_unit_price(self):
        base_unit_price = helper.tick_to_base_unit_price(196147, 6, 18, True)
        self.assertEqual(base_unit_price, Decimal("3032.9826448067293827922140338613115"))
        tick = helper.base_unit_price_to_tick(base_unit_price, 6, 18, True)
        self.assertEqual(tick, 196147)

    def test_base_unit_price_and_sqrt(self):
        base_unit_price = helper.sqrt_price_x96_to_base_unit_price(1438615122195042638686831659635746, 6, 18, True)
        self.assertEqual(base_unit_price, Decimal("3032.9826448067293827922140338613115"))
        sqrted = helper.base_unit_price_to_sqrt_price_x96(base_unit_price, 6, 18, True)
        self.assertEqual(sqrted, 1438615122195042638686831659635746)

    def test_sqrt_and_tick(self):

        sqrt_price_x96 = helper.tick_to_sqrt_price_x96(196147)
        print(sqrt_price_x96)
        tick = helper.sqrt_price_x96_to_tick(sqrt_price_x96)
        print(tick)
        self.assertEqual(tick, 196147)
