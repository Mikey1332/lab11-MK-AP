#https://github.com/Mikey1332/lab11-MK-AP.git
# Partner 1: Michael Kroner
# Partner 2: Alexandra Pippio

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        #Tests if function is correct
        self.assertAlmostEqual(add(2, 4), 6)
        #Tests if negative numbers work
        self.assertAlmostEqual(add(-4, -9), -13)
        #Tests if non-integers work
        self.assertAlmostEqual(add(2, 5.5), 7.5)


    def test_subtract(self): # 3 assertions
        #Tests if function is correct
        self.assertAlmostEqual(subtract(7, 3), 4)
        #Tests if negative numbers work
        self.assertAlmostEqual(subtract(-7, 3), -10)
        #Tests if non-integers work
        self.assertAlmostEqual(subtract(5, 2.3), 2.7)

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        #Tests if function is correct
        self.assertAlmostEqual(mul(5, 8), 40)
        #Tests if negative numbers work
        self.assertAlmostEqual(mul(3, -4), -12)
        # Tests if non-integers work
        self.assertAlmostEqual(mul(3, 0.5), 1.5)

    def test_divide(self): # 3 assertions
        # Tests if function is correct
        self.assertAlmostEqual(div(8, 40), 5)
        # Tests if negative numbers work
        self.assertAlmostEqual(div(-4, 16), -4)
        # Tests if non-integers work for a and b
        self.assertAlmostEqual(div(1.3, 16.9), 13)
        # Tests if non-integers work for answer
        self.assertAlmostEqual(div(2, 7), 3.5)
        # Tests error if divided by zero
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        #Tests if function is correct
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(2, 3,), 1.58496250072)


    def test_log_invalid_base(self): # 1 assertion
        # a <= 1
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    ###########################
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:

        # b is <= 0
        with self.assertRaises(ValueError):
            logarithm(2, -4)


    def test_hypotenuse(self): # 3 assertions
        # Tests negative numbers and if function works
        self.assertAlmostEqual(hypotenuse(3, -4), 5)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # a is negative
        with self.assertRaises(ValueError):
           square_root(-4)
        # Test basic function
        self.assertAlmostEqual(square_root(16), 4)
    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()