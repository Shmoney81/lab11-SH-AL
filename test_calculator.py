# https://github.com/Shmoney81/lab11-SH-AL.git
# Partner 1: Stephen Horvat
# Partner 2: Aiden Lehrhaupt

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(3,4), 7)
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(12,13),25)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5,2), 3)
        self.assertEqual(subtract(-3,-5), 2)
        self.assertEqual(subtract(2,2), 0)

    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-1, 6), -6)
        self.assertEqual(mul(5, 0), 0)
    def test_divide(self): # 3 assertions
        self.assertEqual(div(5, 0), 0)
        self.assertEqual(div(5, -1), -0.2)
        self.assertEqual(div(-2, 4), -2)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(4,1024),5)
        self.assertEqual(logarithm(10,100), 2)
        self.assertEqual(logarithm(2,8), 3)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(1, 5)
        with self.assertRaises(ValueError):
            logarithm(-5, 5)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(8, 0)
        with self.assertRaises(ValueError):
            logarithm(4, -4)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(0, 5), 5)
        self.assertEqual(hypotenuse(-3, -4), 5)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()