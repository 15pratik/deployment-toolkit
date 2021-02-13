import unittest
import math
from calculator.calc import CalcOperations


class MyTestCase(unittest.TestCase):
    def test_sq_root(self):
        self.assertEqual(CalcOperations.sqrt(10), math.sqrt(10))

    def test_sq_root_invalid(self):
        with self.assertRaises(Exception):
            CalcOperations.sqrt(-1)

    def test_factorial(self):
        self.assertEqual(CalcOperations.fact(10), math.factorial(10))

    def test_power(self):
        self.assertEqual(CalcOperations.pow(10, 2), math.pow(10, 2))


if __name__ == '__main__':
    unittest.main()
