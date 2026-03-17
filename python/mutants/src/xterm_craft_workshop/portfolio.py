from __future__ import annotations
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import List
from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.money import Money
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
        self.monies: List[Money] = []
    def xǁPortfolioǁ__init____mutmut_1(self):
        self.monies: List[Money] = None
    
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
        Évalue le portefeuille dans la monnaie donnée en paramètre et retourne un float
        """
        total = Money(0.0, currency)
        for money in self.monies:
            converted = bank.convert(money, currency)
            total = total + converted
        return total.amount

    def xǁPortfolioǁevaluate__mutmut_1(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et retourne un float
        """
        total = None
        for money in self.monies:
            converted = bank.convert(money, currency)
            total = total + converted
        return total.amount

    def xǁPortfolioǁevaluate__mutmut_2(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et retourne un float
        """
        total = Money(None, currency)
        for money in self.monies:
            converted = bank.convert(money, currency)
            total = total + converted
        return total.amount

    def xǁPortfolioǁevaluate__mutmut_3(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et retourne un float
        """
        total = Money(0.0, None)
        for money in self.monies:
            converted = bank.convert(money, currency)
            total = total + converted
        return total.amount

    def xǁPortfolioǁevaluate__mutmut_4(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et retourne un float
        """
        total = Money(currency)
        for money in self.monies:
            converted = bank.convert(money, currency)
            total = total + converted
        return total.amount

    def xǁPortfolioǁevaluate__mutmut_5(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et retourne un float
        """
        total = Money(0.0, )
        for money in self.monies:
            converted = bank.convert(money, currency)
            total = total + converted
        return total.amount

    def xǁPortfolioǁevaluate__mutmut_6(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et retourne un float
        """
        total = Money(1.0, currency)
        for money in self.monies:
            converted = bank.convert(money, currency)
            total = total + converted
        return total.amount

    def xǁPortfolioǁevaluate__mutmut_7(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et retourne un float
        """
        total = Money(0.0, currency)
        for money in self.monies:
            converted = None
            total = total + converted
        return total.amount

    def xǁPortfolioǁevaluate__mutmut_8(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et retourne un float
        """
        total = Money(0.0, currency)
        for money in self.monies:
            converted = bank.convert(None, currency)
            total = total + converted
        return total.amount

    def xǁPortfolioǁevaluate__mutmut_9(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et retourne un float
        """
        total = Money(0.0, currency)
        for money in self.monies:
            converted = bank.convert(money, None)
            total = total + converted
        return total.amount

    def xǁPortfolioǁevaluate__mutmut_10(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et retourne un float
        """
        total = Money(0.0, currency)
        for money in self.monies:
            converted = bank.convert(currency)
            total = total + converted
        return total.amount

    def xǁPortfolioǁevaluate__mutmut_11(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et retourne un float
        """
        total = Money(0.0, currency)
        for money in self.monies:
            converted = bank.convert(money, )
            total = total + converted
        return total.amount

    def xǁPortfolioǁevaluate__mutmut_12(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et retourne un float
        """
        total = Money(0.0, currency)
        for money in self.monies:
            converted = bank.convert(money, currency)
            total = None
        return total.amount

    def xǁPortfolioǁevaluate__mutmut_13(self, bank: Bank, currency: Currency) -> float:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et retourne un float
        """
        total = Money(0.0, currency)
        for money in self.monies:
            converted = bank.convert(money, currency)
            total = total - converted
        return total.amount
    
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

    def evaluate_money(self, bank: Bank, currency: Currency) -> Money:
        args = [bank, currency]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPortfolioǁevaluate_money__mutmut_orig'), object.__getattribute__(self, 'xǁPortfolioǁevaluate_money__mutmut_mutants'), args, kwargs, self)

    def xǁPortfolioǁevaluate_money__mutmut_orig(self, bank: Bank, currency: Currency) -> Money:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et renvoie un objet Money
        """
        total = Money(0.0, currency)
        for money in self.monies:
            converted = bank.convert(money, currency)
            total = total + converted
        return total

    def xǁPortfolioǁevaluate_money__mutmut_1(self, bank: Bank, currency: Currency) -> Money:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et renvoie un objet Money
        """
        total = None
        for money in self.monies:
            converted = bank.convert(money, currency)
            total = total + converted
        return total

    def xǁPortfolioǁevaluate_money__mutmut_2(self, bank: Bank, currency: Currency) -> Money:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et renvoie un objet Money
        """
        total = Money(None, currency)
        for money in self.monies:
            converted = bank.convert(money, currency)
            total = total + converted
        return total

    def xǁPortfolioǁevaluate_money__mutmut_3(self, bank: Bank, currency: Currency) -> Money:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et renvoie un objet Money
        """
        total = Money(0.0, None)
        for money in self.monies:
            converted = bank.convert(money, currency)
            total = total + converted
        return total

    def xǁPortfolioǁevaluate_money__mutmut_4(self, bank: Bank, currency: Currency) -> Money:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et renvoie un objet Money
        """
        total = Money(currency)
        for money in self.monies:
            converted = bank.convert(money, currency)
            total = total + converted
        return total

    def xǁPortfolioǁevaluate_money__mutmut_5(self, bank: Bank, currency: Currency) -> Money:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et renvoie un objet Money
        """
        total = Money(0.0, )
        for money in self.monies:
            converted = bank.convert(money, currency)
            total = total + converted
        return total

    def xǁPortfolioǁevaluate_money__mutmut_6(self, bank: Bank, currency: Currency) -> Money:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et renvoie un objet Money
        """
        total = Money(1.0, currency)
        for money in self.monies:
            converted = bank.convert(money, currency)
            total = total + converted
        return total

    def xǁPortfolioǁevaluate_money__mutmut_7(self, bank: Bank, currency: Currency) -> Money:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et renvoie un objet Money
        """
        total = Money(0.0, currency)
        for money in self.monies:
            converted = None
            total = total + converted
        return total

    def xǁPortfolioǁevaluate_money__mutmut_8(self, bank: Bank, currency: Currency) -> Money:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et renvoie un objet Money
        """
        total = Money(0.0, currency)
        for money in self.monies:
            converted = bank.convert(None, currency)
            total = total + converted
        return total

    def xǁPortfolioǁevaluate_money__mutmut_9(self, bank: Bank, currency: Currency) -> Money:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et renvoie un objet Money
        """
        total = Money(0.0, currency)
        for money in self.monies:
            converted = bank.convert(money, None)
            total = total + converted
        return total

    def xǁPortfolioǁevaluate_money__mutmut_10(self, bank: Bank, currency: Currency) -> Money:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et renvoie un objet Money
        """
        total = Money(0.0, currency)
        for money in self.monies:
            converted = bank.convert(currency)
            total = total + converted
        return total

    def xǁPortfolioǁevaluate_money__mutmut_11(self, bank: Bank, currency: Currency) -> Money:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et renvoie un objet Money
        """
        total = Money(0.0, currency)
        for money in self.monies:
            converted = bank.convert(money, )
            total = total + converted
        return total

    def xǁPortfolioǁevaluate_money__mutmut_12(self, bank: Bank, currency: Currency) -> Money:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et renvoie un objet Money
        """
        total = Money(0.0, currency)
        for money in self.monies:
            converted = bank.convert(money, currency)
            total = None
        return total

    def xǁPortfolioǁevaluate_money__mutmut_13(self, bank: Bank, currency: Currency) -> Money:
        """
        Évalue le portefeuille dans la monnaie donnée en paramètre et renvoie un objet Money
        """
        total = Money(0.0, currency)
        for money in self.monies:
            converted = bank.convert(money, currency)
            total = total - converted
        return total
    
    xǁPortfolioǁevaluate_money__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPortfolioǁevaluate_money__mutmut_1': xǁPortfolioǁevaluate_money__mutmut_1, 
        'xǁPortfolioǁevaluate_money__mutmut_2': xǁPortfolioǁevaluate_money__mutmut_2, 
        'xǁPortfolioǁevaluate_money__mutmut_3': xǁPortfolioǁevaluate_money__mutmut_3, 
        'xǁPortfolioǁevaluate_money__mutmut_4': xǁPortfolioǁevaluate_money__mutmut_4, 
        'xǁPortfolioǁevaluate_money__mutmut_5': xǁPortfolioǁevaluate_money__mutmut_5, 
        'xǁPortfolioǁevaluate_money__mutmut_6': xǁPortfolioǁevaluate_money__mutmut_6, 
        'xǁPortfolioǁevaluate_money__mutmut_7': xǁPortfolioǁevaluate_money__mutmut_7, 
        'xǁPortfolioǁevaluate_money__mutmut_8': xǁPortfolioǁevaluate_money__mutmut_8, 
        'xǁPortfolioǁevaluate_money__mutmut_9': xǁPortfolioǁevaluate_money__mutmut_9, 
        'xǁPortfolioǁevaluate_money__mutmut_10': xǁPortfolioǁevaluate_money__mutmut_10, 
        'xǁPortfolioǁevaluate_money__mutmut_11': xǁPortfolioǁevaluate_money__mutmut_11, 
        'xǁPortfolioǁevaluate_money__mutmut_12': xǁPortfolioǁevaluate_money__mutmut_12, 
        'xǁPortfolioǁevaluate_money__mutmut_13': xǁPortfolioǁevaluate_money__mutmut_13
    }
    xǁPortfolioǁevaluate_money__mutmut_orig.__name__ = 'xǁPortfolioǁevaluate_money'

    def add(self, amount: float, currency: Currency) -> None:
        args = [amount, currency]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPortfolioǁadd__mutmut_orig'), object.__getattribute__(self, 'xǁPortfolioǁadd__mutmut_mutants'), args, kwargs, self)

    def xǁPortfolioǁadd__mutmut_orig(self, amount: float, currency: Currency) -> None:
        """
        Ajoute une somme d'argent dans une monnaie donnée au portefeuille
        """
        self.monies.append(Money(amount, currency))

    def xǁPortfolioǁadd__mutmut_1(self, amount: float, currency: Currency) -> None:
        """
        Ajoute une somme d'argent dans une monnaie donnée au portefeuille
        """
        self.monies.append(None)

    def xǁPortfolioǁadd__mutmut_2(self, amount: float, currency: Currency) -> None:
        """
        Ajoute une somme d'argent dans une monnaie donnée au portefeuille
        """
        self.monies.append(Money(None, currency))

    def xǁPortfolioǁadd__mutmut_3(self, amount: float, currency: Currency) -> None:
        """
        Ajoute une somme d'argent dans une monnaie donnée au portefeuille
        """
        self.monies.append(Money(amount, None))

    def xǁPortfolioǁadd__mutmut_4(self, amount: float, currency: Currency) -> None:
        """
        Ajoute une somme d'argent dans une monnaie donnée au portefeuille
        """
        self.monies.append(Money(currency))

    def xǁPortfolioǁadd__mutmut_5(self, amount: float, currency: Currency) -> None:
        """
        Ajoute une somme d'argent dans une monnaie donnée au portefeuille
        """
        self.monies.append(Money(amount, ))
    
    xǁPortfolioǁadd__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPortfolioǁadd__mutmut_1': xǁPortfolioǁadd__mutmut_1, 
        'xǁPortfolioǁadd__mutmut_2': xǁPortfolioǁadd__mutmut_2, 
        'xǁPortfolioǁadd__mutmut_3': xǁPortfolioǁadd__mutmut_3, 
        'xǁPortfolioǁadd__mutmut_4': xǁPortfolioǁadd__mutmut_4, 
        'xǁPortfolioǁadd__mutmut_5': xǁPortfolioǁadd__mutmut_5
    }
    xǁPortfolioǁadd__mutmut_orig.__name__ = 'xǁPortfolioǁadd'

    def add_money(self, money: Money) -> None:
        args = [money]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPortfolioǁadd_money__mutmut_orig'), object.__getattribute__(self, 'xǁPortfolioǁadd_money__mutmut_mutants'), args, kwargs, self)

    def xǁPortfolioǁadd_money__mutmut_orig(self, money: Money) -> None:
        """
        Ajoute un objet Money au portefeuille
        """
        self.monies.append(money)

    def xǁPortfolioǁadd_money__mutmut_1(self, money: Money) -> None:
        """
        Ajoute un objet Money au portefeuille
        """
        self.monies.append(None)
    
    xǁPortfolioǁadd_money__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPortfolioǁadd_money__mutmut_1': xǁPortfolioǁadd_money__mutmut_1
    }
    xǁPortfolioǁadd_money__mutmut_orig.__name__ = 'xǁPortfolioǁadd_money'