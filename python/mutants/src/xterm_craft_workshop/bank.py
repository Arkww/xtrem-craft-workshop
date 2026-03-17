from __future__ import annotations
from typing import Dict
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
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


class Bank:
    def __init__(self, exchange_rate: Dict[str, float] = None):
        args = [exchange_rate]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁBankǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁBankǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁBankǁ__init____mutmut_orig(self, exchange_rate: Dict[str, float] = None):
        self._exchange_rate = exchange_rate if exchange_rate is not None else {}
    def xǁBankǁ__init____mutmut_1(self, exchange_rate: Dict[str, float] = None):
        self._exchange_rate = None
    def xǁBankǁ__init____mutmut_2(self, exchange_rate: Dict[str, float] = None):
        self._exchange_rate = exchange_rate if exchange_rate is None else {}
    
    xǁBankǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁBankǁ__init____mutmut_1': xǁBankǁ__init____mutmut_1, 
        'xǁBankǁ__init____mutmut_2': xǁBankǁ__init____mutmut_2
    }
    xǁBankǁ__init____mutmut_orig.__name__ = 'xǁBankǁ__init__'

    @staticmethod
    def create(from_currency: Currency, to_currency: Currency, rate: float) -> "Bank":
        """
        Créer une banque avec un taux d'échange initial
        """
        bank = Bank()
        bank.add_exchange_rate(from_currency, to_currency, rate)
        return bank

    def add_exchange_rate(self, from_currency: Currency, to_currency: Currency, rate: float) -> None:
        args = [from_currency, to_currency, rate]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁBankǁadd_exchange_rate__mutmut_orig'), object.__getattribute__(self, 'xǁBankǁadd_exchange_rate__mutmut_mutants'), args, kwargs, self)

    def xǁBankǁadd_exchange_rate__mutmut_orig(self, from_currency: Currency, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange
        """
        self._exchange_rate[f'{from_currency.value}->{to_currency.value}'] = rate

    def xǁBankǁadd_exchange_rate__mutmut_1(self, from_currency: Currency, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange
        """
        self._exchange_rate[f'{from_currency.value}->{to_currency.value}'] = None
    
    xǁBankǁadd_exchange_rate__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁBankǁadd_exchange_rate__mutmut_1': xǁBankǁadd_exchange_rate__mutmut_1
    }
    xǁBankǁadd_exchange_rate__mutmut_orig.__name__ = 'xǁBankǁadd_exchange_rate'

    def convert_currency(self, amount: float, from_currency: Currency, to_currency: Currency) -> float:
        args = [amount, from_currency, to_currency]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁBankǁconvert_currency__mutmut_orig'), object.__getattribute__(self, 'xǁBankǁconvert_currency__mutmut_mutants'), args, kwargs, self)

    def xǁBankǁconvert_currency__mutmut_orig(self, amount: float, from_currency: Currency, to_currency: Currency) -> float:
        """
        Convertir un montant d'une monnaie à une autre
        """
        if from_currency == to_currency:
            return amount

        key = f'{from_currency.value}->{to_currency.value}'
        if key not in self._exchange_rate:
            raise MissingExchangeRateError(from_currency, to_currency)

        return amount * self._exchange_rate[key]

    def xǁBankǁconvert_currency__mutmut_1(self, amount: float, from_currency: Currency, to_currency: Currency) -> float:
        """
        Convertir un montant d'une monnaie à une autre
        """
        if from_currency != to_currency:
            return amount

        key = f'{from_currency.value}->{to_currency.value}'
        if key not in self._exchange_rate:
            raise MissingExchangeRateError(from_currency, to_currency)

        return amount * self._exchange_rate[key]

    def xǁBankǁconvert_currency__mutmut_2(self, amount: float, from_currency: Currency, to_currency: Currency) -> float:
        """
        Convertir un montant d'une monnaie à une autre
        """
        if from_currency == to_currency:
            return amount

        key = None
        if key not in self._exchange_rate:
            raise MissingExchangeRateError(from_currency, to_currency)

        return amount * self._exchange_rate[key]

    def xǁBankǁconvert_currency__mutmut_3(self, amount: float, from_currency: Currency, to_currency: Currency) -> float:
        """
        Convertir un montant d'une monnaie à une autre
        """
        if from_currency == to_currency:
            return amount

        key = f'{from_currency.value}->{to_currency.value}'
        if key in self._exchange_rate:
            raise MissingExchangeRateError(from_currency, to_currency)

        return amount * self._exchange_rate[key]

    def xǁBankǁconvert_currency__mutmut_4(self, amount: float, from_currency: Currency, to_currency: Currency) -> float:
        """
        Convertir un montant d'une monnaie à une autre
        """
        if from_currency == to_currency:
            return amount

        key = f'{from_currency.value}->{to_currency.value}'
        if key not in self._exchange_rate:
            raise MissingExchangeRateError(None, to_currency)

        return amount * self._exchange_rate[key]

    def xǁBankǁconvert_currency__mutmut_5(self, amount: float, from_currency: Currency, to_currency: Currency) -> float:
        """
        Convertir un montant d'une monnaie à une autre
        """
        if from_currency == to_currency:
            return amount

        key = f'{from_currency.value}->{to_currency.value}'
        if key not in self._exchange_rate:
            raise MissingExchangeRateError(from_currency, None)

        return amount * self._exchange_rate[key]

    def xǁBankǁconvert_currency__mutmut_6(self, amount: float, from_currency: Currency, to_currency: Currency) -> float:
        """
        Convertir un montant d'une monnaie à une autre
        """
        if from_currency == to_currency:
            return amount

        key = f'{from_currency.value}->{to_currency.value}'
        if key not in self._exchange_rate:
            raise MissingExchangeRateError(to_currency)

        return amount * self._exchange_rate[key]

    def xǁBankǁconvert_currency__mutmut_7(self, amount: float, from_currency: Currency, to_currency: Currency) -> float:
        """
        Convertir un montant d'une monnaie à une autre
        """
        if from_currency == to_currency:
            return amount

        key = f'{from_currency.value}->{to_currency.value}'
        if key not in self._exchange_rate:
            raise MissingExchangeRateError(from_currency, )

        return amount * self._exchange_rate[key]

    def xǁBankǁconvert_currency__mutmut_8(self, amount: float, from_currency: Currency, to_currency: Currency) -> float:
        """
        Convertir un montant d'une monnaie à une autre
        """
        if from_currency == to_currency:
            return amount

        key = f'{from_currency.value}->{to_currency.value}'
        if key not in self._exchange_rate:
            raise MissingExchangeRateError(from_currency, to_currency)

        return amount / self._exchange_rate[key]
    
    xǁBankǁconvert_currency__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁBankǁconvert_currency__mutmut_1': xǁBankǁconvert_currency__mutmut_1, 
        'xǁBankǁconvert_currency__mutmut_2': xǁBankǁconvert_currency__mutmut_2, 
        'xǁBankǁconvert_currency__mutmut_3': xǁBankǁconvert_currency__mutmut_3, 
        'xǁBankǁconvert_currency__mutmut_4': xǁBankǁconvert_currency__mutmut_4, 
        'xǁBankǁconvert_currency__mutmut_5': xǁBankǁconvert_currency__mutmut_5, 
        'xǁBankǁconvert_currency__mutmut_6': xǁBankǁconvert_currency__mutmut_6, 
        'xǁBankǁconvert_currency__mutmut_7': xǁBankǁconvert_currency__mutmut_7, 
        'xǁBankǁconvert_currency__mutmut_8': xǁBankǁconvert_currency__mutmut_8
    }
    xǁBankǁconvert_currency__mutmut_orig.__name__ = 'xǁBankǁconvert_currency'

    def convert(self, money: Money, to_currency: Currency) -> Money:
        args = [money, to_currency]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁBankǁconvert__mutmut_orig'), object.__getattribute__(self, 'xǁBankǁconvert__mutmut_mutants'), args, kwargs, self)

    def xǁBankǁconvert__mutmut_orig(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)

        converted_amount = self.convert_currency(money.amount, money.currency, to_currency)
        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_1(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency != to_currency:
            return Money(money.amount, to_currency)

        converted_amount = self.convert_currency(money.amount, money.currency, to_currency)
        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_2(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(None, to_currency)

        converted_amount = self.convert_currency(money.amount, money.currency, to_currency)
        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_3(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, None)

        converted_amount = self.convert_currency(money.amount, money.currency, to_currency)
        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_4(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(to_currency)

        converted_amount = self.convert_currency(money.amount, money.currency, to_currency)
        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_5(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, )

        converted_amount = self.convert_currency(money.amount, money.currency, to_currency)
        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_6(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)

        converted_amount = None
        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_7(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)

        converted_amount = self.convert_currency(None, money.currency, to_currency)
        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_8(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)

        converted_amount = self.convert_currency(money.amount, None, to_currency)
        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_9(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)

        converted_amount = self.convert_currency(money.amount, money.currency, None)
        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_10(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)

        converted_amount = self.convert_currency(money.currency, to_currency)
        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_11(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)

        converted_amount = self.convert_currency(money.amount, to_currency)
        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_12(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)

        converted_amount = self.convert_currency(money.amount, money.currency, )
        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_13(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)

        converted_amount = self.convert_currency(money.amount, money.currency, to_currency)
        return Money(None, to_currency)

    def xǁBankǁconvert__mutmut_14(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)

        converted_amount = self.convert_currency(money.amount, money.currency, to_currency)
        return Money(converted_amount, None)

    def xǁBankǁconvert__mutmut_15(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)

        converted_amount = self.convert_currency(money.amount, money.currency, to_currency)
        return Money(to_currency)

    def xǁBankǁconvert__mutmut_16(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)

        converted_amount = self.convert_currency(money.amount, money.currency, to_currency)
        return Money(converted_amount, )
    
    xǁBankǁconvert__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁBankǁconvert__mutmut_1': xǁBankǁconvert__mutmut_1, 
        'xǁBankǁconvert__mutmut_2': xǁBankǁconvert__mutmut_2, 
        'xǁBankǁconvert__mutmut_3': xǁBankǁconvert__mutmut_3, 
        'xǁBankǁconvert__mutmut_4': xǁBankǁconvert__mutmut_4, 
        'xǁBankǁconvert__mutmut_5': xǁBankǁconvert__mutmut_5, 
        'xǁBankǁconvert__mutmut_6': xǁBankǁconvert__mutmut_6, 
        'xǁBankǁconvert__mutmut_7': xǁBankǁconvert__mutmut_7, 
        'xǁBankǁconvert__mutmut_8': xǁBankǁconvert__mutmut_8, 
        'xǁBankǁconvert__mutmut_9': xǁBankǁconvert__mutmut_9, 
        'xǁBankǁconvert__mutmut_10': xǁBankǁconvert__mutmut_10, 
        'xǁBankǁconvert__mutmut_11': xǁBankǁconvert__mutmut_11, 
        'xǁBankǁconvert__mutmut_12': xǁBankǁconvert__mutmut_12, 
        'xǁBankǁconvert__mutmut_13': xǁBankǁconvert__mutmut_13, 
        'xǁBankǁconvert__mutmut_14': xǁBankǁconvert__mutmut_14, 
        'xǁBankǁconvert__mutmut_15': xǁBankǁconvert__mutmut_15, 
        'xǁBankǁconvert__mutmut_16': xǁBankǁconvert__mutmut_16
    }
    xǁBankǁconvert__mutmut_orig.__name__ = 'xǁBankǁconvert'