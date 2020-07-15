from simple_calc import SimpleCalc
import unittest

class Calctests(unittest.TestCase):
    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.add(1, 1), 2)
        self.assertEqual(self.calc.add(-5, -2), -7)
        self.assertIsNotNone(self.calc.add(0, 0))

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5,2),3)
        self.assertEqual(self.calc.subtract(10,1),9)
        self.assertEqual(self.calc.subtract(-5,-2),-3)
        self.assertIsNotNone(self.calc.subtract(0,0))

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5,2),10)
        self.assertEqual(self.calc.multiply(-6,1),-6)
        self.assertEqual(self.calc.multiply(-5,-2),10)
        self.assertIsNotNone(self.calc.multiply(0,0))

    def test_divide(self):
        self.assertEqual(self.calc.divide(50,2),25)
        self.assertEqual(self.calc.divide(6,2),3)
        self.assertEqual(self.calc.divide(-5,1),-5)
        self.assertIsNotNone(self.calc.divide(0,1))