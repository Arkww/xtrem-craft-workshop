import pytest

from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.portfolio import Portfolio
from xterm_craft_workshop.money import Money
from tests.bank_builder import BankBuilder


class TestPortfolio:
    def test_create_empty_portfolio(self):
        # ARRANGE
        portfolio = Portfolio()
        bank = BankBuilder().build()
        
        # ACT
        result = portfolio.evaluate_money(bank, Currency.EUR)
        
        # ASSERT
        assert result == Money(0.0, Currency.EUR)

    def test_add_money_to_portfolio(self):
        # ARRANGE
        portfolio = Portfolio()
        money = Money(10.0, Currency.EUR)
        
        # ACT
        portfolio.add_money(money)
        
        # ASSERT
        assert len(portfolio.monies) == 1
        assert portfolio.monies[0] == money

    def test_evaluate_single_currency_no_conversion(self):
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add_money(Money(10.0, Currency.EUR))
        bank = BankBuilder().build()
        
        # ACT
        result = portfolio.evaluate_money(bank, Currency.EUR)
        
        # ASSERT
        assert result == Money(10.0, Currency.EUR)

    def test_evaluate_single_currency_with_conversion(self):
        # Example: 10 EUR -> USD (rate 1.2) = 11.88 USD
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add_money(Money(10.0, Currency.EUR))
        bank = BankBuilder().with_rate(Currency.USD, 1.2).build()
        
        # ACT
        result = portfolio.evaluate_money(bank, Currency.USD)
        
        # ASSERT
        assert result == Money(11.88, Currency.USD)

    def test_evaluate_multiple_same_currency(self):
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add_money(Money(10.0, Currency.EUR))
        portfolio.add_money(Money(20.0, Currency.EUR))
        portfolio.add_money(Money(5.0, Currency.EUR))
        bank = BankBuilder().build()
        
        # ACT
        result = portfolio.evaluate_money(bank, Currency.EUR)
        
        # ASSERT
        assert result == Money(35.0, Currency.EUR)

    def test_evaluate_multiple_different_currencies(self):
        # Example: 10 USD -> EUR (rate 1.2) = 10 / 1.2 * 0.99 = 8.25 EUR
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add_money(Money(10.0, Currency.USD))
        portfolio.add_money(Money(20.0, Currency.EUR))
        bank = BankBuilder().with_rate(Currency.USD, 1.2).build()
        
        # ACT
        result = portfolio.evaluate_money(bank, Currency.EUR)
        
        # ASSERT
        assert result == Money(28.25, Currency.EUR)

    def test_evaluate_multiple_currencies_multiple_conversions(self):
        # 10 USD -> EUR = 10 / 1.2 * 0.99 = 8.25
        # 1000 KRW -> EUR = 1000 / 1344 * 0.99 = 0.73660714
        # Total = 8.25 + 20.0 + 0.73660714 = 28.98660714 -> rounded to 28.99 (because of the Bank internal rounding)
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add_money(Money(10.0, Currency.USD))
        portfolio.add_money(Money(20.0, Currency.EUR))
        portfolio.add_money(Money(1000.0, Currency.KRW))
        
        bank = BankBuilder()\
            .with_rate(Currency.USD, 1.2)\
            .with_rate(Currency.KRW, 1344.0)\
            .build()
        
        # ACT
        result = portfolio.evaluate_money(bank, Currency.EUR)
        
        # ASSERT
        # 8.25 + 20.0 + 0.74 (1000/1344 * 0.99 = 0.7366... rounded to 0.74 by bank)
        assert result == Money(28.99, Currency.EUR)

    def test_evaluate_with_missing_rate_raises(self):
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add_money(Money(10.0, Currency.EUR))
        portfolio.add_money(Money(10.0, Currency.KRW))
        bank = BankBuilder().with_rate(Currency.USD, 1.2).build()
        
        # ACT & ASSERT
        with pytest.raises(MissingExchangeRateError):
            portfolio.evaluate_money(bank, Currency.USD)

    def test_evaluate_with_some_missing_rates_raises(self):
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add_money(Money(10.0, Currency.EUR))
        portfolio.add_money(Money(10.0, Currency.USD))
        portfolio.add_money(Money(10.0, Currency.KRW))
        
        bank = BankBuilder().with_rate(Currency.USD, 1.2).build()
        # On ne définit pas KRW
        
        # ACT & ASSERT
        with pytest.raises(MissingExchangeRateError):
            portfolio.evaluate_money(bank, Currency.EUR)
