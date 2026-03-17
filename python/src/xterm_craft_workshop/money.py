from __future__ import annotations
from .currency import Currency
from typing import Union


class Money:
    def __init__(self, amount: float, currency: Currency):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.amount = amount
        self.currency = currency

    def __add__(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour additionner deux Money ou un Money avec un nombre
        """
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError("Amount cannot be negative")
            return Money(self.amount + other, self.currency)
        elif isinstance(other, Money):
            if other.amount < 0:
                raise ValueError("Amount cannot be negative")
            if other.currency != self.currency:
                raise ValueError("Cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def __radd__(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour l'addition à droite
        """
        return self.__add__(other)

    def __mul__(self, factor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur * pour multiplier un Money par un facteur
        """
        if isinstance(factor, (int, float)):
            if factor < 0:
                raise ValueError("Factor cannot be negative")
            return Money(self.amount * factor, self.currency)
        return NotImplemented

    def __rmul__(self, factor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur * pour la multiplication à droite
        """
        return self.__mul__(factor)

    def __truediv__(self, divisor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur / pour diviser un Money par un diviseur
        """
        if isinstance(divisor, (int, float)):
            if divisor <= 0:
                raise ValueError("Divisor must be positive")
            return Money(self.amount / divisor, self.currency)
        return NotImplemented

    def __eq__(self, other: object) -> bool:
        """
        Surcharge de l'opérateur == pour comparer deux Money
        """
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency

    def __str__(self) -> str:
        return f"{self.amount} {self.currency.value}"

    def __repr__(self) -> str:
        return f"Money({self.amount}, {self.currency})"