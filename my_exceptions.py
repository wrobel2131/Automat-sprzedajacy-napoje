
class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class WrongValueOfCoinException(Error):
    """ Exception raised if the value of the coin is valid
    Attributes
    ----------
        value: coins value
        message: explanation of the error
    """
    def __init__(self, message="Value of coin not in list: [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]"):

        self.message = message;
        super().__init__(self.message)

    def __str__(self):
        return "{}".format(self.message)
    

class WrongCurrencyOfCoin(Error):
    """ Exception raised if the currency of the coin is valid
    Attributes
    ----------
        value: coins currency
        message: explanation of the error
    """
    def __init__(self,message = "Currency of coin is not PLN"):
        
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "{}".format(self.message)

class ObjectIsNotCoinException(Error):
    """ Exception raised if passed object is not instance of Coin class
    Attributes
    ----------
        value: passed object
        message: explanation of the error
    """
    def __init__(self, message = "Object is not instance of Coin class."):
        
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "{}".format(self.message)

class NoCoinsWithThisValueException(Error):
    """ Exception raised if there is no more coins with given value
    Attributes
    ----------
        value: coins value
        message: explanation of the error
    """
    def __init__(self):
        
        self.message = "Coin with this value is not available now"
        super().__init__(self.message)

    def __str__(self):
        return "{}".format(self.message)

class NoSpecificProductsLeftException(Error):
    """ Exception raised if there is no more products with given number
    Attributes
    ----------
        value: products number
        message: explanation of the error
    """
    def __init__(self):
        
        self.message = "Product with given number is no longer available."
        super().__init__(self.message)

    def __str__(self):
        return "{}".format(self.message)


class NoRestInVendingMachineException(Error):
    """ Exception raised if there is no rest to return to user
    Attributes
    ----------
        
        message: explanation of the error
    """
    def __init__(self, message="No rest. Select the product again and pay the deducted amount"):
        self.message = message;
        super().__init__(self.message)

    def __str__(self):
        return "{}".format(self.message)