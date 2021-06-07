import my_exceptions as ex


class Product:
    """ Class represents the product with unique number, price and name
   
    """
    def __init__(self, number, price, name):
        """Constructor creates new product with specific number, price and name 

            Parameters
            ----------
            number: int
                    number of product
            price: float
                    price of product
            name: str
                    name of product
        """
        self.__name = name
        self.__number = number
        self.__price = price


    def return_product_name(self):
        """Method returns product name """
        return self.__name

    def return_product_number(self):
        """Method returns product number """
        return self.__number
    def return_product_price(self):
        """Method uses _remove_product to decrement amount of specific product in vending machine and returns price of this product """
        return self.__price


