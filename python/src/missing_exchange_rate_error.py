from .currency import Currency


class MissingExchangeRateError(Exception):
    """
    Message d'erreur pour la demande d'un échange de monnaies non proposé par la banque
    """
    def __init__(self, currency1: Currency, currency2: Currency) -> None:
        super().__init__(f'La banque ne propose pas cet échange : {currency1.value}->{currency2.value}')