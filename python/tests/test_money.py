
import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.money_calculator import MoneyCalculator

class TestMoney:
    def test_add_in_usd_returns_value(self):
        #ARRANGE
        base_amount = 5
        other_amount = 10
        expected_amount = 15
        #ACT
        result = MoneyCalculator.add(base_amount, Currency.USD, other_amount)   

        #ASSERT
        assert isinstance(result, float)
        assert result == expected_amount

    def test_multiply_in_euros_returns_positive_number(self):
        #ARRANGE
        base_amount = 10
        expected_amount = 20
        factor = 2
        #ACT
        result = MoneyCalculator.multiply(base_amount, Currency.EUR, factor)
        #ASSERT
        assert result == expected_amount

    def test_divide_in_korean_won_returns_float(self):
        #ARRANGE
        base_amount = 4002
        expected_amount = 1000.5
        divisor = 4
        #ACT
        result = MoneyCalculator.divide(base_amount, Currency.USD, divisor)
        #ASSERT
        assert result == expected_amount