from typing import Dict
from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency

class BankBuilder:
    def __init__(self):
        self._pivot_currency: Currency = Currency.EUR
        self._exchange_rates: Dict[Currency, float] = {}

    def with_pivot_currency(self, currency: Currency) -> "BankBuilder":
        self._pivot_currency = currency
        return self

    def with_rate(self, to_currency: Currency, rate: float) -> "BankBuilder":
        self._exchange_rates[to_currency] = rate
        return self

    def build(self) -> Bank:
        bank = Bank(self._pivot_currency)
        for currency, rate in self._exchange_rates.items():
            bank.add_exchange_rate(currency, rate)
        return bank
