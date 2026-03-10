from typing import Dict
from .currency import Currency
from .missing_exchange_rate_error import MissingExchangeRateError


class Bank:
    _exchange_rate: Dict[str, float] = {}
    """Dictionnaire de taux d'échanges donnant la valeur de chaque monnaie"""

    def __init__(self, exchange_rate = {}) -> None:
        self._exchange_rate = exchange_rate

    @staticmethod
    def create(from_currency: Currency, to_currency: Currency, rate: float) -> "Bank":
        """
        Créer une banque
        """
        bank = Bank({})
        bank.add_echange_rate(from_currency, to_currency, rate)

        return bank
    
    def add_echange_rate(self, from_currency: Currency, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange
        """
        self._exchange_rate[f'{from_currency.value}->{to_currency.value}'] = rate

    def convert_currency(self, amount: float, from_currency: Currency, to_currency: Currency) -> float:
        """
        Convertir d'une monnaie à une autre
        Si la banque ne propose pas la convertion donné en paramètre, renvoie une erreur MissingExchangeRateError
        """
        if not (from_currency.value == to_currency.value or f'{from_currency.value}->{to_currency.value}' in self._exchange_rate):
            raise MissingExchangeRateError(from_currency, to_currency)
        if from_currency.value == to_currency.value:
            return amount
        return amount * self._exchange_rate[f'{from_currency.value}->{to_currency.value}']