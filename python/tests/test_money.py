import pytest

from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.money import Money


class TestMoney:
    def test_add_in_usd_returns_value(self):
        # ARRANGE
        money1 = Money(5, Currency.USD)
        money2 = Money(10, Currency.USD)
        expected = Money(15, Currency.USD)

        # ACT
        result = money1 + money2

        # ASSERT
        assert isinstance(result, Money)
        assert result == expected

    def test_add_number_to_money(self):
        # ARRANGE
        money = Money(5, Currency.USD)
        expected = Money(15, Currency.USD)

        # ACT
        result = money + 10

        # ASSERT
        assert result == expected

    def test_radd_number_to_money(self):
        # ARRANGE
        money = Money(5, Currency.USD)
        expected = Money(15, Currency.USD)

        # ACT
        result = 10 + money

        # ASSERT
        assert result == expected

    def test_multiply_in_euros_returns_positive_number(self):
        # ARRANGE
        money = Money(10, Currency.EUR)
        expected = Money(20, Currency.EUR)

        # ACT
        result = money * 2

        # ASSERT
        assert result == expected

    def test_rmultiply_in_euros_returns_positive_number(self):
        # ARRANGE
        money = Money(10, Currency.EUR)
        expected = Money(20, Currency.EUR)

        # ACT
        result = 2 * money

        # ASSERT
        assert result == expected

    def test_divide_in_korean_won_returns_float(self):
        # ARRANGE
        money = Money(4002, Currency.KRW)
        expected = Money(1000.5, Currency.KRW)

        # ACT
        result = money / 4

        # ASSERT
        assert result == expected

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
        other = Money(other_amount, currency)
        result = monnaie + other
        assert result.amount == expected_amount
        assert result.currency == currency

    def test_times_money(self):
        base_amount = 10
        currency = Currency.EUR
        factor = 3
        expected_amount = 30

        monnaie = Money(base_amount, currency)
        result = monnaie * factor
        assert result.amount == expected_amount
        assert result.currency == currency

    def test_wrong_money(self):
        base_amount = 10
        currency = Currency.EUR
        usd_monnaie = Money(base_amount, Currency.USD)
        eur = Money(base_amount, currency)

        with pytest.raises(ValueError) as error:
            result = eur + usd_monnaie
        assert str(error.value) == "Cannot add money with different currencies"

    def test_negative_money(self):
        base_amount = 10
        currency = Currency.EUR
        eur = Money(base_amount, currency)

        with pytest.raises(ValueError) as error:
            result = eur + (-1)
        assert str(error.value) == "Amount cannot be negative"

    def test_negative_times(self):
        base_amount = 10
        currency = Currency.EUR
        eur = Money(base_amount, currency)

        with pytest.raises(ValueError) as error:
            result = eur * (-1)
        assert str(error.value) == "Factor cannot be negative"

    def test_negative_division(self):
        base_amount = 10
        currency = Currency.EUR
        eur = Money(base_amount, currency)

        with pytest.raises(ValueError) as error:
            result = eur / (-1)
        assert str(error.value) == "Divisor must be positive"