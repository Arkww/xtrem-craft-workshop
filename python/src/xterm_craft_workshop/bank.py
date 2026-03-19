from __future__ import annotations
from typing import Dict
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money


class Bank:
    def __init__(self, pivot_currency: Currency):
        """
        La devise pivot est la devise grâce à laquelle les valeurs des autres devises sont calculées
        """
        self._pivot_currency = pivot_currency
        self._exchange_rates: Dict[Currency, float] = {}

    def add_exchange_rate(self, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange à partir du pivot (User Story 2)
        """
        self._exchange_rates[to_currency] = rate

    def convert(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money (User Story 3)
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        raw_amount = self._calculate_raw_conversion(money, to_currency)
        
        fee = 0.01
        converted_amount = raw_amount * (1 - fee)

        final_amount = round(converted_amount, 2)

        return Money(final_amount, to_currency)

    def _calculate_raw_conversion(self, money: Money, to_currency: Currency) -> float:
        """
        Logique de conversion via le pivot sans commission
        """
        # Cas 1 : de pivot vers autre
        if money.currency == self._pivot_currency:
            if to_currency not in self._exchange_rates:
                raise MissingExchangeRateError(self._pivot_currency, to_currency)
            return money.amount * self._exchange_rates[to_currency]
            
        # Cas 2 : de autre vers pivot
        if to_currency == self._pivot_currency:
            if money.currency not in self._exchange_rates:
                raise MissingExchangeRateError(money.currency, self._pivot_currency)
            return money.amount / self._exchange_rates[money.currency]

        # Cas 3 : entre deux devises non-pivots (via le pivot)
        if money.currency not in self._exchange_rates:
            raise MissingExchangeRateError(money.currency, self._pivot_currency)
        if to_currency not in self._exchange_rates:
            raise MissingExchangeRateError(self._pivot_currency, to_currency)
            
        amount_in_pivot = money.amount / self._exchange_rates[money.currency]
        return amount_in_pivot * self._exchange_rates[to_currency]
