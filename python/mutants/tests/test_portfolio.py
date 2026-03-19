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
        bank = BankBuilder().with_pivot_currency(Currency.EUR).build()
        
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
        bank = BankBuilder().with_pivot_currency(Currency.EUR).build()
        
        # ACT
        result = portfolio.evaluate_money(bank, Currency.EUR)
        
        # ASSERT
        assert result == Money(10.0, Currency.EUR)

    def test_evaluate_single_currency_with_conversion(self):
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add_money(Money(10.0, Currency.EUR))
        bank = BankBuilder().with_pivot_currency(Currency.EUR).with_rate(Currency.USD, 1.2).build()
        
        # ACT
        result = portfolio.evaluate_money(bank, Currency.USD)
        
        # ASSERT
        assert result == Money(12.0, Currency.USD)

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
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add_money(Money(10.0, Currency.USD))
        portfolio.add_money(Money(20.0, Currency.EUR))
        bank = BankBuilder().with_pivot_currency(Currency.USD).with_rate(Currency.EUR, 0.8).build()
        
        # ACT
        result = portfolio.evaluate_money(bank, Currency.EUR)
        
        # ASSERT
        assert result == Money(28.0, Currency.EUR)

    def test_evaluate_multiple_currencies_multiple_conversions(self):
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add_money(Money(10.0, Currency.USD))
        portfolio.add_money(Money(20.0, Currency.EUR))
        portfolio.add_money(Money(1000.0, Currency.KRW))
        
        bank = BankBuilder()\
            .with_pivot_currency(Currency.EUR)\
            .with_rate(Currency.USD, 2)\
            .with_rate(Currency.KRW, 1000)\
            .build()
        
        # ACT
        result = portfolio.evaluate_money(bank, Currency.EUR)
        
        # ASSERT
        expected = 20 + 5 + 1
        assert abs(result.amount - expected) < 1e-10
        assert result.currency == Currency.EUR

    def test_evaluate_with_missing_rate_raises(self):
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add_money(Money(10.0, Currency.EUR))
        portfolio.add_money(Money(10.0, Currency.KRW))
        bank = BankBuilder().with_pivot_currency(Currency.EUR).with_rate(Currency.USD, 1.2).build()
        
        # ACT & ASSERT
        with pytest.raises(MissingExchangeRateError) as exc:
            portfolio.evaluate_money(bank, Currency.USD)
        assert str(exc.value) == "La banque ne propose pas cet échange : KRW->EUR"

    def test_evaluate_with_missing_rate_for_specific_conversion_raises(self):
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add_money(Money(10.0, Currency.EUR))
        portfolio.add_money(Money(10.0, Currency.USD))
        
        bank = BankBuilder().with_pivot_currency(Currency.EUR).with_rate(Currency.KRW, 1.0).build()
        
        # ACT & ASSERT
        with pytest.raises(MissingExchangeRateError) as exc:
            portfolio.evaluate_money(bank, Currency.USD)
        assert str(exc.value) == "La banque ne propose pas cet échange : USD->EUR"