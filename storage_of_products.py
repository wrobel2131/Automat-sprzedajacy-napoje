from product import Product
import my_exceptions as ex

class Storage_of_Products:
    """ This class represents storage of all products. Products are in list
        and have unique number, price and amount.
        """
    def __init__(self, amount):
        """ Constructs storage of products with numbers 30-50 and prices
        Parameters
        ----------
            amount: amount of specific product"""
        self._amount = amount
        self._list_of_products = [Product(30, 2.99,"7 UP"), Product(31, 2.99,"Coca Cola"), Product(32, 5.99,"Dzik Energy"),
                                    Product(33, 2.49,"Mirinda"), Product(34, 6.39,"Monster Red"), Product(35, 6.39,"Monster Classic"),
                                    Product(36, 7.25,"Monster Mango"), Product(37, 5.33,"Monster Orange Juice"), Product(38, 2.11,"Monster Pink"),
                                    Product(39, 4.99,"Monster Gold"), Product(40, 6.89,"Monster Zero BubbleGum"), Product(41, 4.76,"Monster Zero Mango"),
                                    Product(42, 5.55,"Pepsi"), Product(43, 3.29,"Warka Radler Citruit"), Product(44, 4.36,"Warka 3 Cytryny"),
                                    Product(45, 11.33,"Okocim Orange"), Product(46, 9.12,"Redbull"), Product(47, 1.55,"Aloe"),
                                    Product(48, 3.22,"Bio Juice"), Product(49, 2.99,"Sprite"), Product(50, 1.00,"Water")]

        ##CREATES DICTIONARY WITH PRODUCTS AND THEIR AMOUNTS
        self._dict_of_products = {key: self._amount for key in self._list_of_products}

    def show_all_products(self):
        """ Shows all products: their number and price"""
        for k, v in self._dict_of_products.items():
            print("No. {}\tName: {}\t Price: {}\t Amount: {} ".format(k.return_product_number(),k.return_product_name(), k.return_product_price(), v))
    

    def return_product_with_number(self, num):
        """Returns product with given number without removing it from storage
        
            Parameters
            ----------
            num: int
                number of product
         """
        for i in self._dict_of_products.keys():
            if i.return_product_number() == num:
                return i

    def return_product_with_number_to_customer(self, num):
        """Returns product with given number and decrements its amount in dictionary
        
            Parameters
            ----------
            num: int
                number of product
         """
        for i in self._dict_of_products.keys():
            if i.return_product_number() == num:
                self.__remove_product(num)
                return i

    def __remove_product(self, num):
        """Decrements product number in dictionary of products 

            Parameters
            ----------
            num: int
                number of product

            Raises
            ------
            NoSpecificProductsLeftException: If there is no products left with given number, exception is raised
        """ 

        for k, v in self._dict_of_products.items():
            if k.return_product_number() == num:
                if v > 0:
                    self._dict_of_products[k]-=1
                else:
                    raise ex.NoSpecificProductsLeftException
           
