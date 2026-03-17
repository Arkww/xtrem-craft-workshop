
import pytest

from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.money_calculator import MoneyCalculator
from xterm_craft_workshop.money import Money

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

    def test_create_money(self):
        amount = 10
        currency = Currency.EUR
        
        monnaie = Money(amount, currency)
        assert monnaie.amount == amount
        assert monnaie.currency == currency

    def test_add_money(self):
        base_amount = 10
        currency = Currency.EUR
        other_amount = 5
        expected_amount = 15
        
        monnaie = Money(base_amount, currency)
        result = monnaie.add(other_amount, currency)
        assert result.amount == expected_amount
        assert result.currency == currency

    def test_times_money(self):
        base_amount = 10
        currency = Currency.EUR
        factor = 3
        expected_amount = 30
        
        monnaie = Money(base_amount, currency)
        result = monnaie.times(factor)
        assert result.amount == expected_amount
        assert result.currency == currency

    def test_wrong_money(self):
        base_amount = 10
        currency = Currency.EUR
        usd_monnaie = Currency.USD
        eur = Money(base_amount, currency)


        with pytest.raises(ValueError) as error:
            result = eur.add(base_amount, usd_monnaie)
        assert str(error.value) == "Cannot add money with different currencies"

    def test_negative_money(self):
        base_amount = 10
        currency = Currency.EUR
        neg_amount = -1
        eur = Money(base_amount, currency)


        with pytest.raises(ValueError) as error:
            result = eur.add(neg_amount, currency)
        assert str(error.value) == "Amount cannot be negative"

    def test_negative_times(self):
        base_amount = 10
        currency = Currency.EUR
        factor = -1
        eur = Money(base_amount, currency)


        with pytest.raises(ValueError) as error:
            result = eur.times(factor)
        assert str(error.value) == "Factor cannot be negative"