import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            self.calc.divide(1, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(2, 0), 1)

    def test_square_root(self):
        self.assertEqual(self.calc.square_root(4), 2)
        self.assertEqual(self.calc.square_root(0), 0)
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)

if __name__ == '__main__':
    unittest.main()