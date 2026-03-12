
import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.money_calculator import MoneyCalculator
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


class Portfolio:

    def __init__(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPortfolioǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁPortfolioǁ__init____mutmut_mutants'), args, kwargs, self)

    def xǁPortfolioǁ__init____mutmut_orig(self):
        self.content = {}

    def xǁPortfolioǁ__init____mutmut_1(self):
        self.content = None
    
    xǁPortfolioǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPortfolioǁ__init____mutmut_1': xǁPortfolioǁ__init____mutmut_1
    }
    xǁPortfolioǁ__init____mutmut_orig.__name__ = 'xǁPortfolioǁ__init__'

    def evaluate(self, bank: Bank, currency: Currency) -> float:
        args = [bank, currency]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPortfolioǁevaluate__mutmut_orig'), object.__getattribute__(self, 'xǁPortfolioǁevaluate__mutmut_mutants'), args, kwargs, self)

    def xǁPortfolioǁevaluate__mutmut_orig(self, bank: Bank, currency: Currency) -> float:
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

    def xǁPortfolioǁevaluate__mutmut_1(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre
        """
        total = None
        for curr, amount in self.content.items():
            if curr != currency:
                total += bank.convert_currency(amount, curr, currency)
            else:
                total += amount
        return total

    def xǁPortfolioǁevaluate__mutmut_2(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre
        """
        total = 1.0
        for curr, amount in self.content.items():
            if curr != currency:
                total += bank.convert_currency(amount, curr, currency)
            else:
                total += amount
        return total

    def xǁPortfolioǁevaluate__mutmut_3(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre
        """
        total = 0.0
        for curr, amount in self.content.items():
            if curr == currency:
                total += bank.convert_currency(amount, curr, currency)
            else:
                total += amount
        return total

    def xǁPortfolioǁevaluate__mutmut_4(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre
        """
        total = 0.0
        for curr, amount in self.content.items():
            if curr != currency:
                total = bank.convert_currency(amount, curr, currency)
            else:
                total += amount
        return total

    def xǁPortfolioǁevaluate__mutmut_5(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre
        """
        total = 0.0
        for curr, amount in self.content.items():
            if curr != currency:
                total -= bank.convert_currency(amount, curr, currency)
            else:
                total += amount
        return total

    def xǁPortfolioǁevaluate__mutmut_6(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre
        """
        total = 0.0
        for curr, amount in self.content.items():
            if curr != currency:
                total += bank.convert_currency(None, curr, currency)
            else:
                total += amount
        return total

    def xǁPortfolioǁevaluate__mutmut_7(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre
        """
        total = 0.0
        for curr, amount in self.content.items():
            if curr != currency:
                total += bank.convert_currency(amount, None, currency)
            else:
                total += amount
        return total

    def xǁPortfolioǁevaluate__mutmut_8(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre
        """
        total = 0.0
        for curr, amount in self.content.items():
            if curr != currency:
                total += bank.convert_currency(amount, curr, None)
            else:
                total += amount
        return total

    def xǁPortfolioǁevaluate__mutmut_9(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre
        """
        total = 0.0
        for curr, amount in self.content.items():
            if curr != currency:
                total += bank.convert_currency(curr, currency)
            else:
                total += amount
        return total

    def xǁPortfolioǁevaluate__mutmut_10(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre
        """
        total = 0.0
        for curr, amount in self.content.items():
            if curr != currency:
                total += bank.convert_currency(amount, currency)
            else:
                total += amount
        return total

    def xǁPortfolioǁevaluate__mutmut_11(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre
        """
        total = 0.0
        for curr, amount in self.content.items():
            if curr != currency:
                total += bank.convert_currency(amount, curr, )
            else:
                total += amount
        return total

    def xǁPortfolioǁevaluate__mutmut_12(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre
        """
        total = 0.0
        for curr, amount in self.content.items():
            if curr != currency:
                total += bank.convert_currency(amount, curr, currency)
            else:
                total = amount
        return total

    def xǁPortfolioǁevaluate__mutmut_13(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre
        """
        total = 0.0
        for curr, amount in self.content.items():
            if curr != currency:
                total += bank.convert_currency(amount, curr, currency)
            else:
                total -= amount
        return total
    
    xǁPortfolioǁevaluate__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPortfolioǁevaluate__mutmut_1': xǁPortfolioǁevaluate__mutmut_1, 
        'xǁPortfolioǁevaluate__mutmut_2': xǁPortfolioǁevaluate__mutmut_2, 
        'xǁPortfolioǁevaluate__mutmut_3': xǁPortfolioǁevaluate__mutmut_3, 
        'xǁPortfolioǁevaluate__mutmut_4': xǁPortfolioǁevaluate__mutmut_4, 
        'xǁPortfolioǁevaluate__mutmut_5': xǁPortfolioǁevaluate__mutmut_5, 
        'xǁPortfolioǁevaluate__mutmut_6': xǁPortfolioǁevaluate__mutmut_6, 
        'xǁPortfolioǁevaluate__mutmut_7': xǁPortfolioǁevaluate__mutmut_7, 
        'xǁPortfolioǁevaluate__mutmut_8': xǁPortfolioǁevaluate__mutmut_8, 
        'xǁPortfolioǁevaluate__mutmut_9': xǁPortfolioǁevaluate__mutmut_9, 
        'xǁPortfolioǁevaluate__mutmut_10': xǁPortfolioǁevaluate__mutmut_10, 
        'xǁPortfolioǁevaluate__mutmut_11': xǁPortfolioǁevaluate__mutmut_11, 
        'xǁPortfolioǁevaluate__mutmut_12': xǁPortfolioǁevaluate__mutmut_12, 
        'xǁPortfolioǁevaluate__mutmut_13': xǁPortfolioǁevaluate__mutmut_13
    }
    xǁPortfolioǁevaluate__mutmut_orig.__name__ = 'xǁPortfolioǁevaluate'

    def add(self, amount: float, currency: Currency) -> None:
        args = [amount, currency]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPortfolioǁadd__mutmut_orig'), object.__getattribute__(self, 'xǁPortfolioǁadd__mutmut_mutants'), args, kwargs, self)

    def xǁPortfolioǁadd__mutmut_orig(self, amount: float, currency: Currency) -> None:
        """
        Ajoute une somme d'argent dans une monnaie donnée au portefeuille
        """
        if currency in self.content:
            self.content[currency] += amount
        else:
            self.content[currency] = amount

    def xǁPortfolioǁadd__mutmut_1(self, amount: float, currency: Currency) -> None:
        """
        Ajoute une somme d'argent dans une monnaie donnée au portefeuille
        """
        if currency not in self.content:
            self.content[currency] += amount
        else:
            self.content[currency] = amount

    def xǁPortfolioǁadd__mutmut_2(self, amount: float, currency: Currency) -> None:
        """
        Ajoute une somme d'argent dans une monnaie donnée au portefeuille
        """
        if currency in self.content:
            self.content[currency] = amount
        else:
            self.content[currency] = amount

    def xǁPortfolioǁadd__mutmut_3(self, amount: float, currency: Currency) -> None:
        """
        Ajoute une somme d'argent dans une monnaie donnée au portefeuille
        """
        if currency in self.content:
            self.content[currency] -= amount
        else:
            self.content[currency] = amount

    def xǁPortfolioǁadd__mutmut_4(self, amount: float, currency: Currency) -> None:
        """
        Ajoute une somme d'argent dans une monnaie donnée au portefeuille
        """
        if currency in self.content:
            self.content[currency] += amount
        else:
            self.content[currency] = None
    
    xǁPortfolioǁadd__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPortfolioǁadd__mutmut_1': xǁPortfolioǁadd__mutmut_1, 
        'xǁPortfolioǁadd__mutmut_2': xǁPortfolioǁadd__mutmut_2, 
        'xǁPortfolioǁadd__mutmut_3': xǁPortfolioǁadd__mutmut_3, 
        'xǁPortfolioǁadd__mutmut_4': xǁPortfolioǁadd__mutmut_4
    }
    xǁPortfolioǁadd__mutmut_orig.__name__ = 'xǁPortfolioǁadd'