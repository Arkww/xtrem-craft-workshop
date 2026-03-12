
import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.money_calculator import MoneyCalculator


class Portfolio:

    def __init__(self):
        self.content = {}

    def evaluate(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre
        """
        total = 0.0
        for curr, amount in self.content.items():
            if curr != currency:
                total += bank.convert_currency(amount, curr, currency)
            else:
                total += amount
        return total

    def add(self, amount: float, currency: Currency) -> None:
        """
        Ajoute une somme d'argent dans une monnaie donnée au portefeuille
        """
        if currency in self.content:
            self.content[currency] += amount
        else:
            self.content[currency] = amount