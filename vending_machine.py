from storage_of_coins import Storage_of_Coins
from storage_of_products import Storage_of_Products
from coin import Coin
from decimal import *
import my_exceptions as ex
import copy

class Vending_Machine:
    """The class represents vending machine and has all the functionality of the program.
    
     """

    def __init__(self, num = 5):
        """Creates object of Vending_Machine
        
            Parameters
            ----------
            num: int
                default set to 5, amount of products in vending machine
            """

        self._product_storage = Storage_of_Products(num)
        self._coins_storage = Storage_of_Coins(10)
        self._customer_coins = Storage_of_Coins(0)
        self._product_number = 0
        self._rest = Decimal("0")

    def set_product_number(self, num):
        """Sets product number to given value. If the value is not 0, rest is also set. 0 means that purchase was ended and product number was must be set to 0 
        
            Parameters
            ----------
            num: int
                product number
        """
        self._product_number = num
        if num != 0:
            self.set_rest(-self.return_product_price(num))

    def set_rest(self, num):
        """Sets rest to given value 
        
            Parameters
            ----------
            num: float
                rest
        """
        self._rest = Decimal("{:.2f}".format(num))

    def return_rest(self):
        """Returns rest """
        return self._rest

    def check_product_number(self, num):
        """Checks if given product number is correct or not. If so, it returns True, otherwise it returns False
        
            Parameters
            ----------
            num: int
                product number
         """
        if(num < 30 or num > 50 ):
            return False
        else:
            return True

    def return_product_price(self, num):
        """Returns price of product with given number
        
            Parameters
            ----------
            num: int
                product number
         """
        return self._product_storage.return_product_with_number(num).return_product_price()

    def add_coin_to_machine(self, val):
        """Adds coin with given value to customer storage of coins and main storage of coins. It also reduce amount to pay by given value of coin
        
            Parameters
            ----------
            val: float, int
                value of coin
         """
        self._customer_coins.add_coin(Coin(val, "PLN"))
        self._coins_storage.add_coin(Coin(val, "PLN"))
        self.set_rest(self._rest+Decimal("{:.2f}".format(val)))

    def buy(self):
        """The method responsible for entire payment. Checks the rest an on this basisc, returns appropriate "status of payment" number and text
            It returns -1 and text, when amount paid by user is too low.
            It returns rest value, if purchase was successful.

            Excepts
            ------
            NoSpecificProductsLeftException: If there is lack of products with given number, this method returns -2 and  adequate text

            NoRestInVendingMachineException: If machine can't return rest bacause of lack of coins, method returns -3 and adequate text



          """
        ##CALCULATES REST
        rest_list, rest_amount = self.calculate_rest()

        if rest_amount < Decimal("0"):
            text1 = "Zaplaciles za malo"
            return -1, text1
        else:
            try:
                prod1 = self._product_storage.return_product_with_number_to_customer(self._product_number)
                
                ##CONSTRUCTS TEXT TO RETURN
                txt = ""
                it = 0
                for i in rest_list:
                    txt += str(i.get_value())
                    txt+=", "
                    it+=1
                    if it == 10:
                        txt+="\n"
                        it=0
                text1 = "Dziekujemy za zakup\nTwoj zakup:\n {}\t{}\nTwoja reszta:\n{}".format(prod1.return_product_name(), prod1.return_product_price() ,txt)

                ##SETS REST AND PRODUCT NUMBER TO 0
                self.set_rest(0)
                self.set_product_number(0)

                ##REMOVES ALL COINS FROM CUSTOMER COINS SOTRAGE
                self._customer_coins.return_all_coins()

                return rest_amount, text1

            except ex.NoSpecificProductsLeftException:
                text1 = "Obecnie nie ma tego produktu w automacie\n"
                text2 = "Zwracam Twoje monety: \n"
                ##REMOVES ALL COINS FROM CUSTOMER COINS SOTRAGE AND RETURNS THEM
                coins_list = self._customer_coins.return_all_coins()

                ##REMOVES CUSTOMER COINS FROM MAIN STORAGE OF COINS
                self.remove_customer_coins_from_main_storage(coins_list)

                ##SETS REST AND PRODUCT NUMBER TO 0
                self.set_rest(0)
                self.set_product_number(0)
                
                ##CONSTRUCTS TEXT TO RETURN
                it = 0
                for i in coins_list:
                    
                    text2 += str(i.get_value())
                    text2+=", "
                    it+=1
                    if it == 10:
                        text2+="\n"
                        it=0
                    
                text1 = text1+text2
                return -2, text1

            except ex.NoRestInVendingMachineException:
                text1 = "Brak reszty. Wybierz produkt jeszcze raz i zaplac odliczona kwota\nZwracam Twoje monety: \n"

                 ##REMOVES ALL COINS FROM CUSTOMER COINS SOTRAGE AND RETURNS THEM
                coins_list = self._customer_coins.return_all_coins()

                ##REMOVES CUSTOMER COINS FROM MAIN STORAGE OF COINS
                self.remove_customer_coins_from_main_storage(coins_list)

                ##SETS REST AND PRODUCT NUMBER TO 0
                self.set_rest(0)
                self.set_product_number(0)
                
                ##CONSTRUCTS TEXT TO RETURN
                it = 0
                for i in coins_list:
                    text1 += str(i.get_value())
                    text1+=", "
                    it+=1
                    if it == 10:
                        text1+="\n"
                        it=0  
                return -3, text1

    def remove_customer_coins_from_main_storage(self, cust_coins):
        """Removes coins given by cust_coins from main storage of coins 
        
            Parameters
            ----------
            cust_coins: list of customer coins to remove 
        """
        for i in cust_coins:
            tmp_val = i.get_value()
            self._coins_storage.return_coin(tmp_val)


    def calculate_rest(self):
        """Method responsible for calculating the remaining amount to pay and calculating the rest
        
            Excepts
            -------
            NoCoinsWithThisValueException: if there is no coins with given value in main storage of coins, method checks, if there is no coins left. If so, NoRestInVendingMachineException
                                            is raised. Otherwise continues finding coins fitting the rest
            
            Raises
            ------
            ex.NoRestInVendingMachineException: Raised, when there is no coins left in main storage, or rest can't be returned.
         """
        tmp_rest = self.return_rest()
        

        ##CHECKS IF EXACT AMOUNT WAS PAID
        if tmp_rest == Decimal("0"):
            return [],tmp_rest

        ##CHECKS IF AMOUNT PAIN BY USER WAS TOO LOW
        elif tmp_rest < Decimal("0"):
            return [], tmp_rest

        else:
            rest_to_return = []

            ##COPIES COINS FROM MAIN STORAGE OF COINS
            tmp_list_coins = copy.deepcopy(self._coins_storage._list_of_all_coins)

            tmp2_rest = tmp_rest

            
            while tmp2_rest > Decimal("0"):
                for i in tmp_list_coins:
                    tmp_val = i.get_value()
                    if tmp2_rest >= tmp_val:
                        try:
                            rest_to_return.append(self._coins_storage.return_coin(tmp_val))
                        except ex.NoCoinsWithThisValueException:
                            if self._coins_storage.sum_of_all_coins_values() == Decimal("0"):
                                raise ex.NoRestInVendingMachineException
                            else:
                                continue
                        tmp2_rest -= tmp_val
                        break
            if tmp2_rest == Decimal("0"):
                self.set_rest(0)
                return rest_to_return, tmp_rest
            else:
                raise ex.NoRestInVendingMachineException
        
    def resign(self):
        """Responsible for removing and returning all coins from customer storage of coins. Returns list of customer coins and text"""
        text1 = "Zrezygnowales z platnosci\nZwracam Twoje monety: \n"
        coins_list = self._customer_coins.return_all_coins()
        it = 0
        for i in coins_list:
            text1 += str(i.get_value())
            text1+=", "
            it+=1
            if it == 10:
                text1+="\n"
                it=0
        return coins_list, text1
