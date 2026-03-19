from typing import Dict
from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency

class BankBuilder:
    def __init__(self):
        self._exchange_rates: Dict[str, float] = {}

    def with_rate(self, from_currency: Currency, to_currency: Currency, rate: float) -> "BankBuilder":
        self._exchange_rates[f"{from_currency.value}->{to_currency.value}"] = rate
        return self

    def build(self) -> Bank:
        return Bank(self._exchange_rates.copy())
