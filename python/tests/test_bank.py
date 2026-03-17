import pytest

from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money


class TestBank:
    def test_convert_euro_to_usd_returns_float(self):
        # ARRANGE
        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        expected_result = 12.0

        # ACT
        result = bank.convert_currency(10.0, Currency.EUR, Currency.USD)

        # ASSERT
        assert isinstance(result, float)
        assert result == expected_result

    def test_convert_money_euro_to_usd(self):
        # ARRANGE
        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        money = Money(10.0, Currency.EUR)
        expected = Money(12.0, Currency.USD)

        # ACT
        result = bank.convert(money, Currency.USD)

        # ASSERT
        assert isinstance(result, Money)
        assert result == expected

    def test_convert_euro_to_usd_returns_same_value(self):
        # ARRANGE
        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        expected_result = 10.0

        # ACT
        result = bank.convert_currency(10.0, Currency.EUR, Currency.EUR)

        # ASSERT
        assert isinstance(result, float)
        assert result == expected_result

    def test_convert_same_currency_money(self):
        """Test de conversion avec la même monnaie"""
        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        money = Money(10, Currency.EUR)

        result = bank.convert(money, Currency.EUR)

        assert result == money  # Devrait retourner le même objet (ou équivalent)

    def test_convert_with_different_exchange_rate_returns_different_floats(self):
        # ARRANGE
        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        bank2 = Bank.create(Currency.EUR, Currency.USD, 1.2)

        # ACT
        bank2.add_exchange_rate(Currency.EUR, Currency.USD, 1.3)

        # ASSERT
        assert bank.convert_currency(10, Currency.EUR, Currency.USD) == 12
        assert bank2.convert_currency(10, Currency.EUR, Currency.USD) == 13

    def test_add_multiple_exchange_rates(self):
        """Test d'ajout de plusieurs taux d'échange"""
        bank = Bank()
        bank.add_exchange_rate(Currency.EUR, Currency.USD, 1.2)
        bank.add_exchange_rate(Currency.USD, Currency.EUR, 0.8)
        bank.add_exchange_rate(Currency.EUR, Currency.KRW, 1300.0)

        assert bank.convert_currency(10, Currency.EUR, Currency.USD) == 12.0
        assert bank.convert_currency(10, Currency.USD, Currency.EUR) == 8.0
        assert bank.convert_currency(10, Currency.EUR, Currency.KRW) == 13000.0

    def test_convert_currency_precision(self):
        """Test de précision dans les conversions"""
        bank = Bank.create(Currency.EUR, Currency.USD, 1.23456789)

        result = bank.convert_currency(10.12345678, Currency.EUR, Currency.USD)

        expected = 10.12345678 * 1.23456789
        assert abs(result - expected) < 1e-10

    def test_bank_create_without_rate(self):
        """Test de création de banque sans taux initial"""
        bank = Bank()

        assert bank._exchange_rate == {}


    def test_convert_with_missing_exchange_rate_throws_exception(self):
        # ARRANGE
        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)

        # ACT
        with pytest.raises(MissingExchangeRateError) as error:
            bank.convert_currency(10.0, Currency.EUR, Currency.KRW)

        # ASSERT
        assert str(error.value) == "La banque ne propose pas cet échange : EUR->KRW"

    def test_convert_money_with_missing_rate(self):
        """Test que convert lance l'exception appropriée"""
        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        money = Money(10, Currency.EUR)

        with pytest.raises(MissingExchangeRateError) as error:
            bank.convert(money, Currency.KRW)

        assert str(error.value) == "La banque ne propose pas cet échange : EUR->KRW"

    def test_convert_with_missing_rate_from_bank_without_rates(self):
        """Test de conversion avec une banque sans aucun taux"""
        bank = Bank()

        with pytest.raises(MissingExchangeRateError) as error:
            bank.convert_currency(10.0, Currency.EUR, Currency.USD)

        assert str(error.value) == "La banque ne propose pas cet échange : EUR->USD"

    def test_missing_exchange_rate_error_message(self):
        error = MissingExchangeRateError(Currency.EUR, Currency.KRW)
        assert str(error) == "La banque ne propose pas cet échange : EUR->KRW"