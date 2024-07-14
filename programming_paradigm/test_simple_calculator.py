import unittest
from simple_calculator import SimpleCalculator
class SimpleCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -2), -7)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test the addition method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        self.assertEqual(self.calc.subtract(-5, -4), -1)
        self.assertEqual(self.calc.subtract(6, -2), 8)
        self.assertEqual(self.calc.subtract(7, 0), 7)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(5, 4), 20)
        self.assertEqual(self.calc.multiply(-3, 2), -6)
        self.assertEqual(self.calc.multiply(-7, -2), 14)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(4, -10), -40)

        def test_division(self):
            """Test the multiplication method."""
            self.assertEqual(self.calc.divide(9, 3), 3)
            self.assertEqual(self.calc.divide(-10, 2), -5)
            self.assertEqual(self.calc.divide(-9, -3), 3)
            self.assertEqual(self.calc.divide(20, -4), -5)
            with self.assertRaises(ValueError):
                test_division(10, 0)
if __name__ == "__main__":
    unittest.main()
