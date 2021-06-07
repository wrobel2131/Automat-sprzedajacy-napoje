import unittest
from vending_machine import Vending_Machine
from decimal import *

class Tests(unittest.TestCase):
    def Product_Price_Check_Test(self):
        """Checks if the function responsible for the return of price of the product with given number is working properly """
        #given
        vend = Vending_Machine(1)
        product_number = 35
        price = 6.39
        #when
        product_price = vend.return_product_price(product_number)
        #then
        self.assertEqual(product_price, price)

    def No_Rest_Returned_when_Exact_Amount_Entered_Test(self):
        """Checks the case when the exact amount is paid. In this case, the rest should be 0"""
        #given
        vend = Vending_Machine(1)
        product_number = 35
        #price = 6.39
        vend.set_product_number(product_number)
        vend.add_coin_to_machine(5)
        vend.add_coin_to_machine(1)
        vend.add_coin_to_machine(0.20)
        vend.add_coin_to_machine(0.10)
        vend.add_coin_to_machine(0.05)
        vend.add_coin_to_machine(0.02)
        vend.add_coin_to_machine(0.02)
        
        #when
        rest, _ = vend.buy()
        #then
        self.assertEqual(rest, Decimal("0"))
        
    def Correct_Rest_Returned_when_Bigger_Amount_Entered_Test(self):
        """Checks the case when the bigger amount is paid. In this case, the rest should be returned and equal (sum of coins values given bu user) - (product price)"""
        #given
        vend = Vending_Machine(1)
        product_number = 35
        price = 6.39
        vend.set_product_number(product_number)
        vend.add_coin_to_machine(5)
        vend.add_coin_to_machine(2)

        #when
        rest, _ = vend.buy()

        #then
        self.assertEqual(rest, Decimal("7")-Decimal("{}".format(price)))

    def No_Products_Left_Test(self):
        """Checks if there is product with given number. If not, should return False """
        #given
        vend = Vending_Machine(0)
        product_number = 33
        #product_price = 2.49
        vend.set_product_number(product_number)
        vend.add_coin_to_machine(5)

        #when
        rest, _ = vend.buy()
        #then
        self.assertEqual(rest, -2)

    def Product_Price_Check_when_Product_Number_Incorrect_should_Return_False_Test(self):
        """Checks, if there is a product with given number(incorrect number). Should return False, when there is not products with such a number """
        #given
        vend = Vending_Machine(1)
        product_number = 60

        #when
        check = vend.check_product_number(product_number)
        #then
        self.assertFalse(check)
        
    def Correct_Rest_Returned_when_Resign_Pay_Test(self):
        """Checks, if the rest is returned in the case, when user cancel the payment. The rest should be equal to coins entered by user """
        #given
        vend = Vending_Machine(1)
        product_number = 33
        #product_price = 2.49
        vend.set_product_number(product_number)
        vend.add_coin_to_machine(1)
        vend.add_coin_to_machine(0.01)
        vend.add_coin_to_machine(0.5)
        value_set = {Decimal("1"),Decimal("0.01"), Decimal("0.5")}
        
        #when
        returned_coins, _ = vend.resign()
    
        new_value_set= {i.get_value() for i in returned_coins}
            
        #then
        self.assertEqual(value_set, new_value_set)

    def No_Rest_Returned_when_First_Amount_Too_Low_But_Whole_Amount_Correct_Test(self):
        """Checks the case, when user tries first to pay with too small amount for a product and then adds the amount to exact price of the product and pays. Rest returned should equal 0 """
        #given
        vend = Vending_Machine(1)
        product_number = 32
        #product_price = 5.99
        vend.set_product_number(product_number)
        vend.add_coin_to_machine(1)
        vend.add_coin_to_machine(0.2)
        vend.add_coin_to_machine(0.1)
        
        #when
        check1, _ = vend.buy()
        self.assertEqual(check1, -1)
        vend.add_coin_to_machine(2)
        vend.add_coin_to_machine(2)
        vend.add_coin_to_machine(0.5)
        vend.add_coin_to_machine(0.1)
        vend.add_coin_to_machine(0.05)
        vend.add_coin_to_machine(0.02)
        vend.add_coin_to_machine(0.02)
        check2, _ = vend.buy()

        #then
        self.assertEqual(check2, Decimal("0"))
    def Correct_Purchase_With_100_Coins_Test(self):
        """Checks whether if we pay with 0.01 coins we will but a 1.0 value product. Rest returned for this buy should equal 0 """
        #given
        vend = Vending_Machine(1)
        product_number = 50
        #product_price = 1.00
        vend.set_product_number(product_number)
        for i in range(100):
            vend.add_coin_to_machine(0.01)

        #when
    
        rest, _ = vend.buy()

        #then
        self.assertEqual(rest, Decimal("0"))
    

if __name__ == '__main__':
    unittest.main()