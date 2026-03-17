from __future__ import annotations
from typing import Dict
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money


class Bank:
    def __init__(self, exchange_rate: Dict[str, float] = None):
        self._exchange_rate = exchange_rate if exchange_rate is not None else {}

    @staticmethod
    def create(from_currency: Currency, to_currency: Currency, rate: float) -> "Bank":
        """
        Créer une banque avec un taux d'échange initial
        """
        bank = Bank()
        bank.add_exchange_rate(from_currency, to_currency, rate)
        return bank

    def add_exchange_rate(self, from_currency: Currency, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange
        """
        self._exchange_rate[f'{from_currency.value}->{to_currency.value}'] = rate

    def convert_currency(self, amount: float, from_currency: Currency, to_currency: Currency) -> float:
        """
        Convertir un montant d'une monnaie à une autre
        """
        if from_currency == to_currency:
            return amount

        key = f'{from_currency.value}->{to_currency.value}'
        if key not in self._exchange_rate:
            raise MissingExchangeRateError(from_currency, to_currency)

        return amount * self._exchange_rate[key]

    def convert(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)

        converted_amount = self.convert_currency(money.amount, money.currency, to_currency)
        return Money(converted_amount, to_currency)