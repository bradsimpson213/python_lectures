import unittest
from code import add


class TestAddFunction(unittest.TestCase):
    def test_addition(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = add(12, -6)
        self.assertEqual(result, 6)