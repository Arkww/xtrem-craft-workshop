import pytest

from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money
from tests.bank_builder import BankBuilder


class TestBank:
    def test_create_bank_with_exchange_rate(self):
        # Example: Given a bank with EUR as Pivot, When I convert 10 EUR to USD with rate 1.2, Then I receive 11.88 USD (1% fee)
        # ARRANGE
        bank = BankBuilder().with_rate(Currency.USD, 1.2).build()
        money = Money(10.0, Currency.EUR)
        
        # ACT
        result = bank.convert(money, Currency.USD)
        
        # ASSERT
        assert result == Money(11.88, Currency.USD)

    def test_convert_same_currency(self):
        # Example: Same currency conversion should have no fee and no rate change
        # ARRANGE
        bank = BankBuilder().with_rate(Currency.USD, 1.2).build()
        money = Money(10.0, Currency.EUR)
        
        # ACT
        result = bank.convert(money, Currency.EUR)
        
        # ASSERT
        assert result == Money(10.0, Currency.EUR)

    def test_convert_with_different_rate(self):
        # ARRANGE
        bank1 = BankBuilder().with_rate(Currency.USD, 1.2).build()
        bank2 = BankBuilder().with_rate(Currency.USD, 1.3).build()
        money = Money(10.0, Currency.EUR)
        
        # ACT
        result1 = bank1.convert(money, Currency.USD)
        result2 = bank2.convert(money, Currency.USD)
        
        # ASSERT
        assert result1 == Money(11.88, Currency.USD)
        assert result2 == Money(12.87, Currency.USD)

    def test_add_exchange_rate(self):
        # ARRANGE
        bank = BankBuilder().build()
        money = Money(10.0, Currency.EUR)
        
        # ACT
        bank.add_exchange_rate(Currency.USD, 1.2)
        result = bank.convert(money, Currency.USD)
        
        # ASSERT
        assert result == Money(11.88, Currency.USD)

    def test_add_multiple_exchange_rates(self):
        # ARRANGE
        bank = BankBuilder().build()
        eur_money = Money(10.0, Currency.EUR)
        
        # ACT
        bank.add_exchange_rate(Currency.USD, 1.2)
        bank.add_exchange_rate(Currency.KRW, 1344.0)
        
        result1 = bank.convert(eur_money, Currency.USD)
        result2 = bank.convert(eur_money, Currency.KRW)
        
        # ASSERT
        assert result1 == Money(11.88, Currency.USD)
        assert result2 == Money(13305.6, Currency.KRW)

    def test_convert_with_missing_rate_raises(self):
        # Example Mapping: Erreur en cas de devise inconnue
        # Given a bank with Euro as Pivot Currency, When I convert 10 Euros to Korean Wons, Then I receive an error
        # ARRANGE
        bank = BankBuilder().with_rate(Currency.USD, 1.2).build()
        money = Money(10.0, Currency.EUR)
        
        # ACT & ASSERT
        with pytest.raises(MissingExchangeRateError):
            bank.convert(money, Currency.KRW)

    def test_convert_from_bank_without_rates_raises(self):
        # ARRANGE
        bank = BankBuilder().build()
        money = Money(10.0, Currency.EUR)
        
        # ACT & ASSERT
        with pytest.raises(MissingExchangeRateError):
            bank.convert(money, Currency.USD)

    def test_convert_with_precision(self):
        # ARRANGE
        bank = BankBuilder().with_rate(Currency.USD, 1.23456789).build()
        money = Money(10.12345678, Currency.EUR)
        
        # ACT
        result = bank.convert(money, Currency.USD)
        
        # ASSERT
        expected = round((10.12345678 * 1.23456789) * 0.99, 2)
        assert result == Money(expected, Currency.USD)
