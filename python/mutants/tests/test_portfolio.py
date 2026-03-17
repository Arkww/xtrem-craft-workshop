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

    def test_evaluate_precise_value_higher(self):
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add(10.2545648, Currency.EUR)

        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        expected_result = 12.30547776

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

    def test_add_accumulates_amount_for_existing_currency(self):
        portfolio = Portfolio()
        portfolio.add(10, Currency.EUR)
        portfolio.add(15, Currency.EUR)

        bank = Bank.create(Currency.EUR, Currency.USD, 1.0)
        result = portfolio.evaluate(bank, Currency.EUR)

        assert result == 25.0

    def test_evaluate_portfolio_accumulates_multiple_currencies(self):
        portfolio = Portfolio()
        portfolio.add(10, Currency.USD)
        portfolio.add(20, Currency.EUR)
        portfolio.add(30, Currency.EUR)
        bank = Bank.create(Currency.USD, Currency.EUR, 0.8)

        result = portfolio.evaluate(bank, Currency.EUR)

        assert result == 58.0

    def test_evaluate_accumulates_multiple_converted_currencies(self):
        portfolio = Portfolio()
        portfolio.add(10, Currency.USD)
        portfolio.add(100, Currency.KRW)
        bank = Bank.create(Currency.USD, Currency.EUR, 0.8)
        bank.add_exchange_rate(Currency.KRW, Currency.EUR, 0.001)

        result = portfolio.evaluate(bank, Currency.EUR)

        assert result == 8.1

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

    def test_portfolio_with_mixed_addition_methods(self):
        """Test que les deux méthodes d'ajout fonctionnent ensemble"""
        portfolio = Portfolio()
        portfolio.add(10, Currency.USD)
        portfolio.add_money(Money(20, Currency.EUR))
        portfolio.add_money(Money(5, Currency.USD))

        bank = Bank.create(Currency.USD, Currency.EUR, 0.8)

        result = portfolio.evaluate(bank, Currency.EUR)

        # 10 USD + 5 USD = 15 USD = 12 EUR + 20 EUR = 32 EUR
        assert result == 32.0

    def test_portfolio_empty_evaluation(self):
        """Test d'évaluation d'un portefeuille vide"""
        portfolio = Portfolio()
        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)

        result = portfolio.evaluate(bank, Currency.EUR)

        assert result == 0.0

    def test_portfolio_evaluate_money_with_mixed_currencies(self):
        """Test de evaluate_money avec différentes monnaies"""
        portfolio = Portfolio()
        portfolio.add(10, Currency.USD)
        portfolio.add(20, Currency.EUR)
        portfolio.add(1000, Currency.KRW)

        bank = Bank.create(Currency.USD, Currency.EUR, 0.8)
        bank.add_exchange_rate(Currency.KRW, Currency.EUR, 0.00075)

        result = portfolio.evaluate_money(bank, Currency.EUR)

        # 10 USD = 8 EUR + 20 EUR = 28 EUR + 1000 KRW = 0.75 EUR = 28.75 EUR
        assert isinstance(result, Money)
        assert result.currency == Currency.EUR
        assert result.amount == 28.75

    def test_portfolio_accumulate_same_currency_multiple_adds(self):
        """Test que les ajouts multiples dans la même monnaie s'accumulent"""
        portfolio = Portfolio()
        portfolio.add_money(Money(5, Currency.EUR))
        portfolio.add_money(Money(10, Currency.EUR))
        portfolio.add_money(Money(15, Currency.EUR))

        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)

        result = portfolio.evaluate(bank, Currency.EUR)

        assert result == 30.0


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

    def test_evaluate_portfolio_echange_no_evaluation_no_currency(self):
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add(10, Currency.EUR)
        portfolio.add(10, Currency.USD)

        bank = Bank.create(Currency.KRW, Currency.KRW, 1.0)
        result = "La banque ne propose pas cet échange : EUR->USD"

        # ACT
        with pytest.raises(MissingExchangeRateError) as error:
            portfolio.evaluate(bank, Currency.USD)

        # ASSERT
        assert str(error.value) == result

    def test_evaluate_portfolio_echange_no_evaluation_wrong_echange(self):
        # ARRANGE
        portfolio = Portfolio()
        portfolio.add(10, Currency.EUR)
        portfolio.add(10, Currency.USD)
        portfolio.add(10, Currency.KRW)

        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        bank.add_exchange_rate(Currency.EUR, Currency.KRW, 10.0)
        result = "La banque ne propose pas cet échange : USD->EUR"

        # ACT
        with pytest.raises(MissingExchangeRateError) as error:
            portfolio.evaluate(bank, Currency.EUR)

        # ASSERT
        assert str(error.value) == result