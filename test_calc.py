from unittest import TestCase
from calculator import Calculator
import unittest


class CalcTest(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add1(self):
        self.assertEqual(4, self.calc.add(2, 2))

    def test_add2(self):
        self.assertEqual(-0.5, self.calc.add(-2.5, 2))

    def test_subtract1(self):
        self.assertEqual(-1, self.calc.subtract(2, 3))

    def test_subtract2(self):
        self.assertEqual(5, self.calc.subtract(2, -3))

    def test_multiply1(self):
        self.assertEqual(5, self.calc.multiply(1, 5))

    def test_multiply2(self):
        self.assertEqual(0, self.calc.multiply(1, 0))

    def test_divide(self):
        self.assertEqual(float(12 / 8), self.calc.divide(12, 8))

    def test_evaluate1(self):
        self.assertEqual(6, self.calc.evaluate("2+2*2"))

    def test_evaluate2(self):
        self.assertEqual(8, self.calc.evaluate("(2+2)*2"))

    def test_division_by_zero(self):
        self.assertRaises(ZeroDivisionError, lambda: self.calc.divide(1, 0))

    def test_evaluate_error(self):
        self.assertRaises(SyntaxError, lambda: self.calc.evaluate(")2+2(*2"))


if __name__ == '__main__':
    unittest.main()
