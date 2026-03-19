from __future__ import annotations
from typing import Dict
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money


class Bank:
    def __init__(self, pivot_currency: Currency, exchange_rate: Dict[str, float] = {}):
        self._exchange_rate = exchange_rate
        assert pivot_currency is not None, "Le pivot currency ne peut pas être None"
        self._pivot_currency = pivot_currency

    def add_exchange_rate(self, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange (méthode métier)
        """
        assert rate > 0, "Le taux d'échange doit être positif"
        assert to_currency != self._pivot_currency, "Le to_currency doit être différent du pivot_currency"
        assert to_currency not in self._exchange_rate.keys(), "Le taux d'échange existe déjà"
        self._exchange_rate[to_currency] = rate

    def remove_exchange_rate(self, to_currency: Currency) -> None:
        """
        Supprimer un taux d'échange (méthode métier)
        """
        del self._exchange_rate[to_currency]

    def convert(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)
