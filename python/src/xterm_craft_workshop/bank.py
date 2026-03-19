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
        assert to_currency != self._pivot_currency, "Le from_currency doit être différent du pivot_currency"
        exchange_rate_key = f'{self._pivot_currency.value}->{to_currency.value}'
        assert exchange_rate_key not in self._exchange_rate, "Le taux d'échange existe déjà"
        self._exchange_rate[exchange_rate_key] = rate

    def remove_exchange_rate(self, to_currency: Currency) -> None:
        """
        Supprimer un taux d'échange (méthode métier)
        """
        del self._exchange_rate[f'{self._pivot_currency.value}->{to_currency.value}']

    def convert(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        key = f'{money.currency.value}->{to_currency.value}'
        if key not in self._exchange_rate:
            raise MissingExchangeRateError(money.currency, to_currency)

        converted_amount = money.amount * self._exchange_rate[key]

        return Money(converted_amount, to_currency)
