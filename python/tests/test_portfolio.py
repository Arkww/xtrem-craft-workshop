import pytest

from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.portfolio import Portfolio
from xterm_craft_workshop.money import Money


class TestPortfolio:
    def test_evaluate_portfolio_in_euros_returns_value(self):
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add(10, Currency.USD)
        portfolio.add(20, Currency.EUR)
        bank = Bank.create(Currency.USD, Currency.EUR, 0.8)
        expected_amount = 28.0

        # ACT
        result = portfolio.evaluate(bank, Currency.EUR)

        # ASSERT
        assert isinstance(result, float)
        assert result == expected_amount

    def test_evaluate_portfolio_echange(self):
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add(10, Currency.EUR)
        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        expected_amount = 12.0

        # ACT
        result = portfolio.evaluate(bank, Currency.USD)

        # ASSERT
        assert isinstance(result, float)
        assert result == expected_amount

    def test_evaluate_portfolio_echange_0_dollar(self):
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add(10, Currency.EUR)
        bank = Bank.create(Currency.USD, Currency.EUR, 0.9)
        expected_amount = 10.0

        # ACT
        result = portfolio.evaluate(bank, Currency.EUR)

        # ASSERT
        assert isinstance(result, float)
        assert result == expected_amount

    def test_evaluate_portfolio_echange_no_evaluation_no_echange(self):
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add(10, Currency.EUR)
        portfolio.add(10, Currency.USD)
        portfolio.add(10, Currency.KRW)

        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        result = "La banque ne propose pas cet échange : KRW->USD"

        # ACT
        with pytest.raises(MissingExchangeRateError) as error:
            portfolio.evaluate(bank, Currency.USD)

        # ASSERT
        assert str(error.value) == result

    def test_evaluate_precise_value(self):
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add(0.0001, Currency.EUR)

        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        expected_result = 0.00012

        # ACT
        result = portfolio.evaluate(bank, Currency.USD)

        # ASSERT
        assert result == expected_result

    def test_evaluate_portfolio_accumulates_multiple_amounts_same_currency(self):
        portfolio = Portfolio()
        portfolio.add(10, Currency.USD)
        portfolio.add(20, Currency.USD)
        portfolio.add(5, Currency.USD)
        bank = Bank.create(Currency.USD, Currency.EUR, 0.8)

        result = portfolio.evaluate(bank, Currency.EUR)

        assert result == 28.0

    def test_evaluate_portfolio_accumulates_multiple_currencies(self):
        portfolio = Portfolio()
        portfolio.add(10, Currency.USD)
        portfolio.add(20, Currency.EUR)
        portfolio.add(30, Currency.EUR)
        bank = Bank.create(Currency.USD, Currency.EUR, 0.8)

        result = portfolio.evaluate(bank, Currency.EUR)

        assert result == 58.0

    def test_add_money_to_portfolio(self):
        # Test de la nouvelle méthode add_money
        portfolio = Portfolio()
        money1 = Money(10, Currency.USD)
        money2 = Money(20, Currency.EUR)

        portfolio.add_money(money1)
        portfolio.add_money(money2)

        bank = Bank.create(Currency.USD, Currency.EUR, 0.8)
        result = portfolio.evaluate(bank, Currency.EUR)

        assert result == 28.0

    def test_evaluate_money_returns_money_object(self):
        portfolio = Portfolio()
        portfolio.add(10, Currency.USD)
        portfolio.add(20, Currency.EUR)
        bank = Bank.create(Currency.USD, Currency.EUR, 0.8)

        result = portfolio.evaluate_money(bank, Currency.EUR)

        assert isinstance(result, Money)
        assert result.amount == 28.0
        assert result.currency == Currency.EUR