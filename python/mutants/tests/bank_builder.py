from typing import Dict
from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency

class BankBuilder:
    def __init__(self):
        self._exchange_rates: Dict[str, float] = {}
        self._pivot_currency = Currency.EUR

    def with_rate(self, to_currency: Currency, rate: float) -> "BankBuilder":
        self._exchange_rates[to_currency] = rate
        return self
    
    def with_pivot_currency(self, pivot_currency: Currency) -> "BankBuilder":
        self._pivot_currency = pivot_currency
        return self     

    def build(self) -> Bank:
        return Bank(self._pivot_currency, self._exchange_rates.copy())
