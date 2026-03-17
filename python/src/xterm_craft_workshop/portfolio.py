from __future__ import annotations
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import List
from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.money import Money


class Portfolio:
    def __init__(self):
        self.monies: List[Money] = []

    def evaluate_money(self, bank: Bank, currency: Currency) -> Money:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et renvoie un objet Money
        """
        total = Money(0.0, currency)
        for money in self.monies:
            converted = bank.convert(money, currency)
            total = total + converted
        return total

    def add_money(self, money: Money) -> None:
        """
        Ajoute un objet Money au portefeuille
        """
        self.monies.append(money)