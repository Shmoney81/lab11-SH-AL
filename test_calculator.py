import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(3,4), 7)
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(12,13),25)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5,2), 3)
        self.assertEqual(sub(-3,-5), 2)
        self.assertEqual(sub(2,2), 0)

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
        self.assertEqual(log(4,1024),5)
        self.assertEqual(log(10,100), 2)
        self.assertEqual(log(2,8), 3)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(8, 0)
            log(0, 0)
            log(4, -2)

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()