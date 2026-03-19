from __future__ import annotations
from typing import Dict
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money


class Bank:
    def __init__(self, exchange_rate: Dict[str, float] = None):
        self._exchange_rate = exchange_rate if exchange_rate is not None else {}

    def add_exchange_rate(self, from_currency: Currency, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange (méthode métier)
        """
        self._exchange_rate[f'{from_currency.value}->{to_currency.value}'] = rate

    def remove_exchange_rate(self, from_currency: Currency, to_currency: Currency) -> None:
        """
        Supprimer un taux d'échange (méthode métier)
        """
        del self._exchange_rate[f'{from_currency.value}->{to_currency.value}']

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
