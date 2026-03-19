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
    def __init__(self, pivot_currency: Currency, exchange_rate: Dict[str, float] = {}):
        args = [pivot_currency, exchange_rate]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁBankǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁBankǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁBankǁ__init____mutmut_orig(self, pivot_currency: Currency, exchange_rate: Dict[str, float] = {}):
        self._exchange_rate = exchange_rate
        assert pivot_currency is not None, "Le pivot currency ne peut pas être None"
        self._pivot_currency = pivot_currency
    def xǁBankǁ__init____mutmut_1(self, pivot_currency: Currency, exchange_rate: Dict[str, float] = {}):
        self._exchange_rate = None
        assert pivot_currency is not None, "Le pivot currency ne peut pas être None"
        self._pivot_currency = pivot_currency
    def xǁBankǁ__init____mutmut_2(self, pivot_currency: Currency, exchange_rate: Dict[str, float] = {}):
        self._exchange_rate = exchange_rate
        assert pivot_currency is None, "Le pivot currency ne peut pas être None"
        self._pivot_currency = pivot_currency
    def xǁBankǁ__init____mutmut_3(self, pivot_currency: Currency, exchange_rate: Dict[str, float] = {}):
        self._exchange_rate = exchange_rate
        assert pivot_currency is not None, "XXLe pivot currency ne peut pas être NoneXX"
        self._pivot_currency = pivot_currency
    def xǁBankǁ__init____mutmut_4(self, pivot_currency: Currency, exchange_rate: Dict[str, float] = {}):
        self._exchange_rate = exchange_rate
        assert pivot_currency is not None, "le pivot currency ne peut pas être none"
        self._pivot_currency = pivot_currency
    def xǁBankǁ__init____mutmut_5(self, pivot_currency: Currency, exchange_rate: Dict[str, float] = {}):
        self._exchange_rate = exchange_rate
        assert pivot_currency is not None, "LE PIVOT CURRENCY NE PEUT PAS ÊTRE NONE"
        self._pivot_currency = pivot_currency
    def xǁBankǁ__init____mutmut_6(self, pivot_currency: Currency, exchange_rate: Dict[str, float] = {}):
        self._exchange_rate = exchange_rate
        assert pivot_currency is not None, "Le pivot currency ne peut pas être None"
        self._pivot_currency = None
    
    xǁBankǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁBankǁ__init____mutmut_1': xǁBankǁ__init____mutmut_1, 
        'xǁBankǁ__init____mutmut_2': xǁBankǁ__init____mutmut_2, 
        'xǁBankǁ__init____mutmut_3': xǁBankǁ__init____mutmut_3, 
        'xǁBankǁ__init____mutmut_4': xǁBankǁ__init____mutmut_4, 
        'xǁBankǁ__init____mutmut_5': xǁBankǁ__init____mutmut_5, 
        'xǁBankǁ__init____mutmut_6': xǁBankǁ__init____mutmut_6
    }
    xǁBankǁ__init____mutmut_orig.__name__ = 'xǁBankǁ__init__'

    def add_exchange_rate(self, to_currency: Currency, rate: float) -> None:
        args = [to_currency, rate]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁBankǁadd_exchange_rate__mutmut_orig'), object.__getattribute__(self, 'xǁBankǁadd_exchange_rate__mutmut_mutants'), args, kwargs, self)

    def xǁBankǁadd_exchange_rate__mutmut_orig(self, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange (méthode métier)
        """
        assert rate > 0, "Le taux d'échange doit être positif"
        assert to_currency != self._pivot_currency, "Le to_currency doit être différent du pivot_currency"
        assert to_currency not in self._exchange_rate.keys(), "Le taux d'échange existe déjà"
        self._exchange_rate[to_currency] = rate

    def xǁBankǁadd_exchange_rate__mutmut_1(self, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange (méthode métier)
        """
        assert rate >= 0, "Le taux d'échange doit être positif"
        assert to_currency != self._pivot_currency, "Le to_currency doit être différent du pivot_currency"
        assert to_currency not in self._exchange_rate.keys(), "Le taux d'échange existe déjà"
        self._exchange_rate[to_currency] = rate

    def xǁBankǁadd_exchange_rate__mutmut_2(self, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange (méthode métier)
        """
        assert rate > 1, "Le taux d'échange doit être positif"
        assert to_currency != self._pivot_currency, "Le to_currency doit être différent du pivot_currency"
        assert to_currency not in self._exchange_rate.keys(), "Le taux d'échange existe déjà"
        self._exchange_rate[to_currency] = rate

    def xǁBankǁadd_exchange_rate__mutmut_3(self, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange (méthode métier)
        """
        assert rate > 0, "XXLe taux d'échange doit être positifXX"
        assert to_currency != self._pivot_currency, "Le to_currency doit être différent du pivot_currency"
        assert to_currency not in self._exchange_rate.keys(), "Le taux d'échange existe déjà"
        self._exchange_rate[to_currency] = rate

    def xǁBankǁadd_exchange_rate__mutmut_4(self, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange (méthode métier)
        """
        assert rate > 0, "le taux d'échange doit être positif"
        assert to_currency != self._pivot_currency, "Le to_currency doit être différent du pivot_currency"
        assert to_currency not in self._exchange_rate.keys(), "Le taux d'échange existe déjà"
        self._exchange_rate[to_currency] = rate

    def xǁBankǁadd_exchange_rate__mutmut_5(self, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange (méthode métier)
        """
        assert rate > 0, "LE TAUX D'ÉCHANGE DOIT ÊTRE POSITIF"
        assert to_currency != self._pivot_currency, "Le to_currency doit être différent du pivot_currency"
        assert to_currency not in self._exchange_rate.keys(), "Le taux d'échange existe déjà"
        self._exchange_rate[to_currency] = rate

    def xǁBankǁadd_exchange_rate__mutmut_6(self, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange (méthode métier)
        """
        assert rate > 0, "Le taux d'échange doit être positif"
        assert to_currency == self._pivot_currency, "Le to_currency doit être différent du pivot_currency"
        assert to_currency not in self._exchange_rate.keys(), "Le taux d'échange existe déjà"
        self._exchange_rate[to_currency] = rate

    def xǁBankǁadd_exchange_rate__mutmut_7(self, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange (méthode métier)
        """
        assert rate > 0, "Le taux d'échange doit être positif"
        assert to_currency != self._pivot_currency, "XXLe to_currency doit être différent du pivot_currencyXX"
        assert to_currency not in self._exchange_rate.keys(), "Le taux d'échange existe déjà"
        self._exchange_rate[to_currency] = rate

    def xǁBankǁadd_exchange_rate__mutmut_8(self, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange (méthode métier)
        """
        assert rate > 0, "Le taux d'échange doit être positif"
        assert to_currency != self._pivot_currency, "le to_currency doit être différent du pivot_currency"
        assert to_currency not in self._exchange_rate.keys(), "Le taux d'échange existe déjà"
        self._exchange_rate[to_currency] = rate

    def xǁBankǁadd_exchange_rate__mutmut_9(self, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange (méthode métier)
        """
        assert rate > 0, "Le taux d'échange doit être positif"
        assert to_currency != self._pivot_currency, "LE TO_CURRENCY DOIT ÊTRE DIFFÉRENT DU PIVOT_CURRENCY"
        assert to_currency not in self._exchange_rate.keys(), "Le taux d'échange existe déjà"
        self._exchange_rate[to_currency] = rate

    def xǁBankǁadd_exchange_rate__mutmut_10(self, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange (méthode métier)
        """
        assert rate > 0, "Le taux d'échange doit être positif"
        assert to_currency != self._pivot_currency, "Le to_currency doit être différent du pivot_currency"
        assert to_currency in self._exchange_rate.keys(), "Le taux d'échange existe déjà"
        self._exchange_rate[to_currency] = rate

    def xǁBankǁadd_exchange_rate__mutmut_11(self, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange (méthode métier)
        """
        assert rate > 0, "Le taux d'échange doit être positif"
        assert to_currency != self._pivot_currency, "Le to_currency doit être différent du pivot_currency"
        assert to_currency not in self._exchange_rate.keys(), "XXLe taux d'échange existe déjàXX"
        self._exchange_rate[to_currency] = rate

    def xǁBankǁadd_exchange_rate__mutmut_12(self, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange (méthode métier)
        """
        assert rate > 0, "Le taux d'échange doit être positif"
        assert to_currency != self._pivot_currency, "Le to_currency doit être différent du pivot_currency"
        assert to_currency not in self._exchange_rate.keys(), "le taux d'échange existe déjà"
        self._exchange_rate[to_currency] = rate

    def xǁBankǁadd_exchange_rate__mutmut_13(self, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange (méthode métier)
        """
        assert rate > 0, "Le taux d'échange doit être positif"
        assert to_currency != self._pivot_currency, "Le to_currency doit être différent du pivot_currency"
        assert to_currency not in self._exchange_rate.keys(), "LE TAUX D'ÉCHANGE EXISTE DÉJÀ"
        self._exchange_rate[to_currency] = rate

    def xǁBankǁadd_exchange_rate__mutmut_14(self, to_currency: Currency, rate: float) -> None:
        """
        Ajouter un taux d'échange (méthode métier)
        """
        assert rate > 0, "Le taux d'échange doit être positif"
        assert to_currency != self._pivot_currency, "Le to_currency doit être différent du pivot_currency"
        assert to_currency not in self._exchange_rate.keys(), "Le taux d'échange existe déjà"
        self._exchange_rate[to_currency] = None
    
    xǁBankǁadd_exchange_rate__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁBankǁadd_exchange_rate__mutmut_1': xǁBankǁadd_exchange_rate__mutmut_1, 
        'xǁBankǁadd_exchange_rate__mutmut_2': xǁBankǁadd_exchange_rate__mutmut_2, 
        'xǁBankǁadd_exchange_rate__mutmut_3': xǁBankǁadd_exchange_rate__mutmut_3, 
        'xǁBankǁadd_exchange_rate__mutmut_4': xǁBankǁadd_exchange_rate__mutmut_4, 
        'xǁBankǁadd_exchange_rate__mutmut_5': xǁBankǁadd_exchange_rate__mutmut_5, 
        'xǁBankǁadd_exchange_rate__mutmut_6': xǁBankǁadd_exchange_rate__mutmut_6, 
        'xǁBankǁadd_exchange_rate__mutmut_7': xǁBankǁadd_exchange_rate__mutmut_7, 
        'xǁBankǁadd_exchange_rate__mutmut_8': xǁBankǁadd_exchange_rate__mutmut_8, 
        'xǁBankǁadd_exchange_rate__mutmut_9': xǁBankǁadd_exchange_rate__mutmut_9, 
        'xǁBankǁadd_exchange_rate__mutmut_10': xǁBankǁadd_exchange_rate__mutmut_10, 
        'xǁBankǁadd_exchange_rate__mutmut_11': xǁBankǁadd_exchange_rate__mutmut_11, 
        'xǁBankǁadd_exchange_rate__mutmut_12': xǁBankǁadd_exchange_rate__mutmut_12, 
        'xǁBankǁadd_exchange_rate__mutmut_13': xǁBankǁadd_exchange_rate__mutmut_13, 
        'xǁBankǁadd_exchange_rate__mutmut_14': xǁBankǁadd_exchange_rate__mutmut_14
    }
    xǁBankǁadd_exchange_rate__mutmut_orig.__name__ = 'xǁBankǁadd_exchange_rate'

    def remove_exchange_rate(self, to_currency: Currency) -> None:
        """
        Supprimer un taux d'échange (méthode métier)
        """
        del self._exchange_rate[to_currency]

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
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_1(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency != to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_2(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(None, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_3(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, None)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_4(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_5(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, )
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_6(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency not in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_7(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = None

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_8(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(None, 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_9(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], None)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_10(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_11(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], )

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_12(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_13(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 3)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_14(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency or money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_15(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency != self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_16(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency not in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_17(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = None

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_18(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(None, 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_19(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], None)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_20(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_21(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], )

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_22(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_23(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 3)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_24(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(None, to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_25(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, None)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_26(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(to_currency)

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_27(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, )

        return Money(converted_amount, to_currency)

    def xǁBankǁconvert__mutmut_28(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(None, to_currency)

    def xǁBankǁconvert__mutmut_29(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(converted_amount, None)

    def xǁBankǁconvert__mutmut_30(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

        return Money(to_currency)

    def xǁBankǁconvert__mutmut_31(self, money: Money, to_currency: Currency) -> Money:
        """
        Convertir un objet Money dans une autre monnaie
        """
        if money.currency == to_currency:
            return Money(money.amount, to_currency)
        
        if to_currency in self._exchange_rate.keys():
            converted_amount = round(money.amount * self._exchange_rate[to_currency], 2)

        elif to_currency == self._pivot_currency and money.currency in self._exchange_rate.keys():
            converted_amount = round(money.amount / self._exchange_rate[money.currency], 2)

        else:
            raise MissingExchangeRateError(money.currency, to_currency)

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
        'xǁBankǁconvert__mutmut_16': xǁBankǁconvert__mutmut_16, 
        'xǁBankǁconvert__mutmut_17': xǁBankǁconvert__mutmut_17, 
        'xǁBankǁconvert__mutmut_18': xǁBankǁconvert__mutmut_18, 
        'xǁBankǁconvert__mutmut_19': xǁBankǁconvert__mutmut_19, 
        'xǁBankǁconvert__mutmut_20': xǁBankǁconvert__mutmut_20, 
        'xǁBankǁconvert__mutmut_21': xǁBankǁconvert__mutmut_21, 
        'xǁBankǁconvert__mutmut_22': xǁBankǁconvert__mutmut_22, 
        'xǁBankǁconvert__mutmut_23': xǁBankǁconvert__mutmut_23, 
        'xǁBankǁconvert__mutmut_24': xǁBankǁconvert__mutmut_24, 
        'xǁBankǁconvert__mutmut_25': xǁBankǁconvert__mutmut_25, 
        'xǁBankǁconvert__mutmut_26': xǁBankǁconvert__mutmut_26, 
        'xǁBankǁconvert__mutmut_27': xǁBankǁconvert__mutmut_27, 
        'xǁBankǁconvert__mutmut_28': xǁBankǁconvert__mutmut_28, 
        'xǁBankǁconvert__mutmut_29': xǁBankǁconvert__mutmut_29, 
        'xǁBankǁconvert__mutmut_30': xǁBankǁconvert__mutmut_30, 
        'xǁBankǁconvert__mutmut_31': xǁBankǁconvert__mutmut_31
    }
    xǁBankǁconvert__mutmut_orig.__name__ = 'xǁBankǁconvert'
