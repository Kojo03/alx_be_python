import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Addition tests
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_mixed_signs(self):
        self.assertEqual(self.calc.add(-2, 3), 1)
        self.assertEqual(self.calc.add(2, -3), -1)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)

    # Subtraction tests
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtraction_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtraction_mixed_signs(self):
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(5, -3), 8)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # Multiplication tests
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-4, -5), 20)

    def test_multiplication_mixed_signs(self):
        self.assertEqual(self.calc.multiply(-4, 5), -20)
        self.assertEqual(self.calc.multiply(4, -5), -20)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)

    # Division tests
    def test_division_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_division_mixed_signs(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)

    def test_division_with_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))

if __name__ == '__main__':
    unittest.main()

