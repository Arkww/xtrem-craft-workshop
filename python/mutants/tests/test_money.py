import pytest

from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.money import Money


class TestMoney:
    def test_create_money(self):
        money = Money(10, Currency.EUR)
        assert money.amount == 10
        assert money.currency == Currency.EUR

    def test_create_money_negative_amount_raises(self):
        with pytest.raises(ValueError) as exc:
            Money(-10, Currency.EUR)
        assert str(exc.value) == "Amount cannot be negative"

    def test_add_money_same_currency(self):
        money1 = Money(10, Currency.EUR)
        money2 = Money(5, Currency.EUR)
        result = money1 + money2
        assert result == Money(15, Currency.EUR)

    def test_add_money_different_currencies_raises(self):
        eur = Money(10, Currency.EUR)
        usd = Money(5, Currency.USD)
        with pytest.raises(ValueError) as exc:
            eur + usd
        assert str(exc.value) == "Cannot add money with different currencies"

    def test_add_number(self):
        money = Money(10, Currency.EUR)
        result = money + 5
        assert result == Money(15, Currency.EUR)

    def test_add_negative_number_raises(self):
        money = Money(10, Currency.EUR)
        with pytest.raises(ValueError) as exc:
            money + (-5)
        assert str(exc.value) == "Amount cannot be negative"

    def test_add_float(self):
        money = Money(10, Currency.EUR)
        result = money + 5.5
        assert result == Money(15.5, Currency.EUR)

    def test_radd_number(self):
        money = Money(10, Currency.EUR)
        result = 5 + money
        assert result == Money(15, Currency.EUR)

    def test_add_unsupported_type_returns_not_implemented(self):
        money = Money(10, Currency.EUR)
        assert money.__add__("10") is NotImplemented
        assert money.__add__([1, 2]) is NotImplemented
        assert money.__add__({"a": 1}) is NotImplemented
        assert money.__add__(None) is NotImplemented

    def test_mul_by_factor(self):
        money = Money(10, Currency.EUR)
        result = money * 3
        assert result == Money(30, Currency.EUR)

    def test_mul_by_negative_factor_raises(self):
        money = Money(10, Currency.EUR)
        with pytest.raises(ValueError) as exc:
            money * (-2)
        assert str(exc.value) == "Factor cannot be negative"

    def test_mul_by_float(self):
        money = Money(10, Currency.EUR)
        result = money * 2.5
        assert result == Money(25, Currency.EUR)

    def test_rmul_factor(self):
        money = Money(10, Currency.EUR)
        result = 3 * money
        assert result == Money(30, Currency.EUR)

    def test_mul_unsupported_type_returns_not_implemented(self):
        money = Money(10, Currency.EUR)
        assert money.__mul__("3") is NotImplemented

    def test_truediv_by_divisor(self):
        money = Money(10, Currency.EUR)
        result = money / 2
        assert result == Money(5, Currency.EUR)

    def test_truediv_by_float(self):
        money = Money(10, Currency.EUR)
        result = money / 2.5
        assert result == Money(4, Currency.EUR)

    def test_truediv_by_zero_raises(self):
        money = Money(10, Currency.EUR)
        with pytest.raises(ValueError) as exc:
            money / 0
        assert str(exc.value) == "Divisor must be positive"

    def test_truediv_by_negative_raises(self):
        money = Money(10, Currency.EUR)
        with pytest.raises(ValueError) as exc:
            money / (-2)
        assert str(exc.value) == "Divisor must be positive"

    def test_truediv_unsupported_type_returns_not_implemented(self):
        money = Money(10, Currency.EUR)
        assert money.__truediv__("2") is NotImplemented

    def test_equality_same(self):
        money1 = Money(10, Currency.EUR)
        money2 = Money(10, Currency.EUR)
        assert money1 == money2

    def test_equality_different_amount(self):
        money1 = Money(10, Currency.EUR)
        money2 = Money(20, Currency.EUR)
        assert money1 != money2

    def test_equality_different_currency(self):
        money1 = Money(10, Currency.EUR)
        money2 = Money(10, Currency.USD)
        assert money1 != money2

    def test_equality_with_non_money(self):
        money = Money(10, Currency.EUR)
        assert money != 10
        assert money != "10 EUR"

    def test_str_representation(self):
        money = Money(10.5, Currency.EUR)
        assert str(money) == "10.5 EUR"

    def test_repr_representation(self):
        money = Money(10.5, Currency.EUR)
        assert repr(money) == "Money(10.5, Currency.EUR)"