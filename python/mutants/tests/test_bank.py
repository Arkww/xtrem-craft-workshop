import pytest

from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError


class TestBank:
    def test_convert_euro_to_usd_returns_float(self):
        #ARRANGE
        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        expected_result = 12.0
        #ACT
        result = bank.convert_currency(10.0, Currency.EUR, Currency.USD)
        #ASSERT
        assert isinstance(result, float)
        assert result == expected_result

    def test_convert_euro_to_usd_returns_same_value(self):
        #ARRANGE
        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        expected_result = 10.0
        #ACT
        result = bank.convert_currency(10.0, Currency.EUR, Currency.EUR)
        #ASSERT
        assert isinstance(result, float)
        assert result == expected_result

    def test_convert_with_missing_exchange_rate_throws_exception(self):

        #ARRANCE
        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        #ACT
        with pytest.raises(MissingExchangeRateError) as error:
            bank.convert_currency(10.0, Currency.EUR, Currency.KRW)
        #ASSERT
        assert str(error.value) == "La banque ne propose pas cet échange : EUR->KRW"

    def test_convert_with_different_exchange_rate_returns_different_floats(self):

        #ARRANGE
        bank:Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        bank2:Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        #ACT
        bank2.add_echange_rate(Currency.EUR, Currency.USD, 1.3)

        #ASSERT
        assert bank.convert_currency(10, Currency.EUR, Currency.USD) == 12
        assert bank2.convert_currency(10, Currency.EUR, Currency.USD) == 13