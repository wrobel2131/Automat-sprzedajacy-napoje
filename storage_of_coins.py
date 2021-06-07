import my_exceptions as ex
from coin import Coin
from decimal import *
import copy
class Storage_of_Coins:
    """ This class stores all coins in vending machine, is responsible of adding and
        removing coins.
    """
    def __init__(self, amount):
        """ Constructs list of all coins. Constructor adds  coins of each value in
            [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1,2,5] list. At the end, list is sorted
            by key=Coin.get_value
            
            Parameters
            ----------
            amount: int,
                    amount of coins, that storage stores
            """
        self._list_of_all_coins = []
        self._amount = amount

        
        if self._amount > 0:
            ##CREATES LIST OF COINS IN COINS STORAGE
            self._list_of_all_coins = [Coin(j, "PLN") for j in [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1,2,5] for i in range(self._amount)]
            self._list_of_all_coins.sort(key=Coin.get_value, reverse=True)
        
    def add_coin(self, coin):
        """ Checks, if object coin is instance of Coin class. If true, coin is added to list.
            

            Parameters
            ----------
                coin: object which is supposed to be added to list

            Raises
            ------
            ObjectIsNotCoinException: if object coin is not instance of Coin, exception is raised
            """
        if isinstance(coin, Coin):
            self._list_of_all_coins.append(coin)
        else:
            raise ex.ObjectIsNotCoinException

    def return_all_coins(self):
        """Returns all coins from storage and clears list """
        tmp_list = copy.deepcopy(self._list_of_all_coins) 
        self._list_of_all_coins.clear()
        return tmp_list
        
    def return_coin(self, val):
        """Returns coin of given value and removes this coin from list of all coins. 

            Parameters
            ----------
                val: value of coin, which is supposed to be returned

            Raises
            ------
             NoCoinsWithThisValueException: If there is no coin with given value in the storage, exception is raised
            """
        for i in self._list_of_all_coins:
            if i.get_value() == val:
                tmp = copy.deepcopy(i)
                self._list_of_all_coins.remove(i)
                return tmp
            else:
                pass
        raise ex.NoCoinsWithThisValueException
           
    def sum_of_all_coins_values(self):
        """ Sums all values of coins in list of all coins and returns the sum """
        sum_of_coins = Decimal("0")
        for coin in self._list_of_all_coins:
            sum_of_coins = sum_of_coins + coin.get_value()
        return sum_of_coins

    def show_all_coins(self):
        """ Shows all values of coins in list. If list is empty, methods returns:
                Storage is empty """ 
        if not self._list_of_all_coins:
            print("Storage is empty")
        else:
            it = 0
            for i in [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1,2,5]:
                for j in self._list_of_all_coins:
                    if Decimal(str(i)) == j.get_value():
                        it+=1
                print("{} x {}".format(it, i))
                it = 0

