from decimal import *
import my_exceptions as ex


class Coin:
    """ This class represents single coin in PLN
     """
    def __init__(self, value, currency):
        """ Constructs single coin with given value and currency

            Parameters
            ----------
            value: float, int
                    value of coin
            currency: str
                    currency of coin

            Raises
            ------
            WrongValueOfCoinException: If the value is not in [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5], exception is raised, and value is set to Decimal("0")
            WrongCurrencyOfCoin: If the currency is not PLN, exception is raised and currency is set to Unknown

        """

        ##CHECKS IF VALUE IS IN LIST OF VALUES
        if value in [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]:
            self.__value = Decimal(str(value))
        else:
            self.__value = Decimal("0")
            raise ex.WrongValueOfCoinException
        ##CHECKS IF CURRENCY IS CORRECT
        if currency == "PLN":
            self.__currency = "PLN"
        else:
            self.__currency = "Unknown"
            raise ex.WrongCurrencyOfCoin

    def get_value(self):
        """ Returns coin value"""
        return self.__value
    
    def get_currency(self):
        """ Returns coin currency"""
        return self.__currency

