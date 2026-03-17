from __future__ import annotations
from .currency import Currency
from typing import Union
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


class Money:
    def __init__(self, amount: float, currency: Currency):
        args = [amount, currency]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁMoneyǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁMoneyǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁMoneyǁ__init____mutmut_orig(self, amount: float, currency: Currency):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.amount = amount
        self.currency = currency
    def xǁMoneyǁ__init____mutmut_1(self, amount: float, currency: Currency):
        if amount <= 0:
            raise ValueError("Amount cannot be negative")
        self.amount = amount
        self.currency = currency
    def xǁMoneyǁ__init____mutmut_2(self, amount: float, currency: Currency):
        if amount < 1:
            raise ValueError("Amount cannot be negative")
        self.amount = amount
        self.currency = currency
    def xǁMoneyǁ__init____mutmut_3(self, amount: float, currency: Currency):
        if amount < 0:
            raise ValueError(None)
        self.amount = amount
        self.currency = currency
    def xǁMoneyǁ__init____mutmut_4(self, amount: float, currency: Currency):
        if amount < 0:
            raise ValueError("XXAmount cannot be negativeXX")
        self.amount = amount
        self.currency = currency
    def xǁMoneyǁ__init____mutmut_5(self, amount: float, currency: Currency):
        if amount < 0:
            raise ValueError("amount cannot be negative")
        self.amount = amount
        self.currency = currency
    def xǁMoneyǁ__init____mutmut_6(self, amount: float, currency: Currency):
        if amount < 0:
            raise ValueError("AMOUNT CANNOT BE NEGATIVE")
        self.amount = amount
        self.currency = currency
    def xǁMoneyǁ__init____mutmut_7(self, amount: float, currency: Currency):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.amount = None
        self.currency = currency
    def xǁMoneyǁ__init____mutmut_8(self, amount: float, currency: Currency):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.amount = amount
        self.currency = None
    
    xǁMoneyǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁMoneyǁ__init____mutmut_1': xǁMoneyǁ__init____mutmut_1, 
        'xǁMoneyǁ__init____mutmut_2': xǁMoneyǁ__init____mutmut_2, 
        'xǁMoneyǁ__init____mutmut_3': xǁMoneyǁ__init____mutmut_3, 
        'xǁMoneyǁ__init____mutmut_4': xǁMoneyǁ__init____mutmut_4, 
        'xǁMoneyǁ__init____mutmut_5': xǁMoneyǁ__init____mutmut_5, 
        'xǁMoneyǁ__init____mutmut_6': xǁMoneyǁ__init____mutmut_6, 
        'xǁMoneyǁ__init____mutmut_7': xǁMoneyǁ__init____mutmut_7, 
        'xǁMoneyǁ__init____mutmut_8': xǁMoneyǁ__init____mutmut_8
    }
    xǁMoneyǁ__init____mutmut_orig.__name__ = 'xǁMoneyǁ__init__'

    def __add__(self, other: Union[Money, float, int]) -> Money:
        args = [other]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁMoneyǁ__add____mutmut_orig'), object.__getattribute__(self, 'xǁMoneyǁ__add____mutmut_mutants'), args, kwargs, self)

    def xǁMoneyǁ__add____mutmut_orig(self, other: Union[Money, float, int]) -> Money:
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

    def xǁMoneyǁ__add____mutmut_1(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour additionner deux Money ou un Money avec un nombre
        """
        if isinstance(other, (int, float)):
            if other <= 0:
                raise ValueError("Amount cannot be negative")
            return Money(self.amount + other, self.currency)
        elif isinstance(other, Money):
            if other.amount < 0:
                raise ValueError("Amount cannot be negative")
            if other.currency != self.currency:
                raise ValueError("Cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_2(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour additionner deux Money ou un Money avec un nombre
        """
        if isinstance(other, (int, float)):
            if other < 1:
                raise ValueError("Amount cannot be negative")
            return Money(self.amount + other, self.currency)
        elif isinstance(other, Money):
            if other.amount < 0:
                raise ValueError("Amount cannot be negative")
            if other.currency != self.currency:
                raise ValueError("Cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_3(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour additionner deux Money ou un Money avec un nombre
        """
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError(None)
            return Money(self.amount + other, self.currency)
        elif isinstance(other, Money):
            if other.amount < 0:
                raise ValueError("Amount cannot be negative")
            if other.currency != self.currency:
                raise ValueError("Cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_4(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour additionner deux Money ou un Money avec un nombre
        """
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError("XXAmount cannot be negativeXX")
            return Money(self.amount + other, self.currency)
        elif isinstance(other, Money):
            if other.amount < 0:
                raise ValueError("Amount cannot be negative")
            if other.currency != self.currency:
                raise ValueError("Cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_5(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour additionner deux Money ou un Money avec un nombre
        """
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError("amount cannot be negative")
            return Money(self.amount + other, self.currency)
        elif isinstance(other, Money):
            if other.amount < 0:
                raise ValueError("Amount cannot be negative")
            if other.currency != self.currency:
                raise ValueError("Cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_6(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour additionner deux Money ou un Money avec un nombre
        """
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError("AMOUNT CANNOT BE NEGATIVE")
            return Money(self.amount + other, self.currency)
        elif isinstance(other, Money):
            if other.amount < 0:
                raise ValueError("Amount cannot be negative")
            if other.currency != self.currency:
                raise ValueError("Cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_7(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour additionner deux Money ou un Money avec un nombre
        """
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError("Amount cannot be negative")
            return Money(None, self.currency)
        elif isinstance(other, Money):
            if other.amount < 0:
                raise ValueError("Amount cannot be negative")
            if other.currency != self.currency:
                raise ValueError("Cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_8(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour additionner deux Money ou un Money avec un nombre
        """
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError("Amount cannot be negative")
            return Money(self.amount + other, None)
        elif isinstance(other, Money):
            if other.amount < 0:
                raise ValueError("Amount cannot be negative")
            if other.currency != self.currency:
                raise ValueError("Cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_9(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour additionner deux Money ou un Money avec un nombre
        """
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError("Amount cannot be negative")
            return Money(self.currency)
        elif isinstance(other, Money):
            if other.amount < 0:
                raise ValueError("Amount cannot be negative")
            if other.currency != self.currency:
                raise ValueError("Cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_10(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour additionner deux Money ou un Money avec un nombre
        """
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError("Amount cannot be negative")
            return Money(self.amount + other, )
        elif isinstance(other, Money):
            if other.amount < 0:
                raise ValueError("Amount cannot be negative")
            if other.currency != self.currency:
                raise ValueError("Cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_11(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour additionner deux Money ou un Money avec un nombre
        """
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError("Amount cannot be negative")
            return Money(self.amount - other, self.currency)
        elif isinstance(other, Money):
            if other.amount < 0:
                raise ValueError("Amount cannot be negative")
            if other.currency != self.currency:
                raise ValueError("Cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_12(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour additionner deux Money ou un Money avec un nombre
        """
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError("Amount cannot be negative")
            return Money(self.amount + other, self.currency)
        elif isinstance(other, Money):
            if other.amount <= 0:
                raise ValueError("Amount cannot be negative")
            if other.currency != self.currency:
                raise ValueError("Cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_13(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour additionner deux Money ou un Money avec un nombre
        """
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError("Amount cannot be negative")
            return Money(self.amount + other, self.currency)
        elif isinstance(other, Money):
            if other.amount < 1:
                raise ValueError("Amount cannot be negative")
            if other.currency != self.currency:
                raise ValueError("Cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_14(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour additionner deux Money ou un Money avec un nombre
        """
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError("Amount cannot be negative")
            return Money(self.amount + other, self.currency)
        elif isinstance(other, Money):
            if other.amount < 0:
                raise ValueError(None)
            if other.currency != self.currency:
                raise ValueError("Cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_15(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour additionner deux Money ou un Money avec un nombre
        """
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError("Amount cannot be negative")
            return Money(self.amount + other, self.currency)
        elif isinstance(other, Money):
            if other.amount < 0:
                raise ValueError("XXAmount cannot be negativeXX")
            if other.currency != self.currency:
                raise ValueError("Cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_16(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour additionner deux Money ou un Money avec un nombre
        """
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError("Amount cannot be negative")
            return Money(self.amount + other, self.currency)
        elif isinstance(other, Money):
            if other.amount < 0:
                raise ValueError("amount cannot be negative")
            if other.currency != self.currency:
                raise ValueError("Cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_17(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour additionner deux Money ou un Money avec un nombre
        """
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError("Amount cannot be negative")
            return Money(self.amount + other, self.currency)
        elif isinstance(other, Money):
            if other.amount < 0:
                raise ValueError("AMOUNT CANNOT BE NEGATIVE")
            if other.currency != self.currency:
                raise ValueError("Cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_18(self, other: Union[Money, float, int]) -> Money:
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
            if other.currency == self.currency:
                raise ValueError("Cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_19(self, other: Union[Money, float, int]) -> Money:
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
                raise ValueError(None)
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_20(self, other: Union[Money, float, int]) -> Money:
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
                raise ValueError("XXCannot add money with different currenciesXX")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_21(self, other: Union[Money, float, int]) -> Money:
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
                raise ValueError("cannot add money with different currencies")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_22(self, other: Union[Money, float, int]) -> Money:
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
                raise ValueError("CANNOT ADD MONEY WITH DIFFERENT CURRENCIES")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_23(self, other: Union[Money, float, int]) -> Money:
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
            return Money(None, self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_24(self, other: Union[Money, float, int]) -> Money:
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
            return Money(self.amount + other.amount, None)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_25(self, other: Union[Money, float, int]) -> Money:
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
            return Money(self.currency)
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_26(self, other: Union[Money, float, int]) -> Money:
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
            return Money(self.amount + other.amount, )
        return NotImplemented

    def xǁMoneyǁ__add____mutmut_27(self, other: Union[Money, float, int]) -> Money:
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
            return Money(self.amount - other.amount, self.currency)
        return NotImplemented
    
    xǁMoneyǁ__add____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁMoneyǁ__add____mutmut_1': xǁMoneyǁ__add____mutmut_1, 
        'xǁMoneyǁ__add____mutmut_2': xǁMoneyǁ__add____mutmut_2, 
        'xǁMoneyǁ__add____mutmut_3': xǁMoneyǁ__add____mutmut_3, 
        'xǁMoneyǁ__add____mutmut_4': xǁMoneyǁ__add____mutmut_4, 
        'xǁMoneyǁ__add____mutmut_5': xǁMoneyǁ__add____mutmut_5, 
        'xǁMoneyǁ__add____mutmut_6': xǁMoneyǁ__add____mutmut_6, 
        'xǁMoneyǁ__add____mutmut_7': xǁMoneyǁ__add____mutmut_7, 
        'xǁMoneyǁ__add____mutmut_8': xǁMoneyǁ__add____mutmut_8, 
        'xǁMoneyǁ__add____mutmut_9': xǁMoneyǁ__add____mutmut_9, 
        'xǁMoneyǁ__add____mutmut_10': xǁMoneyǁ__add____mutmut_10, 
        'xǁMoneyǁ__add____mutmut_11': xǁMoneyǁ__add____mutmut_11, 
        'xǁMoneyǁ__add____mutmut_12': xǁMoneyǁ__add____mutmut_12, 
        'xǁMoneyǁ__add____mutmut_13': xǁMoneyǁ__add____mutmut_13, 
        'xǁMoneyǁ__add____mutmut_14': xǁMoneyǁ__add____mutmut_14, 
        'xǁMoneyǁ__add____mutmut_15': xǁMoneyǁ__add____mutmut_15, 
        'xǁMoneyǁ__add____mutmut_16': xǁMoneyǁ__add____mutmut_16, 
        'xǁMoneyǁ__add____mutmut_17': xǁMoneyǁ__add____mutmut_17, 
        'xǁMoneyǁ__add____mutmut_18': xǁMoneyǁ__add____mutmut_18, 
        'xǁMoneyǁ__add____mutmut_19': xǁMoneyǁ__add____mutmut_19, 
        'xǁMoneyǁ__add____mutmut_20': xǁMoneyǁ__add____mutmut_20, 
        'xǁMoneyǁ__add____mutmut_21': xǁMoneyǁ__add____mutmut_21, 
        'xǁMoneyǁ__add____mutmut_22': xǁMoneyǁ__add____mutmut_22, 
        'xǁMoneyǁ__add____mutmut_23': xǁMoneyǁ__add____mutmut_23, 
        'xǁMoneyǁ__add____mutmut_24': xǁMoneyǁ__add____mutmut_24, 
        'xǁMoneyǁ__add____mutmut_25': xǁMoneyǁ__add____mutmut_25, 
        'xǁMoneyǁ__add____mutmut_26': xǁMoneyǁ__add____mutmut_26, 
        'xǁMoneyǁ__add____mutmut_27': xǁMoneyǁ__add____mutmut_27
    }
    xǁMoneyǁ__add____mutmut_orig.__name__ = 'xǁMoneyǁ__add__'

    def __radd__(self, other: Union[Money, float, int]) -> Money:
        args = [other]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁMoneyǁ__radd____mutmut_orig'), object.__getattribute__(self, 'xǁMoneyǁ__radd____mutmut_mutants'), args, kwargs, self)

    def xǁMoneyǁ__radd____mutmut_orig(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour l'addition à droite
        """
        return self.__add__(other)

    def xǁMoneyǁ__radd____mutmut_1(self, other: Union[Money, float, int]) -> Money:
        """
        Surcharge de l'opérateur + pour l'addition à droite
        """
        return self.__add__(None)
    
    xǁMoneyǁ__radd____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁMoneyǁ__radd____mutmut_1': xǁMoneyǁ__radd____mutmut_1
    }
    xǁMoneyǁ__radd____mutmut_orig.__name__ = 'xǁMoneyǁ__radd__'

    def __mul__(self, factor: Union[float, int]) -> Money:
        args = [factor]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁMoneyǁ__mul____mutmut_orig'), object.__getattribute__(self, 'xǁMoneyǁ__mul____mutmut_mutants'), args, kwargs, self)

    def xǁMoneyǁ__mul____mutmut_orig(self, factor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur * pour multiplier un Money par un facteur
        """
        if isinstance(factor, (int, float)):
            if factor < 0:
                raise ValueError("Factor cannot be negative")
            return Money(self.amount * factor, self.currency)
        return NotImplemented

    def xǁMoneyǁ__mul____mutmut_1(self, factor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur * pour multiplier un Money par un facteur
        """
        if isinstance(factor, (int, float)):
            if factor <= 0:
                raise ValueError("Factor cannot be negative")
            return Money(self.amount * factor, self.currency)
        return NotImplemented

    def xǁMoneyǁ__mul____mutmut_2(self, factor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur * pour multiplier un Money par un facteur
        """
        if isinstance(factor, (int, float)):
            if factor < 1:
                raise ValueError("Factor cannot be negative")
            return Money(self.amount * factor, self.currency)
        return NotImplemented

    def xǁMoneyǁ__mul____mutmut_3(self, factor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur * pour multiplier un Money par un facteur
        """
        if isinstance(factor, (int, float)):
            if factor < 0:
                raise ValueError(None)
            return Money(self.amount * factor, self.currency)
        return NotImplemented

    def xǁMoneyǁ__mul____mutmut_4(self, factor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur * pour multiplier un Money par un facteur
        """
        if isinstance(factor, (int, float)):
            if factor < 0:
                raise ValueError("XXFactor cannot be negativeXX")
            return Money(self.amount * factor, self.currency)
        return NotImplemented

    def xǁMoneyǁ__mul____mutmut_5(self, factor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur * pour multiplier un Money par un facteur
        """
        if isinstance(factor, (int, float)):
            if factor < 0:
                raise ValueError("factor cannot be negative")
            return Money(self.amount * factor, self.currency)
        return NotImplemented

    def xǁMoneyǁ__mul____mutmut_6(self, factor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur * pour multiplier un Money par un facteur
        """
        if isinstance(factor, (int, float)):
            if factor < 0:
                raise ValueError("FACTOR CANNOT BE NEGATIVE")
            return Money(self.amount * factor, self.currency)
        return NotImplemented

    def xǁMoneyǁ__mul____mutmut_7(self, factor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur * pour multiplier un Money par un facteur
        """
        if isinstance(factor, (int, float)):
            if factor < 0:
                raise ValueError("Factor cannot be negative")
            return Money(None, self.currency)
        return NotImplemented

    def xǁMoneyǁ__mul____mutmut_8(self, factor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur * pour multiplier un Money par un facteur
        """
        if isinstance(factor, (int, float)):
            if factor < 0:
                raise ValueError("Factor cannot be negative")
            return Money(self.amount * factor, None)
        return NotImplemented

    def xǁMoneyǁ__mul____mutmut_9(self, factor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur * pour multiplier un Money par un facteur
        """
        if isinstance(factor, (int, float)):
            if factor < 0:
                raise ValueError("Factor cannot be negative")
            return Money(self.currency)
        return NotImplemented

    def xǁMoneyǁ__mul____mutmut_10(self, factor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur * pour multiplier un Money par un facteur
        """
        if isinstance(factor, (int, float)):
            if factor < 0:
                raise ValueError("Factor cannot be negative")
            return Money(self.amount * factor, )
        return NotImplemented

    def xǁMoneyǁ__mul____mutmut_11(self, factor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur * pour multiplier un Money par un facteur
        """
        if isinstance(factor, (int, float)):
            if factor < 0:
                raise ValueError("Factor cannot be negative")
            return Money(self.amount / factor, self.currency)
        return NotImplemented
    
    xǁMoneyǁ__mul____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁMoneyǁ__mul____mutmut_1': xǁMoneyǁ__mul____mutmut_1, 
        'xǁMoneyǁ__mul____mutmut_2': xǁMoneyǁ__mul____mutmut_2, 
        'xǁMoneyǁ__mul____mutmut_3': xǁMoneyǁ__mul____mutmut_3, 
        'xǁMoneyǁ__mul____mutmut_4': xǁMoneyǁ__mul____mutmut_4, 
        'xǁMoneyǁ__mul____mutmut_5': xǁMoneyǁ__mul____mutmut_5, 
        'xǁMoneyǁ__mul____mutmut_6': xǁMoneyǁ__mul____mutmut_6, 
        'xǁMoneyǁ__mul____mutmut_7': xǁMoneyǁ__mul____mutmut_7, 
        'xǁMoneyǁ__mul____mutmut_8': xǁMoneyǁ__mul____mutmut_8, 
        'xǁMoneyǁ__mul____mutmut_9': xǁMoneyǁ__mul____mutmut_9, 
        'xǁMoneyǁ__mul____mutmut_10': xǁMoneyǁ__mul____mutmut_10, 
        'xǁMoneyǁ__mul____mutmut_11': xǁMoneyǁ__mul____mutmut_11
    }
    xǁMoneyǁ__mul____mutmut_orig.__name__ = 'xǁMoneyǁ__mul__'

    def __rmul__(self, factor: Union[float, int]) -> Money:
        args = [factor]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁMoneyǁ__rmul____mutmut_orig'), object.__getattribute__(self, 'xǁMoneyǁ__rmul____mutmut_mutants'), args, kwargs, self)

    def xǁMoneyǁ__rmul____mutmut_orig(self, factor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur * pour la multiplication à droite
        """
        return self.__mul__(factor)

    def xǁMoneyǁ__rmul____mutmut_1(self, factor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur * pour la multiplication à droite
        """
        return self.__mul__(None)
    
    xǁMoneyǁ__rmul____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁMoneyǁ__rmul____mutmut_1': xǁMoneyǁ__rmul____mutmut_1
    }
    xǁMoneyǁ__rmul____mutmut_orig.__name__ = 'xǁMoneyǁ__rmul__'

    def __truediv__(self, divisor: Union[float, int]) -> Money:
        args = [divisor]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁMoneyǁ__truediv____mutmut_orig'), object.__getattribute__(self, 'xǁMoneyǁ__truediv____mutmut_mutants'), args, kwargs, self)

    def xǁMoneyǁ__truediv____mutmut_orig(self, divisor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur / pour diviser un Money par un diviseur
        """
        if isinstance(divisor, (int, float)):
            if divisor <= 0:
                raise ValueError("Divisor must be positive")
            return Money(self.amount / divisor, self.currency)
        return NotImplemented

    def xǁMoneyǁ__truediv____mutmut_1(self, divisor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur / pour diviser un Money par un diviseur
        """
        if isinstance(divisor, (int, float)):
            if divisor < 0:
                raise ValueError("Divisor must be positive")
            return Money(self.amount / divisor, self.currency)
        return NotImplemented

    def xǁMoneyǁ__truediv____mutmut_2(self, divisor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur / pour diviser un Money par un diviseur
        """
        if isinstance(divisor, (int, float)):
            if divisor <= 1:
                raise ValueError("Divisor must be positive")
            return Money(self.amount / divisor, self.currency)
        return NotImplemented

    def xǁMoneyǁ__truediv____mutmut_3(self, divisor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur / pour diviser un Money par un diviseur
        """
        if isinstance(divisor, (int, float)):
            if divisor <= 0:
                raise ValueError(None)
            return Money(self.amount / divisor, self.currency)
        return NotImplemented

    def xǁMoneyǁ__truediv____mutmut_4(self, divisor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur / pour diviser un Money par un diviseur
        """
        if isinstance(divisor, (int, float)):
            if divisor <= 0:
                raise ValueError("XXDivisor must be positiveXX")
            return Money(self.amount / divisor, self.currency)
        return NotImplemented

    def xǁMoneyǁ__truediv____mutmut_5(self, divisor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur / pour diviser un Money par un diviseur
        """
        if isinstance(divisor, (int, float)):
            if divisor <= 0:
                raise ValueError("divisor must be positive")
            return Money(self.amount / divisor, self.currency)
        return NotImplemented

    def xǁMoneyǁ__truediv____mutmut_6(self, divisor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur / pour diviser un Money par un diviseur
        """
        if isinstance(divisor, (int, float)):
            if divisor <= 0:
                raise ValueError("DIVISOR MUST BE POSITIVE")
            return Money(self.amount / divisor, self.currency)
        return NotImplemented

    def xǁMoneyǁ__truediv____mutmut_7(self, divisor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur / pour diviser un Money par un diviseur
        """
        if isinstance(divisor, (int, float)):
            if divisor <= 0:
                raise ValueError("Divisor must be positive")
            return Money(None, self.currency)
        return NotImplemented

    def xǁMoneyǁ__truediv____mutmut_8(self, divisor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur / pour diviser un Money par un diviseur
        """
        if isinstance(divisor, (int, float)):
            if divisor <= 0:
                raise ValueError("Divisor must be positive")
            return Money(self.amount / divisor, None)
        return NotImplemented

    def xǁMoneyǁ__truediv____mutmut_9(self, divisor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur / pour diviser un Money par un diviseur
        """
        if isinstance(divisor, (int, float)):
            if divisor <= 0:
                raise ValueError("Divisor must be positive")
            return Money(self.currency)
        return NotImplemented

    def xǁMoneyǁ__truediv____mutmut_10(self, divisor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur / pour diviser un Money par un diviseur
        """
        if isinstance(divisor, (int, float)):
            if divisor <= 0:
                raise ValueError("Divisor must be positive")
            return Money(self.amount / divisor, )
        return NotImplemented

    def xǁMoneyǁ__truediv____mutmut_11(self, divisor: Union[float, int]) -> Money:
        """
        Surcharge de l'opérateur / pour diviser un Money par un diviseur
        """
        if isinstance(divisor, (int, float)):
            if divisor <= 0:
                raise ValueError("Divisor must be positive")
            return Money(self.amount * divisor, self.currency)
        return NotImplemented
    
    xǁMoneyǁ__truediv____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁMoneyǁ__truediv____mutmut_1': xǁMoneyǁ__truediv____mutmut_1, 
        'xǁMoneyǁ__truediv____mutmut_2': xǁMoneyǁ__truediv____mutmut_2, 
        'xǁMoneyǁ__truediv____mutmut_3': xǁMoneyǁ__truediv____mutmut_3, 
        'xǁMoneyǁ__truediv____mutmut_4': xǁMoneyǁ__truediv____mutmut_4, 
        'xǁMoneyǁ__truediv____mutmut_5': xǁMoneyǁ__truediv____mutmut_5, 
        'xǁMoneyǁ__truediv____mutmut_6': xǁMoneyǁ__truediv____mutmut_6, 
        'xǁMoneyǁ__truediv____mutmut_7': xǁMoneyǁ__truediv____mutmut_7, 
        'xǁMoneyǁ__truediv____mutmut_8': xǁMoneyǁ__truediv____mutmut_8, 
        'xǁMoneyǁ__truediv____mutmut_9': xǁMoneyǁ__truediv____mutmut_9, 
        'xǁMoneyǁ__truediv____mutmut_10': xǁMoneyǁ__truediv____mutmut_10, 
        'xǁMoneyǁ__truediv____mutmut_11': xǁMoneyǁ__truediv____mutmut_11
    }
    xǁMoneyǁ__truediv____mutmut_orig.__name__ = 'xǁMoneyǁ__truediv__'

    def __eq__(self, other: object) -> bool:
        args = [other]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁMoneyǁ__eq____mutmut_orig'), object.__getattribute__(self, 'xǁMoneyǁ__eq____mutmut_mutants'), args, kwargs, self)

    def xǁMoneyǁ__eq____mutmut_orig(self, other: object) -> bool:
        """
        Surcharge de l'opérateur == pour comparer deux Money
        """
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency

    def xǁMoneyǁ__eq____mutmut_1(self, other: object) -> bool:
        """
        Surcharge de l'opérateur == pour comparer deux Money
        """
        if isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency

    def xǁMoneyǁ__eq____mutmut_2(self, other: object) -> bool:
        """
        Surcharge de l'opérateur == pour comparer deux Money
        """
        if not isinstance(other, Money):
            return True
        return self.amount == other.amount and self.currency == other.currency

    def xǁMoneyǁ__eq____mutmut_3(self, other: object) -> bool:
        """
        Surcharge de l'opérateur == pour comparer deux Money
        """
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount or self.currency == other.currency

    def xǁMoneyǁ__eq____mutmut_4(self, other: object) -> bool:
        """
        Surcharge de l'opérateur == pour comparer deux Money
        """
        if not isinstance(other, Money):
            return False
        return self.amount != other.amount and self.currency == other.currency

    def xǁMoneyǁ__eq____mutmut_5(self, other: object) -> bool:
        """
        Surcharge de l'opérateur == pour comparer deux Money
        """
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency != other.currency
    
    xǁMoneyǁ__eq____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁMoneyǁ__eq____mutmut_1': xǁMoneyǁ__eq____mutmut_1, 
        'xǁMoneyǁ__eq____mutmut_2': xǁMoneyǁ__eq____mutmut_2, 
        'xǁMoneyǁ__eq____mutmut_3': xǁMoneyǁ__eq____mutmut_3, 
        'xǁMoneyǁ__eq____mutmut_4': xǁMoneyǁ__eq____mutmut_4, 
        'xǁMoneyǁ__eq____mutmut_5': xǁMoneyǁ__eq____mutmut_5
    }
    xǁMoneyǁ__eq____mutmut_orig.__name__ = 'xǁMoneyǁ__eq__'

    def __str__(self) -> str:
        return f"{self.amount} {self.currency.value}"

    def __repr__(self) -> str:
        return f"Money({self.amount}, {self.currency})"