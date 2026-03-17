
import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.money_calculator import MoneyCalculator
from xterm_craft_workshop.money import Money


class Portfolio:

    def __init__(self):
        self.content = {}
        self.monies = []

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
    
    def evaluate_money(self, bank: Bank, currency: Currency) -> Money:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et renvoie un objet Money
        """
        total_amount = 0.0
        for money in self.monies:
            converted = bank.convert(money, currency)
            total_amount += converted.amount
        return Money(total_amount, currency)

    def add(self, amount: float, currency: Currency) -> None:
        """
        Ajoute une somme d'argent dans une monnaie donnée au portefeuille
        """
        if currency in self.content:
            self.content[currency] += amount
        else:
            self.content[currency] = amount
    
    def add_money(self, money: Money) -> None:
        """
        Ajoute un objet Money au portefeuille
        """
        self.monies.append(money)