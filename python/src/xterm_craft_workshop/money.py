from .currency import Currency


class Money :

    def __init__(self, amount: float, currency: Currency):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.amount = amount
        self.currency = currency

    def add(self, other_amount: float, other_currency: Currency):
        if other_amount < 0:
            raise ValueError("Amount cannot be negative")
        elif other_currency != self.currency:
            raise ValueError("Cannot add money with different currencies")
        else:
            return Money(other_amount + self.amount, other_currency)
    
    def times(self, factor: float):
        if factor < 0:
            raise ValueError("Factor cannot be negative")
        else:
            return Money(self.amount * factor, self.currency)