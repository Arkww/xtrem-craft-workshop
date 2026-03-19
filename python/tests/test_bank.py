import pytest

from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money
from tests.bank_builder import BankBuilder


class TestBank:
    def test_create_bank_with_exchange_rate(self):
        # ARRANGE
        bank = BankBuilder().with_pivot_currency(Currency.EUR).with_rate(Currency.USD, 1.2).build()
        money = Money(10.0, Currency.EUR)
        
        # ACT
        result = bank.convert(money, Currency.USD)
        
        # ASSERT
        assert result == Money(12.0, Currency.USD)

    def test_convert_same_currency(self):
        # ARRANGE
        bank = BankBuilder().with_pivot_currency(Currency.EUR).with_rate(Currency.USD, 1.2).build()
        money = Money(10.0, Currency.EUR)
        
        # ACT
        result = bank.convert(money, Currency.EUR)
        
        # ASSERT
        assert result == Money(10.0, Currency.EUR)

    def test_convert_with_different_rate(self):
        # ARRANGE
        bank1 = BankBuilder().with_pivot_currency(Currency.EUR).with_rate(Currency.USD, 1.2).build()
        bank2 = BankBuilder().with_pivot_currency(Currency.EUR).with_rate(Currency.USD, 1.3).build()
        money = Money(10.0, Currency.EUR)
        
        # ACT
        result1 = bank1.convert(money, Currency.USD)
        result2 = bank2.convert(money, Currency.USD)
        
        # ASSERT
        assert result1 == Money(12.0, Currency.USD)
        assert result2 == Money(13.0, Currency.USD)

    def test_add_exchange_rate(self):
        # ARRANGE
        bank = BankBuilder().with_pivot_currency(Currency.EUR).build()
        money = Money(10.0, Currency.EUR)
        
        # ACT
        bank.add_exchange_rate(Currency.USD, 1.2)
        result = bank.convert(money, Currency.USD)
        
        # ASSERT
        assert result == Money(12.0, Currency.USD)

    def test_add_multiple_exchange_rates(self):
        # ARRANGE
        bank = BankBuilder().with_pivot_currency(Currency.EUR).build()
        eur_money = Money(10.0, Currency.EUR)
        
        # ACT
        bank.add_exchange_rate(Currency.USD, 1.2)
        bank.add_exchange_rate(Currency.KRW, 1000.0)
        result1 = bank.convert(eur_money, Currency.USD)
        result2 = bank.convert(eur_money, Currency.KRW)
        
        # ASSERT
        assert result1 == Money(12.0, Currency.USD)
        assert result2 == Money(10_000.0, Currency.KRW)

    def test_convert_with_missing_rate_raises(self):
        # ARRANGE
        bank = BankBuilder().with_pivot_currency(Currency.EUR).with_rate(Currency.USD, 1.2).build()
        money = Money(10.0, Currency.EUR)
        
        # ACT & ASSERT
        with pytest.raises(MissingExchangeRateError) as exc:
            bank.convert(money, Currency.KRW)
        assert str(exc.value) == "La banque ne propose pas cet échange : EUR->KRW"

    def test_convert_from_bank_without_rates_raises(self):
        # ARRANGE
        bank = BankBuilder().with_pivot_currency(Currency.EUR).build()
        money = Money(10.0, Currency.EUR)
        
        # ACT & ASSERT
        with pytest.raises(MissingExchangeRateError) as exc:
            bank.convert(money, Currency.USD)
        assert str(exc.value) == "La banque ne propose pas cet échange : EUR->USD"

    def test_missing_exchange_rate_error_message(self):
        # ARRANGE & ACT
        error = MissingExchangeRateError(Currency.EUR, Currency.KRW)
        
        # ASSERT
        assert str(error) == "La banque ne propose pas cet échange : EUR->KRW"

    def test_convert_with_precision(self):
        # ARRANGE
        bank = BankBuilder().with_pivot_currency(Currency.EUR).with_rate(Currency.USD, 1.23456789).build()
        money = Money(10.12345678, Currency.EUR)
        
        # ACT
        result = bank.convert(money, Currency.USD)
        
        # ASSERT
        expected = 10.12345678 * 1.23456789
        assert abs(result.amount - expected) < 1e-2
        assert result.currency == Currency.USD
